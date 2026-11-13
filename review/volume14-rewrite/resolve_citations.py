#!/usr/bin/env python3
"""Print each numbered cross-volume citation of a chapter beside the statement that number has today.

Usage: python3 review/volume14-rewrite/resolve_citations.py volume8-analysis/chapters/ch01-banach.tex
The cited volume's printed order comes from statements.py. A human then reads the two
columns: the tool only shows what the number points to, it does not judge the match.
"""
import re, sys, subprocess, pathlib, functools
root = pathlib.Path(__file__).resolve().parents[2]
dirs = {int(re.match(r"volume(\d+)", p.name).group(1)): p.name for p in root.glob("volume*-*")}
@functools.cache
def table(v):
    out = subprocess.run([sys.executable, str(root / "review/volume14-rewrite/statements.py"), dirs[v]], capture_output=True, text=True).stdout
    t = {}
    for l in out.splitlines():
        if l.startswith("=="):
            p = l.split(None, 2); t[("chapter", p[1])] = p[2][:60]; continue
        p = l.split()
        t[("exercise" if p[1] == "exercise" else "stmt", p[0])] = f"{p[1]} {p[2]} {l[40:100]}"
    return t
kinds = r"(Chapters?|Theorems?|Propositions?|Lemmas?|Corollar(?:y|ies)|Exercises?|Problems?|Definitions?|Examples?|Appendix)"
pat = re.compile(r"Volume~(\d+),?\s*\(?" + kinds + r"~([\dA-Z]+(?:\.\d+)?)((?:(?:, |,? and~|--|,? and " + kinds + r"~)[\dA-Z]+\.\d+)*)")
for f in sys.argv[1:]:
    for n, line in enumerate(pathlib.Path(f).read_text().splitlines(), 1):
        for m in pat.finditer(line):
            v, kind = int(m.group(1)), m.group(2).lower()
            nums = [m.group(3)] + re.findall(r"[\dA-Z]+\.\d+", m.group(4))
            for x in nums:
                key = ("chapter", x) if kind.startswith(("chapter", "appendix")) else ("exercise" if kind.startswith(("exercise", "problem")) else "stmt", x)
                print(f"{pathlib.Path(f).name}:{n}: V{v} {m.group(2)} {x} -> {table(v).get(key, 'MISSING')}")
                a = max(0, m.start() - 90); print("      …" + line[a:m.start()].strip())
