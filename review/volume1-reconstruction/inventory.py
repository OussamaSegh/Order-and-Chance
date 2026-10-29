"""Source inventory and migration evidence; hashes are not proof verification."""
import hashlib,json,re,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
BOOK='volume1-integers'
BASE='a65d685d941b8cef2c1d41f51bff65a71f885e11'
def inventory(files):
    units=[]
    for name,s in files:
        token=re.compile(r'\\(chapter\*?|section\*?|subsection\*?|paragraph)\{([^\n]*)|\\begin\{(theorem|proposition|lemma|corollary|definition|example|exercise|hint|solution|challenge|think|beauty|reminder|figure|proof)\}')
        for m in token.finditer(s):
            kind=m[1] or m[3]
            if m[3]:
                end=s.find('\\end{'+kind+'}',m.end())+len('\\end{'+kind+'}')
                body=s[m.start():end]
            else:
                end=s.find('\n',m.start());body=s[m.start():end]
            target=re.search(r'\\begin\{(?:hint|solution)\}\{([^}]+)\}',body)
            units.append(dict(file=name,line=s.count('\n',0,m.start())+1,kind=kind,
                heading=m[2],labels=re.findall(r'\\label\{([^}]+)\}',body),
                target=target[1] if target else None,
                references=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',body),
                excerpt=' '.join(body.split())[:200],sha256=hashlib.sha256(body.encode()).hexdigest()))
    return units

def main():
    try:
        names=subprocess.check_output(['git','ls-tree','-r','--name-only',BASE,BOOK],cwd=ROOT,text=True).splitlines()
        oldfiles=[(n,subprocess.check_output(['git','show',BASE+':'+n],cwd=ROOT,text=True)) for n in names if n.endswith('.tex')]
        old=inventory(oldfiles)
    except (subprocess.CalledProcessError,FileNotFoundError):
        old=json.loads((OUT/'baseline-inventory.json').read_text())['units']
    files=[(str(p.relative_to(ROOT)),p.read_text()) for p in sorted((ROOT/BOOK).rglob('*.tex'))]
    cur=inventory(files)
    for name,data in [('baseline',dict(commit=BASE,units=old)),('current',dict(units=cur))]:
        (OUT/(name+'-inventory.json')).write_text(json.dumps(data,indent=2)+'\n')
    labels={l:u for u in cur for l in u['labels']}
    migrations=[]
    for u in old:
        candidates=[v for v in cur if v['sha256']==u['sha256']]
        if not candidates:candidates=[labels[l] for l in u['labels'] if l in labels]
        if not candidates and u['target']:candidates=[v for v in cur if v['kind']==u['kind'] and v['target']==u['target']]
        if not candidates:candidates=[v for v in cur if v['kind']==u['kind'] and v['heading']==u['heading'] and Path(v['file']).name==Path(u['file']).name]
        migrations.append(dict(original=u,destinations=[dict(file=v['file'],line=v['line']) for v in candidates],
            status='unchanged' if any(v['sha256']==u['sha256'] for v in candidates) else 'revised' if candidates else 'see documented migration'))
    (OUT/'migration-units.json').write_text(json.dumps(migrations,indent=2)+'\n')
    counts={k:sum(u['kind']==k for u in cur) for k in sorted({u['kind'] for u in cur})}
    exercises={l for u in cur if u['kind']=='exercise' for l in u['labels']}
    hints=[u['target'] for u in cur if u['kind']=='hint'];solutions=[u['target'] for u in cur if u['kind']=='solution']
    oldlabels={l for u in old for l in u['labels']}
    currentlabels=[l for n,s in files for l in re.findall(r'\\label\{([^}]+)\}',s)]
    errors=dict(missing_labels=sorted(oldlabels-set(currentlabels)),duplicate_labels=sorted({l for l in currentlabels if currentlabels.count(l)>1}),
        missing_hints=sorted(exercises-set(hints)),missing_solutions=sorted(exercises-set(solutions)),
        extra_hints=sorted(set(hints)-exercises),extra_solutions=sorted(set(solutions)-exercises),
        duplicate_hints=sorted({l for l in hints if hints.count(l)>1}),duplicate_solutions=sorted({l for l in solutions if solutions.count(l)>1}))
    result=dict(baseline=BASE,counts=counts,original_labels=len(oldlabels),current_labels=len(currentlabels),exercises=len(exercises),errors=errors)
    (OUT/'structure-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
    assert not any(errors.values()),errors
if __name__=='__main__':main()
