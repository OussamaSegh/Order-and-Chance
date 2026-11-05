"""Finite support for Symmetry Diagonalises; no mathematical approval generated."""
from fractions import Fraction as Q
from itertools import product, permutations, combinations
from pathlib import Path
import cmath
import math
import random
import re
import mpmath as mp
from check_appendix_a import mm, power

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT/'volume3-symmetry/chapters/linear-ch09-symmetry.tex'


def det(a):
    a = [list(map(Q, row)) for row in a]
    answer = Q(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return Q(0)
        if pivot != j:
            a[pivot], a[j] = a[j], a[pivot]
            answer = -answer
        v = a[j][j]
        answer *= v
        for i in range(j+1, len(a)):
            ratio = a[i][j]/v
            for k in range(j+1, len(a)):
                a[i][k] -= ratio*a[j][k]
    return answer


def check_circulants_and_cubic():
    with mp.workdps(70):
        for n in range(1, 10):
            omega = mp.exp(2j*mp.pi/n)
            c = [2*k-3 for k in range(n)]
            a = [[c[(k-j) % n] for k in range(n)] for j in range(n)]
            eigenvalues = []
            for t in range(n):
                v = [omega**(t*j) for j in range(n)]
                eigenvalue = sum(c[k]*omega**(t*k) for k in range(n))
                eigenvalues.append(eigenvalue)
                assert max(abs(sum(a[i][j]*v[j] for j in range(n))-eigenvalue*v[i])
                           for i in range(n)) < mp.mpf('1e-60')
            assert abs(mp.fprod(eigenvalues)-int(det(a))) < mp.mpf('1e-55')
            for j, k in product(range(n), repeat=2):
                value = sum(omega**(l*(j+k)) for l in range(n))/n
                assert abs(value-int((j+k) % n == 0)) < mp.mpf('1e-60')
            shift = [[int(k == (j+1) % n) for k in range(n)] for j in range(n)]
            numerator = [[sum(Q(1, 2)**k*power(shift, k)[i][j] for k in range(n))
                          for j in range(n)] for i in range(n)]
            left = [[Q(int(i == j))-Q(1, 2)*shift[i][j] for j in range(n)]
                    for i in range(n)]
            assert mm(left, numerator) == tuple(tuple((1-Q(1, 2)**n)*int(i == j)
                                                       for j in range(n)) for i in range(n))
    cubic = lambda a, b, c: a**3+b**3+c**3-3*a*b*c
    assert cubic(1, 1, 1) == 0 and 1+1+1 > 0  # Old sign claim fails.
    residues = {cubic(a, b, c) % 9 for a, b, c in product(range(9), repeat=3)}
    assert residues == {0, 1, 2, 4, 5, 7, 8}
    for m in range(-100, 101):
        assert cubic(m+1, m, m) == 3*m+1
        assert cubic(m-1, m, m) == 3*m-1
        assert cubic(m+1, m-1, m) == 9*m


def paley(p):
    squares = {x*x % p for x in range(1, p)}
    return tuple(tuple(int((i-j) % p in squares) for j in range(p)) for i in range(p))


def check_paley_and_actual_figures():
    for p in (5, 13, 17, 29, 37):
        a = paley(p)
        aa = mm(a, a)
        for i, j in product(range(p), repeat=2):
            assert aa[i][j] == (p-1)//4-a[i][j]+((p-1)//4)*int(i == j)
        c = next(c for c in range(1, p) if not a[c][0])
        assert all(a[c*i % p][c*j % p] == 1-int(i == j)-a[i][j]
                   for i in range(p) for j in range(p))
    a = paley(17)
    assert [i for i in range(17) if a[0][i] and a[1][i]] == [2, 9, 16]
    cliques = lambda size: [s for s in combinations(range(17), size)
                            if all(a[i][j] for i, j in combinations(s, 2))]
    assert len(cliques(3)) == 68
    assert not cliques(4)
    assert not any(all(not a[i][j] for i, j in combinations(s, 2))
                   for s in combinations(range(17), 4))

    source = (ROOT/'volume3-symmetry/figures/linear-ch09-paley.tex').read_text()
    labels = re.findall(r'\\node[^\n]*?at \(([-\d.]+),([-\d.]+)\) \{(\d+)\}', source)
    assert len(labels) == 13
    coords = {(x, y): int(label) for x, y, label in labels}
    for x, y, label in labels:
        theta = 2*math.pi*int(label)/13
        assert abs(float(x)-2*math.sin(theta)) <= .00051
        assert abs(float(y)-2*math.cos(theta)) <= .00051
    edges = re.findall(r'\\draw\[(MidnightBlue|BrickRed|ForestGreen)[^\n]*?\(([-\d.]+),([-\d.]+)\) -- \(([-\d.]+),([-\d.]+)\)', source)
    actual = set()
    for colour, x, y, u, v in edges:
        i, j = coords[(x, y)], coords[(u, v)]
        difference = (i-j) % 13
        target = {'MidnightBlue': {1, 12}, 'BrickRed': {3, 10}, 'ForestGreen': {4, 9}}
        assert difference in target[colour]
        actual.add(tuple(sorted((i, j))))
    assert len(actual) == len(edges) == 39
    assert actual == {(i, j) for i, j in combinations(range(13), 2) if paley(13)[i][j]}

    source = (ROOT/'volume3-symmetry/figures/linear-ch09-circulant.tex').read_text()
    curve = next(line for line in source.splitlines() if '-- (3.999,0.079)' in line)
    points = re.findall(r'\(([-\d.]+),([-\d.]+)\)', curve)
    assert len(points) == 401
    for j, (x, y) in enumerate(points):
        theta = 2*math.pi*j/400
        value = 1+2*cmath.exp(1j*theta)+cmath.exp(3j*theta)
        assert abs(float(x)-value.real) <= .00051
        assert abs(float(y)-value.imag) <= .00051
        assert abs(float(x)-(1+2*math.cos(theta)+math.cos(3*theta))) <= .00051
        assert abs(float(y)-(2*math.sin(theta)+math.sin(3*theta))) <= .00051
    filled = re.findall(r'\\fill\[BrickRed\] \(([-\d.]+),([-\d.]+)\)', source)
    assert len(filled) == 14
    for j, (x, y) in enumerate(filled[:7]):
        value = 1.2*cmath.exp(2j*math.pi*j/7)
        assert abs(complex(float(x), float(y))-value) <= .00072
    for j, (x, y) in enumerate(filled[7:]):
        z = cmath.exp(2j*math.pi*j/7)
        assert abs(complex(float(x), float(y))-(1+2*z+z**3)) <= .00072


def choose(n, k):
    return math.comb(n, k) if 0 <= k <= n else 0


def kraw(n, k, t):
    return sum((-1)**j*choose(t, j)*choose(n-t, k-j) for j in range(k+1))


def check_codes_and_krawtchouk():
    for n in range(8):
        for k, l in product(range(n+1), repeat=2):
            assert sum(choose(n, t)*kraw(n, k, t)*kraw(n, l, t)
                       for t in range(n+1)) == 2**n*choose(n, k)*int(k == l)
        for t in range(n+1):
            assert sum(kraw(n, k, t) for k in range(n+1)) == 2**n*int(t == 0)
            assert all(kraw(n, k, n-t) == (-1)**k*kraw(n, k, t) for k in range(n+1))
    for n in range(4):
        words = list(range(2**n))
        for mask in range(1, 2**len(words)):
            code = [x for x in words if mask >> x & 1]
            distribution = [Q(sum((x ^ y).bit_count() == i for x in code for y in code), len(code))
                            for i in range(n+1)]
            for k in range(n+1):
                lhs = sum(distribution[i]*kraw(n, k, i) for i in range(n+1))
                rhs = Q(sum(sum((-1)**((x & t).bit_count()) for x in code)**2
                            for t in words if t.bit_count() == k), len(code))
                assert lhs == rhs and lhs >= 0
            minimum = min(((x ^ y).bit_count() for x, y in combinations(code, 2)), default=n+1)
            for d in range(1, n+2):
                if minimum >= d and 2*d > n:
                    assert len(code) <= Q(2*d, 2*d-n)
    simplex = [int(word, 2) for word in re.search(
        r'0000000,.*?1101001', SOURCE.read_text(), re.S).group().replace('\\ ', ' ').replace('\n', ' ').split(',')]
    assert len(simplex) == len(set(simplex)) == 8
    assert all((x ^ y).bit_count() == 4 for x, y in combinations(simplex, 2))
    code = [sum(((a & x).bit_count() % 2 ^ b) << x for x in range(8))
            for a, b in product(range(8), range(2))]
    assert len(set(code)) == 16
    assert {sum((x ^ y).bit_count() == i for y in code) for x in code for i in [4]} == {14}
    assert all((x ^ y).bit_count() in (4, 8) for x, y in combinations(code, 2))
    for t in range(9):
        f = (t-4)*(t-8)
        assert Q(2)+2*kraw(8, 1, t)+Q(1, 2)*kraw(8, 2, t) == f
        if t >= 4:
            assert f <= 0


def check_nonabelian_group_determinant():
    group = list(permutations(range(3)))
    compose = lambda a, b: tuple(a[b[i]] for i in range(3))
    inverse = lambda a: tuple(a.index(i) for i in range(3))
    sign = lambda a: (-1)**sum(a[i] > a[j] for i, j in combinations(range(3), 2))
    def rho(g):
        return tuple(tuple(int(i == g[j])-int(i == g[2]) for j in range(2)) for i in range(2))
    coordinates = [[1]*6, [sign(g) for g in group]]+[
        [rho(g)[i][j] for g in group] for i, j in product(range(2), repeat=2)]
    assert det(coordinates) != 0
    for g, h in product(group, repeat=2):
        assert mm(rho(g), rho(h)) == rho(compose(g, h))
    rng = random.Random(1501)
    for _ in range(40):
        x = dict(zip(group, (rng.randint(-3, 3) for _ in group)))
        regular = [[x[compose(g, inverse(h))] for h in group] for g in group]
        block = [[sum(x[g]*rho(g)[i][j] for g in group) for j in range(2)] for i in range(2)]
        assert det(regular) == sum(x.values())*sum(x[g]*sign(g) for g in group)*det(block)**2


def check_local_contract(source=None):
    source = SOURCE.read_text() if source is None else source
    assert 'not all equal' in source
    assert 'We can earn the needed spectral bound here' in source
    assert 'For every nonempty code' in source
    assert 'The maximum in the statement exists' in source
    assert 'when values' in source and 'multiplicities add' in source
    assert 'For $n=0$' in source and 'If $n\\ge1$' in source
    assert 'generic determinant' in source
    assert 'found in Volume~8' not in source


if __name__ == '__main__':
    check_circulants_and_cubic()
    check_paley_and_actual_figures()
    check_codes_and_krawtchouk()
    check_nonabelian_group_determinant()
    check_local_contract()
    print('Symmetry appendix finite spectral/figure/code/group-determinant probes pass; no approval generated.')
