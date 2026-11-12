#!/usr/bin/env python3
"""Volume 7, Chapter 8: the two limits of Exercise (two limits), Gaussian cosine integral, Dirichlet integral bounds."""
import mpmath as mp
from common import check, check_true, finish
mp.mp.dps = 25
a = lambda n: mp.quad(lambda x: (1 - x / n)**n * mp.exp(x / 2), mp.linspace(0, n, 21))
check("(a) n=10", float(a(10)), 1.51, 6e-3)
check("(a) n=100", float(a(100)), 1.93, 6e-3)
check("(a) limit 2", float(a(4000)), 2, 2e-3)
b = lambda n: mp.quad(lambda x: n * mp.sin(x / n) / (x * (1 + x * x)), [0, 1, 10, 100, 1000, mp.inf])
check("(b) limit pi/2", float(b(10**6)), float(mp.pi / 2), 1e-3)
for t in (0.5, 1, 3):
    check(f"I({t})", float(mp.quad(lambda x: mp.exp(-x * x) * mp.cos(t * x), [0, 3, mp.inf])), float(mp.sqrt(mp.pi) / 2 * mp.exp(-t * t / 4)), 1e-12)
    check(f"F({t})", float(mp.quad(lambda x: mp.exp(-t * x) * mp.sinc(x), [0, 10, 40, mp.inf])), float(mp.pi / 2 - mp.atan(t)), 1e-9)
check_true("(t+1)/(1+t^2) <= 2", max((t / 100 + 1) / (1 + (t / 100)**2) for t in range(0, 5000)) <= 2)
check_true("int over [k pi,(k+1)pi] of |sin t|/t >= 2/((k+1)pi)", all(mp.quad(lambda t: abs(mp.sin(t)) / t, [k * mp.pi, (k + 1) * mp.pi]) >= 2 / ((k + 1) * mp.pi) for k in range(1, 8)))
# figure: g_n = sqrt n on ]0,1/n[: integral over {g_n > M} is <= 1/sqrt n <= 1/M
check_true("escape figure bound", all(1 / mp.sqrt(n) <= mp.mpf(1) / M for M in (1, 2, 5) for n in range(M * M + 1, 200)))
finish()
