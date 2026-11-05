"""Exact example regressions; these computations do not prove general claims."""
from collections import Counter
from fractions import Fraction as Q
import itertools
import math
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]


def check_tools_context(source):
    """A tools list cannot silently require a later chapter of this volume."""
    for body in re.findall(r'\\tools(.*?)(?=\\leads|\\end\{solution\})', source, re.S):
        for chapter in re.findall(r'(?<!Volume~1, )(?<!Volume~2, )Chapter~(\d+)', body):
            assert int(chapter) <= 1, f'Chapter 1 solution requires future Chapter {chapter}'


def check_matrices():
    for p in (2, 3, 5, 7):
        counts = Counter()
        gl = sl = 0
        for a, b, c, d in itertools.product(range(p), repeat=4):
            det, trace = (a*d-b*c) % p, (a+d) % p
            gl += det != 0
            sl += det == 1
            roots = sum((x*x-trace*x+det) % p == 0 for x in range(p))
            kind = ('scalar' if a == d and b == c == 0 else
                    'distinct' if roots == 2 else 'irreducible' if roots == 0 else 'repeated')
            counts[kind] += 1
            # The local 2x2 Cayley--Hamilton identity is checked entrywise.
            assert (a*a+b*c-trace*a+det) % p == 0
            assert (a*b+b*d-trace*b) % p == 0
            assert (c*a+d*c-trace*c) % p == 0
            assert (c*b+d*d-trace*d+det) % p == 0
        assert counts == dict(scalar=p, distinct=p*p*(p*p-1)//2,
                              irreducible=p*p*(p-1)**2//2, repeated=p*(p*p-1))
        assert gl == (p*p-1)*(p*p-p) and sl == p*(p*p-1)


def check_d4_plate():
    # Read the actual 64 node labels and compare with composition on 4 vertices,
    # independently of the symbolic relation used to typeset the table.
    source = (ROOT/'volume3-symmetry/figures/ch01-symmetries.tex').read_text()
    permutations = [tuple((j+k) % 4 for j in range(4)) for k in range(4)]
    permutations += [tuple(-(j+k) % 4 for j in range(4)) for k in range(4)]
    labels = ['e', 'r', 'r^2', 'r^3', 's', 'sr', 'sr^2', 'sr^3']
    nodes = re.findall(r'\\node\[font=\\tiny,text=(?:black|white)\] at \(([-.\d]+),([-.\d]+)\) \{\$(.*?)\$\};', source)
    assert len(nodes) == 64
    for x, y, value in nodes:
        column = round((float(x)-.31)/.62)
        row = round((-float(y)-.31)/.62)
        product = tuple(permutations[row][permutations[column][i]] for i in range(4))
        assert value == labels[permutations.index(product)], (row, column, value)


def check_walks():
    group = list(itertools.permutations(range(3)))
    identity = tuple(range(3))
    compose = lambda a, b: tuple(a[b[i]] for i in range(3))
    mu = {identity: Q(1, 5), (1, 0, 2): Q(2, 5),
          (1, 2, 0): Q(1, 5), (2, 0, 1): Q(1, 5)}
    laws = [{g: Q(g == identity) for g in group}]
    for t in range(13):
        nxt = dict.fromkeys(group, Q(0))
        for x, mass in laws[-1].items():
            for s, weight in mu.items():
                nxt[compose(x, s)] += mass*weight
        laws.append(nxt)
    for t in range(6):
        value = laws[2*t][identity]
        assert value == sum(x*x for x in laws[t].values())
        assert value >= Q(1, len(group))
        assert max(laws[2*t].values()) <= value
        assert laws[2*t+2][identity] <= value
        assert max(laws[2*t+1].values()) <= value
    for n in range(1, 13):
        for t in range(7):
            # Binomial enumeration and trigonometric filter use different data.
            exact = Q(sum(math.comb(2*t, j) for j in range(2*t+1)
                          if (2*j-2*t) % n == 0), 2**(2*t))
            spectral = sum(math.cos(2*math.pi*k/n)**(2*t) for k in range(n))/n
            assert abs(float(exact)-spectral) < 1e-13


if __name__ == '__main__':
    check_tools_context((ROOT/'volume3-symmetry/chapters/ch01-groups.tex').read_text())
    check_matrices()
    check_d4_plate()
    check_walks()
    print('PASS: Chapter 1 local-tool contexts; 4 matrix enumerations; all 64 D4 cells; noncommutative walk and cycle boundaries')
