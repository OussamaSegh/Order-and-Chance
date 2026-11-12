"""Number checks for Volume 6, Chapter 11 (exponential and character sums)."""
import math
import numpy as np
import sympy
from common import primes_upto, check, check_true, finish

def powmod(a, e, m):
    """Vectorised a**e mod m for int64 arrays with m < 3*10^9 (products stay below 2^63)."""
    a = np.asarray(a, dtype=np.int64) % m; r = np.ones_like(a); e = np.asarray(e, dtype=np.int64).copy()
    m = np.asarray(m, dtype=np.int64)
    while np.any(e > 0):
        odd = (e & 1) == 1
        r = np.where(odd, (r * a) % m, r)
        a = (a * a) % m; e >>= 1
    return r

check("1/(2 sqrt e), printed truncated as 0.3032...", math.floor(1e4 / (2 * math.sqrt(math.e))) / 1e4, 0.3032, 1e-9)
check("1/(4 sqrt e) < 0.16", 1 / (4 * math.sqrt(math.e)), 0.1516, 5e-5)

# Figure fig:curlicue: alpha = sqrt2/2, N = 2000
n = np.arange(1, 2001, dtype=np.float64)
S = np.sum(np.exp(2j * np.pi * (math.sqrt(2) / 2) * n * n))
check("curlicue end distance, alpha=sqrt2/2, N=2000", abs(S), 36, 0.5)
check("sqrt 2000", math.sqrt(2000), 45, 0.5)

# Exercise ex:weylsqrt2
for N, printed in ((10**3, 16.5), (10**4, 98.6), (10**5, 132.6)):
    m = np.arange(1, N + 1, dtype=np.float64)
    # reduce sqrt2*m^2 mod 1 exactly enough: use integers for m^2 and high-precision sqrt2 split
    m2 = (np.arange(1, N + 1, dtype=np.int64)) ** 2
    hi, lo = 1.4142135623730951, -9.667293313452913e-17
    frac = (m2 * hi) % 1.0 + m2 * lo
    val = abs(np.sum(np.exp(2j * np.pi * frac)))
    check(f"|sum e(sqrt2 n^2)| at N={N}", val, printed, 0.05)
    check_true(f"below sqrt(N log N) at N={N}", val < math.sqrt(N * math.log(N)))

# Polya-Vinogradov example, p = 1000003
p = 1000003
assert sympy.isprime(p)
a = np.arange(1, p, dtype=np.int64)
chi = powmod(a, (p - 1) // 2, p); chi = np.where(chi == 1, 1, -1)
ps = np.concatenate(([0], np.cumsum(chi)))
mx = int(ps.max() - ps.min())
check("largest interval character sum, p=1000003", mx, 1205, 0)
check("ratio to sqrt p", mx / math.sqrt(p), 1.2, 0.05)

# least non-residues n(p), p < 10^8
P = primes_upto(10 ** 8)
odd = P[1:]
npv = np.zeros(len(odd), dtype=np.int64)
rem = np.arange(len(odd))
Q = list(primes_upto(200))
for q in Q:
    pp = odd[rem]
    isnon = powmod(np.full(len(pp), q), (pp - 1) // 2, pp) == pp - 1
    npv[rem[isnon]] = q
    rem = rem[~isnon]
    if len(rem) == 0: break
check_true("every n(p) found below 200", len(rem) == 0)
m6 = odd < 10 ** 6
i = np.argmax(npv[m6]); 
check("record n(p), p<10^6", npv[m6][i], 43, 0); check("... at p", odd[m6][i], 366791, 0)
check("exponent log 43 / log 366791", math.log(43) / math.log(366791), 0.29, 5e-3)
check("largest n(p), p<10^8", npv.max(), 67, 0)
check("... at p", odd[np.argmax(npv)], 48473881, 0)
for e, printed in ((4, 3.4943), (5, 3.6004), (6, 3.6461), (7, 3.6631), (8, 3.6706)):
    x = 10 ** e
    sel = odd <= x   # mean over the odd primes p <= x
    check(f"untruncated mean n(p) over odd p <= 10^{e}", npv[sel].mean(), printed, 5e-5)
pi8 = len(P)
for q, printed in ((2, 0.500061), (3, 0.250012), (5, 0.125011), (7, 0.062525), (11, 0.031265), (13, 0.015576), (17, 0.007857)):
    check(f"proportion n(p)={q} below 10^8", np.sum(npv == q) / pi8, printed, 5e-7)
Y = math.log(1e8) / 3
check("log(10^8)/3", Y, 6.14, 5e-3)
check("primes with n(p) > log x/3", int(np.sum(npv > Y)), 719697, 0)
check("truncated mean at 10^8", np.minimum(npv, Y).sum() / pi8, 3.1422, 5e-5)
check("2/2+3/4+5/8+6.14/8", 1 + .75 + .625 + 6.14 / 8, 3.1425, 5e-5)
pk = list(sympy.primerange(2, 2000))
check("E = sum p_k/2^k", sum(q / 2 ** (k + 1) for k, q in enumerate(pk)), 3.67464, 5e-6)

# least primitive roots, p < 10^6
recs, best, worst = [], 0, 0.0
for p in map(int, primes_upto(10 ** 6)[1:]):
    fs = sympy.primefactors(p - 1)
    g = 2
    while any(pow(g, (p - 1) // f, p) == 1 for f in fs): g += 1
    if g > best: best = g; recs.append((p, g))
    if p > 1000:
        phi = p - 1
        for f in fs: phi = phi // f * (f - 1)
        bound = 2 ** len(fs) * (p - 1) / phi * math.sqrt(p) * (1 + math.log(p)) + 1
        worst = max(worst, g / bound)
printed = [(3, 2), (7, 3), (23, 5), (41, 6), (71, 7), (191, 19), (409, 21), (2161, 23), (5881, 31), (36721, 37), (55441, 38), (71761, 44), (110881, 69), (760321, 73)]
check_true("records of g(p) below 10^6 match the list", recs == printed)
if recs != printed: print(recs)
check_true("g(p) <= 0.0055 * bound for 1000<p<10^6", worst <= 0.0055)
print(f"   worst ratio {worst:.5f}")
p = 999983
check_true("sqrt p (1+log p) > 10^4 near 10^6", math.sqrt(p) * (1 + math.log(p)) > 1e4)
finish()
