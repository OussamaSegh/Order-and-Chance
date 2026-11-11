#!/usr/bin/env python3
"""Chapter 1 (Mertens's Theorems): every printed number that the page does not prove."""
import math
import numpy as np
from common import *

P = primes_upto(10**7); Pf = P.astype(float)
logP = np.log(Pf)

# Think box and its answer
prod1000 = float(np.prod(1 - 1 / Pf[P <= 1000]))
check("prod_{p<=1000}(1-1/p)", prod1000, 0.0810, 6e-4)   # the box prints the Mertens approximation 0.0813
check("e^-gamma/log 1000", math.exp(-GAMMA) / math.log(1000), 0.0813, 5e-5)
check("1/log 10^6", 1 / math.log(1e6), 0.0724, 5e-5)
check("2e^-gamma", 2 * math.exp(-GAMMA), 1.1229, 5e-5)
check("e^-gamma", math.exp(-GAMMA), 0.5614, 6e-5)

# Figure 1.1: theta(x)/x and psi(x)/x at x = 3000
theta = float(logP[P <= 3000].sum())
psi = sum(math.log(p) * int(math.log(3000) / math.log(p) + 1e-12) for p in P[P <= 3000].tolist())
check("psi(3000)/3000", psi / 3000, 1.0004, 5e-5)
check("theta(3000)/3000", theta / 3000, 0.977, 5e-4)

# R(x) = sum log p / p - log x
cs = np.cumsum(logP / Pf)
def R(x): return float(cs[np.searchsorted(P, x, side="right") - 1]) - math.log(x)
check("R(10^3)", R(10**3), -1.298, 6e-4)
check("R(10^5)", R(10**5), -1.329, 6e-4)
check("R(10^7)", R(10**7), -1.3324, 6e-5)
check("sum log p/(p(p-1))", float((logP / (Pf * (Pf - 1))).sum()), 0.75536, 1e-5)   # printed truncated
check("limit of R", -GAMMA - float((logP / (Pf * (Pf - 1))).sum()), -1.33258, 1e-5)

# Meissel-Mertens constant M and H, from M = gamma - H with H = sum(-log(1-1/p) - 1/p)
h = -np.log1p(-1 / Pf) - 1 / Pf
H = float(h.sum()) + 0.5 / (1e7 * math.log(1e7))          # tail ~ sum_{p>x} 1/(2p^2) ~ 1/(2 x log x)
check("H", H, 0.3157184520, 2e-9)
check("M = gamma - H", GAMMA - H, 0.2614972128, 2e-9)
S7 = float((1 / Pf).sum()) - math.log(math.log(1e7))
check("sum 1/p - loglog x at 10^7", S7, 0.261507, 6e-7)
check("within 1e-5 of M", abs(S7 - 0.2614972128), 0.0, 1e-5)
check("primes to 10^100: sum 1/p", math.log(100 * math.log(10)) + 0.2615, 5.7, 0.05)

# Worked example before Theorem 1.3
check("log 10!", math.lgamma(11), 15.104, 5e-4)
check("8 log2 + 4 log3 + 2 log5 + log7", 8*math.log(2)+4*math.log(3)+2*math.log(5)+math.log(7), 15.104, 5e-4)
check("sum Lambda(n)/n, n<=10", sum(math.log(p)/p**k for p in (2,3,5,7) for k in (1,2,3) if p**k<=10), 1.695, 5e-4)
check("log 10", math.log(10), 2.303, 5e-4)

# Solutions
check("6 e^gamma / pi^2", 6 * math.exp(GAMMA) / math.pi**2, 1.0827, 1e-4)   # printed truncated
check("log 2", math.log(2), 0.69, 5e-3)
check("log 4", math.log(4), 1.39, 5e-3)
check("loglog 10^9", math.log(math.log(1e9)), 3.0, 0.05)
check_true("exercise 1.3: psi(x) >= x log2 - 3 log x - 3 for 2 <= x <= 3000",
           all(sum(math.log(p) * int(math.log(x) / math.log(p) + 1e-12) for p in P[P <= x].tolist()) >= x * math.log(2) - 3 * math.log(x) - 3
               for x in range(2, 3001, 7)))
finish()
