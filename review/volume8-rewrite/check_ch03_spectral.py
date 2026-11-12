#!/usr/bin/env python3
"""Volume 8, Chapter 3: the opening questions, the figure's Rayleigh quotient, interlacing, Weyl, Schur, Horn's
algorithm, Hoffman-Wielandt, and the exercises with numbers in them."""
from math import cos, sin, pi, sqrt
import itertools
import numpy as np
from common import check, check_true, finish
rng = np.random.default_rng(8)
def herm(n):
    M = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)); return (M + M.conj().T) / 2
ev = lambda A: np.sort(np.linalg.eigvalsh(A))[::-1]
def majorised(d, lam, tol=1e-9):
    d, lam = np.sort(d)[::-1], np.sort(lam)[::-1]
    return all(d[:k].sum() <= lam[:k].sum() + tol for k in range(1, len(d))) and abs(d.sum() - lam.sum()) < tol
check_true("(3,0,0) is not majorised by (2,2,-1)", not majorised(np.array([3., 0, 0]), np.array([2., 2, -1])))
check_true("(1,1,1) is majorised by (3,0,0)", majorised(np.ones(3), np.array([3., 0, 0])))
check_true("all-ones 3x3 has eigenvalues 3,0,0", np.allclose(ev(np.ones((3, 3))), [3, 0, 0]))
# Figure: eigenvalues 3 and 1, top eigenvector at angle pi/6
u = np.array([cos(pi / 6), sin(pi / 6)]); v = np.array([-sin(pi / 6), cos(pi / 6)])
A = 3 * np.outer(u, u) + np.outer(v, v)
for th in (0.0, 0.4, 1.3, 2.9):
    x = np.array([cos(th), sin(th)])
    check(f"Rayleigh quotient at {th}", x @ A @ x, 3 * cos(th - pi / 6) ** 2 + sin(th - pi / 6) ** 2, 1e-12)
for trial in range(40):
    n = int(rng.integers(2, 8)); A, B = herm(n), herm(n); a, b, s = ev(A), ev(B), ev(A + B)
    m = int(rng.integers(1, n + 1)); c = ev(A[:m, :m])
    check_true("interlacing", all(a[k] + 1e-9 >= c[k] >= a[k + n - m] - 1e-9 for k in range(m)))
    check_true("Weyl", all(s[i + j] <= a[i] + b[j] + 1e-9 for i in range(n) for j in range(n) if i + j < n))
    check_true("stability", np.all(np.abs(s - a) <= max(abs(b[0]), abs(b[-1])) + 1e-9))
    check_true("Schur majorisation", majorised(np.diag(A).real, a))
    check_true("Hoffman-Wielandt (Hermitian)", np.sum((a - b) ** 2) <= np.linalg.norm(A - B) ** 2 + 1e-9)
    check_true("von Neumann trace", np.trace(A @ B).real <= a @ b + 1e-9)
    k = int(rng.integers(1, n + 1)); Q = np.linalg.qr(rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)))[0][:, :k]
    check_true("Ky Fan", np.trace(Q.conj().T @ A @ Q).real <= a[:k].sum() + 1e-9)
    w = rng.normal(size=n) + 1j * rng.normal(size=n); r = ev(A + np.outer(w, w.conj()))
    check_true("rank-one interlacing", all(r[k] >= a[k] - 1e-9 for k in range(n)) and all(r[k] <= a[k - 1] + 1e-9 for k in range(1, n)))
# Hoffman-Wielandt for normal matrices, best permutation by brute force
for trial in range(10):
    n = 4
    def normal():
        Q = np.linalg.qr(rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)))[0]
        return Q @ np.diag(rng.normal(size=n) + 1j * rng.normal(size=n)) @ Q.conj().T
    A, B = normal(), normal(); al, be = np.linalg.eigvals(A), np.linalg.eigvals(B)
    best = min(sum(abs(al[i] - be[p[i]]) ** 2 for i in range(n)) for p in itertools.permutations(range(n)))
    check_true("Hoffman-Wielandt (normal)", best <= np.linalg.norm(A - B) ** 2 + 1e-9)
# Horn's algorithm as in the proof
def horn(d, lam):
    d, lam = np.sort(d)[::-1], np.sort(lam)[::-1]; n = len(d)
    if n == 1: return np.array([[lam[0]]])
    k = next(k for k in range(n - 1) if lam[k] + 1e-12 >= d[0] >= lam[k + 1] - 1e-12)
    c2 = 1.0 if lam[k] == lam[k + 1] else (d[0] - lam[k + 1]) / (lam[k] - lam[k + 1])
    c, s = sqrt(c2), sqrt(1 - c2)
    lamp = np.concatenate([lam[:k], [lam[k] + lam[k + 1] - d[0]], lam[k + 2:]])
    r = np.zeros(n - 1); r[k] = c * s * (lam[k] - lam[k + 1])
    M = np.zeros((n, n)); M[0, 0] = d[0]
    sub = horn(d[1:], lamp)
    # find Q' with Q' diag(lamp) Q'^T = sub
    wl, Vl = np.linalg.eigh(sub); order = np.argsort(wl)[::-1]; Vl = Vl[:, order]
    idx = np.argsort(lamp)[::-1]; Qp = np.zeros((n - 1, n - 1)); Qp[:, idx] = Vl
    M[1:, 1:] = sub; M[1:, 0] = Qp @ r; M[0, 1:] = Qp @ r
    return M
for d, lam in (([2, 1, 0], [3, 0, 0]), ([1, 1, 1], [3, 0, 0]), ([1, 0.5, 0.5, 0], [1.5, 1, 0, -0.5])):
    M = horn(np.array(d, float), np.array(lam, float))
    check_true(f"Horn: diagonal {d}, eigenvalues {lam}", np.allclose(np.sort(np.diag(M)), np.sort(d)) and np.allclose(ev(M), np.sort(lam)[::-1]))
M = np.array([[2, sqrt(2), 0], [sqrt(2), 1, 0], [0, 0, 0]])
check_true("ex:hornsmall matrix has eigenvalues 3,0,0", np.allclose(ev(M), [3, 0, 0]))
check_true("(2,2,-1) is not majorised by (3,0,0)", not majorised(np.array([2., 2, -1]), np.array([3., 0, 0])))
# path graph eigenvalues
for n in (2, 5, 9):
    A = np.diag(np.ones(n - 1), 1) + np.diag(np.ones(n - 1), -1)
    check_true(f"path P_{n}", np.allclose(ev(A), [2 * cos(k * pi / (n + 1)) for k in range(1, n + 1)]))
# ex:nonnormal
e = 0.01; w = np.linalg.eigvals(np.array([[0, 1], [e, 0]]))
check_true("nonnormal: eigenvalues +-sqrt(eps)", np.allclose(sorted(w.real), [-sqrt(e), sqrt(e)]))
# ex:bordered
lam = np.array([5., 3, 1, -2]); mu = np.array([4., 2, 0])
f = lambda x: np.prod(x - lam); gp = lambda i: np.prod([mu[i] - mu[l] for l in range(3) if l != i])
r = np.array([-f(mu[i]) / gp(i) for i in range(3)]); c = lam.sum() - mu.sum()
check_true("bordered: r_i > 0", np.all(r > 0))
M = np.zeros((4, 4)); M[:3, :3] = np.diag(mu); M[:3, 3] = np.sqrt(r); M[3, :3] = np.sqrt(r); M[3, 3] = c
check_true("bordered matrix has the prescribed spectrum", np.allclose(ev(M), lam))
finish()
