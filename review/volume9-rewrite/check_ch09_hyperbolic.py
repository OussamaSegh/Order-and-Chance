#!/usr/bin/env python3
"""Volume 9, Chapter 9: check the numbers printed in the chapter (hyperbolic plane, modular group, cutting sequences)."""
import math
import numpy as np, sympy as sp
from mpmath import mp, mpf, sqrt as msqrt, floor as mfloor
from common import check, check_true, finish

def mob(g, z): a, b, c, d = g.ravel(); return (a*z+b)/(c*z+d)
def dist(z, w): return math.acosh(1+abs(z-w)**2/(2*z.imag*w.imag))

# circle of radius 10: length 2 pi sinh 10 about 69000, about 6900 times the radius
L = 2*math.pi*math.sinh(10)
check("2 pi sinh 10 (printed about 69000)", L, 69000, 500)
check("ratio to the radius (nearly seven thousand)", L/10, 6900, 100)

# polar coordinates: P(r, theta) at distance r from i; circle length and disc area
Cinv = lambda w: 1j*(1+w)/(1-w)
for r in (0.3, 1.7, 3.0):
    check(f"d(i, P({r}, 1)) = r", dist(1j, Cinv(math.tanh(r/2)*np.exp(1j))), r, 1e-9)
r = 1.3; th = np.linspace(0, 2*np.pi, 20001); pts = np.array([Cinv(math.tanh(r/2)*np.exp(1j*t)) for t in th])
length = sum(abs(pts[k+1]-pts[k])/((pts[k+1]+pts[k]).imag/2) for k in range(len(pts)-1))
check("hyperbolic circle length 2 pi sinh r", length, 2*math.pi*math.sinh(r), 1e-4)

# hyperbolic circles: Euclidean centre i b cosh r, radius b sinh r
b, r = 2.0, 0.8
for t in np.linspace(0, 6, 7):
    z = 1j*b*math.cosh(r)+b*math.sinh(r)*np.exp(1j*t)
    if z.imag > 0: check_true(f"point of circle at distance r (t={t:.0f})", abs(dist(z, 1j*b)-r) < 1e-9)

# Iwasawa of [[2,1],[1,1]] = n_{3/2} a_{-log 2} k_{pi/4}
n = lambda x: np.array([[1, x], [0, 1]]); a = lambda t: np.diag([math.exp(t/2), math.exp(-t/2)])
k = lambda q: np.array([[math.cos(q), -math.sin(q)], [math.sin(q), math.cos(q)]])
g = np.array([[2., 1], [1, 1]])
check_true("[[2,1],[1,1]] = n_{3/2} a_{-log 2} k_{pi/4}", np.allclose(n(1.5) @ a(-math.log(2)) @ k(math.pi/4), g))
check_true("g(i) = 3/2 + i/2", abs(mob(g, 1j)-(1.5+0.5j)) < 1e-12)
q = 0.7; h = 1e-7
check_true("derivative of k_theta at i is e^{-2 i theta}", abs((mob(k(q), 1j+h)-mob(k(q), 1j))/h-np.exp(-2j*q)) < 1e-5)

# trace formula and minimal displacement on the axis
lam = 1.9; G = np.diag([lam, 1/lam]); ell = 2*math.log(lam)
check("translation length 2 log lambda on the axis", dist(1j, mob(G, 1j)), ell, 1e-12)
rng = np.random.default_rng(0)
zs = rng.normal(size=50)+1j*np.abs(rng.normal(size=50))+0.01j
check_true("d(z, g z) >= ell everywhere", all(dist(z, mob(G, z)) >= ell-1e-12 for z in zs))
check("2 cosh(ell/2) = |tr g|", 2*math.cosh(ell/2), lam+1/lam, 1e-12)

# area of F = pi/3 by integrating dx dy / y^2
from scipy import integrate
area = integrate.quad(lambda x: 1/math.sqrt(1-x*x), -0.5, 0.5)[0]   # int_{sqrt(1-x^2)}^inf dy/y^2
check("area of F = pi/3", area, math.pi/3, 1e-10)
check("area of F above height 2 = 1/2", integrate.dblquad(lambda y, x: 1/y**2, -0.5, 0.5, 2, np.inf)[0], 0.5, 1e-8)

# exercise shortest: 2 arccosh(3/2) = 4 log phi = 1.9248
phi = (1+math.sqrt(5))/2
check("2 arccosh(3/2) = 4 log phi", 2*math.acosh(1.5), 4*math.log(phi), 1e-12)
check("4 log phi printed 1.925 / 1.9248", 4*math.log(phi), 1.9248, 5e-5)
# exercise sqrt2axis: g = [[5,2],[2,1]], fixed points 1 +- sqrt 2, ell = 4 log(1+sqrt2) = 3.525
g = np.array([[5., 2], [2, 1]])
check_true("[[5,2],[2,1]] fixes 1 +- sqrt 2", all(abs(mob(g, x)-x) < 1e-12 for x in (1+math.sqrt(2), 1-math.sqrt(2))))
check("ell = 2 arccosh(3) = 4 log(1+sqrt 2), printed 3.525", 2*math.acosh(3), 3.525, 5e-4)
check("4 log(1+sqrt2) = 2 arccosh 3", 4*math.log(1+math.sqrt(2)), 2*math.acosh(3), 1e-12)
M = np.array([[2, 1], [1, 0]])
check_true("[[5,2],[2,1]] = M^2, M = [[2,1],[1,0]]", (M @ M == g).all())

# class numbers: reduced forms of discriminant -20 and -23
def reduced(D):
    out = []
    for A in range(1, int(math.isqrt(-D//3))+2):
        for B in range(-A, A+1):
            if (B*B-D) % (4*A) == 0:
                C = (B*B-D)//(4*A)
                if C >= A and not (B < 0 and (abs(B) == A or A == C)): out.append((A, B, C))
    return out
check_true("reduced forms of -20: (1,0,5), (2,2,3)", reduced(-20) == [(1, 0, 5), (2, 2, 3)])
check_true("reduced forms of -23: (1,1,6), (2,-1,3), (2,1,3)", sorted(reduced(-23)) == [(1, 1, 6), (2, -1, 3), (2, 1, 3)])

# Klein quartic: pi/42 triangles, 336 of them
check("pi - pi/2 - pi/3 - pi/7 = pi/42", math.pi-math.pi/2-math.pi/3-math.pi/7, math.pi/42, 1e-14)
check("8 pi / (pi/42) = 336 = 2*84*(3-1)", 8*42, 336, 0)

# horocycle: d(i+s, i) = 2 arsinh(|s|/2)
for s in (0.5, 3.0, 40.0):
    check(f"d(i+{s}, i) = 2 arsinh(s/2)", dist(1j+s, 1j), 2*math.asinh(s/2), 1e-9)

# Theorem cutting: cutting sequence of the h-line from y to x, computed by walking the Farey triangles
mp.dps = 60
def cutting(x, y, nletters):
    """Walk Farey triangles: current edge (p/q, r/s) crossed by the geodesic; return letters."""
    from fractions import Fraction as Fr
    # start: crossing edge (0, infinity); enter triangle on the side of x (right, since x > 0)
    P, Q = (0, 1), (1, 0)           # endpoints as (num, den); Q is infinity
    word = []
    for _ in range(nletters):
        # third vertex of the triangle beyond edge (P,Q) on the side of x: the mediant P+Q or difference
        cand = [(P[0]+Q[0], P[1]+Q[1]), (P[0]-Q[0], P[1]-Q[1])]
        val = lambda v: mpf(v[0])/v[1] if v[1] != 0 else mp.inf
        def between(t, u, v):  # is t on the arc from u to v not containing x... use sign test via cross-ratio-free check
            lo, hi = sorted([val(u), val(v)]); return lo < t < hi
        # choose the third vertex on the same side of edge (P,Q) as x
        xside = between(x, P, Q)
        W = None
        for c in cand:
            if c[1] < 0: c = (-c[0], -c[1])
            if c[1] == 0: continue
            if between(val(c), P, Q) == xside: W = c
        # the geodesic leaves through (P,W) or (W,Q): the side whose endpoints separate y and x
        def separates(u, v):
            return between(x, u, v) != between(y, u, v)
        if separates(P, W): shared, new = P, (P, W)
        else: shared, new = Q, (W, Q)
        # left or right: shared vertex in the right arc (y, x) (for y < x) means R
        t = val(shared)
        word.append('R' if (y < t < x) else 'L')
        P, Q = new
    return ''.join(word)
for x, cf in ((1+msqrt(2), [2]*6), (phi and (1+msqrt(5))/2, [1]*8), (mp.pi, None), (msqrt(7), None)):
    y = mpf(-0.37)
    if cf is None:
        cf, t = [], x
        for _ in range(5):
            a0 = int(mfloor(t)); cf.append(a0); t = 1/(t-a0)
    expect = ''.join(('L' if i % 2 == 0 else 'R')*c for i, c in enumerate(cf))
    got = cutting(x, y, len(expect))
    check_true(f"cutting sequence of the line from -0.37 to {mp.nstr(x, 8)}: {expect[:24]}", got == expect)
finish()
