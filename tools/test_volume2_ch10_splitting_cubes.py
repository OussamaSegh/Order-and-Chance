"""Independent finite factor searches and exact Eisenstein residue checks."""

import itertools
import math
import unittest

from tools.test_volume2_ch10_euclidean import QuadraticRing


def prime(n):
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))


def irreducible_by_trial(ring, z):
    N = ring.norm(z)
    if N <= 1:
        return False
    bound = math.ceil(math.sqrt(2 * math.isqrt(N)))
    for w in itertools.product(range(-bound, bound + 1), repeat=2):
        norm = ring.norm(w)
        if norm <= 1 or norm*norm > N:
            continue
        numerator = ring.multiply(z, ring.conjugate(w))
        if all(c % norm == 0 for c in numerator):
            return False
    return True


class SplittingCubeChecks(unittest.TestCase):
    def test_prime_classifications_against_trial_factors(self):
        for ring in (QuadraticRing(-1), QuadraticRing(-1, -1)):
            for z in itertools.product(range(-12, 13), repeat=2):
                N = ring.norm(z)
                if N > 225:
                    continue
                q = math.isqrt(N)
                inert_associate = (q*q == N and prime(q) and
                    q % (4 if ring.v == 0 else 3) == (3 if ring.v == 0 else 2) and
                    all(c % q == 0 for c in z))
                self.assertEqual(irreducible_by_trial(ring, z), prime(N) or inert_associate,
                                 (ring.u, ring.v, z))

    def test_two_square_representation_counts(self):
        limit = 10000
        counts, divisor_sums = [0] * (limit+1), [0] * (limit+1)
        for x in range(-100, 101):
            for y in range(-100, 101):
                n = x*x+y*y
                if n <= limit:
                    counts[n] += 1
        for d in range(1, limit+1, 2):
            chi = 1 if d % 4 == 1 else -1
            for n in range(d, limit+1, d):
                divisor_sums[n] += chi
        for n in range(1, limit+1):
            self.assertEqual(counts[n], 4*divisor_sums[n], n)
        self.assertEqual((counts[45], counts[65], counts[325]), (8, 16, 24))

    def test_cube_and_unit_congruences_in_complete_residue_ring(self):
        ring = QuadraticRing(-1, -1)
        lam, omega, omega2 = (1, -1), (0, 1), (-1, -1)
        self.assertEqual(ring.multiply(lam, lam), (0, -3))
        self.assertEqual(ring.multiply((0, -3), (0, -3)), (-9, -9))
        # (lambda^4)=(9), so these are every one of the 81 residue classes.
        for theta in itertools.product(range(9), repeat=2):
            if sum(theta) % 3:
                cube = ring.multiply(ring.multiply(theta, theta), theta)
                self.assertIn(tuple(c % 9 for c in cube), ((1, 0), (8, 0)))
        units = [(1, 0), (-1, 0), omega, (0, -1), omega2, (1, 1)]
        for eta in units:
            for sign1 in (-1, 1):
                for sign2 in (-1, 1):
                    if (sign1+sign2*eta[0]) % 3 == 0 and (sign2*eta[1]) % 3 == 0:
                        self.assertIn(eta, ((1, 0), (-1, 0)))

    def test_linear_relation_between_cubic_factors(self):
        ring = QuadraticRing(-1, -1)
        omega, omega2 = (0, 1), (-1, -1)
        points = list(itertools.product(range(-2, 3), repeat=2))
        for alpha in points:
            for beta in points:
                factors = [tuple(x+y for x, y in zip(alpha, ring.multiply(unit, beta)))
                           for unit in ((1, 0), omega, omega2)]
                terms = [ring.multiply(unit, f) for unit, f in
                         zip(((1, 0), omega, omega2), factors)]
                self.assertEqual(tuple(sum(t[j] for t in terms) for j in range(2)), (0, 0))


if __name__ == "__main__":
    unittest.main()
