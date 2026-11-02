#!/usr/bin/env python3
"""Focused, reproducible mathematical and manuscript checks for Volume 3.

Run from repository root: python3 review/volume3-rewrite/check_volume3.py
These tests check specified examples and structural invariants. They do not
constitute a formal verification of every proof in the book.
"""
from __future__ import annotations

import itertools
import math
import re
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BOOK = ROOT / "volume3-symmetry"


def check_labels_and_figures() -> tuple[int, int, int]:
    main = (BOOK / "main.tex").read_text(encoding="utf-8")
    includes = re.findall(r"\\input\{([^}]+)\}", main)
    source_paths = [BOOK / "main.tex"]
    for item in includes:
        if item.startswith("../"):
            continue
        path = BOOK / (item if item.endswith(".tex") else item + ".tex")
        assert path.exists(), f"Missing main.tex input: {item}"
        source_paths.append(path)
    source_texts = [(p, p.read_text(encoding="utf-8")) for p in source_paths]
    labels: dict[str, str] = {}
    refs: list[tuple[str, str]] = []
    figure_count = 0
    for path, source in source_texts:
        for label in re.findall(r"\\label\{([^}]+)\}", source):
            assert label not in labels, f"Duplicate label {label}: {path} and {labels[label]}"
            labels[label] = str(path)
        for ref in re.findall(r"\\(?:ref|eqref|autoref|pageref)\{([^}]+)\}", source):
            refs.append((ref, str(path)))
        for fig in re.findall(r"\\fig\{([^}]+)\}", source):
            assert (BOOK / "figures" / f"{fig}.tex").exists(), f"Missing figure {fig} in {path}"
            figure_count += 1
        assert source.count(r"\begin{proof}") == source.count(r"\end{proof}"), f"Unbalanced proof in {path}"
        assert source.count(r"\begin{exercise}") == source.count(r"\end{exercise}"), f"Unbalanced exercise in {path}"

        # Every graded exercise has its own hint and an independently addressable
        # full solution, including a How-to-find-it idea and a Write-up.
        exercises = re.findall(
            r"\\begin\{exercise\}(?:\[[^\]]*\])?\s*\\label\{([^}]+)\}", source)
        hints = re.findall(r"\\begin\{hint\}\{([^}]+)\}", source)
        solutions = re.findall(r"\\begin\{solution\}\{([^}]+)\}", source)
        if exercises or hints or solutions:
            assert len(exercises) == len(set(exercises)), f"Duplicate exercise ids in {path}"
            assert sorted(exercises) == sorted(hints), f"Exercise/hint mismatch in {path}"
            assert sorted(exercises) == sorted(solutions), f"Exercise/solution mismatch in {path}"
            for solution in re.finditer(
                    r"\\begin\{solution\}\{([^}]+)\}([\s\S]*?)\\end\{solution\}", source):
                assert r"\idea" in solution[2] and r"\writeup" in solution[2], (
                    f"Solution without finding idea and write-up: {solution[1]} in {path}")

    for ref, path in refs:
        assert ref in labels, f"Undefined reference {ref} in {path}"
    assert r"\input{chapters/afterword}" in main
    assert main.index(r"\appendix") < main.index(r"\input{chapters/paley}")
    assert main.index(r"\input{chapters/combinatorial}") < main.index(r"\input{chapters/paley}")
    return len(labels), len(refs), figure_count


def check_necklaces() -> None:
    words = tuple(itertools.product((0, 1), repeat=6))
    canonical = {min(w[i:] + w[:i] for i in range(6)) for w in words}
    assert len(canonical) == 14
    fixed_counts = [sum(w == w[i:] + w[:i] for w in words) for i in range(6)]
    assert sum(fixed_counts) // 6 == 14
    assert fixed_counts == [64, 2, 4, 8, 4, 2]


def check_cube() -> None:
    # Every orientation-preserving signed coordinate permutation is a cube rotation.
    def sign_of(p: tuple[int, ...]) -> int:
        inversions = sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))
        return -1 if inversions % 2 else 1

    rotations = [(p, signs) for p in itertools.permutations(range(3))
                 for signs in itertools.product((-1, 1), repeat=3)
                 if sign_of(p) * math.prod(signs) == 1]
    assert len(rotations) == 24


def check_quintic() -> None:
    # Eisenstein at 2 and four exact sign checks provide the Galois proof's input.
    c = [2, -4, 0, 0, 0, 1]  # constant through leading coefficient
    assert all(a % 2 == 0 for a in c[:-1])
    assert c[-1] % 2 != 0 and c[0] % 4 != 0
    f = lambda x: x**5 - 4*x + 2
    assert [f(x) for x in (-2, 0, 1, 2)] == [-22, 2, -1, 26]
    # f' = 5x^4 - 4 has just the two real roots +/-(4/5)^(1/4).
    # Rolle's theorem therefore bounds the distinct real zeros of f by three.


def check_rs_distance() -> None:
    # All Reed-Solomon evaluations of linear polynomials over F7 at 1,...,6.
    words = [tuple((a*x + b) % 7 for x in range(1, 7))
             for a, b in itertools.product(range(7), repeat=2)]
    assert len(words) == 49 and len(set(words)) == 49
    distances = (sum(u != v for u, v in zip(w1, w2))
                 for i, w1 in enumerate(words) for w2 in words[i+1:])
    assert min(distances) == 5  # exactly n-k+1 = 6-2+1


def check_two_state_walk() -> None:
    for p in (Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1)):
        u = Fraction(1)
        for t in range(20):
            assert u == (1 + (1 - 2*p) ** t) / 2
            u = (1 - p) * u + p * (1 - u)


def check_sylow_order_30() -> None:
    # Allowed counts: n_p divides |G|/p and n_p=1 mod p.
    def possibilities(p: int) -> list[int]:
        index = 30 // p
        return [n for n in range(1, index + 1) if index % n == 0 and n % p == 1]
    assert possibilities(5) == [1, 6]
    assert possibilities(3) == [1, 10]
    # Distinct prime-order subgroups intersect at the identity only.
    assert 6 * (5 - 1) + 10 * (3 - 1) > 30 - 1



def permutation_compose(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    """Apply b, then a. Both permutations use zero-based indexing."""
    return tuple(a[b[i]] for i in range(len(a)))


def permutation_inverse(a: tuple[int, ...]) -> tuple[int, ...]:
    result = [0] * len(a)
    for i, x in enumerate(a):
        result[x] = i
    return tuple(result)


def permutation_even(a: tuple[int, ...]) -> bool:
    return sum(a[i] > a[j] for i in range(len(a))
               for j in range(i + 1, len(a))) % 2 == 0


def check_a5_classes() -> None:
    group = [p for p in itertools.permutations(range(5)) if permutation_even(p)]
    assert len(group) == 60
    remaining = set(group)
    class_sizes = []
    while remaining:
        x = next(iter(remaining))
        cls = {permutation_compose(permutation_compose(g, x), permutation_inverse(g))
               for g in group}
        assert cls <= remaining
        remaining -= cls
        class_sizes.append(len(cls))
    assert sorted(class_sizes) == [1, 12, 12, 15, 20]

    # Normal subgroups are unions of conjugacy classes, including the identity.
    # No nontrivial proper class-union size can divide 60.
    sizes = [12, 12, 15, 20]
    candidates = {1 + sum(sizes[i] for i in range(4) if mask >> i & 1)
                  for mask in range(16)}
    assert sorted(n for n in candidates if 60 % n == 0) == [1, 60]


def check_s4_character_table() -> None:
    # Class order: (), (12), (12)(34), (123), (1234).
    weights = [1, 6, 3, 8, 6]
    rows = [
        (1, 1, 1, 1, 1),       # trivial
        (1, -1, 1, 1, -1),     # sign
        (2, 0, 2, -1, 0),     # lifted 2-dimensional S3 representation
        (3, 1, -1, 0, -1),    # standard
        (3, -1, -1, 0, 1),    # sign twist of standard
    ]
    assert sum(row[0] ** 2 for row in rows) == 24
    for i, row in enumerate(rows):
        for j, other in enumerate(rows):
            inner = sum(w * a * b for w, a, b in zip(weights, row, other))
            assert inner == (24 if i == j else 0), (i, j, inner)
    for i in range(5):
        for j in range(5):
            product = sum(row[i] * row[j] for row in rows)
            assert product == (24 // weights[i] if i == j else 0)


def check_f4() -> None:
    """F4 = F2[X]/(X^2+X+1), encoded with two bits."""
    def mul(a: int, b: int) -> int:
        c = 0
        for i in range(2):
            for j in range(2):
                if a >> i & 1 and b >> j & 1:
                    c ^= 1 << (i + j)
        if c & 4:       # x^2 = x+1
            c ^= 0b111
        return c
    for a in range(4):
        assert mul(mul(a, a), mul(a, a)) == a
    for a in range(1, 4):
        assert any(mul(a, b) == 1 for b in range(1, 4))


def check_fifteen_parity() -> None:
    tiles = list(range(1, 17))
    blank = 15
    for move in range(600):
        # Deterministic legal walk through a 4x4 grid, with reversals allowed.
        row, col = divmod(blank, 4)
        neighbours = [(r * 4 + c) for r, c in
                      ((row - 1, col), (row + 1, col),
                       (row, col - 1), (row, col + 1))
                      if 0 <= r < 4 and 0 <= c < 4]
        target = neighbours[(move * 7 + 3) % len(neighbours)]
        tiles[blank], tiles[target] = tiles[target], tiles[blank]
        blank = target
        inversions = sum(tiles[i] > tiles[j] for i in range(16) for j in range(i + 1, 16))
        colour = (sum(divmod(blank, 4)) % 2)
        assert (inversions + colour) % 2 == 0
    unsolved = list(range(1, 17))
    unsolved[13], unsolved[14] = unsolved[14], unsolved[13]  # 14 and 15 exchanged
    assert sum(unsolved[i] > unsolved[j] for i in range(16)
               for j in range(i + 1, 16)) % 2 == 1


def check_quaternion_norm() -> None:
    def mul(q: tuple[int, int, int, int],
            r: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
        a, b, c, d = q
        e, f, g, h = r
        return (a*e-b*f-c*g-d*h, a*f+b*e+c*h-d*g,
                a*g-b*h+c*e+d*f, a*h+b*g-c*f+d*e)

    def norm(q: tuple[int, int, int, int]) -> int:
        return sum(x * x for x in q)

    values = list(itertools.product(range(-2, 3), repeat=4))
    for q in values[::17]:
        for p in values[::29]:
            assert norm(mul(q, p)) == norm(q) * norm(p)
    assert mul((0, 1, 0, 0), (0, 0, 1, 0)) == (0, 0, 0, 1)  # i*j=k
    assert mul((0, 0, 1, 0), (0, 1, 0, 0)) == (0, 0, 0, -1)  # j*i=-k



def check_fifteen_rectangle_generation() -> None:
    """Independently check the concrete 15-puzzle loop table in Chapter 4.

    This checks the nontrivial finite bookkeeping in the converse argument.
    It relies on (rather than proves) the preceding abstract growth lemmas.
    """
    def cycle(mapping: tuple[int, ...]) -> dict[int, int]:
        return dict(zip(mapping, mapping[1:] + mapping[:1]))

    def image(h: dict[int, int], x: int) -> int:
        return h.get(x, x)

    s = {11, 12, 15}  # 2-by-2 loop generates A(s)
    assert s == set(cycle((15, 12, 11)).keys())

    h = cycle((14, 15, 12, 11, 10))
    assert len({image(h, x) for x in s} & s) == 2
    s.add(10)

    # An application of growth fact (ii) needs two points staying in s
    # and a third whose image leaves s. The latter is then added.
    def grow(h: dict[int, int], stays: tuple[int, int], exits: tuple[int, ...]) -> None:
        assert len(s) >= 4
        x, y = stays
        assert x in s and y in s and x != y
        assert image(h, x) in s and image(h, y) in s
        for z in exits:
            assert z in s
            new = image(h, z)
            assert new not in s, (z, new, sorted(s))
            s.add(new)

    grow(h, (11, 12), (10,))
    h = cycle((13, 14, 15, 12, 11, 10, 9))
    grow(h, (11, 12), (10,))
    grow(h, (10, 11), (9,))
    h = cycle((11, 15, 12, 8, 7))
    grow(h, (11, 15), (12, 8))
    h = cycle((11, 15, 12, 8, 4, 3, 7))
    grow(h, (11, 15), (8, 4))
    h = cycle((13, 14, 15, 12, 8, 7, 6, 5, 9))
    grow(h, (13, 14), (7, 6))
    h = cycle((13, 14, 15, 12, 8, 4, 3, 2, 1, 5, 9))
    grow(h, (13, 14), (3, 2))
    assert s == set(range(1, 16))



def check_alternating_simple_commutators() -> None:
    """Audit the three explicit commutators in the A_n simplicity proof."""
    def cyc(n: int, *cycles: tuple[int, ...]) -> tuple[int, ...]:
        p = list(range(n))
        for c in cycles:
            for j, x in enumerate(c):
                p[x] = c[(j + 1) % len(c)]
        return tuple(p)

    def comm(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
        return permutation_compose(a, permutation_compose(
            b, permutation_compose(permutation_inverse(a), permutation_inverse(b))))

    sigma = cyc(6, (0, 1, 2, 3))
    tau = cyc(6, (0, 1, 2))
    assert comm(tau, sigma) == cyc(6, (0, 1, 3))

    sigma = cyc(6, (0, 1, 2), (3, 4, 5))
    tau = cyc(6, (0, 1, 3))
    assert comm(tau, sigma) == cyc(6, (0, 1, 4, 2, 3))

    sigma = cyc(6, (0, 1), (2, 3))
    tau = cyc(6, (0, 1, 2))
    rho = comm(tau, sigma)
    assert rho == cyc(6, (0, 2), (1, 3))
    kappa = cyc(6, (0, 2, 4))
    assert comm(kappa, rho) == cyc(6, (0, 4, 2))



def check_maximum_permutation_orders() -> None:
    """Exhaust integer partitions, not 7! or 10! permutations."""
    def orders(n: int, smallest: int = 1):
        if n == 0:
            yield ()
        for k in range(smallest, n + 1):
            for rest in orders(n - k, k):
                yield (k,) + rest
    def max_order(n: int) -> int:
        return max(math.lcm(*lengths) for lengths in orders(n))
    assert max_order(7) == 12
    assert max_order(10) == 30


def check_cube_face_colourings() -> None:
    # Face 2*i is +e_i; face 2*i+1 is -e_i. Signed permutations
    # with determinant +1 are exactly the 24 cube rotations.
    def sign(p):
        return -1 if sum(p[i] > p[j] for i in range(3)
                         for j in range(i+1, 3)) % 2 else 1
    rotations = []
    for p in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            if sign(p) * math.prod(signs) != 1:
                continue
            face_image = tuple(2*p[i//2] + ((i%2) ^ (signs[i//2] == -1))
                               for i in range(6))
            assert sorted(face_image) == list(range(6))
            rotations.append(face_image)
    assert len(rotations) == 24
    words = list(itertools.product(range(3), repeat=6))
    # The canonical member of each orbit is invariant under rotation.
    canonical = {min(tuple(w[g[i]] for i in range(6)) for g in rotations)
                 for w in words}
    assert len(canonical) == 57
    fixed = [sum(all(w[i] == w[g[i]] for i in range(6)) for w in words)
             for g in rotations]
    assert sum(fixed) == 24 * 57
    assert sorted(fixed) == sorted([3**6] + [3**3]*6 + [3**4]*3
                                   + [3**2]*8 + [3**3]*6)


def check_f2_irreducibles() -> None:
    # Polynomials are bitsets; bit i represents coefficient of X^i.
    def degree(a):
        return a.bit_length()-1
    def remainder(a, b):
        while a and degree(a) >= degree(b):
            a ^= b << (degree(a)-degree(b))
        return a
    def product(a, b):
        out = 0
        while b:
            if b & 1:
                out ^= a
            a <<= 1
            b >>= 1
        return out
    irr = []
    for n in range(1, 5):
        for a in range(1 << n, 1 << (n+1)):
            if not any(remainder(a, d) == 0 for k in range(1, n//2+1)
                       for d in range(1 << k, 1 << (k+1))):
                irr.append(a)
    by_degree = [sorted(a for a in irr if degree(a)==n) for n in range(1,5)]
    assert by_degree == [[0b10, 0b11], [0b111],
                         [0b1011, 0b1101],
                         [0b10011, 0b11001, 0b11111]]
    value = 1
    for n in (1, 2, 4):
        for a in by_degree[n-1]:
            value = product(value, a)
    assert value == (1 << 16) | 0b10  # X^16-X = X^16+X in F2


def check_seven_cyclotomic_period() -> None:
    # ζ^7=1, 1+ζ+...+ζ^6=0.
    a, b = (1,2,4), (3,5,6)
    exponents = [(x+y) % 7 for x in a for y in b]
    assert exponents.count(0) == 3
    assert [exponents.count(x) for x in range(1,7)] == [1]*6
    # η+η'=-1 and ηη'=3+(-1)=2.
    assert -(-1) == 1 and 1 - 8 == -7


def check_quaternion_rotation_matrix() -> None:
    def prod(q, r):
        a,b,c,d = q
        e,f,g,h = r
        return (a*e-b*f-c*g-d*h, a*f+b*e+c*h-d*g,
                a*g-b*h+c*e+d*f, a*h+b*g-c*f+d*e)
    for a,b,c,d in [(1,0,0,0), (0,1,0,0), (1,2,3,4), (3,-2,1,-5)]:
        q = (a,b,c,d)
        qb = (a,-b,-c,-d)
        norm = a*a+b*b+c*c+d*d
        numerator_columns = [
            prod(prod(q, v), qb)[1:]
            for v in ((0,1,0,0),(0,0,1,0),(0,0,0,1))
        ]
        matrix_columns = [
            (a*a+b*b-c*c-d*d, 2*(b*c+a*d), 2*(b*d-a*c)),
            (2*(b*c-a*d), a*a-b*b+c*c-d*d, 2*(c*d+a*b)),
            (2*(b*d+a*c), 2*(c*d-a*b), a*a-b*b-c*c+d*d),
        ]
        assert numerator_columns == matrix_columns
        assert sum(matrix_columns[i][i] for i in range(3)) == 4*a*a-norm



def check_fano_plane_and_paley_four() -> None:
    lines = [{1,2,4}, {1,3,5}, {2,3,6},
             {1,6,7}, {2,5,7}, {3,4,7}, {4,5,6}]
    assert len(lines) == 7 and all(len(line) == 3 for line in lines)
    assert all(len(a & b) == 1 for i, a in enumerate(lines)
               for b in lines[i+1:])
    point_vectors = {1:0b001,2:0b010,3:0b100,4:0b011,
                     5:0b101,6:0b110,7:0b111}
    assert all(point_vectors[a] ^ point_vectors[b] == point_vectors[c]
               for line in lines for a,b,c in itertools.permutations(line,3))

    # Paley I for F3 in the rewritten appendix worked solution.
    h = [(1,1,1,1),(-1,1,-1,1),(-1,1,1,-1),(-1,-1,1,1)]
    assert all(sum(a*b for a,b in zip(u,v)) == (4 if i==j else 0)
               for i,u in enumerate(h) for j,v in enumerate(h))


def main() -> None:
    labels, refs, figures = check_labels_and_figures()
    check_necklaces()
    check_cube()
    check_quintic()
    check_rs_distance()
    check_two_state_walk()
    check_sylow_order_30()
    check_a5_classes()
    check_alternating_simple_commutators()
    check_s4_character_table()
    check_f4()
    check_fifteen_parity()
    check_fifteen_rectangle_generation()
    check_quaternion_norm()
    check_maximum_permutation_orders()
    check_cube_face_colourings()
    check_f2_irreducibles()
    check_seven_cyclotomic_period()
    check_quaternion_rotation_matrix()
    check_fano_plane_and_paley_four()
    print(f"Volume 3 checks PASS: {labels} labels, {refs} references, {figures} figure inputs")
    print("PASS: necklaces; cube rotations; quintic; Reed-Solomon; walk; Sylow; A_n commutators; A5 classes; S4 characters; F4; fifteen-puzzle parity and loops; quaternion norms")


if __name__ == "__main__":
    main()
