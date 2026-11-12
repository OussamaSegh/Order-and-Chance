"""Number checks for Volume 6, Chapter 7 (the explicit formula). Sieves to 10^7."""
import math
import numpy as np
import mpmath as mp
from common import GAMMA, primes_upto, check, check_true, finish

mp.mp.dps = 20
X = 10 ** 7
P = primes_upto(X)

# --- psi(x) - x up to 10^7 (Schoenfeld remark): psi jumps at prime powers
pts, w = [], []
for p in P:
    p = int(p); q = p
    while q <= X:
        pts.append(q); w.append(math.log(p)); q *= p
order = np.argsort(pts)
pts = np.array(pts, dtype=np.float64)[order]; w = np.array(w)[order]
psi_at = np.cumsum(w)                       # psi(q) at each prime power q
psi_before = psi_at - w                     # psi(q-)
def worst_ratio(lo, f):
    m = pts >= lo
    a = np.abs(psi_at[m] - pts[m]) / f(pts[m])
    b = np.abs(psi_before[m] - pts[m]) / f(pts[m])
    return max(a.max(), b.max())
r1 = worst_ratio(73.2, lambda x: np.sqrt(x) * np.log(x) ** 2)
check("max |psi-x|/(sqrt x log^2 x) for 73.2 <= x <= 10^7", r1, 0.0365, 5e-4)
check("1/(8 pi)", 1 / (8 * math.pi), 0.0398, 5e-5)
r2 = worst_ratio(1000, np.sqrt)
check_true("|psi-x|/sqrt x < 0.81 on [10^3, 10^7] (max %.4f)" % r2, r2 < 0.81)

# --- the race mod 4 up to 10^7: integers n with pi(n;4,1) > pi(n;4,3)
d = np.zeros(X + 1, dtype=np.int32)
d[P[P % 4 == 1]] += 1
d[P[P % 4 == 3]] -= 1
lead = np.cumsum(d)
check("integers <= 10^7 where class 1 leads", int((lead > 0).sum()), 3406, 0)
check("first such integer", int(np.argmax(lead > 0)), 26861, 0)

# --- zeros of L(s, chi_-4)
Lf = lambda t: mp.dirichlet(mp.mpf(0.5) + 1j * t, [0, 1, 0, -1])
for guess, printed in ((6.02, 6.0209), (10.24, 10.24), (12.99, 12.99)):
    g = mp.findroot(lambda t: Lf(t), mp.mpf(guess))
    check("zero of L(s,chi_-4) near %g" % guess, float(mp.re(g)), printed, 5e-3 if printed != 6.0209 else 5e-5)

# --- bias modulo 8 at 10^6 and log-averaged over [10^3, 10^7]
th = np.zeros(X + 1)
for a in (1, 3, 5, 7):
    pass
cls = {}
for a in (1, 3, 5, 7):
    arr = np.zeros(X + 1)
    sel = P[P % 8 == a]
    arr[sel] = np.log(sel.astype(np.float64))
    cls[a] = np.cumsum(arr)
tot = cls[1] + cls[3] + cls[5] + cls[7] + math.log(2)   # theta(x), including p = 2
x = 10 ** 6
for a, printed in zip((1, 3, 5, 7), (-0.84, 0.34, -0.07, 0.57)):
    check("theta(10^6;8,%d) normalised" % a, (cls[a][x] - tot[x] / 4) / math.sqrt(x), printed, 5e-3)
us = np.linspace(math.log(1e3), math.log(1e7), 200001)
xs = np.exp(us).astype(np.int64)
for a, printed in zip((1, 3, 5, 7), (-0.72, 0.23, 0.25, 0.23)):
    vals = (cls[a][xs] - tot[xs] / 4) / np.sqrt(xs)
    check("log-average for a = %d" % a, float(vals.mean()), printed, 6e-3)

# --- the Cesaro formula at x = 10
x = 10.0
lam = {2: math.log(2), 3: math.log(3), 4: math.log(2), 5: math.log(5), 7: math.log(7), 8: math.log(2), 9: math.log(3)}
lhs = sum(v * (1 - n / x) for n, v in lam.items())
check("left side at x = 10", lhs, 3.37642, 5e-6)
ratio = float(mp.zeta(-1, derivative=1) / mp.zeta(-1))
check("zeta'(-1)/zeta(-1)", ratio, 1.98505, 5e-6)
zs = [mp.zetazero(n) for n in range(1, 201)]
S = sum(2 * mp.re(mp.power(x, r) / (r * (r + 1))) for r in zs)
tail = sum(x ** (-2 * k) / (2 * k * (2 * k - 1)) for k in range(1, 60))
rhs = x / 2 - float(S) - math.log(2 * math.pi) + ratio / x - tail
check("right side with 200 pairs", rhs, 3.37645, 5e-6)

# --- explicit formula figure: 100 pairs, x in [1.5, 30], away from integers by > 0.3
zs100 = zs[:100]
def psi0(y):
    s = 0.0
    for n in range(2, int(y) + 1):
        m, p = n, None
        for q in range(2, n + 1):
            if m % q == 0:
                p = q; break
        while m % p == 0: m //= p
        if m == 1:
            s += math.log(p) * (0.5 if n == y else 1)
    return s
worst = 0.0
for y in np.arange(1.5, 30.0001, 0.01):
    if abs(y - round(y)) <= 0.3: continue
    approx = y - float(sum(2 * mp.re(mp.power(y, r) / r) for r in zs100)) - math.log(2 * math.pi) - 0.5 * math.log(1 - y ** -2)
    worst = max(worst, abs(psi0(y) - approx))
check_true("100 pairs: error below 0.34 away from integers (max %.3f)" % worst, worst < 0.34)

# --- zeta'/zeta(0) = log 2 pi
check("zeta'(0)/zeta(0)", float(mp.zeta(0, derivative=1) / mp.zeta(0)), math.log(2 * math.pi), 1e-12)
finish()
