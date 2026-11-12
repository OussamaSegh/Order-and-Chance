#!/usr/bin/env python3
"""Volume 7, Chapter 12: dimensions, cover sums, mass distribution constants, weak convergence examples."""
import math
from common import check, check_true, finish
s = math.log(2) / math.log(3)
check("log 2/log 3", s, 0.631, 1e-3)
check("log 8/log 3", math.log(8) / math.log(3), 1.893, 1e-3)
check("log 9/log 10", math.log(9) / math.log(10), 0.954, 1e-3)
check_true("2^n 3^{-ns} = 1", all(abs(2**n * 3**(-n * s) - 1) < 1e-9 for n in range(1, 30)))
check("ratio s=1/2", 2 / math.sqrt(3), 1.155, 1e-3)
check("sum n=3, s=1/2", (2 / math.sqrt(3))**3, 1.54, 5e-3)
check("ratio s=3/4", 2 * 3**-0.75, 0.877, 1e-3)
check("sum n=3, s=3/4", (2 * 3**-0.75)**3, 0.675, 1e-3)
check_true("Cantor: 2^-k = (3^-k)^s and 3^s = 2", abs(3**s - 2) < 1e-12)
t = math.log(9) / math.log(10)
check("no digit 7: 2*10^s = 18", 2 * 10**t, 18, 1e-9)
check_true("carpet: 8^k (sqrt2 3^-k)^s = 2^(s/2)", abs(8**4 * (math.sqrt(2) * 3**-4)**(math.log(8) / math.log(3)) - 2**(math.log(8) / math.log(3) / 2)) < 1e-9)
m = 7
check_true("generalised carpet dimension below 2", math.log(m * m - 1) / math.log(m) < 2 and math.log(10**6 - 1) / math.log(10**3) > 1.9999)
check_true("|x - tau_M(x)| <= x^2/M", all(abs(x - max(-M, min(x, M))) <= x * x / M + 1e-12 for M in (1, 3) for x in [i / 10 for i in range(-100, 101)]))
finish()
