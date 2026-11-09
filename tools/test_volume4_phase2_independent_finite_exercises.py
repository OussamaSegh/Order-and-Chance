"""Independent, finite mathematical checks for Volume 4 Phase 2.

Unlike source-string guards, these enumerate sample spaces or solve exact rational
equations independently. They do not certify the general theorems or all 107
exercise solutions. Run with unittest discover -s tools -p 'test_*.py'.
"""
from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import comb, factorial
import heapq
import unittest


def solve_linear(a, b):
    n = len(b)
    x = [[F(v) for v in row] + [F(b[i])] for i, row in enumerate(a)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if x[i][k])
        x[k], x[pivot] = x[pivot], x[k]
        t = x[k][k]
        x[k] = [v / t for v in x[k]]
        for i in range(n):
            if i != k:
                t = x[i][k]
                x[i] = [v - t * w for v, w in zip(x[i], x[k])]
    return [x[i][-1] for i in range(n)]


def cycles(p):
    seen, count = set(), 0
    for root in range(len(p)):
        if root in seen:
            continue
        count += 1
        k = root
        while k not in seen:
            seen.add(k)
            k = p[k]
    return count


class TestIndependentFiniteExerciseCalculations(unittest.TestCase):
    def test_ballot_and_catalan_by_exhaustive_walk_enumeration(self):
        for a in range(1, 9):
            for b in range(a):
                n, good = a + b, 0
                for minus_positions in combinations(range(n), b):
                    minus, height, admissible = set(minus_positions), 0, True
                    for j in range(n):
                        height += -1 if j in minus else 1
                        admissible &= height > 0
                    good += admissible
                self.assertEqual(F(good, comb(n, b)), F(a - b, n))
        for n in range(1, 8):
            good = 0
            for steps in product((-1, 1), repeat=2 * n):
                h, valid = 0, True
                for s in steps:
                    h += s
                    valid &= h >= 0
                good += valid and h == 0
            self.assertEqual(good, comb(2 * n, n) // (n + 1))

    def test_last_return_and_positive_occupation_laws_by_all_paths(self):
        for n in range(1, 6):
            last, occupation, positive = Counter(), Counter(), 0
            for signs in product((-1, 1), repeat=2 * n):
                h, last_return, above, nonnegative = 0, 0, 0, True
                for j, sign in enumerate(signs, 1):
                    nxt = h + sign
                    above += h + nxt > 0
                    h = nxt
                    nonnegative &= h >= 0
                    if h == 0:
                        last_return = j
                last[last_return] += 1
                occupation[above] += 1
                positive += nonnegative
            self.assertEqual(last, occupation)
            for k in range(n + 1):
                u = F(comb(2*k, k), 4**k)
                v = F(comb(2*(n-k), n-k), 4**(n-k))
                self.assertEqual(F(last[2*k], 4**n), u*v)
            self.assertEqual(F(positive, 4**n), F(comb(2*n, n), 4**n))

    def test_ruin_probabilities_and_mean_exit_times_by_rational_linear_algebra(self):
        for n in range(2, 9):
            for p in (F(1, 3), F(1, 2), F(2, 3)):
                q = 1-p
                matrix, win_rhs = [], []
                for k in range(1, n):
                    row = [F(j == k) for j in range(1, n)]
                    if k+1 < n:
                        row[k] -= p
                    if k-1 > 0:
                        row[k-2] -= q
                    matrix.append(row)
                    win_rhs.append(p if k == n-1 else F(0))
                hit = solve_linear(matrix, win_rhs)
                wait = solve_linear(matrix, [F(1)]*(n-1))
                for k in range(1, n):
                    win = F(k,n) if p == q else ((q/p)**k-1)/((q/p)**n-1)
                    mean = (F(k*(n-k)) if p == q else
                            F(k)/(q-p)-F(n)/(q-p)*(1-(q/p)**k)/(1-(q/p)**n))
                    self.assertEqual(hit[k-1], win)
                    self.assertEqual(wait[k-1], mean)

    def test_permutation_fixed_points_cycles_and_quicksort(self):
        for n in range(2, 8):
            sum_fixed = sum_fixed2 = sum_cycles = 0
            for perm in permutations(range(n)):
                fixed = sum(perm[i] == i for i in range(n))
                sum_fixed += fixed
                sum_fixed2 += fixed**2
                sum_cycles += cycles(perm)
            self.assertEqual(F(sum_fixed, factorial(n)), 1)
            self.assertEqual(F(sum_fixed2, factorial(n))-1, 1)
            self.assertEqual(F(sum_cycles, factorial(n)),
                             sum((F(1,k) for k in range(1,n+1)), F(0)))
        cost = [F(0), F(0)]
        for n in range(2, 26):
            cost.append(F(n-1) + F(2,n)*sum(cost[:n]))
        for n in range(1, 26):
            harmonic = sum((F(1,k) for k in range(1,n+1)), F(0))
            self.assertEqual(cost[n], 2*(n+1)*harmonic-4*n)

    def test_coupon_collector_moments_from_one_step_recursion(self):
        for n in range(1, 11):
            mean, second = [F(0)]*(n+1), [F(0)]*(n+1)
            for k in range(n-1, -1, -1):
                p = F(n-k,n)
                q = 1-p
                mean[k] = 1/p + mean[k+1]
                second[k] = (1+2*(q*mean[k]+p*mean[k+1])+p*second[k+1])/p
            harmonic = sum((F(1,k) for k in range(1,n+1)), F(0))
            variance = n*n*sum((F(1,k*k) for k in range(1,n+1)),F(0))-n*harmonic
            self.assertEqual(mean[0], n*harmonic)
            self.assertEqual(second[0]-mean[0]**2, variance)

    def test_two_letter_huffman_coding_optimum_by_priority_queue(self):
        probs = [F(1,2), F(1,3), F(1,6)]
        heap = [x*y for x in probs for y in probs]
        heapq.heapify(heap)
        cost = F(0)
        while len(heap)>1:
            a, b = heapq.heappop(heap), heapq.heappop(heap)
            cost += a+b
            heapq.heappush(heap,a+b)
        self.assertEqual(cost, F(107,36))
        self.assertLess(cost/2, F(3,2))

    def test_three_state_markov_stationarity_exact_two_step_distance(self):
        p = [[F(1,2),F(1,2),F(0)],
             [F(1,3),F(1,3),F(1,3)],
             [F(0),F(1,2),F(1,2)]]
        pi = [F(2,7),F(3,7),F(2,7)]
        self.assertEqual([sum((pi[i]*p[i][j] for i in range(3)),F(0))
                          for j in range(3)], pi)
        row = [sum((p[0][i]*p[i][j] for i in range(3)),F(0))
               for j in range(3)]
        self.assertEqual(row,[F(5,12),F(5,12),F(1,6)])
        self.assertEqual(sum((abs(a-b) for a,b in zip(row,pi)),F(0))/2,F(11,84))

    def test_triangle_moments_by_exhausting_every_graph_on_five_vertices(self):
        for n in range(3, 6):
            edges = [(i,j) for i in range(n) for j in range(i+1,n)]
            lookup = {edge:k for k,edge in enumerate(edges)}
            triangles = [sum(1<<lookup[edge] for edge in ((i,j),(i,k),(j,k)))
                         for i in range(n) for j in range(i+1,n) for k in range(j+1,n)]
            first = second = 0
            for graph in range(1 << len(edges)):
                x = sum((graph & tri) == tri for tri in triangles)
                first += x
                second += x*x
            divisor = 1<<len(edges)
            self.assertEqual(F(first,divisor),F(comb(n,3),8))
            overlap = comb(n,2)*comb(n-2,2)
            expected = (F(comb(n,3),8)+F(2*overlap,32)
                        +F(2*(comb(comb(n,3),2)-overlap),64))
            self.assertEqual(F(second,divisor),expected)

    def test_binomial_thousand_coin_tail_ramsey_and_crossing_arithmetic(self):
        numerator = sum(comb(1000,k) for k in range(600,1001))
        with localcontext() as ctx:
            ctx.prec=48
            p=Decimal(numerator)/Decimal(2)**1000
            self.assertTrue(Decimal("1.3642e-10")<p<Decimal("1.3643e-10"))
        self.assertEqual([comb(n,7) for n in (27,28,33)],
                         [888030,1184040,4272048])
        self.assertEqual(F(33)-F(comb(33,7),2**20),F(1895685,65536))
        self.assertEqual(F(190**3,64*20**2), F(267)+F(119,128))


if __name__=="__main__":
    unittest.main()
