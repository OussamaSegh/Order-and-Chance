"""Volume 12, Chapter 2 (fine structure): the constants of Lemma hitprob, the count E N_n in Theorem dimension, the joint
reflection density, the bridge maximum, the arcsine law for zeros, and the walk-zero asymptotics; plus a simulated modulus."""
import math
import numpy as np
from scipy import integrate, stats
from common import check, check_true, finish

# Lemma hitprob: 4/sqrt(2 pi a) * sqrt(2h/pi) = (4/pi) sqrt(h/a)
a, h = 0.7, 0.01
check("zero-hitting constant", 4 / math.sqrt(2 * math.pi * a) * math.sqrt(2 * h / math.pi), 4 / math.pi * math.sqrt(h / a), 1e-15)
check("E|B_h| = sqrt(2h/pi)", integrate.quad(lambda x: abs(x) * stats.norm.pdf(x, scale=math.sqrt(h)), -1, 1)[0], math.sqrt(2 * h / math.pi), 1e-10)
check_true("sum_{j<n} j^-1/2 <= 2 sqrt n", all(sum(j ** -0.5 for j in range(1, n)) <= 2 * math.sqrt(n) for n in range(2, 3000, 37)))
# exact probability that B has a zero in [a, a+h]: 1 - (2/pi) arcsin sqrt(a/(a+h)) <= (4/pi) sqrt(h/a)
for a, h in [(0.5, 0.01), (0.1, 0.05), (1, 1)]:
    exact = 1 - 2 / math.pi * math.asin(math.sqrt(a / (a + h)))
    check_true(f"exact zero probability {exact:.4f} <= bound, a={a}, h={h}", exact <= 4 / math.pi * math.sqrt(h / a))
# joint density of (M_t, B_t) integrates to 1, and marginal of M - B is that of |B_t|
t = 1.3
f = lambda b, a: 2 * (2 * a - b) / math.sqrt(2 * math.pi * t ** 3) * math.exp(-(2 * a - b) ** 2 / (2 * t))
tot = integrate.dblquad(f, 0, 12, lambda a: -12, lambda a: a)[0]
check("joint reflection density has mass 1", tot, 1.0, 1e-6)
y = 0.4
m = integrate.quad(lambda a: f(a - y, a), 0, 20)[0]
check("density of M-B at y = density of |B_t|", m, 2 * stats.norm.pdf(y, scale=math.sqrt(t)), 1e-8)
# bridge maximum: P(max >= a) = exp(-2a^2), simulated
rng = np.random.default_rng(2)
n, N = 4000, 4000
W = np.cumsum(rng.normal(scale=math.sqrt(1 / n), size=(N, n)), axis=1)
br = W - np.outer(np.ones(N), np.arange(1, n + 1) / n) * W[:, -1:]
check("P(bridge max >= 0.8) ~ exp(-1.28)", np.mean(br.max(axis=1) >= 0.8), math.exp(-2 * 0.64), 0.03)
# arcsine law for no zero in ]a,b[
a_, b_ = 0.3, 1.0
Z = rng.normal(size=(2, 400000))
check("P(no zero in ]a,b[) = (2/pi) arcsin sqrt(a/b)", np.mean(np.abs(math.sqrt(b_ - a_) * Z[1]) < np.abs(math.sqrt(a_) * Z[0])), 2 / math.pi * math.asin(math.sqrt(a_ / b_)), 0.003)
# walk zeros: E Z_{2n} ~ 2 sqrt(n/pi)
n = 200000
u = 1.0; s = 0.0
for j in range(1, n + 1):
    u *= (2 * j - 1) / (2 * j); s += u
check("E Z_2n / (2 sqrt(n/pi)) -> 1", s / (2 * math.sqrt(n / math.pi)), 1.0, 0.005)
# simulated Levy modulus on 2^16 points, h = 2^-8: ratio of max increment to psi(h) near 1
n = 2 ** 16
B = np.concatenate([[0], np.cumsum(rng.normal(scale=math.sqrt(1 / n), size=n))])
k = 2 ** 8
hh = k / n
ratio = np.max(np.abs(B[k:] - B[:-k])) / math.sqrt(2 * hh * math.log(1 / hh))
check_true(f"simulated Levy ratio at h=2^-8 is between 0.6 and 1.3 ({ratio:.3f})", 0.6 < ratio < 1.3)
finish()
