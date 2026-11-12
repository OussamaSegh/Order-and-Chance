#!/usr/bin/env python3
"""Volume 8, Chapter 11: the integral of psi_1 in Newton's potential, the H^1 norm identity, the Sobolev constant, the
sharp Poincare constant, the Gagliardo equality case, the convection-diffusion solution and its boundary layer,
the heat kernel equation, the principal value transform, and the order-1 lower bound."""
from math import pi, sqrt, exp, log, inf
import numpy as np, sympy as sp
from scipy.integrate import quad
from common import check, check_true, finish
r, u, t, x, b = sp.symbols("r u t x b", positive=True)
check_true("3 int r^2/(1+r^2)^(5/2) = 1", sp.simplify(3*sp.integrate(r**2/(1 + r**2)**sp.Rational(5, 2), (r, 0, sp.oo))) == 1)
eps = sp.symbols("epsilon", positive=True); g = -1/(4*sp.pi*sp.sqrt(r**2 + eps**2))
check_true("Laplacian of E_eps is 3 eps^2/(4 pi (r^2+eps^2)^(5/2))", sp.simplify(sp.diff(g, r, 2) + 2/r*sp.diff(g, r) - 3*eps**2/(4*sp.pi*(r**2 + eps**2)**sp.Rational(5, 2))) == 0)
# Sobolev constant C_s^2 = int (1+xi^2)^-s
for s in (0.75, 1.0, 2.0): check(f"C_s^2 for s = {s}", quad(lambda z: (1 + z*z)**-s, -inf, inf)[0], float(sp.sqrt(sp.pi)*sp.gamma(s - sp.Rational(1, 2))/sp.gamma(s)), 1e-8)
# Poincare: ||sin pi x||_2 / ||(sin pi x)'||_2 = 1/pi
check("Poincare ratio for sin(pi x)", sqrt(quad(lambda z: np.sin(pi*z)**2, 0, 1)[0] / quad(lambda z: (pi*np.cos(pi*z))**2, 0, 1)[0]), 1/pi, 1e-12)
# Gagliardo: e^{-|x|}
check("||e^-|x|||_2^2", quad(lambda z: exp(-2*abs(z)), -inf, inf)[0], 1, 1e-10)
# convection-diffusion with f = 1
for bb in (1.0, 20.0):
    r1 = (bb - sqrt(bb*bb + 4))/2; r2 = (bb + sqrt(bb*bb + 4))/2
    M = np.array([[1, 1], [np.exp(r1), np.exp(r2)]]); A, B = np.linalg.solve(M, [-1, -1])
    U = lambda z: 1 + A*np.exp(r1*z) + B*np.exp(r2*z)
    zz = np.linspace(0, 1, 11); h = 1e-4
    res = max(abs(-(U(z + h) - 2*U(z) + U(z - h))/h**2 + bb*(U(z + h) - U(z - h))/(2*h) + U(z) - 1) for z in zz[1:-1])
    check(f"b = {bb}: -u'' + b u' + u = 1", res, 0, 1e-4)
    if bb == 20.0:
        check_true("b = 20: away from x = 1, u is close to 1 - e^(-x/b)", abs(U(0.5) - (1 - exp(-0.5/bb))) < 1e-3)
        check_true("b = 20: u drops to 0 within a layer of width about 1/b at x = 1", U(1 - 3/bb) > 0.8*U(0.9) and abs(U(1)) < 1e-12)
# heat kernel
K = sp.exp(-x**2/(4*t))/sp.sqrt(4*sp.pi*t)
check_true("d_t K = d_x^2 K = (x^2/(4t^2) - 1/(2t)) K", sp.simplify(sp.diff(K, t) - sp.diff(K, x, 2)) == 0 and sp.simplify(sp.diff(K, t) - (x**2/(4*t**2) - 1/(2*t))*K) == 0)
# principal value transform: -2i int_eps^{1/eps} sin(2 pi x xi)/x dx -> -i pi sgn xi
from scipy.special import sici
for xi in (0.5, 3.0):
    e = 1e-6; val = -2*(sici(2*pi*xi/e)[0] - sici(2*pi*e*xi)[0])
    check(f"truncated p.v. transform at xi = {xi} (imaginary part)", val, -pi, 1e-3)
# p.v. is not of order 0: 2 int_{1/n}^{1/2} dx/x = 2 log(n/2)
for n in (10, 1000): check(f"2 int_(1/n)^(1/2) dx/x for n = {n}", 2*quad(lambda z: 1/z, 1/n, 0.5)[0], 2*log(n/2), 1e-9)
finish()
