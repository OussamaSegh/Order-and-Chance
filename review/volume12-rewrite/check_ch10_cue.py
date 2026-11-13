"""Chapter 10 numbers: number variance, Keating-Snaith constants, log-det variance, gap expansion, zero counts."""
import mpmath as mp, numpy as np
from math import comb, factorial, log, sqrt, pi
from fractions import Fraction as F
from common import check, check_true, finish

# number variance formula vs tr M - tr M^2 (exact), and 0.84
for n, alpha in [(40, 0.3), (60, 0.125)]:
    c = lambda m: alpha if m == 0 else (np.exp(2j*np.pi*m*alpha)-1)/(2j*np.pi*m)
    M = np.array([[c(a-b) for b in range(n)] for a in range(n)])
    v = np.trace(M).real - np.trace(M@M).real
    form = 2/pi**2*sum(np.sin(pi*m*alpha)**2/m for m in range(1, n)) + 2*n/pi**2*sum(np.sin(pi*m*alpha)**2/m**2 for m in range(n, 200000))
    check(f"number variance n={n}", v, form, 1e-4)
check("sqrt(log 1000)/pi", sqrt(log(1000))/pi, 0.84, 0.005)
check("sqrt(1000)", sqrt(1000), 32, 0.5)

# Keating-Snaith: exact formula vs product formula, constants and (m^2)! products
def ks(n, m):
    r = F(1)
    for l in range(m):
        for i in range(1, m+1): r *= F(n+l+i, l+i)
    return r
check_true("m=1 gives n+1", all(ks(n, 1) == n+1 for n in range(1, 20)))
check_true("m=2 formula", all(ks(n, 2) == F((n+1)*(n+2)**2*(n+3), 12) for n in range(1, 20)))
def G(k):  # G(k) = prod_{j=0}^{k-2} j!
    r = 1
    for j in range(k-1): r *= factorial(j)
    return r
consts = [F(G(m+1)**2, G(2*m+1)) for m in range(1, 5)]
check_true("constants 1,1/12,1/8640,1/870912000", consts == [1, F(1, 12), F(1, 8640), F(1, 870912000)])
check_true("times (m^2)! = 1,2,42,24024", [c*factorial(m*m) for m, c in zip(range(1, 5), consts)] == [1, 2, 42, 24024])
# Monte Carlo check of E|det(I-U)|^4 for n=6 via the BHNY factorisation
rng = np.random.default_rng(3)
def gam(k, size):
    g = rng.standard_normal((size, k)) + 1j*rng.standard_normal((size, k))
    return g[:, 0]/np.linalg.norm(g, axis=1)
n = 6; Z = np.ones(400000, dtype=complex)
for k in range(1, n+1): Z *= 1 - gam(k, 400000)
check("BHNY Monte Carlo E|Z|^4 n=6", np.mean(np.abs(Z)**4)/float(ks(6, 2)), 1.0, 0.03)
# Ingham: a_2 = 6/pi^2, g_2/4! * a_2 = 1/(2 pi^2)
check("Ingham constant", 2/24*6/pi**2, 1/(2*pi**2), 1e-15)

# log-det variance for n=50: sum_k 1/2 sum_j j!/(j^2 (k)_j)
def varX(k):
    s = mp.mpf(0); term = mp.mpf(1)
    for j in range(1, 4000):
        term *= mp.mpf(j)/(k+j-1)
        s += term/j**2
    return s/2
V = sum(varX(k) for k in range(1, 51))
check("Var log|det(I-U)|, n=50", V, 2.74, 0.006)
check("1/2 log 50", 0.5*log(50), 1.96, 0.005)

# gap probability small s: 1 - s + pi^2/36 s^4
def E0(s, m=40):
    x, w = np.polynomial.legendre.leggauss(m)
    y = (x+1)*s/2; w = w*s/2
    S = np.sinc(y[:, None]-y[None, :])
    return np.linalg.det(np.eye(m) - np.sqrt(w)[:, None]*S*np.sqrt(w)[None, :])
for s in [0.05, 0.1]:
    check(f"E(0;s) expansion s={s}", (E0(s) - (1 - s))/s**4, pi**2/36, 0.02)
# p(s) = E''(s) ~ pi^2/3 s^2
h = 1e-3; s = 0.05
pp = (E0(s+h) - 2*E0(s) + E0(s-h))/h**2
check("p(s) ~ pi^2/3 s^2", pp/s**2, pi**2/3, 0.05)
# zeros between 1e6 and 1e6+5000: smooth Riemann-von Mangoldt count
def Nsmooth(T): return float(mp.siegeltheta(T)/mp.pi + 1)
check("RvM prediction 9533", Nsmooth(1e6+5000) - Nsmooth(1e6), 9533, 3)
# Montgomery/GUE: Wigner surmise integrates to 1 with mean 1
check("unitary surmise mass", mp.quad(lambda x: 32/mp.pi**2*x**2*mp.e**(-4*x*x/mp.pi), [0, mp.inf]), 1, 1e-12)
check("unitary surmise mean", mp.quad(lambda x: 32/mp.pi**2*x**3*mp.e**(-4*x*x/mp.pi), [0, mp.inf]), 1, 1e-12)
finish()
