#!/usr/bin/env python3
"""Recompute the printed numbers of Chapter 6 (ch06-sieves.tex) and test its inequalities on examples."""
import math, itertools, random
from fractions import Fraction as F
from math import gcd
import numpy as np
from common import check, check_true, finish, primes_upto

g = 0.5772156649015329
eg = math.exp(g)

# ---------- Bonferroni example, n <= 30 ----------
S1, S2, S3 = F(15 + 10 + 6, 30), F(5 + 3 + 2, 30), F(1, 30)
part = [F(1), 1 - S1, 1 - S1 + S2, 1 - S1 + S2 - S3]
for v, pr in zip(part, [1, -0.033, 0.300, 0.267]):
    check(f"Bonferroni partial sum {pr}", float(v), pr, 5e-4)
check("phi(30)/30", sum(1 for n in range(1, 31) if gcd(n, 30) == 1) / 30, 0.267, 5e-4)

# ---------- Selberg example P=30, D=6 ----------
ds = [1, 2, 3, 5, 6]
lcm = lambda a, b: a * b // gcd(a, b)
G6 = sum(F(1, 1) if d == 1 else F(1, math.prod(p - 1 for p in [2, 3, 5] if d % p == 0)) for d in ds)
check("G(6) = 13/4", float(G6), 13 / 4, 0)
# minimise sum lambda_d lambda_e / lcm subject to lambda_1 = 1: solve linear system
Q = np.array([[1 / lcm(a, b) for b in ds] for a in ds])
Qr = Q[1:, 1:]; q = Q[1:, 0]
lam = np.concatenate(([1.0], -np.linalg.solve(Qr, q)))
for d, l, pr in zip(ds, lam, [1, -12 / 13, -12 / 13, -5 / 13, 12 / 13]):
    check(f"Selberg weight lambda_{d}", l, pr, 1e-12)
m6 = lam @ Q @ lam
check("m_6 = 4/13", m6, 4 / 13, 1e-12)
check("4/13", 4 / 13, 0.308, 5e-4)
check("alpha = P(A)/m = 13/15", (8 / 30) / m6, 13 / 15, 1e-12)
check("15% too big", m6 / (8 / 30) - 1, 0.15, 0.01)
# orthogonality to 1_{e|n} for e=2,3,5,6 on Z/30
for e in [2, 3, 5, 6]:
    val = sum(sum(l for d, l in zip(ds, lam) if n % d == 0) for n in range(30) if n % e == 0) / 30
    check(f"E[f* 1_(e|n)] = 0, e={e}", val, 0, 1e-12)
check_true("|lambda_d| <= 1", bool(np.all(np.abs(lam) <= 1 + 1e-12)))

# ---------- factor 2 discussion ----------
check("e^gamma", eg, 1.78, 5e-3)
check("2 e^-gamma", 2 / eg, 1.1229, 5e-5)
check("e^gamma/2", eg / 2, 0.8905, 5e-5)

# ---------- Brun's pure sieve: the inequality on examples, and Exercise brunsmall ----------
def Phi(x, z):
    P = math.prod(int(p) for p in primes_upto(int(z)) if p < z)
    return sum(1 for n in range(1, int(x) + 1) if gcd(n, P) == 1)
def W(z): return math.prod(1 - 1 / p for p in primes_upto(int(z)) if p < z)
def L(z): return sum(1 / p for p in primes_upto(int(z)) if p < z)
ok = True
for x in [100, 1000, 12345.6, 10**5]:
    for z in [3, 5, 11, 30, 50]:
        for r in range(0, 4):
            if 2 * r + 2 < L(z): continue
            bound = x * L(z) ** (2 * r + 1) / math.factorial(2 * r + 1) + 3 * z ** (2 * r + 1)
            ok &= abs(Phi(x, z) - x * W(z)) <= bound
check_true("Brun's pure sieve inequality on examples", ok)
check("Phi(1000,11)", Phi(1000, 11), 228, 0)
check("192 in [1,840]", Phi(840, 11), 192, 0)
small = [m for m in range(1, 161) if gcd(m, 210) == 1]
check("survivors in [1,160]", len(small), 36, 0)
check("primes 11..157", sum(1 for p in primes_upto(157) if p >= 11), 33, 0)
check_true("composite survivors are 121 and 143", [m for m in small if m > 1 and not all(m % p for p in range(2, int(m ** .5) + 1))] == [121, 143])
check("1000 W(11)", 1000 * W(11), 228.6, 0.05)
check("L(11)", L(11), 1.176, 5e-4)
check("bound r=1", 1000 * L(11) ** 3 / 6 + 3 * 11 ** 3, 4264, 0.5)
check("bound r=0", 1000 * L(11) + 33, 1209, 0.5)
# corollary constants
check_true("5.5 log(5/e) >= 3.3", 5.5 * math.log(5 / math.e) >= 3.3)
check_true("e*1.1/5.5 = e/5", abs(math.e * 1.1 / 5.5 - math.e / 5) < 1e-15)
check_true("(6l+1)/(10l) <= 0.7 for l >= 1", all((6 * l + 1) / (10 * l) <= 0.7 for l in np.linspace(1, 50, 500)))
check_true("e^-gamma >= 1/2 (W(x) >= 1/(2 log x) eventually)", math.exp(-g) > 0.5)

# ---------- Buchstab table ----------
h = 1e-5
u = np.arange(1, 8 + h / 2, h)
w = np.where(u <= 2, 1 / u, 0.0)
cum = np.zeros_like(u)
k1 = int(round(1 / h))
for i in range(1, len(u)):
    if u[i] > 2 + 1e-12:
        w[i] = (1 + cum[i - k1]) / u[i]
    cum[i] = cum[i - 1] + h * (w[i] + w[i - 1]) / 2
def om(x): return w[int(round((x - 1) / h))]
for x, pr in [(1.5, 1.187), (2, 0.891), (2.5, 1.001), (3, 1.005), (4, 1.000)]:
    check(f"e^gamma omega({x})", eg * om(x), pr, 5e-4)
from scipy.optimize import brentq
f = lambda t: (1 + math.log(t - 1)) / t
u0 = brentq(lambda t: f(t) - math.exp(-g), 2, 2.76)
check("u0", u0, 2.483, 5e-4)
t0 = brentq(lambda t: 1 / t - math.log(t), 1, 2)
check("t0", t0, 1.763, 5e-4)
check("max at 2.763: e^gamma f", eg * f(1 + t0), 1.0101, 5e-5)
check("f(3)", f(3), 0.5644, 5e-5)
check("e^-gamma", math.exp(-g), 0.5615, 5e-5)
check("overshoot at u=2 (12%)", 1 / (eg / 2) - 1, 0.12, 0.005)
check("undershoot at u=1.5 (16%)", 1 - 1 / (eg / 1.5), 0.16, 0.005)

# ---------- Schnirelmann: lemmas on random examples, and the exercises ----------
def sigma(A, n=600):
    A = set(A); c = 0; best = 1.0
    for m in range(1, n + 1):
        c += m in A; best = min(best, c / m)
    return best
def sumset(A, B, n=600):
    return {a + b for a in A for b in B if a + b <= n}
random.seed(1)
ok1 = ok2 = True
for _ in range(60):
    A = {0, 1} | {m for m in range(2, 601) if random.random() < random.uniform(0.05, 0.6)}
    B = {0} | ({1} if random.random() < 0.8 else set()) | {m for m in range(2, 601) if random.random() < random.uniform(0.05, 0.6)}
    sa, sb, sab = sigma(A), sigma(B), sigma(sumset(A, B))
    ok1 &= sab >= sa + sb - sa * sb - 1e-12
    if sa + sb >= 1:
        ok2 &= set(range(0, 601)) <= sumset(A, B) | set()
check_true("Schnirelmann's inequality on 60 random pairs (n <= 600)", ok1)
check_true("sigma(A)+sigma(B) >= 1 gives everything (random pairs)", ok2)
Q = {k * k for k in range(0, 40)}
check_true("not sums of two squares up to 10: 3, 6, 7", [n for n in range(1, 11) if n not in sumset(Q, Q)] == [3, 6, 7])
A = {0} | {n for n in range(1, 601) if n % 3 == 1}
check("sigma(A)", sigma(A), 1 / 3, 1e-12)
check("sigma(2A)", sigma(sumset(A, A)), 2 / 3, 1e-12)
check("sigma(3A)", sigma(sumset(sumset(A, A), A)), 1.0, 1e-12)

# ---------- sum over N <= x of prod (1+1/p)^2 is O(x): constant prod(1+3/p^2) ----------
c2 = math.prod(1 + 3 / p**2 for p in primes_upto(10**6))
print("   prod(1+3/p^2) =", round(c2, 4))
x = 10**5
spf_prod = np.ones(x + 1)
for p in primes_upto(x):
    spf_prod[p::p] *= (1 + 1 / p) ** 2
check_true("sum_{N<=x} prod_{p|N}(1+1/p)^2 <= c2 x at x=1e5", spf_prod[1:].sum() <= c2 * x)
finish()
