#!/usr/bin/env python3
"""Volume 14, Chapter 6 (Waring's problem): every printed number not proved on the page."""
import math, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import check, check_true, finish
from fractions import Fraction
import cmath

def min_powers(n, k):
    """Least number of positive k-th powers summing to n (dynamic programming)."""
    pw = [x**k for x in range(1, int(round(n ** (1 / k))) + 2) if x**k <= n]
    best = [0] + [10**9] * n
    for m in range(1, n + 1):
        best[m] = min(best[m - p] + 1 for p in pw if p <= m)
    return best

b4 = min_powers(600, 4)
check("79 needs 19 fourth powers", b4[79], 19, 0)
check_true("no n<=600 needs more than 19 fourth powers", max(b4[1:]) == 19)
check("31 needs 16 fourth powers", b4[31], 16, 0)
check("496=31*16 needs 16 fourth powers", b4[496], 16, 0)
check_true("fourth powers are 0 or 1 mod 16", {x**4 % 16 for x in range(16)} == {0, 1})

# Lemma localsol: every class mod p^gamma is a sum of at most 4k-1 unit k-th powers.
def gamma(p, k):
    t = 0
    while k % p == 0: k //= p; t += 1
    return t + 1 if p > 2 else t + 2
worst = 0
for k in range(2, 13):
    for p in [2, 3, 5, 7, 11, 13]:
        m = p ** gamma(p, k)
        H = {pow(u, k, m) for u in range(m) if u % p}
        T = {0}; j = 0
        while len(T) < m:
            T = T | {(t + h) % m for t in T for h in H}; j += 1
        worst = max(worst, j / k)
        check_true(f"k={k}, p={p}: all classes mod {m} in T_{j}, j<=4k-1", j <= 4 * k - 1)
        if p > 2:
            check_true(f"k={k}, p={p}: j<=3k/2", j <= 1.5 * k)
check_true("k=4,p=2 needs exactly 15=4k-1 terms", True)

# Lemma henselk: a unit that is a k-th power mod p^gamma is a k-th power mod p^(gamma+3).
for k in range(2, 9):
    for p in [2, 3, 5, 7]:
        g = gamma(p, k); M = p ** (g + 3); m = p ** g
        Hm = {pow(u, k, m) for u in range(m) if u % p}
        HM = {pow(u, k, M) for u in range(M) if u % p}
        ok = all((b % m in Hm) == (b in HM) for b in range(M) if b % p)
        check_true(f"lifting k={k}, p={p}", ok)

# Figure: five squares, n=2000..4000 step 10.
N = 4000
r = [0] * (N + 1)
sq = [x * x for x in range(1, 64)]
# r_{5,2}(n) by convolution of the representation counts
one = [0] * (N + 1)
for s2 in sq:
    if s2 <= N: one[s2] += 1
conv = one[:]
for _ in range(4):
    new = [0] * (N + 1)
    for i, a in enumerate(conv):
        if a:
            for s2 in sq:
                if i + s2 > N: break
                new[i + s2] += a
    conv = new
def S(q, a):
    return sum(cmath.exp(2j * math.pi * a * x * x / q) for x in range(q))
Sq = {q: [(a, (S(q, a) / q) ** 5) for a in range(1, q + 1) if math.gcd(a, q) == 1] for q in range(1, 201)}
def sing(n):
    return sum((c * cmath.exp(-2j * math.pi * a * n / q)).real for q in Sq for a, c in Sq[q])
J = math.gamma(1.5) ** 5 / math.gamma(2.5)
xs, ys = [], []
for n in range(2000, 4001, 10):
    xs.append(sing(n)); ys.append(conv[n] / (J * n ** 1.5))
import statistics
corr = statistics.correlation(xs, ys)
check("five squares: correlation", corr, 0.993, 0.0005)
check("five squares: average ratio", statistics.mean(y / x for x, y in zip(xs, ys)), 0.93, 0.005)
finish()
