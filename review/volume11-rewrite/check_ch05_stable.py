"""Volume 11, Chapter 5 (Infinitely divisible and stable laws): Schlomilch's integrals, the hitting-time law (density, tail,
Laplace transform, median, mode), the hitting-time theorem P(tau_n=k) = (n/k) P(S_k=n) by dynamic programming, the Cauchy
Levy measure, kappa_1, the Levy measures of T_1 and of the gamma law, and the inequality 1 - sin y/y >= c0 y^2/(1+y^2)."""
import math
import numpy as np
from scipy import integrate, stats
from common import check, check_true, finish

for p, q in [(1.0, 1.0), (0.3, 2.0), (2.5, 0.7)]:
    J12 = integrate.quad(lambda t: t ** -0.5 * math.exp(-p * t - q / t), 0, np.inf)[0]
    J32 = integrate.quad(lambda t: t ** -1.5 * math.exp(-p * t - q / t), 0, np.inf)[0]
    check(f"Schlomilch J_1/2 at p={p}, q={q}", J12, math.sqrt(math.pi / p) * math.exp(-2 * math.sqrt(p * q)), 1e-8)
    check(f"Schlomilch J_3/2 at p={p}, q={q}", J32, math.sqrt(math.pi / q) * math.exp(-2 * math.sqrt(p * q)), 1e-8)
dens = lambda t, a=1.0: a / math.sqrt(2 * math.pi) * t ** -1.5 * math.exp(-a * a / (2 * t))
check("T_1 density integrates to 1", integrate.quad(dens, 0, np.inf)[0], 1.0, 1e-8)
for lam in [0.1, 1.0, 3.0]:
    check(f"E exp(-lambda T_2) at lambda={lam}", integrate.quad(lambda t: math.exp(-lam * t) * dens(t, 2.0), 0, np.inf)[0], math.exp(-2 * math.sqrt(2 * lam)), 1e-8)
t = 1e6; check("P(T_1>t) ~ sqrt(2/(pi t)) at t=1e6 (ratio)", (2 * stats.norm.cdf(t ** -0.5) - 1) / math.sqrt(2 / (math.pi * t)), 1.0, 1e-6)
med = 1 / stats.norm.ppf(0.75) ** 2; check("median of T_1 = 1/Phi^{-1}(3/4)^2", med, 2.2, 0.005)
ts = np.linspace(0.05, 2, 200001); check("mode of the Levy density", ts[np.argmax([dens(x) for x in ts])], 1 / 3, 1e-4)
# hitting-time theorem for the coin walk, n=20
n, K = 20, 4000
P = np.zeros(2 * K + 3); P[K + 1] = 1.0  # position offset K+1
first = np.zeros(K + 1)
for k in range(1, K + 1):
    newP = np.zeros_like(P); newP[1:] += 0.5 * P[:-1]; newP[:-1] += 0.5 * P[1:]
    first[k] = newP[K + 1 + n]; newP[K + 1 + n] = 0.0; P = newP
ok = all(abs(first[k] - n / k * (math.comb(k, (k + n) // 2) / 2 ** k if (k + n) % 2 == 0 else 0)) < 1e-14 for k in range(1, 1200))
check_true("P(tau_20 = k) = (20/k) P(S_k = 20), k < 1200", ok)
# Cauchy Levy measure and kappa_1
import mpmath
k1 = float(mpmath.quadosc(lambda u: (1 - mpmath.cos(u)) / u ** 2, [0, mpmath.inf], period=2 * mpmath.pi))
check("int (1-cos u)/u^2 over R = pi", 2 * k1, math.pi, 1e-10)
check("kappa_1 = pi/2", k1, math.pi / 2, 1e-10)
for lam in [0.5, 2.0]:
    check(f"Levy measure of T_1: int (1-e^-lx) dx/(sqrt(2pi) x^1.5) = sqrt(2l), l={lam}", integrate.quad(lambda x: (1 - math.exp(-lam * x)) / (math.sqrt(2 * math.pi) * x ** 1.5), 0, np.inf)[0], math.sqrt(2 * lam), 1e-7)
    check(f"gamma Levy measure: int (1-e^-lx) e^-x/x = log(1+l), l={lam}", integrate.quad(lambda x: (1 - math.exp(-lam * x)) * math.exp(-x) / x, 0, np.inf)[0], math.log(1 + lam), 1e-8)
ys = np.linspace(1e-3, 200, 200000)
ratio = (1 - np.sin(ys) / ys) / (ys ** 2 / (1 + ys ** 2))
check_true("1 - sin y/y >= c0 y^2/(1+y^2) with c0 > 0 (min ratio on (0,200])", ratio.min() > 0.1)
check_true("1 - sin y/y >= 1/2 for |y| >= 2", np.all(1 - np.sin(ys[ys >= 2]) / ys[ys >= 2] >= 0.5))
# Example ex:lkexamples (c): Gaussian part of theta = sigma^2/6
check("t^2 - (1/2) int_{-1}^1 (t+s)^2 ds = -1/3 (t=0.7)", 0.7 ** 2 - 0.5 * integrate.quad(lambda s: (0.7 + s) ** 2, -1, 1)[0], -1 / 3, 1e-12)
finish()
