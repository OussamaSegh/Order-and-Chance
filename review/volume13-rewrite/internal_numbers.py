#!/usr/bin/env python3
"""Find hand-typed statement numbers inside Volume 8 and resolve them to labels.

Usage: python3 review/volume10-rewrite/internal_numbers.py [--apply] [chapter file ...]
A number such as "Theorem~5.5" that is not part of a citation of another volume is
looked up in the order printed BEFORE the rewrite (baseline-numbering.txt). With --apply it is
replaced by \\ref{label} when the kind matches and the statement has a label.
Everything else is printed for a manual decision.
"""
import re, sys, subprocess, pathlib
root = pathlib.Path(__file__).resolve().parents[2]
apply = "--apply" in sys.argv
args = [a for a in sys.argv[1:] if a != "--apply"]
files = [pathlib.Path(a) for a in args] or sorted((root / "volume8-analysis/chapters").glob("*.tex"))
# The hand-typed numbers were written against the order before the rewrite.
out = (root / "review/volume10-rewrite/baseline-numbering.txt").read_text()
table = {}
for l in out.splitlines():
    if l.startswith("=="): continue
    p = l.split()
    table[("exercise" if p[1] == "exercise" else "stmt", p[0])] = (p[1], p[2], l[40:110])
kinds = r"(Theorems?|Propositions?|Lemmas?|Corollar(?:y|ies)|Exercises?|Problems?|Definitions?|Examples?)"
pat = re.compile(kinds + r"~(\d+\.\d+)((?:(?:, |,? and~|--)\d+\.\d+)*)")
def norm(k):
    k = k.lower()
    k = {"corollaries": "corollary"}.get(k, k.rstrip("s"))
    return k
for f in files:
    t = f.read_text()
    head, sep, tail = t.partition("\\section*{Sources")
    def rep(m):
        pre = head[max(0, m.start() - 30):m.start()]
        if re.search(r"Volumes?~\d+,? \(?$|Volume~\d+ \($", pre): return m.group(0)
        kind = norm(m.group(1))
        nums = [m.group(2)] + re.findall(r"\d+\.\d+", m.group(3))
        res, ok = [], True
        for n in nums:
            key = ("exercise" if kind in ("exercise", "problem") else "stmt", n)
            e = table.get(key)
            if not e or e[1] == "-" or (kind not in ("exercise", "problem") and len(nums) == 1 and e[0] != kind):
                ok = False
            res.append(e)
        line = head.count("\n", 0, m.start()) + 1
        print(f"{f.name}:{line}: {m.group(0)!r} -> {[(e[0], e[1], e[2][:50]) if e else None for e in res]} {'OK' if ok else 'MANUAL'}")
        if apply and ok:
            s = m.group(0)
            for n, e in zip(nums, res):
                s = s.replace(n, "\\ref{%s}" % e[1], 1)
            return s
        return m.group(0)
    head = pat.sub(rep, head)
    if apply: f.write_text(head + sep + tail)
