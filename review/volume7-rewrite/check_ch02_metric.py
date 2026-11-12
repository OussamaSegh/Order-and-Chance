#!/usr/bin/env python3
"""Volume 7, Chapter 2: Dottie number, Newton digits, the 5-adic square root of -1, the map of Exercise 2.9."""
from fractions import Fraction as F
import mpmath as mp
from common import check, check_true, finish
mp.mp.dps = 60
x = mp.mpf(1)
for _ in range(400): x = mp.cos(x)
check("Dottie number", float(x), 0.7390851332, 5e-11)
check("sin 1 < 0.85", float(mp.sin(1)), 0.8415, 1e-4)
check("sin x* about 0.67", float(mp.sin(x)), 0.67, 5e-3)
check("steps per decimal digit about six", float(1 / -mp.log10(mp.sin(x))), 6, 0.3)
check("cos 2 <= -1/3", float(mp.cos(2)) <= -1/3 and 1, 1, 0)
# Newton for sqrt 2 from 2: bounds printed in the solution of Exercise 2.2
e = 2 - mp.sqrt(2); bounds = []
for _ in range(5): e = e * e / (2 * mp.sqrt(2)); bounds.append(e)
for b, pr in zip(bounds, [0.12, 5.2e-3, 9.6e-6, 3.3e-11, 3.8e-22]):
    check_true(f"bound {pr}", b <= pr * 1.02 and b >= pr * 0.9)
xs = mp.mpf(2)
for _ in range(5): xs = (xs + 2 / xs) / 2
err = xs - mp.sqrt(2)
check_true("x_5 has 24 correct digits", mp.mpf(10) ** -25 < err < mp.mpf(10) ** -24)
check("e_1 = 3/2 - sqrt 2", float(mp.mpf(3) / 2 - mp.sqrt(2)), 0.086, 1e-3)
# Hensel, Exercise 2.7
T = lambda v: v - 4 * (v * v + 1)
check_true("T(2) = -18 = 7 mod 25", T(2) == -18 and T(2) % 25 == 7)
check_true("T(7) = -193 = 57 mod 125", T(7) == -193 and T(7) % 125 == 57)
check_true("57^2+1 = 26*125", 57 ** 2 + 1 == 3250 == 26 * 125)
check_true("57 = 2 + 1*5 + 2*25", 57 == 2 + 5 + 50)
# 5-adic examples of Example 2.2(d)
def v5(fr):
    n, d, v = fr.numerator, fr.denominator, 0
    while n % 5 == 0: n //= 5; v += 1
    while d % 5 == 0: d //= 5; v -= 1
    return v
check_true("|50|_5 = 1/25, |3/10|_5 = 5, |7|_5 = 1", (v5(F(50)), v5(F(3, 10)), v5(F(7))) == (2, -1, 0))
check_true("1 + 5^10 is nearly ten million away", 9.7e6 < 5 ** 10 < 1e7)
# Exercise 2.9: digits of 1/3 in Z_2 and its image 11/12; bounds of (b) on integers
N = 40; inv3 = pow(3, -1, 2 ** N)
digits = [(inv3 >> k) & 1 for k in range(N)]
check_true("digits of 1/3 in Z_2: 1,1,0,1,0,1,...", digits[:8] == [1, 1, 0, 1, 0, 1, 0, 1])
phi = lambda ds: sum(F(2 * a, 3 ** (k + 1)) for k, a in enumerate(ds))
check("phi(1/3) = 11/12", float(phi(digits)), 11 / 12, 1e-12)
ok = True
for a in range(64):
    for b in range(a):
        j = ((a - b) & -(a - b)).bit_length() - 1
        da = [(a >> k) & 1 for k in range(8)]; db = [(b >> k) & 1 for k in range(8)]
        d = abs(phi(da) - phi(db))
        ok &= F(1, 3 ** (j + 1)) <= d <= F(1, 3 ** j)
check_true("3^(-j-1) <= |phi(x)-phi(y)| <= 3^(-j)", ok)
finish()
