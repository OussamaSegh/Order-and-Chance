#!/usr/bin/env python3
"""Volume 14, Chapter 8 (small gaps): tuple counts, singular series, GPY ratios."""
import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import check, check_true, finish, primes_upto
import numpy as np
from mpmath import mp, mpf, quad, li, matrix, eig
from scipy.linalg import eigh
from scipy.integrate import quad as squad

X = 10**8
isp = np.ones(X + 20, dtype=bool); isp[:2] = False
for p in range(2, int((X + 20)**0.5) + 1):
    if isp[p]: isp[p*p::p] = False
def count(H):
    m = np.ones(X + 1, dtype=bool)
    for h in H: m &= isp[h:X + 1 + h]
    m[0] = False
    return int(m.sum())
def sing(H):
    s = 1.0
    for p in primes_upto(10**6):
        p = int(p); nu = len({h % p for h in H}); k = len(H)
        s *= (1 - nu / p) / (1 - 1 / p) ** k
    return s
def pred(H):
    k = len(H)
    return sing(H) * squad(lambda t: 1 / math.log(t) ** k, 2, X, limit=500)[0]
for H, c, S, r, tol in [((0, 2), 440312, 1.3203, 0.99987, 5e-5),
                        ((0, 2, 6), 55600, 2.8582, 1.002, 6e-4),
                        ((0, 4, 6), 55556, 2.8582, 1.001, 6e-4),
                        ((0, 2, 6, 8), 4768, 4.1512, 1.007, 6e-4)]:
    n = count(H)
    check(f"count {H} to 1e8", n, c, 0)
    check(f"singular series {H}", sing(H), S, 1e-4)
    check(f"ratio {H}", n / pred(H), r, tol)

def admissible(H):
    return all(len({h % p for h in H}) < p for p in primes_upto(len(H) + 1))
for H in [(0, 2, 6, 8, 12), (0, 4, 6, 10, 12, 16), (0, 2, 6, 8, 12, 18, 20)]:
    check_true(f"admissible {H}", admissible(H))

# GPY one-variable ratio: k * int Q^2 (1-x)^(k-2)/(k-2)! / int P^2 (1-x)^(k-1)/(k-1)!
def best_poly(k, deg=8):
    from math import factorial
    # basis P = x^i, Q = x^(i+1)/(i+1); Beta integrals int x^a (1-x)^b = a! b!/(a+b+1)!
    B = lambda a, b: math.exp(math.lgamma(a + 1) + math.lgamma(b + 1) - math.lgamma(a + b + 2))
    n = deg + 1
    I = np.array([[B(i + j, k - 1) / factorial(k - 1) for j in range(n)] for i in range(n)])
    J = np.array([[k * B(i + j + 2, k - 2) / factorial(k - 2) / ((i + 1) * (j + 1)) for j in range(n)] for i in range(n)])
    return eigh(J, I, eigvals_only=True)[-1]
def best_monomial(k):
    return max(2 * k * (2 * l + 1) / ((l + 1) * (k + 2 * l + 1)) for l in range(0, 200))
check("k=6 best polynomial", best_poly(6), 2.084, 5e-4)
check("k=6 best x^l", best_monomial(6), 2.000, 5e-4)
check("k=100 best polynomial", best_poly(100), 3.473, 5e-4)
check("k=100 best x^l", best_monomial(100), 3.303, 5e-4)
check("k=7, l=1 ratio", 2 * 7 * 3 / (2 * 10), 2.1, 1e-12)
check("level for k=6", 2 / best_poly(6), 0.96, 0.0005)
finish()
