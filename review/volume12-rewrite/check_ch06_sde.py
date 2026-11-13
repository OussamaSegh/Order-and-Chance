"""Volume 12, Chapter 6 (SDEs): the Picard constant, the OU stationary law, Black--Scholes (formula, PDE, delta, vega, parity),
Bessel scale functions, McKean's drift identities for Dyson's Lyapunov function, the 2x2 gap, and the Euler--Maruyama
probabilities of Exercise ex:emgbm."""
import math, itertools
import numpy as np
from scipy import stats
from common import check, check_true, finish

# OU: variance sigma^2/(2 theta)(1-e^{-2 theta t}); figure: theta=1, sigma=1, stationary sd 1/sqrt2, 2 sd = 2/sqrt2
check("OU stationary 2 sd for dX=-X dt+dB", 2 * math.sqrt(0.5), 2 / math.sqrt(2), 1e-15)
# Black-Scholes
def C(t, s, K=1.0, r=0.03, sig=0.25, T=1.0):
    tau = T - t
    dp = (math.log(s / K) + (r + sig ** 2 / 2) * tau) / (sig * math.sqrt(tau)); dm = dp - sig * math.sqrt(tau)
    return s * stats.norm.cdf(dp) - K * math.exp(-r * tau) * stats.norm.cdf(dm)
t, s, r, sig = 0.3, 1.1, 0.03, 0.25
h = 1e-4
Ct = (C(t + h, s) - C(t - h, s)) / (2 * h); Cs = (C(t, s + h) - C(t, s - h)) / (2 * h); Css = (C(t, s + h) - 2 * C(t, s) + C(t, s - h)) / h ** 2
check("Black-Scholes PDE residual", Ct + r * s * Cs + sig ** 2 * s ** 2 / 2 * Css - r * C(t, s), 0.0, 1e-5)
tau = 0.7; dp = (math.log(s) + (r + sig ** 2 / 2) * tau) / (sig * math.sqrt(tau)); dm = dp - sig * math.sqrt(tau)
check("delta = Phi(d+)", Cs, stats.norm.cdf(dp), 1e-6)
check("s phi(d+) = K e^{-r tau} phi(d-)", s * stats.norm.pdf(dp), math.exp(-r * tau) * stats.norm.pdf(dm), 1e-12)
vega = (C(t, s, sig=sig + h) - C(t, s, sig=sig - h)) / (2 * h)
check("vega = s phi(d+) sqrt(tau)", vega, s * stats.norm.pdf(dp) * math.sqrt(tau), 1e-6)
Z = np.random.default_rng(6).normal(size=2_000_000)
mc = math.exp(-r * tau) * np.mean(np.maximum(s * np.exp(sig * math.sqrt(tau) * Z + (r - sig ** 2 / 2) * tau) - 1, 0))
check("C as a discounted risk-neutral expectation (MC)", mc, C(t, s), 2e-3)
# Bessel scale functions: L z^p = 0 for p = 1 - delta/2, L log z = (delta-2)/z
for delta in (0.5, 1, 3, 4.5):
    p = 1 - delta / 2; z = 1.7
    check(f"L s = 0, delta={delta}", delta * p * z ** (p - 1) + 2 * z * p * (p - 1) * z ** (p - 2), 0.0, 1e-12)
# McKean: sum b_i^2 = S, and drift of sum x_i^2 = n^2
rng = np.random.default_rng(7)
for n in (2, 3, 5, 8):
    x = np.sort(rng.normal(size=n) * 3)
    b = np.array([sum(1 / (x[i] - x[k]) for k in range(n) if k != i) for i in range(n)])
    S = sum(1 / (x[i] - x[k]) ** 2 for i in range(n) for k in range(n) if i != k)
    check(f"sum b_i^2 = S (n={n})", float(np.sum(b ** 2)), S, 1e-9 * S)
    check(f"n + 2 sum x_i b_i = n^2 (n={n})", n + 2 * float(np.sum(x * b)), n * n, 1e-9)
# 2x2: gap of a traceless Hermitian matrix is 2 sqrt(a^2+|c|^2)
a, c = 0.3, 0.4 - 0.2j
ev = np.linalg.eigvalsh(np.array([[a, c], [np.conj(c), -a]]))
check("2x2 gap", ev[1] - ev[0], 2 * math.sqrt(a * a + abs(c) ** 2), 1e-12)
# Exercise ex:emgbm probabilities
check_true(f"P(B_1 >= 1/2 - log 2) = {stats.norm.sf(0.5 - math.log(2)):.4f} > 0.57", stats.norm.sf(0.5 - math.log(2)) > 0.57)
q = 2 * (stats.norm.cdf(2 / math.sqrt(0.5)) - stats.norm.cdf(0.5 / math.sqrt(0.5)))
check_true(f"P(|N(0,1/2)| in [1/2,2]) = {q:.4f} > 0.47", q > 0.47)
check_true("0.57 + 0.47 + 0.99 - 2 >= 0.03", 0.57 + 0.47 + 0.99 - 2 >= 0.03 - 1e-12)
check("E (dB)^6 = 15 h^3", 15.0, float(np.prod([5, 3, 1])), 0)
# Euler-Maruyama error order for GBM (simulated): E|X_1 - X^h_1|^2 / h roughly constant
errs = []
for hh in (1 / 64, 1 / 256):
    m = int(1 / hh); dB = rng.normal(scale=math.sqrt(hh), size=(20000, m))
    errs.append(np.mean((np.exp(dB.sum(1) - 0.5) - np.prod(1 + dB, axis=1)) ** 2) / hh)
check_true(f"E|X_1-X^h_1|^2/h stable across h ({errs[0]:.3f}, {errs[1]:.3f})", 0.6 < errs[0] / errs[1] < 1.6)
# Langevin 1908 to Ornstein-Uhlenbeck 1930; Black died 1995, Nobel 1997
check("Langevin's paper three years after Einstein's", 1908 - 1905, 3, 0)
finish()
