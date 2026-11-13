#!/usr/bin/env python3
"""List every cross-volume citation of a Volume 8 chapter with its context.

Usage: python3 review/volume9-rewrite/list_citations.py [chapter file ...]
A working tool for the rewrite: it prints file, line, the citation and 60
characters on each side, so each one can be read against the cited volume.
"""
import re, sys, pathlib
root = pathlib.Path(__file__).resolve().parents[2] / "volume8-analysis" / "chapters"
files = [pathlib.Path(f) for f in sys.argv[1:]] or sorted(root.glob("*.tex"))
pat = re.compile(r"Volumes?~\d+(?:,?\s*(?:Chapters?|Theorems?|Propositions?|Lemmas?|Corollar(?:y|ies)|Exercises?|Sections?|Appendix|Problems?|Definitions?|Examples?|Remarks?)~[\dA-Z.]+(?:\([a-z]\))?)?")
for f in files:
    for n, line in enumerate(f.read_text().splitlines(), 1):
        for m in pat.finditer(line):
            a, b = max(0, m.start() - 60), min(len(line), m.end() + 60)
            print(f"{f.name}:{n}: [{m.group(0)}] …{line[a:b]}…")
