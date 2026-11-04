"""Exact finite-field, coding, trace and actual figure probes; not general proofs."""
import itertools
import math
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]


def poly_mul(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        a <<= 1
        b >>= 1
    return out


def rem(a, modulus):
    while a.bit_length() >= modulus.bit_length():
        a ^= modulus << (a.bit_length() - modulus.bit_length())
    return a


def power(a, n, modulus):
    result = 1
    while n:
        if n & 1:
            result = rem(poly_mul(result, a), modulus)
        a = rem(poly_mul(a, a), modulus)
        n >>= 1
    return result


def irreducible(f):
    # Independent trial division, including repeated factors.
    n = f.bit_length() - 1
    return n >= 1 and all(rem(f, d) for k in range(1, n // 2 + 1)
                          for d in range(1 << k, 1 << (k + 1)))


def count_irreducibles(n):
    # Degree recurrence, separately from trial division and Mobius inversion.
    counts = {}
    for k in range(1, n + 1):
        counts[k] = ((1 << k) - sum(d * counts[d] for d in counts if k % d == 0)) // k
    return counts


def check_fields_and_aes():
    lists = {n: [f for f in range(1 << n, 1 << (n + 1)) if irreducible(f)]
             for n in range(1, 5)}
    assert lists == {1: [2, 3], 2: [7], 3: [11, 13], 4: [19, 25, 31]}
    assert {n: len(v) for n, v in lists.items()} == count_irreducibles(4)
    product = 1
    for n in (1, 2, 4):
        for f in lists[n]:
            product = poly_mul(product, f)
    assert product == (1 << 16) ^ 2
    assert [[a ^ b for b in range(4)] for a in range(4)] == [
        [0, 1, 2, 3], [1, 0, 3, 2], [2, 3, 0, 1], [3, 2, 1, 0]]
    assert [[rem(poly_mul(a, b), 7) for b in range(4)] for a in range(4)] == [
        [0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 3, 1], [0, 3, 1, 2]]
    for f, order in ((19, 15), (25, 15), (31, 5)):
        assert next(k for k in range(1, 16) if power(2, k, f) == 1) == order
    m, r = 0x11b, 0x5c
    assert irreducible(m)  # Trial factors, independent of the reader certificate.
    assert power(2, 16, m) ^ 2 == r and power(2, 256, m) == 2
    assert poly_mul(0x13, m) ^ poly_mul(0x51, r) == 1
    assert rem(poly_mul(0x57, 0x13), m) == 0xfe  # NIST section4.3 example.
    # Independently check all three quadratic examples over F3.
    quadratics = [(a, b) for a in range(3) for b in range(3)
                  if all((x*x + a*x + b) % 3 for x in range(3))]
    assert quadratics == [(0, 1), (1, 2), (2, 2)]
    def mul9(a, b):
        u, v = a % 3, a // 3; x, y = b % 3, b // 3
        return (u*x + v*y) % 3 + 3*((u*y + v*x + 2*v*y) % 3)
    assert mul9(5, 5) == mul9(7, 7) == 2  # alpha+2 and 2alpha+1.
    for p in (2, 3, 5, 7):
        for k in range(0, 2*p + 1):
            assert sum(pow(x, k, p) for x in range(p)) % p == (
                p-1 if k > 0 and k % (p-1) == 0 else 0)
        assert { (x*x + y*y) % p for x in range(p) for y in range(p)} == set(range(p))
        # All diagonal ternary quadratics, including zero and characteristic2.
        for a, b, c in itertools.product(range(p), repeat=3):
            zeros = sum((a*x*x+b*y*y+c*z*z) % p == 0
                        for x, y, z in itertools.product(range(p), repeat=3))
            assert zeros % p == 0 and zeros >= p


def check_actual_figures():
    source = (ROOT / 'volume3-symmetry/figures/ch09-f16.tex').read_text()
    labels = re.findall(r'alpha\^\{(\d+)\}.*?scriptscriptstyle ([01]{4})', source)
    assert len(labels) == 15
    for k, bits in labels:
        assert int(bits, 2) == power(2, int(k), 19)
    points = [tuple(map(float, p)) for p in re.findall(
        r'\\fill\[MidnightBlue\] \(([-\d.]+),([-\d.]+)\)', source)]
    assert len(points) == 29
    for k, (x, y) in enumerate(points[:15]):
        assert abs(x - 2 * math.sin(2 * math.pi * k / 15)) < .0006
        assert abs(y - 2 * math.cos(2 * math.pi * k / 15)) < .0006
    counts = count_irreducibles(14)
    for n, (x, y) in enumerate(points[15:], 1):
        assert abs(x - (3.45 + .3 * n)) < .0006
        assert abs(y - (-2.1 + 3.85 / 3 * math.log10(counts[n]))) < .0006
    curve = re.search(r'plot coordinates \{(.*?)\};', source)[1]
    pts = [tuple(map(float, p)) for p in re.findall(r'\(([-\d.]+),([-\d.]+)\)', curve)]
    assert len(pts) == 131
    for j, (x, y) in enumerate(pts):
        n = 1 + j / 10
        assert abs(x - (3.45 + .3 * n)) < .0006
        assert abs(y - (-2.1 + 3.85 / 3 * math.log10(2**n / n))) < .0006
    pascal = (ROOT / 'volume3-symmetry/figures/ch01-pascal.tex').read_text()
    actual = [tuple(map(float, p)) for p in re.findall(
        r'\\fill\[MidnightBlue\] \(([-\d.]+),([-\d.]+)\)', pascal)]
    expected = [(j - n / 2, round(-math.sqrt(3) / 2 * n, 1))
                for n in range(32) for j in range(n + 1) if math.comb(n, j) % 2]
    assert actual == expected and len(actual) == 3**5


def gauss_solve(rows, p):
    rows = [[x % p for x in row] for row in rows]
    pivots = []; k = 0
    for col in range(len(rows[0]) - 1):
        pivot = next((i for i in range(k, len(rows)) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[k], rows[pivot] = rows[pivot], rows[k]
        u = pow(rows[k][col], -1, p)
        rows[k] = [x * u % p for x in rows[k]]
        for i in range(len(rows)):
            if i != k:
                u = rows[i][col]
                rows[i] = [(x - u * y) % p for x, y in zip(rows[i], rows[k])]
        pivots.append(col); k += 1
        if k == len(rows):
            break
    assert all(any(row[:-1]) or not row[-1] for row in rows)
    result = [0] * (len(rows[0]) - 1)
    for i, j in enumerate(pivots):
        result[j] = rows[i][-1]
    return result, len(pivots)


def check_codes():
    y = [5, 3, 2, 4, 0, 1]
    rows = [[-v, -v * j, 1, j, j*j, j**3, v * j*j]
            for j, v in enumerate(y, 1)]
    coeffs, rank = gauss_solve(rows, 7)
    assert coeffs == [3, 0, 2, 6, 3, 2] and rank == 6
    messages = [[(a + b * j) % 7 for j in range(1, 7)]
                for a in range(7) for b in range(7)]
    distances = [sum(a != b for a, b in zip(word, y)) for word in messages]
    assert min(distances) == 2 and distances.count(2) == 1
    f = [(3 + 2 * j) % 7 for j in range(1, 7)]
    e = [(j*j + 3) % 7 for j in range(1, 7)]
    q = [(2*j**3 + 3*j*j + 6*j + 2) % 7 for j in range(1, 7)]
    assert e == [4, 0, 5, 5, 0, 4] and q == [6, 0, 3, 6, 0, 4]
    assert all(a == b*c % 7 for a, b, c in zip(q, y, e))
    # No-error case: E is not unique, but Q/E always recovers f.
    rows = [[-v, -v * j, 1, j, j*j, j**3, v * j*j]
            for j, v in enumerate(f, 1)]
    assert gauss_solve(rows, 7)[1] == 4  # Two free locator coefficients.
    # k=n gives t=0 and interpolation, including the one-symbol endpoint.
    for p, n in ((2, 1), (3, 3), (5, 4)):
        for a in range(p):
            rows = [[pow(j, k, p) for k in range(n)] + [a] for j in range(n)]
            assert gauss_solve(rows, p) == ([a] + [0] * (n - 1), n)


def check_recurrences_and_trace():
    def prime(n):
        return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))
    for p in (3, 5, 7, 11, 13, 17, 19, 23, 31):
        m = (1 << p) - 1; s = 4
        for _ in range(p - 2):
            s = (s*s - 2) % m
        assert (s == 0) == prime(m)
    for p in (3, 7, 11, 13, 17, 19, 23, 29, 31):
        a, b, period = 0, 1, 0
        while True:
            a, b = b, (a + b) % p; period += 1
            if (a, b) == (0, 1):
                break
        delta = 1 if any(x*x % p == 5 % p for x in range(p)) else -1
        assert (p - 1 if delta == 1 else 2 * (p + 1)) % period == 0
        if p in (7, 11):
            assert period == {7: 16, 11: 10}[p]
    for n in range(1, 9):
        modulus = next(f for f in range(1 << n, 1 << (n + 1)) if irreducible(f))
        size, length = 1 << n, (1 << n) - 1
        alpha = next(a for a in range(1, size)
                     if len({power(a, k, modulus) for k in range(length)}) == length)
        def trace(a):
            value = 0
            for _ in range(n):
                value ^= a; a = rem(poly_mul(a, a), modulus)
            return value
        values = [trace(a) for a in range(size)]
        assert set(values) == {0, 1} and values.count(1) == size // 2
        assert trace(1) == n % 2  # Even degrees: Tr(1)=0 but Tr is nonzero.
        s = [trace(power(alpha, k, modulus)) for k in range(length)]
        windows = {tuple(s[(k+j) % length] for j in range(n)) for k in range(length)}
        assert len(windows) == length and (0,) * n not in windows
        assert sum(s) == size // 2
        for t in range(length):
            corr = sum(1 if s[k] == s[(k+t) % length] else -1 for k in range(length))
            assert corr == (length if t == 0 else -1)


def check_moore():
    modulus = 19
    mul = lambda a, b: rem(poly_mul(a, b), modulus)
    for q, n_max in ((2, 3), (4, 2)):
        scalars = [a for a in range(16) if power(a, q, modulus) == a]
        assert len(scalars) == q
        for n in range(n_max + 1):
            for values in itertools.product(range(16), repeat=n):
                # Characteristic2: all permutation signs are +1.
                determinant = 0
                for perm in itertools.permutations(range(n)):
                    term = 1
                    for i, j in enumerate(perm):
                        term = mul(term, power(values[i], q**j, modulus))
                    determinant ^= term
                product = 1
                for i in range(n):
                    for coeffs in itertools.product(scalars, repeat=i):
                        term = values[i]
                        for c, x in zip(coeffs, values):
                            term ^= mul(c, x)
                        product = mul(product, term)
                assert determinant == product
                dependent = any(not _linear_sum(cs, values, mul)
                                for cs in itertools.product(scalars, repeat=n) if any(cs))
                assert bool(determinant) == (not dependent)
    # Odd-characteristic determinant sign, with independent pairs in F9/F3.
    def add9(a, b):
        return (a % 3 + b % 3) % 3 + 3*((a // 3 + b // 3) % 3)
    def scale9(c, a):
        return c*(a % 3) % 3 + 3*((c*(a // 3)) % 3)
    def mul9(a, b):
        u, v = a % 3, a // 3; x, y = b % 3, b // 3
        return (u*x + v*y) % 3 + 3*((u*y + v*x + 2*v*y) % 3)
    nonzero = 0
    for x, y in itertools.product(range(9), repeat=2):
        x3, y3 = mul9(mul9(x, x), x), mul9(mul9(y, y), y)
        determinant = add9(mul9(x, y3), scale9(2, mul9(y, x3)))
        product = x
        for c in range(3):
            product = mul9(product, add9(y, scale9(c, x)))
        assert determinant == product
        nonzero += determinant != 0
    assert nonzero == (9-1)*(9-3)


def _linear_sum(coeffs, values, mul):
    total = 0
    for c, x in zip(coeffs, values):
        total ^= mul(c, x)
    return total


if __name__ == '__main__':
    check_fields_and_aes()
    check_actual_figures()
    check_codes()
    check_recurrences_and_trace()
    check_moore()
    print('PASS: finite fields/AES; all F16/Pascal coordinates; exact decoding; Lucas-Lehmer/Fibonacci; trace/windows/correlation n1..8; Moore q2/4')
