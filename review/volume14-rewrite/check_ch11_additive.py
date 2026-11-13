#!/usr/bin/env python3
"""Volume 14, Chapter 11 (additive combinatorics): small examples."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import check, check_true, finish
A = range(1, 101)
check("|A+A| for {1..100}", len({a + b for a in A for b in A}), 199, 0)
random.seed(1)
hits = 0
for _ in range(200):
    B = random.sample(range(1, 10**9), 100)
    hits += len({a + b for a in B for b in B}) == 5050
check_true(f"100 random numbers below 1e9: 5050 sums in {hits}/200 trials", hits >= 195)
A = [1, 2, 3, 4]
S = {a + b for a in A for b in A}; Pr = {a * b for a in A for b in A}
check("points of (A+A)x(AA)", len(S) * len(Pr), 63, 0)
pts = {(s, p) for s in S for p in Pr}
lines = {(a, b) for a in A for b in A}
check("lines", len(lines), 16, 0)
check_true("each line y=a(x-b) through at least 4 points",
           all(sum(1 for (x, y) in pts if y == a * (x - b)) >= 4 for a, b in lines))
# geometric progression: |A+A| = n(n+1)/2, |A.A| = 2n-1
for n in (8, 64, 512):
    G = [2**i for i in range(n)]
    check(f"GP n={n} |A+A|", len({a + b for a in G for b in G}), n * (n + 1) // 2, 0)
    check(f"GP n={n} |AA|", len({a * b for a in G for b in G}), 2 * n - 1, 0)
check("Rudnev-Stevens exponent", 4 / 3 + 2 / 1167, 1.33505, 1e-5)
finish()
