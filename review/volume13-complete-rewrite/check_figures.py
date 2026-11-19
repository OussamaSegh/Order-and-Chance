#!/usr/bin/env python3
"""Check all added figure sources and chapter references; not visual QA."""
from pathlib import Path
import re
V=Path(__file__).resolve().parents[2]/"volume13-arithmetic"
FILES=("ch11-algebraic","ch12-ideals-quadratic","ch01-number-fields","ch02-ideals","ch03-geometry","ch04-units","ch05-cyclotomic","ch12-padic","ch06-local","ch07-hasse","ch08-zeta","ch09-tate","ch10-cft","ch11-curves","ch12-elliptic","ch13-finite","ch14-modular")
for i,name in enumerate(FILES,1):
    src=(V/"chapters"/(name+".tex")).read_text()
    for x in "ab":
        stem=f"v13c{i:02}{x}"
        art=V/"figures"/(stem+".tex")
        assert art.is_file(), f"Missing {art}"
        s=art.read_text()
        assert s.count(r"\begin{tikzpicture}")==1 and s.count(r"\end{tikzpicture}")==1,stem
        assert src.count(r"\fig{"+stem+"}")==1,stem
        assert src.count(r"\label{fig:v13-extra-"+f"{i:02}"+f"-{x}"+r"}")==1,stem
        assert len(s)>80,stem
        assert not any(ord(c)<32 and c not in "\n\t" for c in s),stem
    print(f"chapter {i:02}: 2 external TikZ plates and labels present")
print("PASS: 34 external TikZ assets referenced once (rendered inspection still required)")
