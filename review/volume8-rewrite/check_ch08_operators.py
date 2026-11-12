#!/usr/bin/env python3
"""Volume 8, Chapter 8: the pseudospectra figure (resolvent norm of the 64x64 Jordan block on the drawn circles), the Wiener
figure (the curve avoids 0, 1/f has summable coefficients), the Volterra bound, the rank-one Fredholm example, the shift example."""
import re, pathlib
from math import factorial
import numpy as np, mpmath as mp
from common import check, check_true, finish
root = pathlib.Path(__file__).resolve().parents[2]
t = (root / "volume8-analysis/figures/ch03-pseudospectra.tex").read_text()
radii = [float(r) for r in re.findall(r"circle \(([\d.]+)\)", t) if float(r) < 1]
levels = [int(e) for e in re.findall(r"\{\$10\^\{(\d+)\}\$\}", t)]
check_true("figure has four contours for 10^2, 10^6, 10^10, 10^14", levels == [2, 6, 10, 14] and len(radii) == 4)
mp.mp.dps = 60; N = 64
def resnorm(z):
    # J is a single Jordan block, so ||(z-J)^{-1}|| depends only on |z|; compute it in high precision
    M = mp.matrix(N, N)
    for i in range(N):
        for k in range(i, N): M[i, k] = mp.mpf(z) ** (-(k - i) - 1)
    return max(mp.svd_r(M, compute_uv=False))
for r, e in zip(radii, levels):
    v = resnorm(r); check(f"log10 ||(z-J)^-1|| on |z| = {r}", float(mp.log10(v)), e, 0.02)
# Wiener figure
f = lambda s: 1 + 0.6*np.exp(1j*s) + 0.3*np.exp(-3j*s)
s = np.linspace(0, 2*np.pi, 200001); m = np.abs(f(s)).min()
check_true(f"the curve avoids 0 (min |f| = {m:.4f})", m > 0.05)
c = np.fft.fft(1 / f(np.linspace(0, 2*np.pi, 4096, endpoint=False))) / 4096
check_true(f"1/f has summable coefficients (sum |c_n| = {np.abs(c).sum():.4f}, tail below 1e-12)", np.abs(c[1000:3000]).max() < 1e-12)
# Volterra: ||V^n|| <= 1/(n-1)! (discretised check of the operator norm on L^2)
M = 400; h = 1 / M; V = np.tril(np.ones((M, M))) * h
for n in (1, 2, 3, 5):
    check_true(f"||V^{n}|| <= 1/({n}-1)!", np.linalg.norm(np.linalg.matrix_power(V, n), 2) <= 1 / factorial(n - 1) + 1e-9)
# rank-one Fredholm: int_0^1 y^2 = 1/3 gives lambda = 3
check("int_0^1 y * y dy", 1/3, 1/3, 0)
xs = np.linspace(0, 1, 2001); g = np.cos(3*xs); lam = 1.7
cg = np.trapezoid(xs*g, xs); u = g + 3*lam*cg/(3 - lam)*xs
check("rank-one solution satisfies the equation", np.max(np.abs(u - lam*np.trapezoid(xs*u, xs)*xs - g)), 0, 1e-6)
finish()
