"""Independent finite checks for the two-kth-powers character exercise.

These test numeric consequences of the proof and the first-use/placement
contract. The general bound still requires the symbolic Gauss/Jacobi-sum
argument in the book; finitely many primes cannot prove it.
"""
import cmath
import math
import unittest
from pathlib import Path


CH11 = (Path(__file__).resolve().parents[1] / "volume2-integers"
        / "chapters" / "ch14-characters.tex")


def primes_to(limit):
    return [n for n in range(2, limit + 1)
            if all(n % d for d in range(2, math.isqrt(n) + 1))]


def generator(p):
    factors = [q for q in primes_to(p - 1) if (p - 1) % q == 0]
    return next(g for g in range(2, p)
                if all(pow(g, (p - 1) // q, p) != 1 for q in factors))


def root_counts(p, k):
    counts = [0] * p
    for x in range(p):
        counts[pow(x, k, p)] += 1
    return counts


def two_power_counts(counts):
    p = len(counts)
    return [sum(counts[u] * counts[(c - u) % p] for u in range(p))
            for c in range(p)]


class TestWaringCharacterBound(unittest.TestCase):
    def test_character_expansion_exact_count_and_general_bound(self):
        cases = 0
        for p in primes_to(97):
            if p == 2:
                continue
            g = generator(p)
            discrete_log = {pow(g, j, p): j for j in range(p - 1)}
            for k in range(2, min(p, 11)):
                if (p - 1) % k:
                    continue

                def chi(j, u):
                    if u == 0:
                        return 1 if j == 0 else 0
                    return cmath.exp(2j * math.pi
                                     * (j * discrete_log[u] % k) / k)

                jacobi = {(a, b):
                          sum(chi(a, u) * chi(b, (1-u) % p)
                              for u in range(p))
                          for a in range(k) for b in range(k)}
                counts = two_power_counts(root_counts(p, k))
                for c in range(1, p):
                    via_characters = sum(
                        chi((a+b) % k, c) * jacobi[(a, b)]
                        for a in range(k) for b in range(k)
                    )
                    with self.subTest(p=p, k=k, c=c):
                        self.assertAlmostEqual(via_characters.real,
                                               counts[c], places=7)
                        self.assertAlmostEqual(via_characters.imag,
                                               0, places=7)
                        self.assertLessEqual(
                            abs(counts[c] - p),
                            (k-1)*(k-2)*math.sqrt(p)+k-1+1e-9
                        )
                        if p >= k**4:
                            self.assertGreater(counts[c], 0)
                    cases += 1
        self.assertGreater(cases, 3000)

    def test_independent_additive_fourier_count(self):
        # Unlike the Jacobi calculation above, this starts from the
        # root-of-unity filter of x^k+y^k-c=0 directly.
        for p, k in ((7, 3), (13, 3), (17, 4), (31, 3), (41, 8)):
            f = root_counts(p, k)
            exact = two_power_counts(f)
            transform = [sum(f[u] * cmath.exp(2j*math.pi*t*u/p)
                             for u in range(p)) for t in range(p)]
            for c in range(p):
                recovered = sum(
                    transform[t]**2 * cmath.exp(-2j*math.pi*t*c/p)
                    for t in range(p)
                ) / p
                with self.subTest(p=p, k=k, c=c):
                    self.assertAlmostEqual(recovered.real,
                                           exact[c], places=7)
                    self.assertAlmostEqual(recovered.imag,
                                           0, places=7)

    def test_exponent_reduces_to_gcd_with_group_order(self):
        for p in primes_to(47):
            if p == 2:
                continue
            for k in range(2, p + 6):
                d = math.gcd(k, p - 1)
                with self.subTest(p=p, k=k):
                    self.assertEqual(root_counts(p, k),
                                     root_counts(p, d))

    def test_first_use_and_reader_clarity(self):
        text = CH11.read_text(encoding="utf-8")
        cubic = text.split(r"\label{pb:fermatcubic}", 1)[1].split(
            r"\end{exercise}", 1)[0]
        waring = text.split(r"\begin{solution}{pb:waring}", 1)[1].split(
            r"\end{solution}", 1)[0]
        self.assertIn(r"e(t)=\exp(2\pi i\widetilde t/p)", cubic)
        self.assertLess(cubic.index("e(t)="), cubic.index("g(\\alpha)="))
        self.assertIn("For a nonzero $k$th power this number is $k$", waring)
        self.assertIn(r"J(\chi,\bar\chi)=\sum_{t\ne0,-1}", waring)
        self.assertIn("same image and exactly $d$ preimages", waring)
        self.assertNotIn("which itself depends on Volume~5",
                         text.split(r"\label{pb:jacobi}", 1)[1].split(
                             r"\end{exercise}", 1)[0])
        powerful = text.split(r"\begin{solution}{pb:powerful}", 1)[1].split(
            r"\end{solution}", 1)[0]
        self.assertNotIn(r"\tools Volume~6", powerful)


if __name__ == "__main__":
    unittest.main()
