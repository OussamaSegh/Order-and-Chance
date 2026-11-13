"""Chapter 13 (shuffling cards): check every printed number."""
import math
from fractions import Fraction
from scipy.stats import norm
from common import check, check_true, finish

n = 52
check("1/2 n ln n, n=52", 0.5 * n * math.log(n), 103, 0.5)
check("1/2 n ln n + n", 0.5 * n * math.log(n) + n, 155, 0.5)

def partitions(n, maxpart=None):
    if maxpart is None: maxpart = n
    if n == 0: yield (); return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest

def hook_f(lam):
    n = sum(lam); conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    logh = sum(math.log(lam[i] - j + conj[j] - i - 1) for i in range(len(lam)) for j in range(lam[i]))
    return math.lgamma(n + 1) - logh

def s_of(lam, n):
    content = sum(j - i for i in range(len(lam)) for j in range(lam[i]))
    r = content / math.comb(n, 2)
    return 1 / n + (n - 1) / n * r

t = 155
S = 0.0
for lam in partitions(n):
    if lam == (n,): continue
    s = s_of(lam, n)
    if s == 0: continue
    S += math.exp(2 * hook_f(lam) + 2 * t * math.log(abs(s)))
check_true("n=52: d(155) <= 1/2 sqrt(S) = %.4f <= 0.06" % (0.5 * math.sqrt(S)), 0.5 * math.sqrt(S) <= 0.06)

# proof constants of Theorem 13.8
check_true("e^{1+2/e} <= e^2.1 < 8.2", math.exp(1 + 2 / math.e) <= math.exp(2.1) < 8.2)
check_true("1+ln3-ln(1e4)/3 <= 2.1", 1 + math.log(3) - math.log(1e4) / 3 <= 2.1)
q = 8.2 * math.exp(-4)
check_true("q<0.151", q < 0.151)
check_true("2q/(1-q) <= 2.36 q", 2 / (1 - 0.151) <= 2.36)
check_true("2.36*8.2 < 19.4", 2.36 * 8.2 < 19.4)
check("x+ln(1-2x+2x^2) at 1/3", 1 / 3 + math.log(1 - 2 / 3 + 2 / 9), -0.254, 0.0005)
check("x+ln(1-2x+2x^2) at 1/2", 0.5 + math.log(0.5), -0.193, 0.0005)
check_true("1/2+ln(0.5001)<-0.19", 0.5 + math.log(0.5001) < -0.19)
check_true("ln 0.56 < -0.57", math.log(0.56) < -0.57)
check_true("x(1-ln x)<=0.85 at 1/2", 0.5 * (1 - math.log(0.5)) <= 0.85)
check_true("ln 1e4 >= 9.2", math.log(1e4) >= 9.2)
check_true("middle: -0.19*9.2+0.85 <= -0.89", -0.19 * 9.2 + 0.85 <= -0.89)
check_true("short: ln2-0.19*9.2+0.85 <= -0.20", math.log(2) - 0.19 * 9.2 + 0.85 <= -0.20)
check_true("2 ln 2 >= 1.38", 2 * math.log(2) >= 1.38)
check_true("1/2 sqrt(19.5) < 3", 0.5 * math.sqrt(19.5) < 3)
check_true("3e^{-8/3}<0.21", 3 * math.exp(-8 / 3) < 0.21)
check_true("1-6e^{-3} > 1/4", 1 - 6 * math.exp(-3) > 0.25)

# three cards: exact d(t)
from itertools import permutations
perms = list(permutations(range(3)))
def compose(a, b): return tuple(a[b[i]] for i in range(3))
Q = {p: Fraction(0) for p in perms}
Q[(0, 1, 2)] += Fraction(1, 3)
for i in range(3):
    for j in range(3):
        if i != j:
            p = list(range(3)); p[i], p[j] = p[j], p[i]; Q[tuple(p)] += Fraction(1, 9)
mu = {p: Fraction(int(p == (0, 1, 2))) for p in perms}
ok = True
for tt in range(8):
    d = sum(abs(v - Fraction(1, 6)) for v in mu.values()) / 2
    ok &= d == Fraction(11 - (-1) ** tt, 12) / 3 ** tt
    new = {p: Fraction(0) for p in perms}
    for a, va in mu.items():
        for b, vb in Q.items():
            new[compose(b, a)] += va * vb
    mu = new
check_true("three cards d(t) = (11-(-1)^t)/12 3^-t", ok)

# riffle shuffles: exact distance via Eulerian numbers
def eulerian(n):
    A = [1]
    for m in range(2, n + 1):
        B = [0] * m
        for k in range(m):
            B[k] = (k + 1) * (A[k] if k < len(A) else 0) + (m - k) * (A[k - 1] if k >= 1 else 0)
        A = B
    return A  # A[k] = number of perms of n with k descents
def riffle_d(n, a):
    A = eulerian(n); nf = math.factorial(n); tot = Fraction(0)
    for k, cnt in enumerate(A):
        r = k + 1
        q = Fraction(math.comb(a + n - r, n), a ** n) if a + n - r >= n else Fraction(0)
        diff = Fraction(1, nf) - q
        if diff > 0: tot += cnt * diff
    return float(tot)
check("6 riffles, 52 cards", riffle_d(52, 2 ** 6), 0.614, 0.0005)
check("7 riffles, 52 cards", riffle_d(52, 2 ** 7), 0.334, 0.0005)
check("theta for 7 riffles of 52", 7 - 1.5 * math.log2(52), -1.55, 0.005)
worst = 0
for i in range(-60, 61):
    th = i / 20
    a = max(1, round(2 ** th * 52 ** 1.5))
    lim = 1 - 2 * norm.cdf(-1 / (4 * math.sqrt(3) * (a / 52 ** 1.5)))
    worst = max(worst, abs(riffle_d(52, a) - lim))
check_true("52 cards: within 0.02 of the limit (max %.4f)" % worst, worst <= 0.02)
finish()
