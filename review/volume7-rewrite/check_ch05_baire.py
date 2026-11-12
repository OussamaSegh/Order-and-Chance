#!/usr/bin/env python3
"""Volume 7, Chapter 5: Takagi's function at 1/2, 1/4, 1/3, its maximum, the slopes at 1/3."""
from fractions import Fraction as F
from common import check, check_true, finish
phi = lambda y: abs(y - round(y)) if not isinstance(y, F) else min(y - (y.numerator // y.denominator), 1 - (y - (y.numerator // y.denominator)))
def T(x, N=60): return sum(phi(2**n * x) / 2**n for n in range(N))
check_true("T(1/2) = 1/2", T(F(1, 2)) == F(1, 2))
check_true("T(1/4) = 1/2", T(F(1, 4)) == F(1, 2))
check("T(1/3) = 2/3", float(T(F(1, 3))), 2 / 3, 1e-12)
check_true("phi(2^n/3) = 1/3", all(phi(F(2**n, 3)) == F(1, 3) for n in range(40)))
check_true("phi(y)+phi(2y)/2 <= 1/2", all(phi(F(i, 997)) + phi(2 * F(i, 997)) / 2 <= F(1, 2) for i in range(998)))
check_true("T <= 2/3 on a grid", max(T(F(i, 1024), 12) for i in range(1025)) <= F(2, 3))
# slopes: s_n = sum_{k<n} eps_k, eps_k = +1 if frac(2^k x) < 1/2
x = F(1, 3); s = 0; slopes = []
for k in range(4):
    fr = (2**k * x) % 1
    s += 1 if fr < F(1, 2) else -1
    slopes.append(s)
print("slopes at 1/3:", slopes)
check_true("slopes 1,0,1,0", slopes == [1, 0, 1, 0])
finish()
