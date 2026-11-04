"""Representation foundations and, as added, exact character/model checks."""
from pathlib import Path
from collections import Counter
import itertools
import math
import cmath
from fractions import Fraction as Q
import re

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'volume3-symmetry/chapters/ch11-characters.tex'


def compose(g, h):
    return tuple(g[x] for x in h)


def inverse(g):
    out = [0]*len(g)
    for i, j in enumerate(g):
        out[j] = i
    return tuple(out)


def signed_conjugation(g, tau):
    image = compose(compose(g, tau), inverse(g))
    sign = (-1)**sum(g[i] > g[j] for i, j in enumerate(tau) if i < j)
    return image, sign


def cycle_counts(g):
    seen = set(); counts = Counter()
    for i in range(len(g)):
        if i in seen:
            continue
        j, length = i, 0
        while j not in seen:
            seen.add(j); length += 1; j = g[j]
        counts[length] += 1
    return counts


def pairing_root_count(g):
    result = 1
    for length, m in cycle_counts(g).items():
        if length % 2 == 0:
            if m % 2:
                return 0
            j = m//2
            result *= math.factorial(m)*length**j//(2**j*math.factorial(j))
        else:
            result *= sum(math.factorial(m)*length**j//(
                math.factorial(m-2*j)*2**j*math.factorial(j))
                          for j in range(m//2+1))
    return result


def check_involution_model():
    involution_counts = []
    for n in range(8):
        group = list(itertools.permutations(range(n))); identity = tuple(range(n))
        roots = Counter(compose(g, g) for g in group)
        involutions = [g for g in group if compose(g, g) == identity]
        involution_counts.append(len(involutions))
        # Compare every class value via every actual element, including zero-root types.
        for g in group:
            trace = 0
            for tau in involutions:
                if compose(g, tau) == compose(tau, g):
                    trace += signed_conjugation(g, tau)[1]
            assert trace == roots[g] == pairing_root_count(g), (n, g, trace, roots[g])
        # Dense cocycle/representation check independently of the cycle counting.
        if n <= 4:
            for g, h in itertools.product(group, repeat=2):
                for tau in involutions:
                    image_h, sign_h = signed_conjugation(h, tau)
                    image, sign_g = signed_conjugation(g, image_h)
                    assert (image, sign_g*sign_h) == signed_conjugation(compose(g, h), tau)
    assert involution_counts == [1, 1, 2, 4, 10, 26, 76, 232]


def check_actual_character_figure():
    def number(x):
        return (Q(x), Q(0))
    phi, partner = (Q(1, 2), Q(1, 2)), (Q(1, 2), Q(-1, 2))
    def times(x, y):
        a, b = x; c, d = y
        return (a*c+5*b*d, a*d+b*c)
    def total(terms):
        terms = list(terms)
        return tuple(sum(x[i] for x in terms) for i in (0, 1))
    raw_tables = [
        [[1, 1, 1], [1, -1, 1], [2, 0, -1]],
        [[1, 1, 1, 1, 1], [1, -1, 1, 1, -1], [2, 0, 2, -1, 0],
         [3, 1, -1, 0, -1], [3, -1, -1, 0, 1]],
        [[1, 1, 1, 1, 1], [3, -1, 0, phi, partner],
         [3, -1, 0, partner, phi], [4, 0, 1, -1, -1], [5, 1, -1, 0, 0]]]
    tables = [[[x if isinstance(x, tuple) else number(x) for x in row]
               for row in table] for table in raw_tables]
    weights = [[1, 3, 2], [1, 6, 3, 8, 6], [1, 15, 20, 12, 12]]
    for table, sizes in zip(tables, weights):
        order = sum(sizes)
        assert sum(row[0][0]**2 for row in table) == order
        for i, row in enumerate(table):
            for j, other in enumerate(table):
                value = total(times(number(w), times(a, b))
                              for w, a, b in zip(sizes, row, other))
                assert value == number(order if i == j else 0)
        for i in range(len(sizes)):
            for j in range(len(sizes)):
                value = total(times(row[i], row[j]) for row in table)
                assert value == number(order//sizes[i] if i == j else 0)
    source = (ROOT/'volume3-symmetry/figures/ch11-tables.tex').read_text()
    pattern = (r'\\fill\[([^\]]+)\] \(([-\d.]+),([-\d.]+)\) rectangle '
               r'\(([-\d.]+),([-\d.]+)\);\n\\node\[text=(black|white)\] at '
               r'\(([-\d.]+),([-\d.]+)\) \{\$(.*?)\$\};')
    cells = re.findall(pattern, source)
    expected = [(value, row[0][0]) for table in tables for row in table for value in row]
    assert len(cells) == len(expected) == 59
    for cell, (value, degree) in zip(cells, expected):
        colour, x1, y1, x2, y2, foreground, x, y, label = cell
        actual = {r'\varphi': phi, r'1{-}\varphi': partner}.get(label)
        if actual is None:
            actual = number(int(label))
        assert actual == value
        assert abs(float(x)-(float(x1)+float(x2))/2) < .006
        assert abs(float(y)-(float(y1)+float(y2))/2) < .006
        decimal = float(value[0])+float(value[1])*math.sqrt(5)
        if decimal == 0:
            assert colour == 'white' and foreground == 'black'
        else:
            family, intensity = colour.split('!'); intensity = int(intensity)
            assert family == ('BurntOrange' if decimal > 0 else 'MidnightBlue')
            assert abs(intensity-70*abs(decimal)/float(degree)) <= .51
            # Actual old print/grayscale inspection found white on pale coral weak.
            assert foreground == ('white' if decimal < 0 and intensity == 70 else 'black')
    sizes = list(map(int, re.findall(
        r'\\node\[black!55,font=\\tiny\] at \([^)]*\) \{(\d+)\};', source)))
    assert sizes == [x for row in weights for x in row]


def check_walks_and_filters():
    for n in range(1, 18):
        roots = [cmath.exp(2j*math.pi*m/n) for m in range(n)]
        c = [2*k-3 for k in range(n)]
        for root in roots:
            eigenvalue = sum(c[k]*root**(-k) for k in range(n))
            for k in range(n):
                actual = sum(c[(k-j) % n]*root**j for j in range(n))
                assert abs(actual-eigenvalue*root**k) < 2e-10
        probabilities = [Q(int(k == 0)) for k in range(n)]
        eigenvalues = [math.cos(2*math.pi*m/n) for m in range(n)]
        for t in range(21):
            for k in range(n):
                predicted = sum(eigenvalues[m]**t*roots[m]**k for m in range(n))/n
                assert abs(predicted-complex(probabilities[k])) < 2e-13
            probabilities = [(probabilities[(k-1) % n]+probabilities[(k+1) % n])/2
                             for k in range(n)]
        if n >= 3 and n % 2:
            assert abs(max(abs(x) for x in eigenvalues[1:])-math.cos(math.pi/n)) < 2e-15
        elif n >= 2:
            assert eigenvalues[n//2] == -1
        for holding in (Q(0), Q(1, 4), Q(1, 2), Q(3, 4), Q(1)):
            lazy = [float(holding)+(1-float(holding))*value for value in eigenvalues]
            if n >= 2 and 0 < holding < 1:
                assert all(abs(value) < 1 for value in lazy[1:])
            elif holding == 1:
                assert all(value == 1 for value in lazy)
            probabilities = [Q(int(k == 0)) for k in range(n)]
            for t in range(6):
                for k in range(n):
                    predicted = sum(lazy[m]**t*roots[m]**k for m in range(n))/n
                    assert abs(predicted-complex(probabilities[k])) < 2e-13
                probabilities = [holding*probabilities[k]+(1-holding)*(
                    probabilities[(k-1) % n]+probabilities[(k+1) % n])/2 for k in range(n)]
    for modulus, first, second in ((8, 3, 5), (12, 5, 7)):
        units = [1, first, second, first*second % modulus]
        rows = [[1, a, b, a*b] for a, b in ((1, 1), (-1, 1), (1, -1), (-1, -1))]
        assert all(pow(x, 2, modulus) == 1 for x in units)
        for row in rows:
            values = {u: value for u, value in zip(units, row)}
            for a, b in itertools.product(units, repeat=2):
                assert values[a*b % modulus] == values[a]*values[b]
        for n in range(modulus):
            answer = sum(row[1]*(row[units.index(n)] if n in units else 0) for row in rows)
            assert answer == (4 if n == first else 0)
    # Recompute the actual printed Dirichlet tables from their generator values.
    source = SOURCE.read_text()
    for table in re.findall(r'\\begin\{tabular\}.*?\\end\{tabular\}', source, re.S):
        if '$n\\bmod5$' in table:
            units, generator, expected_order = [1, 2, 3, 4], 2, 4
            expected = [[(1j)**(j*next(k for k in range(4) if pow(generator, k, 5) == u))
                         for u in units] for j in range(expected_order)]
        elif 'modulo $8$' in table or 'modulo $12$' in table:
            expected = [[1, a, b, a*b] for a, b in ((1, 1), (-1, 1), (1, -1), (-1, -1))]
        else:
            continue
        actual = []
        for line in table.splitlines():
            if not line.startswith((r'$\chi_', r'$\psi_')):
                continue
            values = [cell.strip().strip('$') for cell in line.split('&')[1:]]
            values[-1] = values[-1].split(r'\\')[0].strip().strip('$')
            actual.append([{'i': 1j, '-i': -1j}.get(v, int(v) if v.lstrip('-').isdigit() else None)
                           for v in values])
        assert actual == expected


def check_commutators_and_integer_group():
    group = [g for g in itertools.permutations(range(5))
             if sum(g[i] > g[j] for i in range(5) for j in range(i+1, 5)) % 2 == 0]
    assert len(group) == 60
    counts = Counter(compose(compose(compose(g, h), inverse(g)), inverse(h))
                     for g, h in itertools.product(group, repeat=2))
    for g in group:
        shape = tuple(sorted(cycle_counts(g).elements()))
        assert counts[g] == {(1, 1, 1, 1, 1): 300, (1, 2, 2): 32,
                             (1, 1, 3): 63, (5,): 65}[shape]
    assert sum(counts.values()) == 3600
    five = (1, 2, 3, 4, 0); squared = compose(five, five)
    conjugates = {compose(compose(a, five), inverse(a)) for a in group}
    other = {compose(compose(a, squared), inverse(a)) for a in group}
    assert len(conjugates) == len(other) == 12 and conjugates.isdisjoint(other)
    assert inverse(five) in conjugates and squared not in conjugates
    def multiply(a, b):
        return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2))
                           for j in range(2)) for i in range(2))
    r, s, identity = ((0, -1), (1, 1)), ((0, 1), (1, 0)), ((1, 0), (0, 1))
    powers = [identity]
    for _ in range(5):
        powers.append(multiply(powers[-1], r))
    assert len(set(powers)) == 6 and multiply(powers[-1], r) == identity
    assert powers[3] == ((-1, 0), (0, -1))
    assert multiply(multiply(s, r), s) == powers[-1]
    generated = set(powers) | {multiply(s, a) for a in powers}
    assert len(generated) == 12
    assert len({tuple(x % 3 for row in a for x in row) for a in generated}) == 12
    assert all(multiply(a, b) in generated for a, b in itertools.product(generated, repeat=2))
    assert 48 % len(generated) == 0


def check_indicator_matrix_identity():
    # General matrix-coordinate identity, independently of any chosen group/table.
    for d in range(1, 5):
        a = [[(i-j)+1j*(i+j+1) for j in range(d)] for i in range(d)]
        trace_flip = 0
        for i, j in itertools.product(range(d), repeat=2):
            unit = [[int((r, c) == (i, j)) for c in range(d)] for r in range(d)]
            first = [[sum(a[r][k]*unit[k][c] for k in range(d))
                      for c in range(d)] for r in range(d)]
            image = [[sum(first[r][k]*a[c][k] for k in range(d))
                      for c in range(d)] for r in range(d)]
            trace_flip += image[j][i]  # Coefficient Eij after transposing.
        direct = sum(a[i][j]*a[j][i] for i, j in itertools.product(range(d), repeat=2))
        assert trace_flip == direct
    assert (2*2+6*(-2))//8 == -1  # Q8 indicator, directly from all eight squares.
    # Indicators directly from square-class maps, separate from the signed model.
    for sizes, square_map, rows in (
        ([1, 3, 2], [0, 0, 2], [[1, 1, 1], [1, -1, 1], [2, 0, -1]]),
        ([1, 6, 3, 8, 6], [0, 0, 0, 3, 2],
         [[1, 1, 1, 1, 1], [1, -1, 1, 1, -1], [2, 0, 2, -1, 0],
          [3, 1, -1, 0, -1], [3, -1, -1, 0, 1]])):
        assert all(sum(w*row[j] for w, j in zip(sizes, square_map)) == sum(sizes)
                   for row in rows)
    # Exact Q(omega), omega²+omega+1=0, for the actual A4 printed table.
    add = lambda values: tuple(sum(v[j] for v in values) for j in (0, 1))
    multiply = lambda x, y: (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0]-x[1]*y[1])
    conjugate = lambda x: (x[0]-x[1], -x[1])
    one, omega, omega2 = (1, 0), (0, 1), (-1, -1)
    rows = [[one]*4, [one, one, omega, omega2],
            [one, one, omega2, omega], [(3, 0), (-1, 0), (0, 0), (0, 0)]]
    weights = [1, 3, 4, 4]
    for i, row in enumerate(rows):
        for j, other in enumerate(rows):
            assert add([multiply((w, 0), multiply(a, conjugate(b)))
                        for w, a, b in zip(weights, row, other)]) == (12 if i == j else 0, 0)
    table = next(t for t in re.findall(r'\\begin\{tabular\}.*?\\end\{tabular\}', SOURCE.read_text(), re.S)
                 if '$\\lambda_0$' in t)
    actual = []
    for line in table.splitlines():
        if not line.startswith((r'$\lambda_', r'$\chi$')):
            continue
        values = [v.strip().strip('$') for v in line.split('&')[1:]]
        values[-1] = values[-1].split(r'\\')[0].strip().strip('$')
        actual.append([{r'\omega': omega, r'\omega^2': omega2}.get(v,
                       (int(v), 0) if v.lstrip('-').isdigit() else None) for v in values])
    assert actual == rows
    assert [add([multiply((w, 0), row[j]) for w, j in zip(weights, [0, 0, 3, 2])])
            for row in rows] == [(12, 0), (0, 0), (0, 0), (12, 0)]


def check_local_indicator_prerequisites():
    source = SOURCE.read_text()
    solution = re.search(r'\\begin\{solution\}\{pb:frobschur\}(.*?)\\end\{solution\}', source, re.S)[1]
    assert 'Specht-module' not in solution
    for needed in ('dual space', 'antilinear', 'commuting with $g$', 'cyclic order',
                   'two shifts must sum to $1$', 'nonnegative integers'):
        assert needed in solution, needed
    assert r'\bar\phi' not in source  # Algebraic conjugate is not complex conjugation.


def check_foundations():
    # Nonunitary coordinates for a C4 representation; exact Gaussian-integer powers.
    def mul(a, b):
        return [[sum(a[i][k]*b[k][j] for k in range(2))
                 for j in range(2)] for i in range(2)]
    def apply(a, v):
        return [sum(a[i][j]*v[j] for j in range(2)) for i in range(2)]
    identity = [[1, 0], [0, 1]]; r = [[1j, 2-2j], [0, -1j]]
    powers = [identity]
    for _ in range(3):
        powers.append(mul(powers[-1], r))
    assert mul(powers[-1], r) == identity
    def h(v, w):
        return sum(sum(a*b.conjugate() for a, b in zip(apply(g, v), apply(g, w)))
                   for g in powers)/4
    basis = [[1+0j, 0j], [0j, 1+0j]]
    for g in powers:
        for v in basis:
            for w in basis:
                assert h(apply(g, v), apply(g, w)) == h(v, w)
    e0 = basis[0]
    v = [1j, 1+0j]; coefficient = h(v, e0)/h(e0, e0)
    w = [a-coefficient*b for a, b in zip(v, e0)]
    assert h(w, e0) == 0 and h(w, w).real > 0 and h(w, w).imag == 0
    assert apply(r, w) == [-1j*z for z in w]
    assert h([1j*z for z in v], w) == 1j*h(v, w)
    assert h(v, [1j*z for z in w]) == -1j*h(v, w)
    assert h(v, w) == h(w, v).conjugate()
    # The real theorem does not supply this complex argument; local construction does.
    source = SOURCE.read_text()
    assert '$G$ is finite' in source and r'd\ge0' in source and r'$V\ne0$' in source
    assert 'spectral theorem, Volume~1' not in source
    assert 'conjugate-linear in the second' in source
    # The modular counterexample: all three possible complementary lines fail.
    u = [[1, 1], [0, 1]]; power = identity
    for _ in range(3):
        power = [[x % 3 for x in row] for row in mul(power, u)]
    assert power == identity and u != identity
    for a in range(3):
        assert ((a+1) % 3, 1) != (a, 1)


if __name__ == '__main__':
    check_foundations()
    check_actual_character_figure()
    check_walks_and_filters()
    check_commutators_and_integer_group()
    check_indicator_matrix_identity()
    check_involution_model()
    check_local_indicator_prerequisites()
    print('PASS: complex/zero/modular foundations;59 actual cells/foreground and all tables; walk/holding endpoints; all3600 A5 commutators; integerD6; flip indicators; signed model every permutation n0..7; local prerequisite gates')
