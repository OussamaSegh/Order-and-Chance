"""Volume 11, Chapter 2 (Laws of large numbers): the St Petersburg tail bounds and truncated moments, Etemadi's tail sum,
the Pareto mean, the laws of Exercises ex:feller and ex:seriesiid, and a simulation of Feller's theorem."""
import math
import numpy as np
from scipy import integrate
from common import check, check_true, finish

# St Petersburg: P(X >= 2^j) = 2^{1-j}; P(X > x) <= 2/x; P(X > x) >= 1/(2x) for x >= 2
def tail(x):  # P(X > x) = sum_{j: 2^j > x} 2^{-j}
    j = math.floor(math.log2(x)) + 1
    return 2.0 ** (1 - j)
xs = np.exp(np.linspace(math.log(2), math.log(1e9), 20000))
check_true("St Petersburg: 1/(2x) <= P(X>x) <= 2/x for 2 <= x <= 1e9", all(1 / (2 * x) <= tail(x) <= 2 / x for x in xs))
for b in [10.0, 1e3, 1e6, 1e9]:
    s2 = sum(2 ** j for j in range(1, 80) if 2 ** j <= b)
    check_true(f"E[X^2 1(X<=b)] <= 2b at b={b:g}", s2 <= 2 * b)
# Etemadi: sum_{k >= y, k >= 1} k^{-2} <= 2/y for y >= 1
check_true("sum_{k>=y} k^-2 <= 2/y on [1, 200]", all(sum(1 / k ** 2 for k in range(math.ceil(y), 20000)) + 1 / 20000 <= 2 / y for y in np.linspace(1, 200, 2000)))
# Pareto P(X>x) = x^{-3/2}: mean 3
check("Pareto mean", 1 + integrate.quad(lambda x: x ** -1.5, 1, np.inf)[0], 3.0, 1e-9)
# ex:feller (b): P(|X|>e) = 1
check("ex:feller law at x=e", math.e / (math.e * math.log(math.e)), 1.0, 1e-15)
# ex:seriesiid (b): E Y = 2e
# substitute y = e^u: int_t^oo e dy/(y log^2 y) = int_{log t}^oo e du/u^2
check("ex:seriesiid E Y", math.e + integrate.quad(lambda u: math.e / u ** 2, 1, np.inf)[0], 2 * math.e, 1e-9)
check("ex:seriesiid tail integral from t: e/log t (t=100)", integrate.quad(lambda u: math.e / u ** 2, math.log(100), np.inf)[0], math.e / math.log(100), 1e-9)
# Feller's theorem by simulation: S_n/(n log2 n) at n = 10^6, median over 200 players, close to 1
rng = np.random.default_rng(11)
n = 10 ** 6
ratios = []
for _ in range(200):
    j = rng.geometric(0.5, size=n)
    ratios.append(np.sum(2.0 ** j) / (n * math.log2(n)))
check("St Petersburg median S_n/(n log2 n), n=1e6 (convergence is slow: (log2 log2 n)/log2 n correction)", float(np.median(ratios)), 1.0, 0.25)
finish()
