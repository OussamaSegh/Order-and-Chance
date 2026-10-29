"""Generate the actual TOC, legacy numbering concordance and citation inventory."""
from pathlib import Path
import json
import re

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
BUILD=ROOT/'build/volume0-mathematical-maturity'

def numbers(text):
    return {m[1]:dict(number=m[2],page=m[3]) for m in re.finditer(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}\{([^}]+)\}',text)}

def main():
    base=OUT/'baseline-numbering.json'
    if not base.exists():
        original=Path('/workspace/volume0-checkpoints/A-integrated/main.aux').read_text()
        base.write_text(json.dumps(numbers(original),indent=2)+'\n')
    old=json.loads(base.read_text())
    new=numbers((BUILD/'main.aux').read_text())
    rows=['# Result and exercise numbering concordance','',
        'Original eight-chapter edition → revised ten-chapter edition. Page numbers',
        'are printed page labels, not physical PDF indices. Semantic labels are unchanged.','',
        '| Stable label | Original number | Revised number | Revised page |',
        '|---|---|---|---|']
    for label,value in old.items():
        target=new.get(label)
        if not target: raise AssertionError('Missing original label '+label)
        rows.append(f"| `{label}` | {value['number']} | {target['number']} | {target['page']} |")
    (OUT/'NUMBERING-CONCORDANCE.md').write_text('\n'.join(rows)+'\n')
    toc=['# Final table of contents','', 'Generated from the complete compiled manuscript.','']
    for m in re.finditer(r'\\contentsline \{(chapter|section|subsection)\}\{\\numberline \{([^}]+)\}([^}]*)\}\{([^}]+)\}',(BUILD/'main.toc').read_text()):
        level,num,title,page=m.groups()
        indent={'chapter':'','section':'  ','subsection':'    '}[level]
        toc.append(f'{indent}- {num} {title.strip()} — p. {page}')
    toc+=['','Back matter: A field guide to the next problem; Image credits.']
    (OUT/'TABLE-OF-CONTENTS.md').write_text('\n'.join(toc)+'\n')
    citations=[]
    pattern=re.compile(r'Volume\s*~?\s*0\b|Volume~0\b')
    for book in sorted(ROOT.glob('volume*')):
        if not book.is_dir() or book.name=='volume0-mathematical-maturity':continue
        for p in sorted(book.rglob('*.tex')):
            for i,line in enumerate(p.read_text().splitlines(),1):
                if pattern.search(line):citations.append(dict(file=str(p.relative_to(ROOT)),line=i,text=line))
    (OUT/'other-volume-citations.json').write_text(json.dumps(citations,indent=2)+'\n')
    (OUT/'OTHER-VOLUME-CITATIONS.md').write_text('\n'.join([
        '# Existing citations in other volumes','',
        'Read-only inventory; these manuscripts were not edited. Hardcoded old numbers',
        'must be checked against NUMBERING-CONCORDANCE.md before a coordinated series release.',
        'Some entries name only the volume and need no correction. No automatic rewrite is implied.','',
        *[f"- `{c['file']}:{c['line']}`: {c['text']}" for c in citations]
    ])+'\n')
    print(f'{len(old)} original labels mapped; {len(citations)} other-volume citation lines inventoried')

if __name__=='__main__':main()
