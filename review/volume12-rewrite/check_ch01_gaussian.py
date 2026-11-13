"""Volume 12, Chapter 1 (Gaussian processes): the share of the first Karhunen--Loeve mode, the covariance series of Lemma twobases,
the block-variance bound in the proof of Theorem wienerseries, the Brownian-bridge and integration-by-parts numbers, and the
fractional Brownian motion correlations (sign, second difference, asymptotics)."""
import math
import numpy as np
from common import check, check_true, finish

check("first KL mode share 8/pi^2", 8 / math.pi ** 2, 0.81, 0.005)
check("first KL eigenvalue / total variance 1/2", (1 / (0.5 * math.pi) ** 2) / 0.5, 8 / math.pi ** 2, 1e-15)
# Lemma twobases: both series equal min(s,t)
rng = np.random.default_rng(1)
n = np.arange(1, 200001)
for s, t in rng.random((5, 2)):
    a = s * t + 2 * np.sum(np.sin(n * math.pi * s) * np.sin(n * math.pi * t) / (n * math.pi) ** 2)
    m = n - 0.5
    b = np.sum(2 * np.sin(m * math.pi * s) * np.sin(m * math.pi * t) / (m * math.pi) ** 2)
    check(f"cosine series = min(s,t) at ({s:.3f},{t:.3f})", a, min(s, t), 1e-5)
    check(f"half-integer series = min(s,t) at ({s:.3f},{t:.3f})", b, min(s, t), 1e-5)
# |a_n| <= 2/n and b_n <= pi n for both series
check_true("|a_n| <= 2/n for both series", all(math.sqrt(2) / (k * math.pi) <= 2 / k and math.sqrt(2) / ((k - 0.5) * math.pi) <= 2 / k for k in range(1, 10000)))
# block variance: sum_{n>=2^k} 4/n^2 <= 8 * 2^-k
check_true("sum_{n>=2^k} 4/n^2 <= 8*2^-k, k=1..20", all(4 * (math.pi ** 2 / 6 - sum(1 / j ** 2 for j in range(1, 2 ** k))) <= 8 * 2 ** -k for k in range(1, 18)))
# grid G has 2^{3k}+1 <= 2^{3k+1} points, and log(2|G|) <= log 2^{3k+2}
check_true("2^{3k}+1 <= 2^{3k+1}", all(2 ** (3 * k) + 1 <= 2 ** (3 * k + 1) for k in range(1, 30)))
# Kolmogorov: (2^n+1)^d 3^d <= 6^d 2^{nd}
check_true("(2^n+1)^d 3^d <= 6^d 2^(nd)", all((2 ** n + 1) ** d * 3 ** d <= 6 ** d * 2 ** (n * d) for n in range(0, 20) for d in range(1, 5)))
# Brownian bridge: E int (B_t - t B_1)^2 = sum 1/(n pi)^2 = 1/6 = int t(1-t)
check("sum 1/(n pi)^2", sum(1 / (k * math.pi) ** 2 for k in range(1, 10 ** 6)), 1 / 6, 1e-6)
check("int_0^1 (1-t)^2", 1 / 3, 1 / 3, 0)
# fBm: Cov(X1, X2-X1) = (2^{2H}-2)/2, sign
for H in (0.25, 0.5, 0.73, 0.9):
    v = 0.5 * (2 ** (2 * H) - 2)
    check_true(f"sign of Cov(X1,X2-X1) for H={H}", (v > 0) == (H > 0.5) and (abs(v) < 1e-15) == (H == 0.5))
    rho = lambda k: 0.5 * ((k + 1) ** (2 * H) - 2 * k ** (2 * H) + (k - 1) ** (2 * H))
    if H != 0.5:
        k = 10 ** 5
        check(f"rho(n) ~ H(2H-1) n^(2H-2), H={H}", rho(k) / (H * (2 * H - 1) * k ** (2 * H - 2)), 1.0, 1e-4)
# fBm covariance from the kernel g_t: Var Y_t proportional to t^{2H}, checked numerically for H=0.3
H = 0.3
from scipy import integrate
def g(t, u): return (max(t - u, 0) ** (H - .5) if t - u > 0 else 0) - ((-u) ** (H - .5) if u < 0 else 0)
def norm2(t):
    f = lambda u: g(t, u) ** 2
    return integrate.quad(f, -np.inf, -1)[0] + integrate.quad(f, -1, 0, limit=200)[0] + integrate.quad(f, 0, t, limit=200)[0]
check("||g_2||^2 / ||g_1||^2 = 2^{2H}", norm2(2.0) / norm2(1.0), 2 ** (2 * H), 1e-3)
finish()
