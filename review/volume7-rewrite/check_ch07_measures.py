#!/usr/bin/env python3
"""Volume 7, Chapter 7: fat Cantor set, fourth-moment count, the digits of 1/5 and the dealt numbers, quantiles."""
from fractions import Fraction as F
from itertools import product
import math
from common import check, check_true, finish
check_true("removed length is 1/2", abs(sum(2**(n - 1) * 4.0**-n for n in range(1, 60)) - 0.5) < 1e-15)
l = F(1)
for n in range(1, 25):
    l2 = (l - F(1, 4**n)) / 2
    assert l > F(1, 4**n) and l2 < F(1, 2**n) and l2 > F(1, 2**(n + 1))
    l = l2
check_true("fat Cantor interval lengths between 2^-(n+1) and 2^-n", True)
# Lemma (fourth moment): exact count against the bound, small cases
for b, n in ((2, 8), (3, 6), (10, 3)):
    d = 0; tot = F(0)
    for w in product(range(b), repeat=n):
        tot += (sum(1 for c in w if c == d) - F(n, b))**4
    check_true(f"sum of fourth powers <= b^n (3n^2-2n), b={b}, n={n}", tot <= b**n * (3 * n * n - 2 * n))
    eps = F(1, 4)
    bad = sum(1 for w in product(range(b), repeat=n) if abs(sum(1 for c in w if c == d) - F(n, b)) >= n * eps)
    check_true(f"measure bound b={b}, n={n}", F(bad, b**n) <= 3 / (eps**4 * n * n))
# digits of 1/5
x = F(1, 5); D = [None]
for j in range(1, 2001):
    x *= 2; D.append(int(x >= 1)); x -= D[-1]
check_true("digits 0011 repeated", D[1:9] == [0, 0, 1, 1, 0, 0, 1, 1])
check_true("D_j = 1 iff j = 3, 0 mod 4", all(D[j] == (j % 4 in (3, 0)) for j in range(1, 2001)))
def U(k, J=9): return sum(F(D[2**(k - 1) * (2 * j - 1)], 2**j) for j in range(1, J))
check("U_1(1/5)", float(U(1)), 1 / 3, 2**-8)
check("U_2(1/5)", float(U(2)), 0, 0)
check("U_3(1/5)", float(U(3)), 1, 2**-8)
check("U_4(1/5)", float(U(4, 7)), 1, 2**-6)
check("X_1 = log 3/2", -math.log(1 - 1 / 3), 0.405, 1e-3)
check_true("C+C digits", all(t in (0 + 0, 1 + 0, 1 + 1) for t in (0, 1, 2)))
finish()
