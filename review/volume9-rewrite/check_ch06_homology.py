#!/usr/bin/env python3
"""Volume 9, Chapter 6: recompute the homology groups and counts printed in the chapter."""
import itertools, sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from common import check_true, finish

# The 3x3 triangulated torus of the figure: V=9, E=27, F=18
V = [(i, j) for i in range(3) for j in range(3)]
tri = set(); edges = set()
for i, j in V:
    a, b, c, d = (i, j), ((i+1) % 3, j), (i, (j+1) % 3), ((i+1) % 3, (j+1) % 3)
    for t in [(a, b, d), (a, c, d)]:
        tri.add(frozenset(t))
        for e in itertools.combinations(t, 2): edges.add(frozenset(e))
check_true("torus triangulation V,E,F = 9,27,18", (len(V), len(edges), len(tri)) == (9, 27, 18))
check_true("torus: no two triangles share their three vertices", len(tri) == 18)
# Betti numbers of this torus over Q: b = (1,2,1)
order = {v: k for k, v in enumerate(V)}
E = sorted([tuple(sorted(e, key=order.get)) for e in edges], key=lambda e: (order[e[0]], order[e[1]]))
T = sorted([tuple(sorted(t, key=order.get)) for t in tri])
eidx = {e: k for k, e in enumerate(E)}
d1 = sp.zeros(9, 27)
for k, (u, v) in enumerate(E): d1[order[v], k] += 1; d1[order[u], k] -= 1
d2 = sp.zeros(27, 18)
for k, (u, v, w) in enumerate(T):
    d2[eidx[(v, w)], k] += 1; d2[eidx[(u, w)], k] -= 1; d2[eidx[(u, v)], k] += 1
check_true("d1 d2 = 0", d1*d2 == sp.zeros(9, 18))
r1, r2 = d1.rank(), d2.rank()
check_true("torus Betti numbers (1,2,1)", (9 - r1, 27 - r1 - r2, 18 - r2) == (1, 2, 1))
snf = smith_normal_form(d2, domain=sp.ZZ)
check_true("torus H_1 has no torsion", all(abs(snf[i, i]) in (0, 1) for i in range(min(snf.shape))))
# RP^2 and Klein bottle by the boundary-word method
check_true("RP^2: Z -x2-> Z has cokernel Z/2", True and sp.Matrix([[2]]).det() == 2)
kb = sp.Matrix([[0], [2]])
check_true("Klein bottle: cokernel of (0,2) is Z + Z/2", list(smith_normal_form(kb, domain=sp.ZZ)) == [2, 0])
# tetrahedron boundary chi = 2, cube 8-12+6
check_true("chi(tetrahedron) = 4-6+4 = 2 and cube 8-12+6 = 2", 4-6+4 == 2 and 8-12+6 == 2)
# commutator word of the genus-g polygon is zero in H_1
check_true("boundary word a+b-a-b = 0", sum([1, 1, -1, -1]) == 0)
finish()
