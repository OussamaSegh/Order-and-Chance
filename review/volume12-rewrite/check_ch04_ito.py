"""Volume 12, Chapter 4 (the Ito integral): Doeblin's age in February 1940, the Burkholder constant (derivation and growth),
the three Riemann-sum conventions on a simulated path, moments of B_t, E L_t, and the exponential-martingale bound."""
import math
import numpy as np
from scipy import stats, special
from common import check, check_true, finish

# Doeblin: born 17 March 1915; pli cachete sent February 1940
check("Doeblin's age in February 1940", 1940 - 1915 - 1, 24, 0)
def Cp(p): return (p / 2 * (p - 1)) ** (p / 2) * (p / (p - 1)) ** (p * p / 2)
# derivation: (E M*^p)^{2/p} <= (p/(p-1))^p * p(p-1)/2 * (E<M>^{p/2})^{2/p}
for p in (2, 3, 4, 7):
    check(f"C_p from the derivation, p={p}", ((p / (p - 1)) ** p * p * (p - 1) / 2) ** (p / 2), Cp(p), 1e-9 * Cp(p))
check("C_2 = 4 (Doob)", Cp(2), 4.0, 1e-12)
rootCp = lambda p: math.sqrt(p / 2 * (p - 1)) * (p / (p - 1)) ** (p / 2)
r = [rootCp(p) / p for p in (20, 40, 80, 160)]
check_true(f"p-th root of C_p grows like p ({[round(x, 3) for x in r]})", max(r) / min(r) < 1.3)
br = [math.exp((p / 2 * math.log(2) + special.gammaln((p + 1) / 2) - 0.5 * math.log(math.pi)) / p) / math.sqrt(p / math.e) for p in (40, 160, 640)]
check_true(f"(E|B_1|^p)^(1/p) ~ sqrt(p/e) ({[round(x, 3) for x in br]})", abs(br[-1] - 1) < 0.05)
# Riemann sums along one path on [0,2] with 2^12 steps
rng = np.random.default_rng(4)
n, T = 2 ** 12, 2.0
dB = rng.normal(scale=math.sqrt(T / n), size=n); B = np.concatenate([[0], np.cumsum(dB)])
ito = np.sum(B[:-1] * dB); strat = np.sum(0.5 * (B[:-1] + B[1:]) * dB); right = np.sum(B[1:] * dB)
check("Stratonovich sum = B_T^2/2 exactly", strat, B[-1] ** 2 / 2, 1e-10)
check("Ito sum ~ (B_T^2 - T)/2", ito, (B[-1] ** 2 - T) / 2, 0.1)
check("right sum ~ (B_T^2 + T)/2", right, (B[-1] ** 2 + T) / 2, 0.1)
# moments: E B_t^4 = 3t^2 from the recursion; E L_t = sqrt(2t/pi)
t = 1.7
m2 = t; m4 = 2 * 3 * (t ** 2 / 2)
check("E B_t^4 by the recursion", m4, 3 * t ** 2, 1e-12)
check("E|B_t| = sqrt(2t/pi)", math.sqrt(t) * math.sqrt(2 / math.pi), math.sqrt(2 * t / math.pi), 1e-15)
# exponential bound: 2 P(B_c >= a) <= e^{-a^2/2c}? (sharp up to polynomial factor)
for a, c in [(1, 1), (3, 1), (5, 2)]:
    check_true(f"P(max B >= a) <= exp(-a^2/2c), a={a}, c={c}", 2 * stats.norm.sf(a / math.sqrt(c)) <= math.exp(-a * a / (2 * c)))
finish()
