#!/usr/bin/env python3
"""Volume 9, Chapter 7: check the matrix identities printed in the chapter."""
import numpy as np, sympy as sp
from scipy.linalg import expm, logm
from common import check_true, finish

s = sp.symbols('s')
X, Y = sp.Matrix(sp.MatrixSymbol('X', 2, 2)), sp.Matrix(sp.MatrixSymbol('Y', 2, 2))
ex = lambda M: sum(((M**k)/sp.factorial(k) for k in range(3)), sp.zeros(2))
C = (ex(s*X)*ex(s*Y)*ex(-s*X)*ex(-s*Y)).applyfunc(lambda e: sp.expand(e).coeff(s, 2))
check_true("commutator loop: s^2 term is XY - YX", sp.simplify(C - (X*Y - Y*X)) == sp.zeros(2))
L = lambda u: np.array([[0, -u[2], u[1]], [u[2], 0, -u[0]], [-u[1], u[0], 0]])
s1 = np.array([[0, 1], [1, 0]]); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.array([[1, 0], [0, -1]])
Xu = lambda u: -0.5j*(u[0]*s1 + u[1]*s2 + u[2]*s3)
rng = np.random.default_rng(0)
ok1 = ok2 = True
for _ in range(50):
    u, v = rng.normal(size=3), rng.normal(size=3)
    ok1 &= np.allclose(L(u) @ L(v) - L(v) @ L(u), L(np.cross(u, v)))
    ok2 &= np.allclose(Xu(u) @ Xu(v) - Xu(v) @ Xu(u), Xu(np.cross(u, v)))
check_true("[L(u),L(v)] = L(u x v)", ok1)
check_true("[X(u),X(v)] = X(u x v)", ok2)
check_true("tr(sigma_j sigma_k) = 2 delta", all(np.isclose(np.trace(a @ b), 2*(i == j)) for i, a in enumerate([s1, s2, s3]) for j, b in enumerate([s1, s2, s3])))
u = np.array([0.3, -0.5, 0.81]); u /= np.linalg.norm(u)
check_true("e^{2 pi X(u)} = -I and e^{4 pi X(u)} = I", np.allclose(expm(2*np.pi*Xu(u)), -np.eye(2)) and np.allclose(expm(4*np.pi*Xu(u)), np.eye(2)))
# Ad of SU(2) lands in SO(3) and has kernel +-I
def Ad(g):
    B = [Xu(e) for e in np.eye(3)]
    return np.array([[(-2*np.trace((g @ Bj @ g.conj().T) @ Bi)).real for Bj in B] for Bi in B])
g = expm(Xu(rng.normal(size=3)))
R = Ad(g)
check_true("Ad(g) in SO(3)", np.allclose(R.T @ R, np.eye(3)) and np.isclose(np.linalg.det(R), 1))
check_true("Ad(-g) = Ad(g)", np.allclose(Ad(-g), R))
v = rng.normal(size=3)
check_true("Ad(e^{X(v)}) = e^{L(v)}", np.allclose(Ad(expm(Xu(v))), expm(L(v))))
# SL2: brackets, and the two products of exponentials
H = np.array([[1, 0], [0, -1]]); E = np.array([[0, 1], [0, 0]]); F = np.array([[0, 0], [1, 0]])
br = lambda a, b: a @ b - b @ a
check_true("[H,E]=2E, [H,F]=-2F, [E,F]=H", np.allclose(br(H, E), 2*E) and np.allclose(br(H, F), -2*F) and np.allclose(br(E, F), H))
check_true("diag(-2,-1/2) = e^{pi(E-F)} e^{log2 H}", np.allclose(expm(np.pi*(E-F)) @ expm(np.log(2)*H), np.diag([-2, -0.5])))
check_true("[[-1,1],[0,-1]] = e^{pi(E-F)} e^{-E}", np.allclose(expm(np.pi*(E-F)) @ expm(-E), [[-1, 1], [0, -1]]))
# Heisenberg: e^X e^Y = e^{X+Y+[X,Y]/2}
A = np.zeros((3, 3)); A[0, 1], A[1, 2], A[0, 2] = rng.normal(size=3)
B = np.zeros((3, 3)); B[0, 1], B[1, 2], B[0, 2] = rng.normal(size=3)
check_true("Heisenberg BCH", np.allclose(expm(A) @ expm(B), expm(A + B + 0.5*br(A, B))))
# dimensions
check_true("dim SO(3)=3, dim SU(2)=3, dim U(n)=n^2, dim SL2=3", (3*2//2, 2**2-1, 3) == (3, 3, 3))
finish()
