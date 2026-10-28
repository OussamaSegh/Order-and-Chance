"""Record source units and explicit identifiers without claiming proof verification."""
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
BASE = '3259d462860e13150fc6cb15ecb0e3109f95b5ed'
BOOK = 'tome0-mathematical-maturity'

def inventory(files):
    records = []
    token = re.compile(r'\\(chapter\*?|section\*?|subsection\*?)\{([^\n]*)|\\begin\{(theoremx?|propositionx?|lemmax?|corollaryx?|definitionx?|examplex?|exercise|hint|solution|challenge|think|beauty|reminder|figure|proof)\}')
    for name, source in files:
        matches = list(token.finditer(source))
        for i, match in enumerate(matches):
            end = matches[i+1].start() if i+1<len(matches) else len(source)
            unit = source[match.start():end]
            records.append(dict(file=name, line=source.count('\n',0,match.start())+1,
                kind=match[1] or match[3], heading=match[2],
                labels=re.findall(r'\\label\{([^}]+)\}',unit),
                references=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',unit),
                sha256=hashlib.sha256(unit.encode()).hexdigest()))
    return records

def main():
    names = subprocess.check_output(['git','ls-tree','-r','--name-only',BASE,BOOK],cwd=ROOT,text=True).splitlines()
    baseline = [(n,subprocess.check_output(['git','show',f'{BASE}:{n}'],cwd=ROOT,text=True)) for n in names if n.endswith('.tex')]
    current = [(str(p.relative_to(ROOT)),p.read_text()) for p in sorted((ROOT/BOOK).rglob('*.tex'))]
    old, new = inventory(baseline), inventory(current)
    (OUT/'baseline-inventory.json').write_text(json.dumps(dict(commit=BASE,units=old),indent=2)+'\n')
    (OUT/'current-inventory.json').write_text(json.dumps(dict(units=new),indent=2)+'\n')
    all_old_labels={l for _,s in baseline for l in re.findall(r'\\label\{([^}]+)\}',s)}
    all_new_labels=[l for _,s in current for l in re.findall(r'\\label\{([^}]+)\}',s)]
    missing=sorted(all_old_labels-set(all_new_labels))
    duplicates=sorted({l for l in all_new_labels if all_new_labels.count(l)>1})
    targets={l:(n,s.count('\n',0,m.start())+1) for n,s in current for m in re.finditer(r'\\label\{([^}]+)\}',s) for l in [m[1]]}
    migration=[]
    for u in old:
        dest=[dict(label=l,file=targets[l][0],line=targets[l][1]) for l in u['labels'] if l in targets]
        exact=[dict(file=v['file'],line=v['line']) for v in new if v['sha256']==u['sha256']]
        migration.append(dict(original=u,destinations=dest or exact,status='label retained' if dest else 'unchanged unit' if exact else 'review source diff'))
    (OUT/'migration-units.json').write_text(json.dumps(migration,indent=2)+'\n')
    result=dict(original_labels=len(all_old_labels),current_labels=len(all_new_labels),missing_original_labels=missing,duplicate_labels=duplicates)
    (OUT/'preservation-check.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
    if missing or duplicates: raise SystemExit(1)

if __name__=='__main__': main()
