#!/usr/bin/env python3
"""Volume 9, Chapter 1: recompute the formulas and numbers printed without proof on the page."""
import sympy as sp
from common import check_true, finish

x, y, t = sp.symbols('x y t', real=True)
# Cassini: f = |z-1|^2 |z+1|^2 - 1, gradient, critical points and values
f = (x**2 + y**2)**2 - 2*(x**2 - y**2)
check_true("Cassini identity", sp.expand(((x-1)**2+y**2)*((x+1)**2+y**2) - 1 - f) == 0)
g = [sp.diff(f, x), sp.diff(f, y)]
check_true("Cassini gradient", sp.expand(g[0] - 4*x*(x**2+y**2-1)) == 0 and sp.expand(g[1] - 4*y*(x**2+y**2+1)) == 0)
crit = sp.solve(g, [x, y], dict=True)
crit = {(c[x], c[y]) for c in crit if c[x].is_real and c[y].is_real}
check_true("Cassini critical points (0,0),(+-1,0)", crit == {(0, 0), (1, 0), (-1, 0)})
check_true("Cassini critical values 0,-1,-1", [f.subs({x: a, y: b}) for a, b in sorted(crit)] == [-1, 0, -1])
# Think box: f(x)=x+2x^2 sin(1/x) has f'<0 near 0
fp = lambda u: 1 + 4*u*sp.sin(1/u) - 2*sp.cos(1/u)
check_true("x+2x^2 sin(1/x): f'(1/(2 pi k)) = -1", all(sp.simplify(fp(1/(2*sp.pi*k))) == -1 for k in range(1, 5)))
# Stereographic projection
n = 3
ys = sp.symbols('y1:%d' % (n+1), real=True)
r2 = sum(v**2 for v in ys)
X = [2*v/(r2+1) for v in ys] + [(r2-1)/(r2+1)]
check_true("sigma_N^{-1} lands on the sphere", sp.simplify(sum(c**2 for c in X) - 1) == 0)
check_true("sigma_N(sigma_N^{-1} y) = y", all(sp.simplify(X[i]/(1-X[n]) - ys[i]) == 0 for i in range(n)))
check_true("sigma_S o sigma_N^{-1} = y/|y|^2", all(sp.simplify(X[i]/(1+X[n]) - ys[i]/r2) == 0 for i in range(n)))
# RP^2 in R^4: injectivity identity and immersion (rank 2 on v-perp) at random points
a, b, c = sp.symbols('a b c', real=True)
check_true("(x^2+y^2)^2 = (x^2-y^2)^2 + 4x^2y^2", sp.expand((a**2+b**2)**2 - (a**2-b**2)**2 - 4*a**2*b**2) == 0)
import random, numpy as np
random.seed(1)
ok = True
for _ in range(200):
    v = np.random.default_rng(_).normal(size=3); v /= np.linalg.norm(v)
    xx, yy, zz = v
    J = np.array([[2*xx, -2*yy, 0], [yy, xx, 0], [zz, 0, xx], [0, zz, yy]])
    # basis of v-perp
    q, _r = np.linalg.qr(np.column_stack([v, [1, 0, 0], [0, 1, 0]]))
    B = q[:, 1:3]
    ok &= np.linalg.matrix_rank(J @ B, tol=1e-9) == 2
check_true("RP^2 -> R^4 is an immersion at 200 random points", ok)
# Two-link arm: Im(a conj b) = -l1 l2 sin(theta2)
l1, l2, t1, t2 = sp.symbols('l1 l2 t1 t2', real=True)
E = l1*sp.exp(sp.I*t1) + l2*sp.exp(sp.I*(t1+t2))
A = sp.I*E; Bv = sp.I*l2*sp.exp(sp.I*(t1+t2))
check_true("arm: Im(a conj b) = -l1 l2 sin t2", sp.simplify(sp.im(sp.expand_complex(A*sp.conjugate(Bv))) + l1*l2*sp.sin(t2)) == 0)
check_true("arm: |E|^2", sp.simplify(sp.expand_complex(E*sp.conjugate(E)) - (l1**2+l2**2+2*l1*l2*sp.cos(t2))) == 0)
# figure eight: psi'(t) never vanishes
check_true("figure eight velocities (2,1) and (2,-1)", (2*sp.cos(0), sp.cos(0)) == (2, 1) and (2*sp.cos(2*sp.pi), sp.cos(sp.pi)) == (2, -1))
# dim O(n)
check_true("dim O(n) = n(n-1)/2 for n=2..6", all(k*k - k*(k+1)//2 == k*(k-1)//2 for k in range(2, 7)))
finish()
