#!/usr/bin/env python3
"""Numeric checks for Volume 5, Chapter 3 (Classic Series and Infinite Products).

Run: python3 review/volume5-rewrite/check_ch03_series.py
"""
from fractions import Fraction as Fr
from math import comb, factorial, floor, gcd, isqrt
import mpmath as mp

mp.mp.dps = 40
ok = True


def check(name, cond):
    global ok
    print(("ok   " if cond else "FAIL ") + name)
    ok = ok and bool(cond)


pi = mp.pi
# infinite products
check("prod_{n>=2}(1-1/n^2) = 1/2 (partial product (N+1)/(2N))",
      all(__import__('functools').reduce(lambda u, v: u * v, (1 - Fr(1, n * n) for n in range(2, N + 1))) == Fr(N + 1, 2 * N) for N in (2, 5, 50)))
# cotangent
for x in (mp.mpf("0.3"), mp.mpf("-1.7"), mp.mpf("4.25")):
    s = 1 / x + mp.nsum(lambda n: 2 * x / (x * x - n * n), [1, mp.inf])
    check("pi cot(pi x) partial fractions at x=%s" % x, abs(s - pi * mp.cot(pi * x)) < mp.mpf(10) ** -25)
    check("duplication cot(y) - tan(y) = 2 cot(2y) at %s" % x, abs(mp.cot(x) - mp.tan(x) - 2 * mp.cot(2 * x)) < mp.mpf(10) ** -30)
# sine product, error of order x^2/N
x = mp.mpf("0.7")
PN = lambda N: pi * x * mp.fprod(1 - x * x / (n * n) for n in range(1, N + 1))
check("sine product converges, relative error about x^2/N",
      abs(PN(4000) / mp.sin(pi * x) - 1 - x * x / 4000) < mp.mpf(10) ** -6)
# Wallis and Viete
W = mp.fprod(mp.mpf(4 * n * n) / ((2 * n - 1) * (2 * n + 1)) for n in range(1, 200001))
check("Wallis product -> pi/2", abs(W - pi / 2) < mp.mpf(10) ** -5)
V = mp.fprod(mp.cos(pi / 2 ** (k + 1)) for k in range(1, 80))
check("Viete product = 2/pi", abs(V - 2 / pi) < mp.mpf(10) ** -30)
rad, vv = mp.sqrt(2), mp.mpf(1)
for _ in range(80):
    vv *= rad / 2
    rad = mp.sqrt(2 + rad)
check("Viete nested radicals = 2/pi", abs(vv - 2 / pi) < mp.mpf(10) ** -30)
area = lambda n: n / mp.mpf(2) * mp.sin(2 * pi / n)
check("polygon areas 2, 2 sqrt 2 = 2.83, 3.06", area(4) == 2 and abs(area(8) - 2 * mp.sqrt(2)) < 1e-30 and
      abs(area(8) - mp.mpf("2.83")) < 0.005 and abs(area(16) - mp.mpf("3.06")) < 0.005)
check("doubling the sides multiplies the area by 1/cos(pi/2^k)",
      all(abs(area(2 ** (k + 1)) / area(2**k) - 1 / mp.cos(pi / 2**k)) < mp.mpf(10) ** -30 for k in range(2, 12)))


# Bernoulli numbers and zeta(2k)
def bernoulli(m):
    B = [Fr(1)]
    for n in range(1, m + 1):
        B.append(-sum(comb(n + 1, k) * B[k] for k in range(n)) / (n + 1))
    return B


B = bernoulli(40)
check("B_2, B_4, B_6, B_8 = 1/6, -1/30, 1/42, -1/30", [B[2], B[4], B[6], B[8]] == [Fr(1, 6), Fr(-1, 30), Fr(1, 42), Fr(-1, 30)])
for k in range(1, 20):
    val = (-1) ** (k + 1) * mp.mpf(B[2 * k].numerator) / B[2 * k].denominator * (2 * pi) ** (2 * k) / (2 * mp.factorial(2 * k))
    if abs(val - mp.zeta(2 * k)) > mp.mpf(10) ** -30:
        check("zeta(2k) formula, k=%d" % k, False)
check("zeta(2k) = (-1)^(k+1) B_2k (2 pi)^2k / (2 (2k)!) for k < 20", True)
coef = lambda k: Fr((-1) ** (k + 1)) * B[2 * k] * 2 ** (2 * k) / (2 * factorial(2 * k))
check("zeta(2), (4), (6), (8) = pi^2/6, pi^4/90, pi^6/945, pi^8/9450",
      [coef(k) for k in (1, 2, 3, 4)] == [Fr(1, 6), Fr(1, 90), Fr(1, 945), Fr(1, 9450)])
check("64/60480 = 1/945 and 256/2419200 = 1/9450; 42*2*720 = 60480; 30*2*40320 = 2419200",
      Fr(64, 60480) == Fr(1, 945) and Fr(256, 2419200) == Fr(1, 9450) and 42 * 2 * 720 == 60480 and 30 * 2 * 40320 == 2419200)
check("0 < zeta(2k) - 1 <= 3/4^k", all(0 < mp.zeta(2 * k) - 1 <= mp.mpf(3) / 4**k for k in range(1, 30)))
check("sum 1/(2n+1)^4 = pi^4/96, alternating zeta(2) = pi^2/12",
      abs(mp.nsum(lambda n: 1 / (2 * n + 1) ** 4, [0, mp.inf]) - pi**4 / 96) < mp.mpf(10) ** -25 and
      abs(mp.altzeta(2) - pi**2 / 12) < mp.mpf(10) ** -30)
# exercises
a = mp.mpf("0.5")
check("sum 1/(n^2 - 1/4) = 2", abs(mp.nsum(lambda n: 1 / (n * n - a * a), [1, mp.inf]) - 2) < mp.mpf(10) ** -25)
a = mp.mpf("0.37")
check("sum 1/(n^2-a^2) = 1/(2a^2) - pi cot(pi a)/(2a)",
      abs(mp.nsum(lambda n: 1 / (n * n - a * a), [1, mp.inf]) - (1 / (2 * a * a) - pi * mp.cot(pi * a) / (2 * a))) < mp.mpf(10) ** -25)
check("Leibniz: error after n terms at most 1/(2n+1)",
      all(abs(pi / 4 - sum(mp.mpf((-1) ** k) / (2 * k + 1) for k in range(n))) <= mp.mpf(1) / (2 * n + 1) for n in (1, 10, 1000)))
I1 = mp.quad(lambda x: -mp.log(x) / (1 - x * x), [0, 0.5, 1])
check("int_0^1 -ln x/(1-x^2) = pi^2/8", abs(I1 - pi**2 / 8) < mp.mpf(10) ** -20)
check("int_0^inf dy/(sqrt y (1+y)) = pi", abs(mp.quad(lambda t: 2 / (1 + t * t), [0, mp.inf]) - pi) < mp.mpf(10) ** -25)
check("int_0^1 (-ln x) x^(2n) = 1/(2n+1)^2", all(abs(mp.quad(lambda x: -mp.log(x) * x ** (2 * n), [0, 1]) - mp.mpf(1) / (2 * n + 1) ** 2) < mp.mpf(10) ** -20 for n in range(4)))
# e: tails
for n in (5, 12):
    A = sum(factorial(n) // factorial(k) for k in range(n + 1))
    C = sum((-1) ** k * (factorial(n) // factorial(k)) for k in range(n + 1))
    r, s = factorial(n) * mp.e - A, factorial(n) / mp.e - C
    check("tails of n! e and n!/e, n=%d" % n, 0 < r < mp.mpf(1) / n and mp.sign(s) == (-1) ** (n + 1) and abs(s) < mp.mpf(1) / (n + 1))


# continued fraction of sqrt d
def cf_sqrt(d):
    a0 = isqrt(d)
    m, q, a, out = 0, 1, a0, []
    while True:
        m = q * a - m
        q = (d - m * m) // q
        a = (a0 + m) // q
        out.append(a)
        if a == 2 * a0:
            return a0, out


check("sqrt 14 = [3; 1,2,1,6]", cf_sqrt(14) == (3, [1, 2, 1, 6]))
check("period of sqrt d ends with 2 a_0, d < 500", all(cf_sqrt(d)[1][-1] == 2 * isqrt(d) for d in range(2, 500) if isqrt(d) ** 2 != d))
# coprime pairs
S = sum(mp.mpf(1) / (a_ * a_ * b_ * b_) for a_ in range(1, 1500) for b_ in range(1, 1500) if gcd(a_, b_) == 1)
check("sum over coprime pairs of 1/(ab)^2 = 5/2 = zeta(2)^2/zeta(4)", abs(S - 2.5) < 5e-3 and abs(mp.zeta(2) ** 2 / mp.zeta(4) - 2.5) < mp.mpf(10) ** -30)
omega = lambda n: sum(1 for p in range(2, n + 1) if n % p == 0 and all(p % q for q in range(2, p)))
check("c_n = 2^omega(n)", all(sum(1 for a_ in range(1, n + 1) if n % a_ == 0 and gcd(a_, n // a_) == 1) == 2 ** omega(n) for n in range(1, 200)))
# irrationality proof: F'' + pi^2 F telescopes (check with a rational stand-in for pi^2)
import sympy as sp
xs, c = sp.symbols("x c")
n = 3
f = xs**n * (1 - xs) ** n / sp.factorial(n)
F = sum((-1) ** k * c ** (n - k) * sp.diff(f, xs, 2 * k) for k in range(n + 1))
check("F'' + c F = c^(n+1) f (c in place of pi^2)", sp.expand(sp.diff(F, xs, 2) + c * F - c ** (n + 1) * f) == 0)
check("f^(k)(0), f^(k)(1) integers", all(sp.diff(f, xs, k).subs(xs, v).is_integer for k in range(0, 2 * n + 1) for v in (0, 1)))
# Levy's constant (exercise now at the end of Chapter 10)
check("pi^2/(12 log 2) = 1.18656... (truncated)", mp.floor(pi**2 / (12 * mp.log(2)) * 10**5) == 118656)
check("int_0^1 -log t/(1+t) = pi^2/12", abs(mp.quad(lambda t: -mp.log(t) / (1 + t), [0, 1]) - pi**2 / 12) < mp.mpf(10) ** -20)
check("2 zeta(3) - 3/2 = 0.9041", abs(2 * mp.zeta(3) - 1.5 - mp.mpf("0.9041")) < 5e-5)

print("\nALL CHECKS PASSED" if ok else "\nSOME CHECKS FAILED")
raise SystemExit(0 if ok else 1)
