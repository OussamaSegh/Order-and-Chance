#!/usr/bin/env python3
"""Volume 8, Chapter 9: the Sturm-Liouville eigenvalues of the figure (q = 60x), the bounds pi^2 n^2 <= lambda_n <= pi^2 n^2 + max q,
the min kernel eigenvalues, the 81% of the first Karhunen-Loeve mode, Basel and zeta(4) from the string, the norm 2/pi of Volterra,
the Poisson trace, and the integral in the proof of the initial value lemma."""
from math import pi, sqrt
import numpy as np, sympy as sp
from scipy.linalg import eigh_tridiagonal
from common import check, check_true, finish
# Sturm-Liouville with q = 60x by a fine finite-difference discretisation
M = 20000; h = 1 / M; x = np.arange(1, M) * h
d = 2 / h**2 + 60 * x; e = -np.ones(M - 2) / h**2
lam = eigh_tridiagonal(d, e, select="i", select_range=(0, 3), eigvals_only=True)
for n, (v, p) in enumerate(zip(lam, [36.2, 70.4, 119.5, 188.3]), 1):
    check(f"lambda_{n} for q = 60x", v, p, 0.05)
    check_true(f"pi^2 n^2 <= lambda_{n} <= pi^2 n^2 + 60", pi**2*n*n <= v <= pi**2*n*n + 60)
for n, p in zip(range(1, 5), [9.9, 39.5, 88.8, 157.9]): check(f"pi^2 {n}^2", pi**2*n*n, p, 0.05)
# min kernel
N = 2000; t = (np.arange(N) + 0.5) / N; K = np.minimum.outer(t, t) / N
ev = np.sort(np.linalg.eigvalsh(K))[::-1][:4]
check_true("min(s,t) eigenvalues 1/((n-1/2)^2 pi^2)", np.allclose(ev, [1/((n - 0.5)**2*pi**2) for n in range(1, 5)], rtol=1e-4))
check("first KL mode share 8/pi^2", 8/pi**2, 0.81, 0.005)
check("sum of lambda_n = int_0^1 t dt", sum(1/((n - 0.5)**2*pi**2) for n in range(1, 200001)), 0.5, 1e-5)
# Basel and zeta(4) from G = min - st
s, u = sp.symbols("s u")
check_true("int_0^1 (x - x^2) = 1/6", sp.integrate(s - s**2, (s, 0, 1)) == sp.Rational(1, 6))
check_true("||G||_2^2 = 1/90", sp.integrate(2*sp.integrate(u**2*(1 - s)**2, (u, 0, s)), (s, 0, 1)) == sp.Rational(1, 90))
# Volterra norm
V = np.tril(np.ones((N, N))) / N - np.eye(N) / (2*N)
check("||V|| = 2/pi", np.linalg.norm(V, 2), 2/pi, 1e-4)
# Poisson trace
r = 0.6; check("sum r^|n| = (1+r)/(1-r)", sum(r**abs(n) for n in range(-200, 201)), (1 + r)/(1 - r), 1e-12)
check("P_r(0) = (1-r^2)/(1-r)^2", (1 - r*r)/(1 - r)**2, (1 + r)/(1 - r), 1e-12)
# integral in Lemma ivp
n = sp.symbols("n", positive=True, integer=True); S = sp.symbols("S", positive=True)
check_true("int_0^s (s-t) t^(2n-2) dt = s^(2n)/((2n-1) 2n)", all(sp.simplify(sp.integrate((S - u)*u**(2*k - 2), (u, 0, S)) - S**(2*k)/((2*k - 1)*2*k)) == 0 for k in range(1, 6)))
finish()
