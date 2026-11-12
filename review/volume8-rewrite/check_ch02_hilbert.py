#!/usr/bin/env python3
"""Volume 8, Chapter 2: Legendre norms, the best quadratic fit of |x| (ex:legendrefit), the Beta integral of the
Legendre proof, van der Corput's inequality on random data, Szego's kernel bound, kernel ridge regression."""
from fractions import Fraction as F
from math import factorial, sqrt, pi
import cmath, random
import numpy as np
from common import check, check_true, finish
# polynomials as coefficient lists with Fraction entries
def mul(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): c[i + j] += x * y
    return c
def der(a): return [i * a[i] for i in range(1, len(a))] or [F(0)]
def integ(a, lo=-1, hi=1): return sum(c * (F(hi) ** (i + 1) - F(lo) ** (i + 1)) / (i + 1) for i, c in enumerate(a))
def legendre(n):
    u = [F(1)]
    for _ in range(n): u = mul(u, [F(-1), F(0), F(1)])
    for _ in range(n): u = der(u)
    return [c / (2 ** n * factorial(n)) for c in u]
P = [legendre(n) for n in range(7)]
check_true("P_2 = (3x^2-1)/2", P[2] == [F(-1, 2), 0, F(3, 2)])
check_true("P_3 = (5x^3-3x)/2", P[3] == [0, F(-3, 2), 0, F(5, 2)])
for n in range(7):
    check_true(f"int P_{n}^2 = 2/(2n+1)", integ(mul(P[n], P[n])) == F(2, 2 * n + 1))
    for m in range(n): check_true(f"P_{n} orthogonal to P_{m}", integ(mul(P[n], P[m])) == 0)
    # Beta integral: int (1-x^2)^n = 2^(2n+1) (n!)^2 / (2n+1)!
    u = [F(1)]
    for _ in range(n): u = mul(u, [F(1), F(0), F(-1)])
    check_true(f"Beta integral n={n}", integ(u) == F(2 ** (2 * n + 1) * factorial(n) ** 2, factorial(2 * n + 1)))
# ex:legendrefit: c_n = (2n+1)/2 * 2 * int_0^1 x P_n (even n)
c0 = F(1, 2) * 2 * integ(mul([0, 1], P[0]), 0, 1)
c2 = F(5, 2) * 2 * integ(mul([0, 1], P[2]), 0, 1)
check_true("c_0 = 1/2, c_2 = 5/8", (c0, c2) == (F(1, 2), F(5, 8)))
p = [c0 * a + c2 * b for a, b in zip(P[0] + [0, 0], P[2])]
check_true("p = 3/16 + 15/16 x^2", p == [F(3, 16), 0, F(15, 16)])
err = 2 * integ(mul([-p[0], 1, -p[2]], [-p[0], 1, -p[2]]), 0, 1)
check_true("minimum = 1/96", err == F(1, 96))
# van der Corput (a) on random complex data
random.seed(1)
for N, H in ((30, 1), (30, 7), (50, 50)):
    u = [complex(random.gauss(0, 1), random.gauss(0, 1)) for _ in range(N)]
    g = lambda r: sum(u[m + r] * u[m].conjugate() for m in range(N) if 0 <= m + r < N)
    rhs = (N + H - 1) / H ** 2 * sum((H - abs(r)) * g(r) for r in range(-H + 1, H)).real
    check_true(f"van der Corput N={N} H={H}", abs(sum(u)) ** 2 <= rhs + 1e-9)
# n^2 sqrt(2) mod 1: Weyl sums are small
for k in (1, 2, 3):
    s = abs(sum(cmath.exp(2j * pi * k * n * n * sqrt(2)) for n in range(1, 20001))) / 20000
    check_true(f"Weyl sum of n^2 sqrt2, k={k}, is small ({s:.4f})", s < 0.02)
# Szego kernel: |f(w)| <= ||f|| (1-|w|^2)^(-1/2), equality for f = k_w
w = 0.3 + 0.4j
a = [w.conjugate() ** n for n in range(400)]
norm = sqrt(sum(abs(x) ** 2 for x in a)); val = abs(sum(x * w ** n for n, x in enumerate(a)))
check("Szego: f=k_w attains the bound", val, norm * (1 - abs(w) ** 2) ** -0.5, 1e-9)
# representer theorem: a = (G + lambda I)^{-1} y minimises J on the span
rng = np.random.default_rng(0)
x = rng.normal(size=6); y = rng.normal(size=6); lam = 0.3
G = np.exp(-(x[:, None] - x[None, :]) ** 2 / 2)
J = lambda a: np.sum((G @ a - y) ** 2) + lam * a @ G @ a
a0 = np.linalg.solve(G + lam * np.eye(6), y)
check_true("Gaussian Gram matrix is positive semi-definite", np.linalg.eigvalsh(G).min() > -1e-12)
check_true("kernel ridge solution minimises J", all(J(a0) <= J(a0 + 0.1 * rng.normal(size=6)) for _ in range(200)))
finish()
