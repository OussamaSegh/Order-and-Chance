"""Number checks for Chapter 14 (Sums of Random Pieces), the problem chapter of Volume 11."""
import math
from fractions import Fraction as F
import numpy as np
from scipy import integrate, stats
from common import check, check_true, finish

# Lucky tickets (pb:lucky)
digits = np.zeros(28, dtype=np.int64)
for a in range(10):
    for b in range(10):
        for c in range(10):
            digits[a + b + c] += 1
L3 = int((digits ** 2).sum())
check_true("lucky six-digit tickets = 55252", L3 == 55252)
var_x = F(33, 4); m4 = F(1, 5) * sum((j + F(1, 2)) ** 4 for j in range(5))
check_true("E(X-9/2)^4 = 9669/80", m4 == F(9669, 80))
k4 = 2 * (m4 - 3 * var_x ** 2)
check_true("kappa_4 = -9999/60", k4 == F(-9999, 60))
coef = k4 / (8 * (2 * var_x) ** 2)
check_true("correction -101/1320", coef == F(-101, 1320))
main = 1e6 / math.sqrt(99 * math.pi)
check("main term m=3", main, 56703, 1)
corr = main * (1 - 101 / 3960)
check("corrected m=3", corr, 55257, 1)
check_true("corrected within 0.02%", abs(corr - 55252) / 55252 < 2e-4)
Lint = integrate.quad(lambda t: (math.sin(5 * t) / math.sin(t / 2)) ** 6 if t else 1e6, -math.pi, math.pi, limit=400)[0] / (2 * math.pi)
check("integral formula m=3", Lint, 55252, 0.5)

# Twelve uniforms (pb:twelve)
check("E cos W exact", (2 * math.sin(0.5)) ** 12, 0.603968, 5e-7)
check("e^{-1/2}", math.exp(-0.5), 0.606531, 5e-7)
check_true("Lindeberg bound 1/60 holds", abs((2 * math.sin(.5)) ** 12 - math.exp(-.5)) <= 1 / 60)
check("bound (9/5+3)/(24*12)", (9 / 5 + 3) / (24 * 12), 1 / 60, 1e-15)
p4 = 2 * (2 ** 12 - 12) / math.factorial(12)
check("P(|W|>4)", p4, 1.7e-5, 0.05e-5)
# exact: P(S>10) for S sum of 12 uniforms = (Irwin-Hall) sum_k (-1)^k C(12,k)(12-10-k)^12/12!
ih = sum((-1) ** k * math.comb(12, k) * max(0, 2 - k) ** 12 for k in range(13)) / math.factorial(12)
check("P(|W|>4) via Irwin-Hall", 2 * ih, p4, 1e-15)
check("P(|Z|>4)", 2 * stats.norm.sf(4), 6.3e-5, 0.05e-5)

# Fixed points (pb:fixedtv (b))
check("2(1-1/e)", 2 * (1 - math.exp(-1)), 1.26, 0.005)

# Minkowski question mark (pb:minkowski)
def qm(cf):
    s = 0; tot = 0
    for k, a in enumerate(cf, 1):
        s += a; tot += 2 * (-1) ** (k + 1) * 2.0 ** (-s)
    return tot
check("?((sqrt5-1)/2)", qm([1] * 60), 2 / 3, 1e-12)
check("?(sqrt2-1)", qm([2] * 40), 2 / 5, 1e-12)
check("(sqrt5-1)/2", (math.sqrt(5) - 1) / 2, 0.618, 0.0005)
check("sqrt2-1", math.sqrt(2) - 1, 0.414, 0.0005)

# Kac (pb:kaczeros): degree 100 has about three real roots on average
def rho(t, n):
    a = 1 / (1 - t * t) ** 2 - (n + 1) ** 2 * t ** (2 * n) / (1 - t ** (2 * n + 2)) ** 2
    return math.sqrt(max(a, 0)) / math.pi
EN = 4 * integrate.quad(rho, 0, 1, args=(100,), limit=400, points=[0.9, 0.99])[0]
check("E N_100 (Kac integral)", EN, 3.56, 0.005)
rng = np.random.default_rng(1)
cnt = [np.sum(np.abs(np.roots(rng.standard_normal(101)).imag) < 1e-9) for _ in range(2000)]
check("E N_100 (simulation, 2000 polys)", float(np.mean(cnt)), EN, 0.15)

EN2 = lambda n: 4 * integrate.quad(rho, 0, 1, args=(n,), limit=800, points=[1 - 1 / n, 1 - 0.1 / n])[0]
check("E N_n - (2/pi)log n, n=10^5", EN2(10 ** 5) - 2 / math.pi * math.log(1e5), 0.6257, 0.002)
near = [np.mean(np.abs(np.abs(np.roots(rng.standard_normal(51))) - 1) < 0.1) for _ in range(2000)]
check("share of roots within 0.1 of unit circle, n=50", float(np.mean(near)), 0.81, 0.01)

finish()
