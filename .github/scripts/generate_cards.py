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
LOGO_PATH = os.path.join(REPO_ROOT, 'assets', 'FreeGym Logo.png')
CARD_SIZES = {
    'default': (1080, 1080),
    'wide': (1200, 630),
    'portrait': (1080, 1350),
    'story': (1080, 1920),
}

ACTIVE_WINDOW_DAYS = 60
USE_LOGO = os.getenv('USE_LOGO', '1').lower() not in ('0', 'false', 'no')

# Constant brand line rendered on every communicator card.
COMMUNICATOR_MISSION = "Building the future of health and fitness."

TOPIC_ALIASES = {
    'heart-health': 'cardiology',
}
TOPIC_LABELS = {
    'nutrition': 'Nutrition',
    'exercise': 'Fitness',
    'exercise-physiology': 'Exercise Physiology',
    'pharmacology': 'Pharmacology',
    'biomarkers': 'Biomarkers',
    'wearables': 'Wearables',
    'musculoskeletal-health': 'Musculoskeletal',
    'dermatology': 'Dermatology',
    'sleep': 'Sleep',
    'mental-health': 'Mental Health',
    'supplements': 'Supplements',
    'recovery': 'Recovery',
    'biomechanics': 'Biomechanics',
    'cardiology': 'Cardiology',
    'Womens-Health': "Women's Health",
}


def format_number(value):
    """Format integers with thousands separators for display."""
    try:
        return f"{int(value):,}"
    except (TypeError, ValueError):
        return str(value)


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


def normalize_topics(topics):
    """Return canonical topic keys without duplicates, preserving order."""
    normalized = []
    seen = set()
    for topic in topics or []:
        canonical = TOPIC_ALIASES.get(topic, topic)
        if canonical and canonical not in seen:
            seen.add(canonical)
            normalized.append(canonical)
    return normalized


def label_topic(key):
    """Display label for a canonical topic key."""
    return TOPIC_LABELS.get(key, key.replace('-', ' ').title())


def chunk_topics(topics, max_chars):
    """Wrap topic labels into lines that fit the card width."""
    chunks = []
    current = []
    current_len = 0
    separator_len = len('  ·  ')

    for topic in topics:
        topic_len = len(label_topic(topic))
        next_len = topic_len if not current else current_len + separator_len + topic_len
        if current and next_len > max_chars:
            chunks.append(current)
            current = [topic]
            current_len = topic_len
        else:
            current.append(topic)
            current_len = next_len

    if current:
        chunks.append(current)
    return chunks

def format_verified_since(ym):
    """'2026-05' -> 'May 2026'. Returns the input on parse failure."""
    months = ['', 'January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    try:
        y, m = ym.split('-', 1)
        return f"{months[int(m)]} {int(y)}"
    except Exception:
        return ym or '-'


RED = '#B3131B'
LOGO_CROP_VIEWBOX = (55, 165, 815, 130)
# Sizes that use the modern (tile-grid) contributor layout. The landscape
# 'wide' and very tall 'story' formats keep the original single-column layout.
MODERN_SIZES = ('portrait',)
MODERN_HANDLES = {'mutant1643', 'Thestrongdoc'}


# Professional line icons (Lucide / Tabler, 24x24 viewBox, stroke-based).
# Stored colour-agnostic; _icon() applies stroke colour + scale at render time.
# Canonical paths verified against the lucide / tabler source (24x24 viewBox).
# 'moon' keeps two appended "z" strokes to match the reference's sleep glyph.
_ICON_PATHS = {
    'calendar': '<path d="M8 2v4"/><path d="M16 2v4"/><rect width="18" height="18" x="3" y="4" rx="2"/><path d="M3 10h18"/><path d="M8 14h.01"/><path d="M12 14h.01"/><path d="M16 14h.01"/><path d="M8 18h.01"/><path d="M12 18h.01"/><path d="M16 18h.01"/>',
    'file-text': '<path d="M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z"/><path d="M14 2v5a1 1 0 0 0 1 1h5"/><path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/>',
    'code': '<path d="m18 16 4-4-4-4"/><path d="m6 8-4 4 4 4"/><path d="m14.5 4-5 16"/>',
    'users': '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><path d="M16 3.128a4 4 0 0 1 0 7.744"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><circle cx="9" cy="7" r="4"/>',
    'salad': '<path d="M7 21h10"/><path d="M12 21a9 9 0 0 0 9-9H3a9 9 0 0 0 9 9Z"/><path d="M11.38 12a2.4 2.4 0 0 1-.4-4.77 2.4 2.4 0 0 1 3.2-2.77 2.4 2.4 0 0 1 3.47-.63 2.4 2.4 0 0 1 3.37 3.37 2.4 2.4 0 0 1-1.1 3.7 2.51 2.51 0 0 1 .03 1.1"/><path d="m13 12 4-4"/><path d="M10.9 7.25A3.99 3.99 0 0 0 4 10c0 .73.2 1.41.54 2"/>',
    'run': '<path d="M11.007 5a2 2 0 1 0 4 0a2 2 0 1 0 -4 0"/><path d="M4 17l5 1l.75 -1.5"/><path d="M15 21v-4l-4 -3l1 -6"/><path d="M7 12v-3l5 -1l3 3l3 1"/>',
    'pill': '<path d="m10.5 20.5 10-10a4.95 4.95 0 1 0-7-7l-10 10a4.95 4.95 0 1 0 7 7Z"/><path d="m8.5 8.5 7 7"/>',
    'heart-pulse': '<path d="M2 9.5a5.5 5.5 0 0 1 9.591-3.676.56.56 0 0 0 .818 0A5.49 5.49 0 0 1 22 9.5c0 2.29-1.5 4-3 5.5l-5.492 5.313a2 2 0 0 1-3 .019L5 15c-1.5-1.5-3-3.2-3-5.5"/><path d="M3.22 13H9.5l.5-1 2 4.5 2-7 1.5 3.5h5.27"/>',
    'testtube': '<g transform="rotate(11 12 12)"><path d="M14.5 2v17.5c0 1.4-1.1 2.5-2.5 2.5c-1.4 0-2.5-1.1-2.5-2.5V2"/><path d="M8.5 2h7"/><path d="M14.5 16h-5"/><circle cx="10.9" cy="18.4" r="0.75"/><circle cx="12.7" cy="16.8" r="0.65"/></g>',
    'moon': '<path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/><path d="M17.3 3.4h2.9l-2.9 3.2h2.9"/><path d="M19.6 6.9h2.1l-2.1 2.4h2.1"/>',
    'watch': '<path d="M6 9a3 3 0 0 1 3-3h6a3 3 0 0 1 3 3v6a3 3 0 0 1-3 3h-6a3 3 0 0 1-3-3v-6"/><path d="M9 18v3h6v-3"/><path d="M9 6v-3h6v3"/><path d="M12 9.8v2.7l1.5 1"/>',
    'venus': '<circle cx="12" cy="9" r="6"/><path d="M12 15v7"/><path d="M9 19h6"/>',
    'bone': '<path d="M17 10c.7-.7 1.69 0 2.5 0a2.5 2.5 0 1 0 0-5 .5.5 0 0 1-.5-.5 2.5 2.5 0 1 0-5 0c0 .81.7 1.8 0 2.5l-7 7c-.7.7-1.69 0-2.5 0a2.5 2.5 0 0 0 0 5c.28 0 .5.22.5.5a2.5 2.5 0 1 0 5 0c0-.81-.7-1.8 0-2.5Z"/>',
    'shield': '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/>',
    'tag': '<path d="M12.586 2.586A2 2 0 0 0 11.172 2H4a2 2 0 0 0-2 2v7.172a2 2 0 0 0 .586 1.414l8.704 8.704a2.426 2.426 0 0 0 3.42 0l6.58-6.58a2.426 2.426 0 0 0 0-3.42z"/><circle cx="7.5" cy="7.5" r="1.5"/>',
}

_STAT_ICON = {
    'calendar': 'calendar',
    'citations': 'file-text',
    'commits': 'code',
    'contributions': 'users',
}

_TOPIC_ICON = {
    'nutrition': 'salad',
    'exercise-physiology': 'run',
    'exercise': 'run',
    'pharmacology': 'pill',
    'supplements': 'pill',
    'cardiology': 'heart-pulse',
    'biomarkers': 'testtube',
    'sleep': 'moon',
    'wearables': 'watch',
    'Womens-Health': 'venus',
    'musculoskeletal-health': 'bone',
    'dermatology': 'shield',
}


def _icon(key, cx, cy, size, stroke_px, color):
    """Render a named 24x24 icon, centered on (cx, cy) and scaled to `size`.

    `stroke_px` is the stroke width in the icon's own 24-unit space (lucide's
    native is 2). It is NOT divided by the scale, so the visual stroke scales
    with the icon size — i.e. authentic, proportional lucide weight at any size.
    """
    inner = _ICON_PATHS.get(key) or _ICON_PATHS['tag']
    k = size / 24.0
    sw = stroke_px
    tx = cx - size / 2.0
    ty = cy - size / 2.0
    return (
        f'<g transform="translate({tx:.2f} {ty:.2f}) scale({k:.4f})" '
        f'fill="none" stroke="{color}" stroke-width="{sw:.2f}" '
        f'stroke-linecap="round" stroke-linejoin="round">{inner}</g>'
    )


def _stat_glyph(name, cx, cy, s, sw, color):
    """Stat-tile icon tuned to the supplied reference card."""
    if name == 'calendar':
        w = s * 0.78
        h = s * 0.68
        x = cx - w / 2
        y = cy - h / 2 + s * 0.03
        return (
            f'<g fill="none" stroke="{color}" stroke-width="{sw:.2f}" stroke-linecap="round" stroke-linejoin="round">'
            f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{s*0.08:.2f}"/>'
            f'<path d="M {x:.2f} {y+s*0.21:.2f} H {x+w:.2f}"/>'
            f'<path d="M {x+s*0.18:.2f} {y-s*0.08:.2f} V {y+s*0.12:.2f}"/>'
            f'<path d="M {x+w-s*0.18:.2f} {y-s*0.08:.2f} V {y+s*0.12:.2f}"/>'
            f'<path d="M {cx-s*0.11:.2f} {cy+s*0.08:.2f} l {s*0.08:.2f} {s*0.08:.2f} l {s*0.17:.2f} {-s*0.2:.2f}"/>'
            f'</g>'
        )
    if name == 'citations':
        w = s * 0.62
        h = s * 0.76
        x = cx - w / 2
        y = cy - h / 2 + s * 0.01
        fold = s * 0.17
        txt_y = cy + s * 0.16
        return (
            f'<g fill="none" stroke="{color}" stroke-width="{sw:.2f}" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M {x:.2f} {y:.2f} H {x+w-fold:.2f} L {x+w:.2f} {y+fold:.2f} V {y+h:.2f} H {x:.2f} Z"/>'
            f'<path d="M {x+w-fold:.2f} {y:.2f} V {y+fold:.2f} H {x+w:.2f}"/>'
            f'<path d="M {x+s*0.15:.2f} {y+h-s*0.18:.2f} H {x+w-s*0.16:.2f}"/>'
            f'</g>'
            f'<text x="{cx-s*0.05:.2f}" y="{txt_y:.2f}" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-size="{s*0.285:.2f}" font-weight="700" fill="{color}">6</text>'
            f'<circle cx="{cx+s*0.15:.2f}" cy="{txt_y-s*0.18:.2f}" r="{s*0.055:.2f}" fill="none" stroke="{color}" stroke-width="{sw*0.75:.2f}"/>'
        )
    if name == 'commits':
        left = cx - s * 0.40
        right = cx + s * 0.40
        top = cy - s * 0.28
        mid = cy
        bot = cy + s * 0.28
        return (
            f'<g fill="none" stroke="{color}" stroke-width="{sw*1.12:.2f}" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M {left+s*0.18:.2f} {top:.2f} L {left:.2f} {mid:.2f} L {left+s*0.18:.2f} {bot:.2f}"/>'
            f'<path d="M {right-s*0.18:.2f} {top:.2f} L {right:.2f} {mid:.2f} L {right-s*0.18:.2f} {bot:.2f}"/>'
            f'<path d="M {cx+s*0.12:.2f} {cy-s*0.42:.2f} L {cx-s*0.12:.2f} {cy+s*0.42:.2f}"/>'
            f'</g>'
        )
    if name == 'contributions':
        return (
            f'<g fill="none" stroke="{color}" stroke-width="{sw:.2f}" stroke-linecap="round" stroke-linejoin="round">'
            f'<circle cx="{cx-s*0.17:.2f}" cy="{cy-s*0.19:.2f}" r="{s*0.15:.2f}"/>'
            f'<circle cx="{cx+s*0.23:.2f}" cy="{cy-s*0.13:.2f}" r="{s*0.12:.2f}"/>'
            f'<path d="M {cx-s*0.47:.2f} {cy+s*0.33:.2f} C {cx-s*0.42:.2f} {cy+s*0.02:.2f}, {cx-s*0.16:.2f} {cy-s*0.01:.2f}, {cx+s*0.02:.2f} {cy+s*0.10:.2f}"/>'
            f'<path d="M {cx+s*0.10:.2f} {cy+s*0.12:.2f} C {cx+s*0.33:.2f} {cy+s*0.10:.2f}, {cx+s*0.48:.2f} {cy+s*0.22:.2f}, {cx+s*0.50:.2f} {cy+s*0.43:.2f}"/>'
            f'</g>'
        )
    return _icon(_STAT_ICON.get(name, 'tag'), cx, cy, s, sw, color)

def _topic_glyph(key, cx, cy, s, sw, color):
    """Topic-tile icon. Delegates to the professional icon set."""
    return _icon(_TOPIC_ICON.get(key, 'tag'), cx, cy, s * 1.07, sw, color)


def generate_card_reference(
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
    """Modern "reference" portrait card for the maintainers (Abhinav, Neha).

    DESIGN RULES — preserve these; do NOT revert to a fixed grid or placeholders.

    Scope: rendered only when size_label in MODERN_SIZES (('portrait',)) AND
    github in MODERN_HANDLES ({'mutant1643','Thestrongdoc'}). Every other size or
    handle falls back to the legacy generate_card() layout.

    Topic grid (DYNAMIC — scales with the number of topics):
      * 2-column grid; rows = ceil(n_topics / 2). NO empty "+" placeholders.
      * Tile height scales to fill the panel, capped at a comfortable size
        (height*0.072) so few topics aren't stretched into slabs, and floored
        (height*0.044) so many stay readable. Icon + label font follow tile height.
      * Sparse cards: the TOP TOPICS panel HUGS its content (panel_h_draw =
        min(content_height, full_height)); the freed space becomes open,
        softly-lit card above the footer. ~5+ topics fill the panel completely.
      * Odd topic count: the lone final tile is centered in its row.
      * >10 topics: first 9 + a "+N more" tile (handled where topic_tiles is built).

    Icons: canonical lucide/tabler paths in _ICON_PATHS, drawn by _icon() at a
    thin proportional stroke (icon_sw ~ 1.6, finer than lucide-native 2.0) to
    match the reference. Glyphs picked to match the reference exactly: Biomarkers
    = tilted test tube with bubbles (NOT a flask), Wearables = square smartwatch
    (Tabler device-watch, NOT round), Sleep = crescent moon + two z's. Stat-tile
    icons are bespoke in _stat_glyph(). Do not revert these.

    Footer: a softly-rounded bottom panel (not a hard strip), pure black directly
    behind the logo so the logo asset's black banner blends in, with a crimson
    light-bar accent at the top-center above the logo and no hard divider line.
    """
    width, height = CARD_SIZES[size_label]
    logo_uri, logo_w, logo_h = logo_data if logo_data else (None, None, None)
    unit = min(width, height)

    frame_x = width * 0.028
    frame_y = height * 0.022
    frame_w = width - 2 * frame_x
    frame_h = height - 2 * frame_y
    corner = width * 0.032
    content_inset = width * 0.04
    content_x = frame_x + content_inset
    content_w = frame_w - 2 * content_inset

    citations_display = format_number(citations if citations is not None else 0)
    commits_display = format_number(commits if commits is not None else 0)
    contributions_display = format_number(len(files) if files else 0)
    active_recent = is_active_recent(last_active)
    badge_text = 'Maintainer' if badge_type == 'maintainer' else 'Verified Contributor'

    topic_keys = normalize_topics(topics)
    extra = 0
    if len(topic_keys) > 10:
        extra = len(topic_keys) - 9
        topic_keys = topic_keys[:9]
    topic_tiles = [(k, TOPIC_LABELS.get(k, k.replace('-', ' ').title())) for k in topic_keys]
    if extra:
        topic_tiles.append(('__more__', f'+{extra} more'))
    if not topic_tiles:
        topic_tiles = [('__none__', 'No topics yet')]

    avatar_d = width * 0.204
    avatar_r = avatar_d / 2
    avatar_cx = frame_x + frame_w * 0.18
    avatar_cy = frame_y + frame_h * 0.171
    avatar_url = avatar_data_uri if avatar_data_uri else f"https://github.com/{github}.png?size=200"

    badge_cx = avatar_cx + avatar_r * 0.72
    badge_cy = avatar_cy + avatar_r * 0.72
    badge_r = avatar_r * 0.29
    badge_stroke_w = max(unit * 0.004, 2)
    if badge_type == 'maintainer':
        outer_r = badge_r * 0.58
        inner_r = badge_r * 0.27
        pts = []
        for i in range(10):
            angle = math.radians(-90 + i * 36)
            rr = outer_r if i % 2 == 0 else inner_r
            pts.append(f"{badge_cx + rr * math.cos(angle):.2f},{badge_cy + rr * math.sin(angle):.2f}")
        badge_symbol = f'<polygon points="{" ".join(pts)}" fill="white"/>'
        badge_fill, badge_stroke = RED, '#FFFFFF'
    else:
        cs = badge_r * 0.9
        badge_symbol = (
            f'<polyline points="{badge_cx-cs*0.35:.2f},{badge_cy+cs*0.05:.2f} '
            f'{badge_cx-cs*0.05:.2f},{badge_cy+cs*0.3:.2f} {badge_cx+cs*0.4:.2f},{badge_cy-cs*0.35:.2f}" '
            f'fill="none" stroke="white" stroke-width="{badge_r*0.16:.2f}" stroke-linecap="round" stroke-linejoin="round"/>'
        )
        badge_fill, badge_stroke = RED, RED

    name_x = avatar_cx + avatar_r + width * 0.071
    name_y = frame_y + height * 0.107
    name_size = min(width * 0.0665, 72)
    handle_size = min(width * 0.028, 31)
    role_size = min(width * 0.0225, 25)
    handle_y = name_y + handle_size * 1.55
    role_y = handle_y + role_size * 1.55

    footer_h = max(height * 0.10, 124)
    footer_y = frame_y + frame_h - footer_h
    if logo_uri and logo_w and logo_h:
        _, _, logo_crop_w, logo_crop_h = LOGO_CROP_VIEWBOX
        logo_aspect = logo_crop_w / logo_crop_h
        logo_w_final = width * 0.47
        logo_h_final = logo_w_final / logo_aspect
        logo_x = (width - logo_w_final) / 2
        logo_y = footer_y + footer_h * 0.60 - logo_h_final / 2
    else:
        logo_x = logo_y = logo_w_final = logo_h_final = 0

    active_markup = ''
    if active_recent:
        p_fs = max(width * 0.0215, 18)
        dot_r = max(width * 0.008, 8)
        pad_x = p_fs * 0.9
        gap = p_fs * 0.55
        text_w = len('ACTIVE') * p_fs * 0.62
        pill_w = pad_x * 2 + dot_r * 2 + gap + text_w
        pill_h = p_fs * 2.18
        pill_x = frame_x + frame_w - width * 0.035 - pill_w
        pill_y = frame_y + height * 0.04
        cy_p = pill_y + pill_h / 2
        dot_cx = pill_x + pad_x + dot_r
        txt_x = dot_cx + dot_r + gap
        active_markup = (
            f'  <rect x="{pill_x:.2f}" y="{pill_y:.2f}" width="{pill_w:.2f}" height="{pill_h:.2f}" rx="{pill_h/2:.2f}" fill="url(#activePillGrad)" stroke="#4f3838" stroke-opacity="0.82" stroke-width="1.35"/>\n'
            f'  <circle cx="{dot_cx:.2f}" cy="{cy_p:.2f}" r="{dot_r:.2f}" fill="#5ee27f"/>\n'
            f'  <text x="{txt_x:.2f}" y="{cy_p + p_fs*0.34:.2f}" font-family="system-ui, -apple-system, sans-serif" font-size="{p_fs:.2f}" font-weight="560" letter-spacing="1.25" fill="#e7e7e7">ACTIVE</text>\n'
        )

    stat_x = name_x
    stat_top = frame_y + height * 0.213
    stat_gap = width * 0.022
    stat_right = frame_x + frame_w - width * 0.030
    stat_tile_w = (stat_right - stat_x - stat_gap) / 2
    stat_row_gap = height * 0.016
    stat_tile_h = height * 0.087
    stat_grid_h = 2 * stat_tile_h + stat_row_gap

    block_gap = height * 0.050
    panel_x = content_x
    panel_y = stat_top + stat_grid_h + block_gap
    panel_w = content_w
    panel_bottom_gap = height * 0.024
    panel_h = footer_y - panel_y - panel_bottom_gap
    panel_pad = width * 0.036
    topic_col_gap = width * 0.028
    topic_row_gap = width * 0.0165
    label_row_h = width * 0.024
    gap_after_label = width * 0.018
    n_topics = len(topic_tiles)
    rows = max(1, math.ceil(n_topics / 2))
    topic_tile_w = (panel_w - 2 * panel_pad - topic_col_gap) / 2
    avail_grid_h = panel_h - 2 * panel_pad - label_row_h - gap_after_label
    # Comfortable tile height: shrink to fit when there are many rows, but never
    # stretch past a comfortable size when there are few. The panel then HUGS its
    # content (compact) for sparse cards instead of being a half-empty box; the
    # freed space below becomes open, softly-lit card before the footer.
    raw_tile_h = (avail_grid_h - (rows - 1) * topic_row_gap) / rows
    topic_tile_h = max(min(raw_tile_h, height * 0.072), height * 0.044)
    topic_grid_h = rows * topic_tile_h + (rows - 1) * topic_row_gap
    panel_content_h = 2 * panel_pad + label_row_h + gap_after_label + topic_grid_h
    panel_h_draw = min(panel_content_h, panel_h)

    p = []
    p.append(f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#050505;stop-opacity:1"/>
      <stop offset="42%" style="stop-color:#060505;stop-opacity:1"/>
      <stop offset="76%" style="stop-color:#0B0506;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#1B0709;stop-opacity:1"/>
    </linearGradient>
    <radialGradient id="glow" cx="86%" cy="3%" r="78%">
      <stop offset="0%" style="stop-color:#9C1019;stop-opacity:0.52"/>
      <stop offset="30%" style="stop-color:#760D14;stop-opacity:0.26"/>
      <stop offset="62%" style="stop-color:#3A0608;stop-opacity:0.09"/>
      <stop offset="100%" style="stop-color:#120203;stop-opacity:0"/>
    </radialGradient>
    <radialGradient id="glow2" cx="14%" cy="100%" r="76%">
      <stop offset="0%" style="stop-color:#7E1119;stop-opacity:0.16"/>
      <stop offset="45%" style="stop-color:#3C070A;stop-opacity:0.065"/>
      <stop offset="100%" style="stop-color:#120203;stop-opacity:0"/>
    </radialGradient>
    <radialGradient id="glow3" cx="93%" cy="44%" r="66%">
      <stop offset="0%" style="stop-color:#820E15;stop-opacity:0.21"/>
      <stop offset="42%" style="stop-color:#420709;stop-opacity:0.085"/>
      <stop offset="100%" style="stop-color:#120203;stop-opacity:0"/>
    </radialGradient>
    <radialGradient id="footerAmbient" cx="50%" cy="86%" r="52%">
      <stop offset="0%" style="stop-color:#8C0F17;stop-opacity:0.17"/>
      <stop offset="38%" style="stop-color:#48070C;stop-opacity:0.075"/>
      <stop offset="100%" style="stop-color:#120203;stop-opacity:0"/>
    </radialGradient>
    <linearGradient id="tileGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1D1B1B;stop-opacity:1"/>
      <stop offset="50%" style="stop-color:#111010;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#130708;stop-opacity:1"/>
    </linearGradient>
    <linearGradient id="topicPillGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#171616;stop-opacity:0.78"/>
      <stop offset="54%" style="stop-color:#0D0C0C;stop-opacity:0.68"/>
      <stop offset="100%" style="stop-color:#17090A;stop-opacity:0.58"/>
    </linearGradient>
    <linearGradient id="topicEdgeGlow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#3B0507;stop-opacity:0"/>
      <stop offset="70%" style="stop-color:#6A0B10;stop-opacity:0.055"/>
      <stop offset="100%" style="stop-color:#9E1118;stop-opacity:0.18"/>
    </linearGradient>
    <linearGradient id="panelGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#121111;stop-opacity:1"/>
      <stop offset="46%" style="stop-color:#0D0C0C;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#070606;stop-opacity:1"/>
    </linearGradient>
    <linearGradient id="edgeGlow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#3B0507;stop-opacity:0"/>
      <stop offset="70%" style="stop-color:#7A0C12;stop-opacity:0.09"/>
      <stop offset="100%" style="stop-color:#B3131B;stop-opacity:0.30"/>
    </linearGradient>
    <linearGradient id="activePillGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#171313;stop-opacity:0.96"/>
      <stop offset="100%" style="stop-color:#332020;stop-opacity:0.96"/>
    </linearGradient>
    <linearGradient id="footerPanelGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#0C0708;stop-opacity:1"/>
      <stop offset="34%" style="stop-color:#000000;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#000000;stop-opacity:1"/>
    </linearGradient>
    <radialGradient id="footerTopGlow" cx="50%" cy="50%" r="60%">
      <stop offset="0%" style="stop-color:#D11620;stop-opacity:0.68"/>
      <stop offset="30%" style="stop-color:#8E1017;stop-opacity:0.28"/>
      <stop offset="68%" style="stop-color:#2A0507;stop-opacity:0.06"/>
      <stop offset="100%" style="stop-color:#120304;stop-opacity:0"/>
    </radialGradient>
    <linearGradient id="footerAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#E10600;stop-opacity:0"/>
      <stop offset="26%" style="stop-color:#E10600;stop-opacity:0.10"/>
      <stop offset="50%" style="stop-color:#F4232C;stop-opacity:0.88"/>
      <stop offset="74%" style="stop-color:#E10600;stop-opacity:0.10"/>
      <stop offset="100%" style="stop-color:#E10600;stop-opacity:0"/>
    </linearGradient>
    <filter id="accentGlow" x="-20%" y="-600%" width="140%" height="1300%">
      <feGaussianBlur stdDeviation="5.5"/>
    </filter>
    <radialGradient id="footerLogoBed" cx="50%" cy="58%" r="68%">
      <stop offset="0%" style="stop-color:#010101;stop-opacity:0.98"/>
      <stop offset="58%" style="stop-color:#010101;stop-opacity:0.82"/>
      <stop offset="100%" style="stop-color:#010101;stop-opacity:0"/>
    </radialGradient>
    <pattern id="dots" width="8.5" height="8.5" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.08" fill="#B3131B" shape-rendering="geometricPrecision"/>
    </pattern>
    <radialGradient id="dotFade" cx="93%" cy="4%" r="57%">
      <stop offset="0%" style="stop-color:#ffffff;stop-opacity:1"/>
      <stop offset="18%" style="stop-color:#ffffff;stop-opacity:0.96"/>
      <stop offset="39%" style="stop-color:#ffffff;stop-opacity:0.58"/>
      <stop offset="61%" style="stop-color:#ffffff;stop-opacity:0.18"/>
      <stop offset="81%" style="stop-color:#ffffff;stop-opacity:0.035"/>
      <stop offset="100%" style="stop-color:#ffffff;stop-opacity:0"/>
    </radialGradient>
    <mask id="dotMask" maskUnits="userSpaceOnUse" x="0" y="0" width="{width}" height="{height}">
      <rect width="{width}" height="{height}" fill="#000000"/>
      <rect width="{width}" height="{height}" fill="url(#dotFade)"/>
    </mask>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-opacity="0.3"/>
    </filter>
    <filter id="redGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="0" stdDeviation="8.5" flood-color="#8B0E14" flood-opacity="0.30"/>
    </filter>
    <filter id="frameGlow" x="-8%" y="-8%" width="116%" height="116%">
      <feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="#681016" flood-opacity="0.24"/>
    </filter>
    <filter id="tileGlow" x="-24%" y="-28%" width="148%" height="156%">
      <feDropShadow dx="0" dy="0" stdDeviation="5.5" flood-color="#7A1117" flood-opacity="0.22"/>
    </filter>
    <filter id="softBlackBlend" x="-30%" y="-80%" width="160%" height="260%">
      <feGaussianBlur stdDeviation="18"/>
    </filter>
    <clipPath id="card-clip"><rect x="{frame_x:.2f}" y="{frame_y:.2f}" width="{frame_w:.2f}" height="{frame_h:.2f}" rx="{corner:.2f}"/></clipPath>
    <clipPath id="avatar-clip"><circle cx="{avatar_cx:.2f}" cy="{avatar_cy:.2f}" r="{avatar_r:.2f}"/></clipPath>
  </defs>

  <rect width="{width}" height="{height}" fill="#000000"/>
  <g clip-path="url(#card-clip)">
    <rect x="{frame_x:.2f}" y="{frame_y:.2f}" width="{frame_w:.2f}" height="{frame_h:.2f}" rx="{corner:.2f}" fill="url(#bg)" filter="url(#shadow)"/>
    <rect x="{frame_x:.2f}" y="{frame_y:.2f}" width="{frame_w:.2f}" height="{frame_h:.2f}" rx="{corner:.2f}" fill="url(#glow)"/>
    <rect x="{frame_x:.2f}" y="{frame_y:.2f}" width="{frame_w:.2f}" height="{frame_h:.2f}" rx="{corner:.2f}" fill="url(#glow2)"/>
    <rect x="{frame_x:.2f}" y="{frame_y:.2f}" width="{frame_w:.2f}" height="{frame_h:.2f}" rx="{corner:.2f}" fill="url(#glow3)"/>
    <rect x="{frame_x:.2f}" y="{frame_y:.2f}" width="{frame_w:.2f}" height="{frame_h:.2f}" rx="{corner:.2f}" fill="url(#footerAmbient)"/>
    <g mask="url(#dotMask)"><rect x="{frame_x:.2f}" y="{frame_y:.2f}" width="{frame_w:.2f}" height="{frame_h:.2f}" fill="url(#dots)" fill-opacity="0.56"/></g>
  </g>
''')
    p.append(active_markup)
    p.append(f'''  <circle cx="{avatar_cx:.2f}" cy="{avatar_cy:.2f}" r="{avatar_r:.2f}" fill="#111111"/>
  <image x="{avatar_cx-avatar_r:.2f}" y="{avatar_cy-avatar_r:.2f}" width="{avatar_d:.2f}" height="{avatar_d:.2f}" href="{avatar_url}" xlink:href="{avatar_url}" clip-path="url(#avatar-clip)" preserveAspectRatio="xMidYMid slice"/>
  <circle cx="{avatar_cx:.2f}" cy="{avatar_cy:.2f}" r="{avatar_r:.2f}" fill="none" stroke="{RED}" stroke-width="5.4" filter="url(#redGlow)"/>
  <circle cx="{badge_cx:.2f}" cy="{badge_cy:.2f}" r="{badge_r:.2f}" fill="{badge_fill}" stroke="{badge_stroke}" stroke-width="{badge_stroke_w:.2f}"/>
  {badge_symbol}
  <text x="{name_x:.2f}" y="{name_y:.2f}" font-family="system-ui, -apple-system, sans-serif" font-size="{name_size:.2f}" font-weight="700" fill="#ffffff">{display_name or github}</text>
  <text x="{name_x:.2f}" y="{handle_y:.2f}" font-family="system-ui, -apple-system, sans-serif" font-size="{handle_size:.2f}" font-weight="400" fill="#9f9f9f">@{github}</text>
  <text x="{name_x:.2f}" y="{role_y:.2f}" font-family="system-ui, -apple-system, sans-serif" font-size="{role_size:.2f}" font-weight="400" fill="#858585">FreeGym Wiki {badge_text}</text>
''')

    stats = [
        ('calendar', 'LAST ACTIVE', str(last_active or '-')),
        ('citations', 'CITATIONS', citations_display),
        ('commits', 'COMMITS', commits_display),
        ('contributions', 'CONTRIBUTIONS', contributions_display),
    ]
    for idx, (icon, lbl, val) in enumerate(stats):
        r = idx // 2
        c = idx % 2
        tx = stat_x + c * (stat_tile_w + stat_gap)
        ty = stat_top + r * (stat_tile_h + stat_row_gap)
        icon_r = stat_tile_h * 0.27
        icx = tx + stat_tile_h * 0.45
        icy = ty + stat_tile_h / 2
        isize = icon_r * 1.06
        text_x = tx + stat_tile_h * 0.91
        lbl_size = max(width * 0.0145, 15)
        val_size = min(width * 0.0385, 42)
        tile_rx = stat_tile_h * 0.16
        hl_inset = max(tile_rx * 0.5, 6)
        p.append(
            f'  <rect x="{tx:.2f}" y="{ty:.2f}" width="{stat_tile_w:.2f}" height="{stat_tile_h:.2f}" rx="{tile_rx:.2f}" fill="url(#tileGrad)" stroke="#433637" stroke-opacity="0.94" stroke-width="1.25"/>\n'
            f'  <rect x="{tx+stat_tile_w-width*0.043:.2f}" y="{ty:.2f}" width="{width*0.043:.2f}" height="{stat_tile_h:.2f}" rx="{tile_rx:.2f}" fill="url(#edgeGlow)"/>\n'
            f'  <path d="M {tx+stat_tile_w-tile_rx:.2f} {ty+0.75:.2f} Q {tx+stat_tile_w-0.75:.2f} {ty+0.75:.2f} {tx+stat_tile_w-0.75:.2f} {ty+tile_rx:.2f} V {ty+stat_tile_h-tile_rx:.2f} Q {tx+stat_tile_w-0.75:.2f} {ty+stat_tile_h-0.75:.2f} {tx+stat_tile_w-tile_rx:.2f} {ty+stat_tile_h-0.75:.2f}" fill="none" stroke="{RED}" stroke-opacity="0.42" stroke-width="1.05" filter="url(#tileGlow)"/>\n'
            f'  <line x1="{tx+hl_inset:.2f}" y1="{ty+1.5:.2f}" x2="{tx+stat_tile_w-hl_inset:.2f}" y2="{ty+1.5:.2f}" stroke="#ffffff" stroke-opacity="0.09" stroke-width="1"/>\n'
            f'  <circle cx="{icx:.2f}" cy="{icy:.2f}" r="{icon_r:.2f}" fill="{RED}" fill-opacity="0.10" stroke="{RED}" stroke-opacity="0.62" stroke-width="1.15"/>\n'
            f'  {_stat_glyph(icon, icx, icy, isize, 2.35, RED)}\n'
            f'  <text x="{text_x:.2f}" y="{ty+stat_tile_h*0.38:.2f}" font-family="system-ui, -apple-system, sans-serif" font-size="{lbl_size:.2f}" font-weight="540" letter-spacing="1.35" fill="#a9a9a9">{lbl}</text>\n'
            f'  <text x="{text_x:.2f}" y="{ty+stat_tile_h*0.80:.2f}" font-family="system-ui, -apple-system, sans-serif" font-size="{val_size:.2f}" font-weight="760" fill="#f8f8f8">{val}</text>\n'
        )

    p.append(f'  <rect x="{panel_x:.2f}" y="{panel_y:.2f}" width="{panel_w:.2f}" height="{panel_h_draw:.2f}" rx="{width*0.024:.2f}" fill="url(#panelGrad)" stroke="#352B2C" stroke-opacity="0.95" stroke-width="1.25"/>\n')
    bar_x = panel_x + panel_pad
    bar_y = panel_y + panel_pad
    lbl_size2 = max(width * 0.016, 17)
    bar_w = width * 0.0065
    bar_h = lbl_size2 * 1.25
    p.append(
        f'  <rect x="{bar_x:.2f}" y="{bar_y:.2f}" width="{bar_w:.2f}" height="{bar_h:.2f}" rx="{bar_w/2:.2f}" fill="{RED}"/>\n'
        f'  <text x="{bar_x + bar_w + 16:.2f}" y="{bar_y + lbl_size2:.2f}" font-family="system-ui, -apple-system, sans-serif" font-size="{lbl_size2:.2f}" font-weight="620" letter-spacing="4.6" fill="#e6e6e6">TOP TOPICS</text>\n'
    )
    grid_top = panel_y + panel_pad + label_row_h + gap_after_label
    last_solo = (n_topics % 2 == 1)
    icon_sw = 1.6  # thinner stroke to match the reference (24-unit space)
    for slot in range(n_topics):
        r = slot // 2
        c = slot % 2
        tx = panel_x + panel_pad + c * (topic_tile_w + topic_col_gap)
        ty = grid_top + r * (topic_tile_h + topic_row_gap)
        if last_solo and slot == n_topics - 1:
            tx = panel_x + panel_pad + (panel_w - 2 * panel_pad - topic_tile_w) / 2
        key, lbl = topic_tiles[slot]
        gcx = tx + topic_tile_h * 0.58
        gcy = ty + topic_tile_h / 2
        gsize = topic_tile_h * 0.47
        div_x = tx + topic_tile_h * 1.34
        lab_x = tx + topic_tile_h * 1.58
        lab_size = max(min(topic_tile_h * 0.26, 22), 16)
        p.append(
            f'  <rect x="{tx:.2f}" y="{ty:.2f}" width="{topic_tile_w:.2f}" height="{topic_tile_h:.2f}" rx="{topic_tile_h*0.24:.2f}" fill="url(#topicPillGrad)" stroke="#642226" stroke-opacity="0.50" stroke-width="0.85"/>\n'
            f'  <rect x="{tx+topic_tile_w-width*0.032:.2f}" y="{ty:.2f}" width="{width*0.032:.2f}" height="{topic_tile_h:.2f}" rx="{topic_tile_h*0.24:.2f}" fill="url(#topicEdgeGlow)"/>\n'
            f'  <path d="M {tx+topic_tile_w-topic_tile_h*0.24:.2f} {ty+0.65:.2f} Q {tx+topic_tile_w-0.65:.2f} {ty+0.65:.2f} {tx+topic_tile_w-0.65:.2f} {ty+topic_tile_h*0.24:.2f} V {ty+topic_tile_h-topic_tile_h*0.24:.2f} Q {tx+topic_tile_w-0.65:.2f} {ty+topic_tile_h-0.65:.2f} {tx+topic_tile_w-topic_tile_h*0.24:.2f} {ty+topic_tile_h-0.65:.2f}" fill="none" stroke="{RED}" stroke-opacity="0.24" stroke-width="0.75" filter="url(#tileGlow)"/>\n'
            f'  {_topic_glyph(key, gcx, gcy, gsize*0.94, icon_sw, RED)}\n'
            f'  <line x1="{div_x:.2f}" y1="{ty+topic_tile_h*0.28:.2f}" x2="{div_x:.2f}" y2="{ty+topic_tile_h*0.72:.2f}" stroke="{RED}" stroke-opacity="0.38" stroke-width="1.05"/>\n'
            f'  <text x="{lab_x:.2f}" y="{ty+topic_tile_h*0.61:.2f}" font-family="system-ui, -apple-system, sans-serif" font-size="{lab_size:.2f}" font-weight="460" fill="#dddddd">{lbl}</text>\n'
        )

    footer_top_r = width * 0.030
    footer_path = (
        f'M {frame_x:.2f} {footer_y+footer_top_r:.2f} '
        f'Q {frame_x:.2f} {footer_y:.2f} {frame_x+footer_top_r:.2f} {footer_y:.2f} '
        f'H {frame_x+frame_w-footer_top_r:.2f} '
        f'Q {frame_x+frame_w:.2f} {footer_y:.2f} {frame_x+frame_w:.2f} {footer_y+footer_top_r:.2f} '
        f'V {frame_y+frame_h-corner:.2f} '
        f'A {corner:.2f} {corner:.2f} 0 0 1 {frame_x+frame_w-corner:.2f} {frame_y+frame_h:.2f} '
        f'H {frame_x+corner:.2f} A {corner:.2f} {corner:.2f} 0 0 1 {frame_x:.2f} {frame_y+frame_h-corner:.2f} Z'
    )
    footer_edge_path = (
        f'M {frame_x:.2f} {footer_y + footer_h*0.22:.2f} V {frame_y+frame_h-corner:.2f} '
        f'A {corner:.2f} {corner:.2f} 0 0 0 {frame_x+corner:.2f} {frame_y+frame_h:.2f} '
        f'H {frame_x+frame_w-corner:.2f} A {corner:.2f} {corner:.2f} 0 0 0 {frame_x+frame_w:.2f} {frame_y+frame_h-corner:.2f} '
        f'V {footer_y + footer_h*0.22:.2f}'
    )
    accent_w = frame_w * 0.60
    accent_x = width / 2 - accent_w / 2
    p.append(
        f'  <path d="{footer_path}" fill="url(#footerPanelGrad)"/>\n'
        f'  <ellipse cx="{width/2:.2f}" cy="{footer_y:.2f}" rx="{frame_w*0.46:.2f}" ry="{footer_h*0.24:.2f}" fill="url(#footerTopGlow)"/>\n'
        f'  <rect x="{accent_x:.2f}" y="{footer_y-6:.2f}" width="{accent_w:.2f}" height="12" rx="6" fill="url(#footerAccent)" filter="url(#accentGlow)"/>\n'
        f'  <rect x="{accent_x:.2f}" y="{footer_y-1.1:.2f}" width="{accent_w:.2f}" height="2.2" rx="1.1" fill="url(#footerAccent)"/>\n'
        f'  <path d="{footer_edge_path}" fill="none" stroke="#9A141B" stroke-opacity="0.55" stroke-width="1.35" filter="url(#frameGlow)"/>\n'
    )
    if logo_uri:
        crop_x, crop_y, crop_w, crop_h = LOGO_CROP_VIEWBOX
        p.append(
            f'  <svg x="{logo_x:.2f}" y="{logo_y:.2f}" width="{logo_w_final:.2f}" height="{logo_h_final:.2f}" viewBox="{crop_x} {crop_y} {crop_w} {crop_h}" preserveAspectRatio="xMidYMid meet" overflow="hidden">\n'
            f'    <image x="0" y="0" width="{logo_w:.2f}" height="{logo_h:.2f}" href="{logo_uri}" xlink:href="{logo_uri}" preserveAspectRatio="none"/>\n'
            f'  </svg>\n'
        )
    else:
        p.append(
            f'  <text x="{width/2:.2f}" y="{footer_y + footer_h*0.62:.2f}" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-size="{min(unit*0.08,64):.2f}" font-weight="700"><tspan fill="white">FREE</tspan><tspan fill="{RED}">GYM</tspan></text>\n'
        )

    p.append(
        f'  <rect x="{frame_x+2:.2f}" y="{frame_y+2:.2f}" width="{frame_w-4:.2f}" height="{frame_h-4:.2f}" rx="{corner-0.75:.2f}" fill="none" stroke="#8E1219" stroke-opacity="0.28" stroke-width="7" filter="url(#frameGlow)"/>\n'
        f'  <rect x="{frame_x+2.25:.2f}" y="{frame_y+2.25:.2f}" width="{frame_w-4.5:.2f}" height="{frame_h-4.5:.2f}" rx="{corner-1:.2f}" fill="none" stroke="{RED}" stroke-opacity="0.68" stroke-width="1.4"/>\n'
    )
    p.append('</svg>')
    return ''.join(p)

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
    if size_label in MODERN_SIZES and github in MODERN_HANDLES:
        return generate_card_reference(
            github=github,
            display_name=display_name,
            badge_type=badge_type,
            topics=topics,
            citations=citations,
            files=files,
            last_active=last_active,
            commits=commits,
            size_label=size_label,
            avatar_data_uri=avatar_data_uri,
            logo_data=logo_data,
        )
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
    display_topics = [TOPIC_LABELS.get(t, t.replace('-', ' ').title()) for t in normalize_topics(topics)]
    top_topics = display_topics[:10] if display_topics else []
    topics_tokens = top_topics[:] if top_topics else []
    if display_topics and len(display_topics) > 10:
        topics_tokens.append(f'+{len(display_topics) - len(top_topics)} more')
    if not topics_tokens:
        topics_tokens = ['No topics yet']

    # Each topic on its own line for the left column
    topics_lines = topics_tokens[:]

    # Format contributions as a simple count
    contributions_count = len(files) if files else 0
    contributions_display = format_number(contributions_count)

    commits_value = commits if commits is not None else 0
    citations_display = format_number(citations if citations is not None else 0)
    commits_display = format_number(commits_value)
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
      <stop offset="0%" style="stop-color:#060606;stop-opacity:1" />
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
  <text x="{right_x:.2f}" y="{right2_value_y:.2f}" font-family="system-ui, -apple-system, sans-serif" font-size="{value_size:.2f}" fill="white">{citations_display}</text>

  <text x="{right_x:.2f}" y="{right3_label_y:.2f}" font-family="system-ui, -apple-system, sans-serif" font-size="{label_size:.2f}" fill="#8a8a8a">COMMITS</text>
  <text x="{right_x:.2f}" y="{right3_value_y:.2f}" font-family="system-ui, -apple-system, sans-serif" font-size="{value_size:.2f}" fill="white">{commits_display}</text>

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


def generate_communicator_card(
    github,
    name,
    topics,
    verified_since,
    size_label='default',
    avatar_data_uri=None,
    logo_data=None,
):
    """Generate an SVG card for a verified communicator.

    Communicators are vetted public communicators of FreeGym Wiki content.
    The card composition deliberately differs from the contributor card:
    centered avatar + name, mission line, topic typography (no badges),
    FreeGym logo footer, and a "Verified by FreeGym" stamp instead of
    the contributor stats panel.
    """
    width, height = CARD_SIZES[size_label]
    unit = min(width, height)
    margin = unit * 0.06
    is_wide = width > height
    is_tall = height >= width * 1.4  # story format needs vertical redistribution

    # ── Footer band ──────────────────────────────────────────────────
    footer_h = max(height * 0.17, 145)
    footer_y = height - footer_h

    logo_uri, logo_w, logo_h = (logo_data or (None, None, None))
    if logo_uri and logo_w and logo_h:
        logo_aspect = logo_w / logo_h
        logo_w_max = width * 0.75
        logo_h_cap = footer_h * 0.72
        logo_w_final = logo_w_max
        logo_h_final = logo_w_final / logo_aspect
        if logo_h_final > logo_h_cap:
            logo_h_final = logo_h_cap
            logo_w_final = logo_h_final * logo_aspect
        logo_x = (width - logo_w_final) / 2
        logo_y = footer_y + footer_h * 0.10
    else:
        logo_x = logo_y = logo_w_final = logo_h_final = 0

    auth_size = max(unit * 0.018, 14)
    auth_y_offset = footer_h * 0.13

    # ── Avatar ───────────────────────────────────────────────────────
    if is_wide:
        avatar_d = min(unit * 0.40, 250)
    elif is_tall:
        avatar_d = min(unit * 0.27, 290)
    else:
        avatar_d = min(unit * 0.24, 260)
    avatar_r = avatar_d / 2

    if is_wide:
        avatar_cx = margin + avatar_r + unit * 0.04
        avatar_cy = height / 2
    elif is_tall:
        avatar_cx = width / 2
        avatar_cy = height * 0.18
    else:
        avatar_cx = width / 2
        avatar_cy = margin + avatar_r + unit * 0.015

    ring_stroke_w = max(unit * 0.0025, 1.5)
    ring_color = '#3a3a3a'

    # Verification glyph: red filled circle with white checkmark, bottom-right of avatar
    glyph_r = avatar_r * 0.27
    glyph_cx = avatar_cx + avatar_r * 0.72
    glyph_cy = avatar_cy + avatar_r * 0.72
    check_size = glyph_r * 0.95
    cx1 = glyph_cx - check_size * 0.40
    cy1 = glyph_cy + check_size * 0.05
    cx2 = glyph_cx - check_size * 0.05
    cy2 = glyph_cy + check_size * 0.32
    cx3 = glyph_cx + check_size * 0.42
    cy3 = glyph_cy - check_size * 0.32
    glyph_stroke_w = glyph_r * 0.18

    # ── Name + handle + role label ───────────────────────────────────
    if is_wide:
        text_x_anchor = avatar_cx + avatar_r + unit * 0.06
        text_align = 'start'
        name_size = min(unit * 0.085, 54)
        name_y = height * 0.30
    else:
        text_x_anchor = width / 2
        text_align = 'middle'
        name_size = min(unit * 0.075, 82)
        name_y = avatar_cy + avatar_r + unit * 0.075

    handle_size = name_size * 0.36
    role_size = name_size * 0.24
    if is_wide:
        handle_y = name_y + handle_size * 2.4
        role_y = handle_y + role_size * 2.4
    else:
        handle_y = name_y + handle_size * 1.7
        role_y = handle_y + role_size * 1.9

    # ── Mission pull-quote ───────────────────────────────────────────
    if is_wide:
        mission_size = min(unit * 0.045, 26)
        mission_y = role_y + mission_size * 2.0
        mission_x = text_x_anchor
        mission_anchor = 'start'
    elif is_tall:
        mission_size = min(unit * 0.050, 54)
        mission_y = height * 0.50
        mission_x = width / 2
        mission_anchor = 'middle'
    else:
        mission_size = min(unit * 0.046, 48)
        mission_y = role_y + mission_size * 2.4
        mission_x = width / 2
        mission_anchor = 'middle'

    # ── Topics as typography (no badges) ─────────────────────────────
    visible = list(normalize_topics(topics))

    if is_wide:
        topic_size = min(unit * 0.034, 22)
        topic_x = text_x_anchor
        topic_anchor = 'start'
    elif is_tall:
        topic_size = min(unit * 0.028, 34)
        topic_x = width / 2
        topic_anchor = 'middle'
    else:
        topic_size = min(unit * 0.028, 30)
        topic_x = width / 2
        topic_anchor = 'middle'

    if is_wide:
        topic_max_width = width - topic_x - margin
    else:
        topic_max_width = width - (margin * 2)
    topic_max_chars = max(24, int(topic_max_width / (topic_size * 0.56)))
    chunks = chunk_topics(visible, max_chars=topic_max_chars)

    if is_tall:
        topic_block_top = height * 0.68
        topic_line_height = topic_size * 1.9
    elif is_wide:
        topic_block_top = mission_y + mission_size * 3.3
        topic_line_height = topic_size * 1.95
    else:
        topic_block_top = mission_y + mission_size * 2.0
        topic_line_height = topic_size * 1.7

    topic_label_size = max(unit * 0.014, 11)
    if is_wide:
        topic_label_y = topic_block_top - topic_size * 1.8
    else:
        topic_label_y = topic_block_top - topic_size * 1.4

    # ── Build SVG ────────────────────────────────────────────────────
    avatar_url = avatar_data_uri or f"https://github.com/{github}.png?size=400"

    parts = []
    parts.append(f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#060606;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#1a1a1a;stop-opacity:1"/>
    </linearGradient>
    <radialGradient id="glow" cx="88%" cy="12%" r="55%">
      <stop offset="0%" style="stop-color:#E10600;stop-opacity:0.13"/>
      <stop offset="100%" style="stop-color:#2A0305;stop-opacity:0"/>
    </radialGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-opacity="0.3"/>
    </filter>
    <clipPath id="avatar-clip">
      <circle cx="{avatar_cx}" cy="{avatar_cy}" r="{avatar_r}"/>
    </clipPath>
  </defs>

  <!-- background -->
  <rect width="{width}" height="{height}" rx="{unit * 0.04:.2f}" fill="url(#bg)" filter="url(#shadow)"/>
  <rect width="{width}" height="{height}" rx="{unit * 0.04:.2f}" fill="url(#glow)"/>
  <rect width="{width}" height="{max(unit * 0.008, 5):.2f}" fill="#E10600"/>

  <!-- avatar -->
  <circle cx="{avatar_cx:.2f}" cy="{avatar_cy:.2f}" r="{avatar_r:.2f}" fill="#111111"/>
  <image x="{avatar_cx - avatar_r:.2f}" y="{avatar_cy - avatar_r:.2f}" width="{avatar_d:.2f}" height="{avatar_d:.2f}" href="{avatar_url}" clip-path="url(#avatar-clip)" preserveAspectRatio="xMidYMid slice"/>
  <circle cx="{avatar_cx:.2f}" cy="{avatar_cy:.2f}" r="{avatar_r:.2f}" fill="none" stroke="{ring_color}" stroke-width="{ring_stroke_w:.2f}"/>

  <!-- verification glyph -->
  <circle cx="{glyph_cx:.2f}" cy="{glyph_cy:.2f}" r="{glyph_r:.2f}" fill="#E10600" stroke="#0b0b0b" stroke-width="{max(unit * 0.005, 2.5):.2f}"/>
  <polyline points="{cx1:.2f},{cy1:.2f} {cx2:.2f},{cy2:.2f} {cx3:.2f},{cy3:.2f}" fill="none" stroke="#ffffff" stroke-width="{glyph_stroke_w:.2f}" stroke-linecap="round" stroke-linejoin="round"/>

  <!-- name + handle + role -->
  <text x="{text_x_anchor:.2f}" y="{name_y:.2f}" text-anchor="{text_align}" font-family="system-ui, -apple-system, sans-serif" font-size="{name_size:.2f}" font-weight="700" fill="#ffffff" letter-spacing="-1">{name or github}</text>
  <text x="{text_x_anchor:.2f}" y="{handle_y:.2f}" text-anchor="{text_align}" font-family="system-ui, -apple-system, sans-serif" font-size="{handle_size:.2f}" fill="#7a7a7a">@{github}</text>
  <text x="{text_x_anchor:.2f}" y="{role_y:.2f}" text-anchor="{text_align}" font-family="system-ui, -apple-system, sans-serif" font-size="{role_size:.2f}" font-weight="500" fill="#E10600" letter-spacing="5">VERIFIED COMMUNICATOR</text>

  <!-- mission line — modern, minimal -->
  <text x="{mission_x:.2f}" y="{mission_y:.2f}" text-anchor="{mission_anchor}" font-family="'Inter', 'Helvetica Neue', system-ui, -apple-system, sans-serif" font-weight="300" font-size="{mission_size:.2f}" fill="#ededed" letter-spacing="-0.5">{COMMUNICATOR_MISSION}</text>

  <!-- topic label -->
  <text x="{topic_x:.2f}" y="{topic_label_y:.2f}" text-anchor="{topic_anchor}" font-family="system-ui, -apple-system, sans-serif" font-size="{topic_label_size:.2f}" font-weight="600" fill="#5a5a5a" letter-spacing="4">COMMUNICATES ON</text>
''')

    for line_idx, chunk in enumerate(chunks):
        line_y = topic_block_top + line_idx * topic_line_height
        line_text = '  ·  '.join(label_topic(t) for t in chunk)
        parts.append(f'''  <text x="{topic_x:.2f}" y="{line_y:.2f}" text-anchor="{topic_anchor}" font-family="system-ui, -apple-system, sans-serif" font-size="{topic_size:.2f}" font-weight="500" fill="#cccccc">{line_text}</text>
''')

    parts.append(f'''  <rect x="0" y="{footer_y:.2f}" width="{width}" height="{footer_h:.2f}" rx="0" fill="#000000"/>
  <line x1="{margin:.2f}" y1="{footer_y:.2f}" x2="{width - margin:.2f}" y2="{footer_y:.2f}" stroke="#1f1f1f" stroke-width="1"/>
''')

    if logo_uri:
        parts.append(f'''  <image x="{logo_x:.2f}" y="{logo_y:.2f}" width="{logo_w_final:.2f}" height="{logo_h_final:.2f}" href="{logo_uri}" xlink:href="{logo_uri}" preserveAspectRatio="xMidYMid meet"/>
''')
    else:
        parts.append(f'''  <text x="{width / 2:.2f}" y="{footer_y + footer_h * 0.55:.2f}" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-size="{min(unit * 0.075, 60):.2f}" font-weight="700">
    <tspan fill="white">FREE</tspan><tspan fill="#E10600">GYM</tspan>
  </text>
''')

    parts.append(f'''  <text x="{width / 2:.2f}" y="{footer_y + footer_h - auth_y_offset:.2f}" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-size="{auth_size:.2f}" fill="#666666" letter-spacing="3">VERIFIED BY FREEGYM &#x00B7; SINCE {format_verified_since(verified_since).upper()}</text>
</svg>''')

    return ''.join(parts)


def main():
    os.makedirs('cards', exist_ok=True)

    with open('contributors.yaml', 'r') as f:
        data = yaml.safe_load(f)

    logo_data = load_logo_data()

    all_contributors = []

    # Maintainers
    for m in data.get('maintainers', []):
        topics = normalize_topics(list(m.get('topics', []) or []))
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
                'topics': normalize_topics(t.get('topics', [])),
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
                'topics': normalize_topics(c.get('topics', [])),
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

    # Communicators — separate role with its own card design.
    # Maintainer-curated; not auto-tracked from PR activity. Cards are emitted
    # to cards/<handle>-communicator{,-portrait,-story,-wide}.svg so they don't
    # collide with contributor card filenames if the same handle ever appears
    # in both lists.
    communicators = data.get('communicators') or []
    for comm in communicators:
        if not isinstance(comm, dict) or not comm.get('github'):
            continue
        github = comm.get('github', '')
        name = comm.get('name', github)
        topics = comm.get('verified_topics') or comm.get('topics') or []
        verified_since = comm.get('verified_since', '-')

        avatar_data_uri = fetch_avatar_base64(github)

        for size_label in CARD_SIZES:
            svg = generate_communicator_card(
                github=github,
                name=name,
                topics=topics,
                verified_since=verified_since,
                size_label=size_label,
                avatar_data_uri=avatar_data_uri,
                logo_data=logo_data,
            )

            suffix = '' if size_label == 'default' else f'-{size_label}'
            svg_path = f"cards/{github}-communicator{suffix}.svg"
            png_path = f"cards/{github}-communicator{suffix}.png"

            with open(svg_path, 'w', encoding='utf-8') as f:
                f.write(svg)
            print(f"Generated {svg_path}")

            if HAS_CAIROSVG:
                try:
                    cairosvg.svg2png(bytestring=svg.encode('utf-8'), write_to=png_path, scale=2)
                    print(f"Generated {png_path}")
                except Exception as e:
                    print(f"Warning: Could not generate PNG for {png_path}: {e}")


if __name__ == '__main__':
    main()
