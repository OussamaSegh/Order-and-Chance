"""Independent exact support for Chapter 3 examples; no general proof status."""
from collections import Counter
from functools import lru_cache
import itertools
import math
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)


def add(a, b):
    return trim([ (a[i] if i < len(a) else 0)+(b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def remainder(a, b):
    a = list(trim(a)); b = trim(b)
    while len(a) >= len(b) and a != [0]:
        assert a[-1] % b[-1] == 0
        coefficient, offset = a[-1]//b[-1], len(a)-len(b)
        for j, v in enumerate(b):
            a[offset+j] -= coefficient*v
        a = list(trim(a))
    return trim(a)


@lru_cache(None)
def gaussian(n, k):
    if k < 0 or k > n: return (0,)
    if k == 0 or k == n: return (1,)
    return add(gaussian(n-1, k-1), (0,)*k+gaussian(n-1, k))


@lru_cache(None)
def cyclotomic(n):
    a = [-1]+[0]*(n-1)+[1]
    for d in range(1, n):
        if n % d: continue
        b = cyclotomic(d)
        quotient = [0]*(len(a)-len(b)+1)
        while len(a) >= len(b) and a != [0]:
            coefficient, offset = a[-1]//b[-1], len(a)-len(b)
            quotient[offset] = coefficient
            for j, v in enumerate(b): a[offset+j] -= coefficient*v
            a = list(trim(a))
        assert a == [0]
        a = list(trim(quotient))
    return trim(a)


def check_sieving():
    for n in range(1, 13):
        for k in range(n+1):
            coefficients = gaussian(n, k)
            assert sum(coefficients) == math.comb(n, k)
            for m in range(1, n+1):
                if n % m: continue
                expected = math.comb(n//m, k//m) if k % m == 0 else 0
                assert remainder(add(coefficients, (-expected,)), cyclotomic(m)) == (0,)
            if n <= 9:
                # Independent subset-weight derivation, without the recurrence.
                weights = Counter(sum(c)-k*(k-1)//2
                                  for c in itertools.combinations(range(n), k))
                actual = tuple(weights[i] for i in range(max(weights)+1))
                assert actual == coefficients


def check_necklace_plate():
    text = (ROOT/'volume3-symmetry/figures/ch03-necklaces.tex').read_text()
    groups = re.findall(r'\\draw\[gray\].*?circle \(0\.55\);(.*?)(?=\\draw\[gray\]|\\end\{tikzpicture\})', text, re.S)
    assert len(groups) == 14
    canonical = lambda w: min(w[i:]+w[:i] for i in range(6))
    words = set()
    for block in groups:
        w = tuple(x == 'MidnightBlue' for x in re.findall(r'fill=(white|MidnightBlue)\]', block))
        assert len(w) == 6
        assert canonical(w) not in words
        words.add(canonical(w))
        count = int(re.search(r'\\node\[font=\\scriptsize\].*?\{(\d+)\}', block)[1])
        assert count == len({w[i:]+w[:i] for i in range(6)})
    assert words == {canonical(w) for w in itertools.product((False, True), repeat=6)}


def check_colour_orbits():
    normals = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]
    rotations = []
    for p in itertools.permutations(range(3)):
        parity = (-1)**sum(p[i] > p[j] for i in range(3) for j in range(i+1,3))
        for signs in itertools.product((-1,1), repeat=3):
            if parity*math.prod(signs) == 1:
                rotations.append(tuple(normals.index(tuple(signs[i]*v[p[i]] for i in range(3))) for v in normals))
    colours = list(itertools.product(range(3), repeat=6))
    renamed = list(itertools.permutations(range(3)))
    assert len({min(tuple(w[g[i]] for i in range(6)) for g in rotations) for w in colours}) == 57
    assert len({min(tuple(s[w[g[i]]] for i in range(6)) for g in rotations for s in renamed) for w in colours}) == 15
    # Independently count partitions with <=3 blocks, avoiding palette renaming.
    def partition_key(w):
        names = {}
        return tuple(names.setdefault(x, len(names)) for x in w)
    partitions = {partition_key(w) for w in colours}
    assert len(partitions) == 122
    assert len({min(partition_key(tuple(w[g[i]] for i in range(6))) for g in rotations) for w in partitions}) == 15
    # Graphs on four vertices: direct edge-subset orbits and edge counts.
    edges = list(itertools.combinations(range(4), 2))
    permutations = list(itertools.permutations(range(4)))
    def graph_key(subset):
        return min(tuple(sorted(tuple(sorted((p[a], p[b]))) for a,b in subset)) for p in permutations)
    graphs = {graph_key([edges[i] for i in range(6) if mask >> i & 1]) for mask in range(64)}
    assert len(graphs) == 11 and sum(len(g) == 3 for g in graphs) == 3
    # Q8 from its actual 2x2 complex matrices; entries remain exact Gaussian integers.
    mul = lambda a,b: (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
                       a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3])
    one, i, j = (1,0,0,1), (1j,0,0,-1j), (0,1,-1,0)
    positive = [one, i, j, mul(i,j)]
    group = positive+[tuple(-x for x in a) for a in positive]
    assert len(set(group)) == 8
    inverse = lambda g: next(h for h in group if mul(g,h) == one)
    classes = {frozenset(mul(mul(g,x),inverse(g)) for g in group) for x in group}
    assert sorted(map(len, classes)) == [1,1,2,2,2]
    assert sum(mul(a,b) == mul(b,a) for a,b in itertools.product(group, repeat=2)) == 40


def check_nilpotents():
    for q, n in ((2, 0), (2, 1), (2, 2), (2, 3), (3, 2), (3, 3)):
        count = 0
        for values in itertools.product(range(q), repeat=n*n):
            a = [values[i*n:(i+1)*n] for i in range(n)]
            power = [[int(i == j) for j in range(n)] for i in range(n)]
            for _ in range(n):
                power = [[sum(power[i][k]*a[k][j] for k in range(n)) % q
                          for j in range(n)] for i in range(n)]
            count += not any(any(row) for row in power)
        assert count == q**(n*n-n), (q, n, count)
    # Independent solution of the counting recurrence with rational arithmetic.
    from fractions import Fraction as F
    for q in (2, 3, 4, 5, 8, 9):
        total = F(0)
        for n in range(9):
            gl = math.prod(q**n-q**j for j in range(n))
            total += F(q**(n*n-n), gl)
            assert total == F(q**(n*n), gl)


def check_touchard():
    bell = [1]
    for n in range(125):
        bell.append(sum(math.comb(n, j)*bell[j] for j in range(n+1)))
    for p in (2, 3, 5, 7):
        for n in range(20):
            assert (bell[n+p]-bell[n+1]-bell[n]) % p == 0
        for m in range(1, 7):
            for n in range(10):
                if n+p**m < len(bell):
                    assert (bell[n+p**m]-m*bell[n]-bell[n+1]) % p == 0


if __name__ == '__main__':
    check_sieving()
    check_necklace_plate()
    check_colour_orbits()
    check_nilpotents()
    check_touchard()
    print('PASS: exact Gaussian-root/subset coefficients; all14 actual necklace diagrams; nilpotent matrices and recurrence; Touchard boundaries')
