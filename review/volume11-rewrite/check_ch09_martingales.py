"""Chapter 9 (martingales II): check every printed number."""
import math
import numpy as np
from math import comb, factorial
from fractions import Fraction
from common import check, check_true, finish

check("roulette (18/19)^20", (18 / 19) ** 20, 0.34, 0.005)

# peeking: |S_k|/sqrt k > 1.96 for some k <= K (Gaussian increments)
rng = np.random.default_rng(2026)
def rate(K, R=40000):
    hits = 0
    for _ in range(R // 4000):
        Z = rng.standard_normal((4000, K)).cumsum(1) / np.sqrt(np.arange(1, K + 1))
        hits += (np.abs(Z) > 1.96).any(1).sum()
    return hits / R
check("30 looks", rate(30), 0.28, 0.01)
check("100 looks", rate(100), 0.37, 0.01)

# Gaussian Hellinger affinity
from scipy.integrate import quad
from scipy.stats import norm
for a in [0.3, 1.0, 2.0]:
    rho = quad(lambda x: math.sqrt(norm.pdf(x) * norm.pdf(x - a)), -20, 20)[0]
    check("rho N(0,1),N(%s,1)" % a, rho, math.exp(-a * a / 8), 1e-9)
# coin affinity and expansion
e = 0.01
rho = (math.sqrt(1 + 2 * e) + math.sqrt(1 - 2 * e)) / 2
check("coin rho = sqrt(p q) sum", rho, math.sqrt(.5 * (.5 + e)) + math.sqrt(.5 * (.5 - e)), 1e-15)
check("coin rho ~ 1-e^2/2", (1 - rho) / (e * e / 2), 1, 1e-3)
check_true("eps_n = n^-1/2 /2 is a valid bias for n>=1", 0.5 * 1 ** -0.5 <= 0.5)
# Poisson affinity
lam, mu = 2.0, 5.0
rho = sum(math.sqrt(math.exp(-lam) * lam ** k / factorial(k) * math.exp(-mu) * mu ** k / factorial(k)) for k in range(120))
check("Poisson rho", rho, math.exp(-(math.sqrt(lam) - math.sqrt(mu)) ** 2 / 2), 1e-12)

# anytime test: M_n formula and martingale property
for n in range(0, 8):
    for s in range(n + 1):
        Mn = Fraction(2 ** n * factorial(s) * factorial(n - s), factorial(n + 1))
        up = Fraction(2 ** (n + 1) * factorial(s + 1) * factorial(n - s), factorial(n + 2))
        dn = Fraction(2 ** (n + 1) * factorial(s) * factorial(n + 1 - s), factorial(n + 2))
        assert (up + dn) / 2 == Mn
check_true("M_n martingale under fair coin (exact, n<8)", True)
check("M_0", 2 ** 0 * 1 * 1 / factorial(1), 1, 0)

# Polya urn a,b: sequence probability equals Beta ratio
a, b, n, s = 2, 3, 6, 2
seq = [1, 0, 1, 0, 0, 0]
p = Fraction(1); r = g = 0
for x in seq:
    if x: p *= Fraction(a + r, a + b + r + g); r += 1
    else: p *= Fraction(b + g, a + b + r + g); g += 1
B = lambda x, y: Fraction(factorial(x - 1) * factorial(y - 1), factorial(x + y - 1))
check_true("Polya(a,b) = B(a+s,b+n-s)/B(a,b)", p == B(a + s, b + n - s) / B(a, b))
# Polya (1,1): s!(n-s)!/(n+1)!
check_true("Polya(1,1)", B(1 + s, 1 + n - s) / B(1, 1) == Fraction(factorial(s) * factorial(n - s), factorial(n + 1)))
# sample variance identity
x = np.array([1.0, 4.0, 2.5, 7.0, -1.0])
lhs = sum((x[i] - x[j]) ** 2 for i in range(5) for j in range(i + 1, 5))
check("sum_{i<j}(xi-xj)^2 = n sum (xi-xbar)^2", lhs, 5 * ((x - x.mean()) ** 2).sum(), 1e-9)
finish()
