"""Chapter 11 (mod-phi): check every printed number."""
import math
from mpmath import mp, mpf, euler, gamma as G, harmonic, log, zeta, sqrt, pi, stirling1
from sympy import primerange
from common import check, check_true, finish
mp.dps = 25

check("loglog 1e100", math.log(math.log(1e100)), 5.4, 0.05)
check("H_1e6", float(harmonic(10 ** 6)), 14.4, 0.05)
check("e^-gamma/Gamma(2)", float(mp.exp(-euler) / G(2)), 0.56, 0.005)
check("e^{gamma/2}/Gamma(1/2)", float(mp.exp(euler / 2) / G(0.5)), 0.75, 0.005)
check("loglog 1e8", math.log(math.log(1e8)), 2.9, 0.05)
ps = list(primerange(2, 30))
check_true("2*3*...*23 > 1e8 >= 2*...*19", math.prod(ps[:9]) > 1e8 >= math.prod(ps[:8]))
# k! <= e sqrt k (k/e)^k
check_true("k! <= e sqrt(k) (k/e)^k, k=1..200", all(math.lgamma(k + 1) <= 1 + 0.5 * math.log(k) + k * math.log(k) - k + 1e-12 for k in range(1, 201)))
# local-theorem constants: 2 eps int e^{-2k th^2/pi^2} = 2 eps sqrt(pi^3/(2k))
k = 7
check("Gaussian integral", float(mp.quad(lambda t: mp.exp(-2 * k * t * t / pi ** 2), [-mp.inf, mp.inf])), float(sqrt(pi ** 3 / (2 * k))), 1e-15)
check("e sqrt(k)/(2pi) * 2 sqrt(pi^3/2k)", float(mp.e * sqrt(k) / (2 * pi) * 2 * sqrt(pi ** 3 / (2 * k))), float(mp.e * sqrt(pi / 2)), 1e-15)
check_true("1-cos t >= 2t^2/pi^2 on [-pi,pi]", all(1 - math.cos(t) >= 2 * t * t / math.pi ** 2 - 1e-15 for t in [i * math.pi / 1000 for i in range(-1000, 1001)]))
# log cos u expansion, log(sin v / v)
u = mpf("0.01")
check("log cos u = -u^2/2 - u^4/12", float((log(mp.cos(u)) + u * u / 2) / (-u ** 4 / 12)), 1, 1e-3)
check("log sin v/v = -v^2/6 - v^4/180", float((log(mp.sin(u) / u) + u * u / 6) / (-u ** 4 / 180)), 1, 1e-3)
check("pi^2/120 = zeta(2)/20", float(zeta(2) / 20), float(pi ** 2 / 120), 1e-15)
check("pi^2/72 = zeta(2)/12", float(zeta(2) / 12), float(pi ** 2 / 72), 1e-15)
check("kappa4 sign", 1 - 3, -2, 0)
check("kappa4 uniform", 9 / 5 - 3, -6 / 5, 1e-15)
# Weierstrass product = e^{-gamma w}/Gamma(w+1)
w = mpf("0.7")
prod = mp.nprod(lambda j: (1 + w / j) * mp.exp(-w / j), [1, mp.inf])
check("Weierstrass product", float(prod), float(mp.exp(-euler * w) / G(w + 1)), 1e-8)
# cycles generating function and Stirling asymptotic sanity: P(K_n=k)=|s(n,k)|/n!
n = 12
check_true("sum |s(n,k)| = n!", sum(abs(int(stirling1(n, k))) for k in range(n + 1)) == math.factorial(n))
finish()
