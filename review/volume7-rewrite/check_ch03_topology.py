#!/usr/bin/env python3
"""Volume 7, Chapter 3: the 29 topologies on three points (9 up to relabelling), the map h of Exercise 3.8."""
from itertools import combinations, permutations
from common import check, check_true, finish
pts = (0, 1, 2)
subsets = [frozenset(c) for r in range(4) for c in combinations(pts, r)]
tops = []
for r in range(len(subsets) + 1):
    for fam in combinations(subsets, r):
        fam = set(fam)
        if frozenset() in fam and frozenset(pts) in fam and all(a | b in fam and a & b in fam for a in fam for b in fam):
            tops.append(frozenset(fam))
check("topologies on three points", len(tops), 29, 0)
classes = {min(tuple(sorted(tuple(sorted(tuple(sorted(p[i] for i in s)) for s in t)))) for p in permutations(pts)) for t in tops}
check("up to relabelling", len(classes), 9, 0)
h = lambda t: t / (1 + abs(t)); hinv = lambda s: s / (1 - abs(s))
check_true("h inverse", all(abs(hinv(h(t)) - t) < 1e-9 for t in (-50, -1, 0, 0.3, 7)))
import math
check_true("sin(1/x_n) = (-1)^n", all(abs(math.sin(n * math.pi + math.pi / 2) - (-1) ** n) < 1e-9 for n in range(1, 30)))
finish()
