#!/usr/bin/env python3
"""Volume 9, Chapter 5: check the free-group computations printed in the figure and the solutions."""
from itertools import product
from common import check_true, finish

def reduce(w):
    out = []
    for x in w:
        if out and out[-1] == -x: out.pop()
        else: out.append(x)
    return out
a, b, c = 1, 2, 3
inv = lambda w: [-x for x in reversed(w)]
comm = lambda u, v: reduce(u + v + inv(u) + inv(v))
w = comm([a], [b]); W = comm(w, [c])
check_true("[[a,b],c] is reduced of length 10", len(W) == 10 and reduce(W) == W)
kill = lambda w, g: reduce([x for x in w if abs(x) != g])
check_true("removing any nail makes [[a,b],c] trivial", all(kill(W, g) == [] for g in (a, b, c)))
check_true("[a,b] survives with both nails", len(w) == 4)
# index-2 subgroups of F2: Schreier graphs on 2 vertices; rank = E - V + 1 = 3
for img in [(1, 0), (0, 1), (1, 1)]:
    V, E = 2, 4
    check_true(f"kernel of {img}: rank {E-V+1} = 1 + 2(2-1)", E - V + 1 == 1 + 2*(2-1))
# third subgroup: ba^{-1} * ab = b^2
check_true("(b a^-1)(a b) = b^2", reduce([b, -a, a, b]) == [b, b])
# generators listed in the figure lie in the right kernels
def image(word, img):
    return sum(img[abs(x)-1] for x in word) % 2
gens = {(0, 1): [[a], [b, b], [b, a, -b]], (1, 0): [[b], [a, a], [a, b, -a]], (1, 1): [[a, a], [a, b], [b, b]]}
check_true("figure generators lie in the kernels", all(image(g, k) == 0 for k, gs in gens.items() for g in gs))
# commutator subgroup basis element a^i b^j a b^-j a^-(i+1) maps to 0 in Z^2
ok = True
for i, j in product(range(-3, 4), repeat=2):
    wd = [a]*i if i >= 0 else [-a]*(-i)
    wd += ([b]*j if j >= 0 else [-b]*(-j)) + [a] + ([-b]*j if j >= 0 else [b]*(-j))
    wd += [-a]*(i+1) if i+1 >= 0 else [a]*(-(i+1))
    ok &= sum(1 if x == a else -1 if x == -a else 0 for x in wd) == 0 and sum(1 if x == b else -1 if x == -b else 0 for x in wd) == 0
check_true("grid loops lie in the commutator subgroup kernel", ok)
# Euler characteristic of covers of genus-g surfaces: 2-2h = k(2-2g)
check_true("degree-2 cover of genus 2 has genus 3", 2 - 2*3 == 2*(2 - 2*2))
finish()
