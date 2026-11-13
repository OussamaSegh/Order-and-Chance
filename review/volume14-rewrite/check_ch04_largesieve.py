#!/usr/bin/env python3
"""Volume 14, Chapter 4 (large sieve, Bombieri-Vinogradov): figure data and constants."""
import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import check, check_true, finish, primes_upto
import numpy as np
from mpmath import mp, zeta, euler, pi as mpi, log as mlog, mpf
mp.dps = 25

def phi_upto(n):
    ph = np.arange(n + 1, dtype=np.int64)
    for p in primes_upto(n):
        ph[p::p] -= ph[p::p] // p
    return ph

def theta_classes(x, Q):
    """For q <= Q, return arrays of theta(x;q,a) for all a (numpy)."""
    P = primes_upto(x)
    L = np.log(P.astype(float))
    out = {}
    for q in range(1, Q + 1):
        out[q] = np.bincount(P % q, weights=L, minlength=q)
    return out

for x, (bv, triv) in [(10**6, (0.35, 13.4)), (10**7, (0.26, 15.6))]:
    Q = int(math.isqrt(x))
    P = primes_upto(x); L = np.log(P.astype(float))
    ph = phi_upto(Q)
    E = 0.0; T = 0.0
    for q in range(1, Q + 1):
        th = np.bincount(P % q, weights=L, minlength=q)
        a = np.arange(q); cop = np.gcd(a, q) == 1
        E += np.max(np.abs(th[cop] - x / ph[q])); T += x / ph[q]
    check(f"BV sum / x at Q=sqrt x, x={x}", E / x, bv, 0.006)
    check(f"trivial bound / x, x={x}", T / x, triv, 0.06)

# Hooley constant
s = mpf(0)
for p in primes_upto(10**6):
    s += mlog(int(p)) / (int(p) * (int(p) - 1))
c = euler + mlog(2 * mpi) + 1 + s
check("Hooley c", float(c), 4.1704, 1e-4)

# variance minus Hooley curve
for x, pts in [(10**6, [(1000, 0.20), (4000, 0.07), (20000, 0.02)]), (10**7, [(1000, 0.16), (4000, 0.06)])]:
    P = primes_upto(x); L = np.log(P.astype(float))
    Qmax = max(Q for Q, _ in pts)
    ph = phi_upto(Qmax)
    V = 0.0; want = dict(pts)
    for q in range(1, Qmax + 1):
        th = np.bincount(P % q, weights=L, minlength=q)
        a = np.arange(q); cop = np.gcd(a, q) == 1
        V += float(np.sum((th[cop] - x / ph[q]) ** 2))
        if q in want:
            d = V / (q * x) - (math.log(q) - float(c))
            check(f"variance minus curve x={x} Q={q}", d, want[q], 0.006)

# Burgess exponent
check("1/(4 sqrt e)", 1 / (4 * math.sqrt(math.e)), 0.152, 0.0005)

# least non-residues below 10^6
P = [int(p) for p in primes_upto(10**6) if p > 2]
check("odd primes below 1e6", len(P), 78497, 0)
small = [int(p) for p in primes_upto(100)]
def n2(p):
    for l in small:
        if pow(l, (p - 1) // 2, p) == p - 1: return l
    raise ValueError(p)
vals = [n2(p) for p in P]
check("average n2", sum(vals) / len(vals), 3.65, 0.005)
mx = max(vals); argmx = P[vals.index(mx)]
check("max n2", mx, 43, 0); check("argmax n2", argmx, 366791, 0)
for k in range(1, 9):
    pk = small[k - 1]
    prop = sum(1 for v in vals if v == pk) / len(vals)
    check_true(f"proportion n2=p_{k} within 2% of 2^-{k} ({prop:.5f})", abs(prop * 2**k - 1) < 0.02)
S = sum(mpf(int(p)) / mpf(2) ** k for k, p in enumerate(primes_upto(2000), 1))
check("sum p_k/2^k", float(S), 3.6746, 1e-4)
check("C = zeta(2)zeta(3)/zeta(6)", float(zeta(2) * zeta(3) / zeta(6)), 1.9435, 1e-4)
for x, v in [(10**6, 1.9268), (10**7, 1.9324)]:
    Pr = primes_upto(x)
    # tau(p-1) via divisor-count sieve
    tau = np.zeros(x + 1, dtype=np.int32)
    for d in range(1, x + 1):
        tau[d::d] += 1
    check(f"sum tau(p-1)/x at {x}", float(tau[Pr - 1].sum()) / x, v, 1e-4)
finish()
