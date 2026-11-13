"""Chapter 8 numbers: tree escape, Kesten, hypercube resistance, return probabilities."""
from fractions import Fraction as F
from math import comb, sqrt, pi
import numpy as np
from common import check, check_true, finish

for d in range(3, 9):
    R = sum(F(1, d*(d-1)**(k-1)) for k in range(1, 200))
    check(f"R tree d={d}", float(R), (d-1)/(d*(d-2)), 1e-12)
    check(f"escape d={d}", 1/(d*float(R)), (d-2)/(d-1), 1e-12)
for k in range(1, 6):
    p, q = (2*k-1)/(2*k), 1/(2*k)
    check(f"sqrt(4pq) k={k}", sqrt(4*p*q), sqrt(2*k-1)/k, 1e-14)
    # f harmonic-type bound for g != e
    check(f"Schur ratio k={k}", (sqrt(2*k-1) + (2*k-1)/sqrt(2*k-1))/(2*k), sqrt(2*k-1)/k, 1e-14)
# Catalan lower bound C_m >= 4^m/((2m+1)(m+1))
check_true("Catalan bound", all(comb(2*m, m)//(m+1) >= 4**m/((2*m+1)*(m+1)) for m in range(60)))

# exact return probabilities on F_k via the length chain
def free_return(k, n):
    v = np.zeros(n+2); v[0] = 1.0
    out = []
    for t in range(1, n+1):
        w = np.zeros(n+2)
        w[1] += v[0]
        w[2:] += v[1:-1]*(2*k-1)/(2*k)
        w[:-1] += v[1:]*(1/(2*k)) * (np.arange(1, n+2) >= 1)
        v = w; out.append(v[0])
    return out
pr = free_return(2, 400)
check("F_2: p_{2n}^{1/2n} -> sqrt3/2 (n=200)", pr[399]**(1/400), sqrt(3)/2, 2e-2)
check("(sqrt3/2)^100", (sqrt(3)/2)**100, 5.7e-7, 0.05e-7)
p100Z2 = (comb(100, 50)/2**100)**2
check("Z^2 p_100 ~ 1/(50 pi)", p100Z2, 1/(50*pi), 1e-4)
check("Z^2 p_100 ~ 6e-3", p100Z2, 6e-3, 5e-4)
print("  exact F_2 p_100 =", pr[99], " ratio to Z^2:", p100Z2/pr[99])
check("exact F_2 p_100 ~ 2.4e-9", pr[99], 2.4e-9, 0.05e-9)
check_true("six orders of magnitude", 1e6 <= p100Z2/pr[99] < 1e7)

# hypercube: R = sum 1/((n-j) C(n,j)), n R -> 2, commute ~ 2^{n+1}
import networkx as nx
for n in range(2, 7):
    R = sum(F(1, (n-j)*comb(n, j)) for j in range(n))
    G = nx.hypercube_graph(n)
    L = nx.laplacian_matrix(G).toarray().astype(float)
    nodes = list(G.nodes()); a = nodes.index(tuple([0]*n)); b = nodes.index(tuple([1]*n))
    Lp = np.linalg.pinv(L); e = np.zeros(len(nodes)); e[a] = 1; e[b] = -1
    check(f"hypercube R n={n}", e @ Lp @ e, float(R), 1e-9)
n = 400
R = sum(F(1, (n-j)*comb(n, j)) for j in range(n))
check("n R -> 2 (n=400)", float(n*R), 2.0, 1e-2)
# Z^2 cutsets 8k+4
check_true("box boundary 8k+4", all(4*(2*k+1) == 8*k+4 for k in range(10)))
# speed (k-1)/k
check("speed k=3", (2*3-1)/(2*3) - 1/(2*3), 2/3, 1e-14)
finish()
