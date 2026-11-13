#!/usr/bin/env python3
"""Volume 14, Chapter 3 (sieves): figure data and constants."""
import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import check, check_true, finish, primes_upto
import numpy as np
from mpmath import mp, mpf, euler, log as mlog
mp.dps = 20
# --- Figure rough: Phi(x,z)/(x prod(1-1/p)) for x=10^7 and prime z <= sqrt x
x = 10**7
P = primes_upto(x)
spf = np.zeros(x + 1, dtype=np.int32)   # smallest prime factor
for p in P[P <= int(x**0.5)][::-1]:
    spf[p::p] = p
spf[spf == 0] = np.arange(x + 1)[spf == 0]   # primes (and 0,1)
s = spf[2:]
srt = np.sort(s)
pts = []
prod = 1.0
for z in P[P <= int(x**0.5)]:
    prod *= 1 - 1 / z
    phi = 1 + (len(srt) - np.searchsorted(srt, z, side='right'))  # n=1 plus n>=2 with spf > z
    pts.append((math.log(x) / math.log(z), phi / (x * prod)))
u2 = [pts[-1][1]]  # largest prime z <= sqrt x, u = 2.002
check("ratio at u=2", u2[0], 0.954, 0.0005)
dip = min(r for u, r in pts if 2 <= u <= 2.3)
check("dip near u=2.1", dip, 0.935, 0.0015)
check_true("dip location near 2.1", any(abs(u - 2.1) < 0.06 and r == dip for u, r in pts))
peak = max(r for u, r in pts if 2.5 <= u <= 3.5)
check("overshoot near u=3", peak, 1.005, 0.0015)
check_true("within 3e-4 of 1 from u=3.5", all(abs(r - 1) < 3e-4 for u, r in pts if u >= 3.5))
check("e^gamma/2", float(mp.e ** euler / 2), 0.89, 0.005)
# --- twin constant
C2 = 1.0
for p in P[1:200000]:
    C2 *= 1 - 1 / (p - 1) ** 2
check("C_2", C2, 0.6601618, 2e-7)
# --- Artin's constant and primitive root proportions at 10^7
A = 1.0
for p in P[:200000]:
    A *= 1 - 1 / (p * (p - 1))
check("Artin A", A, 0.3739558, 2e-7)
check("20/19 A", 20 / 19 * A, 0.39364, 1e-5)
def is_primroot(a, p, fac):
    return all(pow(a, (p - 1) // q, p) != 1 for q in fac)
cnt = {2: 0, 3: 0, 5: 0, 10: 0}; tot = {a: 0 for a in cnt}
for p in P:
    p = int(p)
    m = p - 1; fac = set()
    while m > 1:
        q = int(spf[m]); fac.add(q); m //= q
    for a in cnt:
        if p % a == 0 or (a == 10 and p in (2, 5)): continue
        tot[a] += 1
        if is_primroot(a, p, fac): cnt[a] += 1
for a, v in zip([2, 3, 5, 10], [0.37391, 0.37411, 0.39394, 0.37449]):
    check(f"primitive root {a} proportion at 1e7", cnt[a] / len(P), v, 6e-6)
finish()
