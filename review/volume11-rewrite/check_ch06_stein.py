"""Chapter 6 (Stein's method): check every printed number."""
import math
import numpy as np
from scipy.stats import norm, hypergeom
from scipy.integrate import quad
from common import check, check_true, finish

# constant 2 psi(w) psi(-w) / phi(w) max = sqrt(2/pi) at 0  (psi = Phi on (-inf,w]?)
check("2phi(0)=sqrt(2/pi)", 2 * norm.pdf(0), 0.80, 0.005)
w = np.linspace(-6, 6, 120001)
psi = lambda x: norm.pdf(x) - x * norm.sf(x)
g = 2 * psi(w) * psi(-w) / norm.pdf(w)
check_true("max of 2psi(w)psi(-w)/phi(w) is sqrt(2/pi) at w=0", abs(w[np.argmax(g)]) < 1e-3 and abs(g.max() - math.sqrt(2 / math.pi)) < 1e-9 and np.all(g <= 2 * norm.pdf(0) + 1))

# birthdays
lam = math.comb(23, 2) / 365
check("birthday lambda", lam, 0.693, 0.0005)
check("birthday e^-lambda", math.exp(-lam), 0.500, 0.0005)
exact = math.prod((365 - k) / 365 for k in range(23))
check("birthday exact", exact, 0.493, 0.0005)
check("birthday bound", (4 * 23 - 7) * (1 - math.exp(-lam)) / 365, 0.12, 0.005)

# figure: max true error over n
errs = []
for n in range(1, 80):
    ex = math.prod((365 - k) / 365 for k in range(n))
    errs.append(abs(ex - math.exp(-math.comb(n, 2) / 365)))
check_true("figure: true error never exceeds 0.011 (max=%.4f)" % max(errs), max(errs) <= 0.011)

# hashes
d = 2 ** 32
n = 10 ** 5
lam = math.comb(n, 2) / d
check("hash lambda", lam, 1.164, 0.0005)
check("hash e^-lambda", math.exp(-lam), 0.312, 0.0005)
b = (4 * n - 7) * (1 - math.exp(-lam)) / d
check_true("hash bound %.3g <= 6.5e-5" % b, b <= 6.5e-5)
n = 77163
lam = math.comb(n, 2) / d
check("77163: 1-e^-lambda", 1 - math.exp(-lam), 0.5, 4e-5)
b = (4 * n - 7) * (1 - math.exp(-lam)) / d
check_true("77163: |1-e^-lam - 1/2| + bound %.3g < 4e-5" % (abs(1 - math.exp(-lam) - .5) + b), abs(1 - math.exp(-lam) - .5) + b < 4e-5)

# poll: m=1000, N=10^4, p=1/2
N, m, K = 10 ** 4, 1000, 5000
sig = math.sqrt(m * 0.25 * (N - m) / (N - 1))
check("poll sigma", sig, 15, 0.05)
check("poll bound", 2 / sig + 4 / N, 0.13, 0.005)
ks = np.arange(0, m + 1)
pm = hypergeom.pmf(ks, N, K, m)
F = np.cumsum(pm)
# Wasserstein distance = integral |F_W - Phi|
xs = (ks - m / 2) / sig
dw = 0.0
for i in range(len(ks) - 1):
    a, bb = xs[i], xs[i + 1]
    dw += quad(lambda t: abs(F[i] - norm.cdf(t)), a, bb)[0]
dw += quad(lambda t: norm.cdf(t), -np.inf, xs[0])[0] + quad(lambda t: norm.sf(t), xs[-1], np.inf)[0]
check("poll true d_W", dw, 0.017, 0.0015)

# near-birthdays n=14 on circle
n = 14
lam = 3 * math.comb(n, 2) / 365
check("near lambda", lam, 0.748, 0.0005)
check("near e^-lambda", math.exp(-lam), 0.473, 0.0005)
check("near bound", (4 * n - 7) * 3 / 365 * (1 - math.exp(-lam)), 0.21, 0.005)
d = 365
exact = math.prod(range(d - 2 * n + 1, d - n)) / d ** (n - 1)
check("near exact P(no close pair)", exact, 0.463, 0.0005)
# brute-force sanity of the formula on a small circle
import itertools
dd, nn = 12, 3
cnt = sum(1 for t in itertools.product(range(dd), repeat=nn)
          if all(min((t[i] - t[j]) % dd, (t[j] - t[i]) % dd) >= 2 for i in range(nn) for j in range(i)))
check_true("circular formula, d=12,n=3", abs(cnt / dd ** nn - math.prod(range(dd - 2 * nn + 1, dd - nn)) / dd ** (nn - 1)) < 1e-12)

# head runs
n = 10 ** 6
best = min(range(5, 30), key=lambda r: abs(math.exp(-n * 2.0 ** (-r - 1)) - 0.5))
check("best r", best, 19, 0)
lam = n * 2.0 ** (-20)
check("runs lambda", lam, 0.95, 0.005)
check("runs e^-lambda", math.exp(-lam), 0.39, 0.005)
check("runs 1-e^-lambda", 1 - math.exp(-lam), 0.61, 0.005)
check_true("39*2^-20 < 4e-5", 39 * 2.0 ** -20 < 4e-5)
check("2^(r+1) ~ n/log2", n / math.log(2), 1.44e6, 0.005e6)
finish()
