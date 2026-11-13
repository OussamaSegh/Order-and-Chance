"""Chapter 10 (ergodic theory): check every printed number."""
import math
from mpmath import mp, mpf, log, pi, nsum, inf, quad, khinchin, e as E, sqrt
from common import check, check_true, finish
mp.dps = 30

# Gauss measure of cylinder a1=k
for k in [1, 2, 5]:
    g = math.log2(1 + 1 / k) - math.log2(1 + 1 / (k + 1))
    check("gamma(a1=%d)" % k, g, math.log2(1 + 1 / (k * (k + 2))), 1e-15)
# Khinchin's constant
# the slowly convergent product: sum to 10^5, then the tail sum log k/(k^2 log 2) by an integral
N = 10 ** 5
S = sum(math.log(k) * math.log1p(1 / (k * (k + 2))) for k in range(1, N))
S += float(quad(lambda t: log(t) / t ** 2, [N - 0.5, inf]))
K = math.exp(S / math.log(2))
check("Khinchin K (truncated 2.68545...)", K, 2.685452, 2e-6)
check("mpmath khinchin agrees", float(khinchin), K, 2e-6)
# Levy constant
L = pi ** 2 / (12 * log(2))
check_true("Levy 1.18656... (%.8f)" % float(L), str(float(L)).startswith("1.18656"))
I = quad(lambda x: -log(x) / ((1 + x) * log(2)), [0, 1])
check("int -log x dgamma", float(I), float(L), 1e-20)
check("int x^j log(1/x)", float(quad(lambda x: x ** 3 * -log(x), [0, 1])), 1 / 16, 1e-20)
check("golden log phi", float(log((1 + sqrt(5)) / 2)), 0.4812, 5e-5)
check("2L", float(2 * L), 2.373, 5e-4)
check("e^{2L}", float(mp.exp(2 * L)), 10.73, 0.005)
check("e^{2.37}~10.7", math.exp(2.37), 10.7, 0.05)

# continued fraction of e-2
x = E - 2; digs = []
for _ in range(8):
    x = 1 / x; a = int(mp.floor(x)); digs.append(a); x -= a
check_true("e-2 = [0;1,2,1,1,4,1,1,6,...] (%s)" % digs, digs == [1, 2, 1, 1, 4, 1, 1, 6])

# HH: mean return 4 (Kac), first occurrence 6
check("Kac 1/mu(A)", 1 / 0.25, 4, 0)
check("HH from scratch (2+4)", 2 + 4, 6, 0)  # Volume 4 monkey formula: 2^1+2^2
# rotation: lambda(A cap (A - t)) = 1/2 - |t| for |t|<=1/2
check("overlap at shift 1/8", 0.5 - 0.125, 0.375, 0)
# bounded distortion: q_n/(q_n+q_{n-1}) >= 1/2
# Cantor-type base-3 set has density 0: count up to 3^m is 2^m
check_true("density of {0,1}-digit base-3 integers -> 0", 2 ** 20 / 3 ** 20 < 1e-3)
# gas: 2^-N
finish()
