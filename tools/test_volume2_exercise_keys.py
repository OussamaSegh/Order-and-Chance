"""Step 6: independent finite checks for the 144 Volume 2 exercise keys.

These tests detect numerical and structural regressions but do not substitute
for proof review or the printed proof. Run:
    python -m unittest discover -s tools -p "test_volume2_*.py"
"""
import math
import re
import unittest
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHAPTER_DIR = ROOT / "volume2-integers" / "chapters"
CHAPTERS = [
    "ch01-divisibility", "ch02-primes", "ch03-congruences",
    "ch04-arithmetic-functions", "ch05-primitive-roots",
    "ch06-quadratic-reciprocity", "ch07-sums-of-squares",
    "ch09-diophantine", "ch08-continued-fractions",
    "ch10-gaussian-eisenstein", "ch14-characters",
]
EXPECTED_COUNTS = [16, 11, 21, 13, 15, 17, 8, 8, 8, 8, 19]


def content(chapter):
    return (CHAPTER_DIR / (chapter + ".tex")).read_text(encoding="utf-8")


def section(text, env, label):
    if env == "exercise":
        prefix = re.search(
            r"\\begin\{exercise\}(?:\[[^\]]*\])?\s*\\label\{" +
            re.escape(label) + r"\}([\s\S]*?)\\end\{exercise\}", text
        )
    else:
        prefix = re.search(
            r"\\begin\{" + env + r"\}\{" +
            re.escape(label) + r"\}([\s\S]*?)\\end\{" + env + r"\}", text
        )
    if prefix is None:
        raise AssertionError(f"Missing {env}: {label}")
    return prefix.group(1)


def is_prime(n):
    return n > 1 and all(n % d for d in range(2, math.isqrt(n) + 1))


def gcd_moment(n):
    return sum(math.gcd(a, b) for a in range(1, n + 1)
               for b in range(1, n + 1))


class TestVolume2ExerciseKeys(unittest.TestCase):
    def test_every_chapter_retains_its_individual_exercise_inventory(self):
        total = 0
        ids = set()
        for chapter, expected in zip(CHAPTERS, EXPECTED_COUNTS):
            with self.subTest(chapter=chapter):
                source = content(chapter)
                entries = re.findall(
                    r"\\begin\{exercise\}(?:\[([^\]]*)\])?"
                    r"\s*\\label\{([^}]+)\}", source,
                )
                hints = re.findall(r"\\begin\{hint\}\{([^}]+)\}", source)
                solutions = re.findall(
                    r"\\begin\{solution\}\{([^}]+)\}", source
                )
                self.assertEqual(len(entries), expected)
                self.assertEqual([key for _, key in entries], hints)
                self.assertEqual(hints, solutions)
                for grade, key in entries:
                    self.assertNotIn(key, ids)
                    ids.add(key)
                    self.assertIn(
                        grade,
                        (
                            r"$\star$", r"$\star\star$",
                            r"$\star\star\star$", "Journey",
                        ),
                    )
                    self.assertTrue(section(source, "exercise", key).strip())
                    self.assertTrue(section(source, "hint", key).strip())
                    solution = section(source, "solution", key)
                    self.assertIn(r"\idea", solution)
                    self.assertIn(r"\writeup", solution)
                    self.assertIn(r"\tools", solution)
                    self.assertIn(r"\leads", solution)
                total += len(entries)
        self.assertEqual(total, 144)

    def test_imo_1988_vieta_jump_requires_a_positive_integer_root(self):
        text = section(content("ch09-diophantine"), "solution", "ex:imo88")
        for marker in (r"f(b)=(2-k)b^2-k<0", r"f(-1)",
                       r"$1\le a'<b\le a$"):
            # The argument must establish the other root is in (0,b).
            if marker.startswith("$"):
                self.assertIn(marker, text)
            else:
                self.assertIn(marker, text)
        for a in range(1, 160):
            for b in range(1, a + 1):
                numerator = a*a + b*b
                denominator = a*b + 1
                if numerator % denominator:
                    continue
                k = numerator // denominator
                self.assertEqual(math.isqrt(k) ** 2, k)
                if k > 1:
                    self.assertLessEqual(k, a*a + b*b)

    def test_gcd_mean_key_proves_its_own_totient_average(self):
        text = section(
            content("ch05-primitive-roots"), "solution", "pb:gcdmean"
        )
        self.assertIn(r"A(t):=\sum_{d\le t}\frac{\varphi(d)}d", text)
        self.assertIn(r"\frac{t}{\zeta(2)}+O(\log(2t))", text)
        self.assertIn(r"\frac{\log N}{\zeta(2)}+O(1)", text)
        for n in (10, 30, 60):
            phi = [
                sum(math.gcd(j, d) == 1 for j in range(1, d + 1))
                for d in range(1, n + 1)
            ]
            from_totients = sum(
                phi[d - 1] * (n // d) ** 2
                for d in range(1, n + 1)
            )
            self.assertEqual(gcd_moment(n), from_totients)

    def test_diophantine_integer_cases_and_markov_tree(self):
        text = content("ch09-diophantine")
        self.assertIn(r"1\le a'<b\le a", text)
        for x in range(-35, 501):
            cube = x ** 3
            for offset, expected in ((-2, {3}), (-5, set())):
                # y²=x³+offset, with x finite.
                value = cube + offset
                if value < 0:
                    continue
                root = math.isqrt(value)
                if root * root == value and offset == -2:
                    self.assertEqual(x, 3)
                if root * root == value and offset == -5:
                    self.fail(f"Mordell-5 counterexample at x={x}")
        # Enumerate all sorted positive Markov triples whose maximum <=200.
        found = set()
        for a in range(1, 201):
            for b in range(a, 201):
                disc = 9 * a*a * b*b - 4 * (a*a + b*b)
                if disc < 0:
                    continue
                root = math.isqrt(disc)
                if root * root != disc:
                    continue
                for sign in (-1, 1):
                    numer = 3*a*b + sign*root
                    if numer % 2:
                        continue
                    z = numer // 2
                    if b <= z <= 200:
                        found.add((a, b, z))
        self.assertEqual(found, {
            (1, 1, 1), (1, 1, 2), (1, 2, 5), (1, 5, 13),
            (2, 5, 29), (1, 13, 34), (1, 34, 89),
            (2, 29, 169), (5, 13, 194),
        })

    def test_cyclic_roots_legendre_and_two_square_cases(self):
        for p in range(3, 151, 2):
            if not is_prime(p):
                continue
            squares = {x*x % p for x in range(p)}
            sign_2 = 1 if 2 in squares else -1
            expected = 1 if p % 8 in (1, 7) else -1
            self.assertEqual(sign_2, expected)
            if p % 4 == 1:
                self.assertIn(p, {
                    a*a + b*b
                    for a in range(math.isqrt(p) + 1)
                    for b in range(math.isqrt(p) + 1)
                })

    def test_prime_power_fermat_and_modular_root_samples(self):
        self.assertEqual(pow(2, 32, 641), 640)
        self.assertEqual(pow(2, 32, 641) + 1, 641)
        for n in range(2, 251):
            self.assertNotEqual((pow(2, n, n) - 1) % n, 0)
        for k in range(1, 9):
            m = 2 ** k
            roots = {x for x in range(m) if x*x % m == 1 % m}
            if k == 1:
                expected = {1}
            elif k == 2:
                expected = {1, 3}
            else:
                expected = {
                    1, m-1, 1 + m//2, (m//2 - 1) % m
                }
            self.assertEqual(roots, expected)

    def test_waring_character_bound_has_expected_small_exceptions(self):
        misses = {3: [], 4: [], 8: []}
        for p in range(3, 800, 2):
            if not is_prime(p):
                continue
            for k in (3, 4, 8):
                if (p-1) % k:
                    continue
                power_values = {pow(x, k, p) for x in range(p)}
                sums = {(a+b) % p
                        for a in power_values for b in power_values}
                if len(sums) != p:
                    misses[k].append(p)
                if p >= k**4:
                    self.assertEqual(len(sums), p)
        self.assertEqual(misses[3], [7])
        self.assertEqual(misses[4], [5, 13, 17, 29])
        self.assertEqual(misses[8], [
            17, 41, 73, 89, 97, 113, 137, 233, 257, 337, 761
        ])

    def test_pseudoprime_and_primality_certificate_examples(self):
        self.assertEqual(pow(2, 340, 341), 1)
        self.assertFalse(is_prime(341))
        self.assertEqual(pow(3, 1664, 3329), 3328)
        self.assertTrue(is_prime(3329))
        for p in (5, 7, 11):
            n = (4**p - 1)//3
            self.assertFalse(is_prime(n))
            self.assertEqual(pow(2, n-1, n), 1)
        # A base-2 pseudoprime remains one after the Euclid exponent step.
        n = 341
        m = 2**n - 1
        self.assertEqual(pow(2, m-1, m), 1)

    def test_pell_calendar_powerful_and_gaussian_examples(self):
        self.assertEqual(13**2 + 0, 169)
        self.assertEqual(1766319049**2 - 61*226153980**2, 1)
        self.assertEqual(1000009, 293*3413)
        self.assertEqual(1000009, 1000**2+3**2)
        self.assertEqual(1000009, 972**2+235**2)
        self.assertEqual(8+1, 3**2)
        self.assertEqual(288+1, 17**2)
        self.assertAlmostEqual(31/128, 0.2421875, places=9)
        # Unique a²b³ representation for powerful n<=1,000.
        powerful = set()
        for a in range(1, 32):
            for b in range(1, 11):
                # b must be squarefree.
                if any(b % (p*p) == 0 for p in range(2, b+1)):
                    continue
                z = a*a*b*b*b
                if z <= 1000:
                    self.assertNotIn(z, powerful)
                    powerful.add(z)
        for n in range(1, 1001):
            m = n
            is_powerful = True
            for p in range(2, math.isqrt(n)+1):
                if m % p:
                    continue
                count = 0
                while m % p == 0:
                    m //= p
                    count += 1
                if count == 1:
                    is_powerful = False
            if m > 1 and m != n:
                # The remainder has exponent one unless original n was prime.
                is_powerful = False
            if m == n and is_prime(n):
                is_powerful = False
            self.assertEqual(n in powerful, is_powerful, f"n={n}")

    def test_four_square_local_density_seed_at_two(self):
        counts = [0] * 8
        primitive = [0] * 8
        for coordinates in product(range(8), repeat=4):
            value = sum(x*x for x in coordinates) % 8
            counts[value] += 1
            if any(x % 2 for x in coordinates):
                primitive[value] += 1
        self.assertEqual(primitive, [0, 512, 768, 512, 256, 512, 768, 512])


if __name__ == "__main__":
    unittest.main()
