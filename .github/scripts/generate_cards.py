#!/usr/bin/env python3
"""Generate SVG profile cards for verified contributors."""

import base64
import calendar
import math
import os
import urllib.request
from datetime import date
import yaml

try:
    import cairosvg
    HAS_CAIROSVG = True
except ImportError:
    HAS_CAIROSVG = False

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(BASE_DIR, os.pardir, os.pardir))
LOGO_PATH = os.path.join(REPO_ROOT, 'Writing', 'FreeGym Logo.png')
CARD_SIZES = {
    'default': (1080, 1080),
    'wide': (1200, 630),
    'portrait': (1080, 1350),
    'story': (1080, 1920),
}

ACTIVE_WINDOW_DAYS = 60
USE_LOGO = os.getenv('USE_LOGO', '1').lower() not in ('0', 'false', 'no')


def get_png_size(path):
    """Return (width, height) for a PNG image."""
    with open(path, 'rb') as f:
        signature = f.read(8)
        if signature != b'\x89PNG\r\n\x1a\n':
            raise ValueError('Not a PNG file')
        f.seek(16)
        width = int.from_bytes(f.read(4), 'big')
        height = int.from_bytes(f.read(4), 'big')
    return width, height


def load_logo_data():
    """Return (uri, width, height) for the FreeGym logo image."""
    if not USE_LOGO or not os.path.exists(LOGO_PATH):
        return None, None, None
    width, height = get_png_size(LOGO_PATH)
    with open(LOGO_PATH, 'rb') as f:
        data = f.read()
    b64 = base64.b64encode(data).decode('utf-8')
    return f"data:image/png;base64,{b64}", width, height

# Cache for fetched avatars to avoid re-downloading for different card sizes
_avatar_cache = {}


def fetch_avatar_base64(github_username):
    """Fetch GitHub avatar and return as base64 data URI."""
    if github_username in _avatar_cache:
        return _avatar_cache[github_username]

    url = f"https://github.com/{github_username}.png?size=200"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            image_data = response.read()
            content_type = response.headers.get('Content-Type', 'image/png')
            b64 = base64.b64encode(image_data).decode('utf-8')
            data_uri = f"data:{content_type};base64,{b64}"
            _avatar_cache[github_username] = data_uri
            return data_uri
    except Exception as e:
        print(f"Warning: Could not fetch avatar for {github_username}: {e}")
        _avatar_cache[github_username] = None
        return None


def parse_last_active(value):
    """Parse YYYY-MM into a date, using the last day of the month."""
    if not value or value == '-':
        return None
    try:
        year_str, month_str = value.split('-', 1)
        year = int(year_str)
        month = int(month_str)
        last_day = calendar.monthrange(year, month)[1]
        return date(year, month, last_day)
    except Exception:
        return None


def is_active_recent(last_active):
    """Return True if last_active is within ACTIVE_WINDOW_DAYS."""
    last_date = parse_last_active(last_active)
    if not last_date:
        return False
    return (date.today() - last_date).days <= ACTIVE_WINDOW_DAYS


def generate_card(
    github,
    display_name,
    badge_type,
    topics,
    citations,
    files,
    last_active,
    commits,
    size_label,
    avatar_data_uri=None,
    logo_data=None,
):
    """Generate an SVG profile card with GitHub avatar and FreeGym logo."""
    width, height = CARD_SIZES[size_label]
    logo_uri, logo_w, logo_h = logo_data if logo_data else (None, None, None)
    unit = min(width, height)
    margin = unit * 0.06
    header_y = margin

    # Footer scales with card height for better proportions
    footer_h = max(height * 0.14, 120)
    footer_y = height - footer_h

    # Logo placement - fill most of footer width
    if logo_uri and logo_w and logo_h:
        logo_aspect = logo_w / logo_h
        # Use 92% of card width for logo
        logo_w_final = width * 0.92
        logo_h_final = logo_w_final / logo_aspect
        # If height exceeds footer, constrain by height
        if logo_h_final > footer_h * 0.95:
            logo_h_final = footer_h * 0.95
            logo_w_final = logo_h_final * logo_aspect
        logo_x = (width - logo_w_final) / 2
        logo_y = footer_y + (footer_h - logo_h_final) / 2
    else:
        logo_w_final = 0
        logo_h_final = 0
        logo_x = 0
        logo_y = 0

    # Badge symbol and color
    if badge_type == 'maintainer':
        badge_text = 'Maintainer'
        badge_color = '#E10600'
        badge_stroke = '#FFFFFF'
    else:
        badge_text = 'Verified Contributor'
        badge_color = '#E10600'
        badge_stroke = '#E10600'

    # Format topics as broad categories (folder-derived, human-readable)
    topic_labels = {
        'nutrition': 'Nutrition',
        'exercise': 'Fitness',
        'sleep': 'Sleep',
        'mental-health': 'Mental Health',
        'supplements': 'Supplements',
        'recovery': 'Recovery',
        'biomechanics': 'Biomechanics',
    }
    display_topics = [topic_labels.get(t, t.replace('-', ' ').title()) for t in (topics or [])]
    top_topics = display_topics[:3] if display_topics else []
    topics_tokens = top_topics[:] if top_topics else []
    if display_topics and len(display_topics) > 3:
        topics_tokens.append(f'+{len(display_topics) - len(top_topics)} more')
    if not topics_tokens:
        topics_tokens = ['No topics yet']

    # Each topic on its own line for the left column
    topics_lines = topics_tokens[:]

    # Format contributions as a simple count
    contributions_count = len(files) if files else 0
    contributions_display = f'{contributions_count}'

    commits_value = commits if commits is not None else 0
    active_recent = is_active_recent(last_active)

    # Type sizes
    title_size = min(unit * 0.07, 72)
    username_size = title_size * 0.52
    status_size = title_size * 0.4
    label_size = min(unit * 0.03, 30)
    value_size = min(unit * 0.045, 44)
    micro_label_size = max(label_size - 6, 12)

    # Avatar
    avatar_d = min(unit * 0.2, 220)
    avatar_r = avatar_d / 2
    avatar_cx = margin + avatar_r
    avatar_cy = header_y + avatar_r

    badge_cx = avatar_cx + avatar_r * 0.65
    badge_cy = avatar_cy + avatar_r * 0.65
    badge_r = avatar_r * 0.32
    badge_stroke_w = max(unit * 0.004, 2)

    if badge_type == 'maintainer':
        outer_r = badge_r * 0.55
        inner_r = badge_r * 0.26
        points = []
        for i in range(10):
            angle = math.radians(-90 + i * 36)
            r = outer_r if i % 2 == 0 else inner_r
            x = badge_cx + r * math.cos(angle)
            y = badge_cy + r * math.sin(angle)
            points.append(f"{x:.2f},{y:.2f}")
        badge_symbol = (
            f'<polygon points="{" ".join(points)}" fill="white"/>'
        )
    else:
        check_size = badge_r * 0.9
        x1 = badge_cx - check_size * 0.35
        y1 = badge_cy + check_size * 0.05
        x2 = badge_cx - check_size * 0.05
        y2 = badge_cy + check_size * 0.3
        x3 = badge_cx + check_size * 0.4
        y3 = badge_cy - check_size * 0.35
        badge_symbol = (
            f'<polyline points="{x1:.2f},{y1:.2f} {x2:.2f},{y2:.2f} {x3:.2f},{y3:.2f}" '
            f'fill="none" stroke="white" stroke-width="{badge_r * 0.14:.2f}" '
            'stroke-linecap="round" stroke-linejoin="round"/>'
        )

    # Text positions
    name_x = avatar_cx + avatar_r + margin * 0.6
    name_y = header_y + title_size
    username_y = name_y + username_size * 1.45
    status_y = username_y + status_size * 1.45

    # Calculate available space for stats section
    stats_top = avatar_cy + avatar_r + unit * 0.08
    stats_bottom = footer_y - unit * 0.06
    stats_height = stats_bottom - stats_top

    # Two-column layout: left for topics, right for stats
    left_x = margin
    right_x = width * 0.55  # Right column starts at 55% width

    label_value_gap = unit * 0.025
    topics_line_height = value_size * 1.3  # More breathing room between topics

    # Left column: Topics label at top, then topics listed vertically
    topics_label_y = stats_top
    topics_value_start_y = topics_label_y + label_size + label_value_gap

    # Right column: 4 stats evenly distributed
    right_row_height = stats_height / 4

    right1_label_y = stats_top
    right1_value_y = right1_label_y + label_size + label_value_gap

    right2_label_y = stats_top + right_row_height
    right2_value_y = right2_label_y + label_size + label_value_gap

    right3_label_y = stats_top + right_row_height * 2
    right3_value_y = right3_label_y + label_size + label_value_gap

    right4_label_y = stats_top + right_row_height * 3
    right4_value_y = right4_label_y + label_size + label_value_gap

    active_markup = ''
    if active_recent:
        active_dot_r = max(unit * 0.008, 6)
        active_text_size = max(label_size - 4, 12)
        active_x = width - margin
        active_y = header_y + active_dot_r
        active_text_x = active_x - active_dot_r * 2.2
        active_text_y = header_y + active_text_size
        active_markup = f'''  <circle cx="{active_x:.2f}" cy="{active_y:.2f}" r="{active_dot_r:.2f}" fill="#2ecc71"/>
  <text x="{active_text_x:.2f}" y="{active_text_y:.2f}" text-anchor="end" font-family="system-ui, -apple-system, sans-serif" font-size="{active_text_size:.2f}" fill="#b7e3c6">ACTIVE</text>
'''

    # Use base64 data URI if provided, otherwise fall back to external URL
    avatar_url = avatar_data_uri if avatar_data_uri else f"https://github.com/{github}.png?size=200"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0b0b0b;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#1a1a1a;stop-opacity:1" />
    </linearGradient>
    <radialGradient id="glow" cx="85%" cy="15%" r="60%">
      <stop offset="0%" style="stop-color:#E10600;stop-opacity:0.2" />
      <stop offset="100%" style="stop-color:#E10600;stop-opacity:0" />
    </radialGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-opacity="0.3"/>
    </filter>
    <clipPath id="avatar-clip">
      <circle cx="{avatar_cx}" cy="{avatar_cy}" r="{avatar_r}"/>
    </clipPath>
  </defs>

  <!-- Card background -->
  <rect width="{width}" height="{height}" rx="{unit * 0.04:.2f}" fill="url(#bg)" filter="url(#shadow)"/>
  <rect width="{width}" height="{height}" rx="{unit * 0.04:.2f}" fill="url(#glow)"/>
  <rect width="{width}" height="{max(unit * 0.01, 6):.2f}" fill="#E10600"/>

{active_markup}  <!-- Avatar -->
  <circle cx="{avatar_cx}" cy="{avatar_cy}" r="{avatar_r}" fill="#111111"/>
  <image x="{avatar_cx - avatar_r}" y="{avatar_cy - avatar_r}" width="{avatar_d}" height="{avatar_d}" href="{avatar_url}" clip-path="url(#avatar-clip)" preserveAspectRatio="xMidYMid slice"/>
  <circle cx="{avatar_cx}" cy="{avatar_cy}" r="{avatar_r}" fill="none" stroke="#E10600" stroke-width="{max(unit * 0.006, 3):.2f}"/>

  <!-- Badge symbol -->
  <circle cx="{badge_cx:.2f}" cy="{badge_cy:.2f}" r="{badge_r:.2f}" fill="{badge_color}" stroke="{badge_stroke}" stroke-width="{badge_stroke_w:.2f}"/>
  {badge_symbol}

  <!-- Name and status -->
  <text x="{name_x:.2f}" y="{name_y:.2f}" font-family="system-ui, -apple-system, sans-serif" font-size="{title_size:.2f}" font-weight="700" fill="white">{display_name or github}</text>
  <text x="{name_x:.2f}" y="{username_y:.2f}" font-family="system-ui, -apple-system, sans-serif" font-size="{username_size:.2f}" fill="#d0d0d0">@{github}</text>
  <text x="{name_x:.2f}" y="{status_y:.2f}" font-family="system-ui, -apple-system, sans-serif" font-size="{status_size:.2f}" fill="#9b9b9b">FreeGym Wiki {badge_text}</text>

  <!-- Stats -->
  <text x="{left_x:.2f}" y="{topics_label_y:.2f}" font-family="system-ui, -apple-system, sans-serif" font-size="{label_size:.2f}" fill="#8a8a8a">TOP TOPICS</text>
'''
    # Render all topic lines
    for i, topic_line in enumerate(topics_lines):
        line_y = topics_value_start_y + (topics_line_height * i)
        svg += f'''  <text x="{left_x:.2f}" y="{line_y:.2f}" font-family="system-ui, -apple-system, sans-serif" font-size="{value_size:.2f}" fill="white">{topic_line}</text>
'''
    svg += f'''  <text x="{right_x:.2f}" y="{right1_label_y:.2f}" font-family="system-ui, -apple-system, sans-serif" font-size="{label_size:.2f}" fill="#8a8a8a">LAST ACTIVE</text>
  <text x="{right_x:.2f}" y="{right1_value_y:.2f}" font-family="system-ui, -apple-system, sans-serif" font-size="{value_size:.2f}" fill="white">{last_active}</text>

  <text x="{right_x:.2f}" y="{right2_label_y:.2f}" font-family="system-ui, -apple-system, sans-serif" font-size="{label_size:.2f}" fill="#8a8a8a">CITATIONS</text>
  <text x="{right_x:.2f}" y="{right2_value_y:.2f}" font-family="system-ui, -apple-system, sans-serif" font-size="{value_size:.2f}" fill="white">{citations}</text>

  <text x="{right_x:.2f}" y="{right3_label_y:.2f}" font-family="system-ui, -apple-system, sans-serif" font-size="{label_size:.2f}" fill="#8a8a8a">COMMITS</text>
  <text x="{right_x:.2f}" y="{right3_value_y:.2f}" font-family="system-ui, -apple-system, sans-serif" font-size="{value_size:.2f}" fill="white">{commits_value}</text>

  <text x="{right_x:.2f}" y="{right4_label_y:.2f}" font-family="system-ui, -apple-system, sans-serif" font-size="{label_size:.2f}" fill="#8a8a8a">CONTRIBUTIONS</text>
  <text x="{right_x:.2f}" y="{right4_value_y:.2f}" font-family="system-ui, -apple-system, sans-serif" font-size="{value_size:.2f}" fill="white">{contributions_display}</text>

  <!-- Footer -->
  <rect x="0" y="{footer_y:.2f}" width="{width}" height="{footer_h:.2f}" rx="0" fill="#000000"/>
  <rect x="0" y="{footer_y:.2f}" width="{width}" height="{max(unit * 0.01, 6):.2f}" fill="#1f1f1f"/>
'''
    if logo_uri:
        svg += f'''  <image x="{logo_x:.2f}" y="{logo_y:.2f}" width="{logo_w_final:.2f}" height="{logo_h_final:.2f}" href="{logo_uri}" xlink:href="{logo_uri}" preserveAspectRatio="xMidYMid meet"/>
'''
    else:
        svg += f'''  <text x="{width / 2:.2f}" y="{footer_y + footer_h * 0.62:.2f}" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-size="{min(unit * 0.08, 64):.2f}" font-weight="700">
    <tspan fill="white">FREE</tspan><tspan fill="#E10600">GYM</tspan>
  </text>
'''
    svg += '</svg>'
    return svg


def main():
    os.makedirs('cards', exist_ok=True)

    with open('contributors.yaml', 'r') as f:
        data = yaml.safe_load(f)

    logo_data = load_logo_data()

    all_contributors = []

    # Maintainers
    for m in data.get('maintainers', []):
        # Combine topics and specialty fields
        topics = list(m.get('topics', []) or []) + list(m.get('specialty', []) or [])
        all_contributors.append({
            'github': m.get('github', ''),
            'name': m.get('name', m.get('github', '')),
            'type': 'maintainer',
            'topics': topics,
            'citations': m.get('total_citations', 0),
            'files': [c['file'] for c in m.get('contributions', [])],
            'last_active': m.get('last_active', '-'),
            'commits': m.get('commits', 0),
        })

    # Trusted
    trusted = data.get('trusted') or []
    for t in trusted:
        if isinstance(t, dict):
            all_contributors.append({
                'github': t.get('github', ''),
                'name': t.get('name', t.get('github', '')),
                'type': 'trusted',
                'topics': t.get('topics', []),
                'citations': t.get('total_citations', 0),
                'files': [c['file'] for c in t.get('contributions', [])],
                'last_active': t.get('last_active', '-'),
                'commits': t.get('commits', 0),
            })

    # Verified contributors
    contributors = data.get('contributors') or []
    for c in contributors:
        if isinstance(c, dict) and c.get('checkmark'):
            all_contributors.append({
                'github': c.get('github', ''),
                'name': c.get('github', ''),
                'type': 'contributor',
                'topics': c.get('topics', []),
                'citations': c.get('total_citations', 0),
                'files': [cont['file'] for cont in c.get('contributions', [])],
                'last_active': c.get('last_active', '-'),
                'commits': c.get('commits', 0),
            })

    for contrib in all_contributors:
        # Fetch avatar once per contributor (cached for all card sizes)
        avatar_data_uri = fetch_avatar_base64(contrib['github'])

        for size_label in CARD_SIZES:
            svg = generate_card(
                github=contrib['github'],
                display_name=contrib['name'],
                badge_type=contrib['type'],
                topics=contrib['topics'],
                citations=contrib['citations'],
                files=contrib['files'],
                last_active=contrib['last_active'],
                commits=contrib['commits'],
                size_label=size_label,
                avatar_data_uri=avatar_data_uri,
                logo_data=logo_data,
            )

            suffix = '' if size_label == 'default' else f'-{size_label}'
            svg_path = f"cards/{contrib['github']}{suffix}.svg"
            png_path = f"cards/{contrib['github']}{suffix}.png"

            with open(svg_path, 'w', encoding='utf-8') as f:
                f.write(svg)
            print(f"Generated {svg_path}")

            # Also generate PNG version for easy downloading
            if HAS_CAIROSVG:
                try:
                    cairosvg.svg2png(bytestring=svg.encode('utf-8'), write_to=png_path, scale=2)
                    print(f"Generated {png_path}")
                except Exception as e:
                    print(f"Warning: Could not generate PNG for {png_path}: {e}")


if __name__ == '__main__':
    main()
