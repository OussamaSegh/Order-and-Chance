#!/usr/bin/env python3
"""Recompute the printed numbers of Chapter 4 (ra-randommult.tex, ra-polynomials.tex, ch04-multiplicative.tex).

Exact numbers are checked exactly. Monte Carlo numbers (fixed seed) are checked within a tolerance
that is several standard errors wide, since the book prints them as observations of a sample.
Runs in about two minutes.
"""
import math, cmath, numpy as np
from math import gcd
from common import check, check_true, finish, primes_upto

rng = np.random.default_rng(20261113)

# ---------- Theorem fourth moment: exact formula, 16.3 at x = 10^6 ----------
def phi_upto(n):
    ph = np.arange(n + 1, dtype=np.int64)
    for p in primes_upto(n):
        ph[p::p] -= ph[p::p] // p
    return ph

X = 10**6
ph = phi_upto(X)
m = np.arange(1, X + 1)
c = 2 * ph[1:].astype(float); c[0] = 1
fourth = float(np.sum(c * (X // m).astype(float) ** 2)) / X**2
check("E|S(10^6)|^4 / x^2 (exact)", fourth, 16.3, 0.05)
# main term 12/pi^2 log x is a little smaller; the O(x^2) term is positive
print("   12/pi^2 log 10^6 =", 12 / math.pi**2 * math.log(X))

# ---------- Exercise tablelink(b) ----------
c10 = [1] + [2 * int(ph[k]) for k in range(2, 11)]
val = sum(c10[k - 1] * (10 // k) ** 2 for k in range(1, 11))
check("E|S(10)|^4 exact", val, 278, 0)
# brute force: number of (a,b,c,d) <= 10 with ab = cd
bf = sum(1 for a in range(1, 11) for b in range(1, 11) for cc in range(1, 11) for d in range(1, 11) if a * b == cc * d)
check("E|S(10)|^4 brute force", bf, 278, 0)
D10 = len({a * b for a in range(1, 11) for b in range(1, 11)})
check("D(10)", D10, 42, 0)
check("10^4/D(10)", 10**4 / D10, 238.1, 0.05)
check("2*10^2-10", 2 * 100 - 10, 190, 0)

# ---------- loglog factor: 25% between 10 and 10^6 ----------
r = (math.log(math.log(10)) / math.log(math.log(1e6))) ** 0.25
check("(loglog10/loglog10^6)^(1/4)", r, 0.75, 0.005)
check("sqrt(pi)/2", math.sqrt(math.pi) / 2, 0.886, 5e-4)
check("e^{-1/2}", math.exp(-0.5), 0.61, 5e-3)

# ---------- Steinhaus samples of S(x) up to 10^6 ----------
def spf_table(n):
    spf = np.zeros(n + 1, dtype=np.int64)
    for p in primes_upto(int(n ** 0.5) + 1):
        idx = np.arange(p, n + 1, p)
        sel = spf[idx] == 0
        spf[idx[sel]] = p
    z = np.nonzero(spf == 0)[0]
    spf[z] = z
    return spf

N = X
spf = spf_table(N)
primes = primes_upto(N)
pidx = np.full(N + 1, -1, dtype=np.int64); pidx[primes] = np.arange(len(primes))
# build the exponent matrix rows: n -> list of prime indices with multiplicity, as a sparse matrix
from scipy.sparse import csr_matrix
rows, cols = [], []
rem = np.arange(2, N + 1)
owner = np.arange(2, N + 1)
while len(rem):
    p = spf[rem]
    rows.append(owner); cols.append(pidx[p])
    rem = rem // p
    keep = rem > 1
    rem, owner = rem[keep], owner[keep]
rows = np.concatenate(rows); cols = np.concatenate(cols)
A = csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(N + 1, len(primes)))

def steinhaus_partial_sums(nsamp, batch=25):
    """Return an array (nsamp, N+1) of cumulative sums S(n) would be too big; return S at chosen points."""
    pts = np.array([10, 100, 1000, 10**4, 10**5, 10**6])
    out = np.empty((nsamp, len(pts)), dtype=complex)
    done = 0
    while done < nsamp:
        b = min(batch, nsamp - done)
        theta = rng.random((len(primes), b))
        ph_ = A @ theta                      # phase of f(n), n = 0..N (row 0, 1 are zero)
        f = np.exp(2j * np.pi * ph_)
        f[0] = 0
        S = np.cumsum(f, axis=0)
        out[done:done + b] = S[pts].T
        done += b
    return pts, out

pts, S300 = steinhaus_partial_sums(300)
prob = np.mean(np.abs(S300[:, -1]) ** 2 >= 0.5 * 10**6)
check("P(|S(10^6)|^2 >= x/2), 300 samples (ex:pz)", prob, 0.4, 0.08)
pts, S200 = steinhaus_partial_sums(200)
m1 = np.mean(np.abs(S200), axis=0) / np.sqrt(pts)
print("   E|S(x)|/sqrt x over 200 samples at", list(pts), ":", np.round(m1, 3))
check("first moment at x=10 (fig:firstmoment)", m1[0], 0.9, 0.06)
check("first moment at x=10^6 (fig:firstmoment)", m1[-1], 0.70, 0.07)

# ---------- Section condclt: V(x)/x and fourth moments at x=10^5, 500 samples ----------
x = 10**5
rt = int(math.isqrt(x))
small = primes[primes <= rt]
big = primes[(primes > rt) & (primes <= x)]
cnt_half = int(np.sum((primes > x / 2) & (primes <= x)))
check_true("pi(x)-pi(x/2) >= x/(3 log x) at x=10^5", cnt_half >= x / (3 * math.log(x)))
EV = sum(x // int(p) for p in big)
check("E V(x)/x at 10^5 (exact)", EV / x, 0.64, 0.005)
Vs, T4n, T4x = [], [], []
nsm = rt  # f on 1..rt
for _ in range(500):
    th = rng.random(len(small))
    fsm = np.zeros(nsm + 1, dtype=complex); fsm[1] = 1
    # f(n) for n <= rt: completely multiplicative
    for n in range(2, nsm + 1):
        p = int(spf[n]); fsm[n] = np.exp(2j * np.pi * th[pidx[p]]) * fsm[n // p]
    Ssm = np.cumsum(fsm)
    coef = Ssm[x // big]
    V = float(np.sum(np.abs(coef) ** 2))
    fb = np.exp(2j * np.pi * rng.random(len(big)))
    T = np.sum(fb * coef)
    Vs.append(V / x); T4n.append(abs(T) ** 4 / V**2); T4x.append(abs(T) ** 4 / (x * math.log(2)) ** 2)
Vs = np.array(Vs)
print("   V/x: mean %.3f median %.3f  P(>1.4)=%.3f  E|T/sqrtV|^4=%.2f  E|T/sqrt(x log2)|^4=%.2f"
      % (Vs.mean(), np.median(Vs), np.mean(Vs > 1.4), np.mean(T4n), np.mean(T4x)))
check("mean V/x (500 samples)", Vs.mean(), 0.65, 0.05)
check("median V/x (500 samples)", np.median(Vs), 0.33, 0.05)
check("P(V/x > 1.4) (500 samples)", np.mean(Vs > 1.4), 0.10, 0.04)
check("E|T/sqrt V|^4 (500 samples)", np.mean(T4n), 2.1, 0.3)
check("E|T/sqrt(x log 2)|^4 (500 samples)", np.mean(T4x), 5.2, 2.5)

# ---------- Prop orth / Rademacher Chowla model: E C(x)^2 = #{n<=x: n, n+1 squarefree} ----------
def sqfree_upto(n):
    s = np.ones(n + 2, dtype=bool)
    for p in primes_upto(int(math.isqrt(n + 1)) + 1):
        s[p * p::p * p] = False
    return s
sf = sqfree_upto(2000)
pairs = sum(1 for n in range(1, 1001) if sf[n] and sf[n + 1])
# Monte Carlo check of E C(1000)^2 = pairs
rad = []
for _ in range(4000):
    sgn = rng.choice([-1, 1], size=2001)
    f = np.zeros(1002)
    for n in range(1, 1002):
        if not sf[n]: continue
        v, k = 1, n
        while k > 1:
            p = int(spf[k]); v *= sgn[p]; k //= p
        f[n] = v
    rad.append(np.sum(f[1:1001] * f[2:1002]))
rad = np.array(rad)
check("E C(1000)^2 = #{n<=1000: n,n+1 squarefree} (Monte Carlo)", np.mean(rad**2) / pairs, 1.0, 0.06)
check("first moment drop 10 -> 10^6 about 20%", 1 - m1[-1] / m1[0], 0.20, 0.05)

# ---------- Exercise golden: ||k phi|| >= 1/(3k) ----------
phi_g = (1 + 5 ** 0.5) / 2
ks = np.arange(1, 10**5)
dist = np.abs(ks * phi_g - np.round(ks * phi_g))
check_true("||k phi|| >= 1/(3k) for k < 10^5", bool(np.all(dist * 3 * ks >= 1)))

# ---------- Exercise catalan ----------
from scipy.integrate import quad
for mm in range(5):
    v, _ = quad(lambda t: (2 * math.cos(t)) ** (2 * mm) * 2 / math.pi * math.sin(t) ** 2, 0, math.pi)
    check(f"Sato-Tate moment 2m={2*mm}", v, math.comb(2 * mm, mm) / (mm + 1), 1e-8)

# ---------- Exercises squarefreecount and noroot, brute force over small F_p ----------
import itertools
def polys(p, n):
    for coeffs in itertools.product(range(p), repeat=n):
        yield list(coeffs) + [1]  # a_0..a_{n-1}, 1
def has_root(f, p):
    return any(sum(a * pow(r, i, p) for i, a in enumerate(f)) % p == 0 for r in range(p))
import sympy
from sympy import Poly, symbols, GF
Xs = symbols('X')
def squarefree(f, p):
    P = Poly(list(reversed(f)), Xs, modulus=p)
    return P.degree() == 0 or sympy.gcd(P, P.diff(Xs)).degree() == 0
for p, n in [(2, 3), (3, 3), (3, 4), (5, 3)]:
    sq = sum(1 for f in polys(p, n) if squarefree(f, p))
    check(f"squarefree monic count p={p} n={n}", sq, p**n - p**(n - 1), 0)
for p, n in [(2, 2), (2, 3), (3, 3), (3, 4), (5, 5)]:
    nr = sum(1 for f in polys(p, n) if not has_root(f, p))
    check(f"no-root proportion p={p} n={n}", nr / p**n, (1 - 1 / p) ** p, 1e-12)

# ---------- Theorem factortypes: N_lambda(p) = prod binom(N_p(d), m_d); spot check p=5, n=4 ----------
from collections import Counter
def Np(p, d):
    return sum(sympy.mobius(e) * p ** (d // e) for e in sympy.divisors(d)) // d
p, n = 5, 4
types = Counter()
for f in polys(p, n):
    P = Poly(list(reversed(f)), Xs, modulus=p)
    _, fl = P.factor_list()
    if any(e > 1 for _, e in fl): continue
    types[tuple(sorted(q.degree() for q, _ in fl))] += 1
ok = True
for lam, cnt in types.items():
    md = Counter(lam)
    pred = 1
    for d, mdd in md.items(): pred *= math.comb(Np(p, d), mdd)
    ok &= pred == cnt
check_true("N_lambda(5) = prod binom(N_5(d), m_d) for n=4", ok)

# ---------- Proposition birch and figure: p = 1009 ----------
p = 1009
check("p^2 - p curves with Delta != 0", p * p - p, 1017072, 0)
chi = np.zeros(p, dtype=np.int64)
sq = set((t * t) % p for t in range(1, p))
for u in range(1, p): chi[u] = 1 if u in sq else -1
xs = np.arange(p)
tot2 = 0; mom = {2: 0.0, 4: 0.0, 6: 0.0}; cnt = 0; tot_all2 = 0
for a in range(p):
    v = (xs**3 + a * xs) % p
    h = np.bincount(v, minlength=p)                     # how often x^3+ax takes each value
    # a_p(a,b) = -sum_u h[u] chi[(u+b) % p]: circular correlation
    ap = -np.real(np.fft.ifft(np.conj(np.fft.fft(h)) * np.fft.fft(chi))).round().astype(np.int64)
    tot_all2 += int(np.sum(ap**2))
    b = np.arange(p)
    good = (4 * a**3 + 27 * b * b) % p != 0
    t = ap[good] / math.sqrt(p)
    for k in mom: mom[k] += float(np.sum(t**k))
    cnt += int(good.sum())
check("sum_{a,b} a_p^2 = p^2(p-1)", tot_all2, p * p * (p - 1), 0)
check("number of curves", cnt, 1017072, 0)
for k, printed in [(2, 1.0), (4, 2.0), (6, 5.0)]:
    print(f"   moment {k} of a_p/sqrt p over all curves: {mom[k]/cnt:.6f}")
    check(f"Birch moment {k} (printed to 4 places)", mom[k] / cnt, printed, 5e-5)

# ---------- Figure chebotarev: x^5-x-1 and x^5-2 modulo 7 <= p < 10^5 ----------
def ftype(coeffs, p):
    P = Poly(coeffs, Xs, modulus=p)
    _, fl = P.factor_list()
    if any(e > 1 for _, e in fl): return None
    return tuple(sorted(q.degree() for q, _ in fl))
ps = [int(q) for q in primes_upto(10**5) if q >= 7]
for name, coeffs, disc in [("x^5-x-1", [1, 0, 0, 0, -1, -1], 2869), ("x^5-2", [1, 0, 0, 0, 0, -2], 50000)]:
    cnts = Counter()
    for q in ps:
        if disc % q == 0: continue
        t = ftype(coeffs, q)
        if t is not None: cnts[t] += 1
    tot = sum(cnts.values())
    print("  ", name, {k: round(v / tot, 4) for k, v in sorted(cnts.items())})
    if name == "x^5-2":
        check_true("x^5-2: exactly four types occur", len(cnts) == 4)
        for lam, fr in [((1, 1, 1, 1, 1), 1 / 20), ((1, 2, 2), 5 / 20), ((1, 4), 10 / 20), ((5,), 4 / 20)]:
            check(f"x^5-2 frequency of type {lam}", cnts[lam] / tot, fr, 0.01)
        check_true("x^5-2 never of type 1^3 2, 1^2 3, 2 3",
                   all(cnts[l] == 0 for l in [(1, 1, 1, 2), (1, 1, 3), (2, 3)]))
    else:
        s5 = {(1, 1, 1, 1, 1): 1, (1, 1, 1, 2): 10, (1, 2, 2): 15, (1, 1, 3): 20, (2, 3): 20, (1, 4): 30, (5,): 24}
        for lam, k in s5.items():
            check(f"x^5-x-1 frequency of type {lam}", cnts[lam] / tot, k / 120, 0.01)
check("disc(x^5-x-1)", int(sympy.discriminant(Xs**5 - Xs - 1)), 2869, 0)
check("disc(x^5-2)", int(sympy.discriminant(Xs**5 - 2)), 50000, 0)
check("85 years 1936 -> 2021", 2021 - 1936, 85, 0)

finish()
