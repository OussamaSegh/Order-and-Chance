#!/usr/bin/env python3
"""Volume 14, Chapter 7 (three primes): figure data and the explicit bound."""
import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import check, check_true, finish, primes_upto
import numpy as np

M = 100000
lam = np.zeros(M + 1)
P = primes_upto(M)
for p in P:
    q = int(p)
    while q <= M:
        lam[q] = math.log(int(p)); q *= int(p)
L = 1 << 19
F = np.fft.rfft(lam, L)
R = np.fft.irfft(F**3, L)[:M + 1]     # R(N) for N <= M (no wrap: 3M < L)
# exact check of one value
N0 = 1001
direct = sum(lam[a] * lam[b] * lam[N0 - a - b] for a in range(1, N0) if lam[a] for b in range(1, N0 - a) if lam[b])
check("R(1001) FFT vs direct", R[N0], direct, 1e-6 * direct)
BIG = primes_upto(10**6)
tail = np.prod(1 + 1 / (BIG.astype(float) - 1)**3)
def sing(N):
    s = tail
    m = N
    for p in BIG:
        p = int(p)
        if p * p > m: break
        if m % p == 0:
            s *= (1 - 1 / (p - 1)**2) / (1 + 1 / (p - 1)**3)
            while m % p == 0: m //= p
    if m > 1:
        s *= (1 - 1 / (m - 1)**2) / (1 + 1 / (m - 1)**3)
    return s
ratio = lambda N: R[N] / (0.5 * sing(N) * N * N)
for N, v in [(1001, 0.945), (10001, 0.993), (99001, 0.998)]:
    check(f"ratio at N={N}", ratio(N), v, 0.0006)
S = [sing(N) for N in range(1001, 99002, 1000)]
check("min singular series", min(S), 1.47, 0.006)
check("max singular series", max(S), 2.3, 0.01)
check("sup over odd N (tail includes p=2)", tail, 2.30, 0.01)
# Borozdin's bound 3^(3^15): number of digits
check("digits of 3^(3^15) / 10^6", 3**15 * math.log10(3) / 1e6, 6.85, 0.01)
finish()
