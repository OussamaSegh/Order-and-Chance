#!/usr/bin/env python3
"""Numerical checks for Volume 5, Chapter 10 (The Zeta Function)."""
from fractions import Fraction
from math import gcd, isqrt
from mpmath import (mp, mpf, mpc, pi, exp, log, sqrt, gamma, zeta, nsum, inf, quad, cos, bernoulli,
                    zetazero, siegelz, euler, jtheta, floor, altzeta, primepi)
from sympy import primerange, mobius, totient, divisor_count, divisor_sigma, bernoulli as sbern, Rational

mp.dps = 30
ok = True
def check(name, cond):
    global ok
    print(("ok   " if cond else "FAIL ") + name)
    ok = ok and bool(cond)
def close(a, b, tol=mpf(10) ** -10):
    return abs(a - b) <= tol * max(1, abs(b))

# opening: partial Euler products at s = 2
prod, seen = mpf(1), {}
for p in primerange(2, 1000):
    prod *= 1 / (1 - mpf(p) ** -2)
    seen[p] = prod
check("Euler products 4/3, 3/2, 1.5625", seen[2] == mpf(4) / 3 and close(seen[3], 1.5) and close(seen[5], 1.5625))
check("1.5951, 1.6083, 1.6179 at p = 7, 11, 13", all(abs(seen[p] - v) < 5e-5 for p, v in ((7, 1.5951), (11, 1.6083), (13, 1.6179))))
check("1.64473 after the primes below 1000; pi^2/6 = 1.64493", abs(seen[997] - 1.64473) < 5e-6 and abs(pi**2 / 6 - 1.64493) < 5e-6)

# Dirichlet series identities at s = 3 (truncated sums)
N = 20000
def D(f, s): return sum(mpf(int(f(n))) / mpf(n) ** s for n in range(1, N))
check("sum mu/n^s = 1/zeta", abs(D(mobius, 3) - 1 / zeta(3)) < 1e-7)
check("sum phi/n^s = zeta(s-1)/zeta(s)", abs(D(totient, 4) - zeta(3) / zeta(4)) < 1e-7)
check("sum tau/n^s = zeta^2, sum sigma/n^s = zeta(s)zeta(s-1)", abs(D(divisor_count, 3) - zeta(3) ** 2) < 1e-6 and abs(D(divisor_sigma, 4) - zeta(4) * zeta(3)) < 1e-6)
check("sum |mu|/n^s = zeta(s)/zeta(2s)", abs(D(lambda n: abs(mobius(n)), 3) - zeta(3) / zeta(6)) < 1e-7)
check("6/pi^2 = 0.6079", abs(6 / pi**2 - 0.6079) < 5e-5)
M = 2000
cop = sum(1 for a in range(1, M + 1) for b in range(1, M + 1) if gcd(a, b) == 1)
check("coprime pairs up to 2000: density near 6/pi^2", abs(cop / M**2 - 6 / pi**2) < 2e-3)
NN = 10**6
Q = sum(int(mobius(d)) * (NN // (d * d)) for d in range(1, isqrt(NN) + 1))
sieve = bytearray([1]) * (NN + 1)
for d in range(2, isqrt(NN) + 1):
    sieve[d * d::d * d] = bytearray(len(sieve[d * d::d * d]))
check("squarefree count formula and density", Q == sum(sieve[1:]) and abs(Q / NN - 6 / pi**2) < 1e-3)

# zeta near 1
h = mpf(10) ** -8
check("zeta(s) - 1/(s-1) -> gamma", abs(zeta(1 + h) - 1 / h - euler) < 1e-7)
sg = mpf('1.001')
check("log zeta(sigma) - log 1/(sigma-1) between 0 and sigma-1", 0 <= log(zeta(sg)) - log(1 / (sg - 1)) <= sg - 1)
ps = sum(mpf(p) ** -sg for p in primerange(2, 10**6)) + quad(lambda x: x ** -sg / log(x), [10**6, inf])
check("sum p^-sigma = log 1/(sigma-1) + O(1), bound 2 zeta(2)+1", abs(ps - log(1 / (sg - 1))) < 2 * zeta(2) + 1)

# Mellin of the Gaussian, omega, theta
s = mpc(1.7, 2.3)
check("lem:mellingauss", close(quad(lambda t: exp(-pi * 9 * t) * t ** (s / 2 - 1), [0, 1, inf]), pi ** (-s / 2) * gamma(s / 2) * 3 ** -s, mpf(10) ** -12))
def omega(t): return nsum(lambda n: exp(-pi * n * n * t), [1, inf])
check("omega(t) <= 2 e^{-pi t} for t >= 1; e^-pi < 1/2", all(omega(t) <= 2 * exp(-pi * t) for t in (1, 1.5, 3)) and exp(-pi) < 0.5)
theta1 = 1 + 2 * omega(1)
check("omega(t) <= theta(1) t^{-1/2}/2 for t <= 1", all(omega(t) <= theta1 / (2 * sqrt(t)) for t in (mpf('0.01'), mpf('0.3'), 1)))
u = mpf('2.7')
check("omega(1/u) = sqrt u omega(u) + sqrt u/2 - 1/2", close(omega(1 / u), sqrt(u) * omega(u) + sqrt(u) / 2 - mpf(1) / 2))

# the theorem: xi(s) = 1/2 + s(s-1)/2 * I(s)
def I(s): return quad(lambda t: omega(t) * (t ** (s / 2) + t ** ((1 - s) / 2)) / t, [1, 2, 5, 20])
def xi_def(s): return s * (s - 1) / 2 * pi ** (-s / 2) * gamma(s / 2) * zeta(s)
for s in (mpc(2.5, 1), mpc(0.3, 4), mpc(-1.5, 2)):
    check(f"xi formula at {s}", close(xi_def(s), mpf(1) / 2 + s * (s - 1) / 2 * I(s), mpf(10) ** -12))
    check(f"xi(1-s) = xi(s) at {s}", close(xi_def(1 - s), xi_def(s), mpf(10) ** -12))
    check(f"zeta = pi^(s/2) xi/((s-1) Gamma(s/2+1)) at {s}", close(zeta(s), pi ** (s / 2) * xi_def(s) / ((s - 1) * gamma(s / 2 + 1))))
    check(f"asymmetric functional equation at {s}", close(zeta(1 - s), 2 * (2 * pi) ** -s * cos(pi * s / 2) * gamma(s) * zeta(s)))
check("xi(0) = xi(1) = 1/2 (limits)", abs(xi_def(mpf(10) ** -12) - 0.5) < 1e-10 and abs(xi_def(1 + mpf(10) ** -12) - 0.5) < 1e-10)
check("Gamma(3/2) = sqrt(pi)/2", close(gamma(1.5), sqrt(pi) / 2))
check("asymmetric equation at integers 2, 3, 4", all(close(zeta(1 - k), 2 * (2 * pi) ** -k * cos(pi * mpf(k) / 2) * gamma(k) * zeta(k)) for k in (2, 3, 4)))

# values at non-positive integers
check("zeta(0) = -1/2, trivial zeros", close(zeta(0), -0.5) and all(abs(zeta(-2 * k)) < 1e-25 for k in (1, 2, 3)))
vals = {1: Fraction(-1, 12), 2: Fraction(1, 120), 3: Fraction(-1, 252), 4: Fraction(1, 240)}
check("zeta(1-2k) = -B_2k/2k: -1/12, 1/120, -1/252, 1/240",
      all(-Fraction(int(sbern(2 * k).p), int(sbern(2 * k).q)) / (2 * k) == v and close(zeta(1 - 2 * k), mpf(v.numerator) / v.denominator) for k, v in vals.items()))
check("B_2, B_4, B_6, B_8", [sbern(k) for k in (2, 4, 6, 8)] == [Rational(1, 6), Rational(-1, 30), Rational(1, 42), Rational(-1, 30)])

# smoothed sums
for Nn in (50, 400):
    h = mpf(1) / Nn
    s0 = nsum(lambda n: exp(-n * h), [1, inf]); s1 = nsum(lambda n: n * exp(-n * h), [1, inf])
    check(f"smoothed sums k=0,1 at N={Nn}", abs(s0 - Nn + 0.5) < 1 / mpf(Nn) and abs(s1 - Nn**2 + mpf(1) / 12) < 1 / mpf(Nn) ** 2)
    for k in range(0, 7):
        sk = nsum(lambda n: n ** k * exp(-n * h), [1, inf])
        const = (-1) ** k * bernoulli(k + 1) / (k + 1)
        check(f"  k={k}: constant (-1)^k B_(k+1)/(k+1) = zeta(-k), error O(1/N)", close(const, zeta(-k)) and abs(sk - gamma(k + 1) * Nn ** (k + 1) - const) < 3 / mpf(Nn))
s3 = nsum(lambda n: n ** 3 * exp(-n / mpf(100)), [1, inf])
check("N=100, k=3: 6e8 + 0.0083331", abs(s3 - 6 * 10**8 - mpf('0.0083331')) < 5e-8)
check("alternating: sum (-1)^n e^{-n/N} -> 1/2 = eta(0)", abs(1 / (1 + exp(-mpf(1) / 1000)) - 0.5) < 1e-3 and close(altzeta(0), 0.5))

# zeros and Hardy's Z
zs = [zetazero(k).imag for k in range(1, 12)]
printed = [14.13, 21.02, 25.01, 30.42, 32.94, 37.59, 40.92, 43.33, 48.01, 49.77]
check("ten zeros with 0 < t < 50, as printed", all(abs(a - b) < 0.006 for a, b in zip(zs, printed)) and zs[10] > 50)
check("Z real with |Z| = |zeta|, changes sign at each zero", all(abs(abs(siegelz(t)) - abs(zeta(mpc(0.5, t)))) < 1e-15 for t in (3, 17, 40))
      and all(siegelz(z - 0.05) * siegelz(z + 0.05) < 0 for z in zs[:10]))
from mpmath import arg, loggamma
def alpha(t): return loggamma(mpc(0.25, t / 2)).imag - t / 2 * log(pi)
for t in (5, 17.3, 33):
    t = mpf(t); s = mpc(0.5, t)
    lhs = xi_def(s)
    rhs = -(t * t + 0.25) / (2 * pi ** 0.25) * abs(gamma(mpc(0.25, t / 2))) * (exp(1j * alpha(t)) * zeta(s))
    check(f"xi(1/2+it) = -(t^2+1/4)/(2 pi^(1/4)) |Gamma| Z(t), real, at t={t}", close(lhs, rhs) and abs(lhs.imag) < 1e-20 and close(exp(1j * alpha(t)) * zeta(s), siegelz(t)))

# eta and zeta(1/2)
check("eta(s) = (1-2^(1-s)) zeta(s); zeta(1/2) = -1.4604", close(altzeta(mpf('0.5')), (1 - sqrt(2)) * zeta(0.5)) and abs(zeta(0.5) + 1.4604) < 5e-5)

# Hurwitz
from mpmath import bernpoly
check("zeta(-n, a) = -B_(n+1)(a)/(n+1)", all(close(zeta(-n, a), -bernpoly(n + 1, a) / (n + 1)) for n in range(0, 6) for a in (mpf('0.3'), mpf(1))))
check("B_m(1-a) = (-1)^m B_m(a)", all(close(bernpoly(m, 0.7), (-1) ** m * bernpoly(m, 0.3)) for m in range(8)))
check("zeta(2), zeta(4) from the functional equation", close(-2 * pi**2 * zeta(-1), pi**2 / 6) and close(4 * pi**4 * zeta(-3) / 3, pi**4 / 90))

# Gauss-Kuzmin
c = mpf(1) / 2 + 2 * nsum(lambda k: 1 / (k**3 * (k + 1)), [2, inf]) + nsum(lambda k: (k - 1) / (k * (k + 1) ** 2), [2, inf])
check("c = 2 zeta(3) - 3/2 = 0.9041", close(c, 2 * zeta(3) - 1.5) and abs(c - 0.9041) < 5e-5)
check("the two sums", close(nsum(lambda k: 1 / (k**3 * (k + 1)), [2, inf]), zeta(3) - zeta(2) + 0.5) and close(nsum(lambda k: (k - 1) / (k * (k + 1) ** 2), [2, inf]), 2 * zeta(2) - 3))
def P(k, t): return (1 + t) / ((k + t) * (k + t + 1))
def dP(k, t): return (k * k - k - (1 + t) ** 2) / ((k + t) ** 2 * (k + t + 1) ** 2)
t = mpf('0.37')
check("sum P_k = 1; formula for P_k'", close(nsum(lambda k: P(k, t), [1, inf]), 1) and all(close(dP(k, t), (P(k, t + 1e-10) - P(k, t - 1e-10)) / 2e-10, mpf(10) ** -6) for k in (1, 2, 5)))
check("bounds used in (c)", all(abs(dP(k, t)) <= mpf(1) / (k + 1) ** 2 and P(k, t) / (k + t) ** 2 <= mpf(2) / (k**3 * (k + 1)) for k in range(2, 50) for t in (0, mpf('0.5'), 1))
      and all(1 / ((1 + t) ** 2 * (2 + t)) <= 0.5 for t in (0, 0.5, 1)))
# iterate the density recursion on a grid and compare with Gauss's law and the bound c^n
import numpy as np
grid = np.linspace(0, 1, 2001)
f = np.ones_like(grid)
good = True
for n in range(1, 7):
    g = np.zeros_like(grid)
    for k in range(1, 4000):
        g += np.interp(1 / (k + grid), grid, f) / (k + grid) ** 2
    g += np.interp(0.0, grid, f) / (4000 + grid - 0.5)  # tail of sum 1/(k+t)^2 with f ~ f(0)
    f = g
    err = np.max(np.abs(f - 1 / ((1 + grid) * np.log(2))) * (1 + grid))
    good = good and err <= float(c) ** n
check("density recursion: |f_n - Gauss density| (1+t) <= c^n for n <= 6", good)
check("after 6 steps the error is about 0.3037^6 in size (Wirsing's rate is plausible)", err < 5e-3)
check("Gauss-Kuzmin law sums to 1", close(nsum(lambda k: log((k + 1) ** 2 / (k * (k + 2)), 2), [1, inf]), 1))

# Levy
check("int -log t/(1+t) = pi^2/12; constant 1.18656", close(quad(lambda t: -log(t) / (1 + t), [0, 1]), pi**2 / 12) and 0 <= pi**2 / (12 * log(2)) - 1.18656 < 1e-5)
check("e^1.1866", abs(log(exp(pi**2 / (12 * log(2)))) - 1.1866) < 5e-5)
import random
random.seed(1)
from fractions import Fraction as Fr
tot, trials, n = 0.0, 300, 30
for _ in range(trials):
    x = Fr(random.getrandbits(400), 2**400); q0, q1 = 0, 1
    for _ in range(n):
        a = int(1 / x); x = 1 / x - a; q0, q1 = q1, a * q1 + q0
    tot += float(log(q1))
print("     E log q_n - n*L =", tot / trials - n * 1.18656)
check("E log q_n = n L + O(1) (simulation)", abs(tot / trials - n * 1.18656) < 1.0)

print("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED")
raise SystemExit(0 if ok else 1)
