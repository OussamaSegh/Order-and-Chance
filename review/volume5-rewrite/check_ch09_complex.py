#!/usr/bin/env python3
"""Numerical checks for Volume 5, Chapter 9 (Complex Analysis for Computing)."""
from fractions import Fraction
from math import factorial, gcd, log, floor
from mpmath import mp, mpf, mpc, pi, e, exp, sin, cos, sinh, cosh, coth, tanh, cot, sqrt, quad, quadosc, nsum, inf, gamma, zeta, polyroots, euler, sec, tan, taylor, log as mlog

mp.dps = 30
ok = True
def check(name, cond):
    global ok
    print(("ok   " if cond else "FAIL ") + name)
    ok = ok and bool(cond)
def close(a, b, tol=mpf(10) ** -10):
    return abs(a - b) <= tol * max(1, abs(b))
def circ(f, a, r, n=4000):
    """(1/2 pi i) * integral of f over the circle C(a, r), trapezoid rule (spectrally accurate)."""
    return sum(f(a + r * exp(2j * pi * k / n)) * r * exp(2j * pi * k / n) for k in range(n)) / n

# the opening puzzle
check("int cos x/(1+x^2) = pi/e", close(2 * quadosc(lambda x: cos(x) / (1 + x * x), [0, inf], omega=1), pi / e, mpf(10) ** -8))
check("int dx/(1+x^4) = pi/sqrt 2", close(quad(lambda x: 1 / (1 + x**4), [-inf, 0, inf]), pi / sqrt(2)))
a = mpf('0.3')
check("int e^(at)/(1+e^t) = pi/sin(pi a)", close(quad(lambda t: exp(a * t) / (1 + exp(t)), [-inf, 0, inf]), pi / sin(pi * a)))
xi = mpf('0.45')
check("Gaussian with shifted line", close(quad(lambda x: exp(-pi * (x + 1j * xi) ** 2), [-inf, 0, inf]), 1))

# basic contour facts
check("int over circle of 1/(z-a) is 2 pi i; of (z-a)^n is 0", close(circ(lambda z: 1 / (z - 0.3), 0.3, 1, 400), 1) and abs(circ(lambda z: (z - 0.3) ** 3, 0.3, 1, 400)) < 1e-20 and abs(circ(lambda z: (z - 0.3) ** -2, 0.3, 1, 400)) < 1e-20)
f = lambda z: exp(z) * cos(z)
check("Cauchy's formula", close(circ(lambda w: f(w) / (w - mpc(0.2, 0.1)), 0, 1, 400), f(mpc(0.2, 0.1))))
check("Bernoulli generating function: radius 2 pi (h has zeros at 2 pi i k)", abs(exp(2j * pi) - 1) < 1e-25)
check("residue of pi cot(pi z) at integers is 1", close(circ(lambda z: pi * cot(pi * z), 3, mpf('0.3'), 400), 1))
check("pi cot(pi z) = 1/z - pi^2 z/3 + ...", close(circ(lambda z: pi * cot(pi * z) / z**2, 0, mpf('0.3'), 400), -pi**2 / 3))
check("coth(pi/2) = 1.09 < 2", abs(coth(pi / 2) - mpf('1.09')) < 5e-3)
worst = 0
for N in (0, 1, 5):
    h = N + mpf(1) / 2
    for k in range(-200, 201):
        t = h * k / 200
        for z in (mpc(h, t), mpc(-h, t), mpc(t, h), mpc(t, -h)):
            worst = max(worst, abs(cot(pi * z)))
check("|cot(pi z)| <= coth(pi/2) on the squares C_N", worst <= coth(pi / 2) + mpf(10) ** -20)
z0 = mpc(0.3, 0.4)
check("partial fractions of the cotangent at a complex point", close(pi * cot(pi * z0), 1 / z0 + nsum(lambda n: 2 * z0 / (z0 * z0 - n * n), [1, inf]), mpf(10) ** -8))
check("zeta(4) = -1/2 Res_0 pi cot(pi z)/z^4", close(-circ(lambda z: pi * cot(pi * z) / z**4, 0, mpf('0.3'), 400) / 2, zeta(4)))

# Gamma in the complex plane
for n in range(0, 5):
    check(f"residue of Gamma at -{n} is (-1)^n/n!", close(circ(gamma, -n, mpf('0.3'), 600), mpf((-1) ** n) / factorial(n)))
y = mpf('1.7')
check("|Gamma(1/2+iy)|^2 = pi/cosh(pi y)", close(abs(gamma(mpc(0.5, y))) ** 2, pi / cosh(pi * y)))
check("|Gamma(1/2+iy)| ~ sqrt(2 pi) e^(-pi|y|/2)", abs(abs(gamma(mpc(0.5, 8))) / (sqrt(2 * pi) * exp(-4 * pi)) - 1) < 1e-10)
check("reflection at a complex point", close(gamma(z0) * gamma(1 - z0), pi / sin(pi * z0)))

# Rouche examples
r5 = polyroots([1, 0, 0, 0, 3, 1])
check("z^5+3z+1: one root in the unit disc, five in |z| < 3/2", sum(abs(r) < 1 for r in r5) == 1 and all(abs(r) < 1.5 for r in r5) and mpf(243) / 32 > mpf(11) / 2)
r4 = polyroots([1, 0, 0, -6, 3])
check("z^4-6z+3: one root in the unit disc, three in the annulus", sum(abs(r) < 1 for r in r4) == 1 and sum(1 < abs(r) < 2 for r in r4) == 3)
p = lambda z: z**5 + 3 * z + 1; dp = lambda z: 5 * z**4 + 3
check("argument principle counts 1 and 5", close(circ(lambda z: dp(z) / p(z), 0, 1), 1) and close(circ(lambda z: dp(z) / p(z), 0, mpf(3) / 2), 5))

# exercises
for n in (2, 3, 5):
    check(f"int dx/(1+x^{n}) = (pi/n)/sin(pi/n)", close(quad(lambda x: 1 / (1 + x**n), [0, 1, inf]), (pi / n) / sin(pi / n)))
check("Fresnel: 1/2 sqrt(pi/2)", close(sqrt(pi / 2) * mp.fresnelc(inf), sqrt(pi / 2) / 2))
aa = mpf('0.7')
check("sum 1/(n^2+a^2), n >= 1", close(nsum(lambda n: 1 / (n * n + aa * aa), [1, inf]), pi / (2 * aa) * coth(pi * aa) - 1 / (2 * aa * aa), mpf(10) ** -8))
check("alternating sum = pi/(a sinh(pi a))", close(nsum(lambda n: (-1) ** n / (n * n + aa * aa), [-inf, inf]), pi / (aa * sinh(pi * aa)), mpf(10) ** -8))

# rank of random matrices
def nrank(n, r, q):
    v = Fraction(1)
    for i in range(r): v *= Fraction((q**n - q**i) ** 2, q**r - q**i)
    return v
check("rank counts add up to q^(n^2)", all(sum(nrank(n, r, q) for r in range(n + 1)) == q ** (n * n) for q in (2, 3, 4) for n in (1, 2, 3, 4)))
import itertools
def rank2(rows, n):
    rows = list(rows); r = 0
    for c in range(n):
        piv = next((i for i in range(r, len(rows)) if rows[i] >> c & 1), None)
        if piv is None: continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(len(rows)):
            if i != r and rows[i] >> c & 1: rows[i] ^= rows[r]
        r += 1
    return r
cnt = [0] * 4
for rows in itertools.product(range(8), repeat=3): cnt[rank2(rows, 3)] += 1
check("3x3 matrices over F_2 by rank, brute force", cnt == [int(nrank(3, r, 2)) for r in range(4)])
def lim(k, q):
    q = mpf(q); num = mp.nprod(lambda j: 1 - q ** (-j), [k + 1, inf]); den = mp.fprod(1 - q ** (-j) for j in range(1, k + 1))
    return q ** (-k * k) * num / den
law = [lim(k, 2) for k in range(4)]
check("limit law for q=2: 0.2888, 0.5776, 0.1284, 0.0052", all(abs(v - mpf(c)) < 6e-5 for v, c in zip(law, ('0.2888', '0.5776', '0.1284', '0.0052'))))
check("limit law sums to 1 (q = 2, 3, 5)", all(close(nsum(lambda k: lim(int(k), q), [0, 12]), 1) for q in (2, 3, 5)))
x = mpf('0.37')
check("Durfee identity at x = 0.37", close(nsum(lambda k: x ** (k * k) / mp.fprod(1 - x**j for j in range(1, int(k) + 1)) ** 2, [0, 30]), 1 / mp.nprod(lambda j: 1 - x**j, [1, inf])))

# Dedekind sums
def saw(t):
    return Fraction(0) if t.denominator == 1 else t - (t.numerator // t.denominator) - Fraction(1, 2)
def s_def(h, k):
    return sum(saw(Fraction(r, k)) * saw(Fraction(h * r, k)) for r in range(k))
def s_fast(h, k):
    """Dedekind sum by reciprocity along Euclid's algorithm (float)."""
    h %= k; total = 0.0; sign = 1
    while h:
        total += sign * (-0.25 + (h / k + k / h + 1 / (h * k)) / 12)
        sign = -sign
        h, k = k % h, h
    return total
good = True
for k in range(1, 40):
    for h in range(1, 40):
        if gcd(h, k) == 1:
            good &= s_def(h, k) + s_def(k, h) == -Fraction(1, 4) + (Fraction(h, k) + Fraction(k, h) + Fraction(1, h * k)) / 12
            good &= (6 * k * s_def(h, k)).denominator == 1 and abs(s_def(h, k)) <= s_def(1, k)
            good &= abs(s_fast(h, k) - float(s_def(h, k))) < 1e-9
            if k > 1:
                cs = sum(cot(pi * j / k) * cot(pi * h * j / k) for j in range(1, k)) / (4 * k)
                good &= abs(cs - float(s_def(h, k))) < mpf(10) ** -15
    good &= s_def(1, k) == Fraction((k - 1) * (k - 2), 12 * k)
check("Dedekind sums: reciprocity, cotangent formula, s(1,k), integrality, |s| <= s(1,k), Euclid recursion", good)
def cf(h, k):
    out = []
    while h: out.append(k // h); h, k = k % h, h
    return out
good = all(abs(s_def(h, k)) <= Fraction(sum(cf(h, k)), 12) + len(cf(h, k)) for k in range(2, 60) for h in range(1, k) if gcd(h, k) == 1)
check("|s(h,k)| <= (a_1+...+a_n)/12 + n", good)
for k_, avg, l2, ratio in ((101, 0.951, 21.3, 0.045), (1009, 2.037, 47.8, 0.043), (10007, 3.691, 84.8, 0.044), (100003, 5.802, 132.5, 0.044)):
    m = sum(abs(s_fast(h, k_)) for h in range(1, k_)) / (k_ - 1)
    check(f"k={k_}: average |s| = {m:.3f} (printed {avg}), log^2 k = {log(k_)**2:.1f} (printed {l2}), ratio {m/log(k_)**2:.3f}", abs(m - avg) < 6e-4 and abs(log(k_) ** 2 - l2) < 0.06 and abs(m / log(k_) ** 2 - ratio) < 6e-4)

# zigzag numbers
c = taylor(lambda z: sec(z) + tan(z), 0, 10)
A10 = c[10] * factorial(10)
check("A_10 = 50521", abs(A10 - 50521) < mpf(10) ** -10)
approx = 2 * (2 / pi) ** 11
rel = (mpf(50521) / factorial(10) - approx) / approx
print("     A_10/10! =", mp.nstr(mpf(50521) / factorial(10), 6), " approx =", mp.nstr(approx, 6), " rel err =", mp.nstr(rel, 3), " -3^-11 =", mp.nstr(-mpf(3) ** -11, 3))
check("A_10/10! = 0.0139222, 2(2/pi)^11 = 0.0139223, relative error -5.6e-6 = -3^-11", abs(mpf(50521) / factorial(10) - mpf('0.0139222')) < 6e-8 and abs(approx - mpf('0.0139223')) < 6e-8 and abs(rel / mpf('-5.6e-6') - 1) < 0.02 and abs(-mpf(3) ** -11 / mpf('-5.6e-6') - 1) < 0.02)

# Jensen's formula on a polynomial times an exponential
zs = [mpc(0.5, 0.2), mpc(-0.3, 0.6), mpc(0.1, -0.8), mpc(1.4, 0.3)]
F = lambda z: exp(z / 2) * mp.fprod(z - a_ for a_ in zs)
R = mpf('1.1')
lhs = quad(lambda t: mlog(abs(F(R * exp(1j * t)))), mp.linspace(0, 2 * pi, 9)) / (2 * pi)
rhs = mlog(abs(F(0))) + sum(mlog(R / abs(a_)) for a_ in zs if abs(a_) < R)
check("Jensen's formula", close(lhs, rhs, mpf(10) ** -8))
aB = mpc(0.4, -0.5); B = lambda z: R * (z - aB) / (R * R - aB.conjugate() * z)
check("Blaschke factor has modulus 1 on the circle, |B(0)| = |a|/R", all(close(abs(B(R * exp(1j * t))), 1) for t in (0.3, 1.9, 4.4)) and close(abs(B(0)), abs(aB) / R))
check("|sin w / w| <= e^|w| at sample points", all(abs(sin(w) / w) <= exp(abs(w)) for w in (mpc(0.1, 0.1), mpc(3, -4), mpc(0, 9), mpc(-7, 0.5))))
check("zeros of sin(pi z)/(pi z) in |z| <= r: 2 floor(r) <= e pi r, e pi = 8.54", all(2 * floor(r) <= float(e * pi) * r for r in (0.5, 1, 2.5, 10, 100)) and abs(e * pi - mpf('8.54')) < 5e-3)

print("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED")
raise SystemExit(0 if ok else 1)
