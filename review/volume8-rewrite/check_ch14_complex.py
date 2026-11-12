#!/usr/bin/env python3
"""Volume 8, Chapter 14: the elementary factor bound, Stirling on vertical lines, the convexity exponent, M(1-e^-x) = -Gamma,
Mellin inversion for e^-x, the theta sum, the maximum of geometric levels (constant, wobble bound, numerical mean),
the Lambert series of d(n), |Gamma(iy)|^2, the doubly exponential example and the sine product."""
import mpmath as mp
from common import check, check_true, finish
mp.mp.dps = 30
# E_p bound
ok = True
for p in range(0, 5):
    E = lambda z: (1 - z)*mp.exp(sum(z**k/k for k in range(1, p + 1)))
    for r in (0.1, 0.5, 0.9, 1.0):
        for th in mp.linspace(0, 2*mp.pi, 25):
            z = r*mp.e**(1j*th); ok &= abs(1 - E(z)) <= abs(z)**(p + 1) + 1e-20
check_true("|1 - E_p(z)| <= |z|^(p+1) on |z| <= 1, p = 0..4", ok)
# Stirling on vertical lines
for sig in (-0.5, 0.25, 2.0):
    t = mp.mpf(200); check(f"|Gamma(sigma+it)| / (sqrt(2pi) t^(sigma-1/2) e^(-pi t/2)) at sigma = {sig}, t = 200", abs(mp.gamma(sig + 1j*t))/(mp.sqrt(2*mp.pi)*t**(sig - 0.5)*mp.e**(-mp.pi*t/2)), 1, 1e-2)
# convexity: zeta(1/2+it) / t^(1/4) stays bounded on a sample
vals = [abs(mp.zeta(0.5 + 1j*t))/t**0.25 for t in (100, 1000, 10000)]
check_true(f"|zeta(1/2+it)|/t^(1/4) bounded on samples: {[float(v) for v in vals]}", max(vals) < 3)
# M(1 - e^-x) = -Gamma(s) for -1 < sigma < 0
for s in (-0.5, -0.3 + 2j):
    check(f"M(1-e^-x)({s}) = -Gamma", abs(mp.quad(lambda x: (1 - mp.e**-x)*x**(s - 1), [0, 1, mp.inf]) + mp.gamma(s)), 0, 1e-9)
# Mellin inversion for e^-x at c = 1
x = mp.mpf("0.7")
inv = mp.quad(lambda tau: mp.gamma(1 + 1j*tau)*x**(-(1 + 1j*tau)), [-mp.inf, 0, mp.inf])/(2*mp.pi)
check("Mellin inversion recovers e^-0.7", abs(inv - mp.e**-x), 0, 1e-12)
# theta sum
for x in (0.1, 0.01):
    G = mp.nsum(lambda k: mp.e**(-k*k*x), [1, mp.inf])
    check(f"G({x}) - (1/2 sqrt(pi/x) - 1/2) = sqrt(pi/x) sum e^(-pi^2 k^2/x)", G - (mp.sqrt(mp.pi/x)/2 - mp.mpf(1)/2), mp.sqrt(mp.pi/x)*mp.nsum(lambda k: mp.e**(-mp.pi**2*k*k/x), [1, mp.inf]), 1e-25)
# maximum of geometric levels
c0 = mp.euler/mp.log(2) - mp.mpf(1)/2
check("gamma/ln2 - 1/2", c0, 0.3327, 1e-4)
yk = lambda k: 2*mp.pi*k/mp.log(2)
check("y_1 = 2 pi / ln 2", yk(1), 9.06, 5e-3)
bound = 2/mp.log(2)*mp.nsum(lambda k: mp.sqrt(mp.pi/(yk(k)*mp.sinh(mp.pi*yk(k)))), [1, mp.inf])
check_true(f"wobble bound {float(bound):.4g} < 1.6e-6", bound < 1.6e-6)
for y in (1.3, 9.06): check(f"|Gamma(iy)|^2 = pi/(y sinh pi y) at y = {y}", abs(mp.gamma(1j*y))**2, mp.pi/(y*mp.sinh(mp.pi*y)), 1e-25)
for x in (mp.mpf(10)**6, mp.mpf(3)*10**7):
    EH = mp.nsum(lambda k: 1 - mp.e**(-x*2**-k), [1, mp.inf])
    P = -2/mp.log(2)*mp.re(sum(mp.gamma(1j*yk(k))*mp.e**(-2j*mp.pi*k*mp.log(x, 2)) for k in range(1, 6)))
    check(f"E[H] at x = {float(x):.0e} equals log2 x + gamma/ln2 - 1/2 + P(log2 x)", EH, mp.log(x, 2) + c0 + P, 1e-15)
# Lambert series
for x in (mp.mpf("0.05"), mp.mpf("0.01")):
    L = mp.nsum(lambda k: 1/(mp.e**(k*x) - 1), [1, mp.inf])
    approx = (mp.log(1/x) + mp.euler)/x + mp.mpf(1)/4 - x/144
    check_true(f"Lambert series at x = {float(x)}: error {float(abs(L - approx)):.2e} is O(x^(3/2))", abs(L - approx) < x**1.5)
# exp(exp(-is))
s = mp.pi/2 + 3j; check("|exp(exp(-is))| on sigma = pi/2", abs(mp.e**(mp.e**(-1j*s))), 1, 1e-20)
check("|exp(exp(-i(it)))| = exp(e^t) at t = 2", abs(mp.e**(mp.e**(-1j*(2j)))), mp.e**(mp.e**2), 1e-15)
# sine product
z = mp.mpf("0.3"); check("sin(pi z) = pi z prod (1 - z^2/n^2)", mp.sin(mp.pi*z), mp.pi*z*mp.nprod(lambda n: 1 - z*z/n**2, [1, mp.inf]), 1e-15)
check("zeros of cos sqrt z at ((k+1/2) pi)^2", abs(mp.cos(mp.sqrt(((2 + 0.5)*mp.pi)**2))), 0, 1e-25)
finish()
