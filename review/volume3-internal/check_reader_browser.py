"""Measure actual Volume 3 reader output in Chromium; never grant visual approval.

Use an actual tools/site.py output directory. Playwright/Chromium are optional
review dependencies, outside the standard-library tests. URI-rule injection is
an explicitly provisional regression mode; final evidence must omit that flag.
"""
import argparse
from functools import partial
import hashlib
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import re
import threading

from playwright.sync_api import sync_playwright


MEASURE = r"""() => {
 const bounds = e => { const r=e.getBoundingClientRect();return {left:r.left,
   right:r.right,top:r.top,bottom:r.bottom,width:r.width,height:r.height}; };
 const panAncestor = e => { for(let p=e.parentElement;p && p.tagName!=='MAIN';p=p.parentElement)
   if(['auto','scroll'].includes(getComputedStyle(p).overflowX))return p.className||p.tagName;
   return null; };
 const outside = e => {const r=e.getBoundingClientRect();return r.width>0 &&
   (r.left < -1 || r.right > innerWidth+1);};
 const inline=[...document.querySelectorAll('main .math.inline')];
 return {viewport:innerWidth,body_width:document.documentElement.scrollWidth,
   fonts:document.fonts.status,math_count:document.querySelectorAll('span.math').length,
   math_errors:[...document.querySelectorAll('.math-error,.katex-error')].map(e=>({
     text:e.textContent.slice(0,300),title:e.getAttribute('title')})),
   disclosure_count:document.querySelectorAll('details.reveal').length,
   uri_bounds:[...document.querySelectorAll('main a.uri')].map(e=>({text:e.textContent,
     ...bounds(e),outside:outside(e),pan_ancestor:panAncestor(e)})),
   outside_inline:inline.filter(outside).map(e=>({text:e.textContent.slice(0,180),
     class:e.className,...bounds(e),pan_ancestor:panAncestor(e)})),
   images:[...document.querySelectorAll('main img')].map(e=>({src:e.getAttribute('src'),
     loaded:e.complete&&e.naturalWidth>0,natural_width:e.naturalWidth,
     natural_height:e.naturalHeight,...bounds(e),outside:outside(e),
     pan_ancestor:panAncestor(e),aspect_error:e.clientHeight>0&&e.naturalHeight>0?Math.abs((e.clientWidth/e.clientHeight)/
       (e.naturalWidth/e.naturalHeight)-1):null}))};
}"""


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('site', type=Path)
    parser.add_argument('--source-commit', required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--uri-rule-from', type=Path)
    args = parser.parse_args()
    root = args.site.resolve()
    reader = root / 'read/volume3-symmetry'
    # Core output only; site.py also creates compatibility redirects. Their
    # targets belong to the separate complete local-link audit.
    files = sorted(p for p in reader.glob('*.html')
                   if 'reader.js' in p.read_text())
    if not files:
        raise ValueError('No actual reader pages')
    override = None
    if args.uri_rule_from:
        css = args.uri_rule_from.read_text()
        override = {'path': str(args.uri_rule_from),
                    'sha256': hashlib.sha256(css.encode()).hexdigest(),
                    'rule': re.search(r'a\.uri\s*\{[^}]+\}', css).group()}
    server = ThreadingHTTPServer(('127.0.0.1', 0),
                                partial(QuietHandler, directory=str(root)))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    rows, problems = [], []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(executable_path='/usr/bin/chromium',
                                       args=['--no-sandbox'])
            for width in (390, 1280):
                page = browser.new_page(viewport={'width': width, 'height': 844})
                for file in files:
                    failed, errors, http_errors = [], [], []
                    on_fail = lambda request: failed.append(
                        {'url': request.url, 'failure': request.failure})
                    on_error = lambda error: errors.append(str(error))
                    def on_response(response):
                        if response.status >= 400:
                            http_errors.append({'url': response.url,
                                                'status': response.status})
                    page.on('requestfailed', on_fail)
                    page.on('pageerror', on_error)
                    page.on('response', on_response)
                    relative = file.relative_to(root).as_posix()
                    page.goto(f'http://127.0.0.1:{server.server_port}/{relative}',
                              wait_until='load', timeout=45000)
                    if override:
                        page.add_style_tag(content=override['rule'])
                    # Measure every hint/solution, not only the folded shells.
                    page.evaluate("document.querySelectorAll('details.reveal').forEach(e=>e.open=true)")
                    page.evaluate('document.fonts.ready')
                    page.evaluate('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
                    row = page.evaluate(MEASURE)
                    row.update(file=relative, width=width, failed_requests=failed,
                               runtime_errors=errors, http_errors=http_errors)
                    if (failed or errors or http_errors or row['math_errors']
                            or row['body_width'] > width):
                        problems.append({'file': relative, 'width': width,
                                         'error': 'loading/runtime/math/body bounds'})
                    for item in row['uri_bounds'] + row['outside_inline']:
                        if item.get('outside', True) and not item['pan_ancestor']:
                            problems.append({'file': relative, 'width': width,
                                             'error': 'clipped text/math outside viewport',
                                             'item': item})
                    for item in row['images']:
                        if (not item['loaded'] or item['aspect_error'] is None or item['aspect_error'] > .05 or
                                (item['outside'] and not item['pan_ancestor'])):
                            problems.append({'file': relative, 'width': width,
                                             'error': 'image loading/aspect/bounds', 'item': item})
                    rows.append(row)
                    page.remove_listener('requestfailed', on_fail)
                    page.remove_listener('pageerror', on_error)
                    page.remove_listener('response', on_response)
                page.close()
            browser.close()
    finally:
        server.shutdown()
        server.server_close()
        thread.join()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    result = {'source_commit': args.source_commit,
              'method': 'Actual reader site in Chromium390/1280;CDN KaTeX normally loaded;all disclosures expanded before measuring every math/URI/image;intentional ancestor horizontal scrolling distinguished from clipping. Measurements do not approve unopened pixels or navigation/theme/menu/link behavior.',
              'provisional_uri_override': override,
              'pages': rows, 'problems': problems}
    args.output.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(f'{len(rows)} actual page/viewport measurements; {len(problems)} problems; '
          f'URI override: {override is not None}')
    return bool(problems)


if __name__ == '__main__':
    raise SystemExit(main())
