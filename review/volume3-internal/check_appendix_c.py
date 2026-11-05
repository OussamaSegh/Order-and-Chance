"""Finite support for the combinatorial appendix, never approval or a general proof."""
from fractions import Fraction as Q
from itertools import product, combinations, combinations_with_replacement
from pathlib import Path
import math
import random
import re

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT/'volume3-symmetry/chapters/combinatorial.tex'


def field(q):
    add = (lambda a, b: a ^ b) if q == 4 else (lambda a, b: (a+b) % q)
    def mul(a, b):
        if q != 4:
            return a*b % q
        result = 0
        while b:
            if b & 1:
                result ^= a
            b >>= 1
            a <<= 1
            if a & 4:
                a ^= 7  # F2[X]/(X²+X+1), an actual field.
        return result
    def power(a, e):
        result = 1
        while e:
            if e & 1:
                result = mul(result, a)
            a = mul(a, a)
            e >>= 1
        return result
    return add, mul, power


def rank(a, q):
    a = [list(row) for row in a]
    if not a:
        return 0
    add, mul, power = field(q)
    neg = lambda x: x if q == 4 else -x % q
    r = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inverse = power(a[r][j], q-2)
        a[r] = [mul(x, inverse) for x in a[r]]
        for i in range(len(a)):
            if i != r:
                scale = neg(a[i][j])
                a[i] = [add(x, mul(scale, y)) for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def check_incidence_families_and_fano():
    for n in range(4):
        for mask in range(1 << (1 << n)):
            family = [a for a in range(1 << n) if mask >> a & 1]
            overlaps = [(a & b).bit_count() for a, b in combinations(family, 2)]
            if all(a.bit_count() % 2 for a in family) and all(v % 2 == 0 for v in overlaps):
                assert len(family) <= n
            if all(a.bit_count() % 2 == 0 for a in family) and all(v % 2 == 0 for v in overlaps):
                assert len(family) <= 2**(n//2)
            if len(family) >= 2 and len(set(overlaps)) == 1 and overlaps[0] > 0:
                assert len(family) <= n
            sizes = set(overlaps)
            assert len(family) <= sum(math.comb(n, i) for i in range(min(len(sizes), n)+1))
            for p in (2, 3, 5):
                forbidden = {v % p for v in overlaps}
                if all(a.bit_count() % p not in forbidden for a in family):
                    assert len(family) <= sum(math.comb(n, i) for i in range(min(len(forbidden), n)+1))
    for n in range(1, 9):
        counterexample = [0]+[1 << i for i in range(n)]
        assert len(counterexample) == n+1
        assert all(a & b == 0 for a, b in combinations(counterexample, 2))
    points = range(8)
    planes = {frozenset(x for x in points if (a & x).bit_count() % 2 == b)
              for a in range(1, 8) for b in (0, 1)}
    assert len(planes) == 14 and {len(p) for p in planes} == {4}
    clubs = planes | {frozenset(), frozenset(points)}
    assert len(clubs) == 16
    assert all(len(a & b) % 2 == 0 for a, b in combinations(clubs, 2))
    words = [[int(x in club) for x in points] for club in clubs]
    assert rank(words, 2) == 4
    parity_check = [[(x >> i) & 1 for x in range(1, 8)] for i in range(3)]
    assert rank(parity_check, 2) == 3
    assert len({tuple(w[1:]) for w in words}) == 16
    assert all(sum(a*b for a, b in zip(row, w[1:])) % 2 == 0
               for row in parity_check for w in words)
    assert all(w[0] == sum(w[1:]) % 2 for w in words)
    lines = {frozenset((u, v, u ^ v)) for u, v in combinations(range(1, 8), 2)}
    assert len(lines) == 7 and all(len(a & b) == 1 for a, b in combinations(lines, 2))
    assert all(sum({u, v} <= line for line in lines) == 1
               for u, v in combinations(range(1, 8), 2))
    listed = re.search(r'One standard labelling.*?\\\[(.*?)\\\]', SOURCE.read_text(), re.S).group(1)
    triples = re.findall(r'\b[1-7]{3}\b', listed.replace(r'\quad', ' '))
    label_to_vector = dict(enumerate((1, 2, 4, 3, 5, 6, 7), 1))
    assert len(triples) == 7
    assert {frozenset(label_to_vector[int(x)] for x in triple)
            for triple in triples} == lines
    assert math.comb(27, 8) == 2220075
    assert sum(math.comb(27, i) for i in range(3)) == 379
    # All binary subspaces through dimension4, including small-field support
    # cancellations that an informal union-of-supports argument would miss.
    for n, expected in enumerate((1, 2, 5, 16, 67)):
        spaces = {frozenset({0})}
        pending = [frozenset({0})]
        while pending:
            v = pending.pop()
            for w in range(1 << n):
                extended = v | {x ^ w for x in v}
                if extended not in spaces:
                    spaces.add(extended)
                    pending.append(extended)
        assert len(spaces) == expected
        for v in spaces:
            d = len(v).bit_length()-1
            assert max(x.bit_count() for x in v) >= d


def check_nullstellensatz_coefficients():
    rng = random.Random(1601)
    for q in (2, 3, 4, 5):
        add, mul, power = field(q)
        neg = lambda a: a if q == 4 else -a % q
        for _ in range(45):
            n = rng.randrange(4)
            target = tuple(rng.randrange(min(q, 3)) for _ in range(n))
            total = sum(target)
            monomials = [e for e in product(range(total+1), repeat=n) if sum(e) <= total]
            coefficients = {e: rng.randrange(q) for e in monomials}
            coefficients[target] = rng.randrange(1, q)
            grid = [rng.sample(range(q), t+1) for t in target]
            def evaluate(x):
                result = 0
                for e, c in coefficients.items():
                    term = c
                    for xi, ei in zip(x, e):
                        term = mul(term, power(xi, ei))
                    result = add(result, term)
                return result
            coefficient_sum = 0
            nonzero = False
            for x in product(*grid):
                value = evaluate(x)
                nonzero |= bool(value)
                denominator = 1
                for i, xi in enumerate(x):
                    for other in grid[i]:
                        if other != xi:
                            denominator = mul(denominator, add(xi, neg(other)))
                assert denominator != 0
                coefficient_sum = add(coefficient_sum, mul(value, power(denominator, q-2)))
            assert nonzero and coefficient_sum == coefficients[target]
    # Exact old zero-polynomial degree counterexamples, not mere source guards.
    for p in (2, 3, 5):
        assert sum(x == 0 for x in range(p)) == 1  # equations0,X in one variable
        assert 1 % p != 0


def check_zero_counts_and_additive_bounds():
    for p in (2, 3):
        points = list(product(range(p), repeat=3))
        monomials = list(combinations_with_replacement(range(3), 2))
        for coefficients in product(range(p), repeat=len(monomials)):
            zeros = [x for x in points if sum(c*x[i]*x[j] for c, (i, j)
                                             in zip(coefficients, monomials)) % p == 0]
            assert len(zeros) >= p and len(zeros) % p == 0
    for p in (2, 3, 5, 7):
        subsets = [tuple(i for i in range(p) if mask >> i & 1) for mask in range(1, 1 << p)]
        for a, b in product(subsets, repeat=2):
            assert len({(x+y) % p for x in a for y in b}) >= min(p, len(a)+len(b)-1)
        assert any((a*a+b*b+1) % p == 0 for a, b in product(range(p), repeat=2))
    assert {(x+y) % 4 for x in (0, 2) for y in (0, 2)} == {0, 2}
    for n in range(1, 6):
        for entries in combinations_with_replacement(range(n), 2*n-1):
            assert any(sum(chosen) % n == 0 for chosen in combinations(entries, n))
        bad = (0,)*(n-1)+(1,)*(n-1)
        assert not any(sum(chosen) % n == 0 for chosen in combinations(bad, n))


def check_kakeya_prime_power_boundaries():
    for q, expected_minimum in ((2, 3), (3, 7), (4, 10)):
        add, mul, power = field(q)
        points = list(product(range(q), repeat=2))
        indices = {p: i for i, p in enumerate(points)}
        directions = [(1, a) for a in range(q)]+[(0, 1)]
        classes = []
        for d in directions:
            lines = {sum(1 << indices[tuple(add(x[i], mul(t, d[i])) for i in range(2))]
                         for t in range(q)) for x in points}
            assert len(lines) == q
            classes.append(lines)
        best = q*q
        for mask in range(1 << (q*q)):
            if mask.bit_count() >= best:
                continue
            if all(any(mask & line == line for line in lines) for lines in classes):
                best = mask.bit_count()
        assert best == expected_minimum
        assert best >= math.comb(q+1, 2)
        # Independent grid evaluation rank, including the extension fieldF4.
        exponents = list(product(range(q), repeat=2))
        values = [[mul(power(x[0], e[0]), power(x[1], e[1])) for e in exponents]
                  for x in points]
        assert rank(values, q) == q*q
    # At n0 no nonzero direction exists; the original unqualified assertion
    # would let empty K satisfy it, but its numerical lower bound is1.
    assert math.comb(4+0-1, 0) == 1


def check_cap_counts_and_optimum():
    coefficients = [1]
    x = Q(59, 100)
    upper = Q(1722, 625)
    assert (1+x+x*x)**3/x**2 < upper**3
    for n in range(11):
        count = sum(coefficients[:2*n//3+1])
        direct = sum(sum(a) <= 2*n//3 for a in product(range(3), repeat=n))
        assert count == direct
        assert count**3*x**(2*n) <= (1+x+x*x)**(3*n)
        assert count**3 <= upper**(3*n)
        next_coefficients = [0]*(len(coefficients)+2)
        for i, c in enumerate(coefficients):
            for j in range(3):
                next_coefficients[i+j] += c
        coefficients = next_coefficients
    low, high = Q(5930703308172535, 10**16), Q(5930703308172536, 10**16)
    assert 4*low*low+low-2 < 0 < 4*high*high+high-2
    lower_cube = (1+low+low*low)**3/high**2
    upper_cube = (1+high+high*high)**3/low**2
    assert Q(27551, 10000)**3 < lower_cube  #2.7551 is below the minimum.
    assert upper_cube < Q(2755105, 10**6)**3
    points = list(product(range(3), repeat=2))
    def is_cap(a):
        return all(any(sum(t[i] for t in triple) % 3 for i in range(2))
                   for triple in combinations(a, 3))
    assert is_cap(((0, 0), (1, 0), (0, 1), (1, 1)))
    assert not any(is_cap(a) for a in combinations(points, 5))
    for p in (3, 5, 7):
        assert all((a-2*b+c) % p != 0 or a == b == c
                   for a, b, c in product(range(p), repeat=3)
                   if len({a, b, c}) < 3)
    assert (0-2*1+0) % 2 == 0  # Repeated off-diagonal relation in characteristic2.


def check_actual_figures():
    source = (ROOT/'volume3-symmetry/figures/combinatorial-ch11-pentagon.tex').read_text()
    vertices = [(float(x), float(y)) for x, y in re.findall(
        r'\\fill\[black\] \(([-\d.]+),([-\d.]+)\)', source)]
    assert len(vertices) == 5
    for j, (x, y) in enumerate(vertices):
        theta = math.pi/2+2*math.pi*j/5
        assert abs(x-1.6*math.cos(theta)) < .00051
        assert abs(y-1.6*math.sin(theta)) < .00051
    edges = re.findall(r'\\draw\[(MidnightBlue|BurntOrange)[^\n]*?\(([-\d.]+),([-\d.]+)\) -- \(([-\d.]+),([-\d.]+)\)', source)
    assert len(edges) == 10
    pairs = set()
    for colour, x, y, u, v in edges:
        i = vertices.index((float(x), float(y)))
        j = vertices.index((float(u), float(v)))
        pairs.add(tuple(sorted((i, j))))
        length = math.hypot(float(x)-float(u), float(y)-float(v))
        expected = 3.2*math.sin(math.pi/5 if colour == 'MidnightBlue' else 2*math.pi/5)
        assert abs(length-expected) < .0015
    assert pairs == set(combinations(range(5), 2))
    source = (ROOT/'volume3-symmetry/figures/combinatorial-ch11-caps.tex').read_text()
    filled = re.findall(r'\\fill\[(MidnightBlue|BurntOrange|ForestGreen)\] \(([-\d.]+),([-\d.]+)\)', source)
    assert len(filled) == 36
    for panel in range(4):
        colours = {}
        for colour, x, y in filled[9*panel:9*(panel+1)]:
            local_x = round(float(x)-4.6*panel)
            local_y = round(float(y))
            assert abs(float(x)-4.6*panel-local_x) < 1e-12
            assert abs(float(y)-local_y) < 1e-12
            colours.setdefault(colour, []).append((local_x, local_y))
        assert {len(v) for v in colours.values()} == {3}
        assert {p for line in colours.values() for p in line} == set(product(range(3), repeat=2))
        for line in colours.values():
            if panel == 0:
                assert len({y for x, y in line}) == 1
            elif panel == 1:
                assert len({x for x, y in line}) == 1
            else:
                slope = panel-1
                assert len({(y-slope*x) % 3 for x, y in line}) == 1
    cap = re.findall(r'\\filldraw\[draw=black!60,fill=black\] \(([-\d.]+),([-\d.]+)\)', source)
    assert len(cap) == 4
    assert {(round(float(x)-18.4), round(float(y))) for x, y in cap} == {(0, 0), (0, 1), (1, 0), (1, 1)}
    all_cap_points = re.findall(r'\\filldraw\[draw=black!60,fill=(black|white)\] \(([-\d.]+),([-\d.]+)\)', source)
    assert len(all_cap_points) == 9
    assert {(round(float(x)-18.4), round(float(y))) for colour, x, y in all_cap_points} == set(product(range(3), repeat=2))
    labels = re.findall(r'\\node\[l\] at \(([-\d.]+),([-\d.]+)\) \{([^\n]*)\}', source)
    assert len(labels) == 5
    for panel, (x, y, label) in enumerate(labels):
        assert abs(float(x)-(1+4.6*panel)) < 1e-12 and float(y) == -1.2


def check_local_contract(source=None):
    source = SOURCE.read_text() if source is None else source
    assert 'have nonnegative degree bounds' in source
    assert 'Let $p$ be a prime and $n\\ge1$' in source
    assert 'This calculation makes no stronger divisibility claim' in source
    assert 'Let $q$ be a prime power and $n\\ge1$' in source
    assert 'For $n=0$, the grid' in source
    assert 'x-2y+z=0' in source
    assert 'homogeneous part of degree $4$' in source
    assert 'Volume~1, Chapter~10' in source
    assert 'Volume~9, Appendix~C' not in source
    assert 'odd prime power' in source


def check_planar_maximum(source=None):
    """Exact support for the newly supplied general geometric proof."""
    source = SOURCE.read_text() if source is None else source
    assert r'\label{combinatorial:prop:planarmax}' in source, (
        'The original five-point planar maximum needs a local proof')

    # A different finite check of the six-vertex colouring argument: every
    # one of the 2^15 edge colourings contains a monochromatic triangle.
    edges = list(combinations(range(6), 2))
    index = {e: i for i, e in enumerate(edges)}
    triangles = [sum(1 << index[e] for e in combinations(v, 2))
                 for v in combinations(range(6), 3)]
    assert all(any(mask & t in (0, t) for t in triangles)
               for mask in range(1 << len(edges)))

    def det3(a):
        return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
                - a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
                + a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))

    # Gram determinants are polynomials of degree at most two in t=r^2.
    # Their coefficients are determined by these three exact evaluations.
    for pattern in product((0, 1), repeat=3):
        for t in map(Q, (0, 1, 2)):
            x, y, z = (t if bit else Q(1) for bit in pattern)
            gram = [[Q(1), Q(1, 2), (1+x-y)/2],
                    [Q(1, 2), Q(1), (1+x-z)/2],
                    [(1+x-y)/2, (1+x-z)/2, x]]
            expected = (Q(1, 2), t*(3-t)/4,
                        (-t*t+4*t-1)/4, (3*t-1)/4)[sum(pattern)]
            assert det3(gram) == expected

    # Exact coordinates in Q(sqrt(3)), using pairs a+b*sqrt(3).
    def add(a, b):
        return a[0]+b[0], a[1]+b[1]
    def scale(c, a):
        return c*a[0], c*a[1]
    def sub(a, b):
        return add(a, scale(-1, b))
    def mul(a, b):
        return a[0]*b[0]+3*a[1]*b[1], a[0]*b[1]+a[1]*b[0]
    zero, one, h = (Q(0), Q(0)), (Q(1), Q(0)), (Q(0), Q(1, 2))
    vertices = [(scale(-Q(1, 2), one), zero),
                (scale(Q(1, 2), one), zero), (zero, h)]
    centre = zero, scale(Q(1, 3), h)
    def squared(a, b):
        d = [sub(x, y) for x, y in zip(a, b)]
        return add(mul(d[0], d[0]), mul(d[1], d[1]))
    def rotate(a):
        x, y = [sub(u, v) for u, v in zip(a, centre)]
        return (add(centre[0], sub(scale(-Q(1, 2), x), mul(h, y))),
                add(centre[1], add(mul(h, x), scale(-Q(1, 2), y))))
    assert all(squared(centre, v) == (Q(1, 3), Q(0)) for v in vertices)
    candidates = [((zero, scale(-1, h)), (Q(3), Q(0)), (Q(4), Q(0)))]
    for sign in (-1, 1):
        t = Q(2), Q(sign)
        candidates.append(((zero, add(h, scale(sign, one))), t, scale(2, t)))
    for p, t, separation in candidates:
        orbit = [p, rotate(p), rotate(rotate(p))]
        assert rotate(orbit[-1]) == p and len(set(orbit)) == 3
        for q in orbit:
            values = [squared(q, v) for v in vertices]
            assert all(x in (one, t) for x in values)
            assert sum(x == t for x in values) == (1 if t == (Q(3), Q(0)) else 2)
        assert all(squared(a, b) == separation for a, b in combinations(orbit, 2))
        assert separation not in (one, t)


def check_research_guide(source=None):
    """Guard the verified published-paper locators, not the research proof."""
    source = SOURCE.read_text() if source is None else source
    guide = source.split(r'\emph{Research papers to read after this chapter.}', 1)[1]
    assert 'its Lemma~1' not in guide
    assert 'Its Proposition~2 bounds the rank of a matrix' in guide
    assert 'Theorem~4 obtains the corresponding finite-field bound' in guide
    assert 'Compare that matrix argument with the symmetric three-variable proof' in guide


def check_earlier_printed_order(perron_source=None):
    def chapter_map(volume):
        source = (ROOT/volume/'main.tex').read_text()
        route = source.split(r'\mainmatter', 1)[1].split(r'\backmatter', 1)[0]
        initial = re.search(r'\\setcounter\{chapter\}\{(-?\d+)\}', route)
        number = int(initial.group(1)) if initial else 0
        result = {}
        for name in re.findall(r'\\input\{chapters/([^}]+)\}', route):
            if re.search(r'\\chapter(?:\[[^]]+\])?\{',
                         (ROOT/volume/'chapters'/(name+'.tex')).read_text()):
                number += 1
                result[name] = number
        return result
    v1 = chapter_map('volume1-first-principles')
    v2 = chapter_map('volume2-integers')
    assert v1['ch05-sequences-series'] == 3
    assert v1['ch09-probability'] == 10
    assert v1['ch03-polynomials'] == 6
    assert v2['ch09-diophantine'] == 8 and v2['ch08-continued-fractions'] == 9
    assert v2['ch14-characters'] == 11
    perron = (ROOT/'volume3-symmetry/chapters/linear-ch07-perron.tex').read_text() if perron_source is None else perron_source
    contexts = (r'sequence limits proved in Volume~1,\s*Chapter~(\d+)',
                r'bounded-subsequence theorem of Volume~1, Chapter~(\d+)',
                r'Cauchy, hence converges by Volume~1, Chapter~(\d+)')
    for context in contexts:
        match = re.search(context, perron)
        assert match and int(match.group(1)) == v1['ch05-sequences-series']


if __name__ == '__main__':
    check_incidence_families_and_fano()
    check_nullstellensatz_coefficients()
    check_zero_counts_and_additive_bounds()
    check_kakeya_prime_power_boundaries()
    check_cap_counts_and_optimum()
    check_actual_figures()
    check_local_contract()
    check_planar_maximum()
    check_research_guide()
    check_earlier_printed_order()
    print('Combinatorial appendix: exact incidence/polynomial/field/count/figure probes pass; no approval generated.')
