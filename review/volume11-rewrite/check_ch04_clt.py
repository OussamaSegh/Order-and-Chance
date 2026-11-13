"""Volume 11, Chapter 4 (The central limit theorem, sharpened): the Berry--Esseen constant 3.1 and its two parts, Esseen's lower
bound, the lattice lower bound, the inversion counts, Weldon's dice, the local-limit example, and Watson's integral."""
import itertools, math
import numpy as np
from scipy import integrate, special, stats
from common import check, check_true, finish

a = 4 / (3 * math.sqrt(math.pi)); b = 18 / (math.pi * math.sqrt(2 * math.pi))
check("Berry-Esseen first part 4/(3 sqrt pi)", a, 0.7523, 1e-4)
check("Berry-Esseen second part 18/(pi sqrt(2pi))", b, 2.2858, 1e-4)
check_true("sum < 3.1", a + b < 3.1)
check("int t^2 e^{-t^2/4} = 4 sqrt pi", integrate.quad(lambda t: t * t * math.exp(-t * t / 4), -np.inf, np.inf)[0], 4 * math.sqrt(math.pi), 1e-9)
check("Esseen lower bound (sqrt10+3)/(6 sqrt(2 pi))", (math.sqrt(10) + 3) / (6 * math.sqrt(2 * math.pi)), 0.4097, 1e-4)
check("lattice bound 1/(2 sqrt 2)", 1 / (2 * math.sqrt(2)), 0.35, 0.004)
check("1/sqrt(2 pi)", 1 / math.sqrt(2 * math.pi), 0.399, 0.0005)
# Lemma cfestimate checked on the coin and on an exponential-minus-one step, n = 10..200, |t| <= T
for name, phi, rho in [("coin", lambda s: np.cos(s), 1.0), ("Exp(1)-1", lambda s: np.exp(-1j * s) / (1 - 1j * s), 12 / math.e - 2)]:
    ok = True
    for n in [10, 20, 50, 200]:
        T = 4 * math.sqrt(n) / (3 * rho); t = np.linspace(-T, T, 4001)
        lhs = np.abs(phi(t / math.sqrt(n)) ** n - np.exp(-t ** 2 / 2)); rhs = rho * np.abs(t) ** 3 / (3 * math.sqrt(n)) * np.exp(-t ** 2 / 4)
        ok &= bool(np.all(lhs <= rhs + 1e-15))
    check_true(f"Lemma cfestimate for the {name} step", ok)
# Berry-Esseen bound against exact binomial distances (p=1/2 and 0.1, n <= 300): below 0.4748 rho/(sigma^3 sqrt n)
def kdist(n, p):
    k = np.arange(n + 1); pmf = stats.binom.pmf(k, n, p); cdf = np.cumsum(pmf)
    sd = math.sqrt(n * p * (1 - p)); x = (k - n * p) / sd
    return max(np.max(np.abs(cdf - stats.norm.cdf(x))), np.max(np.abs(cdf - pmf - stats.norm.cdf(x))))
ok = True
for p in [0.5, 0.1]:
    s = math.sqrt(p * (1 - p)); rho = p * (1 - p) * (p * p + (1 - p) ** 2)
    for n in range(1, 301):
        ok &= kdist(n, p) * math.sqrt(n) / (rho / s ** 3) <= 0.4748
check_true("binomial Kolmogorov distances below Shevtsova's constant (Figure)", ok)
check("p=1/2, n=300: sqrt n D_n", kdist(300, 0.5) * math.sqrt(300), 1 / math.sqrt(2 * math.pi), 0.01)
# inversions
def inv(pm): return sum(1 for i in range(len(pm)) for j in range(i + 1, len(pm)) if pm[i] > pm[j])
for n in range(1, 8):
    vals = [inv(pm) for pm in itertools.permutations(range(n))]
    check_true(f"inversions n={n}: mean n(n-1)/4, variance (2n^3+3n^2-5n)/72", abs(np.mean(vals) - n * (n - 1) / 4) < 1e-12 and abs(np.var(vals) - (2 * n ** 3 + 3 * n * n - 5 * n) / 72) < 1e-9)
check("10^6 keys: mean", 1e12 / 4, 2.5e11, 1e9)
check("10^6 keys: standard deviation", math.sqrt((2e18 + 3e12 - 5e6) / 72), 1.7e8, 0.05e8)
# Weldon's dice
obs = np.array([185, 1149, 3265, 5475, 6114, 5194, 3067, 1331, 403, 105, 14, 4, 0])
N = obs.sum(); check("Weldon: number of throws", N, 26306, 0)
pk = stats.binom.pmf(np.arange(13), 12, 1 / 3); exp = N * pk
check_true("Weldon: expected counts as printed", list(np.floor(exp + 0.5).astype(int)) == [203, 1216, 3345, 5576, 6273, 5018, 2927, 1255, 392, 87, 13, 1, 0])
check("Weldon: expected in cell 11", exp[11], 1.2, 0.05); check("Weldon: expected in cell 12", exp[12], 0.05, 0.005)
check("Weldon: one throw in cell 12 adds about 18", (1 - exp[12]) ** 2 / exp[12] - exp[12], 18, 0.5)
def merged(o, e): return np.append(o[:10], o[10:].sum()), np.append(e[:10], e[10:].sum())
o, e = merged(obs, exp); chi = np.sum((o - e) ** 2 / e)
check("Weldon: chi^2 over 11 cells", chi, 35.5, 0.05)
check("Weldon: p-value chi^2_10 (about 1e-4)", stats.chi2.sf(chi, 10), 1e-4, 0.3e-4)
phat = np.sum(np.arange(13) * obs) / (12 * N); check("Weldon: estimated p", phat, 0.3377, 1e-4)
o2, e2 = merged(obs, N * stats.binom.pmf(np.arange(13), 12, phat)); chi2 = np.sum((o2 - e2) ** 2 / e2)
check("Weldon: chi^2 with fitted p", chi2, 8.2, 0.05)
check("Pearson's odds 62499 to 1 correspond to P = 1.6e-5", 1 / 62500, 1.6e-5, 1e-12)
# local limit example
vals, pr = np.array([0, 1, 3]), np.array([0.5, 0.25, 0.25])
mu = vals @ pr; var = (vals ** 2) @ pr - mu ** 2
check("LLT example mean", mu, 1.0, 1e-15); check("LLT example variance", var, 1.5, 1e-15)
# Watson's integral and Polya's constant
from scipy.special import ellipk
# W = (sqrt6/(32 pi^3)) Gamma(1/24)Gamma(5/24)Gamma(7/24)Gamma(11/24)
G = special.gamma
W = math.sqrt(6) / (32 * math.pi ** 3) * G(1 / 24) * G(5 / 24) * G(7 / 24) * G(11 / 24)
check("Watson's integral", W, 1.5163, 1e-4)
check("return probability F = 1 - 1/W", 1 - 1 / W, 0.3405, 1e-4)
# numerical check of the triple integral: integrate over t1 analytically: int_{-pi}^{pi} dt/(a - cos t) = 2 pi/sqrt(a^2-1)
def inner(t2, t3):
    a = 3 - math.cos(t2) - math.cos(t3)
    return 3 * 2 * math.pi / math.sqrt(a * a - 1) if a > 1 else 0.0
num = integrate.dblquad(lambda t3, t2: inner(t2, t3), 0, math.pi, 0, math.pi, epsabs=1e-7)[0] * 4 / (2 * math.pi) ** 3
check("triple integral numerically", num, W, 2e-3)
finish()
