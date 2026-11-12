#!/usr/bin/env python3
"""Volume 7, Chapter 1: the Calkin-Wilf numbers of Exercises 1.9 and 1.10, and the injection of Theorem 1.17."""
from fractions import Fraction as F
from math import floor
from itertools import product
from common import check_true, finish

def newman(q): return 1 / (2 * floor(q) + 1 - q)
q = [None, F(1)]
for n in range(1, 3000): q.append(newman(q[n]))
check_true("q_1..q_10 as printed", q[1:11] == [F(1), F(1, 2), F(2), F(1, 3), F(3, 2), F(2, 3), F(3), F(1, 4), F(4, 3), F(3, 5)])
check_true("q_43 = 13/5", q[43] == F(13, 5))
# children of q_n are q_2n and q_2n+1 (the tree numbering)
check_true("children", all(q[2 * n] == q[n] / (q[n] + 1) and q[2 * n + 1] == q[n] + 1 for n in range(1, 1400)))
check_true("no repetition among the first 3000", len(set(q[1:])) == len(q) - 1)
# Theorem 1.17: A -> sum 2*3^(-n-1) separates subsets; brute force on subsets of {0..11}
vals = {}
for bits in product([0, 1], repeat=12):
    vals.setdefault(sum(F(2 * b, 3 ** (n + 1)) for n, b in enumerate(bits)), bits)
check_true("the ternary map is injective on 4096 subsets", len(vals) == 4096)
# Exercise 1.1: phi(q) = (2q+2)/(q+2)
ok = True
for a in range(1, 40):
    for b in range(1, 40):
        x = F(a, b); y = (2 * x + 2) / (x + 2)
        ok &= (y * y - 2 == 2 * (x * x - 2) / (x + 2) ** 2) and ((y > x) == (x * x < 2))
check_true("phi improves approximations of sqrt 2", ok)
finish()
