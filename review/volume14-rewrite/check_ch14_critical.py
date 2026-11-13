#!/usr/bin/env python3
"""Volume 14, Chapter 14 (critical line): Hardy's identity, constants, zero counts."""
import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import check, check_true, finish
from mpmath import mp, mpf, quad, zeta, gamma, pi, exp, cos, euler, nzeros, inf, jtheta, nsum
mp.dps = 25
def omega(u):
    return nsum(lambda n: exp(-pi * n * n * u), [1, inf])
def Xi(t):
    s = mpf(1) / 2 + 1j * t
    return (s * (s - 1) / 2 * pi ** (-s / 2) * gamma(s / 2) * zeta(s)).real
def rhs(x):
    return pi / 2 * (exp(-x / 2) - 2 * exp(x / 2) * omega(exp(2 * x)))
def lhs(x):
    f = lambda t: Xi(t) / (t * t + mpf(1) / 4) * cos(x * t)
    return quad(f, [0, 10, 20, 40, 80, 160])
check("Hardy identity RHS at 0", float(rhs(0)), 1.4350248428, 1e-10)
for x in (0, 0.5, 1):
    a, b = lhs(mpf(x)), rhs(mpf(x))
    check(f"Hardy identity at x={x}", float(a), float(b), 1e-15)
check("2 gamma - 1", float(2 * euler - 1), 0.1544, 1e-4)
check("N(5000)", int(nzeros(5000)), 4520, 0)
check_true("0.47 pi / 4 > 0.36", 0.47 * math.pi / 4 > 0.36)
finish()
