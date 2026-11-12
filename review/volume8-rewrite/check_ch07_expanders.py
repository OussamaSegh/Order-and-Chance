#!/usr/bin/env python3
"""Volume 8, Chapter 7: tree moments (a_4 = 15, a_6 = 87 for d = 3) against the Kesten-McKay measure, the q_k polynomials,
Ihara-Bass on small graphs, K_4 (N_3 = N_4 = 24, pi(3) = 8, pi(4) = 6), the cycle zeta function, the graph prime number theorem,
|SL_2(F_p)|, the Catalan moments of the semicircle, the figure's poles (598 on |u| = 1/sqrt 2, plus 1 and 1/2), the Chernoff algebra."""
import re, pathlib
from math import comb, sqrt, pi
import numpy as np, networkx as nx, sympy as sp
from scipy.integrate import quad
from common import check, check_true, finish
root = pathlib.Path(__file__).resolve().parents[2]
x, d = sp.symbols("x d")
# q_k
q = [sp.Integer(1), x, x**2 - d]
for k in range(2, 7): q.append(sp.expand(x * q[k] - (d - 1) * q[k - 1]))
check_true("q_3 = x^3 - (2d-1) x", sp.expand(q[3] - (x**3 - (2*d - 1)*x)) == 0)
check_true("q_4 = x^4 - (3d-2)x^2 + d(d-1)", sp.expand(q[4] - (x**4 - (3*d - 2)*x**2 + d*(d - 1))) == 0)
check_true("q_6 coefficients", sp.expand(q[6] - (x**6 - (5*d - 4)*x**4 + (6*d**2 - 9*d + 3)*x**2 - d*(d - 1)**2)) == 0)
# tree closed walks by brute force on a ball of T_d, against the formulas and the measure
def tree_walks(dd, k):
    # count closed walks of length k from the root of T_dd by dynamic programming on distance
    v = {0: 1}
    for _ in range(k):
        w = {}
        for r, c in v.items():
            if r == 0: w[1] = w.get(1, 0) + dd * c
            else:
                w[r + 1] = w.get(r + 1, 0) + (dd - 1) * c; w[r - 1] = w.get(r - 1, 0) + c
        v = w
    return v.get(0, 0)
for dd in (3, 4, 5):
    check(f"d={dd}: a_4 = d(2d-1)", tree_walks(dd, 4), dd * (2*dd - 1), 0)
    check(f"d={dd}: a_6 = d(5d^2-6d+2)", tree_walks(dd, 6), dd * (5*dd**2 - 6*dd + 2), 0)
    R = 2 * sqrt(dd - 1); dens = lambda t: dd * sqrt(max(4*(dd - 1) - t*t, 0)) / (2*pi*(dd*dd - t*t))
    check(f"d={dd}: mass of nu_d", quad(dens, -R, R)[0], 1, 1e-8)
    for k in (2, 4, 6, 8):
        check(f"d={dd}: moment {k} of nu_d = closed walks", quad(lambda t: t**k * dens(t), -R, R, limit=200)[0], tree_walks(dd, k), 1e-6 * tree_walks(dd, k))
check("a_4 for d = 3", tree_walks(3, 4), 15, 0); check("a_6 for d = 3", tree_walks(3, 6), 87, 0)
# Catalan moments of the semicircle
for k in range(6):
    m = quad(lambda y: y**(2*k) * sqrt(4 - y*y) / (2*pi), -2, 2)[0]
    check(f"semicircle moment 2k={2*k} = C_k", m, comb(2*k, k) // (k + 1), 1e-8)
# Hashimoto matrix and Ihara-Bass
def hashimoto(G):
    E = [(u, v) for u, v in G.edges()] + [(v, u) for u, v in G.edges()]; idx = {e: i for i, e in enumerate(E)}
    B = np.zeros((len(E), len(E)))
    for (a, b) in E:
        for c in G[b]:
            if c != a: B[idx[(a, b)], idx[(b, c)]] = 1
    return B
def bass_ok(G):
    B = hashimoto(G); A = nx.to_numpy_array(G); n, m = len(G), G.number_of_edges()
    Q = np.diag([G.degree(v) - 1 for v in G])
    for u in (0.13, -0.37, 0.71):
        lhs = np.linalg.det(np.eye(2*m) - u*B); rhs = (1 - u*u)**(m - n) * np.linalg.det(np.eye(n) - u*A + u*u*Q)
        if abs(lhs - rhs) > 1e-8 * max(1, abs(lhs)): return False
    return True
for name, G in [("Petersen", nx.petersen_graph()), ("K_4", nx.complete_graph(4)), ("Q_3", nx.hypercube_graph(3)), ("irregular (lollipop)", nx.lollipop_graph(4, 3)), ("random 3-regular", nx.random_regular_graph(3, 12, seed=2))]:
    check_true(f"Ihara-Bass (with Q) on {name}", bass_ok(G))
B = hashimoto(nx.complete_graph(4))
N = {k: round(np.trace(np.linalg.matrix_power(B, k))) for k in range(1, 9)}
check("K_4: N_3", N[3], 24, 0); check("K_4: N_4", N[4], 24, 0); check_true("K_4: N_1 = N_2 = 0", N[1] == N[2] == 0)
def prims(N, K):
    pr = {}
    for k in range(1, K + 1): pr[k] = (N[k] - sum(l * pr[l] for l in range(1, k) if k % l == 0)) // k
    return pr
pr = prims(N, 8); check("K_4: pi(3)", pr[3], 8, 0); check("K_4: pi(4)", pr[4], 6, 0)
mu = np.roots([1, 1, 2])[0]; check("mu^3 + conj = 5", (mu**3 + np.conj(mu)**3).real, 5, 1e-12); check("mu^4 + conj = 1", (mu**4 + np.conj(mu)**4).real, 1, 1e-12)
# cycle zeta
for n in (5, 6):
    B = hashimoto(nx.cycle_graph(n)); u = sp.symbols("u")
    ok = all(abs(np.linalg.det(np.eye(2*n) - t*B) - (1 - t**n)**2) < 1e-10 for t in (0.3, -0.6, 0.9))
    check_true(f"C_{n}: det(I - uB) = (1-u^n)^2", ok)
# graph prime number theorem on Petersen (Ramanujan, non-bipartite, q = 2)
P = nx.petersen_graph(); B = hashimoto(P); n = 10; qq = 2
N = {k: round(np.trace(np.linalg.matrix_power(B, k))) for k in range(1, 21)}; pr = prims(N, 20)
check_true("Petersen: |pi(k) - q^k/k| <= 6 n q^(k/2)/k for 2 <= k <= 20", all(abs(pr[k] - qq**k / k) <= 6*n*qq**(k/2) / k for k in range(2, 21)))
# SL_2(F_p)
for p in (3, 5, 7):
    import itertools
    G = [(a, b, c, e) for a, b, c, e in itertools.product(range(p), repeat=4) if (a*e - b*c) % p == 1]
    check(f"|SL_2(F_{p})| = p(p^2-1)", len(G), p*(p*p - 1), 0)
    mul = lambda X, Y: ((X[0]*Y[0] + X[1]*Y[2]) % p, (X[0]*Y[1] + X[1]*Y[3]) % p, (X[2]*Y[0] + X[3]*Y[2]) % p, (X[2]*Y[1] + X[3]*Y[3]) % p)
    gens = [(1, 1, 0, 1), (1, p - 1, 0, 1), (1, 0, 1, 1), (1, 0, p - 1, 1)]
    seen = {(1, 0, 0, 1)}; fr = [(1, 0, 0, 1)]
    while fr:
        nf = []
        for g in fr:
            for s in gens:
                h = mul(s, g)
                if h not in seen: seen.add(h); nf.append(h)
        fr = nf
    check_true(f"U, L generate SL_2(F_{p})", len(seen) == p*(p*p - 1))
# the figure: right panel poles
t = (root / "volume8-analysis/figures/ch09-kestenmckay.tex").read_text()
pts = re.findall(r"\\fill\[([^\]]*)\] \(([\d.-]+),([\d.-]+)\) circle \(([\d.]+)pt\)", t)
r = [np.hypot(float(a) - 8.6, float(b)) / 2.5 for c, a, b, s in pts if float(a) > 5.7]
check("figure: poles on |u| = 1/sqrt2", sum(abs(v - 1/sqrt(2)) < 2e-3 for v in r), 598, 0)
check_true("figure: the two others at 1 and 1/2", sorted(round(v, 3) for v in r if abs(v - 1/sqrt(2)) >= 2e-3) == [0.5, 1.0])
check("figure: 598 + 2 = 2n poles from det(I - uA + 2u^2 I), n = 300", len(r), 600, 0)
# Chernoff algebra: the exponent with r = eps(1 - alpha)/10
eps, al = sp.symbols("epsilon alpha", positive=True); rr = eps*(1 - al)/10
check_true("Chernoff exponent = -eps^2 (1-alpha) t/20", sp.simplify(-rr*eps + 5*rr**2/(1 - al) + eps**2*(1 - al)/20) == 0)
finish()
