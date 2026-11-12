"""Number checks for Volume 6, Chapter 5 (the prime number theorem). Sieves to 10^8: about a minute."""
import math
import numpy as np
import mpmath as mp
from common import GAMMA, primes_upto, check, check_true, finish

mp.mp.dps = 30
X = 10 ** 8
P = primes_upto(X)
logP = np.log(P)

# --- opening, think box, figure
pi = len(P)
check("pi(10^8)", pi, 5761455, 0)
Li = float(mp.li(X) - mp.li(2))
check("Li(10^8) - pi(10^8)", Li - pi, 753, 0.5)
check("pi / (x/log x) at 10^8", pi / (X / math.log(X)), 1.0613, 5e-5)
check("pi / Li at 10^8", pi / Li, 0.99987, 5e-6)
check("x/log x too small by about 6 percent", 100 * (1 - (X / math.log(X)) / pi), 6, 0.5)
check("Li too large by about 0.013 percent", 100 * (Li / pi - 1), 0.013, 5e-4)
check("1/log x at 10^8", 1 / math.log(X), 0.054, 5e-4)
check("observed excess of pi log x / x at 10^8", pi * math.log(X) / X - 1, 0.061, 5e-4)

# --- A(x) = sum_{n<=x} mu(n)/n
N = 10 ** 7
mu = np.ones(N + 1, dtype=np.int8)
for p in primes_upto(int(N ** 0.5) + 1):
    p = int(p)
    mu[p::p] *= -1
    mu[p * p::p * p] = 0
# primes above sqrt(N): each n has at most one such factor
rem = np.arange(N + 1, dtype=np.int64)
for p in primes_upto(int(N ** 0.5) + 1):
    p = int(p)
    q = p
    while q <= N:
        rem[q::q] //= p
        q *= p
mu[rem > 1] *= -1
mu[0] = 0
A = np.cumsum(mu[1:] / np.arange(1, N + 1))
check("A(10^4)", A[10 ** 4 - 1], -0.0021, 5e-5)
check("A(10^6)", A[10 ** 6 - 1], 0.00020, 5e-6)
check("A(10^7)", A[10 ** 7 - 1], 0.00010, 5e-6)

# --- sum Lambda(n)/n - log x and the constant of Exercise ex:rlimit
# sum_p log p/(p(p-1)) = sum_{k>=2} sum_p log p / p^k = - sum_{k>=2} P'(k), P the prime zeta function
c = float(-mp.nsum(lambda k: mp.diff(mp.primezeta, k), [2, mp.inf]))
check("sum log p/(p(p-1))", c, 0.75536, 1e-5)
check("-gamma - that sum", -GAMMA - c, -1.33258, 1e-5)
lam = 0.0
for k in range(1, 27):
    r = P[P <= int(round(X ** (1.0 / k))) + 1]
    r = r[r.astype(object) ** k <= X] if k > 1 else r
    r = r.astype(np.float64)
    lam += float((np.log(r) / r ** k).sum())
check("sum_{n<=10^8} Lambda(n)/n - log x", lam - math.log(X), -0.577234, 2e-6)

# --- n-th prime
n = 10 ** 6
pn = int(P[n - 1])
check("p_n for n = 10^6", pn, 15485863, 0)
check("p_n/(n log n)", pn / (n * math.log(n)), 1.121, 5e-4)
cip = n * (math.log(n) + math.log(math.log(n)) - 1)
check("Cipolla off by 0.29 percent", 100 * abs(cip / pn - 1), 0.29, 5e-3)

# --- lcm(1..n)^(1/n) = exp(psi(n)/n)
def psi(x):
    s = 0.0
    k = 1
    while 2 ** k <= x:
        r = P[P <= int(round(x ** (1.0 / k))) + 1]
        r = [int(q) for q in r] if k > 1 else r
        if k > 1:
            s += sum(math.log(q) for q in r if q ** k <= x)
        else:
            s += float(np.log(r[r <= x]).sum())
        k += 1
    return s
check("lcm^(1/n), n = 100", math.exp(psi(100) / 100), 2.561, 5e-4)
check("lcm^(1/n), n = 1000", math.exp(psi(1000) / 1000), 2.709, 5e-4)
check("lcm^(1/n), n = 10^8", math.exp(psi(X) / X), 2.71823, 5e-6)

# --- L'/L(1, chi) for chi_-4 and chi_-3
def logder(q, classes):
    L = lambda s: mp.mpf(q) ** (-s) * sum(c * mp.zeta(s, mp.mpf(a) / q) for a, c in classes)
    h = mp.mpf(10) ** (-8)
    return (L(1 + h) - L(1 - h)) / (2 * h) / ((L(1 + h) + L(1 - h)) / 2)
r4 = float(logder(4, [(1, 1), (3, -1)]))
r3 = float(logder(3, [(1, 1), (2, -1)]))
check("L'/L(1, chi_-4)", r4, 0.24561, 5e-6)
closed = GAMMA + 2 * math.log(2) + 3 * math.log(math.pi) - 4 * float(mp.log(mp.gamma(0.25)))
check("closed form gamma + 2 log 2 + 3 log pi - 4 log Gamma(1/4)", closed, r4, 1e-9)
check("L'/L(1, chi_-3)", r3, 0.36828, 5e-6)
s4 = 0.0
for k in range(1, 27):
    r = P[P <= int(round(X ** (1.0 / k))) + 1]
    r = np.array([int(q) for q in r if int(q) ** k <= X and q != 2], dtype=np.int64)
    if len(r) == 0: continue
    sign = np.where(r % 4 == 1, 1.0, -1.0) ** k
    rf = r.astype(np.float64)
    s4 += float((sign * np.log(rf) / rf ** k).sum())
check("sum_{n<=10^8} chi_-4(n) Lambda(n)/n", s4, -0.24558, 5e-6)

# --- semiprimes up to 10^8
small = P[P <= 10 ** 4]
idx = np.searchsorted(P, X // small, side="right")          # pi(x/p)
pi2 = int((idx - np.arange(len(small))).sum())               # q >= p
check("pi_2(x) log x / (x log log x) at 10^8", pi2 * math.log(X) / (X * math.log(math.log(X))), 1.102, 5e-4)

# --- closing problems
check("log 2^1023", 1023 * math.log(2), 709, 0.5)
check("with the wheel 30", 1023 * math.log(2) * 4 / 15, 189, 0.5)
check("e^gamma", math.exp(GAMMA), 1.78, 5e-3)
Q = P[P % 4 == 1].astype(np.float64)
prod = float(np.exp(np.log1p(-2 / Q ** 2).sum()))
check("prod_{p=1 (4)} (1 - 2/p^2)", prod, 0.8948, 5e-5)
check("6/pi^2", 6 / math.pi ** 2, 0.6079, 5e-5)
M = 10 ** 6
n = np.arange(1, M + 1, dtype=np.int64)
v = n * n + 1
sqfree = np.ones(M, dtype=bool)
for p in primes_upto(M):
    p = int(p)
    if p % 4 != 1: continue
    p2 = p * p
    if p2 > M * M + 1: break
    # roots of x^2 = -1 mod p^2, found by lifting a root mod p
    g = next(a for a in range(2, p) if pow(a, (p - 1) // 2, p) == p - 1)
    x0 = pow(g, (p - 1) // 4, p)
    t = (-(x0 * x0 + 1) // p * pow(2 * x0, -1, p)) % p
    x1 = (x0 + t * p) % p2
    for root in (x1, p2 - x1):
        sqfree[(root - 1) % p2::p2] = False
check("proportion of n <= 10^6 with n^2+1 squarefree", sqfree.mean(), 0.8948, 5e-4)

# --- Ruzsa's Sidon set modulo p(p-1), exercise pb:sidon (d)
for p in (5, 7, 11, 13, 101):
    g = next(a for a in range(2, p) if len({pow(a, k, p) for k in range(p - 1)}) == p - 1)
    Nmod = p * (p - 1)
    S = [next(a for a in range(1, Nmod + 1) if a % (p - 1) == i % (p - 1) and a % p == pow(g, i, p)) for i in range(1, p)]
    sums = [(S[i] + S[j]) % Nmod for i in range(len(S)) for j in range(i, len(S))]
    check_true("Ruzsa set is Sidon modulo p(p-1), p = %d" % p, len(set(sums)) == len(sums) and len(set(S)) == p - 1)
# Erdos-Turan set
for p in (3, 5, 7, 11, 101):
    S = [2 * p * k + (k * k) % p for k in range(p)]
    sums = [S[i] + S[j] for i in range(p) for j in range(i, p)]
    check_true("Erdos-Turan set is Sidon, p = %d" % p, len(set(sums)) == len(sums) and max(S) < 2 * p * p)

finish()
