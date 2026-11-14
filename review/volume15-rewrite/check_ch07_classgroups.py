#!/usr/bin/env python3
"""Recompute the printed numbers of Chapter 7 (ra-cohenlenstra.tex, ra-symmoments.tex, ch07-classgroups.tex)
and test the moment theorems by brute force on small cases."""
import math, itertools
import numpy as np
from common import check, check_true, finish

def cinf(p, N=200): return math.prod(1 - p ** -i for i in range(1, N))
for p, pr in [(2, 0.2888), (3, 0.5601), (5, 0.7603)]:
    check(f"c_inf({p})", cinf(p), pr, 5e-5)
c3 = cinf(3)
check("1-c_inf(3)", 1 - c3, 0.4399, 5e-5)
check("1-c_inf(5)", 1 - cinf(5), 0.2397, 5e-5)
check("1-c_inf(7)", 1 - cinf(7), 0.1632, 5e-5)
check("mu_CL(Z/3) = c/2 (28%)", c3 / 2, 0.28, 5e-3)
check("|GL_2(F_3)| = 48", (9 - 1) * (9 - 3), 48, 0)
check("|Aut Z/9| = 6", 6, 6, 0)
check("cyclic probability p=3", c3 * (1 + 3 / 4), 0.9802, 5e-5)
check("0.5601 x 1.75", 0.5601 * 1.75, 0.9802, 5e-5)
check("c p/(p-1) at p=3", c3 * 1.5, 0.840, 5e-4)
check("Z/3xZ/3 contribution c/(p(p-1))", c3 / 6, 0.093, 5e-4)
check("Z/3xZ/3 prob formula", c3 / (3 * 4 * 4), c3 / 48, 1e-15)
check("missing 0.160", 1 - c3 * 1.5, 0.160, 5e-4)
# sum over all groups of c/|Aut| = 1: enumerate partitions with parts <= 6 and at most 8 parts (p=3)
def aut_order(parts, p):
    parts = sorted(parts, reverse=True)
    r = lambda k: sum(1 for a in parts if a >= k)
    e = sum(r(k) ** 2 for k in range(1, (parts[0] if parts else 0) + 1))
    m = {}
    for a in parts: m[a] = m.get(a, 0) + 1
    return p ** e * math.prod(math.prod(1 - p ** -i for i in range(1, ma + 1)) for ma in m.values())
def partitions(n, maxpart):
    if n == 0: yield []; return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k): yield [k] + rest
tot = sum(c3 / aut_order(pa, 3) for n in range(0, 25) for pa in partitions(n, n))
check("sum of Cohen-Lenstra weights (|G| <= 3^24)", tot, 1.0, 1e-6)
# rank law
for r in range(4):
    pr = sum(c3 / aut_order(pa, 3) for n in range(0, 25) for pa in partitions(n, n) if len(pa) == r)
    check(f"P(rank={r}) formula", pr, c3 * 3 ** (-r * r) / math.prod((1 - 3 ** -i) ** 2 for i in range(1, r + 1)), 1e-6)

# ---------- Friedman-Washington: exact finite-n formula against Monte Carlo, n=12 over Z/81 ----------
def snf_valuations(M, p, e):
    """p-adic valuations of the elementary divisors of M over Z/p^e (returns list, e for zero)."""
    M = [list(map(int, row)) for row in M]
    n = len(M); q = p ** e; vals = []
    def v(x):
        if x % q == 0: return e
        k = 0
        while x % p == 0: x //= p; k += 1
        return k
    rows = list(range(n)); cols = list(range(n))
    A = M
    for step in range(n):
        best = None
        for i in range(step, n):
            for j in range(step, n):
                vv = v(A[i][j])
                if best is None or vv < best[0]: best = (vv, i, j)
                if vv == 0: break
            if best and best[0] == 0: break
        vv, i, j = best
        vals.append(vv)
        if vv == e:
            vals += [e] * (n - step - 1); break
        A[step], A[i] = A[i], A[step]
        for row in A: row[step], row[j] = row[j], row[step]
        piv = A[step][step]; u = piv // p ** vv; uinv = pow(u, -1, q)
        for i2 in range(step + 1, n):
            if A[i2][step] % q:
                f = (A[i2][step] // p ** vv) * uinv % q
                A[i2] = [(a - f * b) % q for a, b in zip(A[i2], A[step])]
        for j2 in range(step + 1, n):
            if A[step][j2] % q:
                f = (A[step][j2] // p ** vv) * uinv % q
                for row in A: row[j2] = (row[j2] - f * row[step]) % q
    return sorted([x for x in vals if x > 0], reverse=True)
rng = np.random.default_rng(7)
n, e, p = 12, 4, 3
counts = {}
NS = 3000
for _ in range(NS):
    t = tuple(snf_valuations(rng.integers(0, p ** e, (n, n)), p, e))
    counts[t] = counts.get(t, 0) + 1
def fw(parts):
    r = len(parts)
    return math.prod(1 - p ** (i - n) for i in range(r)) * math.prod(1 - p ** -j for j in range(1, n + 1)) / aut_order(list(parts), p)
for G in [(), (1,), (2,), (1, 1)]:
    check(f"P(cok = {G}) MC (3000 samples) vs Friedman-Washington", counts.get(G, 0) / NS, fw(G), 0.025)
check("Z/9 vs Z/3xZ/3 weight ratio", fw((2,)) / fw((1, 1)), 8.0, 0.01)

# ---------- Theorem cokmoments and symmoments by brute force ----------
def sur_count_moment(n, k, G, symmetric):
    """E #Sur(cok M, G) for uniform (symmetric) n x n M over Z/p^k, p=2, G given by its cyclic orders (powers of 2)."""
    q = 2 ** k
    gens = list(itertools.product(*[range(o) for o in G]))   # elements of G
    # surjections F: R^n -> G given by images of basis vectors (must be well defined: o | q always)
    def generates(imgs):
        # subgroup generated: close under addition
        S = {tuple(0 for _ in G)}; frontier = list(S)
        while frontier:
            new = []
            for s in frontier:
                for g in imgs:
                    t = tuple((a + b) % o for a, b, o in zip(s, g, G))
                    if t not in S: S.add(t); new.append(t)
            frontier = new
        return len(S) == math.prod(G)
    Fs = [imgs for imgs in itertools.product(gens, repeat=n) if generates(imgs)]
    Farr = np.array(Fs)                       # (#F, n, len(G))
    if symmetric:
        idx = [(i, j) for i in range(n) for j in range(i, n)]
    else:
        idx = [(i, j) for i in range(n) for j in range(n)]
    total = 0; count = 0
    Gv = np.array(G)
    for vals in itertools.product(range(q), repeat=len(idx)):
        M = np.zeros((n, n), dtype=np.int64)
        for (i, j), v in zip(idx, vals):
            M[i, j] = v
            if symmetric: M[j, i] = v
        # F(M e_j) = sum_i M[i,j] F(e_i)
        img = np.einsum('ij,fil->fjl', M, Farr) % Gv
        total += int(np.sum(np.all(img == 0, axis=(1, 2)))); count += 1
    return total / count
def wedge(G):
    lam = [int(round(math.log2(o))) for o in G]
    return 2 ** sum(min(a, b) for a, b in itertools.combinations(lam, 2))
def sur_factor(n, G):
    r = len(G)
    return math.prod(1 - 2.0 ** (i - n) for i in range(r))
for n, k, G in [(3, 1, (2,)), (3, 1, (2, 2)), (2, 2, (4,)), (2, 2, (2, 4))]:
    val = sur_count_moment(n, k, G, symmetric=False)
    check(f"cokmoments n={n} k={k} G={G}", val, sur_factor(n, G), 1e-12)
for n, k, G in [(3, 1, (2,)), (3, 1, (2, 2)), (4, 1, (2, 2)), (3, 2, (4,)), (3, 2, (2, 4)), (3, 2, (4, 4))]:
    val = sur_count_moment(n, k, G, symmetric=True)
    check(f"symmoments n={n} k={k} G={G}", val, sur_factor(n, G) * wedge(G), 1e-12)

# ---------- Exercise clrank (a): number of n x n matrices of rank n-r over F_2, n=3 ----------
def rank_f2(M):
    M = [row[:] for row in M]; r = 0; n = len(M)
    for c in range(n):
        piv = next((i for i in range(r, n) if M[i][c]), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(n):
            if i != r and M[i][c]: M[i] = [a ^ b for a, b in zip(M[i], M[r])]
        r += 1
    return r
from collections import Counter
cnt = Counter(rank_f2([list(bits[3 * i:3 * i + 3]) for i in range(3)]) for bits in itertools.product([0, 1], repeat=9))
pp, nn = 2, 3
for r in range(4):
    k = nn - r
    num = math.prod((pp ** nn - pp ** i) ** 2 for i in range(k)); den = math.prod(pp ** k - pp ** i for i in range(k))
    check(f"rank {k} matrices over F_2, n=3", cnt[k], num / den, 0)
finish()
