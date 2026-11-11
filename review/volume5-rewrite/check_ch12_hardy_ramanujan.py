"""Numerical checks for Volume 5, Chapter 12 (The Hardy-Ramanujan Formula).

Run: python3 review/volume5-rewrite/check_ch12_hardy_ramanujan.py
Every number printed in the chapter that is not proved on the page is recomputed here.
"""
from fractions import Fraction
from math import gcd
import mpmath as mp

mp.mp.dps = 40


def partitions(N):
    """p(0..N) by Euler's pentagonal recurrence (exact integers)."""
    p = [1] + [0] * N
    for n in range(1, N + 1):
        s, k = 0, 1
        while True:
            g1, g2 = k * (3 * k - 1) // 2, k * (3 * k + 1) // 2
            if g1 > n:
                break
            sign = 1 if k % 2 else -1
            s += sign * p[n - g1]
            if g2 <= n:
                s += sign * p[n - g2]
            k += 1
        p[n] = s
    return p


def eta_product(tau, terms=400):
    q = mp.exp(2j * mp.pi * tau)
    out = mp.exp(1j * mp.pi * tau / 12)
    for m in range(1, terms):
        out *= 1 - q ** m
    return out


def eta_series(tau, J=60):
    return mp.fsum((-1) ** j * mp.exp(1j * mp.pi * tau * (6 * j - 1) ** 2 / 12) for j in range(-J, J + 1))


def dedekind_s(h, k):
    return sum(Fraction(r, k) * (Fraction((h * r) % k, k) - Fraction(1, 2)) for r in range(1, k))


def rademacher(n, K):
    x = mp.mpf(n) - mp.mpf(1) / 24
    f = lambda v, k: mp.sinh(mp.pi / k * mp.sqrt(mp.mpf(2) / 3 * v)) / mp.sqrt(v)
    total = 0
    for k in range(1, K + 1):
        A = mp.fsum(mp.exp(1j * mp.pi * (mp.mpf(dedekind_s(h, k).numerator) / dedekind_s(h, k).denominator)
                           - 2j * mp.pi * n * h / k)
                    for h in range(k) if gcd(h, k) == 1)
        total += A.real * mp.sqrt(k) * mp.diff(lambda v: f(v, k), x)
    return total / (mp.pi * mp.sqrt(2))


def main():
    p = partitions(5000)
    assert p[4] == 5 and p[100] == 190569292 and p[200] == 3972999029388
    print("p(100) =", p[100], " p(200) =", p[200], " digits:", len(str(p[200])))

    # eta: product = theta series, and the transformation at three points off the imaginary axis too
    for tau in (mp.mpc(0, 1.3), mp.mpc(0.3, 0.7), mp.mpc(-0.45, 0.25)):
        e1, e2 = eta_product(tau), eta_series(tau)
        lhs = eta_series(-1 / tau)
        rhs = mp.sqrt(-1j * tau) * e2
        print("tau =", tau, "|product-series| =", mp.nstr(abs(e1 - e2), 3),
              "|eta(-1/tau)-sqrt(-i tau) eta(tau)| =", mp.nstr(abs(lhs - rhs), 3))
        assert abs(e1 - e2) < mp.mpf(10) ** -30 and abs(lhs - rhs) < mp.mpf(10) ** -30

    # cos(pi |6j-1| / 6) = (-1)^j sqrt(3)/2
    for j in range(-20, 21):
        assert abs(mp.cos(mp.pi * abs(6 * j - 1) / 6) - (-1) ** j * mp.sqrt(3) / 2) < mp.mpf(10) ** -30

    # Lemma (transformation of P) at t = 0.01
    P = lambda x: 1 / mp.nprod(lambda m: 1 - x ** m, [1, mp.inf])
    t = mp.mpf("0.01")
    direct = mp.exp(mp.fsum(1 / (m * (mp.exp(m * t) - 1)) for m in range(1, 20000)))
    via = mp.sqrt(t / (2 * mp.pi)) * mp.exp(mp.pi ** 2 / (6 * t) - t / 24)
    print("P(e^-0.01): direct", mp.nstr(direct, 12), "via lemma", mp.nstr(via, 12), " 4pi^2/t =", mp.nstr(4 * mp.pi ** 2 / t, 6))

    # the asymptotic and the ratio
    C = mp.pi * mp.sqrt(mp.mpf(2) / 3)
    hr = lambda n: mp.exp(C * mp.sqrt(n)) / (4 * mp.sqrt(3) * n)
    for n in (10, 100, 200, 1000, 5000):
        print("n =", n, " HR =", mp.nstr(hr(n), 10), " ratio p/HR =", mp.nstr(p[n] / hr(n), 5),
              " sqrt(n)(1-ratio) =", mp.nstr(mp.sqrt(n) * (1 - p[n] / hr(n)), 4))
    print("1/C + C/48 =", mp.nstr(1 / C + C / 48, 5))

    # constants in the proof
    a = mp.mpf(3)
    bound = 12 / a + 2 * mp.exp(-12 * a) * mp.sqrt(2 * mp.pi / a) + 3 * mp.sqrt(2 * mp.pi) / a ** 1.5 + mp.exp(-a) / a
    print("major-arc error bound at a=3:", mp.nstr(bound, 5), "<= 20/a =", mp.nstr(20 / a, 5))
    assert bound <= 20 / a
    r = mp.exp(-mp.pi / 10)
    print("r >=", mp.nstr(r, 5), " (1+4r/pi^2)^(-1/2) at r=0.73:", mp.nstr((1 + 4 * 0.73 / mp.pi ** 2) ** -0.5, 5),
          " gain constant:", mp.nstr(0.73 * 0.121 / (2 * mp.pi), 5), "> 1/80 =", 1 / 80)
    N17 = 17 - mp.mpf(1) / 24
    print("n=17: 1/y =", mp.nstr(mp.sqrt(24 * N17), 6), " a =", mp.nstr(mp.pi * mp.sqrt(N17 / 6), 6))
    # the minor arc inequality, sampled
    for y in (mp.mpf(1) / 20, mp.mpf(1) / 50, mp.mpf(1) / 300):
        rr = mp.exp(-2 * mp.pi * y)
        worst = min(rr / (1 - rr) - rr / abs(1 - rr * mp.exp(2j * mp.pi * x)) - 1 / (80 * y)
                    for x in mp.linspace(y, 0.5, 400))
        assert worst > 0

    # Rademacher partial sums at n = 200
    for K in (1, 2, 3, 5, 8):
        print("Rademacher, n=200,", K, "terms: error", mp.nstr(rademacher(200, K) - p[200], 4))

    # heights of the peaks of log|P| at r = 0.99
    r = mp.mpf("0.99")
    logP = lambda z: mp.fsum((z ** m / (m * (1 - z ** m))).real for m in range(1, 6000))
    base = logP(r)
    print("log P(0.99) =", mp.nstr(base, 6), " peaks:",
          [mp.nstr(logP(r * mp.exp(2j * mp.pi / k)) / base, 3) for k in (2, 3, 4, 5)])

    # congruences
    assert all(p[5 * m + 4] % 5 == 0 for m in range(999))
    assert all(p[7 * m + 5] % 7 == 0 for m in range(713))
    assert all(p[11 * m + 6] % 11 == 0 for m in range(454))
    print("Ramanujan congruences mod 5, 7, 11 hold for all n <= 5000")

    # exercises
    n = 1000
    print("saddle bound / p(1000) =", mp.nstr(2 * (24 * n) ** -0.25 * mp.exp(C * mp.sqrt(n)) / p[n], 5), " 1000^(3/4) =", mp.nstr(mp.mpf(n) ** 0.75, 4))
    print("average number of ones, n=1000:", mp.nstr(mp.mpf(sum(p[n - k] for k in range(1, n + 1))) / p[n], 5), " sqrt(6n)/pi =", mp.nstr(mp.sqrt(6 * n) / mp.pi, 5))
    q = [1] + [0] * 1000
    for part in range(1, 1001):
        for m in range(1000, part - 1, -1):
            q[m] += q[m - part]
    qa = mp.exp(mp.pi * mp.sqrt(mp.mpf(n) / 3)) / (4 * mp.mpf(3) ** 0.25 * mp.mpf(n) ** 0.75)
    print("q(1000) =", q[1000], " ratio to asymptotic:", mp.nstr(q[1000] / qa, 5))
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
