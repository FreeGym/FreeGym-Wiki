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
CARDS_SRC = REPO_ROOT / 'cards'
CARDS_DEST = SITE_DIR / 'cards'

REPO_URL = os.getenv('REPO_URL', 'https://github.com/FreeGym/FreeGym-Wiki')
RAW_BASE = os.getenv('RAW_BASE', 'https://raw.githubusercontent.com/FreeGym/FreeGym-Wiki/main')
SITE_BASE_URL = os.getenv('SITE_BASE_URL', 'https://freegym.github.io/FreeGym-Wiki').rstrip('/')

TOPIC_LABELS = {
    'nutrition': 'Nutrition',
    'exercise': 'Fitness',
    'sleep': 'Sleep',
    'mental-health': 'Mental Health',
    'supplements': 'Supplements',
    'recovery': 'Recovery',
    'biomechanics': 'Biomechanics',
    'core': 'Core',
    'governance': 'Governance',
}

TOPIC_ORDER = [
    'nutrition',
    'exercise',
    'sleep',
    'mental-health',
    'supplements',
    'recovery',
    'biomechanics',
    'core',
    'governance',
]


def label_topic(topic):
    return TOPIC_LABELS.get(topic, topic.replace('-', ' ').title())


def esc(value):
    return html.escape(str(value))


def read_data():
    with open(REPO_ROOT / 'contributors.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def collect_profiles(data):
    profiles = []
    topic_keys = set()

    def add_profile(entry, role):
        github = entry.get('github', '')
        name = entry.get('name') or github
        topics = entry.get('topics', []) or entry.get('specialty', []) or []
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
    contributions_label = 'contribution' if contributions == 1 else 'contributions'

    return f'''
    <article class="profile-card reveal" data-profile data-name="{esc(profile['name'])}" data-handle="{esc(profile['github'])}" data-topics="{esc(topics_attr)}">
      <div class="card-top">
        <div class="identity">
          <h3>{esc(profile['name'])}</h3>
          <p>@{esc(profile['github'])}</p>
        </div>
        <span class="role-badge {role_class(profile['role'])}">{role_badge(profile['role'])}</span>
      </div>
      <div class="stats">
        <div class="stat"><span>Citations</span><strong>{profile['citations']}</strong></div>
        <div class="stat"><span>Contributions</span><strong>{contributions} {contributions_label}</strong></div>
        <div class="stat"><span>Last Active</span><strong>{esc(profile['last_active'])}</strong></div>
      </div>
      <div class="topic-row">{render_topics(profile['topics'])}</div>
      <a class="card-link" href="contributors/{esc(profile['github'])}/">View profile</a>
    </article>
    '''


def render_index(profiles, topics, stats):
    topic_buttons = ['<button class="filter-chip active" data-topic="all">All topics</button>']
    for key in topics:
        topic_buttons.append(
            f'<button class="filter-chip" data-topic="{esc(key)}">{esc(label_topic(key))}</button>'
        )

    cards_html = '\n'.join(render_profile_card(p) for p in profiles)

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
  <meta property="og:image" content="{RAW_BASE}/cards/mutant1643.svg">
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
        <h1>Every checkmark is a public receipt.</h1>
        <p>These profiles summarize evidence based contributions to the FreeGym Wiki. No follower counts, no credentials, just the work.</p>
        <div class="hero-actions">
          <a class="button primary" href="{REPO_URL}">View repo</a>
          <a class="button ghost" href="{REPO_URL}/issues">Open a debate</a>
        </div>
      </div>
      <div class="hero-panel">
        <div class="stat"><span>Verified profiles</span><strong>{stats['verified']}</strong></div>
        <div class="stat"><span>Total citations</span><strong>{stats['citations']}</strong></div>
        <div class="stat"><span>Active topics</span><strong>{stats['topics']}</strong></div>
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

    <section class="profile-grid">
      {cards_html}
    </section>

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
    <span>Citations added: {citations_added}</span>
    <span>File: {esc(file_path)}{pr_link}</span>
  </div>
</div>'''
        )
    return '\n'.join(items)


def render_profile(profile):
    contributions = profile['contribution_count']
    contributions_label = 'contribution' if contributions == 1 else 'contributions'
    profile_url = f"{SITE_BASE_URL}/contributors/{profile['github']}/"
    card_url = f"{RAW_BASE}/cards/{profile['github']}.svg"
    card_local = f"../../cards/{profile['github']}.svg"

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
          <div class="stat"><span>Citations</span><strong>{profile['citations']}</strong></div>
          <div class="stat"><span>Contributions</span><strong>{contributions} {contributions_label}</strong></div>
          <div class="stat"><span>Commits</span><strong>{profile['commits']}</strong></div>
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


def main():
    data = read_data()
    profiles, topic_keys = collect_profiles(data)
    profiles = sort_profiles(profiles)
    topics = build_topic_filters(topic_keys)

    stats = {
        'verified': len(profiles),
        'citations': sum(p['citations'] for p in profiles),
        'topics': len(topic_keys),
        'updated': datetime.date.today().isoformat(),
    }

    SITE_DIR.mkdir(parents=True, exist_ok=True)
    CONTRIB_DIR.mkdir(parents=True, exist_ok=True)

    copy_cards()
    copy_static_assets()

    # Ensure GitHub Pages serves all files.
    write_file(SITE_DIR / '.nojekyll', '')

    index_html = render_index(profiles, topics, stats)
    write_file(SITE_DIR / 'index.html', index_html)

    for profile in profiles:
        profile_html = render_profile(profile)
        write_file(CONTRIB_DIR / profile['github'] / 'index.html', profile_html)

    print(f"Generated site for {len(profiles)} profiles")


if __name__ == '__main__':
    main()
