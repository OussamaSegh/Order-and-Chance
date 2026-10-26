#!/bin/bash
# quick build of tome0 in a4 and print; report errors, overfull boxes, numbering changes
cd /home/claude/repo/tome0-back-in-shape
for fmt in a4 print; do
  for i in 1 2; do
    pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/home/claude/b0 -jobname=q-$fmt "\def\TOMENUM{0}\def\TOMETITLE{Back in Shape}\def\FORMAT{$fmt}\def\PRINTINNER{0.75in}\input{main.tex}" > /home/claude/b0/q-$fmt.stdout 2>&1 || { echo "FAIL $fmt"; grep -n -A12 "^!" /home/claude/b0/q-$fmt.stdout | head -60; exit 1; }
  done
  echo "$fmt: $(pdfinfo /home/claude/b0/q-$fmt.pdf | sed -n 's/Pages: *//p') pages; overfull>10pt: $(grep -c 'Overfull \\hbox ([1-9][0-9]\.\|Overfull \\hbox ([1-9][0-9][0-9]' /home/claude/b0/q-$fmt.log) ; multiply defined: $(grep -c 'multiply defined' /home/claude/b0/q-$fmt.log); undefined refs: $(grep -c 'Reference .* undefined' /home/claude/b0/q-$fmt.log)"
done
python3 - <<'PY'
import re
aux=open('/home/claude/b0/q-a4.aux').read()
new={}
for m in re.finditer(r'\\newlabel\{([^}]*)\}\{\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}',aux):
    lab,num,page,title,anchor=m.groups()
    if anchor.startswith(('theorem','exo')): new[lab]=num
old={}
for line in open('/home/claude/numbering-old.txt'):
    lab,num,anc=line.split(); old[lab]=num
bad=[(l,old[l],new.get(l)) for l in old if new.get(l)!=old[l]]
print("numbering changes vs first edition:", bad if bad else "none")
PY
