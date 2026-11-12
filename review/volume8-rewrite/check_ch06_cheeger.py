#!/usr/bin/env python3
"""Volume 8, Chapter 6: the Fiedler figure (two clusters of 11, three bridges, best sweep set one cluster), Cheeger's inequality
on small graphs, hypercube h = 1, cycle asymptotics, Petersen (10,3,2), Alon-Boppana's bound, the path Laplacian."""
import re, pathlib
from itertools import combinations
from math import cos, pi, sqrt, floor, log
import numpy as np, networkx as nx
from common import check, check_true, finish
root = pathlib.Path(__file__).resolve().parents[2]
t = (root / "volume8-analysis/figures/spectral-ch09-fiedler.tex").read_text()
top = re.findall(r"\\draw\[(black!30|BrickRed,thick)\] \(([\d.]+),([\d.]+)\) -- \(([\d.]+),([\d.]+)\);", t)
G = nx.Graph(); bridges = 0
for st, a, b, c, d in top:
    G.add_edge((a, b), (c, d)); bridges += st.startswith("Brick")
check("vertices in the figure", G.number_of_nodes(), 22, 0); check("bridges", bridges, 3, 0)
L = nx.laplacian_matrix(G).toarray().astype(float); w, V = np.linalg.eigh(L); f = V[:, 1]; nodes = list(G)
order = np.argsort(f); best = None
for k in range(1, len(nodes)):
    S = {nodes[i] for i in order[:k]}
    if len(S) > len(nodes) / 2: S = set(nodes) - S
    r = nx.cut_size(G, S) / len(S)
    if best is None or r < best[0]: best = (r, S)
comps = list(nx.connected_components(nx.Graph([(u, v) for u, v in G.edges() if (float(u[0]) < 2.3) == (float(v[0]) < 2.3)])))
check_true("best sweep set is one cluster of 11 and cuts the 3 bridges", len(best[1]) == 11 and any(best[1] == c for c in comps) and nx.cut_size(G, best[1]) == 3)
# Cheeger on small regular graphs, brute force
def h(G):
    n = G.number_of_nodes(); V = list(G)
    return min(nx.cut_size(G, S) / len(S) for s in range(1, n // 2 + 1) for S in map(set, combinations(V, s)))
for name, H in [("Petersen", nx.petersen_graph()), ("Q_3", nx.hypercube_graph(3)), ("Q_4", nx.hypercube_graph(4)), ("C_9", nx.cycle_graph(9)), ("K_{3,3}", nx.complete_bipartite_graph(3, 3))]:
    d = max(dict(H.degree()).values()); mu = sorted(np.linalg.eigvalsh(nx.laplacian_matrix(H).toarray()))[1]; hh = h(H)
    check_true(f"Cheeger on {name}: mu2/2 <= h <= sqrt(2 d mu2)", mu / 2 - 1e-12 <= hh <= sqrt(2 * d * mu) + 1e-12)
for n in (3, 4): check(f"h(Q_{n})", h(nx.hypercube_graph(n)), 1, 1e-12)
for n in (7, 8, 10): check(f"h(C_{n}) = 2/floor(n/2)", h(nx.cycle_graph(n)), 2 / floor(n / 2), 1e-12)
n = 10**6; check("h/sqrt(2 d mu2) for C_n -> 1/pi", (2 / (n // 2)) / sqrt(4 * (2 - 2 * cos(2 * pi / n))), 1 / pi, 1e-5)
# Petersen (10,3,2), independent bound 4
s = sorted(np.linalg.eigvalsh(nx.to_numpy_array(nx.petersen_graph())))
check("Petersen lambda", max(abs(s[0]), abs(s[-2])), 2, 1e-9); check("n lambda/(d + lambda)", 10 * 2 / 5, 4, 0)
# path Laplacian eigenvectors
for n in (5, 8):
    Lp = nx.laplacian_matrix(nx.path_graph(n)).toarray()
    ok = all(np.allclose(Lp @ np.array([cos(j*pi*(2*v-1)/(2*n)) for v in range(1, n+1)]), (2 - 2*cos(j*pi/n)) * np.array([cos(j*pi*(2*v-1)/(2*n)) for v in range(1, n+1)])) for j in range(n))
    check_true(f"path P_{n}: Laplacian eigenpairs", ok)
# Alon-Boppana algebra, and checking the bound on a large random regular graph
for d in (3, 4, 7):
    a = lambda i: (d - 1) ** (-i / 2)
    check_true(f"d={d}: (d-1)(a_i - a_(i+1))^2 = a_i^2 (d - 2 sqrt(d-1))", all(abs((d-1)*(a(i)-a(i+1))**2 - a(i)**2*(d-2*sqrt(d-1))) < 1e-12 for i in range(5)))
R = nx.random_regular_graph(3, 2000, seed=1); l2 = sorted(np.linalg.eigvalsh(nx.to_numpy_array(R)))[-2]
check_true(f"random 3-regular graph on 2000 vertices: lambda_2 = {l2:.4f} is near 2 sqrt 2 = {2*sqrt(2):.4f}", abs(l2 - 2 * sqrt(2)) < 0.1)
finish()
