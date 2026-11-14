#!/usr/bin/env python3
"""Recompute the printed numbers of Chapter 13 (ch13-bias.tex, ra-bias.tex).
Slow parts (the race to 10^9, the Lemke Oliver-Soundararajan count) are in race_mod4.py and lastdigit.py; their outputs are
compared here if passed as files: python3 check_ch13_bias.py race.txt lastdigit.txt"""
import sys, math, re, numpy as np, mpmath
from scipy import special, integrate
from common import check, check_true, finish
from lchi4_zeros import zeros, L
g = 0.5772156649015329
check("L(1, chi_-4) = pi/4", float(L(1)), math.pi / 4, 1e-12)
Lp = float(mpmath.diff(L, 1)); check("L'(1) = 0.19290", Lp, 0.19290, 5e-6)
V = math.log(4 / math.pi) - g + 2 * Lp / (math.pi / 4)
check("V = 0.15557", V, 0.15557, 5e-6); check("sqrt V = 0.394", math.sqrt(V), 0.394, 5e-4)
check("Chebyshev bound 1 - V/2 >= 0.92", 1 - V / 2, 0.92, 5e-3)
check("head start in standard deviations ~ 2.5", 1 / math.sqrt(V), 2.5, 0.05)
z = np.array(zeros(300))
for got, pr in zip(z[:7], [6.0209, 10.2438, 12.9881, 16.3426, 18.2920, 21.4506, 23.2784]):
    check(f"ordinate {pr}", got, pr, 5e-5)
r = np.sqrt(.25 + z ** 2)
for k, pr in enumerate([0.3310, 0.1950, 0.1539, 0.1223, 0.1093, 0.0932, 0.0859]):
    check(f"2/|rho_{k+1}|", 2 / r[k], pr, 5e-5)
cs = np.cumsum(2 / r[:7])
for k, pr in enumerate([0.3310, 0.5260, 0.6799, 0.8022, 0.9115, 1.0047]):
    check(f"partial sum {k+1}", cs[k], pr, 1.5e-4)
check_true("least k with sum > 1 is 6", int(np.argmax(cs > 1)) + 1 == 6)
check("203 positive ordinates below 300", len(z), 203, 0)
check("3130 positive ordinates below 3000 (Riemann-von Mangoldt main term)", 3000 / (2 * math.pi) * math.log(4 * 3000 / (2 * math.pi * math.e)), 3130, 3)
tail = V - np.sum(2 / r ** 2)
phi = lambda x: np.prod(special.j0(2 * x / r)) * math.exp(-tail * x * x / 2)
delta = 0.5 + integrate.quad(lambda x: math.sin(x) / x * phi(x), 0, 200, limit=2000)[0] / math.pi
check("delta(4;3,1) = 0.99593", delta, 0.99593, 5e-6)
check("mass left of 0 ~ 0.0041", 1 - delta, 0.0041, 5e-5)
xs = np.linspace(0.01, 200, 200000)
check_true("|J0(x)| <= sqrt(2/(pi x))", bool(np.all(np.abs(special.j0(xs)) <= np.sqrt(2 / (np.pi * xs)) + 1e-12)))
check("first zeta zero 14.13", float(mpmath.zetazero(1).imag), 14.13, 5e-3)
z3 = float(mpmath.findroot(lambda s: mpmath.dirichlet(s, [0, 1, -1]), mpmath.mpc(.5, 8.04)).imag)
check("first zero of L(s,chi_-3) 8.04", z3, 8.04, 5e-3)
if len(sys.argv) > 1:
    t = open(sys.argv[1]).read(); m = re.search(r"c1 (\d+) c3 (\d+) first lead (\d+) lead share of log scale ([\d.e-]+)", t)
    check("primes 4n+1 below 1e9", int(m.group(1)), 25423491, 0); check("primes 4n+3 below 1e9", int(m.group(2)), 25424042, 0)
    check("first lead of 4n+1", int(m.group(3)), 26861, 0); check("share of log scale 0.04%", float(m.group(4)), 0.0004, 5e-5)
    check("u = log 26861 = 10.2", math.log(26861), 10.2, 0.05)
if len(sys.argv) > 2:
    t = open(sys.argv[2]).read(); v = float(re.search(r"= ([\d.]+)", t).group(1))
    check("1 followed by 1 among the first 1e8 primes ~ 18%", v, 0.18, 0.006)
finish()
