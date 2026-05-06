#!/usr/bin/env python3
"""Generate a static contributor site from contributors.yaml."""

import datetime
import html
import os
import shutil
from pathlib import Path

import yaml

BASE_DIR = Path(__file__).resolve().parent
REPO_ROOT = BASE_DIR.parent.parent
SITE_DIR = REPO_ROOT / 'site'
SITE_SRC = REPO_ROOT / 'site-src'
CONTRIB_DIR = SITE_DIR / 'contributors'
COMMUNICATORS_DIR = SITE_DIR / 'communicators'
CARDS_SRC = REPO_ROOT / 'cards'
CARDS_DEST = SITE_DIR / 'cards'

CHANNEL_LABELS = {
    'freegym': 'FreeGym',
    'youtube': 'YouTube',
    'instagram': 'Instagram',
    'twitter': 'Twitter',
    'x': 'X',
    'linkedin': 'LinkedIn',
    'tiktok': 'TikTok',
    'podcast': 'Podcast',
    'website': 'Website',
}

REPO_URL = os.getenv('REPO_URL', 'https://github.com/FreeGym/FreeGym-Wiki')
RAW_BASE = os.getenv('RAW_BASE', 'https://raw.githubusercontent.com/FreeGym/FreeGym-Wiki/main')
SITE_BASE_URL = os.getenv('SITE_BASE_URL', 'https://freegym.github.io/FreeGym-Wiki').rstrip('/')
BUILD_STAMP = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')

TOPIC_ALIASES = {
    'heart-health': 'cardiology',
}
TOPIC_LABELS = {
    'nutrition': 'Nutrition',
    'exercise-physiology': 'Exercise Physiology',
    'pharmacology': 'Pharmacology',
    'biomarkers': 'Biomarkers',
    'wearables': 'Wearables',
    'musculoskeletal-health': 'Musculoskeletal',
    'exercise': 'Fitness',
    'sleep': 'Sleep',
    'mental-health': 'Mental Health',
    'supplements': 'Supplements',
    'recovery': 'Recovery',
    'biomechanics': 'Biomechanics',
    'cardiology': 'Cardiology',
    'Womens-Health': "Women's Health",
}

TOPIC_ORDER = [
    'nutrition',
    'exercise-physiology',
    'pharmacology',
    'cardiology',
    'Womens-Health',
    'exercise',
    'sleep',
    'mental-health',
    'supplements',
    'recovery',
    'biomechanics',
]


def normalize_topic(topic):
    return TOPIC_ALIASES.get(topic, topic)


def normalize_topics(topics):
    normalized = []
    seen = set()
    for topic in topics or []:
        canonical = normalize_topic(topic)
        if canonical and canonical not in seen:
            seen.add(canonical)
            normalized.append(canonical)
    return normalized


def label_topic(topic):
    canonical = normalize_topic(topic)
    return TOPIC_LABELS.get(canonical, canonical.replace('-', ' ').title())


def esc(value):
    return html.escape(str(value))


def format_number(value):
    try:
        return f"{int(value):,}"
    except (TypeError, ValueError):
        return str(value)


def format_verified_since(ym):
    """'2026-05' -> 'May 2026'. Returns the input on parse failure."""
    months = ['', 'January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    try:
        y, m = ym.split('-', 1)
        return f"{months[int(m)]} {int(y)}"
    except Exception:
        return ym or '-'


def read_data():
    with open(REPO_ROOT / 'contributors.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def collect_profiles(data):
    profiles = []
    topic_keys = set()

    def add_profile(entry, role):
        github = entry.get('github', '')
        name = entry.get('name') or github
        topics = normalize_topics(entry.get('topics', []) or [])
        contributions = entry.get('contributions', []) or []
        citations = entry.get('total_citations', 0)
        commits = entry.get('commits', 0)
        last_active = entry.get('last_active', '-')
        prs_merged = entry.get('prs_merged', 0)

        topic_keys.update(topics)

        profiles.append({
            'github': github,
            'name': name,
            'role': role,
            'topics': topics,
            'topic_labels': [label_topic(t) for t in topics],
            'contributions': contributions,
            'contribution_count': len(contributions),
            'citations': citations,
            'commits': commits,
            'last_active': last_active,
            'prs_merged': prs_merged,
        })

    for m in data.get('maintainers', []):
        add_profile(m, 'maintainer')

    for t in data.get('trusted', []) or []:
        if isinstance(t, dict):
            add_profile(t, 'trusted')

    for c in data.get('contributors', []) or []:
        if isinstance(c, dict) and c.get('checkmark'):
            add_profile(c, 'verified')

    return profiles, topic_keys


def sort_profiles(profiles):
    role_priority = {'maintainer': 0, 'trusted': 1, 'verified': 2}
    return sorted(
        profiles,
        key=lambda p: (role_priority.get(p['role'], 9), p['name'].lower())
    )


def collect_communicators(data):
    """Build a list of communicator profile dicts from contributors.yaml.

    Communicators are a separate role tier from contributors — maintainer-curated,
    no commit/citation history, just verified topic authorization.
    """
    communicators = []
    for entry in data.get('communicators') or []:
        if not isinstance(entry, dict) or not entry.get('github'):
            continue
        github = entry.get('github', '')
        topics = normalize_topics(entry.get('verified_topics') or entry.get('topics') or [])
        channels = entry.get('channels') or {}
        # Filter out channels with empty values; preserve insertion order
        channels = {k: v for k, v in channels.items() if v}
        communicators.append({
            'github': github,
            'name': entry.get('name') or github,
            'topics': topics,
            'topic_labels': [label_topic(t) for t in topics],
            'verified_since': entry.get('verified_since', '-'),
            'channels': channels,
        })
    return sorted(communicators, key=lambda c: c['name'].lower())


def build_topic_filters(topic_keys):
    ordered = []
    remaining = set(topic_keys)
    for key in TOPIC_ORDER:
        if key in remaining:
            ordered.append(key)
            remaining.remove(key)
    ordered.extend(sorted(remaining))
    return ordered


def render_topics(topics):
    if not topics:
        return '<span class="chip">No topics yet</span>'
    return ''.join(f'<span class="chip">{esc(label_topic(t))}</span>' for t in topics)


def role_badge(role):
    if role == 'maintainer':
        return 'Maintainer'
    if role == 'trusted':
        return 'Trusted'
    return 'Verified'


def role_class(role):
    if role == 'maintainer':
        return 'maintainer'
    if role == 'trusted':
        return 'trusted'
    return 'verified'


def render_profile_card(profile):
    topics_attr = ','.join(profile['topics'])
    contributions = profile['contribution_count']

    return f'''
    <article class="profile-card reveal" data-profile data-name="{esc(profile['name'])}" data-handle="{esc(profile['github'])}" data-topics="{esc(topics_attr)}">
      <div class="card-top">
        <img class="avatar" src="https://github.com/{esc(profile['github'])}.png?size=200" alt="{esc(profile['name'])} avatar">
        <div class="identity">
          <h3>{esc(profile['name'])}</h3>
          <p>@{esc(profile['github'])}</p>
        </div>
        <span class="role-badge {role_class(profile['role'])}">{role_badge(profile['role'])}</span>
      </div>
      <div class="stats">
        <div class="stat"><span>Citations</span><strong>{format_number(profile['citations'])}</strong></div>
        <div class="stat"><span>Contributions</span><strong>{format_number(contributions)}</strong></div>
        <div class="stat"><span>Commits</span><strong>{format_number(profile['commits'])}</strong></div>
        <div class="stat"><span>Last Active</span><strong>{esc(profile['last_active'])}</strong></div>
      </div>
      <div class="topic-row">{render_topics(profile['topics'])}</div>
      <a class="card-link" href="contributors/{esc(profile['github'])}/">View profile</a>
    </article>
    '''


def render_communicator_homepage_card(comm):
    """Compact homepage card for a communicator. Reuses existing CSS classes."""
    topics_attr = ','.join(comm['topics'])
    topic_count = len(comm['topics'])

    return f'''
    <article class="profile-card reveal" data-profile data-name="{esc(comm['name'])}" data-handle="{esc(comm['github'])}" data-topics="{esc(topics_attr)}">
      <div class="card-top">
        <img class="avatar" src="https://github.com/{esc(comm['github'])}.png?size=200" alt="{esc(comm['name'])} avatar">
        <div class="identity">
          <h3>{esc(comm['name'])}</h3>
          <p>@{esc(comm['github'])}</p>
        </div>
        <span class="role-badge verified">Verified Communicator</span>
      </div>
      <div class="stats">
        <div class="stat"><span>Verified Since</span><strong>{esc(format_verified_since(comm['verified_since']))}</strong></div>
        <div class="stat"><span>Topics</span><strong>{format_number(topic_count)}</strong></div>
        <div class="stat"><span>Verified By</span><strong>FreeGym</strong></div>
      </div>
      <div class="topic-row">{render_topics(comm['topics'])}</div>
      <a class="card-link" href="communicators/{esc(comm['github'])}/">View profile</a>
    </article>
    '''


def render_index(profiles, communicators, topics, stats):
    topic_buttons = ['<button class="filter-chip active" data-topic="all">All topics</button>']
    for key in topics:
        topic_buttons.append(
            f'<button class="filter-chip" data-topic="{esc(key)}">{esc(label_topic(key))}</button>'
        )

    cards_html = '\n'.join(render_profile_card(p) for p in profiles)

    if communicators:
        communicator_cards_html = '\n'.join(render_communicator_homepage_card(c) for c in communicators)
        communicator_section = f'''
    <section class="reveal" style="margin-top: 4rem;">
      <h2 style="margin-bottom: 0.5rem;">Verified Communicators</h2>
      <p style="opacity: 0.7; margin-bottom: 1.5rem;">Vetted public communicators of FreeGym Wiki articles.</p>
      <section class="profile-grid">
        {communicator_cards_html}
      </section>
    </section>
'''
    else:
        communicator_section = ''

    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>FreeGym Wiki Profiles</title>
  <meta name="description" content="Verified contributors to the FreeGym Wiki and their evidence based track records.">
  <meta property="og:title" content="FreeGym Wiki Profiles">
  <meta property="og:description" content="Verified contributors to the FreeGym Wiki and their evidence based track records.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{SITE_BASE_URL}/">
  <meta property="og:image" content="{RAW_BASE}/cards/mutant1643.svg?v={BUILD_STAMP}">
  <link rel="stylesheet" href="assets/styles.css">
</head>
<body>
  <header class="site-header">
    <div class="brand"><span class="dot"></span>FreeGym Wiki</div>
    <nav class="nav-links">
      <a href="{REPO_URL}">GitHub</a>
      <a href="{REPO_URL}/blob/main/CONTRIBUTING.md">Contribute</a>
      <a href="{REPO_URL}/blob/main/VERIFICATION.md">Verification</a>
    </nav>
  </header>

  <main class="page">
    <section class="hero reveal">
      <div>
        <div class="eyebrow">Verification directory</div>
        <h1>This repo exists so health claims are backed by sources, not followers or algorithms.</h1>
        <p>These profiles summarize evidence based contributions to the FreeGym Wiki. No follower counts, no credentials, just the work.</p>
        <div class="hero-actions">
          <a class="button primary" href="{REPO_URL}">View repo</a>
          <a class="button ghost" href="{REPO_URL}/issues">Open a debate</a>
        </div>
      </div>
      <div class="hero-panel">
        <div class="stat"><span>Verified profiles</span><strong>{format_number(stats['verified'])}</strong></div>
        <div class="stat"><span>Total citations</span><strong>{format_number(stats['citations'])}</strong></div>
        <div class="stat"><span>Active topics</span><strong>{format_number(stats['topics'])}</strong></div>
      </div>
    </section>

    <section class="filters reveal">
      <div class="search-box">
        <input data-search type="search" placeholder="Search by name or handle">
      </div>
      <div class="topic-filters">
        {''.join(topic_buttons)}
      </div>
      <div class="results-bar" data-results>0 profiles</div>
    </section>

    <section class="reveal" style="margin-top: 1rem;">
      <h2 style="margin-bottom: 0.5rem;">Verified Contributors</h2>
      <p style="opacity: 0.7; margin-bottom: 1.5rem;">Authors and editors of FreeGym Wiki articles.</p>
      <section class="profile-grid">
        {cards_html}
      </section>
    </section>
{communicator_section}
    <div class="footer">Generated from contributors.yaml. Last updated {stats['updated']}.</div>
  </main>

  <script src="assets/app.js"></script>
</body>
</html>
'''


def render_contributions(contributions):
    if not contributions:
        return '<div class="contribution-item">No recorded contributions yet.</div>'

    items = []
    for item in contributions:
        file_path = item.get('file', '-')
        file_name = file_path.split('/')[-1]
        ctype = item.get('type', 'edit')
        citations_added = item.get('citations_added', 0)
        pr_number = item.get('pr')

        pr_link = ''
        if pr_number:
            pr_link = f' | PR <a href="{REPO_URL}/pull/{pr_number}">#{pr_number}</a>'

        items.append(
            f'''<div class="contribution-item">
  <a href="{REPO_URL}/blob/main/{file_path}">{esc(file_name)}</a>
  <div class="contribution-meta">
    <span>Type: {esc(ctype)}</span>
    <span>Citations added: {format_number(citations_added)}</span>
    <span>File: {esc(file_path)}{pr_link}</span>
  </div>
</div>'''
        )
    return '\n'.join(items)


def render_profile(profile):
    contributions = profile['contribution_count']
    profile_url = f"{SITE_BASE_URL}/contributors/{profile['github']}/"
    card_url = f"{RAW_BASE}/cards/{profile['github']}-portrait.png?v={BUILD_STAMP}"
    card_local = f"../../cards/{profile['github']}-portrait.png?v={BUILD_STAMP}"

    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(profile['name'])} - FreeGym Wiki</title>
  <meta name="description" content="FreeGym Wiki profile for {esc(profile['name'])} (@{esc(profile['github'])}).">
  <meta property="og:title" content="{esc(profile['name'])} - FreeGym Wiki">
  <meta property="og:description" content="Evidence based contributions and verification status.">
  <meta property="og:type" content="profile">
  <meta property="og:url" content="{profile_url}">
  <meta property="og:image" content="{card_url}">
  <link rel="stylesheet" href="../../assets/styles.css">
</head>
<body>
  <header class="site-header">
    <div class="brand"><span class="dot"></span>FreeGym Wiki</div>
    <nav class="nav-links">
      <a href="../../index.html">Directory</a>
      <a href="{REPO_URL}">GitHub</a>
      <a href="{REPO_URL}/blob/main/VERIFICATION.md">Verification</a>
    </nav>
  </header>

  <main class="page">
    <section class="profile-hero reveal">
      <div class="profile-panel">
        <img class="avatar" src="https://github.com/{esc(profile['github'])}.png?size=200" alt="{esc(profile['name'])} avatar">
        <h1>{esc(profile['name'])}</h1>
        <div class="handle">@{esc(profile['github'])}</div>
        <div class="role-badge {role_class(profile['role'])}" style="margin-top: 0.75rem; display: inline-flex;">{role_badge(profile['role'])}</div>
        <div class="topic-row">{render_topics(profile['topics'])}</div>
        <div class="stats">
          <div class="stat"><span>Citations</span><strong>{format_number(profile['citations'])}</strong></div>
          <div class="stat"><span>Contributions</span><strong>{format_number(contributions)}</strong></div>
          <div class="stat"><span>Commits</span><strong>{format_number(profile['commits'])}</strong></div>
          <div class="stat"><span>Last Active</span><strong>{esc(profile['last_active'])}</strong></div>
        </div>
      </div>
      <div class="profile-card-preview">
        <img src="{card_local}" alt="{esc(profile['name'])} card preview">
      </div>
    </section>

    <section class="section reveal">
      <h2>Contributions</h2>
      <div class="contribution-list">
        {render_contributions(profile['contributions'])}
      </div>
    </section>

    <div class="footer">Profile data from contributors.yaml. Last updated {datetime.date.today().isoformat()}.</div>
  </main>

  <script src="../../assets/app.js"></script>
</body>
</html>
'''


def render_channel_links(channels):
    """Render channel links as an unordered list. Returns empty string if none."""
    if not channels:
        return ''
    items = []
    for key, value in channels.items():
        label = CHANNEL_LABELS.get(key, key.title())
        href = value if value.startswith(('http://', 'https://')) else f'https://{value}'
        items.append(f'<li><a href="{esc(href)}" rel="noopener" target="_blank">{esc(label)}</a></li>')
    return '<ul class="channels">' + ''.join(items) + '</ul>'


def render_communicator_profile(comm):
    """Render the per-communicator HTML profile page."""
    handle = comm['github']
    profile_url = f"{SITE_BASE_URL}/communicators/{handle}/"
    card_url = f"{RAW_BASE}/cards/{handle}-communicator-portrait.png?v={BUILD_STAMP}"
    card_local = f"../../cards/{handle}-communicator-portrait.png?v={BUILD_STAMP}"

    topics_inline = ', '.join(comm['topic_labels']) if comm['topic_labels'] else 'multiple topics'

    channels_section = ''
    if comm['channels']:
        channels_section = f'''
    <section class="section reveal">
      <h2>Find {esc(comm['name'])} on</h2>
      {render_channel_links(comm['channels'])}
    </section>
'''

    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(comm['name'])} - FreeGym Wiki Communicator</title>
  <meta name="description" content="Verified Communicator on FreeGym Wiki — {esc(comm['name'])} (@{esc(handle)}) communicates on {esc(topics_inline)}.">
  <meta property="og:title" content="{esc(comm['name'])} - FreeGym Wiki Communicator">
  <meta property="og:description" content="Verified Communicator on FreeGym Wiki — communicates on {esc(topics_inline)}.">
  <meta property="og:type" content="profile">
  <meta property="og:url" content="{profile_url}">
  <meta property="og:image" content="{card_url}">
  <link rel="stylesheet" href="../../assets/styles.css">
</head>
<body>
  <header class="site-header">
    <div class="brand"><span class="dot"></span>FreeGym Wiki</div>
    <nav class="nav-links">
      <a href="../../index.html">Directory</a>
      <a href="{REPO_URL}">GitHub</a>
      <a href="{REPO_URL}/blob/main/VERIFICATION.md">Verification</a>
    </nav>
  </header>

  <main class="page">
    <section class="profile-hero reveal">
      <div class="profile-panel">
        <img class="avatar" src="https://github.com/{esc(handle)}.png?size=200" alt="{esc(comm['name'])} avatar">
        <h1>{esc(comm['name'])}</h1>
        <div class="handle">@{esc(handle)}</div>
        <div class="role-badge verified" style="margin-top: 0.75rem; display: inline-flex;">Verified Communicator</div>
        <div class="topic-row">{render_topics(comm['topics'])}</div>
        <div class="stats">
          <div class="stat"><span>Verified Since</span><strong>{esc(format_verified_since(comm['verified_since']))}</strong></div>
          <div class="stat"><span>Topics</span><strong>{format_number(len(comm['topics']))}</strong></div>
          <div class="stat"><span>Verified By</span><strong>FreeGym</strong></div>
        </div>
      </div>
      <div class="profile-card-preview">
        <img src="{card_local}" alt="{esc(comm['name'])} card preview">
      </div>
    </section>
{channels_section}
    <div class="footer">Profile data from contributors.yaml. Last updated {datetime.date.today().isoformat()}.</div>
  </main>

  <script src="../../assets/app.js"></script>
</body>
</html>
'''


def write_file(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def copy_static_assets():
    if not SITE_SRC.exists():
        return
    for item in SITE_SRC.iterdir():
        dest = SITE_DIR / item.name
        if item.is_dir():
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(item, dest)
        else:
            shutil.copy2(item, dest)


def copy_cards():
    if CARDS_SRC.exists():
        CARDS_DEST.mkdir(parents=True, exist_ok=True)
        for card in CARDS_SRC.glob('*.svg'):
            shutil.copy2(card, CARDS_DEST / card.name)
        for card in CARDS_SRC.glob('*.png'):
            shutil.copy2(card, CARDS_DEST / card.name)


def main():
    data = read_data()
    profiles, topic_keys = collect_profiles(data)
    profiles = sort_profiles(profiles)
    topics = build_topic_filters(topic_keys)

    communicators = collect_communicators(data)

    stats = {
        'verified': len(profiles),
        'citations': sum(p['citations'] for p in profiles),
        'topics': len(topic_keys),
        'updated': datetime.date.today().isoformat(),
    }

    SITE_DIR.mkdir(parents=True, exist_ok=True)
    CONTRIB_DIR.mkdir(parents=True, exist_ok=True)
    if communicators:
        COMMUNICATORS_DIR.mkdir(parents=True, exist_ok=True)

    copy_cards()
    copy_static_assets()

    # Ensure GitHub Pages serves all files.
    write_file(SITE_DIR / '.nojekyll', '')

    index_html = render_index(profiles, communicators, topics, stats)
    write_file(SITE_DIR / 'index.html', index_html)

    for profile in profiles:
        profile_html = render_profile(profile)
        write_file(CONTRIB_DIR / profile['github'] / 'index.html', profile_html)

    for comm in communicators:
        comm_html = render_communicator_profile(comm)
        write_file(COMMUNICATORS_DIR / comm['github'] / 'index.html', comm_html)

    print(f"Generated site for {len(profiles)} profiles, {len(communicators)} communicators")


if __name__ == '__main__':
    main()
