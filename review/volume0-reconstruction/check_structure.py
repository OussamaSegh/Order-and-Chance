"""Check active manuscript navigation and preservation of original exercise triples."""
from collections import Counter
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
BOOK = ROOT/'tome0-mathematical-maturity'
OUT = Path(__file__).resolve().parent

def main():
    main = (BOOK/'main.tex').read_text()
    names = re.findall(r'\\input\{(chapters/[^}]+)\}',main)
    sources=[(name,(BOOK/(name+'.tex')).read_text()) for name in names]
    all_text='\n'.join(s for _,s in sources)
    errors=[]
    labels=re.findall(r'\\label\{([^}]+)\}',all_text)
    if len(labels)!=len(set(labels)): errors.append('duplicate active labels')
    refs=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',all_text)
    missing=sorted(set(refs)-set(labels))
    if missing: errors.append('unresolved source references: '+repr(missing))
    coverage={}
    all_ex=[]
    for name,source in sources:
        ex=re.findall(r'\\begin\{exercise\}(?:\[[^\]]*\])?\s*\\label\{([^}]+)\}',source)
        hints=re.findall(r'\\begin\{hint\}\{([^}]+)\}',source)
        solutions=re.findall(r'\\begin\{solution\}\{([^}]+)\}',source)
        if Counter(ex)!=Counter(hints) or Counter(ex)!=Counter(solutions): errors.append(name+': exercise pairing mismatch')
        for m in re.finditer(r'\\begin\{solution\}\{([^}]+)\}(.*?)\\end\{solution\}',source,re.S):
            if not all(x in m[2] for x in ('\\idea','\\writeup')): errors.append(m[1]+': missing discovery/write-up split')
        for asset in re.findall(r'\\fig\{([^}]+)\}',source):
            if not (BOOK/'figures'/(asset+'.tex')).exists(): errors.append('missing figure '+asset)
        coverage[name]=len(ex)
        all_ex+=ex
    baseline=json.loads((OUT/'baseline-inventory.json').read_text())['units']
    old_ex=[l for unit in baseline if unit['kind']=='exercise' for l in unit['labels'] if l.startswith('ex:')]
    if len(old_ex)!=130: errors.append('baseline inventory did not identify 130 exercises')
    lost=sorted(set(old_ex)-set(all_ex))
    if lost: errors.append('lost original exercises: '+repr(lost))
    if len(all_ex)!=len(set(all_ex)): errors.append('duplicate exercise identifiers')
    chapters=[re.search(r'\\chapter\{([^}]+)\}',s)[1] for _,s in sources if re.search(r'\\chapter\{([^}]+)\}',s)]
    result=dict(chapters=chapters,exercise_coverage=coverage,total_exercises=len(all_ex),original_exercises_retained=130-len(lost),explicit_labels=len(labels),explicit_references=len(refs),errors=errors)
    (OUT/'structure-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    if errors: raise SystemExit(1)

if __name__=='__main__': main()
