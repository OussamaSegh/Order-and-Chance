#!/usr/bin/env python3
"""Volume 7, Chapter 6: the winding numbers of Exercise 6 (three winding numbers) and the crossings of the real axis."""
import cmath, math
from common import check, check_true, finish
def wind(g, a, N=20000):
    tot = 0.0; prev = g(0) - a
    for j in range(1, N + 1):
        cur = g(2 * math.pi * j / N) - a
        tot += cmath.phase(cur / prev); prev = cur
    return tot / (2 * math.pi)
g1 = lambda t: 2 * cmath.exp(2j * t) + cmath.exp(1j * t)
g2 = lambda t: cmath.exp(1j * t) + 2 * cmath.exp(-3j * t)
check("n(gamma_1, 0)", wind(g1, 0), 2, 1e-9)
check("n(gamma_2, 0)", wind(g2, 0), -3, 1e-9)
check("n(gamma_1, 5)", wind(g1, 5), 0, 1e-9)
check("gamma_1(0)", g1(0).real, 3, 1e-12)
check("gamma_1(pi)", g1(math.pi).real, 1, 1e-12)
t = math.acos(-0.25)
check("real part where cos t = -1/4", g1(t).real, -2, 1e-12)
check("imaginary part there", g1(t).imag, 0, 1e-12)
check("derivative of Im at 0", 4 * math.cos(0) + math.cos(0), 5, 0)
check("derivative of Im at pi", 4 * math.cos(2 * math.pi) + math.cos(math.pi), 3, 1e-12)
finish()
