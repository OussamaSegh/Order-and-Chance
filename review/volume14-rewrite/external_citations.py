#!/usr/bin/env python3
"""Citations of Volume 14 in other volumes: old number (baseline, before Waring) -> label -> number today.

Run before fixing: it reads every cited number as a baseline number. After the fix (2026-11-13)
the four citations it flagged read 14.15, 10.4, 9.5 and 7.5 and are correct."""
import re, sys, pathlib, subprocess
ROOT = pathlib.Path(__file__).resolve().parents[2]
HERE = pathlib.Path(__file__).parent
def parse(text):
    out = {}; ch = None
    for line in text.splitlines():
        m = re.match(r'^(\d+\.\d+)\s+(\w+)\s+(\S+)', line)
        if m: out.setdefault((m.group(2), m.group(1)), m.group(3))
    return out
base = parse((HERE / 'baseline-numbering.txt').read_text())
now_txt = subprocess.run([sys.executable, str(HERE / 'statements.py'), str(ROOT / 'volume14-primes')], capture_output=True, text=True).stdout
now = parse(now_txt)
label_now = {}
for (kind, num), lab in now.items(): label_now.setdefault(lab, (kind, num))
KIND = {'theorem': 'theorem', 'lemma': 'lemma', 'proposition': 'proposition', 'corollary': 'corollary', 'exercise': 'exercise', 'definition': 'definition', 'remark': 'remark', 'example': 'example'}
pat = re.compile(r'Volume~14,?\s*(Theorems?|Lemmas?|Propositions?|Corollar(?:y|ies)|Exercises?|Definitions?|Remarks?|Examples?|Chapters?)~?(\d+(?:\.\d+)?)((?:(?:,|~and|\s+and)~?\d+(?:\.\d+)?)*)')
for f in sorted(ROOT.glob('volume*/**/*.tex')):
    if 'volume14-primes' in str(f): continue
    for i, line in enumerate(f.read_text().splitlines(), 1):
        for m in pat.finditer(line):
            word = m.group(1).lower()
            nums = [m.group(2)] + re.findall(r'\d+(?:\.\d+)?', m.group(3))
            for n in nums:
                if word.startswith('chapter'):
                    c = int(n); new = c + 1 if c >= 6 else c
                    print(f"{f.relative_to(ROOT)}:{i}: Chapter {n} -> Chapter {new}")
                    continue
                kind = 'corollary' if word.startswith('corollar') else word.rstrip('s')
                lab = None
                for k in ([kind] if kind != 'theorem' else ['theorem']) + list(KIND):
                    if (k, n) in base: lab = base[(k, n)]; break
                newk, newn = label_now.get(lab, ('?', '?'))
                flag = '' if n == newn and newk == kind else '   <-- CHANGE'
                print(f"{f.relative_to(ROOT)}:{i}: {word} {n} = {lab} -> {newk} {newn}{flag}")
