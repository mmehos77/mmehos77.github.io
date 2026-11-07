"""Check Symptom Sorter (WFA) sign quotes that cite a full WMS paper against its PDF.

Usage: python3 tools/check_wms.py wfa/index.html heat24=heat.pdf:112 alt24=alt.pdf:2 hypo19=hypo.pdf:47 fb24=fb.pdf:183 spine24=spine.pdf:78 burn25=burns.pdf:549
A sign whose page is "W:<key>@<label>" cites the printed page <label> (114S, S52, 550) of paper <key>;
firstpage is the number of the PDF's first printed page (112 for 112S, 47 for S47). Needs pdftotext (poppler-utils).
Quotes citing a key with no PDF given, or citing a WMS summary ("W:<key>" with no page), are counted, not checked.
"""
import json, re, subprocess, sys

def norm(s):
    for a, b in (('’', "'"), ('‘', "'"), ('–', '-'), ('—', '-'), ('­', ''), ('ﬁ', 'fi'), ('ﬂ', 'fl')):
        s = s.replace(a, b)
    return re.sub(r"[^a-z0-9<>=≤≥%/']+", ' ', s.lower().replace('-', '')).strip()   # degree signs and control glyphs become spaces

html, specs = sys.argv[1], sys.argv[2:]
pdfs = {}
for sp in specs:
    k, rest = sp.split('=', 1); path, first = rest.rsplit(':', 1); pdfs[k] = (path, int(first))
conds = json.loads(re.search(r'<script id="conds" type="application/json">(.*?)</script>', open(html, encoding='utf-8').read(), re.S).group(1))['conds']
cache, bad, n = {}, 0, {'checked': 0, 'no pdf given': 0, 'summary (no page)': 0}
for c in conds:
    links = list(c['signs']) + [[None, c['basis'][0], c['basis'][1]]]
    for link in links:
        quote, page = link[1], link[2]
        if not (isinstance(page, str) and page.startswith('W:')): continue
        if '@' not in page: n['summary (no page)'] += 1; continue
        key, label = page[2:].split('@'); jp = int(re.sub(r'\D', '', label))   # printed page label, e.g. 114S, S52, 550
        if key not in pdfs: n['no pdf given'] += 1; continue
        path, first = pdfs[key]; pp = jp - first + 1
        for layout in ('', '-layout', '-raw'):
            ck = (key, pp, layout)
            if ck not in cache:
                args = ['pdftotext'] + ([layout] if layout else []) + ['-f', str(pp), '-l', str(pp), path, '-']
                cache[ck] = norm(subprocess.run(args, capture_output=True, text=True).stdout)
            q = norm(quote)
            if q in cache[ck] or re.search(r'\b' + r'\b.*?\b'.join(map(re.escape, q.split())) + r'\b', cache[ck], re.S): break
        else:
            print(f'{c["name"]}: "{quote}" not found on {key} p.{label}'); bad += 1; continue
        n['checked'] += 1
print(f'{html}: {n}')
print('OK' if not bad else f'{bad} problem(s)')
sys.exit(1 if bad else 0)
