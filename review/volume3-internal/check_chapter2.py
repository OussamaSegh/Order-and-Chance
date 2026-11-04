"""Focused boundary and actual subgroup-plate regressions; not proof certificates."""
import itertools
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]


def check_infinite_cyclic_explanation(source):
    solution = re.search(r'\\begin\{solution\}\{ex:normalnormal\}(.*?)\\end\{solution\}', source, re.S)[1]
    assert 'infinite cyclic' in solution.lower(), 'Unrestricted cyclic case needs its infinite-order proof'
    assert 'g^{-1}' in solution, 'Infinite cyclic automorphism must account for inversion'


def check_subgroup_plate():
    # D4 as affine functions j -> sign*j+shift on Z4, with rightmost map first.
    group = [(k, sign) for sign in (1, -1) for k in range(4)]
    mul = lambda a, b: ((a[0]+a[1]*b[0]) % 4, a[1]*b[1])
    identity = (0, 1)
    def generate(generators):
        reached = {identity}
        while True:
            grown = reached | {mul(x, g) for x in reached for g in generators}
            if grown == reached:
                return frozenset(reached)
            reached = grown
    subgroups = set()
    for size in range(1 << len(group)):
        subset = {group[i] for i in range(len(group)) if size >> i & 1}
        if identity in subset and all(mul(a, b) in subset for a in subset for b in subset):
            subgroups.add(frozenset(subset))
    r, s = (1, 1), (0, -1)
    nodes = {'d0': frozenset({identity}), 'd1': generate([(2, 1)]),
             'd2': generate([s]), 'd3': generate([mul(s, r)]),
             'd4': generate([mul(s, (2, 1))]), 'd5': generate([mul(s, (3, 1))]),
             'd6': generate([r]), 'd7': generate([s, (2, 1)]),
             'd8': generate([mul(s, r), (2, 1)]), 'd9': frozenset(group)}
    assert set(nodes.values()) == subgroups and len(subgroups) == 10
    def inverse(g):
        return next(h for h in group if mul(g, h) == identity)
    normal = {name for name, h in nodes.items()
              if all(mul(mul(g, x), inverse(g)) in h for g in group for x in h)}
    source = (ROOT/'volume3-symmetry/figures/ch02-lattices.tex').read_text()
    actual_normal = set(re.findall(r'\\node\[nor\] \((d\d+)\)', source))
    assert actual_normal == normal and len(normal) == 6
    expected_edges = {frozenset((a, b)) for a, h in nodes.items() for b, k in nodes.items()
                      if h < k and not any(h < l < k for l in subgroups)}
    actual_edges = {frozenset((a, b)) for a, b in re.findall(r'\((d\d+)\) -- \((d\d+)\)', source)}
    assert expected_edges == actual_edges and len(expected_edges) == 15
    # C12 lattice, independently construct the actual additive subgroups.
    z = {f'z{d}': frozenset((k*(12//d)) % 12 for k in range(d)) for d in (1, 2, 3, 4, 6, 12)}
    covers = {frozenset((a, b)) for a, h in z.items() for b, k in z.items()
              if h < k and not any(h < l < k for l in z.values())}
    actual = {frozenset((a, b)) for a, b in re.findall(r'\((z\d+)\) -- \((z\d+)\)', source)}
    assert covers == actual


def check_semidirect():
    for n in range(1, 10):
        group = list(itertools.product(range(n), range(2)))
        mul = lambda a, b: ((a[0]+(-1)**a[1]*b[0]) % n, (a[1]+b[1]) % 2)
        for a in group:
            inverse = ((-(-1)**a[1]*a[0]) % n, a[1])
            assert mul(a, inverse) == mul(inverse, a) == (0, 0)
        for a, b, c in itertools.product(group, repeat=3):
            assert mul(mul(a, b), c) == mul(a, mul(b, c))
    # Concrete counterexample behind the repaired infinite argument:
    # 2Z and 3Z both have infinite cardinality and are distinct subgroups.
    assert {2*k for k in range(-9, 10)} != {3*k for k in range(-9, 10)}


if __name__ == '__main__':
    check_infinite_cyclic_explanation((ROOT/'volume3-symmetry/chapters/ch02-quotients.tex').read_text())
    check_subgroup_plate()
    check_semidirect()
    print('PASS: infinite-cyclic proof coverage; all D4/C12 lattice nodes/edges; semidirect associativity/inverses in finite probes')
