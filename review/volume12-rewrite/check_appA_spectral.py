"""Appendix A numbers: spanning-tree counts, Laplacian spectra, de Bruijn counts."""
import networkx as nx, numpy as np, itertools
from math import comb, factorial
from common import check, check_true, finish

def tau(G):
    import sympy
    L = sympy.Matrix(nx.laplacian_matrix(G).toarray().astype(int))
    return int(L[1:, 1:].det(method='bareiss'))
for n in range(2, 8):
    check(f"tau(K_{n})", tau(nx.complete_graph(n)), n**(n-2), 0)
for n in range(1, 6):
    f = 2**(2**n-n-1)
    for j in range(1, n+1): f *= j**comb(n, j)
    check(f"tau(Q_{n})", tau(nx.hypercube_graph(n)), f, 0)
check("tau(Q_3)=384", tau(nx.hypercube_graph(3)), 384, 0)
check("Petersen 2000", tau(nx.petersen_graph()), 2000, 0)
ev = sorted(np.round(np.linalg.eigvalsh(nx.laplacian_matrix(nx.petersen_graph()).toarray().astype(float)), 8))
check_true("Petersen Laplacian 0, 2^5, 5^4", ev == [0]+[2]*5+[5]*4)
for m, n in [(2, 3), (3, 4), (1, 4)]:
    check(f"tau(K_{m},{n})", tau(nx.complete_bipartite_graph(m, n)), m**(n-1)*n**(m-1), 0)
star = sorted(np.round(np.linalg.eigvalsh(nx.laplacian_matrix(nx.star_graph(4)).toarray().astype(float)), 8))
check_true("star K_{1,4} Laplacian 0,1,1,1,5", star == [0, 1, 1, 1, 5])
# de Bruijn sequences: count binary cyclic sequences of length 2^n containing every n-word, starting with n zeros
def debruijn(n, q=2):
    N = q**n; out = []
    for tail in itertools.product(range(q), repeat=N-n):
        s = (0,)*n + tail
        words = {tuple(s[(i+k) % N] for k in range(n)) for i in range(N)}
        if len(words) == N: out.append(''.join(map(str, s)))
    return out
d3 = debruijn(3)
check_true("n=3: exactly 00010111 and 00011101", sorted(d3) == ['00010111', '00011101'])
check("n=4: 16 sequences", len(debruijn(4)), 16, 0)
check("formula 2^{2^{n-1}-n} at n=6", 2**(2**5-6), 2**26, 0)
q, n = 3, 2
check("q-ary count (q!)^{q^{n-1}}/q^n, q=3,n=2", len(debruijn(2, 3)), factorial(3)**(3**1)//3**2, 0)
finish()
