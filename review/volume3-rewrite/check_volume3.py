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


def main() -> None:
    labels, refs, figures = check_labels_and_figures()
    check_necklaces()
    check_cube()
    check_quintic()
    check_rs_distance()
    check_two_state_walk()
    check_sylow_order_30()
    print(f"Volume 3 checks PASS: {labels} labels, {refs} references, {figures} figure inputs")
    print("PASS: necklaces; cube rotations; quintic input; RS distance; two-state walk; Sylow counts")


if __name__ == "__main__":
    main()
