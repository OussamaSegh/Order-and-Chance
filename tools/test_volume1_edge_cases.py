"""Finite regression checks for Volume 1's exercise edge cases."""

from itertools import combinations, product
from math import comb
import unittest


def connected(n, edges):
    seen = {0}
    frontier = [0]
    while frontier:
        v = frontier.pop()
        for a, b in edges:
            if a == v and b not in seen:
                seen.add(b)
                frontier.append(b)
            elif b == v and a not in seen:
                seen.add(a)
                frontier.append(a)
    return len(seen) == n


def spanning_tree_count(n, edges):
    return sum(connected(n, choice) for choice in combinations(edges, n - 1))


def first_empty_spot(n, preferences):
    used = set()
    for preferred in preferences:
        for position in range(preferred, n + 2):
            if position not in used:
                used.add(position)
                break
    return next(position for position in range(1, n + 2) if position not in used)


class VolumeOneEdgeCases(unittest.TestCase):
    def test_schwartz_zippel_bound_is_sharp_below_and_above_sample_size(self):
        # Polynomials over F_7, sampled uniformly on S = {0, 1, 2}.
        sample = (0, 1, 2)
        for degree in range(7):
            roots = sample[:min(degree, len(sample))]

            def evaluate(x):
                value = pow(x, max(0, degree - len(sample)), 7)
                for root in roots:
                    value = value * (x - root) % 7
                return value

            zero_count = sum(evaluate(x) == 0 for x in sample)
            self.assertEqual(zero_count, min(degree, len(sample)))
            self.assertEqual(zero_count / len(sample), min(1, degree / len(sample)))

    def test_parking_function_endpoint_counts(self):
        # Explicit enumeration includes k=0 and k=n (the empty assignment 0**0=1).
        for n in range(1, 5):
            actual = [0] * (n + 1)
            for preferences in product(range(1, n + 2), repeat=n):
                k = first_empty_spot(n, preferences) - 1
                actual[k] += 1
            expected = [comb(n, k) * (k + 1) ** (k - 1) * (n - k) ** (n - k)
                        for k in range(n + 1)]
            self.assertEqual(actual, expected)
            self.assertEqual(sum(actual), (n + 1) ** n)

    def test_spanning_tree_bound_and_equality_for_small_simple_graphs(self):
        # For n>=2, n*tau*(n-1)^(n-1) <= (2m)^(n-1).
        for n in range(2, 5):
            possible_edges = list(combinations(range(n), 2))
            for mask in range(1 << len(possible_edges)):
                edges = [edge for i, edge in enumerate(possible_edges) if mask & (1 << i)]
                if not connected(n, edges):
                    continue
                tau = spanning_tree_count(n, edges)
                lhs = n * tau * (n - 1) ** (n - 1)
                rhs = (2 * len(edges)) ** (n - 1)
                self.assertLessEqual(lhs, rhs)
                self.assertEqual(lhs == rhs, len(edges) == len(possible_edges))


if __name__ == "__main__":
    unittest.main()
