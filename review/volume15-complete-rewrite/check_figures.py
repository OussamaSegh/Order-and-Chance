#!/usr/bin/env python3
"""Check the added figure sources and chapter references. Not visual QA."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
V = ROOT / "volume15-order-and-chance"
UNITS = [
    ("ch01-integers", ["ra-anatomy"], ("v15c01-smooth", "v15c01-arcsine")),
    ("ch02-cramer", ["ra-largemoduli", "ra-gaps"], ("v15c02-buchstab", "v15c02-gaps")),
    ("ch03-divisors", ["ra-additive", "ra-selbergdelange", "ra-erdoskac"], ("v15c03-valuation", "v15c03-gaussian")),
    ("ch04-multiplicative", ["ra-randommult", "ra-polynomials"], ("v15c04-phases", "v15c04-cubics")),
    ("ch05-short", [], ("v15c05-series", "v15c05-patterns")),
    ("ch06-sieves", [], ("v15c06-bonferroni", "v15c06-factor")),
    ("ch07-classgroups", ["ra-cohenlenstra", "ra-symmoments"], ("v15c07-auts", "v15c07-product")),
    ("ch08-ranks", [], ("v15c08-chain", "v15c08-parity")),
    ("ch09-gue", ["moments-zeta"], ("v15c09-tent", "v15c09-surmise")),
    ("ch10-moments", ["ra-moments"], ("v15c10-split", "v15c10-arithmetic")),
    ("ch11-values", ["ra-bohrjessen", "ra-selberg"], ("v15c11-euler", "v15c11-bell")),
    ("ch12-pseudorandom", [], ("v15c12-cycle", "v15c12-progression")),
    ("ch13-bias", ["ra-bias"], ("v15c13-wave", "v15c13-symmetry")),
    ("ch14-meeting", [], ("v15c14-ledger", "v15c14-interval")),
]
INPUT = re.compile(r"\\input\{chapters/([^}]+)\}")


def expand(name):
    text = (V / "chapters" / f"{name}.tex").read_text()
    return INPUT.sub(lambda m: expand(m.group(1)), text)


for index, (name, _includes, stems) in enumerate(UNITS, 1):
    src = expand(name)
    assert len(stems) == 2
    for stem in stems:
        art = V / "figures" / f"{stem}.tex"
        assert art.is_file(), stem
        body = art.read_text()
        assert body.count(r"\begin{tikzpicture}") == 1, stem
        assert body.count(r"\end{tikzpicture}") == 1, stem
        assert src.count(r"\fig{" + stem + "}") == 1, stem
        assert src.count(r"\label{fig:" + stem + "}") == 1, stem
        assert len(body) > 80, stem
        assert not any(ord(c) < 32 and c not in "\n\t" for c in body), stem
    print(f"chapter {index:02}: 2 external TikZ plates and labels present")
print("PASS: 28 external TikZ assets referenced once (rendered inspection still required)")
