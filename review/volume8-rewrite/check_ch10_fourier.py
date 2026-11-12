#!/usr/bin/env python3
"""Volume 8, Chapter 10: the Gaussian and Cauchy transforms, the Hermite norms and eigenvalues, the coth sum, the sharpness of
Hausdorff-Young on Gaussians, the hexagonal theta identity and its derivative at the fixed point, the sinc sampling formula."""
from math import pi, sqrt, exp, log, cosh, sinh
import numpy as np, mpmath as mp
from scipy.integrate import quad
from common import check, check_true, finish
def ft(f, xi, L=40):
    return complex(quad(lambda x: f(x)*np.cos(2*pi*x*xi), -L, L, limit=400)[0], -quad(lambda x: f(x)*np.sin(2*pi*x*xi), -L, L, limit=400)[0])
for xi in (0, 0.7, 1.3): check(f"Gaussian transform at {xi}", ft(lambda x: exp(-pi*x*x), xi).real, exp(-pi*xi*xi), 1e-10)
a = 0.8
for xi in (0, 0.5, 2.0): check(f"transform of e^(-2 pi a|x|) at {xi}", ft(lambda x: exp(-2*pi*a*abs(x)), xi).real, a/(pi*(a*a + xi*xi)), 1e-8)
# Hermite: g_n = (A^dagger)^n e^{-pi x^2}, norms and F g_n = (-i)^n g_n
def g(n):
    import sympy as sp
    t = sp.symbols("t"); e = sp.exp(-sp.pi*t**2)
    for _ in range(n): e = sp.simplify(2*sp.pi*t*e - sp.diff(e, t))
    return sp.lambdify(t, e, "mpmath"), e
for n in range(5):
    f, e = g(n); nrm = mp.quad(lambda t: f(t)**2, [-mp.inf, mp.inf])
    check(f"||g_{n}||^2 = (4 pi)^n n!/sqrt 2", float(nrm), float((4*mp.pi)**n*mp.factorial(n)/mp.sqrt(2)), 1e-8*float(nrm))
    for xi in (0.3, 1.1):
        F = mp.quad(lambda t: f(t)*mp.exp(-2j*mp.pi*t*xi), [-mp.inf, mp.inf])
        check(f"F g_{n} = (-i)^{n} g_{n} at {xi}", abs(complex(F) - complex((-1j)**n*f(xi))), 0, 1e-9)
# coth sum
for aa in (0.3, 1.0, 2.5):
    check(f"sum 1/(n^2+a^2) = (pi/a) coth(pi a), a = {aa}", float(mp.nsum(lambda n: 1/(n*n + aa*aa), [-mp.inf, mp.inf])), pi/aa*cosh(pi*aa)/sinh(pi*aa), 1e-10)
# Hausdorff-Young on Gaussians
for p in (1.2, 1.5, 1.9):
    q = p/(p - 1); r = q**(-1/(2*q)) / p**(-1/(2*p))
    check_true(f"p = {p}: ||gamma^||_p' / ||gamma||_p = {r:.4f} < 1, equals sqrt(p^(1/p)/p'^(1/p'))", r < 1 and abs(r - sqrt(p**(1/p)/q**(1/q))) < 1e-12)
# hexagonal lattice theta
A = np.array([[1, 0.5], [0, sqrt(3)/2]])
pts = [A @ np.array([m, n]) for m in range(-30, 31) for n in range(-30, 31)]
r2 = np.array([v @ v for v in pts])
theta = lambda t: float(np.exp(-pi*t*r2).sum())
check("covolume", abs(np.linalg.det(A)), sqrt(3)/2, 1e-12)
for t in (0.4, 1.0, 2.0): check(f"theta(t) = 2/(sqrt3 t) theta(4/(3t)) at t = {t}", theta(t), 2/(sqrt(3)*t)*theta(4/(3*t)), 1e-10)
t0 = 2/sqrt(3); h = 1e-5; d = (theta(t0 + h) - theta(t0 - h))/(2*h)
check("t0 theta'(t0) = -theta(t0)/2", t0*d, -theta(t0)/2, 1e-7)
D = np.linalg.inv(A).T
check_true("dual basis has |w|^2 = 4/3 and angle 120 degrees", np.allclose([D[:, 0] @ D[:, 0], D[:, 1] @ D[:, 1], D[:, 0] @ D[:, 1]], [4/3, 4/3, -2/3]))
# sampling: reconstruct a band-limited function from its samples
W = 1.0; f = lambda x: np.sinc(W*(x - 0.3))**2   # its transform is a triangle supported in [-W, W]
xs = np.linspace(-3, 3, 13); n = np.arange(-4000, 4001)
rec = [np.sum(f(n/(2*W))*np.sinc(2*W*xx - n)) for xx in xs]
check("sampling formula error", max(abs(np.array(rec) - f(xs))), 0, 1e-3)
# Paley-Wiener (b): F(iy) for the indicator of [-R, R]
R = 0.7
for y in (0.5, 2.0): check(f"F(iy) = sinh(2 pi R y)/(pi y) at y = {y}", quad(lambda x: np.exp(2*pi*x*y), -R, R)[0], sinh(2*pi*R*y)/(pi*y), 1e-9*sinh(2*pi*R*y))
finish()
