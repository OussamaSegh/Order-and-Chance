"""Volume 10, Chapter 11 (Compact groups): Weyl's dimension formula against the hook-content formula, the exercise dimensions,
Theorem 11.9 (moments of tr U = permutations with bounded longest increasing subsequence) exactly and by Monte Carlo,
Gaussian moments, E|det(I-U)|^2 = n+1, the U(2) Catalan count, and the Keating--Snaith constants 42 and 24024."""
import itertools, math, bisect
from fractions import Fraction
import numpy as np
from common import check, check_true, finish

def partitions(n, m=None):
    m = n if m is None else m
    if n == 0: yield (); return
    for k in range(min(n, m), 0, -1):
        for p in partitions(n - k, k): yield (k,) + p
def conj(l): return tuple(sum(1 for r in l if r > j) for j in range(l[0])) if l else ()
def f_hook(l):
    lc = conj(l); return math.factorial(sum(l)) // math.prod(l[i] - j - 1 + lc[j] - i for i in range(len(l)) for j in range(l[i]))
def weyl_dim(lam, n):
    lam = list(lam) + [0] * (n - len(lam)); nu = [lam[j] + n - 1 - j for j in range(n)]
    return Fraction(math.prod(nu[j] - nu[k] for j in range(n) for k in range(j + 1, n)), math.prod(k - j for j in range(n) for k in range(j + 1, n)))
def hook_content(lam, n):
    lc = conj(lam)
    return math.prod(Fraction(n + j - i, lam[i] - j - 1 + lc[j] - i) for i in range(len(lam)) for j in range(lam[i]))
check_true("Weyl dimension = hook-content formula (n<=5, |lambda|<=7, at most n rows)", all(weyl_dim(l, n) == hook_content(l, n) for n in range(1, 6) for k in range(1, 8) for l in partitions(k) if len(l) <= n))
check_true("ex:dims: Sym^k = C(n+k-1,k), Lambda^k = C(n,k), V_(1,0..0,-1) = n^2-1", all(weyl_dim((k,), n) == math.comb(n + k - 1, k) and (k > n or weyl_dim((1,) * k, n) == math.comb(n, k)) for n in range(2, 7) for k in range(1, 6)) and all(weyl_dim([2] + [1] * (n - 2), n) == n * n - 1 for n in range(2, 7)))
check_true("ex:tensorsquare: n^2 = n(n+1)/2 + n(n-1)/2", all(weyl_dim((2,), n) + weyl_dim((1, 1), n) == n * n for n in range(2, 9)))

def lis(w):
    t = []
    for x in w:
        i = bisect.bisect(t, x)
        if i == len(t): t.append(x)
        else: t[i] = x
    return len(t)
ok = True
for n in range(1, 5):
    for a in range(0, 8):
        rhs = sum(1 for w in itertools.permutations(range(a)) if lis(w) <= n)
        lhs = sum(f_hook(l) ** 2 for l in partitions(a) if len(l) <= n) if a else 1
        ok &= lhs == rhs and (a > n or rhs == math.factorial(a))
check_true("Thm 11.9: sum over l(lambda)<=n of (f^lambda)^2 = #{sigma in S_a: LIS <= n}, = a! for a <= n", ok)
check_true("ex:catalanu2: 321-avoiding count is Catalan", all(sum(1 for w in itertools.permutations(range(a)) if lis([-x for x in w]) <= 2) == math.comb(2 * a, a) // (a + 1) for a in range(1, 9)))
check_true("Gaussian moments: (2r)!/(4^r r!) * 2^r = (2r)!/(2^r r!)", all(Fraction(math.factorial(2 * r), 4 ** r * math.factorial(r)) * 2 ** r == Fraction(math.factorial(2 * r), 2 ** r * math.factorial(r)) for r in range(10)))
check_true("binomial(2r, r) r!/4^r = (2r)!/(4^r r!)", all(Fraction(math.comb(2 * r, r) * math.factorial(r), 4 ** r) == Fraction(math.factorial(2 * r), 4 ** r * math.factorial(r)) for r in range(10)))

# Monte Carlo with Haar unitaries (QR of a complex Gaussian with phase correction, as in Volume 9, Chapter 8)
rng = np.random.default_rng(1)
def haar(n, N):
    Z = (rng.standard_normal((N, n, n)) + 1j * rng.standard_normal((N, n, n))) / math.sqrt(2)
    Q, R = np.linalg.qr(Z)
    d = np.diagonal(R, axis1=1, axis2=2)
    return Q * (d / abs(d))[:, None, :]
N = 200000
U2 = haar(2, N); t = np.trace(U2, axis1=1, axis2=2)
check("U(2): E|tr U|^6 = 5 (Catalan)", float(np.mean(abs(t) ** 6)), 5, 0.15)
U3 = haar(3, N); t3 = np.trace(U3, axis1=1, axis2=2)
check("U(3): E|tr U|^4 = 2", float(np.mean(abs(t3) ** 4)), 2, 0.05)
check("U(3): E|det(I-U)|^2 = n+1 = 4", float(np.mean(abs(np.linalg.det(np.eye(3) - U3)) ** 2)), 4, 0.08)
check("U(3): E[tr U^2 conj(tr U^2)] = 2", float(np.mean(abs(np.trace(U3 @ U3, axis1=1, axis2=2)) ** 2)), 2, 0.05)

# Keating--Snaith: g_k = (k^2)! prod_{j<k} j!/(j+k)!
g = lambda k: Fraction(math.factorial(k * k)) * math.prod(Fraction(math.factorial(j), math.factorial(j + k)) for j in range(k))
check_true("Keating-Snaith g_1..g_4 = 1, 2, 42, 24024", [g(k) for k in range(1, 5)] == [1, 2, 42, 24024])
finish()
