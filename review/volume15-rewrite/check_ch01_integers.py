#!/usr/bin/env python3
"""Recompute the printed numbers of Chapter 1 (ra-anatomy.tex): smooth numbers, divisors, multiplication table."""
import math, numpy as np
from scipy.optimize import minimize_scalar
from scipy.integrate import quad
from common import check, check_true, finish, primes_upto

# delta of Erdos's multiplication table theorem
d = 1 - (1 + math.log(math.log(2))) / math.log(2)
check("delta", d, 0.08607, 5e-6)
check("kappa", 1 / math.log(2), 1.4427, 5e-5)
check("kappa/2", 0.5 / math.log(2), 0.7213, 5e-5)
check("Q*(kappa)=delta", (1/math.log(2))*math.log(1/math.log(2)) - 1/math.log(2) + 1, d, 1e-12)

def D(N):
    seen = np.zeros(N * N + 1, dtype=bool)
    for a in range(1, N + 1): seen[a * np.arange(1, N + 1)] = True
    return int(seen.sum())
check("D(10)", D(10), 42, 0)
r = D(8192) / 8192**2
check("D(8192)/8192^2", r, 0.227, 5e-4)
# Ford's shape fitted at N=2^13, and where it reaches 0.1
f = lambda N: math.log(N) ** (-d) * math.log(math.log(N)) ** (-1.5)
c = r / f(8192)
check("fitted c", c, 0.89, 5e-3)
lo, hi = 1e5, 1e40
for _ in range(200):
    mid = math.sqrt(lo * hi)
    lo, hi = (mid, hi) if c * f(mid) > 0.1 else (lo, mid)
print("   N where Ford's curve reaches 0.1:", "%.2e" % lo)
check_true("Ford curve reaches 0.1 near 1e15 (within a factor 10)", 1e14 <= lo <= 1e16)
check_true("(log N)^-delta > 0.8 at 2^13", math.log(8192) ** (-d) > 0.8)

# arcsine numbers
F = lambda t: 2 / math.pi * math.asin(math.sqrt(t))
check("P(S<=0.1)", F(0.1), 0.205, 5e-4)
check("P(0.45<S<0.55)", F(0.55) - F(0.45), 0.064, 5e-4)

# random divisor of n<=1e6: atom at d=1 and the largest gap
X = 10**6
tau = np.zeros(X + 1, dtype=np.int64)
for k in range(1, X + 1): tau[k::k] += 1
atom = (1.0 / tau[1:]).mean()
check("P(d=1) at 1e6", atom, 0.151, 5e-4)
# the law of log d / log n at t = 0 (the atom) and at t = 0.005, the first plotted point
def cdf_at(t0):
    tot = 0.0
    for dd in range(1, X + 1):
        ns = np.arange(dd, X + 1, dd)
        if dd == 1: tot += (1.0 / tau[ns]).sum(); continue
        ok = math.log(dd) <= t0 * np.log(ns)
        tot += (1.0 / tau[ns][ok]).sum()
        if dd > X ** t0 + 1: break
    return tot / X
c5 = cdf_at(0.005)
check("gap at t=0.005", c5 - F(0.005), 0.11, 0.005)
# C of Exercise ex:invtau
ps = primes_upto(10**7).astype(float)
logprod = np.sum(0.5 * np.log1p(-1 / ps) + np.log(ps * np.log(ps / (ps - 1))))
# tail beyond 1e7: log term ~ -1/(24 p^2), negligible
prod = math.exp(logprod)
check("Euler product of ex:invtau", prod, 0.9692, 5e-4)
check("C of ex:invtau", prod / math.sqrt(math.pi), 0.5468, 5e-4)
check("prediction C/sqrt(log 1e6)", prod / math.sqrt(math.pi) / math.sqrt(math.log(1e6)), 0.147, 5e-4)

# Dickman rho(7) and 10-smooth numbers below 1e7
def rho_table(umax, h=1e-4):
    n = int(umax / h) + 1; u = np.arange(n) * h; r = np.ones(n)
    k = int(round(1 / h))
    for i in range(k + 1, n):  # rho'(u) = -rho(u-1)/u, trapezoid
        r[i] = r[i-1] - h * 0.5 * (r[i-1-k] / u[i-1] + r[i-k] / u[i])
    return u, r
u, rr = rho_table(8)
rho7 = rr[int(round(7 / 1e-4))]
check("1e7 rho(7)", 1e7 * rho7, 9, 1)
def psi(x, y):
    P = [p for p in range(2, y + 1) if all(p % q for q in range(2, int(p**.5) + 1))]
    def rec(i, m):
        if i == len(P): return 1
        s, mm = 0, m
        while mm <= x:
            s += rec(i + 1, mm); mm *= P[i]
        return s
    return rec(0, 1)
check("Psi(1e7,10)", psi(10**7, 10), 2155, 0)
# Rankin's bound with the best sigma, ratio to Psi, for the figure's y values
ys = [2,3,4,6,7,10,13,18,24,32,42,56,75,100,133,178,237,316,422,562,750,1000,1334,1778,2371,3162,4217,5623,7499,10000]
x = 1e7; pr = primes_upto(10000)
ratios = []
for y in ys:
    py = pr[pr <= y].astype(float)
    g = lambda s: s * math.log(x) - np.sum(np.log1p(-py ** (-s)))
    res = minimize_scalar(g, bounds=(0.05, 1.0), method="bounded")
    if y <= 13: ps_ = psi(10**7, y)
    else: ps_ = None
    ratios.append((y, res.fun, ps_))
# exact Psi for larger y by sieve of largest prime factor
N = 10**7
lpf = np.zeros(N + 1, dtype=np.int32)
for p in primes_upto(N):
    lpf[p::p] = p
lpf[1] = 1
srt = np.sort(lpf[1:])
rs = []
for y, lb, _ in ratios:
    cnt = np.searchsorted(srt, y, side="right")
    rs.append(math.exp(lb) / cnt)
print("   Rankin/Psi ratios:", [round(v, 1) for v in rs])
check("smallest Rankin/Psi ratio", min(rs), 2.7, 0.05)
check("largest Rankin/Psi ratio", max(rs), 21, 0.5)
check("(64/9)^(1/3)", (64 / 9) ** (1 / 3), 1.92, 5e-3)
# squarefree windows of the opening
N = 2 * 10**6; sf = np.ones(N + 1, bool)
for dd in range(2, int(N**.5) + 1): sf[dd*dd::dd*dd] = False
cs = np.concatenate([[0], np.cumsum(sf[1:])])
starts = np.arange(10**6, 10**6 + 10**5)
wins = cs[starts + 100] - cs[starts]
check("6/pi^2", 6 / math.pi**2, 0.6079, 5e-5)
check("min squarefree in a window", wins.min(), 54, 0); check("max", wins.max(), 65, 0)
check("sd of the window count", wins.std(), 1.5, 0.05)
check("binomial sd", math.sqrt(100 * 6/math.pi**2 * (1 - 6/math.pi**2)), 4.9, 0.05)
finish()
