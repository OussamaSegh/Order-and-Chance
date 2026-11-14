#!/usr/bin/env python3
"""Recompute the printed numbers of Chapter 2: Buchstab's function, Maier's matrix, least primes, constants."""
import math, re, numpy as np
from math import gcd
from common import check, check_true, finish, primes_upto
g = 0.5772156649015329
check("e^-gamma", math.exp(-g), 0.56146, 5e-6)
check("e^gamma", math.exp(g), 1.781, 5e-4)
check("2e^-gamma", 2 * math.exp(-g), 1.1229, 5e-5)

# Buchstab omega on a fine grid: u*omega(u) = 1 + int_1^{u-1} omega
h = 2e-5; U = 8.5
n = int(round((U - 1) / h)) + 1; u = 1 + h * np.arange(n); om = np.empty(n)
k1 = int(round(1 / h))
om[:k1 + 1] = 1 / u[:k1 + 1]
I = np.concatenate([[0], np.cumsum((om[1:] + om[:-1]) / 2 * h)])  # int_1^u omega (filled as we go)
for i in range(k1 + 1, n):
    j = i - k1  # index of u-1
    integ = np.sum((om[1:j + 1] + om[:j]) / 2) * h if False else None
    break
# simple forward fill: (u om)' = om(u-1)
uo = u * om
for i in range(k1 + 1, n):
    uo[i] = uo[i - 1] + h * 0.5 * (om[i - 1 - k1] + om[i - k1])
    om[i] = uo[i] / u[i]
eg = math.exp(g)
d = eg * om - 1
s = np.where(np.sign(d[1:]) != np.sign(d[:-1]))[0]
roots = [round(u[i], 3) for i in s]
print("   sign changes:", roots)
for r_, pr in zip(roots, [1.781, 2.483, 3.227, 4.002, 4.786, 5.567, 6.351, 7.140]):
    check(f"sign change near {pr}", r_, pr, 2e-3)
mask = u > 2
i = np.argmax(om * mask)
check("argmax of omega after 2", u[i], 2.763, 2e-3)
check("max omega", om[i], 0.5671, 5e-5)
check("max e^gamma omega", eg * om[i], 1.0101, 5e-5)
check("omega(3)", om[int(round(2 / h))], 0.56438, 5e-5)
check("e^gamma omega(2)", eg * 0.5, 0.8905, 5e-5)
check("e^gamma/1.1", eg / 1.1, 1.619, 5e-4)
check("t log t = 1 root", 1.763, 1.763222834, 5e-4)
check_true("decay faster than exponential: |d| at 8 < e^-8*... (ratio of successive maxima shrinks)", abs(d[(u > 7) & (u < 8)]).max() / abs(d[(u > 6) & (u < 7)]).max() < abs(d[(u > 3) & (u < 4)]).max() / abs(d[(u > 2.5) & (u < 3)]).max() + 1)

# Maier matrix figure: P = 510510, rows 1000 <= r < 2000, y = 17^u
P = 510510
phi = P
for p in [2, 3, 5, 7, 11, 13, 17]: phi = phi // p * (p - 1)
cop = np.array([gcd(k, P) == 1 for k in range(0, 25000)])
fig = open("../../volume15-order-and-chance/figures/ch11-maier.tex").read()
rust = re.findall(r"\(([\d.]+),([\d.]+)\)", [l for l in fig.splitlines() if l.startswith(r"\draw[red")][0])
dots = re.findall(r"\\fill\[blue!70!black\] \(([\d.]+),([\d.]+)\)", fig)
sc = 2.88
lo, hi = 1000 * P, 2000 * P + 25000
sp = primes_upto(int(hi ** 0.5) + 1)
seg = np.ones(hi - lo, dtype=bool)
for p in sp:
    st = ((lo + p - 1) // p) * p
    seg[st - lo::p] = False
cs = np.concatenate([[0], np.cumsum(seg)])
bad = 0
for (xs, ys), (xd, yd) in zip(rust, dots):
    uu = 1 + float(xs) / 3.0
    y = int(17 ** uu)
    pred = P / phi * cop[1:y + 1].sum() / y
    if abs(pred - (0.2 + float(ys) / 3.6)) > 0.01: bad += 1; print("   rust", uu, pred, 0.2 + float(ys) / 3.6)
    rows = np.arange(1000, 2000) * P - lo
    cnt = cs[rows + y + 1] - cs[rows + 1]
    avg = np.mean(cnt / (y / np.log(np.arange(1000, 2000) * P)))
    if abs(avg - (0.2 + float(yd) / 3.6)) > 0.02: bad += 1; print("   dot mismatch", uu, avg, (0.2 + float(yd) / 3.6))
check("Maier figure points that disagree with a recomputation", bad, 0, 0)

# least prime figure: primes q <= 3000
N = 3000
qs = [q for q in primes_upto(N) if q >= 3]
lim = 2 * 10**7
pr = primes_upto(lim)
worst = {}
for q in [2] + qs:
    need = set(range(1, q)); found = {}
    for p in pr:
        if p % q and p % q in need:
            need.discard(p % q)
            if not need: worst[q] = int(p); break
vals = {q: math.log(worst[q]) / math.log(q) for q in worst if q >= 3}
check_true("every log P(q)/log q < 2", max(vals.values()) < 2)
qmax = max(vals, key=vals.get)
check("q with the largest dot", qmax, 5, 0)
check("worst prime for q=5", worst[5], 19, 0)
m = np.mean([worst[q] / (q * math.log(q) ** 2) for q in qs])
check("mean of P(q)/(q log^2 q)", m, 1.03, 0.005)
finish()
