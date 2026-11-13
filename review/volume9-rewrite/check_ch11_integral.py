#!/usr/bin/env python3
"""Volume 9, Chapter 11 (file ch10-integral.tex): check the numbers of integral geometry."""
import math
import numpy as np
from scipy import integrate
from common import check, check_true, finish

rng = np.random.default_rng(3)
N = 2_000_000
# Bertrand: under the invariant measure P(chord > sqrt 3) = 1/2; other laws 1/3 and 1/4
p = rng.uniform(0, 1, N)
check("invariant measure: P(chord > sqrt 3)", (2*np.sqrt(1-p**2) > math.sqrt(3)).mean(), 0.5, 0.002)
phi = rng.uniform(0, 2*np.pi, N); pe = abs(np.cos(phi/2))
check("random endpoints: P = 1/3", (pe < 0.5).mean(), 1/3, 0.002)
r = np.sqrt(rng.uniform(0, 1, N))
check("random midpoint: P = 1/4", (r < 0.5).mean(), 0.25, 0.002)
check("random endpoints: density 2/(pi sqrt(1-p^2)) integrates to P(|p|<1/2) = 1/3", integrate.quad(lambda x: 2/(math.pi*math.sqrt(1-x*x)), 0, 0.5)[0], 1/3, 1e-12)
check("mean chord under the invariant measure = pi/2", integrate.quad(lambda x: 2*math.sqrt(1-x*x), 0, 1)[0], math.pi/2, 1e-12)
check("1 - cos x <= x^2/2 at x = delta/2 gives delta^2/8", 1-math.cos(0.05), 0.1**2/8, 2e-6)
check("int_0^pi |cos(theta - phi)| = 2", integrate.quad(lambda t: abs(math.cos(t-0.7)), 0, math.pi, points=[0.7+math.pi/2])[0], 2, 1e-10)

# Crofton for an ellipse: measure of lines meeting it (counted twice) = 2L
a, b = 2.0, 0.7
L = integrate.quad(lambda t: math.hypot(a*math.sin(t), b*math.cos(t)), 0, 2*math.pi)[0]
width = lambda th: 2*math.sqrt((a*math.cos(th))**2+(b*math.sin(th))**2)
check("Cauchy: perimeter of an ellipse = int_0^pi width", integrate.quad(width, 0, math.pi)[0], L, 1e-9)
# Monte Carlo Crofton on a wiggly closed curve inside the disc of radius 3
t = np.linspace(0, 2*np.pi, 4001)
cx = (1.5+0.6*np.cos(5*t))*np.cos(t); cy = (1.5+0.6*np.cos(5*t))*np.sin(t)
Lc = np.hypot(np.diff(cx), np.diff(cy)).sum()
M = 20000; th = rng.uniform(0, np.pi, M); pp = rng.uniform(-3, 3, M)
vals = np.cos(th)[:, None]*cx[None, :]+np.sin(th)[:, None]*cy[None, :]-pp[:, None]
cross = (np.sign(vals[:, 1:]) != np.sign(vals[:, :-1])).sum(1)
check("Crofton by Monte Carlo: mean crossings * measure / 2 = L", cross.mean()*(6*np.pi)/2, Lc, 0.02*Lc)

# Buffon noodle: mean crossings 2L/(pi d)
d, Ln = 1.0, 2.7
ang = rng.uniform(0, np.pi, N); y0 = rng.uniform(0, d, N)
y1 = y0+Ln*np.sin(ang)
check("needle of length 2.7 on lines at distance 1: mean crossings", (np.floor(y1/d)-np.floor(y0/d)).mean(), 2*Ln/(math.pi*d), 0.005)

# Exercise chord: mean chord of the unit square = pi/4; two lines: square 2 pi/16
check("mean chord of the unit square printed 0.785", math.pi/4, 0.785, 5e-4)
check("two lines in a square: 2 pi / 16, printed 0.39", 2*math.pi/16, 0.39, 0.005)
# Monte Carlo: two random lines meeting the unit square cross inside it
def lines_meeting_square(n):
    out = []
    while sum(len(o) for o in out) < n:
        th = rng.uniform(0, np.pi, n); p = rng.uniform(-1.5, 1.5, n)
        c = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
        proj = np.cos(th)[:, None]*c[None, :, 0]+np.sin(th)[:, None]*c[None, :, 1]
        ok = (proj.min(1) < p) & (p < proj.max(1)); out.append(np.c_[th[ok], p[ok]])
    return np.vstack(out)[:n]
n = 400000; A = lines_meeting_square(n); B = lines_meeting_square(n)
M2 = np.stack([np.c_[np.cos(A[:, 0]), np.sin(A[:, 0])], np.c_[np.cos(B[:, 0]), np.sin(B[:, 0])]], 1)
X = np.linalg.solve(M2, np.c_[A[:, 1], B[:, 1]][:, :, None])[:, :, 0]
inside = ((X >= 0) & (X <= 1)).all(1)
check("two random lines cross inside the unit square", inside.mean(), 2*math.pi/16, 0.003)

# Laplace's grid: (4ld - l^2)/(pi d^2); 3/pi for l = d
l = 0.8
ang = rng.uniform(0, 2*np.pi, N); x0 = rng.uniform(0, 1, N); y0 = rng.uniform(0, 1, N)
x1 = x0+l*np.cos(ang); y1 = y0+l*np.sin(ang)
hit = (np.floor(x1) != np.floor(x0)) | (np.floor(y1) != np.floor(y0))
check("Laplace's grid, l = 0.8 d", hit.mean(), (4*l-l*l)/math.pi, 0.002)
check("3/pi printed 0.95", 3/math.pi, 0.95, 0.006)

# Cauchy surface formula: mean shadow of the unit cube = 3/2; diagonal shadow sqrt 3
u = rng.normal(size=(N, 3)); u /= np.linalg.norm(u, axis=1)[:, None]
check("mean of |u1|+|u2|+|u3|", abs(u).sum(1).mean(), 1.5, 0.002)
check_true("hat box: <u, n> uniform on [-1,1]", abs((u[:, 2] < 0.3).mean()-0.65) < 0.002)
from scipy.spatial import ConvexHull
cube = np.array([[i, j, k] for i in (0, 1) for j in (0, 1) for k in (0, 1)], float)
dvec = np.ones(3)/math.sqrt(3); e1 = np.array([1, -1, 0])/math.sqrt(2); e2 = np.cross(dvec, e1)
proj = np.c_[cube @ e1, cube @ e2]
hull = ConvexHull(proj)
check("diagonal shadow of the cube has area sqrt 3", hull.volume, math.sqrt(3), 1e-12)
check_true("and it is a hexagon", len(hull.vertices) == 6)

# Poincare: two unit segments moving: int n dg = 4ab
a_, b_ = 1.0, 0.6
al = rng.uniform(0, 2*np.pi, N); v = rng.uniform(-2, 2, (N, 2))
P0, P1 = np.zeros((N, 2)), np.tile([a_, 0], (N, 1))
Q0 = v; Q1 = v+b_*np.c_[np.cos(al), np.sin(al)]
def orient(A, B, C): return np.sign((B[:, 0]-A[:, 0])*(C[:, 1]-A[:, 1])-(B[:, 1]-A[:, 1])*(C[:, 0]-A[:, 0]))
meet = (orient(P0, P1, Q0) != orient(P0, P1, Q1)) & (orient(Q0, Q1, P0) != orient(Q0, Q1, P1))
check("Poincare: measure of motions making two segments meet = 4ab", meet.mean()*16*2*math.pi, 4*a_*b_, 0.03)

# Exercise spherecrofton: great circle, L = 2 pi, int n dsigma = 2
check("L/pi for a great circle", 2*math.pi/math.pi, 2, 0)
# a small circle of colatitude 0.5: length 2 pi sin 0.5; random great circles cross it 2 times or 0
c = 0.5; uu = u[:200000]
# great circle u-perp meets the circle of colatitude c iff |<u, north>| < sin c
check("Crofton on the sphere, small circle", 2*(abs(uu[:, 2]) < math.sin(c)).mean(), 2*math.pi*math.sin(c)/math.pi, 0.01)
finish()
