"""Volume 10, Chapter 1: the finite checks behind Theorem thm:notnatural and Exercise ex:f2plane."""
import itertools
from common import check_true, finish

# thm:notnatural: lambda^2 = 1 for every nonzero lambda exactly when |K| <= 3 (prime fields 2, 3, 5, 7).
for p in (2, 3, 5, 7):
    allsq1 = all(l * l % p == 1 for l in range(1, p))
    check_true(f"F_{p}: every nonzero square is 1 iff p<=3", allsq1 == (p <= 3))
# F_4 = F_2[w]/(w^2+w+1), elements a+bw as pairs (a, b)
def mul4(x, y):
    a, b = x; c, d = y  # (a+bw)(c+dw) = ac + (ad+bc)w + bd w^2, w^2 = w+1
    return ((a * c + b * d) % 2, (a * d + b * c + b * d) % 2)
check_true("F_4: some nonzero square is not 1", any(mul4(x, x) != (1, 0) for x in [(1, 0), (0, 1), (1, 1)]))

def vecs(n): return list(itertools.product((0, 1), repeat=n))
def add(u, v): return tuple((a + b) % 2 for a, b in zip(u, v))
def indep(u, v): return any(u) and any(v) and u != v

# ex:f2plane: eta(v)(w) = 1 iff v, w independent is linear in w and in v, bijective onto V*, GL_2-invariant.
V = vecs(2)
eta = {v: tuple(int(indep(v, w)) for w in V) for v in V}
lin_w = all(eta[v][V.index(add(w1, w2))] == (eta[v][V.index(w1)] + eta[v][V.index(w2)]) % 2 for v in V for w1 in V for w2 in V)
lin_v = all(eta[add(v1, v2)] == tuple((a + b) % 2 for a, b in zip(eta[v1], eta[v2])) for v1 in V for v2 in V)
check_true("eta(v) is a linear form", lin_w)
check_true("eta is additive in v", lin_v)
check_true("eta is injective", len(set(eta.values())) == 4)

# dimension 3: no nonzero GL_3(F_2)-invariant bilinear form B(v,w) depending only on (v==w, independent)
V3 = vecs(3)
found = []
for c, d in itertools.product((0, 1), repeat=2):
    B = lambda v, w: 0 if not any(v) or not any(w) else (c if v == w else d)
    if all(B(v, add(w1, w2)) == (B(v, w1) + B(v, w2)) % 2 for v in V3 for w1 in V3 for w2 in V3):
        found.append((c, d))
check_true("dimension 3 over F_2: only the zero invariant form", found == [(0, 0)])
finish()
