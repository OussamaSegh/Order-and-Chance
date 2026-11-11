#!/usr/bin/env python3
"""Chapter 2 (Arithmetic Functions on Average): every printed number that the page does not prove."""
import math
import numpy as np
from mpmath import mp, zeta, findroot, diff, mpf
from common import *
mp.dps = 25
N = 10**6

# divisor counts up to 10^6
tau = np.zeros(N + 1, dtype=np.int32)
for d in range(1, N + 1): tau[d::d] += 1
check("tau(720720)", int(tau[720720]), 240, 0)
check("mean of tau, n<=10^6 (formula)", math.log(N) + 2 * GAMMA - 1, 13.97, 6e-3)
check("mean of tau, n<=10^6 (exact)", tau[1:].mean(), 13.97, 6e-3)
check("median of tau", float(np.median(tau[1:])), 8, 0)
check("share with tau>=14", float((tau[1:] >= 14).mean()), 0.34, 5e-3)
check("(log 10^6)^log 2", math.log(N) ** math.log(2), 6.2, 0.05)

# Figure 2.1: coprime pairs in [1,24]^2
vis = sum(1 for a in range(1, 25) for b in range(1, 25) if math.gcd(a, b) == 1)
check("coprime pairs in 24x24", vis, 359, 0)
check("proportion", vis / 576, 0.623, 5e-4)
check("6/pi^2", 6 / math.pi**2, 0.6079, 1e-4)

# three-fold divisor function: constant term of P_3 (Stieltjes gamma_1 = -0.0728158...)
g1 = float(mp.stieltjes(1))
check("constant term of P_3", 3 * GAMMA**2 - 3 * GAMMA - 3 * g1 + 1, 0.4863, 1e-4)
# divisor problem remark
check("131/416", 131 / 416, 0.3149, 1e-4)
check("Cramer's constant", float(zeta(1.5)**4 / zeta(3) / (6 * mp.pi**2)), 0.6543, 1e-4)
check("x^(1/4) at 400", 400**0.25, 4.5, 0.05); check("x^(1/4) at 1600", 1600**0.25, 6.3, 0.05)
cs = np.cumsum(tau[1:401 * 4].astype(np.int64))
D = lambda x: int(cs[x - 1]) - x * math.log(x) - (2 * GAMMA - 1) * x
rms = math.sqrt(np.mean([(D(x) / x**0.25) ** 2 for x in range(400, 1601)]))
check_true(f"rms of Delta/x^(1/4) on [400,1600] is close to 1 (computed {rms:.3f}; Cramer predicts sqrt(c*3/2)... order 1)", 0.5 < rms < 1.5)

# Exercises
check("zeta(2)zeta(3)/zeta(6)", float(zeta(2) * zeta(3) / zeta(6)), 1.9435, 1e-4)
phi = np.arange(N + 1, dtype=np.int64)
for p in primes_upto(N).tolist(): phi[p::p] -= phi[p::p] // p
n = np.arange(1, N + 1)
check("mean of n/phi(n), n<=10^6", float((n / phi[1:]).mean()), 1.94358, 2e-5)
check("mean of phi(n)/n", float((phi[1:] / n).mean()), 0.608, 5e-4)
check("1/zeta(3)", float(1 / zeta(3)), 0.8319, 1e-4)
mu = np.ones(1001, dtype=np.int64)
for p in primes_upto(1000).tolist():
    mu[p::p] *= -1; mu[p * p::p * p] = 0
for k, got, lim in ((2, 0.60838, 0.60793), (3, 0.83205, 0.83191), (4, 0.92399, 0.92394)):
    Ck = sum(int(mu[d]) * (1000 // d) ** k for d in range(1, 1001))
    check(f"C_{k}(1000)/1000^{k}", Ck / 1000**k, got, 6e-6)
    check(f"1/zeta({k})", float(1 / zeta(k)), lim, 6e-6)
r = 1000
Nr = sum(2 * math.isqrt(r * r - a * a) + 1 for a in range(-r, r + 1))
check("N(1000) - pi 10^6", Nr - math.pi * r * r, -43.65, 6e-3)
check("bound pi(sqrt2 r + 1/2)", math.pi * (math.sqrt(2) * r + 0.5), 4444, 1)
zp = float(diff(zeta, 2) / zeta(2))
check("C for 2^omega", 6 / math.pi**2 * (2 * GAMMA - 1 - 2 * zp), 0.7869, 1e-4)
check("tau(12)^2 = 36", int(tau[12])**2, 36, 0)
check_true("tau(n) <= sqrt(3n) with equality only at 12", all((tau[m]**2 < 3 * m) or m == 12 for m in range(1, N + 1)) and tau[12]**2 == 36)
check("720720 = 2^4 3^2 5 7 11 13", 2**4 * 3**2 * 5 * 7 * 11 * 13, 720720, 0)
# phi(n)/n: proportion with phi(n) <= n/2
check("share with phi(n)<=n/2", float((2 * phi[1:] <= n).mean()), 0.511, 1e-3)
check("phi(105)", int(phi[105]), 48, 0)
# ordered factorisations
rho = float(findroot(lambda s: zeta(s) - 2, 1.7))
check("rho", rho, 1.7286, 1e-4)
H = [0, 1] + [0] * 2000
for m in range(2, 2002): H[m] = sum(H[d] for d in range(1, m) if m % d == 0)
check("H(12)", H[12], 8, 0)
check_true("H(p^a) = 2^(a-1)", all(H[2**a] == 2**(a - 1) for a in range(1, 11)))
check_true("Fubini numbers 1,3,13,75", [H[2], H[6], H[30], H[210]] == [1, 3, 13, 75])
check_true("H(n) <= n^rho for n<=2001", all(H[m] <= m**rho for m in range(1, 2002)))
check("Kalmar's constant", float(-1 / (rho * diff(zeta, rho))), 0.3181, 1e-4)
# remainders on average
check("1 - pi^2/12", 1 - math.pi**2 / 12, 0.1775, 1e-4)
Nn = 10**5
check_true("sum (N mod n) ~ (1-pi^2/12) N^2 at N=10^5", abs(sum(Nn % k for k in range(1, Nn + 1)) / Nn**2 - (1 - math.pi**2 / 12)) < 1e-4)
check_true("sum {x/n} ~ (1-gamma) x at x=10^5", abs(sum((Nn % k) / k for k in range(1, Nn + 1)) / Nn - (1 - GAMMA)) < 1e-3)
# radical
P = primes_upto(10**7).astype(float)
C = float(np.prod(1 - 1 / (P * (P + 1))))
check("C = prod(1-1/(p(p+1)))", C, 0.70444, 1e-5)
M7 = 10**7
rad = np.ones(M7 + 1, dtype=np.int64)
for p in primes_upto(M7).tolist(): rad[p::p] *= p
check("2/x^2 sum rad(n), x=10^7", 2 * float(rad[1:].sum()) / M7**2, 0.704446, 2e-6)
check("C to six places", C, 0.704442, 2e-6)
check("zeta(3/2)", float(zeta(1.5)), 2.612, 1e-3)
finish()
