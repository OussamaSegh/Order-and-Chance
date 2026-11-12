#!/usr/bin/env python3
"""Volume 7, Chapter 9: ball volumes, dimension 100, cone, Ritelli's integral, Frullani, the failing Fubini example."""
import mpmath as mp
from common import check, check_true, finish
mp.mp.dps = 30
V = lambda d: mp.pi**(mp.mpf(d) / 2) / mp.gamma(mp.mpf(d) / 2 + 1)
for d, pr in ((1, 2), (2, mp.pi), (3, 4 * mp.pi / 3), (4, mp.pi**2 / 2)):
    check(f"volume of B^{d}", float(V(d)), float(pr), 1e-12)
check("sigma(S^1)", float(2 * V(2)), float(2 * mp.pi), 1e-12)
check("sigma(S^2)", float(3 * V(3)), float(4 * mp.pi), 1e-12)
v100 = V(100)
check_true("V_100 = pi^50/50! about 2.4e-40", abs(v100 - mp.pi**50 / mp.factorial(50)) < 1e-60 and abs(v100 / mp.mpf("2.4e-40") - 1) < 0.02)
check_true("2^100 about 1.3e30", abs(mp.mpf(2)**100 / mp.mpf("1.3e30") - 1) < 0.03)
check_true("fraction about 2e-70", abs(v100 / mp.mpf(2)**100 / mp.mpf("2e-70") - 1) < 0.08)
check("sqrt(100/3)", float(mp.sqrt(mp.mpf(100) / 3)), 5.8, 0.03)
check_true("0.9^100 about 2.7e-5", abs(mp.mpf("0.9")**100 / mp.mpf("2.7e-5") - 1) < 0.02)
check("cone, d=3", float(mp.quad(lambda t: (1 - t / 2)**2, [0, 2])), 2 / 3, 1e-12)
check("Ritelli: int -ln x/(1-x^2)", float(mp.quad(lambda x: -mp.log(x) / (1 - x * x), [0, 0.5, 1])), float(mp.pi**2 / 8), 1e-10)
check("sum 1/(2k+1)^2", float(mp.nsum(lambda k: 1 / (2 * k + 1)**2, [0, mp.inf])), float(mp.pi**2 / 8), 1e-12)
check("int e^{-|x|}/|x| over R^3", float(4 * mp.pi * mp.gamma(2)), float(4 * mp.pi), 0)
a, b = mp.mpf(2), mp.mpf(7)
check("Frullani", float(mp.quad(lambda x: (mp.exp(-a * x) - mp.exp(-b * x)) / x, [0, 1, 10, mp.inf])), float(mp.log(b / a)), 1e-10)
check("inner integral of the failing example", float(mp.quad(lambda y: (0.3**2 - y * y) / (0.3**2 + y * y)**2, [0, 0.3, 1])), 1 / (1 + 0.09), 1e-9)
check("simplex n=3", float(1 / mp.factorial(3)), 1 / 6, 1e-15)
check("Gamma sum: Beta identity", float(mp.beta(2.5, 1.5)), float(mp.gamma(2.5) * mp.gamma(1.5) / mp.gamma(4)), 1e-12)
finish()
