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
                end_line=source.count('\n',0,end)+1,
                kind=match[1] or match[3], heading=match[2],
                exercise_target=(re.search(r'\\begin\{(?:hint|solution)\}\{([^}]+)\}',unit)[1]
                    if re.search(r'\\begin\{(?:hint|solution)\}\{([^}]+)\}',unit) else None),
                excerpt=' '.join(unit.split())[:160],
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
    counting_ex={'ex:stars','ex:pigeon','ex:phi','ex:derangrec','ex:surj','ex:erdos','ex:catalan'}
    def homes(u):
        name=Path(u['file']).name
        ex=u['exercise_target'] or next(iter(u['labels']),None)
        if name=='ch08-counting-probability.tex':
            if ex in counting_ex or 29<=u['line']<=95 or 340<=u['line']<=350:
                return ['chapters/ch02-counting.tex']
            if u['kind']=='chapter':
                return ['chapters/ch09-probability.tex','chapters/ch02-counting.tex']
            return ['chapters/ch09-probability.tex']
        if name=='ch01-sums.tex' and (324<=u['line']<=351 or ex=='ex:catalan'):
            return ['chapters/ch02-counting.tex']
        if name=='ch04-inequalities.tex' and 59<=u['line']<=66:
            return ['chapters/ch05-sequences-series.tex','chapters/ch04-inequalities.tex']
        if name=='ch04-inequalities.tex' and 67<=u['line']<=74:
            return ['chapters/ch01-sums.tex','chapters/ch04-inequalities.tex']
        if name=='ch06-integrals-taylor.tex' and 30<=u['line']<=55:
            return ['chapters/ch05-sequences-series.tex','chapters/ch06-integrals-taylor.tex']
        if name=='ch06-integrals-taylor.tex' and 240<=u['line']<=267:
            return ['chapters/ch06-integrals-taylor.tex','chapters/ch04-inequalities.tex']
        return [str(Path(u['file']).relative_to(BOOK))]
    migration=[]
    for u in old:
        dest=[dict(label=l,file=targets[l][0],line=targets[l][1]) for l in u['labels'] if l in targets]
        exact=[dict(file=v['file'],line=v['line']) for v in new if v['sha256']==u['sha256']]
        mapped=[dict(file=BOOK+'/'+p,locator='Retained/revised source unit; compare original excerpt and source diff') for p in homes(u)]
        migration.append(dict(original=u,destinations=dest or exact or mapped,
            documented_homes=mapped,
            status='label retained' if dest else 'unchanged unit' if exact else 'documented source migration'))
    (OUT/'migration-units.json').write_text(json.dumps(migration,indent=2)+'\n')
    result=dict(original_labels=len(all_old_labels),current_labels=len(all_new_labels),missing_original_labels=missing,duplicate_labels=duplicates)
    (OUT/'preservation-check.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
    if missing or duplicates: raise SystemExit(1)

if __name__=='__main__': main()
