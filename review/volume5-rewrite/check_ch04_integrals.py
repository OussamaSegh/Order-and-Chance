#!/usr/bin/env python3
"""Numeric checks for Volume 5, Chapter 4 (Integration Techniques, BBP, Borwein integrals).

Run: python3 review/volume5-rewrite/check_ch04_integrals.py
"""
from fractions import Fraction as Fr
from math import factorial
import mpmath as mp
import sympy as sp

mp.mp.dps = 30
ok = True


def check(name, cond):
    global ok
    print(("ok   " if cond else "FAIL ") + name)
    ok = ok and bool(cond)


pi, inf, q = mp.pi, mp.inf, mp.quad
near = lambda a, b, d=20: abs(a - b) < mp.mpf(10) ** -d
osc = lambda f, w: mp.quadosc(f, [0, inf], omega=w)

check("int_0^1 (x-1)/ln x = ln 2", near(q(lambda x: (x - 1) / mp.log(x), [0, 1]), mp.log(2), 15))
check("F(t) = ln(1+t) at t = 2.5", near(q(lambda x: (x**2.5 - 1) / mp.log(x), [0, 1]), mp.log(3.5), 15))
check("Gaussian integral sqrt(pi)/2", near(q(lambda x: mp.exp(-x * x), [0, inf]), mp.sqrt(pi) / 2))
t = mp.mpf("1.3")
check("F + G = pi/4 in the Gaussian example", near(q(lambda x: mp.exp(-x * x), [0, t]) ** 2 + q(lambda y: mp.exp(-t * t * (1 + y * y)) / (1 + y * y), [0, 1]), pi / 4))
a, b = mp.mpf(2), mp.mpf(5)
check("Frullani with e^-x", near(q(lambda x: (mp.exp(-a * x) - mp.exp(-b * x)) / x, [0, 1, inf]), mp.log(b / a), 15))
check("Frullani with arctan", near(q(lambda x: (mp.atan(b * x) - mp.atan(a * x)) / x, [0, 1, 100, inf]), pi / 2 * mp.log(b / a), 10))
check("int ln sin = -pi/2 ln 2", near(q(lambda x: mp.log(mp.sin(x)), [0, pi / 2]), -pi / 2 * mp.log(2), 15))
check("Dirichlet integral pi/2", near(osc(lambda x: mp.sin(x) / x, 1), pi / 2, 15))
check("F(t) = pi/2 - arctan t at t = 0.7", near(q(lambda x: mp.exp(-0.7 * x) * mp.sin(x) / x, [0, inf]), pi / 2 - mp.atan(0.7), 12))
check("arch k has integral of |sin x/x| at least 2/((k+1)pi)",
      all(q(lambda x: abs(mp.sin(x)) / x, [k * pi, (k + 1) * pi]) >= 2 / ((k + 1) * pi) for k in range(0, 8)))
check("Si(pi) = 1.852, 18% above pi/2", abs(mp.si(pi) - 1.852) < 5e-4 and abs(mp.si(pi) / (pi / 2) - 1.18) < 5e-3)

# exercises
check("f_n = n^2 x e^(-nx) has integral 1", all(near(q(lambda x: n * n * x * mp.exp(-n * x), [0, 1 / mp.mpf(n), inf]), 1, 15) for n in (1, 7, 50)))
a = mp.mpf("0.8")
check("Gaussian cosine transform", near(q(lambda x: mp.exp(-x * x) * mp.cos(2 * a * x), [-inf, 0, inf]), mp.sqrt(pi) * mp.exp(-a * a)))
check("int sin^2 x / x^2 = pi/2", near(q(lambda x: mp.sin(x) ** 2 / x**2, [0, 1]) + mp.mpf(1) / 2 - mp.quadosc(lambda x: mp.cos(2 * x) / (2 * x * x), [1, inf], omega=2), pi / 2, 10))
check("int_0^pi x sin x/(1+cos^2 x) = pi^2/4", near(q(lambda x: x * mp.sin(x) / (1 + mp.cos(x) ** 2), [0, pi]), pi**2 / 4))
check("int_0^1 ln x ln(1-x) = 2 - pi^2/6", near(q(lambda x: mp.log(x) * mp.log(1 - x), [0, 0.5, 1]), 2 - pi**2 / 6, 15))
check("J(a) = pi ln(1+a), a = 2.2", near(q(lambda x: mp.log(1 + 2.2**2 * x * x) / (1 + x * x), [0, 1, inf]), pi * mp.log(3.2), 12))
E1 = lambda u: mp.e1(u)
lam1 = q(lambda u: 1 - mp.exp(-E1(u)), [0, 1, 5, inf])
lam2 = q(lambda u: mp.exp(-u - E1(u)), [0, 1, 5, inf])
check("Golomb-Dickman constant 0.6243299885", near(lam1, lam2, 12) and abs(lam2 - mp.mpf("0.6243299885")) < 1e-10)
check("E_1(u) <= e^-u for u >= 1", all(E1(u) <= mp.exp(-u) for u in (1, 1.5, 3, 10)))


def longest_cycle_mean(n):
    # E[L_n] exactly: number of permutations of [n] with all cycles <= m, via exponential formula
    tot = Fr(0)
    for m in range(0, n):
        c = [Fr(1)] + [Fr(0)] * n  # c[k] = (number of perms of k with cycles <= m)/k!
        for k in range(1, n + 1):
            c[k] = sum(c[k - j] for j in range(1, min(m, k) + 1)) / k
        tot += 1 - c[n]
    return tot


check("E[L_60]/60 close to 0.6243 (figure)", abs(float(longest_cycle_mean(60)) / 60 - 0.6243) < 0.01)
gam = mp.euler
I = mp.quad(lambda x, y: (1 - x) / ((1 - x * y) * (-mp.log(x * y))), [0, 1], [0, 1])
check("Sondow double integral = gamma (numerically)", abs(I - gam) < 1e-6)
S1 = mp.nsum(lambda m: 1 / m - mp.log(1 + 1 / m), [1, inf])
check("sum (1/m - log(1+1/m)) = gamma", near(S1, gam, 15))
S2 = mp.nsum(lambda m: (-1) ** (m - 1) * (1 / m - mp.log(1 + 1 / m)), [1, inf])
check("alternating version = log(4/pi)", near(S2, mp.log(4 / pi), 15))
check("int_m^inf du/(u^2(u+1)) = 1/m - log(1+1/m)", all(near(q(lambda u: 1 / (u * u * (u + 1)), [m, inf]), mp.mpf(1) / m - mp.log(1 + mp.mpf(1) / m), 15) for m in (1, 2, 9)))
# Fresnel (new exercise)
fres = q(lambda u: mp.sin(u) / (2 * mp.sqrt(u)), [0, pi]) + mp.quadosc(lambda u: mp.sin(u) / (2 * mp.sqrt(u)), [pi, inf], omega=1)
fresc = q(lambda u: mp.cos(u) / (2 * mp.sqrt(u)), [0, pi]) + mp.quadosc(lambda u: mp.cos(u) / (2 * mp.sqrt(u)), [pi, inf], omega=1)
check("Fresnel: int sin(x^2) = int cos(x^2) = (1/2) sqrt(pi/2)",
      near(fres, mp.sqrt(pi / 2) / 2, 10) and near(fresc, mp.sqrt(pi / 2) / 2, 10))
for t in (1, 3, 10):
    Phi = q(lambda x: mp.expj(x * x), mp.linspace(0, t, 40 * t + 1))
    G = q(lambda y: mp.expj(t * t * (1 + y * y)) / (1 + y * y), mp.linspace(0, 1, 20 * t * t + 1))
    check("Fresnel: F = i(pi/4 - G) and |G| <= 2/t at t=%d" % t, near(Phi**2, 1j * (pi / 4 - G), 12) and abs(G) <= mp.mpf(2) / t)

# BBP
S = lambda j: mp.nsum(lambda k: 1 / (16**k * (8 * k + j)), [0, inf])
check("BBP: pi = 4 S_1 - 2 S_4 - S_5 - S_6", near(4 * S(1) - 2 * S(4) - S(5) - S(6), pi, 25))
y = sp.symbols("y")
check("16 - y^8 factorisation", sp.expand(-(y**2 - 2) * (y**2 + 2) * (y**2 - 2 * y + 2) * (y**2 + 2 * y + 2) - (16 - y**8)) == 0)
check("4 - 2y^3 - y^4 - y^5 = (1-y)(y^2+2)(y^2+2y+2)", sp.expand((1 - y) * (y**2 + 2) * (y**2 + 2 * y + 2) - (4 - 2 * y**3 - y**4 - y**5)) == 0)
check("partial fractions of 16(y-1)/((y^2-2)(y^2-2y+2))",
      sp.simplify(4 * y / (y**2 - 2) - 4 * (y - 1) / ((y - 1) ** 2 + 1) + 4 / ((y - 1) ** 2 + 1) - 16 * (y - 1) / ((y**2 - 2) * (y**2 - 2 * y + 2))) == 0)


def hex_digits(d, n=8):
    def T(j):
        s = 0.0
        for k in range(d + 1):
            s = (s + pow(16, d - k, 8 * k + j) / (8 * k + j)) % 1.0
        for k in range(d + 1, d + 12):
            s += 16.0 ** (d - k) / (8 * k + j)
        return s

    x = (4 * T(1) - 2 * T(4) - T(5) - T(6)) % 1.0
    out = ""
    for _ in range(n):
        x *= 16
        out += "%X" % int(x)
        x -= int(x)
    return out


check("hex digits of pi from position 1: 243F6A88", hex_digits(0) == "243F6A88")
check("hex digits of pi starting at position 10^6 (d = 10^6 - 1): 26C65E52", hex_digits(10**6 - 1) == "26C65E52")

# Borwein integrals
a7 = [Fr(1, 2 * k + 1) for k in range(1, 8)]
check("1/3 + ... + 1/13 = 43024/45045 = 0.955", sum(a7[:6]) == Fr(43024, 45045) and abs(float(sum(a7[:6])) - 0.955) < 5e-4)
check("adding 1/15 gives 1.0218", abs(float(sum(a7)) - 1.0218) < 5e-5)
eps = sum(a7) - 1
check("epsilon = 982/45045 and 15 epsilon < 2", eps == Fr(982, 45045) and 15 * eps < 2)
prod = Fr(1)
for k in range(1, 8):
    prod *= 2 * k + 1
deficit = Fr(prod, factorial(7) * 2**7) * eps**7  # times pi
frac = Fr(467807924713440738696537864469, 935615849440640907310521750000)
check("deficit formula equals 1/2 - the Borweins' fraction", Fr(1, 2) - frac == deficit)
check("deficit = 2.31e-11, probability 7.4e-12 per side", abs(float(deficit) * float(pi) - 2.31e-11) < 5e-14 and abs(float(deficit) - 7.4e-12) < 5e-14)
check("first Borwein integrals equal pi/2 (n = 1, 2 factors)",
      near(osc(lambda x: mp.sinc(x) * mp.sinc(x / 3), 1), pi / 2, 8))

print("\nALL CHECKS PASSED" if ok else "\nSOME CHECKS FAILED")
raise SystemExit(0 if ok else 1)
