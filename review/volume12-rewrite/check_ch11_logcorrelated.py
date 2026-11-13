"""Chapter 11 numbers: BRW constants, cosine lemma, chaos mass, two variances, maxima of log|Z_n| (simulation)."""
import sys
import numpy as np, mpmath as mp
from math import log, sqrt, pi, e
from common import check, check_true, finish

cstar = sqrt(2*log(2))
check("c* = sqrt(2 log 2)", cstar, 1.1774100225154747, 1e-15)
# half-moment constant C = sum sqrt(2L+2) e^{-L/2}
C = sum(sqrt(2*L+2)*np.exp(-L/2) for L in range(400))
check("half-moment constant 5.39...", C, 5.39, 0.01)
check_true("C < 5.4", C < 5.4)
check("critical BRW: sum e^step", 1/(2*e)*e + e/2/e, 1, 1e-15)
check("critical BRW: sum step e^step", 1/(2*e)*e - e/2/e, 0, 1e-15)
check("mean offspring 1.54", 1/(2*e) + e/2, 1.54, 0.005)
# ballot bound a_n <= n^{-1/2}
from math import comb
check_true("central binomial <= n^{-1/2}", all(comb(n, n//2)/2**n <= n**-0.5 for n in range(1, 400)))
# cosine lemma: |sum_{j<=N} cos(jx)/j - log min(N, 1/|x|)| <= 6
worst = 0
for N in [1, 2, 5, 10, 50, 200, 1000]:
    j = np.arange(1, N+1)
    for x in np.concatenate([np.linspace(1e-4, pi, 3000), [pi]]):
        worst = max(worst, abs(np.sum(np.cos(j*x)/j) - log(min(N, 1/x))))
print("  worst cosine-lemma error:", worst)
check_true("cosine lemma bound 6", worst <= 6)
# covariance of log|Z_n| differs from 1/2 log min(n,1/|x|) by at most 4
worst = 0
for n in [5, 20, 100]:
    r = np.arange(1, 200000)
    for x in np.linspace(1e-3, pi, 400):
        cov = 0.5*np.sum(np.minimum(r, n)/r**2*np.cos(r*x))
        worst = max(worst, abs(cov - 0.5*log(min(n, 1/x))))
print("  worst covariance error:", worst)
check_true("covariance within 4", worst <= 4)
# chaos second moment: int |2 sin(x/2)|^{-g^2/2} dx/2pi = Gamma(1-g^2/2)/Gamma(1-g^2/4)^2
for g in [0.5, 1.0, 1.3]:
    a = mp.mpf(g)**2/2; p = 1/(1-a)
    I = 2*mp.quad(lambda u: (2*mp.sin(mp.pi*u**p/2))**(-a)*mp.pi*p*u**(p-1), [0, 1])/(2*mp.pi)
    check(f"E M(1)^2 gamma={g}", I, mp.gamma(1-g*g/2)/mp.gamma(1-g*g/4)**2, 1e-8)
# C(x) = -1/2 log|2 sin(x/2)|
x = 0.7
check("C(x) closed form", 0.5*mp.nsum(lambda j: mp.cos(j*x)/j, [1, mp.inf]), -0.5*mp.log(abs(2*mp.sin(x/2))), 1e-10)
# two variances: S(k) = sum_{r>=k} 1/r^2
for k in [1, 2, 5, 17]:
    S = mp.mpf(0); t = mp.mpf(1)
    for j in range(1, 20000):
        t *= mp.mpf(j)/(k+j-1); S += t/j**2
    check(f"S({k}) = psi'(k)", S, mp.psi(1, k), 1e-3/k)
# Bernstein: (1+1/n)^n <= e; upper bound exponent
check_true("(1+1/n)^n <= e", all((1+1/n)**n <= e for n in range(1, 10000)))
# figure: log 1000 and log n - 3/4 log log n
check("log 1000", log(1000), 6.91, 0.005)
check("log n - 3/4 log log n at 1000", log(1000) - 0.75*log(log(1000)), 5.46, 0.005)
# independent maximum correction 1/4 log log n
s2 = lambda n: 0.5*log(n)
check("independent correction coefficient", sqrt(s2(1e8))/(2*sqrt(2*log(1e8)))*1, 0.25, 1e-12)

# Figure ch12-maxima: the plotted means (y = 0.31 + 0.62 (value - 1)) against the caption
import re, os
fs = open(os.path.join(os.path.dirname(__file__), "../../volume12-random-motion/figures/ch12-maxima.tex")).read()
pts = [float(y) for x, y in re.findall(r"\\fill\[blue!60!black\] \(([\d.]+),([\d.]+)\) circle", fs)]
ns = [2**k for k in range(4, 11)]
vals = [1 + (y-0.31)/0.62 for y in pts]
d34 = [v-(log(n)-0.75*log(log(n))) for v, n in zip(vals, ns)]
d14 = [v-(log(n)-0.25*log(log(n))) for v, n in zip(vals, ns)]
check_true("seven plotted means", len(vals) == 7)
check("3/4 difference min 0.31", min(d34), 0.31, 0.006)
check("3/4 difference max 0.44", max(d34), 0.44, 0.006)
check("1/4 difference at n=16: -0.11", d14[0], -0.11, 0.006)
check("1/4 difference at n=1024: -0.66", d14[-1], -0.66, 0.006)
check_true("1/4 difference drifts steadily down", all(a > b for a, b in zip(d14, d14[1:])))
best = max(float(y) for line in fs.splitlines() if line.count("--") > 20
           for x, y in re.findall(r"\(([\d.]+),([\d.-]+)\)", line) if float(x) <= 5.45)
check("left panel maximum 5.62 (plot resolution)", (best-2.6)/0.28, 5.62, 0.06)

if "--sim" in sys.argv:
    rng = np.random.default_rng(2024)
    def haar_angles(n):
        Z = (rng.standard_normal((n, n)) + 1j*rng.standard_normal((n, n)))/sqrt(2)
        Q, R = np.linalg.qr(Z); d = np.diag(R); Q = Q*(d/abs(d))
        return np.angle(np.linalg.eigvals(Q))
    def maxlog(th, n):
        grid = np.linspace(0, 2*pi, 16*n, endpoint=False)
        best = -np.inf
        for chunk in np.array_split(grid, 16):
            v = np.sum(np.log(np.abs(1 - np.exp(1j*(th[None, :] - chunk[:, None])))), axis=1)
            best = max(best, v.max())
        return best
    d34, d14 = [], []
    for n, reps in [(16, 400), (32, 300), (64, 200), (128, 150), (256, 100), (512, 60), (1024, 40)]:
        m = np.mean([maxlog(haar_angles(n), n) for _ in range(reps)])
        d34.append(m - (log(n) - 0.75*log(log(n)))); d14.append(m - (log(n) - 0.25*log(log(n))))
        print(f"  n={n}: mean max {m:.3f}, minus 3/4 form {d34[-1]:.3f}, minus 1/4 form {d14[-1]:.3f}", flush=True)
    check_true("independent re-simulation: 3/4 differences stay in [0.2, 0.55]", min(d34) > 0.2 and max(d34) < 0.55)
    ms = [maxlog(haar_angles(1000), 1000) for _ in range(20)]
    print("  n=1000 single-sample maxima:", np.round(sorted(ms), 2))
    check_true("5.62 is a typical single maximum at n=1000", min(ms) < 5.62 < max(ms))
finish()
