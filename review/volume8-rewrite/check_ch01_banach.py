#!/usr/bin/env python3
"""Volume 8, Chapter 1: Lebesgue constants (the printed values and the lower bound of the divergence theorem),
the norm of x^n in two norms (Exercise ex:twonorms), the average of unit vectors (ex:mazur)."""
from math import pi, sin, log, sqrt
from mpmath import mp, quad, mpf
from common import check, check_true, finish
mp.dps = 20
def L(N):
    # (1/2pi) int_{-pi}^{pi} |D_N| = (1/pi) int_0^pi |sin((N+1/2)t)| / sin(t/2) dt, split at the zeros
    zs = [mpf(0)] + [k * mp.pi / (N + mpf(1) / 2) for k in range(1, N + 1)] + [mp.pi]
    return float(quad(lambda t: abs(mp.sin((N + mpf(1) / 2) * t)) / mp.sin(t / 2), zs) / mp.pi)
printed = {1: 1.436, 10: 2.223, 100: 3.139, 1000: 4.070}
for N, v in printed.items():
    check(f"Lebesgue constant L_{N}", L(N), v, 6e-4)
    H = sum(1 / k for k in range(1, N + 1))
    check_true(f"L_{N} >= (4/pi^2) H_{N}", L(N) >= 4 / pi**2 * H)
# growth like (4/pi^2) ln N: the difference stays bounded
d = [L(N) - 4 / pi**2 * log(N) for N in (10, 100, 1000)]
check_true("L_N - (4/pi^2) ln N is bounded (between 1.2 and 1.4)", all(1.2 < x < 1.4 for x in d))
# ex:twonorms: ||x^n||_1 = 1/(n+1)
for n in (1, 5, 20):
    check(f"int_0^1 x^{n}", float(quad(lambda x: x**n, [0, 1])), 1 / (n + 1), 1e-12)
# ex:mazur: ||(e_1+...+e_n)/n||_2 = 1/sqrt(n)
for n in (4, 100):
    check(f"average of {n} unit vectors", sqrt(n * (1 / n) ** 2), 1 / sqrt(n), 1e-15)
finish()
