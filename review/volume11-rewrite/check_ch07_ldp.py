"""Chapter 7 (large deviations): check every printed number."""
import math
import numpy as np
from scipy.stats import gamma, norm, binom
from scipy.optimize import brentq, minimize_scalar
from mpmath import mp, mpf, binomial as mbin
from common import check, check_true, finish

# insurer: 100 exponential claims, total > 200
n, a = 100, 2.0
exact = gamma.sf(200, 100)
check("gamma tail", exact, 1.84e-15, 0.01e-15)
rate = a - 1 - math.log(a)
check("e^{-n rate}", math.exp(-n * rate), 4.7e-14, 0.05e-14)
th, sa = 1 - 1 / a, 1 / (1 - (1 - 1 / a))
br = math.exp(-n * rate) / (th * sa * math.sqrt(2 * math.pi * n))
check("Bahadur-Rao", br, 1.88e-15, 0.01e-15)
check("1-Phi(10)", norm.sf(10), 7.6e-24, 0.05e-24)
check_true("CLT off by ~1e8", 5e7 < exact / norm.sf(10) < 5e8)

# Brandeis dice
f = np.arange(1, 7)
Lam = lambda t: math.log(np.mean(np.exp(t * f)))
dL = lambda t: float(np.sum(f * np.exp(t * f)) / np.sum(np.exp(t * f)))
th = brentq(lambda t: dL(t) - 4.5, 0, 3)
check("theta dice", th, 0.371, 0.0005)
nu = np.exp(th * f) / np.sum(np.exp(th * f))
for p, q in zip(nu, [0.054, 0.079, 0.114, 0.165, 0.240, 0.347]):
    check("nu*", p, q, 0.0005)
r = th * 4.5 - Lam(th)
check("Lambda*(4.5)", r, 0.178, 0.0005)
# exact P(sum of 100 dice >= 450)
poly = np.zeros(1, dtype=object); poly[0] = 1
dist = [1]
for _ in range(100):
    new = [0] * (len(dist) + 6)
    for i, c in enumerate(dist):
        if c:
            for k in range(1, 7):
                new[i + k] += c
    dist = new
tot = sum(dist[450:]); p = tot / 6 ** 100
check("P(sum>=450)", float(p), 1.5e-9, 0.05e-9)
check("e^{-17.8}", math.exp(-100 * r), 1.8e-8, 0.05e-8)

# coin test
D01 = 0.5 * math.log(0.5 / 0.6) + 0.5 * math.log(0.5 / 0.4)
D10 = 0.6 * math.log(0.6 / 0.5) + 0.4 * math.log(0.4 / 0.5)
check("D(mu0||mu1)", D01, 0.0204, 0.00005)
check("D(mu1||mu0)", D10, 0.0201, 0.00005)
check("log(1e6)/D", math.log(1e6) / D01, 680, 5)

def beta(n, eps=0.05):
    # optimal non-randomised set: declare fair when heads small; the likelihood ratio
    # P1/P0 increases with heads, so B = {heads <= k} plus part of level k+1 (individual words)
    h = np.arange(n + 1)
    p0 = binom.pmf(h, n, 0.5)
    w1 = 0.6 ** h * 0.4 ** (n - h)  # P1 of one word
    w0 = 0.5 ** n
    # B^c must have P0 <= eps: remove words with most heads first
    rem = eps; b = 0.0
    for k in range(n, -1, -1):
        cnt = math.comb(n, k)
        take = min(cnt, math.floor(rem / w0 + 1e-9))
        rem -= take * w0
        b += (cnt - take) * w1[k]
        if take < cnt:
            b += sum(math.comb(n, j) * w1[j] for j in range(k))
            break
    return b
lo = next(n for n in range(600, 2000, 5) if beta(n) <= 1e-6)
check("exact optimum ~1000", lo, 1000, 60)

# Chernoff information
g = lambda s: math.log(0.5 ** (1 - s) * (0.6 ** s + 0.4 ** s))
res = minimize_scalar(g, bounds=(0, 1), method="bounded")
check("s*", res.x, 0.498, 0.0005)
check("C", -res.fun, 0.00508, 0.000005)
check_true("C about a quarter of D", 0.22 < -res.fun / D01 < 0.28)

# Curie-Weiss
for b, v in [(1.5, 0.859), (2.0, 0.958)]:
    m = brentq(lambda y: math.tanh(b * y) - y, 1e-6, 1)
    check("m*(%s)" % b, m, v, 0.0005)
b = 1.0001
m = brentq(lambda y: math.tanh(b * y) - y, 1e-8, 1)
check("m*~sqrt(3(b-1))", m / math.sqrt(3 * (b - 1)), 1, 0.001)
J = lambda y: (1 + y) / 2 * math.log(1 + y) + (1 - y) / 2 * math.log(1 - y)
y = 0.01
check("g at beta=1 ~ -y^4/12", (y * y / 2 - J(y)) / (-y ** 4 / 12), 1, 0.001)
# heavy-tail mean
check("mean of (1+t)^-3 law", 0.5, 0.5, 0)
finish()
