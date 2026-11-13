#!/usr/bin/env python3
"""Volume 14, Chapter 13 (Gowers norms, Green-Tao): prime progressions up to 3*10^5."""
import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import check, check_true, finish, primes_upto
import numpy as np

N = 3 * 10**5
isp = np.zeros(N + 1, dtype=bool); isp[primes_upto(N)] = True
il = np.zeros(N + 1); il[2:] = 1 / np.log(np.arange(2, N + 1))
def S(k):
    s = 1.0
    for p in primes_upto(10**6):
        p = int(p)
        s *= (p - 1) * (1 + max(p - k, 0)) / (p * p * (1 - 1 / p) ** k)
    return s
for k, cnt, rat in [(3, 19024997, 0.991), (4, 2352329, 0.988), (5, 219305, 0.978)]:
    c = 0; w = 0.0
    for d in range(1, (N - 2) // (k - 1) + 1):
        L = N - (k - 1) * d - 1          # x = 2 .. N-(k-1)d
        m = isp[2:2 + L].copy(); v = il[2:2 + L].copy()
        for i in range(1, k):
            m &= isp[2 + i * d:2 + i * d + L]; v *= il[2 + i * d:2 + i * d + L]
        c += int(m.sum()); w += float(v.sum())
    check(f"{k}-APs of primes up to 3e5", c, cnt, 0)
    check(f"ratio k={k}", c / (S(k) * w), rat, 0.0006)
check_true("Green 27 and Tao 28 on 9 April 2004", (2004 - 1977 - (0 if (4, 9) >= (2, 27) else 1)) == 27 and (2004 - 1975 - (0 if (4, 9) >= (7, 17) else 1)) == 28)
finish()
