#!/usr/bin/env python3
"""Among the first 10^8 primes: share of primes ending in 1 followed by a prime ending in 1 (Lemke Oliver-Soundararajan)."""
import numpy as np
LIM = 2_100_000_000; N = 10 ** 8
base = np.ones(int(LIM ** .5) + 2, bool); base[:2] = False
for p in range(2, int(len(base) ** .5) + 1):
    if base[p]: base[p * p::p] = False
bp = np.nonzero(base)[0]; seg = 10 ** 7; count = 0; last = None; n11 = n1 = 0
for lo in range(0, LIM, seg):
    hi = lo + seg; s = np.ones(seg, bool)
    if lo == 0: s[:2] = False
    for p in bp:
        if p * p >= hi: break
        st = max(p * p, ((lo + p - 1) // p) * p); s[st - lo::p] = False
    ps = np.nonzero(s)[0] + lo
    take = min(len(ps), N - count); ps = ps[:take]; d = ps % 10
    if last is not None: d = np.concatenate(([last], d))
    a, b = d[:-1], d[1:]; n1 += int(np.sum(a == 1)); n11 += int(np.sum((a == 1) & (b == 1)))
    last = int(d[-1]); count += take
    if count >= N: break
print("first 1e8 primes: P(next ends in 1 | ends in 1) =", n11 / n1, n11, n1)
