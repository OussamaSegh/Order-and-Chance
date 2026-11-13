#!/usr/bin/env python3
"""Volume 9, Chapter 3: recompute the numbers and formulas printed without proof."""
import math, numpy as np, sympy as sp
from common import check, check_true, finish

x, y, t = sp.symbols('x y t', real=True)
rho = x**2 + y**2
check_true("d(theta) closed", sp.simplify(sp.diff(x/rho, x) + sp.diff(y/rho, y)) == 0)
# winding number of (cos2t + cos t/2, sin2t + sin t/2) around 0
T = np.linspace(0, 2*np.pi, 200001)
z = np.exp(2j*T) + 0.5*np.exp(1j*T)
check("winding number of the second curve", np.sum(np.diff(np.unwrap(np.angle(z))))/(2*np.pi), 2, 1e-9)
# shoelace on a segment: x dy - y dx pulls back to det(p,q)
p1, p2, q1, q2 = sp.symbols('p1 p2 q1 q2', real=True)
X = p1 + t*(q1-p1); Y = p2 + t*(q2-p2)
check_true("segment: x dy - y dx = det(p,q) dt", sp.expand(X*sp.diff(Y, t) - Y*sp.diff(X, t) - (p1*q2 - p2*q1)) == 0)
# volumes of balls
om = lambda n: math.pi**(n/2)/math.gamma(n/2+1)
for n, v in [(1, 2), (2, math.pi), (3, 4*math.pi/3), (4, math.pi**2/2), (5, 8*math.pi**2/15)]:
    check(f"omega_{n}", om(n), v, 1e-12)
check_true("omega_n is largest at n=5", max(range(1, 40), key=om) == 5)
check("omega_5", om(5), 5.26, 0.005)
check("omega_10 / 2^10", om(10)/2**10, 0.0025, 0.00005)
check("area of S^2 = 3 * 4pi/3", 3*om(3), 4*math.pi, 1e-12)
# sigma on R^n: d sigma = n dx  (coefficient check: sum of d/dx_i of x_i)
finish()
