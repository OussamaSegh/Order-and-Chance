"""Number checks for Volume 6, Chapter 10 (random models of the primes)."""
import math
import numpy as np
import sympy
from common import GAMMA, primes_upto, check, check_true, finish

# Lemma oneminus
check("4(log 2 - 1/2)", 4 * (math.log(2) - 0.5), 0.77, 5e-3)

# Record gaps (Figure fig:gaps): consecutive primes and ratios g/log^2 p
for p, g, printed in ((4302407359, 354, 0.72), (1693182318746371, 1132, 0.92),
                      (1425172824437699411, 1476, 0.84)):
    check_true(f"{p} and {p}+{g} are consecutive primes",
               sympy.isprime(p) and sympy.nextprime(p) == p + g)
    check(f"ratio g/log^2 p for gap {g}", g / math.log(p) ** 2, printed, 5e-3)
check("Granville 2e^-gamma", 2 * math.exp(-GAMMA), 1.1229, 5e-5)

# Singular series
P = primes_upto(10 ** 7)
pf = P[1:].astype(np.float64)
C2 = float(np.prod(pf * (pf - 2) / (pf - 1) ** 2))
check("2C_2 (primes to 10^7)", 2 * C2, 1.3203, 5e-5)
check("C_2", C2, 0.66, 5e-3)
def S(d, C2=C2):
    if d % 2: return 0.0
    r = 2 * C2
    for p in sympy.primefactors(d):
        if p > 2: r *= (p - 1) / (p - 2)
    return r
check("S({0,6})", S(6), 2.64, 5e-3)
check("S({0,30})", S(30), 3.52, 5e-3)

# Gallagher sums: sum_{d<=h} S({0,d}) - h
H = 10 ** 5
fac = np.ones(H + 1)
for p in P[1:]:
    if p > H: break
    fac[p::p] *= (p - 1) / (p - 2)
Sd = np.zeros(H + 1); Sd[2::2] = 2 * C2 * fac[2::2]
cs = np.cumsum(Sd)
for e, printed in ((2, -2.8), (3, -3.9), (4, -4.9), (5, -6.2)):
    h = 10 ** e
    check(f"Gallagher sum minus h at h=10^{e}", cs[h] - h, printed, 0.05)
    print(f"      (-1/2 log h = {-0.5*math.log(h):.2f})")

# Twins and sexy pairs below 10^7
s = np.zeros(10 ** 7 + 7, dtype=bool); s[P] = True
tw = int(np.sum(s[P[P <= 10 ** 7 - 2] + 2]))
check("twin pairs (p, p+2), p+2 <= 10^7", tw, 58980, 0)
sx = int(np.sum(s[P + 6]))
check("pairs (p, p+6), p <= 10^7", sx, 117207, 0)
check("ratio sexy/twins", sx / tw, 1.99, 5e-3)
n = np.arange(3, 10 ** 7 + 1, dtype=np.float64)
model = float(np.sum(1 / (np.log(n) * np.log(n + 2))))
check("Cramer model twins below 10^7", model, 44500, 300)

# Poisson figure: ]10^9, 10^9 + 21*10^6], blocks of 21
A, L = 10 ** 9, 21 * 10 ** 6
seg = np.ones(L, dtype=bool)            # seg[i] <-> A+1+i
for p in primes_upto(int(math.isqrt(A + L)) + 1):
    p = int(p); start = (-(A + 1)) % p
    seg[start::p] = False
cnt = seg.reshape(-1, 21).sum(axis=1)
check("number of blocks", len(cnt), 10 ** 6, 0)
check("mean count per block", cnt.mean(), 1.013, 5e-4)
check("variance of count per block", cnt.var(), 0.79, 5e-3)
check("log 10^9", math.log(1e9), 20.7, 0.05)
c = GAMMA + math.log(2 * math.pi) - 1
check("gamma + log 2pi - 1", c, 1.415, 5e-4)
check("Montgomery-Soundararajan variance", 1.013 * (1 - (math.log(21) + 1.415) / 20.7), 0.79, 5e-3)
print("   empty blocks: data %.4f, Poisson %.4f" % ((cnt == 0).mean(), math.exp(-cnt.mean())))

# Hawkins recursion: 1/q_n - log n
q, inv = 1.0, 1.0
N = 10 ** 7
for k in range(2, N):
    inv += 1 / (k - q); q = 1 / inv
check("Hawkins limit 1/q_n - log n (n=10^7)", inv - math.log(N), 1.2400, 5e-4)

# Last digit of the next prime, after a prime ending in 1, 7 <= p < 10^8
Q = primes_upto(10 ** 8)
Q = Q[Q >= 7]
a, b = Q[:-1], Q[1:]
m = (a % 10 == 1) & (b < 10 ** 8)
nxt = b[m] % 10
tot = m.sum()
for dgt, printed in ((1, 17.7), (3, 30.4), (7, 31.0), (9, 20.9)):
    check(f"frequency 1 -> {dgt} (%)", 100 * np.mean(nxt == dgt), printed, 0.05)
qq = 2.5 / np.log(a[m].astype(np.float64))
den = 1 - (1 - qq) ** 4
for j, dgt, printed in ((1, 3, 31.1), (2, 7, 26.6), (3, 9, 22.8), (4, 1, 19.5)):
    check(f"model 1 -> {dgt} (%)", 100 * np.mean(qq * (1 - qq) ** (j - 1) / den), printed, 0.05)
finish()
