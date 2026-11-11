#!/usr/bin/env python3
"""Numerical checks for Volume 5, Chapter 13 (The Arithmetic-Geometric Mean) and its closing problems."""
from fractions import Fraction
from math import comb, factorial, gcd
from itertools import product
from mpmath import (mp, mpf, pi, e, exp, log, sqrt, gamma, zeta, quad, inf, euler, agm, ellipk, ellipe, sin, cos, tan,
                    nsum, harmonic, binomial, diff, asinh, floor)

mp.dps = 60
ok = True
def check(name, cond):
    global ok
    print(("ok   " if cond else "FAIL ") + name)
    ok = ok and bool(cond)
def close(a, b, tol=mpf(10) ** -25):
    return abs(a - b) <= tol * max(1, abs(b))
def steps(a, b, n):
    out = [(mpf(a), mpf(b))]
    for _ in range(n):
        a, b = out[-1]; out.append(((a + b) / 2, sqrt(a * b)))
    return out
I = lambda a, b: quad(lambda t: 1 / sqrt(a * a * cos(t) ** 2 + b * b * sin(t) ** 2), [0, pi / 4, pi / 2])
J = lambda a, b: quad(lambda t: sqrt(a * a * cos(t) ** 2 + b * b * sin(t) ** 2), [0, pi / 4, pi / 2])

# the iteration
st = steps(1, sqrt(2), 6)
d = [abs(a - b) for a, b in st]
check("think box: 1.2071, 1.1892; M(1, sqrt 2) = 1.19814023473559", abs(st[1][0] - 1.2071) < 5e-5 and abs(st[1][1] - 1.1892) < 5e-5 and abs(st[4][0] - mpf('1.19814023473559')) < 1e-14)
check("differences 0.41, 0.018, 3.3e-5, 1.2e-10, 1.4e-21, 2e-43", all(abs(x / y - 1) < 0.05 for x, y in zip(d, [0.41, 0.018, 3.3e-5, 1.2e-10, 1.4e-21, 2.1e-43])))
st = steps(1, mpf('0.01'), 6); d = [a - b for a, b in st]
check("figure: 0.99, 0.405, 0.078, 2.9e-3, 4.0e-6, 7.5e-12; M(1,0.01) = 0.2621668872", all(abs(x / y - 1) < 0.02 for x, y in zip(d, [0.99, 0.405, 0.078, 2.9e-3, 4.0e-6, 7.5e-12])) and abs(agm(1, mpf('0.01')) - mpf('0.2621668872')) < 1e-10)
a, b = mpf(3), mpf('0.7'); a1, b1 = (a + b) / 2, sqrt(a * b)
check("a1 - b1 <= (a-b)^2/(8b); c1 = c0^2/(4 a1)", a1 - b1 <= (a - b) ** 2 / (8 * b) and close(sqrt(a1**2 - b1**2), (a * a - b * b) / (4 * a1)))

# Gauss, Landen, lemniscate
check("I(a,b) = pi/(2 M(a,b)); I(a1,b1) = I(a,b)", close(I(a, b), pi / (2 * agm(a, b))) and close(I(a1, b1), I(a, b)))
k = mpf('0.6'); kp = sqrt(1 - k * k); k1 = (1 - kp) / (1 + kp)
check("K(k) = pi/(2 M(1,k')) ; Landen K(k) = (1+k1) K(k1)", close(ellipk(k * k), pi / (2 * agm(1, kp))) and close(ellipk(k * k), (1 + k1) * ellipk(k1 * k1)))
varpi = 2 * quad(lambda r: 1 / sqrt(1 - r**4), [0, 0.5, 1])
check("varpi = 2.62205755429211981 = pi/M(1, sqrt 2)", abs(varpi - mpf('2.62205755429211981')) < 1e-16 and close(varpi, pi / agm(1, sqrt(2)), mpf(10) ** -20))
check("Gamma(1/4) = (2 pi)^(3/4)/sqrt(M(1,sqrt2)) = 3.62560990822; a_5 = 1.19814023473559220744", close(gamma(0.25), (2 * pi) ** 0.75 / sqrt(agm(1, sqrt(2)))) and abs(gamma(0.25) - mpf('3.62560990822')) < 1e-11
      and abs(steps(1, sqrt(2), 5)[5][0] - mpf('1.19814023473559220744')) < 1e-20)

# perimeter
check("lem:jderiv(a): J = a^2 b^2 int R^(-3/2)", close(J(a, b), a * a * b * b * quad(lambda t: (a * a * cos(t) ** 2 + b * b * sin(t) ** 2) ** -1.5, [0, pi / 4, pi / 2])))
dI = diff(lambda x: I(x, b), a)
check("lem:jderiv(b): J = a^2 I + a(a^2-b^2) dI/da", close(J(a, b), a * a * I(a, b) + a * (a * a - b * b) * dI, mpf(10) ** -15))
check("prop:jstep: 2J(a1,b1) - J(a,b) = ab I(a,b)", close(2 * J(a1, b1) - J(a, b), a * b * I(a, b)))
def perimeter(a, b, n=8):
    st = steps(a, b, n); s = a * a - sum(2 ** (i - 1) * (x * x - y * y) for i, (x, y) in enumerate(st))
    return 2 * pi / st[-1][0] * s
check("thm:perimeter; L(2,1) = 9.68844822054767619842 after five steps", close(perimeter(a, b), 4 * J(a, b)) and abs(perimeter(2, 1, 5) - mpf('9.68844822054767619842')) < 1e-19)
ecc = mpf('0.0167')
check("Earth: 0.99993027", abs(perimeter(1, sqrt(1 - ecc**2)) / (2 * pi) - 0.99993027) < 5e-9)
ram = lambda a, b: pi * (3 * (a + b) - sqrt((3 * a + b) * (a + 3 * b)))
worst = max(abs(ram(1, mpf(i) / 200) / perimeter(1, mpf(i) / 200, 12) - 1) for i in range(1, 201))
check("Ramanujan: 3e-6 at a = 2b, at most 0.5% everywhere", abs(abs(ram(2, 1) / perimeter(2, 1) - 1) - 3e-6) < 1e-6 and worst < 0.005 and abs(1 - pi * (3 - sqrt(3)) / 4) < 0.005)
check("Euler's bounds", all(pi * (1 + x) <= perimeter(1, x, 12) <= pi * sqrt(2 * (1 + x * x)) for x in (mpf('0.1'), mpf('0.5'), mpf('0.9'))))

# Legendre, Brent-Salamin
K = lambda k: ellipk(k * k); E = lambda k: ellipe(k * k)
check("dE/dk, dK/dk", close(diff(E, k), (E(k) - K(k)) / k, mpf(10) ** -15) and close(diff(K, k), (E(k) - kp**2 * K(k)) / (k * kp**2), mpf(10) ** -15))
check("Legendre's relation", all(close(E(x) * K(sqrt(1 - x * x)) + E(sqrt(1 - x * x)) * K(x) - K(x) * K(sqrt(1 - x * x)), pi / 2) for x in (mpf('0.1'), mpf('0.6'), mpf('0.95'))))
x = mpf('0.01')
check("bounds in the proof: K-E <= pi k^2/(2k'), K' <= pi/2 arsinh(1/(sqrt2 k)) + sqrt2 pi/4", K(x) - E(x) <= pi * x * x / (2 * sqrt(1 - x * x)) and K(sqrt(1 - x * x)) <= pi / 2 * asinh(1 / (sqrt(2) * x)) + sqrt(2) * pi / 4)
mp.dps = 800
a, b, s, errs, first = mpf(1), 1 / sqrt(mpf(2)), mpf(0), [], None
for n in range(1, 9):
    c = (a - b) / 2; a, b = (a + b) / 2, sqrt(a * b); s += 2 ** (n + 1) * c * c
    pin = 4 * ((a + b) / 2) ** 2 / (1 - s); errs.append(abs(pin - pi))
    if n == 1: first = pin
check("Brent-Salamin: pi_1 = 3.1405...; errors below 1e-8, 1e-18, 1e-40, 1e-83, 1e-170, 1e-344, 1e-693",
      3.1405 <= first < 3.1406 and all(er < mpf(10) ** -t for er, t in zip(errs[1:], (8, 18, 40, 83, 170, 344, 693))))
check("formula: pi = 4 M^2/(1 - sum 2^(n+1) c_n^2)", abs(4 * a * a / (1 - s) - pi) < mpf(10) ** -340)
mp.dps = 1500
st = steps(1, 1 / sqrt(mpf(2)), 10)
check("ex:agmsteps: e_0 = 0.0518, difference after 10 steps about 1e-1396", abs((1 - 1 / sqrt(mpf(2))) / (8 / sqrt(mpf(2))) - 0.0518) < 5e-5 and abs(log(st[10][0] - st[10][1], 10) + 1396) < 2)
mp.dps = 60
check("Machin and Chudnovsky", close(4 * (4 * mp.atan(mpf(1) / 5) - mp.atan(mpf(1) / 239)), pi)
      and close(1 / (12 * nsum(lambda n: (-1) ** n * mp.factorial(6 * n) * (13591409 + 545140134 * n) / (mp.factorial(3 * n) * mp.factorial(n) ** 3 * mpf(640320) ** (3 * n + 1.5)), [0, 6])), pi))

# exercises of the chapter
M = agm(1, cos(pi / 4))
check("pendulum: M(1, cos 45) = 0.8472, 18.0% longer; 0.19% at 10 degrees; almost 4 times at 179", abs(M - 0.8472) < 5e-5 and abs(1 / M - 1.180) < 5e-4 and abs(1 / agm(1, cos(pi / 36)) - 1.0019) < 5e-5 and 3.5 < 1 / agm(1, cos(pi * 179 / 360)) < 4)
err = lambda x: abs(pi / (2 * agm(1, x)) - log(4 / x))
check("agm log: errors 6.8e-3, 1.25e-4, 3.6e-12", abs(err(mpf('0.1')) / 6.8e-3 - 1) < 0.02 and abs(err(mpf('0.01')) / 1.25e-4 - 1) < 0.02 and abs(err(mpf(10) ** -6) / 3.6e-12 - 1) < 0.03)

# closing problems (a selection of the printed numbers)
qn = lambda k, n: sum(cos(2 * pi * j / k) ** n for j in range(k)) / k
check("cycle walk closed forms", all(close(qn(3, n), (1 + 2 * mpf(-0.5) ** n) / 3) and close(qn(6, n), (1 + 2 * mpf(2) ** -n + 2 * mpf(-0.5) ** n + (-1) ** n) / 6) for n in range(1, 9)))
import numpy as np
tot = 0
for bits in product((-1, 1), repeat=9):
    A = np.array(bits).reshape(3, 3); tot += round(np.linalg.det(A)) ** 2
check("E det^2 = n! for n = 3", tot == 6 * 2**9)
def paley(p):
    chi = lambda x: 0 if x % p == 0 else (1 if pow(x, (p - 1) // 2, p) == 1 else -1)
    Q = np.array([[chi(b - a) for b in range(p)] for a in range(p)])
    S = np.zeros((p + 1, p + 1), dtype=int); S[0, 1:] = 1; S[1:, 0] = -1; S[1:, 1:] = Q
    H = np.eye(p + 1, dtype=int) + S
    return (H @ H.T == (p + 1) * np.eye(p + 1, dtype=int)).all() and (abs(H) == 1).all()
check("Paley matrices for p = 3, 7, 11, 19, 23", all(paley(p) for p in (3, 7, 11, 19, 23)))
orders = {4, 8, 12, 20, 24, 32, 44, 48, 60} | {1, 2, 4, 8, 16, 32, 64} | {24, 40, 48, 64}
check("Hadamard orders up to 64: all multiples of 4 except 28, 36, 52, 56", {n for n in range(4, 65, 4)} - orders == {28, 36, 52, 56})
check("Gauss measure: log2(4/3) = 0.415; law sums to 1", abs(log(mpf(4) / 3, 2) - 0.415) < 5e-4)
def vp(n, p):
    v = 0
    while n % p == 0: n //= p; v += 1
    return v
def carries(m, n, p):
    c = t = 0
    while m or n:
        c = 1 if m % p + n % p + c >= p else 0; t += c; m //= p; n //= p
    return t
check("Kummer's theorem", all(vp(comb(m + n, m), p) == carries(m, n, p) for p in (2, 3, 5) for m in range(40) for n in range(40)))
sdig = lambda n: bin(n).count("1"); Bblk = lambda n: bin(n)[2:].count("10")
check("Pascal mod 4", all(sum(1 for k in range(n + 1) if comb(n, k) % 4 == 2) == Bblk(n) * 2 ** (sdig(n) - 1) for n in range(1, 200)))
def digs(n, p):
    out = []
    while n: out.append(n % p); n //= p
    return out
check("central binomial mod p", all((comb(2 * n, n) - np.prod([comb(2 * d, d) for d in digs(n, p)], dtype=object)) % p == 0 for p in (3, 5, 7) for n in range(1, 300)))
st_ = [0, 1]
for n in range(2, 5000): st_.append(st_[n // 2] if n % 2 == 0 else st_[n // 2] + st_[n // 2 + 1])
fib = [0, 1]
for _ in range(30): fib.append(fib[-1] + fib[-2])
check("Stern: s(n+1) counts odd binom(n-k,k); max is F_(k+2) at (2^(k+2)-(-1)^k)/3", all(st_[n + 1] == sum(comb(n - k, k) % 2 for k in range(n // 2 + 1)) for n in range(300))
      and all(max(st_[2**k:2 ** (k + 1) + 1]) == fib[k + 2] == st_[(2 ** (k + 2) - (-1) ** k) // 3] for k in range(1, 11)))
check("sum 1/(n C(2n,n)) = pi/(3 sqrt 3) = 0.6046; sum 1/C(2n,n) = 4/3 + 2 pi sqrt3/27 = 1.7364",
      close(nsum(lambda n: 1 / (n * binomial(2 * n, n)), [1, inf]), pi / (3 * sqrt(3))) and abs(pi / (3 * sqrt(3)) - 0.6046) < 5e-5 and close(nsum(lambda n: 1 / binomial(2 * n, n), [0, inf]), mpf(4) / 3 + 2 * pi * sqrt(3) / 27) and abs(mpf(4) / 3 + 2 * pi * sqrt(3) / 27 - 1.7364) < 5e-5)
cn = lambda n: binomial(2 * n, n) / mpf(4) ** n
check("sum c_n/(2n+1) = pi/2 (partial), sum c_n/n = 2 log 2 (partial), sum c_n^2/(n+1) -> 4/pi", abs(4 * 4000 * cn(4000) ** 2 - 4 / pi) < 1e-4 and close(sum(cn(n) ** 2 / (n + 1) for n in range(50)), 4 * 50 * cn(50) ** 2))
check("Ramanujan series (42n+5)", close(nsum(lambda n: binomial(2 * n, n) ** 3 * (42 * n + 5) / mpf(2) ** (12 * n + 4), [0, inf]), 1 / pi))
check("Catalan moments", all(close(quad(lambda x: x ** (2 * n) * sqrt(4 - x * x), [-2, 0, 2]) / (2 * pi), mpf(comb(2 * n, n)) / (n + 1), mpf(10) ** -12) for n in range(5)))
p = 43
Qs = {x * x % p for x in range(1, p)}
T = sum(1 for x in range(p) for dd in range(p) if x in Qs and (x + dd) % p in Qs and (x + 2 * dd) % p in Qs)
check("progressions in the squares mod 43", abs(T - (p - 1) ** 3 / (8 * p)) <= (p**0.5 + 1) * (p - 1) / 4)
def mult(n):
    F = np.array([[np.exp(-2j * np.pi * j * k / n) for k in range(n)] for j in range(n)]) / np.sqrt(n)
    ev = np.linalg.eigvals(F); return tuple(int(sum(abs(ev - z) < 1e-6)) for z in (1, -1, -1j, 1j))
tab = {0: lambda m: (m + 1, m, m, m - 1), 1: lambda m: (m + 1, m, m, m), 2: lambda m: (m + 1, m + 1, m, m), 3: lambda m: (m + 1, m + 1, m + 1, m)}
check("DFT eigenvalue multiplicities, n = 4..15", all(mult(n) == tab[n % 4](n // 4) for n in range(4, 16)))
check("2 + 2 pi + 4/pi = 9.55", 0 <= 2 + 2 * pi + 4 / pi - 9.55 < 0.01)
def tinv(n):
    t = [1, 1]
    for k in range(2, n + 1): t.append(t[-1] + (k - 1) * t[-2])
    return t[n]
n = 1000; r = (sqrt(mpf(4 * n + 1)) - 1) / 2; bb = r + 2 * r * r
approx_c = mp.factorial(n) * exp(r + r * r / 2) / (r**n * sqrt(2 * pi * bb)); approx_d = mpf(n) ** (mpf(n) / 2) * exp(-mpf(n) / 2 + sqrt(n) - 0.25) / sqrt(2)
check("involutions n = 1000: ratios 0.99983 and 1.0091", abs(tinv(n) / approx_c - 0.99983) < 2e-5 and abs(tinv(n) / approx_d - 1.0091) < 2e-4)
N = 301
dc = [Fraction(1)] + [Fraction(0)] * (N - 1)
for k in range(1, N):
    for j in range(N - 1, k - 1, -1): dc[j] += dc[j - k] / k
check("distinct cycles: d_1..d_5 = 1, 1/2, 5/6, 7/12, 37/60; d_300 = 0.5633; e^-gamma = 0.5614", dc[1:6] == [1, Fraction(1, 2), Fraction(5, 6), Fraction(7, 12), Fraction(37, 60)] and abs(float(dc[300]) - 0.5633) < 5e-5 and abs(exp(-euler) - 0.5614) < 6e-5)
def QR(n):
    Q = t = mpf(1)
    for k in range(1, n): t *= mpf(n - k) / n; Q += t
    R = nsum(lambda j: mp.rf(n + 1, j) ** -1 * mpf(n) ** j, [0, inf]); return Q, R
Q, Rr = QR(400)
check("Ramanujan: Q = sqrt(pi n/2) - 1/3 + .., R = .. + 1/3; n(theta - 1/3) -> 4/135", abs(Q - sqrt(pi * 200) + mpf(1) / 3) < 0.05 and abs(Rr - sqrt(pi * 200) - mpf(1) / 3) < 0.05 and abs(400 * ((Rr - Q) / 2 - mpf(1) / 3) - mpf(4) / 135) < 2e-3 and abs(mpf(4) / 135 - 0.029630) < 1e-6)
Cn = lambda n: sum(mp.ff(n, k) / (k * mpf(n) ** k) for k in range(1, n + 1))
check("random maps: C_100 = 2.979 against 2.938; excess about 0.42/sqrt n", abs(Cn(100) - 2.979) < 5e-4 and abs((log(200) + euler) / 2 - 2.938) < 5e-4 and abs((Cn(400) - (log(800) + euler) / 2) * 20 - 0.42) < 0.03)
y = mpf(1); Delta = mpf(0); nn = 200000
mp.dps = 20
for k in range(nn): Delta += 1 / y - mpf(1) / (2 * k + 1); y = y + 2 + 1 / y
C = y - 2 * nn - log(nn) / 2
check("x + 1/x: C = 1.72314, Delta = -0.2586", abs(C - 1.72314) < 2e-5 and abs(Delta + 0.2586) < 1e-4 and abs(1 + log(2) + euler / 2 + Delta - C) < 1e-4)
mp.dps = 40
zp = diff(zeta, -1); lnA = mpf(1) / 12 - zp; lnH = sum(k * log(k) for k in range(1, 11))
f10 = (50 + 5 + mpf(1) / 12) * log(10) - 25 + lnA
check("Glaisher: zeta'(-1) = -0.1654211, A = 1.2824271291, ln H(10) = 102.0828, error 1.39e-5", abs(zp + 0.1654211) < 5e-8 and abs(exp(lnA) - mpf('1.2824271291')) < 1e-10 and abs(lnH - 102.0828) < 5e-5 and abs(lnH - f10 - 1.39e-5) < 1e-7)
ER = (2 * 50 + 1) * binomial(100, 50) / mpf(4) ** 50 - 1
check("Banach: E[R] = 7.04 against 6.98 for N = 50", abs(ER - 7.04) < 5e-3 and abs(2 * sqrt(50 / pi) - 1 - 6.98) < 5e-3)
from sympy import mobius, primerange
P2 = sum(int(mobius(k)) * log(zeta(2 * k)) / k for k in range(1, 21))
check("prime zeta: P(2) = 0.452247420041; 1/(x log x) = 6.2e-9 at 1e7; difference 5.86e-9", abs(P2 - mpf('0.452247420041')) < 1e-12 and abs(1 / (mpf(10) ** 7 * log(mpf(10) ** 7)) - 6.2e-9) < 5e-11 and abs(mpf('0.452247420041') - mpf('0.452247414181') - 5.86e-9) < 1e-12)
part = sum(mpf(q) ** -2 for q in primerange(2, 10**6)); tail = P2 - part
check("the tail beyond 1e6 is below 1/(x-1) and near 1/(x log x)", 0 < tail < 1 / mpf(10**6 - 1) and abs(tail * 10**6 * log(mpf(10) ** 6) - 1) < 0.1)
check("e^gamma = 1.78107, 2 e^-gamma = 1.1229, exp(-1/20 + 1/1200) = 0.952022", abs(exp(euler) - 1.78107) < 5e-6 and abs(2 * exp(-euler) - 1.1229) < 5e-5 and abs(exp(-mpf(1) / 20 + mpf(1) / 1200) - 0.952022) < 1e-6)
q = 5
def Nk(k): return sum(int(mobius(k // dd)) * q**dd for dd in range(1, k + 1) if k % dd == 0) // k
En = mpf(1)
for k_ in range(1, 11): En *= (1 - mpf(q) ** -k_) ** Nk(k_)
check("polynomial Mertens: n e^gamma E_n = 0.952015 for q = 5, n = 10", abs(10 * exp(euler) * En - 0.952015) < 1e-6)
# Dickman: integral of rho = e^gamma (numerical solution of the delay equation)
h = mpf(1) / 2000; rho = [mpf(1)] * 2001
for i in range(2001, 2000 * 12 + 1):
    u = i * h; rho.append(rho[-1] - h * (rho[i - 2001] / (u - h) + rho[i - 2000] / u) / 2)
integral = h * (sum(rho) - (rho[0] + rho[-1]) / 2)
check("Dickman: integral of rho = e^gamma; rho(2) = 1 - log 2", abs(integral - exp(euler)) < 1e-3 and abs(rho[4000] - (1 - log(2))) < 1e-3)

print("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED")
raise SystemExit(0 if ok else 1)
