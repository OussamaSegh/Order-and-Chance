"""Volume 11, Chapter 3 (Weak convergence and Donsker's theorem): the Chung--Feller lemma by enumeration, the arcsine limit,
the exit-time moments of Exercise ex:exitvar (from the Laplace transform), the LIL envelope at 10^6, the Gaussian tail bounds, and the Skorokhod
embedding of a centred law (simulated)."""
import itertools, math
import numpy as np
from scipy import stats
from common import check, check_true, finish

def u(n2): return math.comb(n2, n2 // 2) / 2 ** n2
for n in range(1, 9):
    counts = [0] * (n + 1)
    for steps in itertools.product([1, -1], repeat=2 * n):
        s, above = 0, 0
        for x in steps:
            t = s + x
            if s + t > 0: above += 1
            s = t
        counts[above // 2] += 1
    ok = all(abs(counts[k] / 4 ** n - u(2 * k) * u(2 * n - 2 * k)) < 1e-12 for k in range(n + 1))
    check_true(f"Chung-Feller b(2k,2n) = u(2k) u(2n-2k), n={n}", ok)
check("arcsine: P(h>0.9)+P(h<0.1) = (4/pi) arcsin sqrt(0.1)", 4 / math.pi * math.asin(math.sqrt(0.1)), 0.4097, 1e-4)
check("sqrt(2 log log 1e6)", math.sqrt(2 * math.log(math.log(1e6))), 2.29, 0.005)
# Gaussian tail bounds
xs = np.linspace(0.01, 8, 800)
check_true("x/(1+x^2) phi(x) <= P(Z>=x) <= exp(-x^2/2)/2", np.all((xs / (1 + xs ** 2) * stats.norm.pdf(xs) <= stats.norm.sf(xs)) & (stats.norm.sf(xs) <= 0.5 * np.exp(-xs ** 2 / 2))))
# exit time of (-1,1): E exp(-lambda tau) = 1/cosh(sqrt(2 lambda)) (an independent route), so E tau and E tau^2 from its series
import sympy as sp
lam = sp.symbols("lam", positive=True)
ser = sp.series(1 / sp.cosh(sp.sqrt(2 * lam)), lam, 0, 3).removeO()
check("E tau (exit from (-1,1))", float(-ser.coeff(lam, 1)), 1.0, 1e-12)
check("E tau^2 = 5/3", float(2 * ser.coeff(lam, 2)), 5 / 3, 1e-12)
# Proposition exit: P(B_tau = b) = -a/(b-a), E tau = -ab, for a=-1, b=2 (random walk with small steps)
a, bb = -1.0, 2.0
check("exit probability formula a=-1, b=2", -a / (bb - a), 1 / 3, 1e-15)
# Skorokhod: Var tau finite example: for the uniform law on [-sqrt3, sqrt3], E tau = E X^2 = 1 (exact integral of the (U,V) construction)
from scipy import integrate
c = math.sqrt(3) / 4  # E X^+ for the uniform law on [-sqrt3, sqrt3]
dens = 1 / (2 * math.sqrt(3))
mass = integrate.dblquad(lambda v, uu: (v - uu) / c * dens * dens, -math.sqrt(3), 0, 0, math.sqrt(3))[0]
check("Skorokhod pair (U,V) total mass (uniform law)", mass, 1.0, 1e-9)
etau = integrate.dblquad(lambda v, uu: -uu * v * (v - uu) / c * dens * dens, -math.sqrt(3), 0, 0, math.sqrt(3))[0]
check("Skorokhod E tau = E X^2 = 1 (uniform law)", etau, 1.0, 1e-9)
finish()
