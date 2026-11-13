#!/usr/bin/env python3
"""Volume 9, Chapter 4: recompute curvatures, the Gauss triangle excess and the torus spectrum facts."""
import math, sympy as sp
from scipy.integrate import quad
from common import check, check_true, finish

x, y, s, ph, r = sp.symbols('x y s phi r', positive=True)
def K(a, b, u, v):
    return sp.simplify(-1/(a*b)*(sp.diff(sp.diff(b, u)/a, u) + sp.diff(sp.diff(a, v)/b, v)))
check_true("sphere K = 1", K(1, sp.sin(ph), ph, x) == 1)
check_true("half-plane K = -1", K(1/y, 1/y, x, y) == -1)
check_true("polar plane K = 0", K(1, r, r, x) == 0)
R, a = sp.symbols('R a', positive=True)
rr = R + a*sp.cos(s/a)
check_true("torus K", sp.simplify(-sp.diff(rr, s, 2)/rr - sp.cos(s/a)/(a*rr)) == 0)
check_true("torus total curvature 0", sp.simplify(sp.integrate(-sp.diff(rr, s, 2), (s, 0, 2*sp.pi*a))) == 0)
# Gauss's triangle: area by Heron, excess in arc seconds
A, B, C = 69, 85, 107
p = (A+B+C)/2
area = math.sqrt(p*(p-A)*(p-B)*(p-C))
check("Heron area (km^2)", area, 2.9e3, 50)
check("excess in arc seconds", area/6371**2*180/math.pi*3600, 15, 0.5)
# pseudosphere: area 2 pi, volume pi/3
check("pseudosphere area", quad(lambda t: 2*math.pi*math.exp(-t), 0, 50)[0], 2*math.pi, 1e-9)
check("pseudosphere volume", quad(lambda t: math.pi*math.exp(-2*t)*math.sqrt(1-math.exp(-2*t)), 0, 50)[0], math.pi/3, 1e-9)
# Weyl law on the flat torus: N(lambda) ~ lambda/(4 pi)
lam = 4*math.pi**2*10000
N = sum(1 for k1 in range(-101, 102) for k2 in range(-101, 102) if 4*math.pi**2*(k1*k1+k2*k2) <= lam)
check("N(lambda)/(lambda/4pi) close to 1", N/(lam/(4*math.pi)), 1, 0.01)
# index of z^2 is 2 (winding of t -> e^{2it})
finish()
