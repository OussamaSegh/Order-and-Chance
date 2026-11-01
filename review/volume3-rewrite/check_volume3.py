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


def main() -> None:
    labels, refs, figures = check_labels_and_figures()
    check_necklaces()
    check_cube()
    check_quintic()
    check_rs_distance()
    check_two_state_walk()
    check_sylow_order_30()
    check_a5_classes()
    check_s4_character_table()
    check_f4()
    check_fifteen_parity()
    check_quaternion_norm()
    print(f"Volume 3 checks PASS: {labels} labels, {refs} references, {figures} figure inputs")
    print("PASS: necklaces; cube rotations; quintic; Reed-Solomon; walk; Sylow; A5 classes; S4 characters; F4; fifteen-puzzle parity; quaternion norms")


if __name__ == "__main__":
    main()
