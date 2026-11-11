"""Numerical checks for Volume 5, Chapter 1 (Finite Calculus).
Run: python3 review/volume5-rewrite/check_ch01_finite.py"""
from fractions import Fraction as F
from math import comb, factorial, exp
from itertools import permutations
from sympy import bernoulli, isprime, harmonic, Rational

def S2(n, k, memo={}):
    if n == k: return 1
    if k == 0 or k > n: return 0
    if (n, k) not in memo: memo[(n, k)] = k * S2(n - 1, k) + S2(n - 1, k - 1)
    return memo[(n, k)]

def S1(n, k, memo={}):
    if n == k: return 1
    if k == 0 or k > n: return 0
    if (n, k) not in memo: memo[(n, k)] = (n - 1) * S1(n - 1, k) + S1(n - 1, k - 1)
    return memo[(n, k)]

def B(n):  # convention B_1 = -1/2
    b = bernoulli(n)
    return -b if n == 1 and b > 0 else b

def main():
    assert sum(k ** 10 for k in range(1, 1001)) == 91409924241424243424241924242500
    assert sum(k ** 5 for k in range(1000)) == 166167083333250000
    n = 1000
    assert F(n**6, 6) - F(n**5, 2) + F(5 * n**4, 12) - F(n**2, 12) == 166167083333250000
    assert [S2(6, k) for k in range(1, 7)] == [1, 31, 90, 65, 15, 1]
    assert [S2(5, k) for k in range(1, 6)] == [1, 15, 25, 10, 1] and S2(4, 2) == 7
    assert [S1(6, k) for k in range(1, 7)] == [120, 274, 225, 85, 15, 1]
    assert [S1(5, k) for k in range(1, 6)] == [24, 50, 35, 10, 1] and S1(4, 2) == 11
    assert [B(k) for k in (1, 2, 4, 6, 8, 10, 12)] == [Rational(-1, 2), Rational(1, 6), Rational(-1, 30), Rational(1, 42), Rational(-1, 30), Rational(5, 66), Rational(-691, 2730)]
    # worked examples
    for n in range(1, 12):
        assert sum(k * 2**k for k in range(n)) == (n - 2) * 2**n + 2
        assert sum(harmonic(k) for k in range(n)) == n * harmonic(n) - n
        assert sum(k * k * 2**k for k in range(n + 1)) == (n * n - 2 * n + 3) * 2**(n + 1) - 6
        assert sum(F(1, k * (k + 1) * (k + 2)) for k in range(1, n + 1)) == F(1, 4) - F(1, 2 * (n + 1) * (n + 2))
        assert sum(k * harmonic(k) for k in range(n)) == Rational(n * (n - 1), 2) * (harmonic(n) - Rational(1, 2))
        assert sum(k**2 for k in range(n)) == F((n - 1) * n * (2 * n - 1), 6)
        assert sum(k**3 for k in range(n)) == (n * (n - 1) // 2) ** 2
    # von Staudt-Clausen and the formula B_m = sum (-1)^k k!/(k+1) S2(m,k)
    for m in range(1, 31):
        assert sum(F((-1)**k * factorial(k), k + 1) * S2(m, k) for k in range(0, m + 1)) == F(int(B(m).p), int(B(m).q))
    for m in range(2, 41, 2):
        t = F(int(B(m).p), int(B(m).q)) + sum(F(1, p) for p in range(2, m + 2) if isprime(p) and m % (p - 1) == 0)
        assert t.denominator == 1
    assert F(1, 6) + F(1, 2) + F(1, 3) == 1
    assert F(-691, 2730) + F(1, 2) + F(1, 3) + F(1, 5) + F(1, 7) + F(1, 13) == 1
    # difference table of x^3+x+1
    f = lambda x: x**3 + x + 1
    assert [f(x) for x in range(6)] == [1, 3, 11, 31, 69, 131]
    # sums of powers mod p
    for p in (2, 3, 5, 7, 11, 13):
        for m in range(1, 30):
            assert sum(pow(k, m, p) for k in range(1, p)) % p == ((-1) % p if m % (p - 1) == 0 else 0)
    # 6 S(m,3) = 3^m - 3*2^m + 3 and S(m,3) even for even m
    for m in range(2, 30):
        assert 6 * S2(m, 3) == 3**m - 3 * 2**m + 3 and (m % 2 or S2(m, 3) % 2 == 0)
    print("ALL CHECKS PASSED")

if __name__ == "__main__":
    main()
