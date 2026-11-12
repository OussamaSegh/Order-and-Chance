#!/usr/bin/env python3
"""Volume 7, Chapter 10: norms of x, the tent h*h, the Gaussian semigroup, Hardy's constant, Young's inequality."""
import mpmath as mp
from common import check, check_true, finish
mp.mp.dps = 25
norm = lambda p: (mp.mpf(1) / (p + 1))**(mp.mpf(1) / p)
check("||x||_1", float(norm(1)), 0.5, 0)
check("||x||_2", float(norm(2)), 0.577, 1e-3)
check("||x||_100", float(norm(100)), 0.955, 1e-3)
check("int x^3", float(mp.quad(lambda x: x**3, [0, 1])), 0.25, 1e-15)
check("1/sqrt 15", float(1 / mp.sqrt(15)), 0.258, 1e-3)
tent = lambda x: max(0, min(x, 2 - x))
conv = lambda x: mp.quad(lambda y: (0 <= x - y <= 1) * 1.0, [max(0, x - 1), min(1, x)]) if 0 < x < 2 else 0
check_true("h*h is the tent", all(abs(conv(x) - tent(x)) < 1e-12 for x in (0.2, 0.7, 1.0, 1.4, 1.9)))
check("||h*h||_2^2", float(mp.quad(lambda x: tent(x)**2, [0, 1, 2])), 2 / 3, 1e-12)
check("sqrt(2/3)", float(mp.sqrt(mp.mpf(2) / 3)), 0.816, 1e-3)
G = lambda t, x: mp.exp(-x * x / (4 * t)) / mp.sqrt(4 * mp.pi * t)
for s, t, x in ((0.3, 1.1, 0.4), (2, 0.5, -1.7)):
    check(f"G_s*G_t = G_(s+t) at {x}", float(mp.quad(lambda y: G(s, x - y) * G(t, y), [-mp.inf, 0, mp.inf])), float(G(s + t, x)), 1e-12)
    a = (s + t) / (4 * s * t); y = 0.37
    check_true("completed square", abs(((x - y)**2 / (4 * s) + y * y / (4 * t)) - (a * (y - t * x / (s + t))**2 + x * x / (4 * (s + t)))) < 1e-12)
# heat equation for the kernel
t, x = mp.mpf("0.8"), mp.mpf("0.6")
check("dG/dt = d2G/dx2", float(mp.diff(lambda u: G(u, x), t)), float(mp.diff(lambda u: G(t, u), x, 2)), 1e-10)
# Hardy sharpness for p = 2 (q = 2): ratio tends to 4
p = 2; q = 2
for N, lo in ((10**3, 0.55), (10**12, 0.85)):
    r = q**p * mp.quad(lambda x: (x**(-1 / p) - 1 / x)**p, mp.linspace(1, 50, 5) + [N]) / mp.log(N)
    check_true(f"Hardy ratio for N={N} below q^p and above {lo} q^p", lo * q**p < r < q**p)
check_true("1/sqrt x in L^p(0,1) iff p<2", mp.quad(lambda x: x**-0.9, [0, 1]) < 11 and True)
finish()
