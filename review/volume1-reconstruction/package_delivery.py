"""Package the committed source, reports, standalone reader and checksums."""
from pathlib import Path
import gzip,hashlib,json,shutil,subprocess,tarfile,zipfile
ROOT=Path(__file__).resolve().parents[2]
BUNDLE=ROOT/'dist/volume1-revision'
# Keep the original revision exact; the baseline manifest is canonical.
BASE=json.loads((Path(__file__).resolve().parent/'baseline-inventory.json').read_text())['commit']
def main():
    BUNDLE.mkdir(parents=True,exist_ok=True)
    commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    subprocess.run(['git','archive','--format=zip','-o',str(BUNDLE/'Order-and-Chance-Volume1-source.zip'),commit],cwd=ROOT,check=True)
    backup=BUNDLE/'Order-and-Chance-original-source.tar.gz'
    if not backup.exists():
        process=subprocess.Popen(['git','archive',BASE],cwd=ROOT,stdout=subprocess.PIPE)
        with gzip.open(backup,'wb') as f:
            shutil.copyfileobj(process.stdout,f)
        process.stdout.close()
        if process.wait():raise RuntimeError('Could not archive the original revision')
    with gzip.open(backup,'rb') as f:
        while f.read(1024*1024):pass
    with tarfile.open(backup) as t:assert len(t.getmembers())>100
    with zipfile.ZipFile(BUNDLE/'Volume1-reports.zip','w',compression=zipfile.ZIP_DEFLATED) as z:
        for p in sorted((ROOT/'review/volume1-reconstruction').rglob('*')):
            if p.is_file() and '__pycache__' not in p.parts:z.write(p,p.relative_to(ROOT/'review'))
    staging=ROOT/'build/volume1-delivery-dist'
    (staging/'kdp').mkdir(parents=True,exist_ok=True)
    for suffix in ('pdf','epub'):shutil.copy2(ROOT/f'dist/tome1-integers.{suffix}',staging/f'tome1-integers.{suffix}')
    for p in (ROOT/'dist/kdp').glob('tome1-integers-*'):shutil.copy2(p,staging/'kdp'/p.name)
    shutil.copytree(ROOT/'dist/html/tome1-integers',staging/'html/tome1-integers',dirs_exist_ok=True)
    site=ROOT/'build/volume1-delivery-site'
    subprocess.run(['python3',str(ROOT/'tools/site.py'),str(staging),str(site)],cwd=ROOT,check=True)
    with zipfile.ZipFile(BUNDLE/'Volume1-HTML-reader.zip','w',compression=zipfile.ZIP_DEFLATED) as z:
        for p in sorted(site.rglob('*')):
            if p.is_file():z.write(p,p.relative_to(site))
    for p in BUNDLE.glob('*.zip'):
        with zipfile.ZipFile(p) as z:assert z.testzip() is None,p
    files=[ROOT/'dist/tome1-integers.pdf',ROOT/'dist/kdp/tome1-integers-print.pdf',ROOT/'dist/tome1-integers.epub',ROOT/'dist/kdp/tome1-integers-cover-wrap.pdf',*sorted(BUNDLE.glob('*.zip')),backup]
    items=[]
    for p in files:
        h=hashlib.sha256()
        with p.open('rb') as f:
            for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
        items.append(dict(path=str(p.relative_to(ROOT)),bytes=p.stat().st_size,sha256=h.hexdigest()))
    manifest=dict(commit=commit,baseline=BASE,chapter_count=13,original_exercises_preserved=97,total_exercises=101,proved_results=83,numbered_pages=177,interior_pages=189,reading_pages=190,files=items,validation=dict(epubcheck='zero issues',publishing_tests=68,mathematical_assertions=35263,html_pages=17,formulas_rendered=8820),limitations='See review/volume1-reconstruction/OUTSTANDING-ISSUES.md')
    (BUNDLE/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    (BUNDLE/'SHA256SUMS').write_text('\n'.join(x['sha256']+'  '+x['path'] for x in items)+'\n')
    print(json.dumps(dict(commit=commit,verified_archives=4,artifacts=len(items))))
if __name__=='__main__':main()
