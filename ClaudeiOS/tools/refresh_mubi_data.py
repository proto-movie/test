#!/usr/bin/env python3
"""Refresh the catalogue baked into browse_prototype1.html from MUBI's public v4 API (UK).

Rebuilds FILMS, COLLECTIONS, DIRECTOR_COUNTS and DIRECTOR_IMAGES. Collection categories
(the Spotlight / Director Focus / ... pills) were picked by hand, so existing collections
keep theirs and only new ones get a best guess. DIRECTOR_CATS is curated and left alone.

    python3 tools/refresh_mubi_data.py
"""
import json, re, sys, time, urllib.request, gzip
from collections import Counter
from pathlib import Path

PAGE = Path(__file__).resolve().parent.parent / 'browse_prototype1.html'
API = 'https://api.mubi.com/v4'
HEADERS = {'Client': 'web', 'Client-Country': 'GB', 'Accept-Language': 'en', 'Accept': 'application/json',
           'Accept-Encoding': 'gzip'}


def get(path):
    req = urllib.request.Request(API + path, headers=HEADERS)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                body = r.read()
                if r.headers.get('Content-Encoding') == 'gzip':
                    body = gzip.decompress(body)
                return json.loads(body)
        except Exception as e:
            if attempt == 3:
                raise
            time.sleep(1 + attempt)


def all_pages(path, key):
    items, page = [], 1
    while page:
        sep = '&' if '?' in path else '?'
        d = get(f'{path}{sep}page={page}&per_page=100')
        items += d[key]
        page = d['meta'].get('next_page')
    return items


def read_var(html, name):
    return json.loads(re.search(r'var ' + name + r' = (.*?);\n', html).group(1))


def write_var(html, name, value):
    text = json.dumps(value, ensure_ascii=False, separators=(',', ':'))
    new, n = re.subn(r'(var ' + name + r' = ).*?;\n', lambda m: m.group(1) + text + ';\n', html, count=1)
    assert n == 1, name
    return new


def strip_query(url):
    return url.split('?')[0] if url else url


def film_row(f):
    series = f.get('series') or {}
    # Series come back as their first episode; show the series' name and artwork instead.
    art = {a['format']: a['image_url'] for a in (f.get('artworks') or [])}
    art.update({a['format']: a['image_url'] for a in (series.get('artworks') or [])})
    stills = f.get('stills') or {}
    row = {
        't': series.get('title') or f['title'],
        'd': ', '.join(d['name'] for d in f.get('directors') or []),
        'y': str(f.get('year') or ''),
        'c': ', '.join(f.get('historic_countries') or []),
        'i': strip_query(stills.get('medium')) or f.get('still_url') or art.get('cover_artwork_horizontal', ''),
        'r': f.get('average_rating_out_of_ten') or 0,
        'g': f.get('genres') or [],
    }
    if art.get('cover_artwork_vertical'):
        row['pv'] = art['cover_artwork_vertical']
    if f.get('series'):
        row['s'] = 1
    return row


def guess_category(title, sub, director_names):
    text = f'{title} {sub}'
    if re.search(r'\b(1[89]\d0s|20[0-2]0s|\d0s)\b', text):
        return 'decade'
    if re.search(r'\b(Two|Three|Four|Five|Films|Comedies|A Trilogy) by\b|The (Cinema|Films) of|Restored By', text) or \
            any(n and n in text for n in director_names):
        return 'director'
    if re.search(r'Oscar|Festival|Cannes|Venice|Berlinale|Sundance|Locarno|Award|Prize|Palme\b|Golden', text, re.I):
        return 'awards'
    if re.search(r'British|American|French|Italian|Japanese|Korean|Asian|African|Latin|European|Nordic|'
                 r'Iranian|Indian|Chinese|German|Spanish|Mexican|Brazil|on Screen', text):
        return 'region'
    return ''


def main():
    html = PAGE.read_text()
    old_films = read_var(html, 'FILMS')
    old_colls = read_var(html, 'COLLECTIONS')
    old_images = read_var(html, 'DIRECTOR_IMAGES')

    print('Fetching films…', file=sys.stderr)
    films_raw = all_pages('/browse/films?sort=popularity_quality_score&playable=true', 'films')
    films = [film_row(f) for f in films_raw]

    print('Fetching collections…', file=sys.stderr)
    groups = all_pages('/browse/film_groups', 'film_groups')
    groups.sort(key=lambda g: g['id'], reverse=True)  # newest first, for "Recently Added"
    norm = lambda t, sub: re.sub(r'\s+', ' ', f'{t} {sub}').strip().lower()
    old_cat = {norm(c['t'], c['sub']): c['cat'] for c in old_colls}
    director_names = {d['name'] for f in films_raw for d in f.get('directors') or []}
    colls, guessed = [], []
    for g in groups:
        t, sub = g.get('title') or '', g.get('subtitle') or ''
        key = norm(t, sub)
        if key in old_cat:
            cat = old_cat[key]
        else:
            cat = guess_category(t, sub, director_names)
            guessed.append((t + (' ' + sub if sub else ''), cat or '(none)'))
        colls.append({
            't': t, 'sub': sub, 'n': str(g.get('total_items') or 0), 'img': g.get('image') or '',
            'tr': g.get('title_treatment_url') or '',
            'col': '#' + (g.get('color') or g.get('average_colour_hex') or g.get('image_color') or '000000'),
            'cat': cat,
        })

    counts = Counter(f['d'] for f in films if f['d'])
    images = {}
    slugs = {d['name']: d['slug'] for f in films_raw for d in f.get('directors') or []}
    for name in sorted({n for key in counts for n in key.split(', ')}):
        if old_images.get(name):
            images[name] = old_images[name]
        elif name in slugs:
            try:
                url = get('/cast_members/' + slugs[name]).get('image_url')
                if url:
                    images[name] = url
            except Exception:
                print('  no image for', name, file=sys.stderr)

    for name, value in [('FILMS', films), ('COLLECTIONS', colls),
                        ('DIRECTOR_COUNTS', dict(counts.most_common())), ('DIRECTOR_IMAGES', images)]:
        html = write_var(html, name, value)
    PAGE.write_text(html)

    old_titles = {f['t'] for f in old_films}
    new_titles = {f['t'] for f in films}
    print(json.dumps({
        'films': [len(old_films), len(films)],
        'films_added': sorted(new_titles - old_titles),
        'films_removed': sorted(old_titles - new_titles),
        'collections': [len(old_colls), len(colls)],
        'collections_new_with_guessed_category': guessed,
        'collections_removed': sorted({norm(c['t'], c['sub']) for c in old_colls} - {norm(c['t'], c['sub']) for c in colls}),
        'directors': len(counts), 'director_images': len(images),
    }, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
