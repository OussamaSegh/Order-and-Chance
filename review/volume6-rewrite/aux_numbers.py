#!/usr/bin/env python3
"""Print 'number  label' for every label of a built volume, from its .aux file.

Usage: python3 review/volume6-rewrite/aux_numbers.py path/to/main.aux [regex]
Used to check hand-typed citations of another volume against that volume's labels.
"""
import re, sys
aux = open(sys.argv[1], encoding="utf-8", errors="replace").read()
pat = re.compile(sys.argv[2]) if len(sys.argv) > 2 else None
for m in re.finditer(r"\\newlabel\{([^}]+)\}\{\{([^}]*)\}\{(\d+)\}", aux):
    lab, num, page = m.groups()
    line = f"{num:8} {lab}  (p. {page})"
    if pat is None or pat.search(line):
        print(line)
