#!/usr/bin/env python3
"""Recompute the printed numbers of Chapter 11 (ch11-values.tex, ra-bohrjessen.tex, ra-selberg.tex)."""
import math, numpy as np, mpmath
from common import check, check_true, finish, primes_upto
from rs_zeta import Z
g = 0.5772156649015329
check("zeta(0.7) = -2.78", float(mpmath.zeta(0.7)), -2.78, 5e-3)
ps = primes_upto(10 ** 7)
var = 0.5 * sum(sum(1 / (k * k * p ** (1.4 * k)) for k in range(1, 30)) for p in ps[:2000]) + 0.5 * sum(p ** -1.4 for p in ps[2000:])
check("exact Bohr-Jessen variance at 0.7", var, 0.529, 2e-3)
# sample at 1e5 vs random Euler product (smaller samples)
rng = np.random.default_rng(4)
t = rng.uniform(1e5, 2e5, 2000)
vals = np.array([float(mpmath.log(abs(mpmath.zeta(mpmath.mpc(0.7, x))))) for x in t])
check("sample variance of log|zeta(0.7+it)| near 0.53", vals.var(), 0.53, 0.05)
P5 = np.array(primes_upto(10 ** 5), float)
X = rng.uniform(0, 2 * np.pi, (4000, len(P5)))
modl = -np.sum(np.log(np.abs(1 - np.exp(1j * X) * P5 ** -0.7)), axis=1)
check("random Euler product variance near 0.53", modl.var(), 0.53, 0.04)
# Selberg variances
check("1/2 loglog 1e6", 0.5 * math.log(math.log(1e6)), 1.31, 5e-3)
check("1/2 loglog 1e10", 0.5 * math.log(math.log(1e10)), 1.57, 5e-3)
check("RMT variance at 1.5e6", 0.5 * (math.log(math.log(1.5e6 / (2 * math.pi))) + g + 1), 2.05, 5e-3)
check("RMT variance at 1.5e10", 0.5 * (math.log(math.log(1.5e10 / (2 * math.pi))) + g + 1), 2.32, 5e-3)
t = rng.uniform(1e6, 2e6, 200000); z = np.log(np.abs(Z(t)))
check("sample variance at 1e6 about 2.0", z.var(), 2.0, 0.06)
t = rng.uniform(1e10, 2e10, 8000); z = np.log(np.abs(Z(t)))
check("sample variance at 1e10 about 2.2 (8000 points)", z.var(), 2.2, 0.12)
check("sample mean at 1e10 near 0", z.mean(), 0.0, 0.05)
# window figure
tt = np.linspace(1e6, 1e6 + 12, 120001); zz = Z(tt)
check("zeros in [1e6, 1e6+12]", int(np.sum(np.sign(zz[1:]) != np.sign(zz[:-1]))), 22, 0)
s0 = 0.5 + 1 / math.log(1e6)
check("sigma_0 = 0.572", s0, 0.572, 5e-4)
def P(tv, N):
    ns, w = [], []
    for p in primes_upto(N):
        q = p
        while q <= N: ns.append(q); w.append(math.log(p) / (q ** s0 * math.log(q))); q *= p
    ln, w = np.log(np.array(ns, float)), np.array(w)
    return np.array([np.sum(w * np.cos(x * ln)) for x in tv])
pts = rng.uniform(1e6, 2e6, 1500)
off = np.array([float(mpmath.log(abs(mpmath.zeta(mpmath.mpc(s0, x))))) for x in pts])
check("corr(charcoal, rust n<=1e3)", np.corrcoef(off, P(pts, 10 ** 3))[0, 1], 0.95, 0.01)
check("corr(charcoal, rust n<=1e5)", np.corrcoef(off, P(pts, 10 ** 5))[0, 1], 0.98, 0.01)
check("corr(grey, charcoal) about 0.9", np.corrcoef(np.log(np.abs(Z(pts))), off)[0, 1], 0.9, 0.03)
w = np.linspace(1e6, 1e6 + 12, 600)
offw = np.array([float(mpmath.log(abs(mpmath.zeta(mpmath.mpc(s0, x))))) for x in w])
check("rms difference on the window", np.sqrt(np.mean((offw - P(w, 10 ** 3)) ** 2)), 0.28, 0.01)
# ex:half
for k in range(2, 21, 2):
    check(f"ex:half k={k}", 2 ** -k * math.comb(k, k // 2) * math.factorial(k // 2), 2 ** (-k / 2) * math.prod(range(k - 1, 0, -2)), 1e-12)
# ex:jointbj: L(2 sigma, chi_4) < 1
for sg in [0.55, 0.7, 0.9]:
    Lv = float(mpmath.nsum(lambda n: (-1) ** n / (2 * n + 1) ** (2 * sg), [0, mpmath.inf]))
    check_true(f"L(2sigma,chi_4) < 1 - 3^-2s + 5^-2s < 1, sigma={sg}", Lv < 1 - 3 ** (-2 * sg) + 5 ** (-2 * sg) < 1)
finish()
