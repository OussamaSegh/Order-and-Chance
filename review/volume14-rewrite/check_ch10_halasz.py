#!/usr/bin/env python3
"""Volume 14, Chapter 10 (multiplicative functions): figure data."""
import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import check, check_true, finish, primes_upto
import numpy as np

X = 10**7
P = primes_upto(X)
mu = np.ones(X + 1, dtype=np.int8)
lam = np.ones(X + 1, dtype=np.int8)
sq2 = np.zeros(X + 1, dtype=bool)         # n is a sum of two squares
for a in range(int(X**0.5) + 1):
    bmax = int((X - a * a) ** 0.5)
    b = np.arange(a, bmax + 1)
    sq2[a * a + b * b] = True
for p in P:
    p = int(p)
    mu[p::p] *= -1
    pk = p
    while pk <= X:
        lam[pk::pk] *= -1
        pk *= p
    if p * p <= X: mu[p*p::p*p] = 0
mu[0] = 0; lam[0] = 0; sq2[0] = False
check("sum mu to 1e7", int(mu[1:].astype(np.int64).sum()), 1037, 0)
check("sum lambda to 1e7", int(lam[1:].astype(np.int64).sum()), -842, 0)
check("squarefree density at 1e7", float((mu[1:] != 0).sum()) / X, 0.607929, 1e-6)
check("6/pi^2", 6 / math.pi**2, 0.607927, 1e-6)
check("sums of two squares density at 1e7", float(sq2[1:].sum()) / X, 0.1985, 1e-4)
# n^i and mu^2 n^i at 1e6
Y = 10**6
n = np.arange(1, Y + 1, dtype=float)
z = np.exp(1j * np.log(n))
check("|avg n^i| at 1e6", abs(z.sum()) / Y, 0.70711, 1e-5)
check("|avg mu^2 n^i| at 1e6", abs((z * (mu[1:Y + 1] != 0)).sum()) / Y, 0.42987, 1e-5)
check("1/|1+i|", 1 / math.sqrt(2), 0.7071, 1e-4)
check("6/pi^2/|1+i|", 6 / math.pi**2 / math.sqrt(2), 0.4299, 1e-4)
finish()
