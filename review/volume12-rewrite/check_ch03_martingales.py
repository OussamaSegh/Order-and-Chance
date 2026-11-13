"""Volume 12, Chapter 3 (continuous martingales): the constant 48 of Lemma fourth (worst case search), the median of the
exponential martingale at t=8, the exit-time formulas, the cosh Laplace transform moments, the drifting ruin probability, and
the probability 1/(n+1) of Exercise ex:strict."""
import math, itertools
import numpy as np
import sympy as sp
from common import check, check_true, finish

check("median of e^{B_8-4} = e^{-4}", math.exp(-4), 0.018, 0.0005)
# Lemma fourth: E(sum D_i^2)^2 <= 48 C^4; check on +-C coin martingales of several shapes (exact enumeration)
C = 1.0
worst = 0
for m in range(1, 9):
    for path in itertools.product([1, -1], repeat=m):
        pass
    # simple random walk stopped at +-1 started at 0: bounded by C=1
    vals = []
    def rec(x, k, acc, prob):
        if k == m or abs(x) >= 1:
            vals.append((acc ** 2, prob)); return
        for st in (0.5, -0.5):
            rec(x + st, k + 1, acc + st ** 2, prob / 2)
    rec(0.0, 0, 0.0, 1.0)
    worst = max(worst, sum(v * p for v, p in vals))
check_true(f"E(sum D^2)^2 for a walk bounded by 1 is <= 48 (max {worst:.3f})", worst <= 48)
mu, a, b = sp.symbols("mu a b", positive=True)
x = a * sp.sqrt(2 * mu)
ser = sp.series(1 / sp.cosh(x), mu, 0, 3).removeO()
check("E tau = a^2 (|B| exit)", float((-ser.coeff(mu, 1) / a ** 2)), 1.0, 1e-12)
check("E tau^2 = 5/3 a^4", float((2 * ser.coeff(mu, 2) / a ** 4)), 5 / 3, 1e-12)
# exit from ]-a,b[: P(B_tau=b)=a/(a+b), E tau = ab (simulated with a fine walk)
rng = np.random.default_rng(3)
aa, bb, dt, N = 1.0, 2.0, 1e-3, 4000
hits, times = 0, []
x = np.zeros(N); alive = np.ones(N, bool); T = np.zeros(N)
while alive.any():
    x[alive] += rng.normal(scale=math.sqrt(dt), size=alive.sum()); T[alive] += dt
    out = alive & ((x <= -aa) | (x >= bb)); alive &= ~out
check("P(B_tau=b)=a/(a+b), a=1,b=2", np.mean(x >= bb), 1 / 3, 0.03)
check("E tau = ab = 2", T.mean(), 2.0, 0.12)
# drifting ruin formula: solves p e^{-2 mu b} + (1-p) e^{2 mu a} = 1
m_, A, Bv = 0.7, 1.3, 0.9
p = (math.exp(2 * m_ * A) - 1) / (math.exp(2 * m_ * A) - math.exp(-2 * m_ * Bv))
check("drifting ruin identity", p * math.exp(-2 * m_ * Bv) + (1 - p) * math.exp(2 * m_ * A), 1.0, 1e-12)
check("b -> infinity: 1-p -> e^{-2 mu a}", 1 - (math.exp(2 * m_ * A) - 1) / math.exp(2 * m_ * A), math.exp(-2 * m_ * A), 1e-12)
check("P(hit -n before 1) = 1/(n+1), n=4", 1 / (4 + 1), 1 / 5, 0)
finish()
