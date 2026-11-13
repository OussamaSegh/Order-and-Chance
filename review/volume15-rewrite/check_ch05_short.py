#!/usr/bin/env python3
"""Recompute the printed numbers of Chapter 5 (ch05-short.tex): singular series, pair average, variance of psi in short intervals.

Needs about 4 GB of memory (Lambda and psi up to 10^8) and runs in a few minutes.
"""
import math, numpy as np
from scipy.integrate import quad
from common import check, check_true, finish, primes_upto

g = 0.5772156649015329
L2PI = math.log(2 * math.pi)
C2 = 0.66016181584686957392781211  # twin prime constant (Wrench); checked against a partial product below
P = primes_upto(10**7)
part = math.exp(np.sum(np.log1p(-1.0 / (P[1:].astype(float) - 1) ** 2)))
check("C2 partial product to 1e7", part, C2, 1e-7)
check("C2 (printed 0.6601...)", math.floor(C2 * 1e4) / 1e4, 0.6601, 1e-12)
check("2 C2", 2 * C2, 1.32, 5e-3)
check("(1-gamma-log 2pi)/2", (1 - g - L2PI) / 2, -0.7075, 5e-5)
check("gamma + log 2pi", g + L2PI, 2.4151, 5e-5)
check("gamma + log 2pi - 1", g + L2PI - 1, 1.415, 5e-4)
I1 = sum(quad(lambda t: (t - k) / t**2, k, k + 1)[0] for k in range(1, 20000)) + 0.5 / 20000
check("int {t}/t^2 = 1-gamma", I1, 1 - g, 1e-4)
check("I = 2 - log 2pi", 2 - L2PI, 0.1621, 5e-5)
I2 = sum(quad(lambda t: (t - k) * (1 - t + k) / t**2, k, k + 1)[0] for k in range(1, 20000)) + (1 / 6) / 20000
check("int beta(t)/t^2 numerically", I2, 2 - L2PI, 1e-5)

# ---------- table of Theorem pairexpansion ----------
HMAX = 10**5
S = np.zeros(HMAX + 1)
odd_part_factor = np.ones(HMAX + 1)
for p in primes_upto(HMAX):
    if p == 2: continue
    odd_part_factor[p::p] *= (p - 1) / (p - 2)
S[2::2] = 2 * C2 * odd_part_factor[2::2]
check("S(2) = 2 C2", S[2], 2 * C2, 1e-15)
# brute force singular series for a few h from the definition (product over p <= 10^5)
def S_def(hs, pmax=10**5):
    k = len(hs); val = 1.0
    for p in primes_upto(pmax):
        nu = len({h % p for h in hs})
        val *= (1 - nu / p) / (1 - 1 / p) ** k
    return val
for h in [2, 6, 30]:
    check(f"S(0,{h}) from definition", S_def([0, h]), S[h], 2e-5)
for H, printed in [(10**2, 1.8), (10**3, 2.6), (10**4, 9.2), (10**5, 3.0)]:
    lhs = math.fsum((H - h) * S[h] for h in range(1, H + 1))
    main = H * H / 2 - 0.5 * H * math.log(H) + 0.5 * (1 - g - L2PI) * H
    check(f"pair sum minus main terms, H={H}", lhs - main, printed, 0.05)
    if H == 10**5:
        check("left side at H=1e5 (about 5e9)", lhs / 1e9, 5.0, 0.01)
        check("third term at 1e5", -0.5 * (1 - g - L2PI) * H, 70755, 1)
check("two thirds at H = X^(1/3)", 1 - 1 / 3, 2 / 3, 1e-15)

# ---------- Exercises ----------
check("b_5 for (0,2,6)", (1 - 3 / 5) / (1 - 1 / 5) ** 3, 50 / 64, 1e-15)
check("4 * 9/8", 4 * 9 / 8, 4.5, 0)
check("log 21", math.log(21), 3.045, 5e-4)
check("log 1e9", math.log(1e9), 20.72, 5e-3)
check("ratio with 2.415", 1 - (math.log(21) + g + L2PI) / math.log(1e9), 0.737, 5e-4)
check("ratio with 1.415", 1 - (math.log(21) + g + L2PI - 1) / math.log(1e9), 0.785, 5e-4)
check("0.785 * 1.01", 0.785 * 1.01, 0.79, 5e-3)
check("0.785 lambda with log X=20.7", 1 - (math.log(21) + 1.415) / 20.7, 0.785, 5e-4)
check("0.785 * 1.01", 0.785 * 1.01, 0.79, 5e-3)
check("1 - 1 + 1/2", 0.5, 0.5, 0)
check("1 - 1 + 1/2 - 1/6", 1 - 1 + 0.5 - 1 / 6, 0.333, 5e-4)
check("e^-1", math.exp(-1), 0.368, 5e-4)
check("log 1e8", math.log(1e8), 18.4, 0.05)

# ---------- opening: a million intervals of length 21 starting at 10^9 ----------
lo = 10**9; n_int = 10**6; L = 21
seg = np.ones(L * n_int + 1, dtype=bool)
for p in primes_upto(int(math.isqrt(lo + L * n_int)) + 1):
    st = ((lo + 1 + p - 1) // p) * p
    seg[st - (lo + 1)::p] = False
counts = seg[:L * n_int].reshape(n_int, L).sum(axis=1)
check("mean count near 1e9 (V6 Fig 10.2)", counts.mean(), 1.013, 5e-4)
check("variance of the count near 1e9", counts.var(), 0.79, 5e-3)

# ---------- V(X,H) at X = 10^8 ----------
X = 10**8; HM = 10**4
N = X + HM + 1
sieve = np.ones(N + 1, dtype=bool); sieve[:2] = False
for p in range(2, int(N ** 0.5) + 1):
    if sieve[p]: sieve[p * p::p] = False
Lam = np.zeros(N + 1)
pr = np.nonzero(sieve)[0]
Lam[pr] = np.log(pr)
del sieve
for p in pr[pr <= int(N ** 0.5) + 1]:
    q = p * p
    while q <= N:
        Lam[q] = math.log(p); q *= p
psi = np.cumsum(Lam); del Lam
def V(H, a=1, b=X):
    n = np.arange(a, b + 1)
    th = psi[n + H] - psi[n] - H
    return float(np.dot(th, th)) / (b - a + 1)
def pred(H, XX, const=g + L2PI):
    return H * math.log(XX / H) - const * H
v100, v1000 = V(100), V(1000)
check("V(1e8,100)", v100, 1142.8, 0.05)
check("prediction H=100", pred(100, X), 1140.0, 0.05)
check("Cramer H=100", 100 * math.log(X), 1842.1, 0.05)
check("V(1e8,1000)", v1000, 9076.5, 0.05)
check("prediction H=1000", pred(1000, X), 9097.8, 0.05)
check("Cramer H=1000", 1000 * math.log(X), 18420.7, 0.05)
# the remark: window ]0.9e8, 1e8]
vw = V(100, 9 * 10**7 + 1, X)
check("window variance H=100", vw, 1237.8, 0.05)
check("formula 1.415 at X=0.95e8", pred(100, 0.95e8, g + L2PI - 1), 1234.9, 0.05)
check("formula 2.415 at X=0.95e8", pred(100, 0.95e8), 1134.9, 0.05)
# the figure: relative deviation up to 3000, and near 1e4
devs = {}
for H in [10, 20, 30, 50, 100, 200, 300, 500, 1000, 2000, 3000, 5000, 10000]:
    devs[H] = abs(V(H) / pred(H, X) - 1)
    print(f"   H={H}: V/H={V(H)/H:.3f}, prediction {pred(H, X)/H:.3f}, rel dev {devs[H]*100:.2f}%")
check_true("within 1% up to H=3000", max(d for H, d in devs.items() if H <= 3000) <= 0.01)
check("deviation at H=1e4 (1.6%)", devs[10000] * 100, 1.6, 0.1)
finish()
