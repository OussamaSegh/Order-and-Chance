"""Exact finite support for Positive Matrices; never generates approval."""
from fractions import Fraction as Q
from itertools import product, permutations
from pathlib import Path
import math
import random
import re

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT/'volume3-symmetry/chapters/linear-ch07-perron.tex'


def mm(a, b):
    return tuple(tuple(sum(x*y for x, y in zip(row, col))
                       for col in zip(*b)) for row in a)


def power(a, k):
    b = tuple(tuple(int(i == j) for j in range(len(a))) for i in range(len(a)))
    while k:
        if k % 2:
            b = mm(b, a)
        a = mm(a, a)
        k //= 2
    return b


def mv(a, v):
    return tuple(sum(x*y for x, y in zip(row, v)) for row in a)


def solve(a, b):
    a = [list(map(Q, row))+[Q(x)] for row, x in zip(a, b)]
    n = len(a)
    for j in range(n):
        pivot = next(i for i in range(j, n) if a[i][j])
        a[j], a[pivot] = a[pivot], a[j]
        v = a[j][j]
        a[j] = [x/v for x in a[j]]
        for i in range(n):
            if i != j:
                v = a[i][j]
                a[i] = [x-v*y for x, y in zip(a[i], a[j])]
    return tuple(row[-1] for row in a)


def check_periods_and_wielandt():
    checked = 0
    for n in range(1, 4):
        for entries in product((0, 1), repeat=n*n):
            a = tuple(tuple(entries[i*n:(i+1)*n]) for i in range(n))
            powers = [power(a, k) for k in range(n+1)]
            if not all(any(b[i][j] for b in powers[:n])
                       for i in range(n) for j in range(n)):
                continue
            h = math.gcd(*(k for k in range(1, n+1)
                           if any(powers[k][i][i] for i in range(n))))
            if not h:
                assert a == ((0,),)
                assert not power(a, 1)[0][0]
                continue
            levels = {0: 0}
            pending = [0]
            while pending:
                i = pending.pop()
                for j in range(n):
                    if a[i][j] and j not in levels:
                        levels[j] = (levels[i]+1) % h
                        pending.append(j)
            assert set(levels.values()) == set(range(h))
            assert all((levels[j]-levels[i]-1) % h == 0
                       for i in range(n) for j in range(n) if a[i][j])
            bound = (n-1)**2+1
            positive = all(x > 0 for row in power(a, bound) for x in row)
            assert positive == (h == 1)
            checked += 1
    # One nonzero graph on one vertex; four on two vertices; eighteen
    # loop-free strongly connected graphs on three vertices, each with8
    # independent loop choices.
    assert checked == 1+4+18*8, checked
    for n in range(2, 13):
        a = [[0]*n for _ in range(n)]
        for i in range(n-1):
            a[i][i+1] = 1
        a[-1][0] = a[-1][1] = 1
        bound = (n-1)**2+1
        assert power(a, bound-1)[0][0] == 0
        assert all(x > 0 for row in power(a, bound) for x in row)


def check_oscillation_and_two_states():
    rng = random.Random(1401)
    for _ in range(240):
        n = rng.randint(1, 4)
        a = tuple(tuple(Q(rng.randint(1, 9)) for _ in range(n)) for _ in range(n))
        x = tuple(Q(rng.randint(1, 9)) for _ in range(n))
        y = tuple(Q(rng.randint(1, 9)) for _ in range(n))
        c = min(a[i][j]/a[k][j] for i, j, k in product(range(n), repeat=3))
        r = [u/v for u, v in zip(x, y)]
        s = [u/v for u, v in zip(mv(a, x), mv(a, y))]
        assert min(r) <= min(s) <= max(s) <= max(r)
        assert max(s)-min(s) <= (1-c*c)*(max(r)-min(r))
    for a, b in product((Q(1, 10), Q(1, 2), Q(9, 10)), repeat=2):
        p = ((1-a, a), (b, 1-b))
        e = ((b/(a+b), a/(a+b)),)*2
        for k in range(1, 11):
            expected = tuple(tuple(e[i][j]+(1-a-b)**k*(int(i == j)-e[i][j])
                                   for j in range(2)) for i in range(2))
            assert power(p, k) == expected


def check_actual_graphs_and_pagerank():
    fig = (ROOT/'volume3-symmetry/figures/linear-ch07-period.tex').read_text()
    edges = [(int(i)-1, int(j)-1) for i, j in re.findall(
        r'\\draw[^\n]*?\(v(\d+)(?:\.[^)]*)?\)[^\n]*?\(v(\d+)(?:\.[^)]*)?\)', fig)]
    assert len(edges) == 11
    a = tuple(tuple(int((i, j) in edges) for j in range(7)) for i in range(7))
    assert all(any(power(a, k)[i][j] for k in range(7))
               for i in range(7) for j in range(7))
    assert math.gcd(*(k for k in range(1, 8) if any(power(a, k)[i][i]
                                                  for i in range(7)))) == 3
    assert all((i, j) in edges for i, j in ((0, 2), (2, 5), (5, 0)))

    fig = (ROOT/'volume3-symmetry/figures/linear-ch07-pagerank.tex').read_text()
    edges = re.findall(r'\\draw[^\n]*?\(([A-H])\)[^\n]*?\(([A-H])\)', fig)
    names = 'ABCDEFGH'
    assert len(edges) == 15
    outdegree = {i: sum(u == i for u, v in edges) for i in names}
    assert sum(v == 'C' for u, v in edges) == 6
    assert [u for u, v in edges if v == 'A'] == ['C', 'D']
    assert [u for u, v in edges if v == 'B'] == ['A', 'E']
    alpha = Q(17, 20)
    g = tuple(tuple(alpha*Q(int((i, j) in edges), outdegree[i])+(1-alpha)/8
                    for j in names) for i in names)
    equations = [[g[j][i]-int(i == j) for j in range(8)] for i in range(7)]
    equations.append([1]*8)
    pi = solve(equations, [0]*7+[1])
    assert all(x > 0 for x in pi) and sum(pi) == 1
    assert tuple(sum(pi[i]*g[i][j] for i in range(8)) for j in range(8)) == pi
    assert [round(float(x), 3) for x in pi] == [.329, .169, .351, .029, .036, .040, .027, .019]
    # Independent derivation: convergent finite geometric iteration, with an
    # exact a priori contraction error, must enclose the stationary solution.
    mu = (Q(1),)+(Q(0),)*7
    for _ in range(40):
        mu = tuple(sum(mu[i]*g[i][j] for i in range(8)) for j in range(8))
    assert sum(abs(x-y) for x, y in zip(mu, pi)) <= 2*alpha**40
    sizes = {name: Q(size) for size, name in re.findall(
        r'minimum size=([\d.]+)cm[^\n]*?\(([A-H])\)', fig)}
    assert set(sizes) == set(names)
    for i, name in enumerate(names):
        expected = 1.30*math.sqrt(float(pi[i]/pi[2]))
        assert abs(float(sizes[name])-expected) < .006
    assert alpha**50 > Q(1, 10000)
    assert alpha**85 > Q(1, 10**6) > alpha**86
    assert alpha**50 < Q(296, 10**6)
    # Actual two-page counterexample to50-step/six-digit accuracy:
    # P=I, uniform teleportation, initial row(1,0), stationary row(1/2,1/2).
    assert alpha**50/2 > Q(1, 10**6)
    for name in ('A', 'C'):
        line = next(line for line in fig.splitlines() if f'({name}) at' in line)
        assert 'text=white' in line


def check_corrected_domains_and_prerequisites(source=None):
    source = SOURCE.read_text() if source is None else source
    assert source.index(r'\label{linear:prop:levels}') < source.index(r'\label{linear:thm:frobenius}')
    assert 'For non-zero irreducible' in source
    assert r'no period under our definition' in source
    assert r'$z/\|z\|$' in source
    assert 'finite sequential compactness' in source.replace('\n', ' ')
    assert 'state-independent' in source
    assert 'positive-length closed walk' in source
    assert 'about $50$' not in source


if __name__ == '__main__':
    check_periods_and_wielandt()
    check_oscillation_and_two_states()
    check_actual_graphs_and_pagerank()
    check_corrected_domains_and_prerequisites()
    print('Positive Matrices: exact graph, contraction, stationary-rank and boundary probes pass; no approval generated.')
