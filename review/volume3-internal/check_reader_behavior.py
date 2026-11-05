"""Exercise actual reader controls and every hint/solution via Chromium clicks.

This is behavioral evidence, separate from mathematical and visual approval.
The source commit identifies the output; the exact checker bytes are hashed.
"""
import argparse
from functools import partial
import hashlib
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import threading
from urllib.parse import unquote, urlsplit

from playwright.sync_api import sync_playwright


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def main():
    tool_sha256 = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('site', type=Path)
    p.add_argument('--source-commit', required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    root = a.site.resolve()
    files = sorted(f for f in (root/'read/volume3-symmetry').glob('*.html')
                   if 'reader.js' in f.read_text())
    server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(root)))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    rows, controls, failures, hidden_targets = [], [], [], []
    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch(executable_path='/usr/bin/chromium', args=['--no-sandbox'])
            for width in (390, 1280):
                page = browser.new_page(viewport={'width': width, 'height': 844}, color_scheme='light')
                for file in files:
                    relative = file.relative_to(root).as_posix()
                    url = f'http://127.0.0.1:{server.server_port}/{relative}'
                    page.goto(url, wait_until='load')
                    page.evaluate('document.fonts.ready')
                    details = page.locator('details.reveal')
                    count = details.count()
                    assert page.locator('details.reveal[open]').count() == 0, relative
                    for i in range(count):
                        item = details.nth(i)
                        summary = item.locator(':scope > summary')
                        summary.click()
                        assert item.get_attribute('open') is not None, (relative, i, 'open')
                        content = item.locator(':scope > div')
                        assert content.is_visible(), (relative, i, 'visible')
                        backlink = content.locator('.oc-head a')
                        assert backlink.count() == 1, (relative, i, 'backlink parity')
                        href = backlink.get_attribute('href')
                        key = unquote(urlsplit(href).fragment)
                        backlink.click()
                        assert unquote(urlsplit(page.url).fragment) == key, (relative, i, 'hash')
                        target = page.evaluate('id => {const e=document.getElementById(id); if(!e)return null; const r=e.getBoundingClientRect(); return {exercise:e.classList.contains("exercise"),top:r.top,bottom:r.bottom};}', key)
                        assert target and target['exercise'] and -1 <= target['top'] < 844, (relative, i, target)
                        summary.click()
                        assert item.get_attribute('open') is None, (relative, i, 'close')
                        rows.append({'file': relative, 'width': width, 'ordinal': i+1,
                                     'kind': content.get_attribute('class'), 'prompt_key': key,
                                     'opened_by_click': True, 'content_visible': True,
                                     'backlink_clicked': href, 'prompt_target': target,
                                     'closed_by_click': True})
                    # Existing IDs inside folded content exercise the actual
                    # hashchange handler. No IDs are invented for this check.
                    targets = page.locator('details.reveal [id]').evaluate_all('(es)=>es.map(e=>e.id)')
                    for key in targets:
                        page.evaluate('location.hash=""')
                        page.evaluate('document.querySelectorAll("details.reveal").forEach(e=>e.open=false)')
                        page.evaluate('id => location.hash=encodeURIComponent(id)', key)
                        page.wait_for_function('id => {let e=document.getElementById(id);for(;e;e=e.parentElement)if(e.tagName==="DETAILS"&&!e.open)return false;return true;}', arg=key)
                        hidden_targets.append({'file': relative, 'width': width, 'id': key, 'actual_hash_opened_ancestors': True})
                    # Each core page receives actual theme and navigation checks.
                    page.evaluate('window.scrollTo(0,0)')
                    page.locator('#theme').click()
                    theme = page.locator('html').get_attribute('data-theme')
                    assert theme in ('dark', 'light')
                    assert page.evaluate('localStorage.getItem("theme")') == theme
                    page.reload(wait_until='load')
                    assert page.locator('html').get_attribute('data-theme') == theme
                    control = {'file': relative, 'width': width, 'theme_clicked': theme,
                               'theme_persisted_after_reload': True}
                    if width == 390:
                        menu = page.locator('#menu')
                        menu.click()
                        assert menu.get_attribute('aria-expanded') == 'true'
                        assert page.locator('body').evaluate('e=>e.classList.contains("menu-open")')
                        page.locator('#shade').click(position={'x': 370, 'y': 20})
                        assert menu.get_attribute('aria-expanded') == 'false'
                        menu.click()
                        nav = page.locator('#side nav a.current').first
                        if not nav.count():
                            nav = page.locator('#side nav a').first
                        nav.click()
                        assert not page.locator('body').evaluate('e=>e.classList.contains("menu-open")')
                        control['menu_open_shade_close_and_navigation_close'] = True
                    else:
                        assert not page.locator('#menu').is_visible()
                        assert page.locator('#side').is_visible()
                        control['wide_sidebar_visible_menu_hidden'] = True
                    controls.append(control)
                    print(width, file.name, count, 'disclosures/control checks passed', flush=True)
                page.close()
            browser.close()
    except Exception as error:
        failures.append({'type': type(error).__name__, 'error': str(error)})
    finally:
        server.shutdown()
        server.server_close()
        thread.join()
    result = {'source_commit': a.source_commit,
              'measurement_tool_sha256': tool_sha256,
              'method': 'Actual unmodified output in Chromium at390/1280. Every existing hint/solution summary clicked open, visible block checked, actual prompt backlink clicked and destination checked, summary clicked closed. Theme click/localStorage/reload and menu/shade/navigation checked on each core page. Existing folded-content IDs tested for hash opening; no fabricated IDs. Browser behavior only, no native-device or visual approval.',
              'disclosures': rows, 'controls': controls,
              'existing_folded_hash_targets': hidden_targets, 'problems': failures}
    a.output.write_text(json.dumps(result, indent=2)+'\n')
    print(len(rows), 'actual disclosure checks,', len(controls), 'page/control checks,', len(failures), 'problems')
    return bool(failures)


if __name__ == '__main__':
    raise SystemExit(main())
