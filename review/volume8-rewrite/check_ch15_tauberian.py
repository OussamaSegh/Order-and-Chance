#!/usr/bin/env python3
"""Volume 8, Chapter 15: Ces\`aro means of the Abel-not-Ces\`aro example, Karamata on powers, the Fejer pair, the trapezoid,
the sinc bound 2/pi, the Landau-Ramanujan constant, the partition bound, quicksort (exact formula, monotonicity, the
million-item numbers), the oscillating example of Wiener-Ikehara, Wiener on Z, and Tauber's age."""
from math import pi, sqrt, log, lgamma, gamma, sin, cos, isclose
import numpy as np
from scipy.integrate import quad
from sympy import primerange
from common import check, check_true, finish
a = [(-1)**n*(n + 1) for n in range(2000)]; s = np.cumsum(a); sig = np.cumsum(s)/np.arange(1, 2001)
check("sigma_{2m} -> 1/2 (m = 999)", sig[1998], 0.5, 1e-3); check("sigma_{2m+1} = 0", abs(sig[1999]), 0, 0)
for rho in (0.5, 2.0):
    for k in (0, 3): check(f"I(y^{k}) = (k+1)^-rho for rho = {rho}", quad(lambda v: np.exp(-(k + 1)*v)*v**(rho - 1), 0, np.inf)[0]/gamma(rho), (k + 1)**-rho, 1e-8)
F = lambda x: (np.sinc(x))**2
for xi in (0.0, 0.3, 0.8, 1.5):
    check(f"Fejer transform at {xi} = (1-|xi|)_+", quad(lambda x: F(x)*np.cos(2*pi*x*xi), -400, 400, limit=4000)[0], max(0, 1 - abs(xi)), 3e-3)
Lam = lambda x: max(0.0, 1 - abs(x))
check_true("2 Lambda(xi/2) - Lambda(xi) is the trapezoid", all(isclose(2*Lam(x/2) - Lam(x), 1 if abs(x) <= 1 else (2 - abs(x) if abs(x) <= 2 else 0), abs_tol=1e-12) for x in np.linspace(-3, 3, 121)))
check_true("sin(pi x)/(pi x) >= 2/pi on |x| <= 1/2", min(np.sinc(np.linspace(-0.5, 0.5, 1001))) >= 2/pi - 1e-12)
P = 1.0
for q in primerange(3, 10**7):
    if q % 4 == 3: P *= 1/(1 - q**-2)
check("Landau-Ramanujan K = (1/sqrt2) prod (1-q^-2)^(-1/2)", sqrt(P/2), 0.7642236535, 1e-7)
check("(pi/4) * 2 * P(1) = pi K^2", pi/4*2*P, pi*(sqrt(P/2))**2, 1e-12)
check("Gamma(3/2) = sqrt(pi)/2", gamma(1.5), sqrt(pi)/2, 1e-15)
pp = [1] + [0]*300
for part in range(1, 301):
    for m in range(part, 301): pp[m] += pp[m - part]
check_true("log p(n) <= pi sqrt(2n/3) for n = 1..300", all(log(pp[n]) <= pi*sqrt(2*n/3) for n in range(1, 301)))
C = [0.0]
for n in range(1, 60): C.append(n - 1 + 2/n*sum(C))
H = lambda n: sum(1/k for k in range(1, n + 1))
check_true("C_n = 2(n+1)H_n - 4n for n < 60", all(abs(C[n] - (2*(n + 1)*H(n) - 4*n)) < 1e-9 for n in range(60)))
check_true("C_n non-decreasing", all(C[n + 1] >= C[n] for n in range(59)))
n = 10**6; Hn = log(n) + 0.5772156649 + 1/(2*n)
check("C_(10^6)", 2*(n + 1)*Hn - 4*n, 2.48e7, 2e5); check("log2(10^6!)", lgamma(n + 1)/log(2), 1.85e7, 1e5)
check("2 ln 2", 2*log(2), 1.39, 5e-3)
# 1 + cos(log n): partial sums over x near peaks and troughs
for target, val in ((2*pi*2 + pi/4, 1 + 1/sqrt(2)), (2*pi*2 + pi/4 + pi, 1 - 1/sqrt(2))):
    x = int(np.exp(target))
    k = np.arange(1, x + 1, dtype=float); A = (1 + np.cos(np.log(k))).sum()
    check(f"(1/x) sum_(n<=x) (1+cos log n) at log x = {target:.3f}", A/x, val, 1e-3)
check("1 - 1/sqrt 2", 1 - 1/sqrt(2), 0.29, 5e-3)
check_true("|2 + e^(it)|/3 > 0 everywhere", min(abs(2 + np.exp(1j*np.linspace(0, 2*pi, 1000)))/3) > 0.3)
check("Tauber's age in June 1942 (born 5 November 1866)", 1942 - 1866 - 1, 75, 0)
finish()
