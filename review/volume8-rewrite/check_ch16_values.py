#!/usr/bin/env python3
"""Volume 8, Chapter 16: Welch equality cases, equiangular lines in R^2 and R^3, the majorant of the mean value problem,
the constants of its part (c), Ramanujan's sigma(n)/n mean, the Mellin-Plancherel constant, van de Lune's threshold,
the extremes of |zeta(2+it)|, the Cantor measure coefficient, the Bergman norm of z and the Sobolev kernel."""
from math import pi, sqrt, log, cos, sinh, cosh
import numpy as np, mpmath as mp
from scipy.integrate import quad
from sympy import primerange, divisor_sigma
from common import check, check_true, finish
mp.mp.dps = 30
# Welch: three planar vectors, six icosahedron diagonals
U3 = np.array([[cos(2*pi*k/3), np.sin(2*pi*k/3)] for k in range(3)])
eps = max(abs(U3[i] @ U3[j]) for i in range(3) for j in range(3) if i != j)
check("planar triple: eps^2 = (R-n)/(n(R-1))", eps**2, (3 - 2)/(2*2), 1e-12)
phi = (1 + sqrt(5))/2
V = np.array([[0, 1, phi], [0, 1, -phi], [1, phi, 0], [1, -phi, 0], [phi, 0, 1], [-phi, 0, 1]]); V = V/np.linalg.norm(V, axis=1)[:, None]
G = np.abs(V @ V.T); off = G[~np.eye(6, dtype=bool)]
check("icosahedron diagonals: all |<u_i,u_j>| = 1/sqrt5", max(abs(off - 1/sqrt(5))), 0, 1e-12)
check("Welch bound for R = 6, n = 3", 3/(3*5), (1/sqrt(5))**2, 1e-12)
check("angle arccos(1/sqrt5) in degrees", np.degrees(np.arccos(1/sqrt(5))), 63.4, 0.05)
check("Gerzon n(n+1)/2 for n = 3", 6, 3*4//2, 0)
# majorant
Delta, T, Uu = 1.0, 6.0, 2.0
k = lambda v: Delta*np.sinc(Delta*v)**2
w = lambda t: quad(k, t - T - Uu, t + Uu, limit=400)[0]
mn = min(w(t) for t in np.linspace(0, T, 61))
check_true(f"majorant >= 1 - 2/(pi^2 Delta U) = {1 - 2/(pi**2*Delta*Uu):.4f} on [0,T] (min {mn:.4f})", mn >= 1 - 2/(pi**2*Delta*Uu))
check("1 - 2/(pi^2 U) at U = 2", 1 - 2/(pi**2*2), 0.90, 0.005)
check("pi/(pi-1)", pi/(pi - 1), 1.467, 5e-4); check("1.467 * 4/pi", 1.467*4/pi, 1.868, 5e-4)
check_true("1.868 * 1.5 <= 2.81", 1.868*1.5 <= 2.81)
# Ramanujan
N = 2000000; sig = np.zeros(N + 1)
for d in range(1, N + 1): sig[d::d] += d
val = np.mean((sig[1:]/np.arange(1, N + 1))**2)
check("(1/N) sum (sigma(n)/n)^2 at N = 2e6", val, 3.00510, 5e-5)
check("5/2 zeta(3)", 2.5*float(mp.zeta(3)), 3.00514, 1e-5)
# Mellin-Plancherel
check("log(2 pi) - gamma", log(2*pi) - float(mp.euler), 1.2606, 1e-4)
I = mp.quad(lambda t: abs(mp.zeta(0.5 + 1j*t))**2/(0.25 + t*t), [0, 10, 50, 200, 1000])*2/(2*mp.pi)
check_true(f"(1/2pi) int |zeta(1/2+it)|^2/(1/4+t^2) over |t| <= 1000 = {float(I):.4f}, below and close to 1.2606", 1.25 < I < 1.2606)
# van de Lune
f = lambda s: sum(mp.asin(mp.mpf(p)**-s) - mp.mpf(p)**-s for p in primerange(2, 10**5)) + mp.primezeta(s) - mp.pi/2
s0 = mp.findroot(f, 1.19)
check("van de Lune threshold (prime zeta plus arcsin corrections)", s0, mp.mpf("1.19234733718619303"), 1e-15)
# zeta(2+it) extremes
check("zeta(2) = pi^2/6", float(mp.zeta(2)), 1.6449, 1e-4); check("zeta(4)/zeta(2) = pi^2/15", float(mp.zeta(4)/mp.zeta(2)), 0.6579, 1e-4)
check_true("|zeta(2+it)| stays within [pi^2/15, pi^2/6] on a sample", all(pi**2/15 - 1e-12 <= abs(mp.zeta(2 + 1j*t)) <= pi**2/6 + 1e-12 for t in np.linspace(0.1, 200, 400)))
# Cantor measure
check("|mu^(1)| = prod |cos(2 pi 3^-j)|", float(mp.nprod(lambda j: abs(mp.cos(2*mp.pi*mp.mpf(3)**-j)), [1, mp.inf])), 0.37143, 1e-5)
# Bergman: ||z||^2 = pi/2, area of disc
check("int_D |z|^2 dA = pi/2", quad(lambda r: r**2*2*pi*r, 0, 1)[0], pi/2, 1e-12)
# Sobolev kernel on [0, L]
L = 2.0; y = 0.7
K = lambda x: cosh(min(x, y))*cosh(L - max(x, y))/sinh(L)
check("K_y(y) = cosh y cosh(L-y)/sinh L <= coth L", max(K(t) for t in np.linspace(0, L, 201)), max(cosh(t)*cosh(L - t)/sinh(L) for t in [y]), 1e-12)
check("sup_y K_y(y) = coth L (at the ends)", max(cosh(t)*cosh(L - t)/sinh(L) for t in np.linspace(0, L, 2001)), cosh(L)/sinh(L), 1e-12)
check("K_(L/2)(L/2) = (1/2) coth(L/2)", cosh(L/2)**2/sinh(L), 0.5*cosh(L/2)/sinh(L/2), 1e-12)
finish()
