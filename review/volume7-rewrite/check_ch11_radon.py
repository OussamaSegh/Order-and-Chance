#!/usr/bin/env python3
"""Volume 7, Chapter 11: likelihood ratio, the die, the maximal function of an indicator, variation estimates."""
from fractions import Fraction as F
import mpmath as mp
from common import check, check_true, finish
mp.mp.dps = 20
phi = lambda x: mp.exp(-x * x / 2) / mp.sqrt(2 * mp.pi)
m = mp.mpf("0.7")
check("E_P[L] = 1", float(mp.quad(lambda x: mp.exp(m * x - m * m / 2) * phi(x), [-mp.inf, 0, mp.inf])), 1, 1e-12)
check("relative entropy m^2/2", float(mp.quad(lambda x: (m * x - m * m / 2) * phi(x - m), [-mp.inf, 0, mp.inf])), float(m * m / 2), 1e-12)
check("Gaussian ratio e^{x-1/2}", float(phi(mp.mpf(2) - 1) / phi(2)), float(mp.exp(1.5)), 1e-12)
# die
faces = [1, 2, 3, 4, 5, 6]
avg = lambda S: F(sum(S), len(S))
check_true("odd 3, even 4", avg([1, 3, 5]) == 3 and avg([2, 4, 6]) == 4 and avg(faces) == F(7, 2))
check_true("Y = 3/2, 7/2, 11/2", [avg([1, 2]), avg([3, 4]), avg([5, 6])] == [F(3, 2), F(7, 2), F(11, 2)])
check_true("tower on B_1", avg([1, 2, 3, 4]) == F(5, 2) == (F(3, 2) * 2 + F(7, 2) * 2) / 4)
# maximal function of 1_[-1,1]
def M(x, steps=4000):
    best = 0
    for i in range(1, steps + 1):
        r = 6.0 * i / steps
        ov = max(0.0, min(1, x + r) - max(-1, x - r))
        best = max(best, ov / (2 * r))
    return best
for x in (1.0, 1.5, 3.0):
    check(f"Mf({x})", M(x), 1 / (abs(x) + 1), 2e-3)
check("Mf(0.4)", M(0.4), 1, 1e-9)
for t in (0.1, 0.25, 0.5):
    check_true(f"measure of Mf > {t} is 2/t - 2 <= 6/t", abs((2 / t - 2) - 2 * (1 / t - 1)) < 1e-12 and 2 / t - 2 <= 6 / t)
# variation exercise: (1/4) ln((6k+1)/(6k-1)) >= c/k with c = 1/12
check_true("log bound", all(mp.log(mp.mpf(6 * k + 1) / (6 * k - 1)) / 4 >= mp.mpf(1) / (12 * k) for k in range(1, 2000)))
check_true("1/x - 2x >= 1/(2x) for x <= 1/2", all(1 / x - 2 * x >= 1 / (2 * x) - 1e-12 for x in [i / 1000 for i in range(1, 501)]))
# biased coin fourth moment: E[(sum Y)^4] = n E Y^4 + 3n(n-1) (E Y^2)^2 <= 3n^2
p = F(1, 3)
EY2 = p * (1 - p)**2 + (1 - p) * p**2; EY4 = p * (1 - p)**4 + (1 - p) * p**4
check_true("fourth moment bound", all(n * EY4 + 3 * n * (n - 1) * EY2**2 <= 3 * n * n for n in range(1, 200)))
finish()
