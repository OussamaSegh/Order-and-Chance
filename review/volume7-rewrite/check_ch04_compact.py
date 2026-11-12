#!/usr/bin/env python3
"""Volume 7, Chapter 4: the variance identity of Bernstein's proof and the uniform bound of Exercise 4 (Bernstein)."""
from fractions import Fraction as F
from math import comb
from common import check, check_true, finish
for n in (1, 2, 5, 12):
    for x in (F(0), F(1, 3), F(1, 2), F(7, 9), F(1)):
        v = sum(comb(n, k) * x**k * (1 - x)**(n - k) * (F(k, n) - x)**2 for k in range(n + 1))
        check_true(f"variance identity n={n} x={x}", v == x * (1 - x) / n)
# x(1-x) <= 1/4, used in the bound
check_true("x(1-x) <= 1/4", all(F(i, 100) * (1 - F(i, 100)) <= F(1, 4) for i in range(101)))
# Bernstein polynomials of |x - 1/2| converge
f = lambda x: abs(x - 0.5)
def B(n, x): return sum(f(k / n) * comb(n, k) * x**k * (1 - x)**(n - k) for k in range(n + 1))
errs = [max(abs(B(n, i / 50) - f(i / 50)) for i in range(51)) for n in (10, 40, 160)]
check_true("Bernstein error decreases", errs[0] > errs[1] > errs[2] and errs[2] < 0.04)
finish()
