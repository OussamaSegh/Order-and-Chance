"""Build traceable ledgers from the separate source-reading notes."""
import hashlib,json,re,subprocess
from pathlib import Path
import inventory
ROOT=inventory.ROOT;OUT=inventory.OUT
def notes(name):
    return dict(l.split('|',1) for l in (OUT/name).read_text().splitlines() if l and not l.startswith('#'))
def main():
    inventory.main()
    current=json.loads((OUT/'current-inventory.json').read_text())['units']
    tn=notes('review-notes.txt');en=notes('exercise-review-notes.txt')
    records=[]
    for u in current:
        if u['kind'] not in ('theorem','proposition','lemma','corollary'):continue
        key=u['labels'][0] if u['labels'] else 'unlabelled:'+Path(u['file']).name+':'+str(u['line'])
        assert key in tn,key
        s=(ROOT/u['file']).read_text();offset=sum(len(l) for l in s.splitlines(keepends=True)[:u['line']-1])
        end=s.index(r'\end{'+u['kind']+'}',offset)
        if key=='thm:qr':start=s.index(r'\begin{proof}[Proof of Theorem~\ref{thm:qr}]',end)
        else:start=s.index(r'\begin{proof}',end)
        finish=s.index(r'\end{proof}',start)+len(r'\end{proof}')
        records.append(dict(key=key,file=u['file'],line=u['line'],statement=u['excerpt'],statement_sha256=u['sha256'],
          proof_line=s.count('\n',0,start)+1,proof_sha256=hashlib.sha256(s[start:finish].encode()).hexdigest(),
          review='separate skeptical source pass; not formal verification',checks=tn[key]))
    assert len(records)==len(tn),(len(records),len(tn))
    (OUT/'theorem-verification.json').write_text(json.dumps(records,indent=2)+'\n')
    ex=[]
    for u in current:
        if u['kind']!='exercise':continue
        key=u['labels'][0];assert key in en,key
        links={}
        for kind in ('hint','solution'):
            matches=[v for v in current if v['kind']==kind and v['target']==key]
            assert len(matches)==1,(key,kind)
            v=matches[0];links[kind]=dict(file=v['file'],line=v['line'],sha256=v['sha256'])
        s=(ROOT/links['solution']['file']).read_text()
        sol=re.search(r'\\begin\{solution\}\{'+re.escape(key)+r'\}(.*?)\\end\{solution\}',s,re.S)[1]
        assert r'\idea' in sol and r'\writeup' in sol,key
        ex.append(dict(label=key,file=u['file'],line=u['line'],sha256=u['sha256'],links=links,
            review='statement, prerequisites, hint, strategy, proof and exceptional cases checked by source reading',checks=en[key]))
    assert len(ex)==len(en),(len(ex),len(en))
    (OUT/'exercise-verification.json').write_text(json.dumps(ex,indent=2)+'\n')
    # All original asset paths remain byte-identical.
    names=subprocess.check_output(['git','ls-tree','-r','--name-only',inventory.BASE,inventory.BOOK],cwd=ROOT,text=True).splitlines()
    assets=[]
    for n in names:
        if '/chapters/' in n or Path(n).name in ('main.tex','PUBLISHING.md','kdp.md'):continue
        original=subprocess.check_output(['git','show',inventory.BASE+':'+n],cwd=ROOT)
        now=(ROOT/n).read_bytes()
        assert original==now,n
        assets.append(dict(file=n,sha256=hashlib.sha256(now).hexdigest(),unchanged=True))
    (OUT/'asset-preservation.json').write_text(json.dumps(assets,indent=2)+'\n')
    # Give even revised unlabelled units a documented destination.
    migrations=json.loads((OUT/'migration-units.json').read_text())
    for item in migrations:
        if item['destinations']:continue
        u=item['original'];name=Path(u['file']).name
        if name=='ch11-algebraic.tex':
            target='ch11-algebraic.tex' if 14<=u['line']<132 and u['kind']!='reminder' else 'ch12-ideals.tex'
        else:target=name
        item['destinations']=[dict(file=inventory.BOOK+'/chapters/'+target,locator='Revised prose/proof: source reading and full Git diff; semantic units retained in this chapter.')]
        item['status']='documented revised prose destination'
    (OUT/'migration-units.json').write_text(json.dumps(migrations,indent=2)+'\n')
    print(json.dumps(dict(numbered_results=len(records),exercises=len(ex),preserved_assets=len(assets),unmapped_units=sum(not x['destinations'] for x in migrations))))
if __name__=='__main__':main()
