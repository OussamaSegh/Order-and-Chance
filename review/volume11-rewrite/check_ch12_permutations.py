"""Chapter 12 (permutations and Poisson-Dirichlet): check every printed number."""
import math, re, collections
import numpy as np
from scipy.integrate import quad
from common import check, check_true, finish

# Dickman rho on a grid by the delay equation u rho'(u) = -rho(u-1)
h = 1e-4
U = np.arange(0, 12 + h / 2, h)
rho = np.ones_like(U)
m = int(round(1 / h))
for i in range(m, len(U) - 1):
    # trapezoid on rho' = -rho(u-1)/u
    f0 = -rho[i - m] / U[i]
    f1 = -rho[i + 1 - m] / U[i + 1]
    rho[i + 1] = rho[i] + h / 2 * (f0 + f1)
r = lambda u: float(np.interp(u, U, rho))
check("rho(2)=1-log2", r(2), 1 - math.log(2), 1e-8)
check_true("rho(3)=0.04860... (%.7f)" % r(3), str(r(3)).startswith("0.04860"))
check("rho(3)~0.049", r(3), 0.049, 0.0005)
check("1-log2", 1 - math.log(2), 0.31, 0.005)
check("log 2", math.log(2), 0.69, 0.005)
lam = np.trapezoid((1 - rho[m:]) / U[m:] ** 2, U[m:]) + 1 / U[-1]  # tail: rho~0 beyond 12
check("Golomb-Dickman", lam, 0.6243299885, 2e-9)
check("100 lambda digits", 100 * lam, 62, 0.5)
# rho(u) <= 1/floor(u)!
check_true("rho(u) <= 1/floor(u)!", all(r(u) <= 1 / math.factorial(int(u)) + 1e-12 for u in np.arange(0, 12, 0.01)))

# Simpson for int_2^3 log(t-1)/t
g = lambda t: math.log(t - 1) / t
vals = [g(2), g(2.25), g(2.5), g(2.75), g(3)]
for v, p in zip(vals[1:], [0.09917, 0.16219, 0.20350, 0.23105]):
    check("g", v, p, 5e-6)
simp = (vals[0] + 4 * vals[1] + 2 * vals[2] + 4 * vals[3] + vals[4]) / 12
check("Simpson", simp, 0.14718, 5e-6)
check("rho(3) by Simpson", 1 - math.log(3) + simp, 0.0486, 5e-5)
check("log 3", math.log(3), 1.09861, 5e-6)

# E sum V_i^2 = 1/2
check("E sum V^2", (1 / 3) / (1 - 1 / 3), 0.5, 1e-15)

# smooth integers n <= 1e7 with all prime factors <= x^{1/3}
N = 10 ** 7
lpf = np.ones(N + 1, dtype=np.int64)  # largest prime factor
for p in range(2, N + 1):
    if lpf[p] == 1:
        lpf[p::p] = p
y = N ** (1 / 3)
prop = np.count_nonzero(lpf[1:] <= y) / N
check("smooth proportion x=1e7, u=3", prop, 0.067, 0.0005)

# sticks figure
src = open("../../volume11-randomness/figures/ch12-sticks.tex").read()
rows = collections.defaultdict(list)
for x0, y0, x1, y1 in re.findall(r"\(([\d.]+),([\d.]+)\) rectangle \(([\d.]+),([\d.]+)\)", src):
    rows[y0].append((float(x1) - float(x0)) * 100)
top, mid, bot = rows["2.000"], rows["1.000"], rows["0.000"]
check("first cycle", top[0], 251, 0.01)
check("number of cycles", len(top), 9, 0)
check("total", sum(top), 1000, 0.05)
dev = max(abs(a - b) for a, b in zip(sorted(top, reverse=True) + [0] * 300, sorted(bot, reverse=True))) / 1000
check_true("sorted cycles within 0.0015 of the stick (%.5f)" % dev, dev <= 0.0015 + 2e-5)
finish()
