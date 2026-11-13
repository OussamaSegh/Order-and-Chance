#!/usr/bin/env python3
"""Volume 9, Appendices A-K: check the printed numbers and finite counts."""
import itertools, math
import numpy as np
from fractions import Fraction as Fr
from common import check, check_true, finish

# B (inversion): Descartes' circle theorem on (-1, 2, 2, 3) and its second root
k = [-1, 2, 2, 3]
check("Descartes: 2 sum k^2 = (sum k)^2", 2*sum(x*x for x in k), sum(k)**2, 0)
check("other root k4' = 2(k1+k2+k3) - k4", 2*(-1+2+2)-3, 3, 0)

# C (projective): P^2(F_q) has q^2+q+1 points, each line q+1 points; brute force for q = 2, 3, 5
for q in (2, 3, 5):
    pts = set()
    for v in itertools.product(range(q), repeat=3):
        if any(v):
            i = next(j for j in range(3) if v[j]); inv = pow(v[i], -1, q)
            pts.add(tuple(x*inv % q for x in v))
    check(f"#P^2(F_{q})", len(pts), q*q+q+1, 0)
    line = [p for p in pts if (p[0]+2*p[1]+p[2]) % q == 0]
    check(f"points on a line of P^2(F_{q})", len(line), q+1, 0)

# D (conics): Poncelet with R = 1, r = 0.36, d^2 = R^2 - 2Rr: the zigzag closes after 3 steps
R, r = 1.0, 0.36; d = math.sqrt(R*R-2*R*r)
def poncelet(t0, steps=3):
    P = np.array([math.cos(t0), math.sin(t0)]); c = np.array([d, 0.0]); start = P.copy(); prev = None
    for _ in range(steps):
        # tangent lines from P to the circle (c, r): direction angles
        v = c-P; L = np.linalg.norm(v); a = math.atan2(v[1], v[0]); s = math.asin(r/L)
        dirs = [a+s, a-s]
        cand = []
        for th in dirs:
            u = np.array([math.cos(th), math.sin(th)]); tpar = -2*P.dot(u)   # second intersection with unit circle
            Q = P+tpar*u; cand.append(Q)
        Q = cand[0] if prev is None or np.linalg.norm(cand[0]-prev) > 1e-9 else cand[1]
        prev, P = P, Q
    return np.linalg.norm(P-start)
check_true("Poncelet triangles close for three starting points", all(poncelet(t) < 1e-9 for t in (0.3, 1.9, 4.0)))

# E (quadrics): points of nondegenerate quadric surfaces over F_q: (q+1)^2 hyperbolic, q^2+1 elliptic
def count(form, q):
    n = 0
    for v in itertools.product(range(q), repeat=4):
        if any(v) and form(v) % q == 0: n += 1
    return n//(q-1)
for q in (3, 5, 7):
    nonsq = next(a for a in range(2, q) if pow(a, (q-1)//2, q) == q-1)
    check(f"hyperbolic quadric xy - zw over F_{q}", count(lambda v: v[0]*v[1]-v[2]*v[3], q), (q+1)**2, 0)
    check(f"elliptic quadric x^2 - n y^2 + zw over F_{q}", count(lambda v: v[0]**2-nonsq*v[1]**2+v[2]*v[3], q), q*q+1, 0)

# F (curves): circle x^2+y^2 = 3.24 and y = x^3 - 3x meet in 6 real points
roots = np.roots(np.poly1d([1, 0, -3, 0])**2+np.poly1d([1, 0, 0])-3.24)
check("real intersections of the circle and the cubic", sum(abs(z.imag) < 1e-9 for z in roots), 6, 0)

# G (cubics): Bachet, the tangent at (3,5) on y^2 = x^3 - 2
lam = Fr(27, 10); x3 = lam**2-6; y3 = -(5+lam*(x3-3))
check_true("2P = (129/100, -383/1000) and it is on the curve", x3 == Fr(129, 100) and y3 == Fr(-383, 1000) and y3**2 == x3**3-2)
lam = (y3-5)/(x3-3); x4 = lam**2-3-x3; y4 = -(5+lam*(x4-3))
check_true("3P = (164323/29241, -66234835/5000211), on the curve", x4 == Fr(164323, 29241) and y4 == Fr(-66234835, 5000211) and y4**2 == x4**3-2)
p = 101
aff = sum(1 for x in range(p) for y in range(p) if (y*y-(x**3-x+1)) % p == 0)
check("affine points of y^2 = x^3 - x + 1 over F_101", aff, 99, 0)
check_true("Hasse: |100 - 102| <= 2 sqrt 101", abs(aff+1-p-1) <= 2*math.sqrt(p))
check("# points of y^2=x^3+1 over F_11 (p = 2 mod 3): p+1", 1+sum(1 for x in range(11) for y in range(11) if (y*y-x**3-1) % 11 == 0), 12, 0)
# multiples of (0,1) on y^2 = x^3 + x + 1 over F_5, and of (2,3) on y^2 = x^3 + 1 over Q
def addp(P, Q, a, mod=None):
    inv = (lambda t: pow(t, -1, mod)) if mod else (lambda t: 1/Fr(t))
    red = (lambda t: t % mod) if mod else (lambda t: t)
    if P is None: return Q
    if Q is None: return P
    (x1, y1), (x2, y2) = P, Q
    if red(x1-x2) == 0 and red(y1+y2) == 0: return None
    l = red((3*x1*x1+a)*inv(2*y1)) if P == Q else red((y2-y1)*inv(x2-x1))
    x3 = red(l*l-x1-x2); return (x3, red(-(y1+l*(x3-x1))))
M = []; Q = None
for n in range(9): Q = addp(Q, (0, 1), 1, 5); M.append(Q)
check_true("F_5: multiples of (0,1) are (4,2),(2,1),(3,4),(3,1),(2,4),(4,3),(0,4), then O",
           M == [(0, 1), (4, 2), (2, 1), (3, 4), (3, 1), (2, 4), (4, 3), (0, 4), None])
M = []; Q = None
for n in range(6): Q = addp(Q, (Fr(2), Fr(3)), 0); M.append(Q)
check_true("Q: multiples of (2,3) on y^2 = x^3+1: (0,1),(-1,0),(0,-1),(2,-3),O",
           M == [(2, 3), (0, 1), (-1, 0), (0, -1), (2, -3), None])

# H (lattices)
check("hexagonal density pi/sqrt 12", math.pi/math.sqrt(12), 0.9069, 5e-5)
check("D3 density pi/sqrt 18", (4*math.pi/3)/2**2.5, 0.7405, 5e-5)
check("D3 density equals pi/sqrt 18", (4*math.pi/3)/2**2.5, math.pi/math.sqrt(18), 1e-12)
check("D4 density pi^2/16", (math.pi**2/2)/2**3, 0.617, 5e-4)
for n in (3, 4, 5, 8):
    vecs = [v for v in itertools.product(range(-1, 2), repeat=n) if sum(x*x for x in v) == 2 and sum(v) % 2 == 0]
    check(f"shortest vectors of D_{n}: 2n(n-1)", len(vecs), 2*n*(n-1), 0)
half = [v for v in itertools.product((-0.5, 0.5), repeat=8) if sum(1 for x in v if x < 0) % 2 == 0]
check("E8 roots: 112 + 128 = 240", 2*8*7+len(half), 240, 0)
check("377/233 printed 1.618", 377/233, 1.618, 5e-4)
check("(4 pi/3) and pi^4/24 unit ball volumes: V8", math.pi**4/24, math.pi**4/math.gamma(5), 1e-12)
check("Minkowski bound 4/pi printed 1.273", 4/math.pi, 1.273, 5e-4)
check("Hermite 2/sqrt3 printed 1.155", 2/math.sqrt(3), 1.155, 5e-4)
check("sum of two squares: 13 = 2^2 + 3^2", 2**2+3**2, 13, 0)

# I (non-Euclidean): d(1+i, 3+i) = arcosh 3 = log(3+2 sqrt2) about 1.763
check("arcosh 3", math.acosh(3), 1.763, 5e-4)
check("arcosh 3 = log(3 + 2 sqrt 2)", math.acosh(3), math.log(3+2*math.sqrt(2)), 1e-12)
check("distance formula 1 + |z-w|^2/(2 Im z Im w) = 3", 1+4/2, 3, 0)

# J (convex): Reuleaux area, Minkowski sum figure numbers
check("Reuleaux area (pi - sqrt3)/2 printed 0.705", (math.pi-math.sqrt(3))/2, 0.705, 5e-4)
check("disk of diameter 1: pi/4 printed 0.785", math.pi/4, 0.785, 5e-4)
check("sqrt 4.27 printed 2.07", math.sqrt(4.27), 2.07, 5e-3)
check("sqrt 1.4 + sqrt 0.49 printed 1.88", math.sqrt(1.4)+math.sqrt(0.49), 1.88, 5e-3)

# K (curvature): osculating radii of x = 1.6 cos t, y = sin t
a, b = 1.6, 1.0
check("radius at the ends of the long axis b^2/a", b*b/a, 0.625, 1e-12)
check("radius at the ends of the short axis a^2/b", a*a/b, 2.56, 1e-12)
# Descartes: angular defects of a cube add to 4 pi; Euler V - E + F = 2 for the five Platonic solids
check("cube: 8 vertices, defect pi/2 each", 8*(2*math.pi-3*math.pi/2), 4*math.pi, 1e-12)
check_true("Euler V-E+F=2 for the Platonic solids", all(V-E+F == 2 for V, E, F in [(4, 6, 4), (8, 12, 6), (6, 12, 8), (20, 30, 12), (12, 30, 20)]))
finish()
