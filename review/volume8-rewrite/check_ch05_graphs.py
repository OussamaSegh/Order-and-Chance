#!/usr/bin/env python3
"""Volume 8, Chapter 5: basic spectra, Petersen, the Hoffman bound 4, Moore multiplicities (1729, 1520), the Kneser bound,
Huang's matrices, the Q_4 search (48 of 11440), the spectrum-count exercise, the infinite friendship graph's degree 5."""
from itertools import combinations
from math import comb, sqrt
import numpy as np, networkx as nx
from common import check, check_true, finish

def spec(G): return np.sort(np.linalg.eigvalsh(nx.to_numpy_array(G)))[::-1]
P = nx.petersen_graph(); s = spec(P)
check_true("Petersen spectrum 3, 1^5, -2^4", np.allclose(s, [3] + [1] * 5 + [-2] * 4))
check("Hoffman bound for Petersen", 10 * 2 / (3 + 2), 4, 1e-12)
check("alpha(Petersen)", max(len(c) for c in nx.find_cliques(nx.complement(P))), 4, 0)
for n in (5, 7, 8):
    check_true(f"C_{n} spectrum 2cos(2 pi j/n)", np.allclose(spec(nx.cycle_graph(n)), sorted([2*np.cos(2*np.pi*j/n) for j in range(n)], reverse=True)))
    check_true(f"P_{n} spectrum 2cos(j pi/(n+1))", np.allclose(spec(nx.path_graph(n)), sorted([2*np.cos(j*np.pi/(n+1)) for j in range(1, n+1)], reverse=True)))
for n in (3, 4, 5):
    exp = sorted(sum([[n - 2*j] * comb(n, j) for j in range(n + 1)], []), reverse=True)
    check_true(f"Q_{n} spectrum n-2j with multiplicity C(n,j)", np.allclose(spec(nx.hypercube_graph(n)), exp))
# friendship: windmill satisfies the hypothesis
W = nx.windmill_graph(4, 3)  # four triangles sharing a vertex
check_true("windmill: every pair has one common neighbour", all(len(set(W[u]) & set(W[v])) == 1 for u, v in combinations(W, 2)))
# spectrum count exercise
sp = [3, 1, 1, 1, 1, 1, -2, -2, -2, -2]
check("tr A^2 / 2 = edges", sum(x*x for x in sp) / 2, 15, 0); check("tr A^3 / 6 = triangles", sum(x**3 for x in sp) / 6, 0, 0)
# srg multiplicities
def mult(n, k, l, m):
    D = (l - m)**2 + 4*(k - m); q = (2*k + (n - 1)*(l - m)) / sqrt(D)
    return (n - 1 - q) / 2, (n - 1 + q) / 2
check_true("Petersen multiplicities 5, 4", np.allclose(mult(10, 3, 0, 1), (5, 4)))
mt, mu = mult(3250, 57, 0, 1); check("Moore 57: m_theta", mt, 1729, 1e-9); check("Moore 57: m_tau", mu, 1520, 1e-9)
check_true("Moore 57: roots 7, -8 of x^2 + x - 56", 49 + 7 - 56 == 0 and 64 - 8 - 56 == 0)
check_true("Moore 57 satisfies k(k-l-1) = (n-k-1) mu", 57*56 == 3250 - 58)
ks = [k for k in range(1, 5000) if (lambda s: s*s == 4*k - 3 and (s**4 - 2*s*s - 15) % (16*s) == 0)(int(round(sqrt(4*k - 3))))]
check_true("degrees with 4k-3 square and 16s | s^4-2s^2-15 are 1, 3, 7, 57", ks == [1, 3, 7, 57])
# Kneser K(n,2)
for n in range(4, 9):
    K = nx.kneser_graph(n, 2); s = spec(K); k = comb(n - 2, 2)
    bound = comb(n, 2) * (-s[-1]) / (k - s[-1])
    check(f"Kneser K({n},2): Hoffman bound = n-1", bound, n - 1, 1e-9)
    check_true(f"Kneser K({n},2): eigenvalues {{k, 1, 3-n}}", set(np.round(s, 9)) <= {k, 1, 3 - n})
# Huang
A = np.array([[0, 1], [1, 0]])
for n in range(2, 8):
    A = np.block([[A, np.eye(2**(n-1))], [np.eye(2**(n-1)), -A]])
    Q = nx.to_numpy_array(nx.hypercube_graph(n), nodelist=sorted(nx.hypercube_graph(n), key=lambda v: v[::-1]))
    ok = np.allclose(A @ A, n * np.eye(2**n)) and np.array_equal(np.abs(A), Q)
    check_true(f"Huang A_{n}: A^2 = {n} I and |A| = adjacency of Q_{n}", ok)
# Q_4 search
Q4 = nx.hypercube_graph(4); V = list(Q4); cnt = 0; shapes = set()
for S in combinations(V, 9):
    H = Q4.subgraph(S); d = max(dict(H.degree()).values())
    check_true("Huang bound on Q_4 (max degree >= 2)", d >= 2) if d < 2 else None
    if d == 2:
        cnt += 1; shapes.add(tuple(sorted(len(c) for c in nx.connected_components(H))))
check("nine-element sets of Q_4 with max degree 2", cnt, 48, 0); check("C(16,9)", comb(16, 9), 11440, 0)
check_true("each is an 8-cycle plus an isolated vertex", shapes == {(1, 8)})
cyc = ["0000","0001","0101","0111","1111","1011","1010","0010"]
H = nx.Graph([(a, b) for a, b in combinations(cyc + ["1100"], 2) if sum(x != y for x, y in zip(a, b)) == 1])
H.add_nodes_from(cyc + ["1100"])
check_true("the printed 8-cycle plus 1100 has max degree 2 and is a cycle plus a point", max(dict(H.degree()).values()) == 2 and sorted(len(c) for c in nx.connected_components(H)) == [1, 8])
# infinite friendship graph: degree of a in G_2
def step(G):
    G = G.copy(); new = []
    for u, v in combinations(list(G), 2):
        if not set(G[u]) & set(G[v]): new.append((u, v))
    for u, v in new:
        w = ("w", u, v); G.add_edge(w, u); G.add_edge(w, v)
    return G
G0 = nx.empty_graph(["a", "b", "c"]); G1 = step(G0); G2 = step(G1)
check_true("G_1 is a hexagon", nx.is_isomorphic(G1, nx.cycle_graph(6)))
check("degree of a in G_2", G2.degree("a"), 5, 0)
check_true("G_2 has at most one common neighbour per pair", all(len(set(G2[u]) & set(G2[v])) <= 1 for u, v in combinations(G2, 2)))
# Schwenk: -3 is not a Petersen eigenvalue; 5 + 5 > 9
check_true("-3 not in Petersen spectrum", not np.any(np.isclose(spec(P), -3)))
finish()
