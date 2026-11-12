#!/usr/bin/env python3
"""Volume 8, Chapter 12: the 251 minors, Chebotarev's lemma for p = 5 and 7, Tao's theorem and its converse for p = 5,
a composite counterexample, Gauss sum multiplicativity and quadratic reciprocity, sums of two squares mod p, the circle
over F_p, the MacWilliams identity for the Hamming code, the majority function and the BLR test, cap sets in small
dimension, Meshulam's final inequality, and the Ellenberg-Gijswijt constant."""
from itertools import combinations, product
from math import comb, log, log2
import numpy as np
from sympy import legendre_symbol as leg, primerange
from scipy.optimize import minimize_scalar
from common import check, check_true, finish
check("number of square minors of a 5x5 matrix", sum(comb(5, n)**2 for n in range(1, 6)), 251, 0)
for p in (5, 7):
    F = np.exp(2j*np.pi*np.outer(range(p), range(p))/p); mn = 1e9
    for n in range(1, p + 1):
        for R in combinations(range(p), n):
            for C in combinations(range(p), n):
                mn = min(mn, abs(np.linalg.det(F[np.ix_(R, C)])))
    check_true(f"Chebotarev: every minor of the {p}x{p} Fourier matrix is non-zero (min |det| = {mn:.3g})", mn > 1e-6)
# Tao converse for p = 5: for every A, B with |A|+|B| = 6 there is f with these supports
p = 5; F = np.exp(-2j*np.pi*np.outer(range(p), range(p))/p)/p; ok = True
for a in range(1, p + 1):
    for A in combinations(range(p), a):
        for B in combinations(range(p), p + 1 - a):
            M = F[np.ix_([b for b in range(p) if b not in B], list(A))]
            ns = np.linalg.svd(M)[2].conj().T[:, -1] if M.shape[0] else np.ones(len(A))
            f = np.zeros(p, complex); f[list(A)] = ns; fh = F @ f
            ok &= set(np.nonzero(abs(f) > 1e-9)[0]) == set(A) and set(np.nonzero(abs(fh) > 1e-9)[0]) == set(B)
check_true("Tao's converse for p = 5: every pair of supports with |A|+|B| = 6 occurs", ok)
# composite: subgroup indicator in Z/12 with u = 3, v = 4
n = 12; f = np.array([1.0 if k % 3 == 0 else 0 for k in range(n)]); fh = np.fft.fft(f)/n
check("Z/12: |supp f| + |supp f^| for f = 1_{3Z/12Z}", (abs(f) > 1e-9).sum() + (abs(fh) > 1e-9).sum(), 3 + 4, 0)
check("Z/12: Donoho-Stark equality |supp f| |supp f^| = 12", (abs(f) > 1e-9).sum()*(abs(fh) > 1e-9).sum(), 12, 0)
e = lambda t: np.exp(2j*np.pi*t)
G = lambda a, n: sum(e(a*x*x/n) for x in range(n))
eps = lambda n: 1 if n % 4 == 1 else 1j
for n in (3, 5, 7, 11, 15, 21, 35): check(f"G(1;{n}) = eps_n sqrt(n)", abs(G(1, n) - eps(n)*n**0.5), 0, 1e-9)
for p in (3, 5, 7, 11, 13):
    check_true(f"G(a;{p}) = (a/p) G(1;{p}) for all a", all(abs(G(a, p) - leg(a, p)*G(1, p)) < 1e-9 for a in range(1, p)))
for m, nn in ((3, 5), (5, 7), (3, 11), (7, 9)):
    for a in (1, 2): check(f"G({a};{m*nn}) = G({a*nn};{m}) G({a*m};{nn})", abs(G(a, m*nn) - G(a*nn, m)*G(a*m, nn)), 0, 1e-8)
ps = list(primerange(3, 60))
check_true("quadratic reciprocity for odd primes below 60", all(leg(p, q)*leg(q, p) == (-1)**((p - 1)//2*(q - 1)//2) for p in ps for q in ps if p != q))
# sums of two squares
for p in primerange(3, 40):
    Q = {x*x % p for x in range(1, p)}
    for a in range(1, p):
        N = sum(1 for x in Q for y in Q if (x + y) % p == a)
        if N != (p - 2 - leg(-1, p))/4 - leg(a, p)/2: check_true(f"N({a}) mod {p}", False)
    check_true(f"p = {p}: every a != 0 is a sum of two non-zero squares iff p >= 7", all(any((x + y) % p == a for x in Q for y in Q) for a in range(1, p)) == (p >= 7))
    check(f"#(x^2+y^2=1) mod {p}", sum(1 for x in range(p) for y in range(p) if (x*x + y*y) % p == 1), p - leg(-1, p), 0)
# MacWilliams for the Hamming [7,4] code
H = np.array([[1,0,1,0,1,0,1],[0,1,1,0,0,1,1],[0,0,0,1,1,1,1]])
C = [v for v in product((0, 1), repeat=7) if not (H @ v % 2).any()]
D = {tuple(np.array(c) @ H % 2) for c in product((0, 1), repeat=3)}
check_true("Hamming code weights 1,7,7,1", sorted(sum(c) for c in C) == [0] + [3]*7 + [4]*7 + [7])
dual = [v for v in product((0, 1), repeat=7) if all(np.dot(v, c) % 2 == 0 for c in C)]
check_true("dual of Hamming: one word of weight 0, seven of weight 4", sorted(sum(v) for v in dual) == [0] + [4]*7)
import sympy as sp
X, Y = sp.symbols("X Y")
W = lambda code, X, Y: sum(X**(7 - sum(c))*Y**sum(c) for c in code)
check_true("MacWilliams identity for the Hamming code", sp.expand(W(dual, X, Y) - W(C, X + Y, X - Y)/len(C)) == 0)
# majority
pts = list(product((1, -1), repeat=3)); Maj = {x: 1 if sum(x) > 0 else -1 for x in pts}
check_true("Maj = (x1+x2+x3)/2 - x1x2x3/2", all(Maj[x] == (x[0] + x[1] + x[2])/2 - x[0]*x[1]*x[2]/2 for x in pts))
acc = np.mean([Maj[x]*Maj[y] == Maj[tuple(a*b for a, b in zip(x, y))] for x in pts for y in pts])
check("BLR acceptance probability of majority", acc, 5/8, 1e-12)
check("distance from majority to x1", np.mean([Maj[x] != x[0] for x in pts]), 1/4, 1e-12)
# cap sets: largest caps in F_3^2 and F_3^3 are 4 and 9
def maxcap(n):
    V = list(product(range(3), repeat=n)); idx = {v: i for i, v in enumerate(V)}
    third = lambda a, b: idx[tuple((-x - y) % 3 for x, y in zip(V[a], V[b]))]
    best = 0
    def grow(S, start):
        nonlocal best; best = max(best, len(S))
        for c in range(start, len(V)):
            if all(third(a, c) not in S for a in S): grow(S | {c}, c + 1)
    grow(frozenset({0}), 1); return best
check("largest cap in F_3^2", maxcap(2), 4, 0)
check("largest cap in F_3^3", maxcap(3), 9, 0)
check_true("x+y+z = 0 in F_3 iff all equal or all different", all(((x + y + z) % 3 == 0) == (len({x, y, z}) in (1, 3)) for x, y, z in product(range(3), repeat=3)))
# Meshulam: for n > 32 and alpha just above 32/n the right side is < n
check_true("Meshulam: 8/a + log2(1/a) + 1 + log3(2/a^2) < n at a = 32/n, n = 33..10^5", all(8/a + log2(1/a) + 1 + log(2/a**2, 3) < n for n in range(33, 100001) for a in [32/n]))
check_true("2 log2 n <= n/2 for n >= 16", all(2*log2(n) <= n/2 for n in range(16, 10**5)))
# Ellenberg-Gijswijt
g = lambda t: (1 + t + t*t)/t**(2/3)
check("(1+0.6+0.36)/0.6^(2/3)", g(0.6), 2.7552, 1e-4)
r = minimize_scalar(g, bounds=(0.3, 1), method="bounded")
check("optimal t", r.x, 0.5931, 1e-3); check("optimal value", r.fun, 2.7551, 1e-4)
check_true("M_d <= (1+t+t^2)^n / t^d for n = 6, d = 4, t = 0.6", sum(1 for e_ in product(range(3), repeat=6) if sum(e_) <= 4) <= g(0.6)**6*0.6**(2*6/3 - 4))
finish()
