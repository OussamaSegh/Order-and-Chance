#!/usr/bin/env python3
"""Volume 8, Chapter 4: the ellipse example, the figure's error fractions (recomputed from the original panel of the
figure), the photograph budget, Eckart-Young, the exercises with numbers."""
import re, pathlib
from math import sqrt
import numpy as np
from common import check, check_true, finish
root = pathlib.Path(__file__).resolve().parents[2]
A = np.array([[3., 0], [4, 5]]); s = np.linalg.svd(A, compute_uv=False)
check("sigma_1 = 3 sqrt5", s[0], 3 * sqrt(5), 1e-12); check("sigma_2 = sqrt5", s[1], sqrt(5), 1e-12)
W = np.array([[2, -1], [1, 2]]) / sqrt(5); P = W.T @ A
check_true("polar factor W orthogonal, P = W^T A symmetric positive", np.allclose(W @ W.T, np.eye(2)) and np.allclose(P, P.T) and np.all(np.linalg.eigvalsh(P) > 0))
check_true("P = sqrt5 (2 1;1 2)", np.allclose(P, sqrt(5) * np.array([[2, 1], [1, 2]])))
# figure: the last panel is the original, as intensities 1 - darkness
t = (root / "volume8-analysis/figures/linear-ch06-lowrank.tex").read_text()
O = np.zeros((32, 32))
for v, x, y in re.findall(r"\\fill\[black!(\d+)\] \((-?[\d.]+),(-?[\d.]+)\)", t):
    x, y = float(x), float(y)
    if x >= 114: O[31 - int(y), int(x - 114)] = int(v) / 100
M = 1 - O; sv = np.linalg.svd(M, compute_uv=False)
for k, printed in ((1, 0.30), (3, 0.16), (8, 0.07)):
    check(f"relative Frobenius error of rank {k}", sqrt((sv[k:] ** 2).sum() / (sv ** 2).sum()), printed, 0.006)
check_true("rank 8 costs 520 numbers", 8 * 65 == 520)
check_true("photograph: 24 triples fit, 25 do not", 24 * 2001 == 48024 <= 50000 < 25 * 2001 == 50025)
rng = np.random.default_rng(4)
for _ in range(20):
    m, n, k = 7, 5, 2
    A = rng.normal(size=(m, n)); U, s, Vt = np.linalg.svd(A); Ak = (U[:, :k] * s[:k]) @ Vt[:k]
    B = rng.normal(size=(m, k)) @ rng.normal(size=(k, n))
    check_true("Eckart-Young (both norms)", np.linalg.norm(A - B, 2) >= s[k] - 1e-12 and np.linalg.norm(A - B) ** 2 >= (s[k:] ** 2).sum() - 1e-9)
    check_true("pseudo-inverse = numpy pinv", np.allclose(np.linalg.pinv(A), Vt.T @ np.diag(1 / s) @ U[:, :n].T))
# pcatoy
X = np.array([[-2, -1], [-1, -1], [0, 0], [1, 1], [2, 1]], float); G = X.T @ X
w, V = np.linalg.eigh(G)
check("PCA slope 1/phi", V[1, 1] / V[0, 1], (sqrt(5) - 1) / 2, 1e-12)
check("explained variance", w[1] / w.sum(), (7 + 3 * sqrt(5)) / 14, 1e-12)
check("explained variance ~ 0.979", w[1] / w.sum(), 0.979, 5e-4)
# pinv of all-ones 2x2 is all-ones/4
check_true("pinv(J_2) = J_2/4", np.allclose(np.linalg.pinv(np.ones((2, 2))), np.ones((2, 2)) / 4))
# matrix completion
C = np.array([[2, 4, 20 / 3], [3, 6, 10], [1.5, 3, 5]])
check_true("completion has rank 1", np.linalg.matrix_rank(C) == 1)
finish()
