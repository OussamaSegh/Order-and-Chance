#!/usr/bin/env python3
"""Numerical checks for Volume 5, Chapter 5 (The Gamma and Beta Functions)."""
from fractions import Fraction
from itertools import permutations
from math import comb, factorial, lcm
from mpmath import mp, mpf, gamma, beta, pi, sqrt, exp, log, quad, findroot, digamma, euler, sin, nsum, inf, fprod

mp.dps = 30
ok = True
def check(name, cond):
    global ok
    print(("ok   " if cond else "FAIL ") + name)
    ok = ok and bool(cond)
def close(a, b, tol=1e-12):
    return abs(a - b) <= tol * max(1, abs(b))

# Euler's integral, functional equation, Gamma(1/2)
check("Gamma(x) = int t^(x-1) e^-t", close(quad(lambda t: t**mpf('1.7') * exp(-t), [0, inf]), gamma(mpf('2.7'))))
check("Gamma(x+1) = x Gamma(x)", close(gamma(mpf('3.3')), mpf('2.3') * gamma(mpf('2.3'))))
check("Gamma(1/2) = sqrt(pi)", close(gamma(mpf(1) / 2), sqrt(pi)))
check("(1/2)! = sqrt(pi)/2 = 0.886", abs(gamma(mpf(3) / 2) - sqrt(pi) / 2) < 1e-25 and abs(gamma(mpf(3) / 2) - mpf('0.886')) < 5e-4)
check("log-convexity: Gamma(3/2)^2 <= Gamma(1) Gamma(2)", gamma(mpf(3) / 2) ** 2 <= 1)

# minimum of Gamma on ]0, oo[
x0 = findroot(digamma, 1.46)
print("     minimum at", mp.nstr(x0, 8), "value", mp.nstr(gamma(x0), 8))
check("minimum near 1.4616, value 0.8856", abs(x0 - mpf('1.4616')) < 1e-4 and abs(gamma(x0) - mpf('0.8856')) < 1e-4)

# Gauss and Weierstrass products
x = mpf('0.7'); n = 10**6
gauss = exp(x * log(n) + sum(log(mpf(k)) for k in range(1, n + 1)) - sum(log(x + k) for k in range(0, n + 1)))
check("Gauss product (n = 10^6)", abs(gauss - gamma(x)) < 1e-5)
w = exp(-euler * x) / x * exp(nsum(lambda k: x / k - log(1 + x / k), [1, inf]))
check("Weierstrass product", close(w, gamma(x), 1e-10))
check("Gamma'(1) = -gamma", close(mp.diff(gamma, 1), -euler, 1e-10))

# Stirling
for xx in (10, 100, 1000):
    r = gamma(mpf(xx)) / (sqrt(2 * pi) * mpf(xx) ** (xx - mpf(1) / 2) * exp(-xx))
    check(f"Stirling ratio at {xx} is 1 + 1/(12x) + O(1/x^2)", abs(r - 1 - mpf(1) / (12 * xx)) < mpf(1) / xx**2)
t, nn = mpf('0.4'), 50
ratio = gamma(nn + t) / (gamma(nn) * nn**t)
check("squeeze (n/(n+t))^(1-t) <= Gamma(n+t)/(Gamma(n) n^t) <= 1", (mpf(nn) / (nn + t)) ** (1 - t) <= ratio <= 1)
check("n ln(1+t/n) - t in [-1/(2n), 0]", -mpf(1) / (2 * nn) <= nn * log(1 + t / nn) - t <= 0)

# Beta, reflection, duplication, multiplication
a, b = mpf('1.3'), mpf('2.6')
check("B(a,b) = int = Gamma Gamma / Gamma", close(quad(lambda u: u**(a - 1) * (1 - u)**(b - 1), [0, 1]), gamma(a) * gamma(b) / gamma(a + b)))
check("reflection", close(gamma(mpf('0.3')) * gamma(mpf('0.7')), pi / sin(pi * mpf('0.3'))))
check("duplication", close(gamma(x) * gamma(x + mpf(1) / 2), 2 ** (1 - 2 * x) * sqrt(pi) * gamma(2 * x)))
for m in (3, 5):
    lhs = fprod(gamma(x + mpf(k) / m) for k in range(m))
    check(f"multiplication formula m={m}", close(lhs, (2 * pi) ** (mpf(m - 1) / 2) * mpf(m) ** (mpf(1) / 2 - m * x) * gamma(m * x)))
    check(f"product of sines m={m}", close(fprod(sin(k * pi / m) for k in range(1, m)), mpf(m) / 2 ** (m - 1)))
for k in (4, 7):
    W = quad(lambda th: sin(th) ** k, [0, pi / 2])
    check(f"Wallis W_{k} = B(1/2,(k+1)/2)/2", close(W, beta(mpf(1) / 2, mpf(k + 1) / 2) / 2))

# volume and surface of balls
V = lambda n: pi ** (mpf(n) / 2) / gamma(mpf(n) / 2 + 1)
check("V_2 = pi, V_3 = 4pi/3", close(V(2), pi) and close(V(3), 4 * pi / 3))
check("V_5 = 8 pi^2/15 = 5.264", close(V(5), 8 * pi**2 / 15) and abs(V(5) - mpf('5.264')) < 5e-4)
check("V_5 is the maximum", all(V(5) > V(k) for k in range(0, 60) if k != 5))
check("V_20 = 0.026", abs(V(20) - mpf('0.026')) < 5e-4)
check("V_n/V_{n-1} slicing", close(V(7) / V(6), quad(lambda t: (1 - t * t) ** 3, [-1, 1])))
check("V_n/V_{n-1} ~ sqrt(2 pi/n)", abs(V(400) / V(399) / sqrt(2 * pi / 400) - 1) < 1e-2)
S = lambda n: n * V(n)
print("     surface areas S_6, S_7, S_8:", [mp.nstr(S(k), 5) for k in (6, 7, 8)])

# lemniscate
varpi = 2 * quad(lambda r: 1 / sqrt(1 - r**4), [0, 1])
check("varpi = Gamma(1/4)^2/(2 sqrt(2 pi)) = 2.62206", close(varpi, gamma(mpf(1) / 4) ** 2 / (2 * sqrt(2 * pi)), 1e-10) and abs(varpi - mpf('2.62206')) < 5e-6)
check("varpi/2 = 1.31103", abs(varpi / 2 - mpf('1.31103')) < 5e-6)

# Nair
good = True
for nq in range(1, 200):
    d = lcm(*range(1, nq + 1))
    good &= all(d % (m * comb(nq, m)) == 0 for m in range(1, nq + 1))
    if nq >= 7:
        good &= d >= 2**nq
check("m C(n,m) | lcm(1..n) for n < 200, and lcm >= 2^n for n >= 7", good)
check("lcm(1..6) = 60 < 64 (so n >= 7 is needed)", lcm(*range(1, 7)) == 60)
check("int x^(m-1)(1-x)^(n-m) = 1/(m C(n,m))", all(Fraction(factorial(m - 1) * factorial(nq - m), factorial(nq)) == Fraction(1, m * comb(nq, m)) for nq in range(1, 30) for m in range(1, nq + 1)))

# n-cycles: number of (a, b) n-cycles with ab = c
def count(n):
    c = tuple(list(range(1, n)) + [0])
    def is_cycle(p):
        j, L = p[0], 1
        while j != 0:
            j, L = p[j], L + 1
        return L == n
    cyc = [p for p in permutations(range(n)) if is_cycle(p)]
    cs = set(cyc)
    tot = 0
    for a in cyc:
        ainv = [0] * n
        for i, v in enumerate(a):
            ainv[v] = i
        bb = tuple(ainv[c[i]] for i in range(n))   # a o b = c  =>  b = a^-1 o c
        tot += bb in cs
    return tot
for nq in (3, 4, 5, 6, 7):
    f = 2 * factorial(nq - 1) // (nq + 1) if nq % 2 else 0
    check(f"n-cycle factorisations n={nq}: brute {count(nq)} = formula {f}", count(nq) == f)
check("values 8 (n=5) and 180 (n=7)", 2 * 24 // 6 == 8 and 2 * 720 // 8 == 180)
check("sum (-1)^r / C(m,r) = (m+1)/(m+2) (1+(-1)^m)", all(sum(Fraction((-1)**r, comb(m, r)) for r in range(m + 1)) == Fraction(m + 1, m + 2) * (1 + (-1)**m) for m in range(0, 40)))

# Dalzell
def pmul(p, q):
    r = [0] * (len(p) + len(q) - 1)
    for i, u in enumerate(p):
        for j, v in enumerate(q):
            r[i + j] += u * v
    return r
A = [0, 0, 0, 0, 1, -4, 6, -4, 1]                 # x^4 (1-x)^4, ascending
Q = [4, 0, -4, 0, 5, -4, 1]                        # x^6-4x^5+5x^4-4x^2+4
prod = pmul(Q, [1, 0, 1]); prod[0] -= 4
check("x^4(1-x)^4 = Q (1+x^2) - 4", prod == A)
I = Fraction(1, 7) - Fraction(4, 6) + 1 - Fraction(4, 3) + 4
check("rational part is 22/7", I == Fraction(22, 7))
val = quad(lambda u: u**4 * (1 - u)**4 / (1 + u * u), [0, 1])
check("integral = 22/7 - pi, between 1/1260 and 1/630", close(val, mpf(22) / 7 - pi, 1e-15) and mpf(1) / 1260 < val < mpf(1) / 630)
check("4! 4!/9! = 1/630", Fraction(24 * 24, factorial(9)) == Fraction(1, 630))
for k in (1, 2, 3):
    v = quad(lambda u: (u**4 * (1 - u)**4) ** k / (1 + u * u), [0, 1])
    r = v - (-4) ** k * pi / 4
    approx = -4 * mpf(-4) ** (-k) * r
    check(f"Dalzell family n={k}: |pi - approx| < 4^(1-5n)", abs(pi - approx) < mpf(4) ** (1 - 5 * k))

# sophomore's dream
s1 = nsum(lambda k: mpf(k) ** (-k), [1, inf])
check("int x^-x = sum n^-n = 1.2912859970...", close(quad(lambda u: u**(-u), [0, 1]), s1, 1e-15) and abs(s1 - mpf('1.2912859970')) < 1e-10)
s2 = nsum(lambda k: (-1) ** (k + 1) * mpf(k) ** (-k), [1, inf])
check("int x^x = sum (-1)^(n+1) n^-n", close(quad(lambda u: u**u, [0, 1]), s2, 1e-15))
check("max of -x log x on [0,1] is 1/e", close(-(1 / mp.e) * log(1 / mp.e), 1 / mp.e))
for N, claim in ((9, mpf('1.1e-10')), (10, mpf('3.9e-12'))):
    bound = mpf(N + 1) ** (-N - 1) / (1 - mpf(1) / (N + 1))
    tail = s1 - sum(mpf(k) ** (-k) for k in range(1, N + 1))
    check(f"tail bound N={N}: {mp.nstr(bound, 3)} ~ {mp.nstr(claim, 2)}, true tail {mp.nstr(tail, 3)}", tail <= bound and abs(bound / claim - 1) < 0.05)
check("ten terms give ten decimals", abs(sum(mpf(k) ** (-k) for k in range(1, 11)) - s1) < 5e-11)

print("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED")
raise SystemExit(0 if ok else 1)
