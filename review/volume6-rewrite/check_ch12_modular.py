"""Number checks for Volume 6, Chapter 12 (modular forms and the closing problems).

Runs in several minutes: it sieves to 10^8 (omega, sums of two squares, Pi(x) - li(x)).
Needs python-flint (Delta to q^50000), scipy (li) and mpmath.
"""
import math, sys
from fractions import Fraction
from functools import lru_cache
import numpy as np
import sympy, mpmath, flint
from scipy.special import expi
from common import GAMMA, primes_upto, check, check_true, finish

sys.setrecursionlimit(100000)
def powmod(a, e, m):
    a = np.asarray(a, dtype=np.int64) % m; r = np.ones_like(a); e = np.asarray(e, dtype=np.int64).copy()
    while np.any(e > 0):
        odd = (e & 1) == 1
        r = np.where(odd, (r * a) % m, r); a = (a * a) % m; e >>= 1
    return r
def sigma(k, n): return sum(d ** k for d in sympy.divisors(n))
def trunc(name, value, printed):
    """A value printed as 'printed\\ldots': its digits are the truncation of the true value."""
    nd = len(str(printed).split('.')[1])
    check(name + " (truncated digits)", math.floor(value * 10 ** nd) / 10 ** nd, printed, 10 ** -(nd + 3))

# ---------------- main text ----------------
NT = 50001
eta3 = [0] * NT                      # prod (1-q^n)^3 = sum (-1)^k (2k+1) q^{k(k+1)/2}
k = 0
while k * (k + 1) // 2 < NT:
    eta3[k * (k + 1) // 2] = (-1) ** k * (2 * k + 1); k += 1
P = flint.fmpz_poly(eta3)
def mullow(a, b): return flint.fmpz_poly((a * b).coeffs()[:NT])
P2 = mullow(P, P); P4 = mullow(P2, P2); P8 = mullow(P4, P4)
c = P8.coeffs()
tau = [0] + [int(c[n - 1]) for n in range(1, NT)]      # tau(n) = coefficient of q^{n-1} in prod^24
check_true("tau(1..5) = 1, -24, 252, -1472, 4830", tau[1:6] == [1, -24, 252, -1472, 4830])
check_true("tau(6) = -6048 = tau(2) tau(3)", tau[6] == -6048 == tau[2] * tau[3])
check_true("tau(n) = sigma_11(n) mod 691 for n <= 2000", all((tau[n] - sigma(11, n)) % 691 == 0 for n in range(1, 2001)))
check_true("Mordell relation tau(p)tau(n) = tau(pn) + p^11 tau(n/p), p<=7, pn<=5000",
           all(tau[p] * tau[n] == tau[p * n] + (p ** 11 * tau[n // p] if n % p == 0 else 0)
               for p in (2, 3, 5, 7) for n in range(1, 5000 // p + 1)))
B = {4: Fraction(-1, 30), 6: Fraction(1, 42), 8: Fraction(-1, 30), 10: Fraction(5, 66), 12: Fraction(-691, 2730)}
check_true("Bernoulli numbers B_4..B_12", all(sympy.bernoulli(k) == sympy.Rational(B[k].numerator, B[k].denominator) for k in B))
coef = {k: -2 * k / B[k] for k in B}
check_true("E_k coefficients 240, -504, 480, -264, 65520/691",
           [coef[k] for k in (4, 6, 8, 10, 12)] == [240, -504, 480, -264, Fraction(65520, 691)])
check_true("sigma_7(2) = sigma_3(2) + 120 sigma_3(1)^2: 129 = 9 + 120", sigma(7, 2) == 129 == sigma(3, 2) + 120)
check_true("720 + 1008 = 1728 and 720 - 65520/691 = 432000/691", 720 + 1008 == 1728 and 720 - Fraction(65520, 691) == Fraction(432000, 691))
check_true("65520 = 566 = -125 and 432000 = 125 mod 691", 65520 % 691 == 566 and (566 + 125) % 691 == 0 and 432000 % 691 == 125)
check_true("ex:sigma9 identity, n <= 60", all(11 * sigma(9, n) == 21 * sigma(5, n) - 10 * sigma(3, n) + 5040 * sum(sigma(3, m) * sigma(5, n - m) for m in range(1, n)) for n in range(1, 61)))
check_true("E_4^3 - E_6^2 starts 1728 q", 3 * 240 + 2 * 504 == 1728)
ps = [p for p in sympy.primerange(2, 50001)]
check("number of primes <= 50000", len(ps), 5133, 0)
xp = [tau[p] / (2 * p ** 5.5) for p in ps]
check("largest |x_p|, p <= 50000", max(abs(v) for v in xp), 0.990, 5e-4)
check_true("all |x_p| <= 1 (Deligne)", max(abs(v) for v in xp) <= 1)

# ---------------- problems ----------------
# pb:singer (c)
for D, N in (({0, 1, 3}, 7), ({0, 1, 3, 9}, 13), ({0, 1, 4, 14, 16}, 21)):
    diffs = sorted((a - b) % N for a in D for b in D if a != b)
    check_true(f"perfect difference set mod {N}", diffs == list(range(1, N)))
PR = primes_upto(10 ** 7); pf = PR.astype(np.float64)
prodp = lambda f: float(np.exp(np.sum(np.log(f(pf)))))
check("prod (1-2/p^2)", prodp(lambda p: 1 - 2 / p ** 2), 0.3226, 5e-5)
trunc("prod (1-3/p^2)", prodp(lambda p: 1 - 3 / p ** 2), 0.1254)
trunc("prod_{p<=13} (1-2/p^2)", float(np.prod([1 - 2 / p ** 2 for p in (2, 3, 5, 7, 11, 13)])), 0.33350)
P2sum = float(mpmath.primezeta(2))
check("prime zeta P(2)", P2sum, 0.452247, 5e-7)
trunc("sum_{p>=17} p^-2", P2sum - sum(1 / p ** 2 for p in (2, 3, 5, 7, 11, 13)), 0.016546)
check_true("0.3335 - 0.0331 >= 0.30 and 4097/0.30 < 13657", 0.3335 - 0.0331 >= 0.30 and 4097 / 0.30 < 13657)
X = 10 ** 7
sqf = np.ones(X + 1, dtype=bool); sqf[0] = False
for p in PR[PR <= int(math.isqrt(X))]: sqf[int(p) * int(p)::int(p) * int(p)] = False
run = np.convolve((~sqf[1:2001]).astype(int), np.ones(4, dtype=int), 'valid')
check("first run of 4 non-squarefree starts at", int(np.argmax(run == 4)) + 1, 242, 0)
ok = all(any(sqf[a] and sqf[n - a] for a in range(1, n)) for n in range(2, 14000))
check_true("every 2 <= n < 14000 is a sum of two squarefree integers", ok)
for kk, printed in ((3, 0.2867), (4, 0.1149)):
    check(f"pairwise coprime probability k={kk}", prodp(lambda p: (1 - 1 / p) ** (kk - 1) * (1 + (kk - 1) / p)), printed, 5e-5)
check("(6/pi^2)^3", (6 / math.pi ** 2) ** 3, 0.2247, 5e-5)
# pb:dsquared
x5 = 10 ** 5
d = np.zeros(x5 + 1, dtype=np.int64)
for kk in range(1, x5 + 1): d[kk::kk] += 1
check("sum d(n)^2 / (x log^3 x) at 10^5", float(np.sum(d[1:] ** 2)) / (x5 * math.log(x5) ** 3), 0.17, 5e-3)
check("1/pi^2", 1 / math.pi ** 2, 0.101, 5e-4)
check("delta = 1 - (1+loglog2)/log2", 1 - (1 + math.log(math.log(2))) / math.log(2), 0.086, 5e-4)
# pb:chebyshevsum
check("M_1 = 6/pi^2", 6 / math.pi ** 2, 0.6079, 5e-5)
check("M_2 = prod(1 - 2/p^2 + 1/p^3)", prodp(lambda p: 1 - 2 / p ** 2 + 1 / p ** 3), 0.4282, 5e-5)
check("M_1^2", (6 / math.pi ** 2) ** 2, 0.3696, 5e-5)
phi = np.arange(10 ** 6 + 1, dtype=np.float64)
for p in PR[PR <= 10 ** 6]: phi[int(p)::int(p)] *= (1 - 1 / p)
r = phi[1:] / np.arange(1, 10 ** 6 + 1)
check("mean of (phi(n)/n)^2 up to 10^6", float(np.mean(r ** 2)), 0.4282, 5e-4)
# pb:primitive leads
tail = 1 / math.log(1e7)
check("sum_{p<=10^7} 1/(p log p) + tail 1/log(10^7)", float(np.sum(1 / (pf * np.log(pf)))) + tail, 1.6366, 2e-3)
# pb:divisorbound
check("2520^(1/3) ratio d/n^(1/3)", 48 / 2520 ** (1 / 3), 3.527, 5e-4)
dd = np.zeros(10 ** 6 + 1, dtype=np.int64)
for kk in range(1, 10 ** 6 + 1): dd[kk::kk] += 1
rat = dd[1:] / np.arange(1, 10 ** 6 + 1) ** (1 / 3)
check("argmax d(n)/n^(1/3), n <= 10^6", int(np.argmax(rat)) + 1, 2520, 0)
n14 = 2 ** 5 * 3 ** 3 * 5 ** 2 * 7 * 11 * 13
check("n_{1/4}", n14, 21621600, 0); check("d(n_{1/4})", int(sympy.divisor_count(n14)), 576, 0)
trunc("576 / n_{1/4}^{1/4}", 576 / n14 ** 0.25, 8.446)
def best(alpha, bound=60):
    v = 1.0
    for p in sympy.primerange(2, bound):
        v *= max((e + 1) / p ** (e * alpha) for e in range(0, 40))
    return v
check("max d(n)/n^(1/4) = product formula", best(0.25), 576 / n14 ** 0.25, 1e-9)
# irrationality measures
check("4(3-2sqrt2)", 4 * (3 - 2 * math.sqrt(2)), 0.686, 5e-4)
L = math.log(3 + 2 * math.sqrt(2))
check("mu for log 2", 1 + (1 + L) / (L - 1), 4.62, 5e-3)
tg = (math.sqrt(5) - 1) / 2
check("9 tau^5", 9 * tg ** 5, 0.81, 5e-3)
check("27 (sqrt2-1)^4", 27 * (math.sqrt(2) - 1) ** 4, 0.79, 5e-3)
check_true("sum_k C(n,k)^2 C(n+k,k) = 1,3,19,147,1251", [sum(math.comb(n, kk) ** 2 * math.comb(n + kk, kk) for kk in range(n + 1)) for n in range(5)] == [1, 3, 19, 147, 1251])
check_true("Apery numbers 1,5,73,1445", [sum(math.comb(n, kk) ** 2 * math.comb(n + kk, kk) ** 2 for kk in range(n + 1)) for n in range(4)] == [1, 5, 73, 1445])
u2 = [sum(math.comb(n, kk) ** 2 * math.comb(n + kk, kk) for kk in range(n + 1)) for n in range(30)]
check_true("n^2 u_n = (11n^2-11n+3) u_{n-1} + (n-1)^2 u_{n-2}", all(n * n * u2[n] == (11 * n * n - 11 * n + 3) * u2[n - 1] + (n - 1) ** 2 * u2[n - 2] for n in range(2, 30)))
u3 = [sum(math.comb(n, kk) ** 2 * math.comb(n + kk, kk) ** 2 for kk in range(n + 1)) for n in range(30)]
check_true("n^3 u_n = (34n^3-51n^2+27n-5) u_{n-1} - (n-1)^3 u_{n-2}", all(n ** 3 * u3[n] == (34 * n ** 3 - 51 * n * n + 27 * n - 5) * u3[n - 1] - (n - 1) ** 3 * u3[n - 2] for n in range(2, 30)))
xmax = max(x * (1 - x) * y * (1 - y) / (1 - x * y) for x in np.linspace(0, 1, 801)[:-1] for y in np.linspace(0, 1, 801)[:-1])
check_true("max x(1-x)y(1-y)/(1-xy) <= tau^5", xmax <= tg ** 5 + 1e-12)
trunc("log(2pi) - gamma - 1", math.log(2 * math.pi) - GAMMA - 1, 0.2606)
trunc("C = sum (1/k) log(1+1/k)", float(mpmath.nsum(lambda k: mpmath.log(1 + 1 / k) / k, [1, mpmath.inf])), 1.25774)
trunc("e^C", math.exp(float(mpmath.nsum(lambda k: mpmath.log(1 + 1 / k) / k, [1, mpmath.inf]))), 3.5174)
# pb:leastpf
x = 10 ** 7
s = int(np.sum(PR))
check("sum of primes <= 10^7", s, 3203324994356, 0)
check("ratio to x^2/(2 log x)", s / (x * x / (2 * math.log(x))), 1.0326, 5e-5)
check("ratio to Li(x^2)", s / float(mpmath.li(1e14) - mpmath.li(2)), 0.99950, 5e-6)
check("1/(2 log 10^7) = 3.1%", 100 / (2 * math.log(x)), 3.1, 0.05)
# pb:largestpf
lpf = np.zeros(X + 1, dtype=np.int64)
for p in PR: lpf[int(p)::int(p)] = int(p)
sP = float(np.sum(lpf[2:]))
check("sum P+(n) ratio to pi^2/12 x^2/log x", sP / (math.pi ** 2 / 12 * x * x / math.log(x)), 1.0767, 5e-5)
# pb:factorialdiv
for e, printed in ((4, 1.58), (5, 1.51), (6, 1.45), (7, 1.42)):
    n = 10 ** e; pp = PR[PR <= n]
    v = np.zeros(len(pp), dtype=np.int64); pk = pp.copy()
    while True:
        m = pk <= n
        if not m.any(): break
        v[m] += n // pk[m]; pk = np.where(m, pk * pp, n + 1)
    val = float(np.sum(np.log1p(v))) / (n / math.log(n))
    check(f"log tau(n!)/(n/log n) at 10^{e}", val, printed, 5e-3)
    if e in (4, 7): check(f"excess over C at 10^{e}", val - 1.2577468869, {4: 0.33, 7: 0.16}[e], 5e-3); check(f"3/log n at 10^{e}", 3 / math.log(n), {4: 0.33, 7: 0.19}[e], 5e-3) if e else None
# pb:centralbinom
n = 5 * 10 ** 6; pp = PR[PR <= 2 * n]
v = np.zeros(len(pp), dtype=np.int64); pk = pp.copy()
while True:
    m = pk <= 2 * n
    if not m.any(): break
    v[m] += (2 * n) // pk[m] - 2 * (n // pk[m]); pk = np.where(m, pk * pp, 2 * n + 1)
w = int(np.sum(v > 0))
check("omega(binom(2n,n)), n=5*10^6", w, 453587, 0)
check("log4 n/log n", math.log(4) * n / math.log(n), 449368, 0.5)
check("ratio", w / (math.log(4) * n / math.log(n)), 1.0094, 5e-5)
# pb:superprimes
P8 = primes_upto(10 ** 8)
idx = P8[P8 <= len(P8)] - 1          # p_{p_n} for p_n <= pi(10^8)
spr = P8[idx]
check_true("p_{p_n} start 3,5,11,17,31,41,59", list(spr[:7]) == [3, 5, 11, 17, 31, 41, 59])
check("pi(pi(10^8))", len(spr), 397557, 0)
check("ratio to x/log^2 x", len(spr) / (1e8 / math.log(1e8) ** 2), 1.349, 5e-4)
check("partial sum of 1/p_{p_n} up to 10^8", float(np.sum(1 / spr.astype(np.float64))), 0.9833, 5e-5)
check("1/log(397557)", 1 / math.log(397557), 0.078, 5e-4)
y = 5761455
check("pi(10^8)", len(P8), y, 0)
check("y/log y (1 + 1/log y)", y / math.log(y) * (1 + 1 / math.log(y)), 393900, 50)
check("x/log^2 x", 1e8 / math.log(1e8) ** 2, 294700, 50)
# pb:ramprimes
M = 10 ** 6
pic = np.zeros(M + 1, dtype=np.int64); pic[P8[P8 <= M]] = 1; pic = np.cumsum(pic)
f = pic[np.arange(M + 1)] - pic[np.arange(M + 1) // 2]
def Rn(n):
    last = np.nonzero(f < n)[0].max()
    return int(last + 1)
check_true("R_1..R_5 = 2, 11, 17, 29, 41", [Rn(n) for n in range(1, 6)] == [2, 11, 17, 29, 41])
check("R_10000", Rn(10000), 242057, 0)
check("p_20000", int(P8[19999]), 224737, 0)
check("log p_20000", math.log(224737), 12.32, 5e-3)
check("1 + log2/12.32", 1 + math.log(2) / 12.32, 1.056, 5e-4)
check("242057/224737", 242057 / 224737, 1.077, 5e-4)
# pb:pminusone
A = prodp(lambda q: 1 - 1 / (q * (q - 1)))
check("Artin's constant", A, 0.3739558, 5e-7)
spf = np.zeros(X + 1, dtype=np.int64)
for p in PR[::-1]: spf[int(p)::int(p)] = int(p)
odd = PR[1:]
m = odd - 1; isroot = np.ones(len(odd), dtype=bool)
while np.any(m > 1):
    act = m > 1
    q = np.where(act, spf[np.where(act, m, 2)], 1)
    test = act & (powmod(np.full(len(odd), 2), (odd - 1) // np.where(act, q, 1), odd) == 1)
    isroot &= ~test
    while True:
        dv = act & (m % np.where(act, q, 1) == 0) & (m > 1)
        if not dv.any(): break
        m = np.where(dv, m // np.where(act, q, 1), m)
check("odd primes below 10^7", len(odd), 664578, 0)
check("2 primitive root modulo how many", int(isroot.sum()), 248491, 0)
check("proportion", isroot.sum() / len(odd), 0.37391, 5e-6)
# pb:titchmarsh
Z = float(mpmath.zeta(2) * mpmath.zeta(3) / mpmath.zeta(6))
trunc("Z = zeta(2)zeta(3)/zeta(6)", Z, 1.94359)
check("B = prod (1 + 1/(q-1)^2)", prodp(lambda q: 1 + 1 / (q - 1) ** 2), 2.82642, 2e-5)
dX = np.zeros(X + 1, dtype=np.int32)
for kk in range(1, X // 2 + 1): dX[kk::kk] += 1
dX[X // 2 + 1:] += 1   # the loop counted the divisors k <= X/2; for n > X/2 add the divisor n itself
for e, printed in ((5, 1.916), (6, 1.927), (7, 1.932)):
    xx = 10 ** e; pp = PR[PR <= xx]
    check(f"(1/x) sum tau(p-1), x=10^{e}", float(np.sum(dX[pp[1:] - 1]) + 1) / xx, printed, 5e-4)
# pb:menon
P6 = PR[PR < 10 ** 6]
for n, printed in ((12, 5.994), (24, 7.982), (60, 11.978)):
    check(f"average gcd(n, p-1), n={n}", float(np.mean(np.gcd(n, P6 - 1))), printed, 5e-4)
# pb:omegapoly
for e, printed in ((4, 0.598), (5, 0.603), (6, 0.606)):
    xx = 10 ** e
    nn = np.arange(1, xx + 1, dtype=np.int64); val = nn * nn + 1; om = np.zeros(xx, dtype=np.int64)
    for p in PR[PR <= xx]:
        p = int(p)
        if p == 2: roots = [1]
        elif p % 4 == 1: rr = sympy.sqrt_mod(-1, p); roots = [rr, p - rr]
        else: continue
        for r0 in roots:
            idx = np.arange((r0 - 1) % p, xx, p)
            om[idx] += 1
            while True:
                dv = idx[val[idx] % p == 0]
                if len(dv) == 0: break
                val[dv] //= p; idx = dv
    om += (val > 1)
    check(f"(1/x) sum omega(n^2+1) - loglog x, x=10^{e}", om.mean() - math.log(math.log(xx)), printed, 5e-4)
# pb:rankin
PRk = list(sympy.primerange(2, 1001))
@lru_cache(maxsize=None)
def Psi(x, k):
    if k == 0 or x < 2: return 1 if x >= 1 else 0
    p = PRk[k - 1]
    if p >= x: return x
    if k == 1: return x.bit_length()
    return Psi(x, k - 1) + Psi(x // p, k)
check("Psi(10^10, 100)", Psi(10 ** 10, 25), 8800084, 0)
Psi1 = Psi(10 ** 12, 168)
check("Psi(10^12, 1000)", Psi1, 6471274933, 0)
Psi.cache_clear()
def rankin(x, y):
    pl = np.array(list(sympy.primerange(2, y + 1)), dtype=np.float64)
    return min(x ** s * float(np.prod(1 / (1 - pl ** (-s)))) for s in np.linspace(0.3, 1, 7001))
r1, r2 = rankin(1e10, 100), rankin(1e12, 1000)
check("best Rankin bound 10^10, 100", r1 / 1e7, 9.95, 5e-3)
check("best Rankin bound 10^12, 1000", r2 / 1e11, 1.26, 5e-3)
check("factor 1", r1 / 8800084, 11.3, 0.05); check("factor 2", r2 / Psi1, 19.4, 0.05)
# pb:renyi
check("mean sum 1/(p(p-1))", float(np.sum(1 / (pf * (pf - 1)))), 0.77315, 2e-5)
check("C_2", prodp(lambda p: np.where(p > 2, 1 - 1 / (p - 1) ** 2, 1.0)), 0.66016, 5e-5)
C2 = prodp(lambda p: np.where(p > 2, 1 - 1 / (p - 1) ** 2, 1.0))
check("1/(4 C_2)", 1 / (4 * C2), 0.37869, 5e-5)
K = 12; ser = np.zeros(K); ser[0] = 1.0
for p in PR[PR < 10 ** 6]:
    p = float(p); fac = np.array([(1 - 1 / p) * (1 + 1 / p)] + [(1 - 1 / p) * p ** (-j - 1) for j in range(1, K)])
    ser = np.convolve(ser, fac)[:K]
check("d_0 = 6/pi^2", ser[0], 6 / math.pi ** 2, 1e-6)
for kk, printed in ((1, 0.200756), (2, 0.096302), (3, 0.047615)):
    check(f"d_{kk}", ser[kk], printed, 2e-6)
Om = np.zeros(X + 1, dtype=np.int8); omg = np.zeros(X + 1, dtype=np.int8)
for p in PR:
    p = int(p); omg[p::p] += 1; pk = p
    while pk <= X: Om[pk::pk] += 1; pk *= p
diff = (Om[1:] - omg[1:])
for kk, printed in ((1, 0.200758), (2, 0.096306), (3, 0.047616)):
    check(f"proportion Omega-omega={kk} up to 10^7", float(np.mean(diff == kk)), printed, 5e-7)
check("2^11 d_11 -> 1/(4 C_2)", 2 ** 11 * ser[11], 1 / (4 * C2), 1e-4)
# pb:twosquares
N8 = 10 ** 8
b = np.zeros(N8 + 1, dtype=bool)
for a in range(0, math.isqrt(N8) + 1):
    bmax = min(a, math.isqrt(N8 - a * a))
    bb = np.arange(0, bmax + 1, dtype=np.int64); b[a * a + bb * bb] = True
b[0] = False
B8 = int(b.sum())
check("B(10^8)", B8, 18457847, 0)
check("B(x) sqrt(log x)/x", B8 * math.sqrt(math.log(N8)) / N8, 0.7922, 5e-5)
p3 = pf[pf % 4 == 3]
pr3 = float(np.prod(1 / (1 - p3 ** -2.0)))
check("prod_{p=3(4)} (1-p^-2)^-1", pr3, 1.168076, 5e-6)
C = math.sqrt(math.pi / 2 * pr3)
check("C", C, 1.35455, 5e-6); check("K = C/sqrt(pi)", C / math.sqrt(math.pi), 0.764224, 5e-6)
check("0.7922/K", 0.7922 / (C / math.sqrt(math.pi)), 1.037, 5e-4)
check("1 - sqrt2 e^-1/2", 1 - math.sqrt(2) * math.exp(-0.5), 0.142, 5e-4)
del b
# pb:ramanujanE2 (f)
s7 = sum(sigma(1, m) * sigma(1, 7 - m) for m in range(1, 7))
check("sum sigma(m)sigma(7-m)", s7, 6 * (5 * 49 - 7 - 6) // 12, 0)
check_true("sigma(1..6) = 1,3,4,7,6,12", [sigma(1, m) for m in range(1, 7)] == [1, 3, 4, 7, 6, 12])
check_true("pb:ramanujanE2 (d),(e) for n <= 40", all(12 * sum(sigma(1, m) * sigma(1, n - m) for m in range(1, n)) == 5 * sigma(3, n) + (1 - 6 * n) * sigma(1, n)
           and 240 * sum(sigma(1, m) * sigma(3, n - m) for m in range(1, n)) == 21 * sigma(5, n) + (10 - 30 * n) * sigma(3, n) - sigma(1, n) for n in range(1, 41)))
# pb:hearzeros
zs = [float(mpmath.zetazero(n).imag) for n in range(1, 41)]
check_true("tick values 14.13 ... 49.77", [round(z, 2) for z in zs[:10]] == [14.13, 21.02, 25.01, 30.42, 32.94, 37.59, 40.92, 43.33, 48.01, 49.77])
check("gap 49.77 - 48.01 (unrounded)", zs[9] - zs[8], 1.77, 5e-3)
check("gap / s", (zs[9] - zs[8]) / 0.6, 2.9, 0.05)
sv = 0.6
lam = [(n, math.log(int(sympy.factorint(n).popitem()[0]))) for n in range(2, int(math.exp(10)) + 1) if len(sympy.factorint(n)) == 1]
def rhs(T):
    return sv / math.sqrt(2 * math.pi) * math.log(T / (2 * math.pi)) - 2 * sv / math.sqrt(2 * math.pi) * sum(l / math.sqrt(n) * math.cos(T * math.log(n)) * math.exp(-sv * sv * math.log(n) ** 2 / 2) for n, l in lam)
def lhs(T): return sum(math.exp(-(g - T) ** 2 / (2 * sv * sv)) for g in zs)
dev = max(abs(rhs(T) - lhs(T)) for T in np.linspace(5, 50, 451))
check_true(f"prime side agrees with zero side on [5,50] within 0.003 (max {dev:.4f})", dev <= 0.003)
termmax = 2 * sv / math.sqrt(2 * math.pi) * max(math.log(n) / math.sqrt(n) * math.exp(-sv * sv * math.log(n) ** 2 / 2) for n in range(int(math.exp(10)) + 1, int(math.exp(10)) + 50))
check_true(f"terms with n > e^10 below 1e-9 (largest {termmax:.2e})", termmax < 1e-9)
# pb:cramersign
P8f = P8.astype(np.float64)
li = lambda t: expi(np.log(t))
pk_pts, pk_w = [P8f], [np.ones(len(P8f))]
for kk in range(2, 27):
    q = P8f[P8f ** kk <= 1e8] ** kk
    if len(q) == 0: break
    pk_pts.append(q); pk_w.append(np.full(len(q), 1 / kk))
pts = np.concatenate(pk_pts); wts = np.concatenate(pk_w); o = np.argsort(pts); pts, wts = pts[o], wts[o]
Pi_after = np.cumsum(wts); Pi_before = Pi_after - wts
F_before = Pi_before - li(pts); F_after = Pi_after - li(pts)
seq = np.empty(2 * len(pts)); seq[0::2] = F_before; seq[1::2] = F_after
sg = np.sign(seq[1:])            # start just after the jump at 2
changes = int(np.sum(sg[1:] != sg[:-1]))
check("sign changes of Pi(x) - li(x) below 10^8", changes, 66112, 0)
m3 = pts >= 1e3
scale = np.sqrt(pts) / np.log(pts)
check("inf (Pi-li)/(sqrt x/log x) on [10^3,10^8] (just before a jump)", float(np.min(F_before[m3] / scale[m3])), -0.89, 5e-3)
check("max (Pi-li)/(sqrt x/log x) on [10^3,10^8]", float(np.max(F_after[m3] / scale[m3])), 0.71, 5e-3)
pm = P8f >= 1e3; pi_after = np.arange(1, len(P8f) + 1, dtype=np.float64)
Gb = (pi_after - 1 - li(P8f))[pm] / (np.sqrt(P8f) / np.log(P8f))[pm]
Ga = (pi_after - li(P8f))[pm] / (np.sqrt(P8f) / np.log(P8f))[pm]
check_true("pi(x) < li(x) on [10^3, 10^8]", Ga.max() < 0)
check("inf (pi-li)/(sqrt x/log x) (just before a jump, at 1423)", float(Gb.min()), -2.74, 5e-3)
check("max (pi-li)/(sqrt x/log x)", float(Ga.max()), -0.53, 5e-3)
check("sqrt(x/log x) at 10^8", math.sqrt(1e8 / math.log(1e8)), 2330, 1)
# pb:selberg
theta = np.zeros(X + 1); theta[PR] = np.log(pf); theta = np.cumsum(theta)
for e, printed in ((4, -3.668), (5, -3.667), (6, -3.668), (7, -3.666)):
    xx = 10 ** e; pp = PR[PR <= xx]
    S = theta[xx] * math.log(xx) + float(np.sum(np.log(pp.astype(np.float64)) * theta[xx // pp]))
    check(f"Selberg normalised error at 10^{e}", (S - 2 * xx * math.log(xx)) / xx, printed, 5e-4)
    if e == 7: check("left side / (2x log x) at 10^7", S / (2 * xx * math.log(xx)), 0.886, 5e-4)
# pb:schur
for p, Sp, Lp in ((7, 1, 1.18741), (23, 3, 1.96520), (163, 3, 0.246069), (1019, 39, 1.27940), (10007, 77, 2.41818)):
    chi = [0] + [sympy.legendre_symbol(a, p) for a in range(1, p)]
    S_ = sum(chi[1:(p + 1) // 2]); T_ = sum(a * chi[a] for a in range(1, p))
    Lval = -math.pi * T_ / p ** 1.5
    check(f"S for p={p}", S_, Sp, 0); check(f"L(1,chi) for p={p}", Lval, Lp, 6e-6)
    check(f"formula (e) for p={p}", (2 - chi[2]) * math.sqrt(p) / math.pi * Lval, Sp, 1e-9)
# pb:euler41
rab = [q for q in sympy.primerange(2, 5001) if all(sympy.isprime(n * n + n + q) for n in range(q - 1))]
check_true("Rabinowitsch primes q <= 5000 are 2,3,5,11,17,41", rab == [2, 3, 5, 11, 17, 41])
def kron(p): return int(sympy.jacobi_symbol(-163 % p, p)) if p > 2 else -1
chis = np.array([kron(int(p)) for p in PR[1:10 ** 5]], dtype=np.float64); pq = pf[1:10 ** 5]
Cfast = 4 / 3 * math.sqrt(163) / math.pi * float(np.prod((1 - chis / (pq - 1)) / (1 - chis / pq)))
check("C for n^2+n+41", Cfast, 6.6395, 5e-4)
def polysieve(Nmax, rootsfun, f):
    nn = np.arange(0, Nmax, dtype=np.int64); val = f(nn); isp = val > 1
    lim = int(math.isqrt(int(val.max()))) + 1
    for p in PR[PR <= lim]:
        p = int(p)
        for r0 in rootsfun(p):
            idx = np.arange(r0 % p, Nmax, p)
            isp[idx[val[idx] != p]] = False
    return isp
def roots41(p):
    if p == 2: return []
    if p == 163: return [81]
    if sympy.jacobi_symbol(-163 % p, p) != 1: return []
    s_ = sympy.sqrt_mod(-163, p); inv2 = pow(2, -1, p)
    return list({((-1 + s_) * inv2) % p, ((-1 - s_) * inv2) % p})
isp = polysieve(10 ** 6, roots41, lambda n: n * n + n + 41)
cnt41 = int(isp.sum())
check("primes among n^2+n+41, n < 10^6", cnt41, 261081, 0)
nn = np.arange(0, 10 ** 6, dtype=np.float64)
check("prediction C sum 1/log f(n)", Cfast * float(np.sum(1 / np.log(nn * nn + nn + 41))), 261020, 30)
def roots1(p):
    if p == 2: return [1]
    if p % 4 != 1: return []
    s_ = sympy.sqrt_mod(-1, p); return [s_, p - s_]
isp1 = polysieve(10 ** 6, roots1, lambda n: n * n + 1)
isp1[0] = False
check("primes among n^2+1, 1 <= n < 10^6", int(isp1.sum()), 54110, 0)
chi4 = np.where(pf[1:] % 4 == 1, 1.0, -1.0)
Cp = float(np.prod(1 - chi4 / (pf[1:] - 1)))
check("C' for n^2+1", Cp, 1.3728, 5e-4)
nn1 = np.arange(1, 10 ** 6, dtype=np.float64)
check("prediction C' sum 1/log(n^2+1)", Cp * float(np.sum(1 / np.log(nn1 * nn1 + 1))), 53972, 30)
# pb:hecke
aa, bb_ = [], []
for a in range(1, 3163):
    bmax = min(a - 1, math.isqrt(max(10 ** 7 - 1 - a * a, 0)))
    if bmax < 1: continue
    bs = np.arange(1, bmax + 1); aa.append(np.full(len(bs), a)); bb_.append(bs)
aa = np.concatenate(aa); bb_ = np.concatenate(bb_); nrm = aa * aa + bb_ * bb_
isprime8 = np.zeros(10 ** 7 + 1, dtype=bool); isprime8[PR] = True
sel = isprime8[nrm]; aa, bb_ = aa[sel], bb_[sel]
check("primes p = 1 mod 4 below 10^7", len(aa), 332180, 0)
check_true("that is the count of primes = 1 mod 4", len(aa) == int(np.sum(PR % 4 == 1)))
ph = np.arctan2(bb_, aa)
check("proportion phi_p <= pi/8", float(np.mean(ph <= math.pi / 8)), 0.499795, 5e-7)
check("proportion b < a/10", float(np.mean(10 * bb_ < aa)), 0.12658, 5e-6)
check("Hecke prediction (4/pi) arctan(1/10)", 4 / math.pi * math.atan(0.1), 0.1269, 5e-5)
h, _ = np.histogram(ph, bins=20, range=(0, math.pi / 4)); h = h / (len(ph) / 20)
print(f"   bars from {h.min():.4f} to {h.max():.4f}"); check_true("all bars between 0.990 and 1.007", h.min() >= 0.990 and h.max() <= 1.007)
# pb:shifted
N8 = 10 ** 8
om8 = np.zeros(N8 + 1, dtype=np.int8)
for p in P8: om8[int(p)::int(p)] += 1
w8 = om8[1:].astype(np.float64)
check("mean omega(n), n <= 10^8", w8.mean(), 3.150, 5e-4); check("variance omega(n), n <= 10^8", w8.var(), 1.214, 5e-4)
del w8
check("model mean", float(np.sum(1 / (P8f - 1))), 3.948, 5e-4)
check("model variance", float(np.sum(1 / (P8f - 1) * (1 - 1 / (P8f - 1)))), 2.573, 5e-4)
for e, mp, mm, vv in ((4, 3.027, 0.807, 0.540), (5, 3.298, 0.855, 0.656), (6, 3.518, 0.892, 0.781), (7, 3.696, 0.916, 0.906), (8, 3.847, 0.933, 1.021)):
    xx = 10 ** e; pp = P8[P8 <= xx]; wv = om8[pp - 1].astype(np.float64)
    wv[0] = 0  # p = 2: p-1 = 1
    check(f"mean omega(p-1), 10^{e}", wv.mean(), mp, 5e-4)
    check(f"mean - loglog, 10^{e}", wv.mean() - math.log(math.log(xx)), mm, 5e-4)
    check(f"variance, 10^{e}", wv.var(), vv, 5e-4)
    check(f"deficit from 1.034654, 10^{e}", 1.034654 - (wv.mean() - math.log(math.log(xx))), {4: 0.228, 5: 0.180, 6: 0.142, 7: 0.119, 8: 0.102}[e], 5e-4)
for kk, printed in ((2, 0.0835), (3, 0.2922), (4, 0.3709), (5, 0.2041), (6, 0.0459), (7, 0.0033)):
    check(f"proportion omega(p-1)={kk}", float(np.mean(wv == kk)), printed, 5e-5)
check("Meissel-Mertens + sum 1/(q(q-1))", 0.261497 + 0.773157, 1.034654, 1e-9)
check("loglog 10^8", math.log(math.log(1e8)), 2.91, 5e-3)
del om8
# pb:romanoff
check_true("11184810 = 2*3*5*7*13*17*241", 2 * 3 * 5 * 7 * 13 * 17 * 241 == 11184810)
n0 = 7629217
check_true("n - 2^k always divisible by one of 3,5,7,13,17,241", all(any((n0 - pow(2, kk, 11184810)) % q == 0 for q in (3, 5, 7, 13, 17, 241)) for kk in range(1, 25)))
check_true("orders of 2 modulo 3,5,7,13,17,241 are 2,4,3,12,8,24", [sympy.n_order(2, q) for q in (3, 5, 7, 13, 17, 241)] == [2, 4, 3, 12, 8, 24])
inR = np.zeros(X + 1, dtype=bool)
kk = 1
while 2 ** kk < X:
    t = PR + 2 ** kk; inR[t[t <= X]] = True; kk += 1
for e, pa, po in ((4, 0.475, 0.947), (5, 0.4662, 0.932), (6, 0.4605, 0.921), (7, 0.4578, 0.916)):
    xx = 10 ** e
    check(f"proportion in R, 10^{e}", float(inR[1:xx + 1].mean()), pa, 5e-4 if e > 4 else 5e-4)
    check(f"proportion of odd n in R, 10^{e}", float(inR[1:xx + 1:2].mean()), po, 5e-4)
for Lm, printed in ((10, 2.155), (20, 2.372), (40, 2.487), (80, 2.535)):
    fv = [(Fraction(2 ** m - 1, int(sympy.totient(2 ** m - 1)))) ** 2 for m in range(1, Lm + 1)]
    check(f"(1/L) sum f(m), L={Lm}", float(sum(fv)) / Lm, printed, 5e-4)
finish()
