#!/usr/bin/env python3
"""Recompute the printed numbers of Chapter 9 (ch09-gue.tex, moments-zeta.tex)."""
import math
import numpy as np
from scipy import integrate
from common import check, check_true, finish

# form factor: transform of sinc^2 is the triangle
for a in [0.0, 0.3, 0.7, 0.99, 1.3]:
    val = 2 * integrate.quad(lambda u: (np.sinc(u)) ** 2 * math.cos(2 * math.pi * a * u), 0, 400, limit=4000)[0]
    check(f"hat K({a})", val, max(0, 1 - a), 3e-3)
check("int_0^1 alpha = 1/2", integrate.quad(lambda a: a, 0, 1)[0], 0.5, 1e-12)
# surmises: densities, means, small-gap constants, Monte Carlo
p1 = lambda s: math.pi / 2 * s * math.exp(-math.pi * s * s / 4)
p2 = lambda s: 32 / math.pi ** 2 * s * s * math.exp(-4 * s * s / math.pi)
for name, f in [("p1", p1), ("p2", p2)]:
    check(f"{name} mass", integrate.quad(f, 0, np.inf)[0], 1, 1e-10)
    check(f"{name} mean", integrate.quad(lambda s: s * f(s), 0, np.inf)[0], 1, 1e-10)
e = 1e-3
check("int_0^e p1 ~ pi/4 e^2", integrate.quad(p1, 0, e)[0] / e ** 2, math.pi / 4, 1e-5)
check("int_0^e p2 ~ 32/(3pi^2) e^3", integrate.quad(p2, 0, e)[0] / e ** 3, 32 / (3 * math.pi ** 2), 1e-5)
rng = np.random.default_rng(3); M = 400000
a, c = rng.standard_normal(M), rng.standard_normal(M)
b = rng.normal(0, math.sqrt(.5), M)
D = np.sqrt((a - c) ** 2 + 4 * b * b); S = D / D.mean()
check("GOE 2x2: P(S<0.5) vs surmise", (S < .5).mean(), integrate.quad(p1, 0, .5)[0], 3e-3)
u, v = rng.normal(0, math.sqrt(.5), M), rng.normal(0, math.sqrt(.5), M)
D = np.sqrt((a - c) ** 2 + 4 * (u * u + v * v)); S = D / D.mean()
check("GUE 2x2: P(S<0.5) vs surmise", (S < .5).mean(), integrate.quad(p2, 0, .5)[0], 3e-3)
check("E R (GOE) = sqrt(pi/2)", integrate.quad(lambda r: r * r * math.exp(-r * r / 2), 0, np.inf)[0], math.sqrt(math.pi / 2), 1e-10)
check("E R (GUE) = 2 sqrt(2/pi)", math.sqrt(2 / math.pi) * integrate.quad(lambda r: r ** 3 * math.exp(-r * r / 2), 0, np.inf)[0], 2 * math.sqrt(2 / math.pi), 1e-10)
# Barnes G and Keating-Snaith
def G(n):  # G(n) for integer n >= 1
    return math.prod(math.factorial(j) for j in range(n - 1))
for k, pr in [(1, 1), (2, 1 / 12), (3, 42 / math.factorial(9)), (4, 24024 / math.factorial(16))]:
    check(f"G(k+1)^2/G(2k+1), k={k}", G(k + 1) ** 2 / G(2 * k + 1), pr, 1e-15 * max(pr, 1e-30) + 1e-25)
check_true("hint G values 1,1,1,2,12,288,34560", [G(n) for n in range(1, 8)] == [1, 1, 1, 2, 12, 288, 34560])
check_true("9! = 42*8640", math.factorial(9) == 42 * 8640)
check("Ingham: 6/pi^2 * 1/12 = 1/(2 pi^2)", 6 / math.pi ** 2 / 12, 1 / (2 * math.pi ** 2), 1e-15)
def ks(N, k): return math.prod((N + l + i) / (l + i) for l in range(k) for i in range(1, k + 1))
for k in range(1, 5):
    check(f"prod (l+i) = G(2k+1)/G(k+1)^2, k={k}", math.prod(l + i for l in range(k) for i in range(1, k + 1)), G(2 * k + 1) / G(k + 1) ** 2, 0)
    check(f"KS product N=1 is binom(2k,k), k={k}", ks(1, k), math.comb(2 * k, k), 1e-9)
    check(f"KS product ~ G-ratio N^k^2, k={k}", ks(10 ** 7, k) / 10 ** (7 * k * k), G(k + 1) ** 2 / G(2 * k + 1), 1e-5 * G(k + 1) ** 2 / G(2 * k + 1) * k * k)
check("E|det(1-U)|^2 = N+1 (N=5)", ks(5, 1), 6, 1e-12)
# CUE Monte Carlo for k=2, N=3 (Haar via QR)
def haar(n):
    Z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / math.sqrt(2)
    Q, R = np.linalg.qr(Z); d = np.diag(R); return Q * (d / abs(d))
vals = [abs(np.linalg.det(np.eye(3) - haar(3))) ** 4 for _ in range(60000)]
check("CUE N=3, E|det|^4 Monte Carlo", np.mean(vals), ks(3, 2), 0.03 * ks(3, 2))
# Riemann-von Mangoldt: unfolding constant and mean spacing
F = lambda g: g / (2 * math.pi) * math.log(g / (2 * math.pi * math.e)) + 7 / 8
try:
    import mpmath
    zs = [float(mpmath.zetazero(n).imag) for n in range(1, 301)]
    check("N(T) vs F at T=gamma_300", 300 - F(zs[-1]), 0, 2.0)
    sp = np.diff([F(g) for g in zs])
    check("unfolded mean spacing (first 300 zeros)", sp.mean(), 1, 0.02)
    check_true("no unfolded spacing below 0.05 (repulsion)", sp.min() > 0.05)
except ImportError:
    print("   mpmath missing: zero checks skipped")
finish()
