#!/usr/bin/env python3
"""Heuristic prose comparison against starting main, including short sentences.

Excludes figures, centered blocks and bibliography; those need manual review.
Mathematics and references are masked. Formula-only introducers (Let <math>)
are not explanatory sentences. This checks coverage, never prose quality.
"""
import json,re,subprocess
from pathlib import Path
root=Path(__file__).resolve().parents[2]; inv=json.loads((root/'review/volume10-complete-rewrite/starting-source.json').read_text())
def sentences(s):
 s=s.split('\\section*{Sources and further reading}')[0]
 s=re.sub(r'\\begin\{(figure|center)\}.*?\\end\{\1\}', ' ',s,flags=re.S)
 s=re.sub(r'(?m)(?<!\\)%.*$', ' ',s)
 s=re.sub(r'\\\[.*?\\\]|\\\(.*?\\\)|(?<!\\)\$\$.*?(?<!\\)\$\$|(?<!\\)\$.*?(?<!\\)\$', ' MATH ',s,flags=re.S)
 s=re.sub(r'\\(?:chapter|section|subsection|subsubsection)\*?(?:\[[^]]*\])?\{[^}]*\}',' ',s)
 s=re.sub(r'\\(?:label|begin|end)\{[^}]*\}(?:\[[^]]*\])?', ' ',s)
 s=re.sub(r'\\(?:ref|eqref|pageref)\{[^}]*\}', ' REF ',s)
 s=re.sub(r'\\[a-zA-Z]+\*?(?:\[[^]]*\])?', ' ',s)
 s=s.replace('~',' ').replace('{','').replace('}','')
 s=re.sub(r'\s+',' ',s).strip()
 return [x.strip() for x in re.split(r'(?<=[.!?])\s+',s) if len(re.findall(r'\b(?!MATH\b|REF\b)[A-Za-z]{2,}\b',x))>=2]
rows=[]
for u in inv['printed_units']:
 p=u['path'];old=subprocess.check_output(['git','show',inv['starting_main_sha']+':'+p],cwd=root,text=True);new=(root/p).read_text();a=sentences(old);b=set(sentences(new));same=[x for x in a if x in b]
 rows.append({'path':p,'old_sentences':len(a),'new_sentences':len(sentences(new)),'unchanged':same})

for r in rows:
 print(r['path'],r['old_sentences'],'->',r['new_sentences'],'unchanged:',len(r['unchanged']))
 for x in r['unchanged']: print('  '+x)
