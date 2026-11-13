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
# Montgomery's explicit formula, as an exact identity in the proof of lem:montexplicit, at x=10, t=100.
# The first 2000 zeros (computed with mpmath.zetazero, stored next to this script).
import numpy as np
from common import primes_upto
from mpmath import mpc
g = np.array([float(l) for l in open(pathlib.Path(__file__).parent / 'zeta_zeros_2000.txt')])
check("2000 zeros stored", len(g), 2000, 0)
check("zero 2000 (mpmath.zetazero)", float(__import__('mpmath').zetazero(2000).imag), g[-1], 1e-9)
x, t = 10.0, 100.0
G = np.concatenate([g, -g])
L = 2 * np.sum(np.exp(1j * G * math.log(x)) / (1 + (t - G) ** 2))
s1 = 0j; s2 = 0j; N = 10**7
for p in primes_upto(N):
    p = int(p); lp = math.log(p); q = p
    while q <= N:
        y = x / q
        if q <= x: s1 += lp * y ** complex(-0.5, t)
        else: s2 += lp * y ** complex(1.5, t)
        q *= p
s = mpc(0.5, t)
gw = lambda w: x ** (w - 0.5) / ((1 + w - s) * (1 + s - w))
w = mpc(-0.5, t)
exact = complex(2 * gw(1) - x ** complex(-1, t) * (zeta(w, derivative=1) / zeta(w)) - 2 * sum(gw(-2 * k) for k in range(1, 60))) - x**-0.5 * (s1 + s2)
main = -x**-0.5 * (s1 + s2) + x ** complex(-1, t) * math.log(abs(t) + 2)
for name, v in [("zero side", L), ("prime side, exact", exact)]:
    check(f"explicit formula {name} real", v.real, 0.8285, 6e-5)
    check(f"explicit formula {name} imag", v.imag, 1.3374, 6e-5)
check("difference to the lemma's main terms, real", (exact - main).real, 0.13, 0.005)
check("difference to the lemma's main terms, imag", (exact - main).imag, 0.17, 0.005)
finish()
