"""Finite independent certificates for final-chapter primality exercises."""

import math
import unittest

from tools.test_volume2_ch06_carmichael_pratt import factors


def primes_to(limit):
    return [n for n in range(2, limit+1) if factors(n) == {n: 1}]


def order(a, modulus, exponent):
    e = exponent
    for q in factors(exponent):
        while e % q == 0 and pow(a, e//q, modulus) == 1:
            e //= q
    return e


def quotient(a, p):
    # Only the residue modulo p is needed; avoid unnecessarily huge powers.
    return (pow(a, p-1, p*p)-1)//p


class CertificateChecks(unittest.TestCase):
    def test_pseudoprime_constructions(self):
        self.assertEqual(factors(341), {11: 1, 31: 1})
        self.assertEqual(pow(2, 340, 341), 1)
        for n in (341, 561, 645):
            self.assertEqual(pow(2, n-1, n), 1)
            m = 2**n-1
            a = min(factors(n))
            self.assertEqual(m % (2**a-1), 0)
            self.assertGreater(m, 2**a-1)
            self.assertEqual(pow(2, m-1, m), 1)
        for p in primes_to(47)[2:]:
            N = (4**p-1)//3
            self.assertEqual(N, (2**p-1)*((2**p+1)//3))
            self.assertEqual((N-1) % (2*p), 0)
            self.assertEqual(pow(2, N-1, N), 1)

    def test_partial_factor_and_proth_certificates(self):
        for n in range(2, 401):
            divisors = [F for F in range(1, n) if (n-1) % F == 0]
            for a in range(2, min(n, 18)):
                if pow(a, n-1, n) != 1:
                    continue
                for F in divisors:
                    if all(math.gcd(pow(a, (n-1)//q, n)-1, n) == 1 for q in factors(F)):
                        self.assertTrue(all((p-1) % F == 0 for p in factors(n)))
                        if F*F > n:
                            self.assertEqual(factors(n), {n: 1})
        self.assertEqual(pow(3, 1664, 3329), 3328)
        self.assertEqual(factors(3329), {3329: 1})
        self.assertEqual([pow(3, 2**j, 3329) for j in range(11)],
                         [3, 9, 81, 3232, 2751, 1184, 347, 565, 2970, 2379, 341])

    def test_fermat_quotient_identities(self):
        for p in primes_to(43)[1:]:
            for a in range(1, p):
                for b in range(1, p):
                    self.assertEqual((quotient(a*b, p)-quotient(a, p)-quotient(b, p)) % p, 0)
                for t in range(-2, 3):
                    self.assertEqual((quotient(a+p*t, p)-quotient(a, p)+t*pow(a, -1, p)) % p, 0)
            alternating = sum((-1)**(k-1)*pow(k, -1, p) for k in range(1, p)) % p
            self.assertEqual(2*quotient(2, p) % p, alternating)
            W = (math.factorial(p-1)+1)//p
            self.assertEqual(sum(quotient(a, p) for a in range(1, p)) % p, W % p)
        for p in primes_to(101)[1:] + [1093, 3511]:
            e = order(2, p, p-1)
            E = order(2, p*p, p*(p-1))
            self.assertIn(E, (e, p*e))
            self.assertEqual(pow(2, p-1, p*p) == 1, e == E)


if __name__ == '__main__':
    unittest.main()
