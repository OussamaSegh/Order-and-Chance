#!/usr/bin/env python3
"""Numerical checks for Volume 5, Chapter 11 (Asymptotics)."""
from fractions import Fraction
from math import comb, factorial, isqrt
from mpmath import (mp, mpf, pi, e, exp, log, sqrt, gamma, loggamma, zeta, quad, inf, euler, harmonic, bernoulli,
                    bernpoly, floor, nsum, rf, cos, binomial)
from sympy import bernoulli as sbern
from sympy.functions.combinatorial.numbers import partition as npartitions

mp.dps = 40
ok = True
def check(name, cond):
    global ok
    print(("ok   " if cond else "FAIL ") + name)
    ok = ok and bool(cond)
def close(a, b, tol=mpf(10) ** -12):
    return abs(a - b) <= tol * max(1, abs(b))

# opening
n = 10**6
four = log(n) + euler + 1 / mpf(2 * n) - 1 / mpf(12 * n * n)
check("H_1000000 = 14.39272672286572363138 from four terms", abs(four - harmonic(n)) < mpf(10) ** -24 and abs(four - mpf('14.39272672286572363138')) < mpf(10) ** -20)
f10 = log(10) + euler + mpf(1) / 20 - mpf(1) / 1200
check("n = 10: 2.9289674 against 2.9289683", abs(f10 - 2.9289674) < 5e-8 and abs(harmonic(10) - 2.9289683) < 5e-8)
check("first omitted term 1/(120 n^4) ~ 1e-26 at n = 1e6", abs(1 / mpf(120 * n**4) - mpf(10) ** -26) < mpf(10) ** -26)

# Euler's series
f = lambda x: quad(lambda t: exp(-t) / (1 + x * t), [0, 1, 10, inf])
check("f(1) = 0.5963473623", abs(f(1) - mpf('0.5963473623')) < 1e-10)
x = mpf('0.1'); fx = f(x)
check("f(0.1) = 0.9156333394", abs(fx - mpf('0.9156333394')) < 1e-10)
part = lambda K: sum((-1) ** k * factorial(k) * x**k for k in range(K))
check("K=10: bound 3.6e-4, error 1.77e-4; K=20: error 8e-3", abs(factorial(10) * x**10 - 3.6e-4) < 5e-6 and abs(abs(fx - part(10)) - 1.77e-4) < 5e-7 and abs(abs(fx - part(20)) - 8e-3) < 1e-3)
check("remainder has the sign (-1)^K and is at most K! x^K", all(((fx - part(K)) * (-1) ** K > 0) and abs(fx - part(K)) <= factorial(K) * x**K for K in range(0, 25)))

# periodic Bernoulli functions
def Bbar(m, x): return bernpoly(m, x - floor(x))
for m in (2, 3, 4, 7):
    xx = mpf('0.37')
    ser = -gamma(m + 1) / (2j * pi) ** m * sum(exp(2j * pi * k * xx) / mpf(k) ** m for k in range(-4000, 4001) if k)
    check(f"Fourier series of B_{m}", abs(ser - Bbar(m, xx)) < 1e-5)
    check(f"|B_{m}(x)| <= 2 m! zeta(m)/(2 pi)^m", all(abs(Bbar(m, mpf(i) / 50)) <= 2 * gamma(m + 1) * zeta(m) / (2 * pi) ** m + mpf(10) ** -30 for i in range(51)))
check("sign of B_2k - Bbar_2k is (-1)^(k+1)", all((-1) ** (k + 1) * (bernoulli(2 * k) - Bbar(2 * k, mpf(i) / 20)) > 0 for k in (1, 2, 3, 4) for i in range(1, 20)))

# Euler-Maclaurin on a test function, order 4
g = lambda t: exp(-t / 3) * cos(t)
from mpmath import diff
a, b, m = 1, 6, 4
lhs = sum(g(k) for k in range(a + 1, b + 1))
rhs = quad(g, [a, b]) + sum((-1) ** j * (bernoulli(j) if j != 1 else mpf(-1) / 2) / factorial(j) * (diff(g, b, j - 1) - diff(g, a, j - 1)) for j in range(1, m + 1))
R = (-1) ** (m + 1) / mpf(factorial(m)) * quad(lambda t: Bbar(m, t) * diff(g, t, m), list(range(a, b + 1)))
check("Euler-Maclaurin formula, m = 4", close(lhs, rhs + R, mpf(10) ** -10))
check("coefficients 1/12, -1/720, 1/30240", [Fraction(int(sbern(2 * k).p), int(sbern(2 * k).q)) / factorial(2 * k) for k in (1, 2, 3)] == [Fraction(1, 12), Fraction(-1, 720), Fraction(1, 30240)])

# harmonic numbers
def Hexp(n, M): return log(n) + euler + 1 / mpf(2 * n) - sum(bernoulli(2 * k) / (2 * k * mpf(n) ** (2 * k)) for k in range(1, M))
for n in (3, 10, 50):
    for M in (1, 2, 3, 4, 5):
        E = harmonic(n) - Hexp(n, M); U = -bernoulli(2 * M) / (2 * M * mpf(n) ** (2 * M))
        check(f"H_{n}, M={M}: error between 0 and first omitted term", 0 < E / U < 1)
check("H_10 = 2.928968253968; error 4.1e-11 after -1/(252 n^6); next term 4.2e-11",
      abs(harmonic(10) - mpf('2.928968253968')) < 1e-12 and abs(abs(harmonic(10) - Hexp(10, 4)) - 4.1e-11) < 1e-12 and abs(1 / mpf(240 * 10**8) - 4.2e-11) < 1e-12)
check("terms 1/12n^2, 1/120n^4, 1/252n^6", [Fraction(int(sbern(2 * k).p), int(sbern(2 * k).q)) / (2 * k) for k in (1, 2, 3)] == [Fraction(1, 12), Fraction(-1, 120), Fraction(1, 252)])

# zeta by Euler-Maclaurin
def zem(s, N, M):
    return (sum(mpf(k) ** -s for k in range(1, N + 1)) + mpf(N) ** (1 - s) / (s - 1) - mpf(N) ** -s / 2
            + sum(bernoulli(2 * k) / factorial(2 * k) * rf(s, 2 * k - 1) * mpf(N) ** (1 - s - 2 * k) for k in range(1, M + 1))
            - rf(s, 2 * M) / factorial(2 * M) * quad(lambda t: Bbar(2 * M, t) * t ** (-s - 2 * M), list(range(N, N + 30)) + [inf]))
for s in (mpf(3), mpf('0.5'), mpf('-0.5'), mpf('-2.5')):
    check(f"prop:zetaem at s={s}", abs(zem(s, 3, 3) - zeta(s)) < 1e-7)
check("zeta(-n) from the finite combination, n <= 20", all(close(sum(mpf(k) ** n for k in range(1, 3)) + mpf(2) ** (1 + n) / (-n - 1) - mpf(2) ** n / 2
      + sum(bernoulli(2 * k) / factorial(2 * k) * rf(-n, 2 * k - 1) * mpf(2) ** (1 + n - 2 * k) for k in range(1, 12)), zeta(-n)) for n in range(0, 21)))
check("zeta(-1) = 1 - 1/2 - 1/2 - 1/12", Fraction(1) - Fraction(1, 2) - Fraction(1, 2) - Fraction(1, 12) == Fraction(-1, 12))
S = sum(Fraction(1, k**3) for k in range(1, 11))
approx = S + Fraction(1, 200) - Fraction(1, 2000) + Fraction(1, 4 * 10**4) - Fraction(1, 12 * 10**6) + Fraction(1, 12 * 10**8)
approx = mpf(approx.numerator) / approx.denominator
check("zeta(3): first sum 1.19753198567, formula 1.2020569031742, true 1.2020569031596, error 1.5e-11",
      abs(mpf(S.numerator) / S.denominator - mpf('1.19753198567')) < 1e-11 and abs(approx - mpf('1.2020569031742')) < 1e-13 and abs(zeta(3) - mpf('1.2020569031596')) < 1e-13 and abs(abs(approx - zeta(3)) - 1.5e-11) < 1e-12)
bound = 2 * zeta(7) / (2 * pi) ** 7 * factorial(8) / (2 * mpf(10) ** 9)
check("remainder bound 1.05e-10 <= 1.1e-10, seven times the error", abs(bound - 1.05e-10) < 1e-12 and 6.5 < bound / abs(approx - zeta(3)) < 7.5)
for nn in (50, 400):
    r1 = sum(sqrt(mpf(k)) for k in range(1, nn + 1)) - (mpf(2) / 3 * mpf(nn) ** 1.5 + sqrt(nn) / 2 + zeta(-0.5) + 1 / (24 * sqrt(mpf(nn))))
    r2 = sum(1 / sqrt(mpf(k)) for k in range(1, nn + 1)) - (2 * sqrt(mpf(nn)) + zeta(0.5) + 1 / (2 * sqrt(mpf(nn))) - 1 / (24 * mpf(nn) ** 1.5))
    check(f"sqrt sums at n={nn}: errors O(n^-5/2), O(n^-7/2)", abs(r1) * mpf(nn) ** 2.5 < 0.01 and abs(r2) * mpf(nn) ** 3.5 < 0.01)
check("zeta(-1/2) = -0.2078862, zeta(1/2) = -1.4603545, zeta(-1/2) = -zeta(3/2)/(4 pi)", abs(zeta(-0.5) + 0.2078862) < 1e-7 and abs(zeta(0.5) + 1.4603545) < 1e-7 and close(zeta(-0.5), -zeta(1.5) / (4 * pi)))

# Stirling's series
def stir(x, m): return (x - mpf(1) / 2) * log(x) - x + log(2 * pi) / 2 + sum(bernoulli(2 * k) / (2 * k * (2 * k - 1) * mpf(x) ** (2 * k - 1)) for k in range(1, m))
for x in (1, 2, 4, mpf('0.7')):
    for m in range(1, 9):
        rho = loggamma(x) - stir(x, m); T = bernoulli(2 * m) / (2 * m * (2 * m - 1) * mpf(x) ** (2 * m - 1))
        check(f"Stirling x={x}, m={m}: 0 < rho/T < 1", 0 < rho / T < 1)
check("coefficients 1/12, -1/360, 1/1260, -1/1680", [Fraction(int(sbern(2 * k).p), int(sbern(2 * k).q)) / (2 * k * (2 * k - 1)) for k in (1, 2, 3, 4)] == [Fraction(1, 12), Fraction(-1, 360), Fraction(1, 1260), Fraction(-1, 1680)])
best = {x: min(abs(loggamma(x) - stir(x, m)) for m in range(1, 40)) for x in (1, 2, 4)}
check("best errors about 1e-3.5, 1e-6.4, 1e-12", abs(log(best[1], 10) + 3.5) < 0.5 and abs(log(best[2], 10) + 6.4) < 0.5 and abs(log(best[4], 10) + 12) < 0.6)
sm = min(abs(bernoulli(2 * k) / (2 * k * (2 * k - 1) * mpf(4) ** (2 * k - 1))) for k in range(1, 40))
check("smallest term at x=4 about e^{-8 pi}/(2 pi) = 2e-12", 0.5 < sm / (exp(-8 * pi) / (pi * 2)) < 2 and abs(exp(-8 * pi) / (2 * pi) - 2e-12) < 3e-13)
check("n! between sqrt(2 pi n)(n/e)^n and that times e^(1/12n)", all(sqrt(2 * pi * k) * (k / e) ** k < factorial(k) < sqrt(2 * pi * k) * (k / e) ** k * exp(mpf(1) / (12 * k)) for k in range(1, 30)))

# Laplace, saddle, transfer
check("n! by Laplace: ratio -> 1", abs(factorial(200) / (sqrt(2 * pi * 200) * (200 / e) ** 200) - 1) < 1e-3)
check("binom(2n,n) = 4^n/sqrt(pi n) (1 - 1/8n + O(n^-2))", abs(comb(400, 200) / (mpf(4) ** 200 / sqrt(pi * 200)) - (1 - mpf(1) / 1600)) < 1e-5)
al = mpf('0.3')
an = lambda al, k: gamma(k + al) / (gamma(al) * factorial(k))
check("a_n(alpha) expansion", abs(an(al, 500) / (mpf(500) ** (al - 1) / gamma(al)) - (1 + al * (al - 1) / 1000)) < 1e-5)
# 2-regular graphs via the EGF
N = 31
c = [Fraction(0)] * N
for k in range(3, N): c[k] = Fraction(1, 2 * k)
egf = [Fraction(1)] + [Fraction(0)] * (N - 1)
for nn in range(1, N):  # F' = C' F
    egf[nn] = sum(k * c[k] * egf[nn - k] for k in range(1, nn + 1)) / nn
gn = [egf[k] * factorial(k) for k in range(N)]
check("g_3..g_7 = 1, 3, 12, 70, 465", gn[3:8] == [1, 3, 12, 70, 465])
ratio = exp(mpf(-3) / 4) / sqrt(pi * 30) / (mpf(egf[30].numerator) / egf[30].denominator)
check("2-regular graphs, n = 30: approximation 2% too large", abs(ratio - 1.02) < 0.006)
der = sum(Fraction((-1) ** k, factorial(k)) for k in range(0, 11))
check("derangements: |D_n/n! - 1/e| < 1/(n+1)!", abs(mpf(der.numerator) / der.denominator - 1 / e) < 1 / mpf(factorial(11)))

# exercises
S = sum(mpf(k) ** k for k in range(1, 101))
check("sum k^k: O-term/n^(n-2) about 0.32 at n=100", abs((S - mpf(100) ** 100 * (1 + 1 / (e * 100))) / mpf(100) ** 98 - 0.32) < 0.01)
for nn in (10, 100, 1000):
    Cn = 2 * (nn + 1) * harmonic(nn) - 4 * nn
    ex = 2 * nn * log(nn) + (2 * euler - 4) * nn + 2 * log(nn) + 2 * euler + 1 + mpf(5) / (6 * nn)
    check(f"quicksort expansion at n={nn}: error ~ -1/(6 n^2)", abs((Cn - ex) * nn**2 + mpf(1) / 6) < 0.3 / nn + 1e-3)
check("partitions: ln p(n) <= pi sqrt(2n/3), p(n) >= 2^(floor sqrt n - 1)", all(log(int(npartitions(k))) <= pi * sqrt(mpf(2 * k) / 3) and npartitions(k) >= 2 ** (isqrt(k) - 1) for k in range(1, 300)))
rat = lambda k: log(int(npartitions(k))) / (pi * sqrt(mpf(2 * k) / 3))
check("ratio 0.74, 0.89, 0.92 at n = 100, 1000, 2000", abs(rat(100) - 0.74) < 0.006 and abs(rat(1000) - 0.89) < 0.006 and abs(rat(2000) - 0.92) < 0.006)
Mz = [1, 1]
for k in range(2, 201): Mz.append(((2 * k + 1) * Mz[k - 1] + (3 * k - 3) * Mz[k - 2]) // (k + 2))
check("Motzkin 1,1,2,4,9,21; ratio 0.988 at n=200", Mz[:6] == [1, 1, 2, 4, 9, 21] and abs(Mz[200] / (mpf(3) ** 201.5 / (2 * sqrt(pi) * mpf(200) ** 1.5)) - 0.988) < 0.002)
check("Gamma(-1/2) = -2 sqrt(pi)", close(gamma(-0.5), -2 * sqrt(pi)))
g10 = 12005168
r10 = mpf(g10) * factorial(10) / 2**45
check("graphs on 10 vertices: ratio 1.24, two-term 1.18", abs(r10 - 1.24) < 0.005 and abs(1 + mpf(90) / 512 - 1.18) < 0.005)
# odd cycles: o_n via EGF (1+x)/sqrt(1-x^2)
def o(nn):
    m = nn // 2
    return factorial(nn) * comb(2 * m, m) // 4**m
dd = lambda m: 1 if m <= 0 else m * dd(m - 2)
check("o_n = (1.3.5...(n-1))^2 for even n; o_n = n o_(n-1) for odd n", all(o(2 * m) == dd(2 * m - 1) ** 2 and o(2 * m + 1) == (2 * m + 1) * o(2 * m) for m in range(1, 12)))
from itertools import permutations
def allodd(p):
    seen = set()
    for i in range(len(p)):
        if i not in seen:
            L, j = 0, i
            while j not in seen: seen.add(j); j = p[j]; L += 1
            if L % 2 == 0: return False
    return True
check("o_n by enumeration, n <= 7", all(sum(allodd(p) for p in permutations(range(k))) == o(k) for k in range(1, 8)))
lhs = sum(mpf(k) ** 100 for k in range(1, 101)) / mpf(100) ** 100
check("power sum n=100: 1.57211 against 1.57202", abs(lhs - 1.57211) < 5e-6 and abs(e / (e - 1) - e * (e + 1) / (2 * (e - 1) ** 3) / 100 - 1.57202) < 5e-6)
check("sum j^2 e^-j = e(e+1)/(e-1)^3", close(nsum(lambda j: j * j * exp(-j), [0, inf]), e * (e + 1) / (e - 1) ** 3))
ET = lambda nn: quad(lambda t: exp(-t) * (1 + t / nn + t * t / (2 * mpf(nn) ** 2)) ** nn, [0, 50, 100, 200, 400, 1000, inf])
check("birthday triple: exact 88.74, asymptotic 82.9; pairs 23.9 against 24.62",
      abs(ET(365) - 88.74) < 0.005 and abs(gamma(mpf(4) / 3) * (6 * 365**2) ** (mpf(1) / 3) - 82.9) < 0.05 and abs(sqrt(pi * 365 / 2) - 23.9) < 0.05
      and abs(quad(lambda t: exp(-t) * (1 + t / 365) ** 365, [0, 50, 200, 1000, inf]) - 24.62) < 0.005)
check("int psi = 3; int e^{-y^3} = Gamma(4/3)", close(quad(lambda x: exp(-x) * (1 + x + x * x / 2), [0, inf]), 3) and close(quad(lambda y: exp(-y**3), [0, inf]), gamma(mpf(4) / 3)))
check("Wallis W_n ~ sqrt(pi/2n)", abs(quad(lambda t: cos(t) ** 400, [0, 0.3, pi / 2]) / sqrt(pi / 800) - 1) < 1e-3)

print("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED")
raise SystemExit(0 if ok else 1)
