#!/usr/bin/env python3
"""Volume 14, Chapter 5 (exponential sums over primes): figure data."""
import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import check, check_true, finish, primes_upto
import numpy as np

# --- Figure: |S(alpha)|/psi(N), N = 10^5, bars = max over windows of width 1/4000
N = 10**5
P = primes_upto(N)
ns, lam = [], []
for p in P:
    q = int(p)
    while q <= N:
        ns.append(q); lam.append(math.log(int(p))); q *= int(p)
ns = np.array(ns, dtype=float); lam = np.array(lam)
psi = lam.sum()
def peak(a, q):
    # bar containing a/q: window [k/4000, (k+1)/4000]
    k = math.floor(4000 * a / q - 1e-12) if a / q == 0.5 else math.floor(4000 * a / q)
    al = np.linspace(k / 4000, (k + 1) / 4000, 801)
    vals = np.abs(np.exp(2j * np.pi * np.outer(al, ns)) @ lam)
    return vals.max() / psi
for (a, q), v, tol in [((1, 2), 0.9998, 1e-4), ((1, 3), 0.499, 0.001), ((1, 6), 0.499, 0.001),
                       ((1, 5), 0.250, 0.001), ((2, 5), 0.250, 0.001), ((1, 10), 0.250, 0.001),
                       ((3, 10), 0.250, 0.001), ((1, 7), 0.168, 0.001), ((1, 11), 0.10, 0.005)]:
    check(f"peak at {a}/{q}", peak(a, q), v, tol)
for a, q in [(1, 4), (1, 8), (1, 9)]:
    check_true(f"no peak at {a}/{q} ({peak(a, q):.4f})", peak(a, q) < 0.02)

# --- Figure: Kloosterman sums for p = 100003 via one FFT
p = 100003
check_true("p prime", int(primes_upto(p)[-1]) == p)
b = np.arange(1, p)
inv = np.array([pow(int(x), p - 2, p) for x in b])
A = np.zeros(p, dtype=complex)
A[b] = np.exp(2j * np.pi * inv / p)          # A(b) = e(b^{-1}/p)
K = (np.fft.ifft(A) * p).real[1:]            # K(n) = sum_b A(b) e(nb/p), n = 1..p-1
# spot check one value directly
n0 = 12345
direct = sum(math.cos(2 * math.pi * ((x + n0 * pow(x, p - 2, p)) % p) / p) for x in range(1, p))
check("K(12345) FFT vs direct", K[n0 - 1], direct, 1e-6)
check("number of sums", len(K), 100002, 0)
check("max K/(2 sqrt p)", np.abs(K).max() / (2 * math.sqrt(p)), 0.99988, 5e-6)
check("second moment", np.mean(K**2) / p, 1.0000, 5e-5)
check("fourth moment", np.mean(K**4) / p**2, 2.0000, 5e-5)
finish()
