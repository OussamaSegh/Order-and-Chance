"""Volume 10, Chapter 2 (Kronecker products, tensor rank, Strassen): every printed number recomputed."""
import itertools, math
import numpy as np, sympy as sp
from common import check, check_true, finish
rng = np.random.default_rng(1)

# Proposition linear:prop:kronecker on random matrices
A, B = rng.normal(size=(3, 3)), rng.normal(size=(2, 2))
K = np.kron(A, B)
check("det(A (x) B) = det(A)^p det(B)^m", np.linalg.det(K), np.linalg.det(A) ** 2 * np.linalg.det(B) ** 3, 1e-9)
ev = np.sort_complex(np.linalg.eigvals(np.kron(A, np.eye(2)) + np.kron(np.eye(3), B)))
ev2 = np.sort_complex(np.array([a + b for a in np.linalg.eigvals(A) for b in np.linalg.eigvals(B)]))
check("Kronecker sum eigenvalues", float(np.max(np.abs(ev - ev2))), 0.0, 1e-9)
X, C = rng.normal(size=(3, 4)), rng.normal(size=(4, 2))
vec = lambda M: M.reshape(-1, order="F")
check("vec trick", float(np.max(np.abs(vec(A @ X @ C) - np.kron(C.T, A) @ vec(X)))), 0.0, 1e-12)

# Example linear:exa:rotation: the real decomposition of length 3 of the tensor with slices I, J
def tensor(terms, n=2):
    T = np.zeros((n, n, n))
    for u, v, w in terms: T += np.einsum("i,j,k->ijk", u, v, w)
    return T
T = tensor([((1, 1), (0, 1), (1, 0)), ((-1, 1), (1, 0), (0, 1)), ((1, 0), (1, -1), (1, 1))])
check_true("slice 1 is I", np.allclose(T[:, :, 0], np.eye(2)))
check_true("slice 2 is J", np.allclose(T[:, :, 1], [[0, -1], [1, 0]]))

# Example linear:exa:wtensor
e1, e2 = np.array([1., 0]), np.array([0., 1])
W = tensor([(e1, e1, e2), (e1, e2, e1), (e2, e1, e1)])
check_true("W slices", np.allclose(W[:, :, 0], [[0, 1], [1, 0]]) and np.allclose(W[:, :, 1], [[1, 0], [0, 0]]))
for eps in (0.1, 0.01):
    f = e1 + eps * e2
    We = (tensor([(f, f, f)]) - tensor([(e1, e1, e1)])) / eps
    rest = tensor([(e1, e2, e2), (e2, e1, e2), (e2, e2, e1)])
    check(f"W_eps expansion eps={eps}", float(np.max(np.abs(We - (W + eps * rest + eps ** 2 * tensor([(e2, e2, e2)]))))), 0.0, 1e-12)
check("||W||", float(np.linalg.norm(W)), math.sqrt(3), 1e-12)

# Strassen's formulas over non-commuting symbols
a = sp.Matrix(2, 2, lambda i, j: sp.Symbol(f"a{i+1}{j+1}", commutative=False))
b = sp.Matrix(2, 2, lambda i, j: sp.Symbol(f"b{i+1}{j+1}", commutative=False))
M1 = (a[0,0] + a[1,1]) * (b[0,0] + b[1,1]); M2 = (a[1,0] + a[1,1]) * b[0,0]
M3 = a[0,0] * (b[0,1] - b[1,1]); M4 = a[1,1] * (b[1,0] - b[0,0])
M5 = (a[0,0] + a[0,1]) * b[1,1]; M6 = (a[1,0] - a[0,0]) * (b[0,0] + b[0,1])
M7 = (a[0,1] - a[1,1]) * (b[1,0] + b[1,1])
S = sp.Matrix([[M1 + M4 - M5 + M7, M3 + M5], [M2 + M4, M1 - M2 + M3 + M6]])
check_true("Strassen = AB without commutativity", all(sp.expand(x) == 0 for x in (S - a * b)))

# Exercise linear:ex:strassencount
T_ = {1: 1}
for s_ in range(1, 11): T_[2 ** s_] = 7 * T_[2 ** (s_ - 1)] + 18 * 4 ** (s_ - 1)
check_true("T(n) = 7 n^log2(7) - 6 n^2", all(T_[2 ** s_] == 7 * 7 ** s_ - 6 * 4 ** s_ for s_ in range(11)))
check("T(512)", T_[512] / 1e8, 2.81, 0.005); check("schoolbook 512", (2 * 512 ** 3 - 512 ** 2) / 1e8, 2.68, 0.005)
check("T(1024)", T_[1024] / 1e9, 1.97, 0.005); check("schoolbook 1024", (2 * 1024 ** 3 - 1024 ** 2) / 1e9, 2.15, 0.005)
check_true("crossover at 1024, not 512", T_[512] > 2 * 512 ** 3 - 512 ** 2 and T_[1024] < 2 * 1024 ** 3 - 1024 ** 2)
check("log2 7", math.log2(7), 2.807, 0.0005)

# Exercise linear:ex:complexmult: complex decomposition
c = lambda *x: np.array(x, dtype=complex)
Tc = sum(np.einsum("i,j,k->ijk", u, v, w) for u, v, w in [(c(1, 1j), c(1, 1j), c(1, -1j) / 2), (c(1, -1j), c(1, -1j), c(1, 1j) / 2)])
check_true("complex multiplication tensor of rank 2", np.allclose(Tc[:, :, 0], [[1, 0], [0, -1]]) and np.allclose(Tc[:, :, 1], [[0, 1], [1, 0]]))
x_, y_ = 1.3 + 0.7j, -0.4 + 2.1j
P1, P2, P3 = x_.real * y_.real, x_.imag * y_.imag, (x_.real + x_.imag) * (y_.real + y_.imag)
check("Gauss three products", abs(complex(P1 - P2, P3 - P1 - P2) - x_ * y_), 0.0, 1e-12)

# Exercise linear:ex:waring
x, y, z = sp.symbols("x y z")
check_true("24xyz identity", sp.expand((x+y+z)**3 - (-x+y+z)**3 - (x-y+z)**3 - (x+y-z)**3 - 24*x*y*z) == 0)

# Exercise linear:ex:schmidtcheck
sv = np.linalg.svd(np.array([[1, 2], [2, 0]]) / 3, compute_uv=False)
check("sigma1", sv[0], 0.854, 0.0005); check("sigma2", sv[1], 0.521, 0.0005)
check("entropy", float(-sum(s * s * math.log2(s * s) for s in sv)), 0.843, 0.0005)

# Exercise linear:ex:gridlap
for n in (50, 200):
    L = np.diag([2.0] * n) - np.diag([1.0] * (n - 1), 1) - np.diag([1.0] * (n - 1), -1)
    lap = np.kron(L, np.eye(n)) + np.kron(np.eye(n), L) if n == 50 else None
    lam = 2 - 2 * np.cos(np.pi * np.arange(1, n + 1) / (n + 1))
    check_true(f"L_{n} eigenvalues", np.allclose(np.sort(np.linalg.eigvalsh(L)), np.sort(lam)))
    kappa = (2 * lam.max()) / (2 * lam.min())
    check(f"kappa / (4n^2/pi^2), n={n}", kappa / (4 * n * n / math.pi ** 2), 1.0, 0.05)
finish()
