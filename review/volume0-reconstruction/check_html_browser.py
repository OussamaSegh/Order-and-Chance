from pathlib import Path
import json,os
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[2];site=root/'build/digital-review/site';out=root/'build/digital-review'
base='http://127.0.0.1:8765/read/tome0-mathematical-maturity/'
errors=[];rows=[]
with sync_playwright() as p:
 proxy=os.environ.get('HTTPS_PROXY') or os.environ.get('HTTP_PROXY')
 options={'headless':True,'args':['--no-sandbox']}
 if proxy:options['proxy']={'server':proxy,'bypass':'127.0.0.1,localhost'}
 browser=p.chromium.launch(**options)
 context=browser.new_context(viewport={'width':1360,'height':900},color_scheme='light')
 page=context.new_page()
 page.on('pageerror',lambda e:errors.append(str(e)))
 for path in sorted((site/'read/tome0-mathematical-maturity').glob('*.html')):
  page.goto(base+path.name,wait_until='networkidle',timeout=60000)
  page.evaluate('document.fonts.ready')
  row=page.evaluate('''() => ({math:document.querySelectorAll('span.math').length,rendered:document.querySelectorAll('span.math .katex').length,errors:[...document.querySelectorAll('.katex-error,.math-error')].map(n=>n.textContent),brokenImages:[...document.images].filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.src),reveals:document.querySelectorAll('details.reveal').length})''')
  row['page']=path.name;rows.append(row)
  assert row['rendered']==row['math'],row
  assert not row['errors'] and not row['brokenImages'],row
 page.set_viewport_size({'width':320,'height':900})
 for path in sorted((site/'read/tome0-mathematical-maturity').glob('*.html')):
  page.goto(base+path.name,wait_until='networkidle',timeout=60000)
  page.evaluate('document.fonts.ready')
  dimensions=page.evaluate('({width:innerWidth,scroll:document.documentElement.scrollWidth})')
  assert dimensions['scroll']<=320,(path.name,dimensions)
 for width in [1360,320]:
  page.set_viewport_size({'width':width,'height':900})
  for mode in ['light','dark']:
   page.goto(base+'ch-language.html',wait_until='networkidle')
   page.evaluate('(mode)=>document.documentElement.dataset.theme=mode',mode)
   page.evaluate('document.fonts.ready')
   dimensions=page.evaluate('({width:innerWidth,scroll:document.documentElement.scrollWidth})')
   assert dimensions['scroll']<=width,dimensions
   page.screenshot(path=str(out/f'language-{width}-{mode}.png'),full_page=False)
   if width==320:
    page.locator('#menu').click();assert page.locator('#menu').get_attribute('aria-expanded')=='true'
    page.locator('#menu').click();assert page.locator('#menu').get_attribute('aria-expanded')=='false'
  before=page.evaluate('document.documentElement.dataset.theme')
  page.locator('#theme').click();after=page.evaluate('document.documentElement.dataset.theme');assert before!=after
 details=page.locator('details.reveal').first
 assert not details.get_attribute('open')
 details.locator('summary').click();assert details.get_attribute('open') is not None
 page.goto(base+'ch-probability.html',wait_until='networkidle')
 assert page.locator('h1').first.inner_text().startswith('9 First Probability')
 page.screenshot(path=str(out/'probability-mobile.png'),full_page=False)
 browser.close()
assert not errors,errors
result={'pages':rows,'formulas_rendered':sum(r['rendered'] for r in rows),'reveal_controls':sum(r['reveals'] for r in rows),'all_pages_desktop_and_mobile':'passed','language_light_dark':'passed','menu_theme_reveal_controls':'passed','javascript_errors':errors}
(out/'browser-results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
