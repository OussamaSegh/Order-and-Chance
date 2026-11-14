#!/usr/bin/env python3
"""Recompute the printed numbers of Chapter 12 (ch12-pseudorandom.tex) and test its identities on examples."""
import math, itertools, numpy as np
from scipy import integrate
from common import check, check_true, finish, primes_upto
rng = np.random.default_rng(12)
def fhat(f): N = len(f); return np.fft.fft(f) / N          # E_x f(x) e(-x xi/N)
def u2_4(f):
    N = len(f); x = np.arange(N); tot = 0
    for h in range(N):
        for k in range(N):
            tot += np.sum(f[x] * np.conj(f[(x + h) % N]) * np.conj(f[(x + k) % N]) * f[(x + h + k) % N])
    return (tot / N ** 3).real
def corr_avg(f):
    N = len(f); return np.mean([abs(np.mean(np.roll(f, -h) * np.conj(f))) ** 2 for h in range(N)])
for N in [9, 15, 21]:
    f = rng.standard_normal(N) + 1j * rng.standard_normal(N)
    a, b, c = u2_4(f), corr_avg(f), np.sum(abs(fhat(f)) ** 4)
    check(f"prop:u2corr U2^4 = corr avg, N={N}", a, b, 1e-10)
    check(f"prop:u2corr U2^4 = sum |fhat|^4, N={N}", a, c, 1e-10)
    m = abs(fhat(f)).max()
    check_true(f"max|fhat| <= U2 <= max^1/2 (E|f|^2)^1/4, N={N}", m <= a ** .25 + 1e-12 and a ** .25 <= m ** .5 * np.mean(abs(f) ** 2) ** .25 + 1e-12)
    eta = 0.6 * m; S = abs(fhat(f)) >= eta
    fp = np.fft.ifft(np.where(S, fhat(f), 0) * N); fpsr = f - fp
    check_true(f"prop:strpsr bounds, N={N}", S.sum() <= np.mean(abs(f) ** 2) / eta ** 2 and u2_4(fpsr) <= eta ** 2 * np.mean(abs(f) ** 2) + 1e-12)
def L3(A, N):
    a = np.zeros(N); a[list(A)] = 1; x = np.arange(N)
    return sum(np.sum(a[x] * a[(x + d) % N] * a[(x + 2 * d) % N]) for d in range(N)) / N ** 2
ok = True; ok2 = True
for N in [15, 31, 45, 101]:
    for trial in range(30):
        A = set(np.nonzero(rng.random(N) < rng.uniform(.1, .9))[0].tolist()) or {0}
        dl = len(A) / N; a = np.zeros(N); a[list(A)] = 1; F = fhat(a - dl)
        bound = dl * (1 - dl) * abs(F[1:]).max()
        ok &= abs(L3(A, N) - dl ** 3) <= bound + 1e-12
        x = np.arange(N); third = np.sum(F ** 2 * F[(-2 * x) % N]).real
        ok2 &= abs(L3(A, N) - dl ** 3 - third) < 1e-12
check_true("thm:u2count bound on random sets", ok)
check_true("Lambda_3 - delta^3 = sum fhat^2 fhat(-2xi)", ok2)
# dichotomy on progression-free sets (Behrend-like: digits 0,1 in base 3, in Z_N with N > 2*max)
A = [m for m in range(400) if set(np.base_repr(m, 3)) <= {'0', '1'}]
N = 2 * 400 + 1; d = len(A) / N; a = np.zeros(N); a[A] = 1
check("progression-free set: Lambda_3 = delta/N", L3(A, N), d / N, 1e-15)
if d * d * N >= 4:
    check_true("ex:noap coefficient >= 3/4 delta^2", abs(fhat(a)[1:]).max() >= .75 * d * d)
# interval
for N, m in [(1001, 500), (2001, 667)]:
    a = np.zeros(N); a[:m] = 1
    check(f"interval coefficient formula N={N}", abs(fhat(a)[1]), abs(math.sin(math.pi * m / N)) / (N * math.sin(math.pi / N)), 1e-12)
check("sin(pi/2)/pi = 0.318", 1 / math.pi, 0.318, 5e-4)
# random set U2 expectation exact (enumerate all subsets for N=7, delta=0.3)
N, dl = 7, 0.3; s2 = dl * (1 - dl); mu4 = s2 * (1 - 3 * s2)
tot = 0
for bits in itertools.product([0, 1], repeat=N):
    pr = math.prod(dl if b else 1 - dl for b in bits)
    tot += pr * np.sum(abs(fhat(np.array(bits) - dl)) ** 4)
check("prop:randomu2 exact, N=7, delta=0.3", tot, (2 * (N - 1) * s2 ** 2 + mu4) / N ** 2, 1e-12)
check("mu4 = sigma^2(1-3sigma^2)", dl * (1 - dl) ** 4 + (1 - dl) * dl ** 4, mu4, 1e-15)
check("ex:randommu4 delta=1/2: mu4 = 1/16", .25 * (1 - .75), 1 / 16, 0)
# quadratic residues
for p in [101, 211, 401]:
    A = {(y * y) % p for y in range(1, p)}; a = np.zeros(p); a[list(A)] = 1
    check_true(f"QR coefficients <= (sqrt p + 1)/(2p), p={p}", abs(fhat(a)[1:]).max() <= (math.sqrt(p) + 1) / (2 * p) + 1e-12)
    check(f"QR Lambda_3 ~ 1/8, p={p}", L3(A, p), 1 / 8, 2 / math.sqrt(p))
    check(f"|Gauss sum| = sqrt p, p={p}", abs(sum(np.exp(2j * math.pi * 3 * y * y / p) for y in range(p))), math.sqrt(p), 1e-8)
# quadratic phase
for N in [101, 99]:
    x = np.arange(N); f = np.exp(2j * math.pi * x * x / N)
    val = np.mean([np.mean(f * np.conj(f[(x + d) % N]) ** 3 * f[(x + 2 * d) % N] ** 3 * np.conj(f[(x + 3 * d) % N])) for d in range(N)])
    check(f"ex:fourterm average = 1, N={N}", val.real, 1, 1e-9)
check("quadratic phase U2 = N^-1/4 (N=101)", np.sum(abs(fhat(np.exp(2j * math.pi * np.arange(101) ** 2 / 101))) ** 4) ** .25, 101 ** -.25, 1e-12)
# local factors
for p in [3, 5, 7, 11]:
    c = sum(1 for x in range(p) for d in range(p) if x % p and (x + d) % p and (x + 2 * d) % p)
    check(f"local count p={p}", c / p ** 2, (p - 1) * (p - 2) / p ** 2, 1e-15)
    check(f"beta_p p={p}", (c / p ** 2) / (1 - 1 / p) ** 3, 1 - 1 / (p - 1) ** 2, 1e-12)
c = sum(1 for x in range(2) for d in range(2) if x % 2 and (x + d) % 2 and (x + 2 * d) % 2)
check("p=2 proportion 1/4", c / 4, .25, 0); check("beta_2 = 2", (c / 4) / .125, 2, 0)
prod = math.prod(1 - 1 / (p - 1) ** 2 for p in primes_upto(10 ** 6) if p > 2)
check("prod_{3<=p<=1e6} = 0.66016", prod, 0.66016, 5e-6)
S3 = 2 * prod; check("S_3 = 1.3203", S3, 1.3203, 5e-5)
# 3-APs of primes table
for N, cnt, pred, ratio in [(10 ** 4, 59504, 62140, .958), (10 ** 5, 2856331, 2890267, .988), (10 ** 6, 157300309, 157968254, .996)]:
    ps = np.array(primes_upto(N)); ind = np.zeros(N + 1); ind[ps] = 1
    L = 1 << (2 * N + 2).bit_length(); Fq = np.fft.rfft(ind, L)
    conv = np.rint(np.fft.irfft(Fq * Fq, L)[:2 * N + 1]).astype(np.int64)
    tot = int(sum((conv[2 * p] - 1) // 2 for p in ps))
    I = integrate.dblquad(lambda d, x: 1 / (math.log(x) * math.log(x + d) * math.log(x + 2 * d)), 2, N, 0, lambda x: (N - x) / 2, epsabs=1e-3)[0]
    check(f"3-APs of primes <= {N}", tot, cnt, 0)
    check(f"prediction at {N}", S3 * I, pred, 1.0)
    check(f"ratio at {N}", tot / (S3 * I), ratio, 5e-4)
    check_true(f"26%..32% excess over Cramer at {N}", 1.255 <= tot / I <= 1.325)
check_true("3,5,7 only progression starting 3,5", all(not (p1 == 3 and p2 == 5) or p2 * 2 - p1 == 7 for p1 in [3] for p2 in [5]))
finish()
