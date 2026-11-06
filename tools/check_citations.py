"""Check every symptom citation in the Symptom Sorter apps against the FM-51 PDF.

Usage: python3 tools/check_citations.py path/to/FM51.pdf index.html wfa/index.html
Needs pdftotext (poppler-utils). Exits with an error if any FM-51 quote is not
found on its cited page, or if a link has an unknown tag.

Tags (4th item of each sign link): none = FM-51 states the finding;
"a" = FM-51 only says to check it; "x" = the app's reading of nearby FM-51 text.
Links whose page is a string (e.g. "W:fb") cite WMS and are not checked here.
"""
import json, re, subprocess, sys

def norm(s):
    for a, b in (('’', "'"), ('‘', "'"), ('–', '-'), ('—', '-'), ('­', '')):
        s = s.replace(a, b)
    # hyphens are dropped: the PDF text loses them at line breaks ("blood-tinged" -> "bloodtinged")
    return re.sub(r"[^a-z0-9<>=≤≥°%/']+", ' ', s.lower().replace('-', '')).strip()

def page_text(pdf, p, layout):
    args = ['pdftotext'] + (['-layout'] if layout else []) + ['-f', str(p), '-l', str(p), pdf, '-']
    return norm(subprocess.run(args, capture_output=True, text=True).stdout)

pdf, files = sys.argv[1], sys.argv[2:]
cache, bad = {}, 0
for f in files:
    html = open(f, encoding='utf-8').read()
    conds = json.loads(re.search(r'<script id="conds" type="application/json">(.*?)</script>', html, re.S).group(1))['conds']
    n = {'finding': 0, 'a': 0, 'x': 0, 'other source': 0}
    for c in conds:
        for link in c['signs']:
            chip, quote, page = link[:3]
            tag = link[3] if len(link) > 3 else None
            if tag not in (None, 'a', 'x'):
                print(f'{f}: {c["name"]}: unknown tag {tag!r}'); bad += 1
            if not isinstance(page, int) or page == 0 or quote.startswith('APP:'):
                n['other source'] += 1; continue
            n[tag or 'finding'] += 1
            q = norm(quote.rstrip('*'))
            words = q.split()
            for layout in (False, True):
                key = (page, layout)
                if key not in cache: cache[key] = page_text(pdf, page, layout)
                t = cache[key]
                # exact match, or all words present in order (text in table columns can be split)
                if q in t or re.search(r'\b' + r'\b.*?\b'.join(map(re.escape, words)) + r'\b', t, re.S):
                    break
            else:
                print(f'{f}: {c["name"]}: "{quote}" not found on p.{page}'); bad += 1
    print(f'{f}: {n}')
print('OK' if not bad else f'{bad} problem(s)')
sys.exit(1 if bad else 0)
