#!/usr/bin/env python3
"""Recompute the printed numbers of Chapter 10 (ch10-moments.tex, ra-moments.tex)."""
import math, numpy as np
from common import check, check_true, finish, primes_upto
from rs_zeta import Z
from fig_ch10_ratios import ratios, ak, G
g = 0.5772156649015329
# a_k
check("a_1 = 1", ak(1), 1, 1e-9)
check("a_2 = 6/pi^2", ak(2), 6 / math.pi ** 2, 1e-7)
def ak_real(k, P=10 ** 6):
    s = 0.0
    for p in primes_upto(P):
        u = 1 / p; c = 1.0; tot = 0.0
        for r in range(80):
            tot += c * c * u ** r; c *= (k + r) / (r + 1)
        s += k * k * math.log1p(-u) + math.log(tot)
    return math.exp(s)
check("a_{1/2} = 0.988", ak_real(0.5), 0.988, 5e-4)
# h_0 expansion: coefficient of u^2 is -k^2(k-1)^2/4
for k in [0.5, 1, 2, 3, 1.7]:
    u = 1e-4; c = 1.0; tot = 0.0
    for r in range(10):
        tot += c * c * u ** r; c *= (k + r) / (r + 1)
    h0 = (1 - u) ** (k * k) * tot
    check(f"h_0 u^2 coefficient, k={k}", (h0 - 1) / u ** 2, -k * k * (k - 1) ** 2 / 4, 2e-3 * max(1, k ** 4))
check("exp(-1/64 sum p^-2)", math.exp(-sum(p ** -2.0 for p in primes_upto(10 ** 6)) / 64), math.exp(-0.007), 3e-4)
# g_k
for k, gk in [(1, 1), (2, 2), (3, 42), (4, 24024)]:
    check(f"g_{k}", G(k + 1) ** 2 / G(2 * k + 1) * math.factorial(k * k), gk, 1e-6)
    check(f"G-ratio as prod j!/(j+k)!, k={k}", G(k + 1) ** 2 / G(2 * k + 1), math.prod(math.factorial(j) / math.factorial(j + k) for j in range(k)), 1e-12 * G(k + 1) ** 2 / G(2 * k + 1))
check("a_2/12 = 1/(2pi^2)", 6 / math.pi ** 2 / 12, 1 / (2 * math.pi ** 2), 1e-15)
# ex:ak generating function
u = 0.3
check("sum (r+1)^2 u^r = (1+u)/(1-u)^3", sum((r + 1) ** 2 * u ** r for r in range(200)), (1 + u) / (1 - u) ** 3, 1e-12)
# ex:lognormal numbers at T=10^6
L = math.log(1e6)
for k, pr in [(1, 0.07), (2, 3e-5), (3, 6e-11)]:
    check(f"(log 10^6)^(-k^2), k={k}", L ** (-k * k), pr, 0.35 * pr)
# lem:dk2 shape for k=2: sum d(n)^2/n over (log x)^4 bounded and positive
x = 10 ** 6
d = np.zeros(x + 1, dtype=np.int64)
for i in range(1, x + 1): d[i::i] += 1
S = np.sum(d[1:] ** 2 / np.arange(1, x + 1))
print("   sum_{n<=1e6} d(n)^2/n / (log x)^4 =", round(S / math.log(x) ** 4, 4), " (limit 1/(4 pi^2) =", round(1 / (4 * math.pi ** 2), 4), ")")
check_true("lem:dk2, k=2: ratio between 0.02 and 0.2 at x=1e6", 0.02 < S / math.log(x) ** 4 < 0.2)
# figure ch08-share at T=10^6
rng = np.random.default_rng(5); t = rng.uniform(1e6, 2e6, 400000); z = np.abs(Z(t))
for k, top1, top01 in [(1, .31, .07), (2, .77, .33), (3, .95, .60)]:
    w = np.sort(z ** (2 * k))[::-1]; tot = w.sum()
    check(f"share of top 1%, k={k}", w[:4000].sum() / tot, top1, 0.012)
    check(f"share of top 0.1%, k={k}", w[:400].sum() / tot, top01, 0.03)
# figure ch08-ratios at T=10^6, and k=1 against Theorem ingham
r = ratios(1e6, 400000, 7)
Lt = np.log(t / (2 * math.pi))
check("k=1 ratio 1.09 (Monte Carlo)", r[1], 1.09, 0.025)
check("theory: mean(L+2gamma)/mean(L)", np.mean(Lt + 2 * g) / np.mean(Lt), 1.09, 0.005)
check("log(t/2pi) ~ 12.4 on [1e6,2e6]", np.mean(Lt), 12.4, 0.05)
check("k=2 ratio about 2.5", r[2], 2.5, 0.12)
check("k=3 ratio about 45", r[3], 45, 4)
finish()
