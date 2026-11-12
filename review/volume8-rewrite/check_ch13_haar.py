#!/usr/bin/env python3
"""Volume 8, Chapter 13 (and the exercise moved to Volume 13, Chapter 8): det of left multiplication on n x n matrices,
the Hausdorff rotations (exact integer recursion, 3 does not divide b, no reduced word up to length 10 fixes (1,0,0)),
the measure of the p-adic squares, the local zeta integral, the Gamma integral at infinity."""
from fractions import Fraction as Fr
from itertools import product
from math import pi, gamma, exp, sqrt
import numpy as np, sympy as sp
from scipy.integrate import quad
from common import check, check_true, finish
for n in (2, 3):
    A = sp.Matrix(n, n, lambda i, j: sp.Symbol(f"a{i}{j}"))
    X = sp.Matrix(n, n, lambda i, j: sp.Symbol(f"x{i}{j}")); v = list(X.T.reshape(n*n, 1))
    L = (A*X).T.reshape(n*n, 1).jacobian(v)
    check_true(f"det of X -> AX on {n}x{n} matrices is det(A)^{n}", sp.expand(L.det() - A.det()**n) == 0)
r2 = sp.sqrt(2)
phi = {1: sp.Matrix([[1, -2*r2, 0], [2*r2, 1, 0], [0, 0, 3]])/3, -1: sp.Matrix([[1, 2*r2, 0], [-2*r2, 1, 0], [0, 0, 3]])/3}
rho = {1: sp.Matrix([[3, 0, 0], [0, 1, -2*r2], [0, 2*r2, 1]])/3, -1: sp.Matrix([[3, 0, 0], [0, 1, 2*r2], [0, -2*r2, 1]])/3}
check_true("phi is the rotation by arccos(1/3) about z, phi^-1 its inverse", phi[1]*phi[-1] == sp.eye(3) and phi[1][0, 0] == sp.Rational(1, 3) and sp.simplify(phi[1].det()) == 1)
check_true("rho is the rotation by arccos(1/3) about x, rho^-1 its inverse", rho[1]*rho[-1] == sp.eye(3) and sp.simplify(rho[1].det()) == 1)
# integer recursion of the text
step = {("p", 1): lambda a, b, c: (a - 4*b, b + 2*a, 3*c), ("p", -1): lambda a, b, c: (a + 4*b, b - 2*a, 3*c),
        ("r", 1): lambda a, b, c: (3*a, b - 2*c, c + 4*b), ("r", -1): lambda a, b, c: (3*a, b + 2*c, c - 4*b)}
M = {("p", 1): phi[1], ("p", -1): phi[-1], ("r", 1): rho[1], ("r", -1): rho[-1]}
letters = list(step); ok_rec = ok_b = ok_fix = True; count = 0
def words(k):
    if k == 0: yield (); return
    for w in words(k - 1):
        for s in letters:
            if w and w[0][0] == s[0] and w[0][1] == -s[1]: continue
            yield (s,) + w          # leftmost letter applied last
for k in range(1, 11):
    for w in words(k):
        if w[-1][0] != "p": continue
        t = (1, 0, 0)
        for s in reversed(w): t = step[s](*t)
        ok_b &= t[1] % 3 != 0; ok_fix &= t != (3**k, 0, 0); count += 1
        if k <= 4:
            vec = sp.Matrix([1, 0, 0])
            for s in reversed(w): vec = M[s]*vec
            ok_rec &= sp.simplify(vec - sp.Matrix([t[0], t[1]*r2, t[2]])/3**k) == sp.zeros(3, 1)
check_true("the integer recursion matches the matrices (words up to length 4)", ok_rec)
check_true(f"3 does not divide b for all {count} reduced words up to length 10 ending in phi^(+-1)", ok_b and ok_fix)
# p-adic squares: sample residues mod p^K
def sq_measure(p, K):
    tot = Fr(0)
    for x in range(1, p**K):
        v = 0; y = x
        while y % p == 0: y //= p; v += 1
        if v % 2: continue
        if p == 2:
            if v <= K - 3 and y % 8 == 1: tot += Fr(1, p**K)
        elif v < K and pow(y % p, (p - 1)//2, p) == 1: tot += Fr(1, p**K)
    return tot
for p, K in ((3, 7), (5, 5), (7, 4)):
    check(f"measure of squares in Z_{p} (residues mod {p}^{K})", float(sq_measure(p, K)), p/(2*(p + 1)), 2*p**(-K + 1))
check("measure of squares in Z_2 (residues mod 2^14)", float(sq_measure(2, 14)), 1/6, 1e-3)
# local zeta: sum_v p^{-v(s-1)} p^{-v}(1-1/p)
for p, s in ((2, 2.0), (3, 1.5), (5, 3.0)):
    check(f"local zeta integral at p = {p}, s = {s}", sum(p**(-v*(s - 1))*p**(-v)*(1 - 1/p) for v in range(200)), (1 - 1/p)/(1 - p**-s), 1e-12)
for s in (1.5, 2.0, 3.7):
    check(f"int e^(-pi x^2)|x|^(s-1) dx = pi^(-s/2) Gamma(s/2) at s = {s}", 2*quad(lambda x: exp(-pi*x*x)*x**(s - 1), 0, np.inf)[0], pi**(-s/2)*gamma(s/2), 1e-8)
finish()
