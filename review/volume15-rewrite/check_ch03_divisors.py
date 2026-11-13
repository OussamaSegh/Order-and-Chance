#!/usr/bin/env python3
"""Recompute the printed numbers of Chapter 3: Landau's B(x), Selberg-Delange ratios, (-1)^omega, sigma(n)/n."""
import math, numpy as np
from scipy.integrate import quad
from scipy.special import gamma
from common import check, check_true, finish, primes_upto

X = 10**7
P = primes_upto(10**8)
p3 = P[P % 4 == 3].astype(float)
prod3 = math.exp(-0.5 * np.sum(np.log1p(-p3 ** -2)))
b = prod3 / math.sqrt(2)
check("Landau's b", b, 0.764223, 5e-6)
c3 = math.sqrt(2) / math.pi * prod3
check("c_3", c3, 0.48652, 5e-5)

# omega(n), Omega-free arrays, and sums of two squares up to 1e7
small = P[P <= X]
omega = np.zeros(X + 1, dtype=np.int8)
bad3 = np.zeros(X + 1, dtype=bool)       # some p=3 mod 4 to an odd power
only3 = np.ones(X + 1, dtype=bool)       # all prime factors are 3 mod 4
only3[0] = False
for p in small:
    omega[p::p] += 1
    if p % 4 != 3: only3[p::p] = False
    if p % 4 == 3:
        # parity of v_p
        par = np.zeros(X + 1, dtype=bool)
        pk = int(p)
        while pk <= X:
            par[pk::pk] ^= True
            pk *= int(p)
        bad3 |= par
B = int((~bad3[1:]).sum())
check("B(1e7)", B, 1985459, 0)
L = math.log(X)
check("Landau's formula at 1e7", b * X / math.sqrt(L), 1903547, 1)
ram = b * (quad(lambda t: 1 / math.sqrt(math.log(t)), 2, X, limit=500)[0])
check("Ramanujan's formula at 1e7", ram, 1969213, 1)

# Selberg-Delange ratios at 1e7
def F(z):
    pp = P[P <= 10**7].astype(float)
    return math.exp(np.sum(np.log1p((z - 1) / pp) + (z - 1) * np.log1p(-1 / pp)))
om = omega[1:].astype(float)
for z, pr in [(0.5, 1.034), (2, 1.080), (3, 1.454)]:
    s = np.sum(z ** om)
    main = X * L ** (z - 1) * F(z) / gamma(z)
    check(f"SD ratio z={z}", s / main, pr, 2e-3)
check("(-1)^omega mean at 1e7", np.sum((-1.0) ** om) / X, -0.000165, 2e-6)
n3 = int(only3[1:].sum())   # n=1 has no prime factor: counted (empty condition)
check("only-3-mod-4 ratio at 1e7", n3 / (c3 * X / math.sqrt(L)), 1.026, 2e-3)

# sigma(n)/n up to 1e6
N = 10**6
sig = np.zeros(N + 1)
for d in range(1, N + 1): sig[d::d] += d
r = sig[1:] / np.arange(1, N + 1)
check("abundant share up to 1e6 (percent)", 100 * np.mean(r >= 2), 24.75, 0.006)
check("largest sigma(n)/n below 1e6", r.max(), 4.509, 5e-4)
check("argmax", int(np.argmax(r)) + 1, 720720, 0)
finish()
