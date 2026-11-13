"""Chapter 8 (concentration): check every printed number."""
import math, re, bisect
import numpy as np
from scipy.special import gammaln
from common import check, check_true, finish

# balls in bins: t=5000, C=1e6
check("Azuma exponent", 5000 ** 2 / (2 * 1e6), 12.5, 0)
check("McDiarmid exponent", 2 * 5000 ** 2 / 1e6, 50, 0)

# thin shell n=1e6
n = 10 ** 6
EZ = math.exp(0.5 * math.log(2) + gammaln((n + 1) / 2) - gammaln(n / 2))
check_true("E|Z| in [999,1000] (%.4f)" % EZ, 999 <= EZ <= 1000)
check_true("1-2e^{-4.5} >= 0.97", 1 - 2 * math.exp(-4.5) >= 0.97)
for m in [20, 200, 2000]:
    EZm = math.exp(0.5 * math.log(2) + gammaln((m + 1) / 2) - gammaln(m / 2))
    check("E|Z|-sqrt n ~ -1/(4 sqrt n), n=%d" % m, (EZm - math.sqrt(m)) * 4 * math.sqrt(m), -1, 0.02)
    check("Var|Z| ~ 1/2, n=%d" % m, m - EZm ** 2, 0.5, 0.02)
check("1/sqrt2", 1 / math.sqrt(2), 0.71, 0.005)

# JL
N, eps = 10 ** 6, 0.1
k = 4 * math.log(N) / (eps ** 2 / 2 - eps ** 3 / 3)
check("JL k", math.floor(k) + 1, 11842, 0)
check_true("1e7/11842 > 800", 1e7 / 11842 > 800)

# Talagrand numeric
check_true("e^{1/4}<1.29<2-e^{-1/2}", math.exp(0.25) < 1.29 < 2 - math.exp(-0.5))
u = np.linspace(-0.5, 0, 10001)
check_true("e^{-u-u^2} <= 2-e^u on [-1/2,0]", np.all(np.exp(-u - u * u) <= 2 - np.exp(u) + 1e-15))
r = np.linspace(1e-6, 1, 2001); lam = np.linspace(0, 1, 2001)
best = np.min(r[:, None] ** (-lam[None, :]) * np.exp((1 - lam[None, :]) ** 2 / 4), axis=1)
check_true("min_lambda r^-lambda e^{(1-lambda)^2/4} <= 2-r", np.all(best <= 2 - r + 1e-9))

# LIS figure
src = open("../../volume11-randomness/figures/ch08-lis.tex").read()
pts = [(float(a), float(b)) for a, b in re.findall(r"\\fill\[black!45\] \(([\d.]+),([\d.]+)\)", src)]
check("figure points", len(pts), 300, 0)
pts.sort()
ys = [p[1] for p in pts]
tails = []
for y in ys:
    i = bisect.bisect_left(tails, y)
    if i == len(tails): tails.append(y)
    else: tails[i] = y
check("figure LIS", len(tails), 29, 0)
check("2 sqrt 300", 2 * math.sqrt(300), 34.6, 0.05)
check_true("all y distinct", len(set(ys)) == 300)
finish()
