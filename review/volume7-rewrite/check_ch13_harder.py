"""Number checks for Volume 7, Chapter 13 (Almost every number)."""
from fractions import Fraction
from math import log, sqrt, pi, exp, cos, floor
from common import check, check_true, finish

# Problem khinchin (b): c = 2 sum 1/(k sqrt(k+1))
N = 2_000_000
c = 2 * sum(1 / (k * sqrt(k + 1)) for k in range(1, N))
tail_hi = 2 * 2 / sqrt(N - 1)          # sum_{k>=N} k^{-3/2} <= 2/sqrt(N-1)
check("c (partial sum plus tail estimate 4/sqrt(N))", c + 4 / sqrt(N), 4.3680, 1e-4)
check_true("c < 4.4 with tail", c + tail_hi < 4.4)
check_true("(2c)^2 < 77 < e^5", (2 * (c + tail_hi)) ** 2 < 77 < exp(5))
check_true("e^5/(1-e^-5) < 150", exp(5) / (1 - exp(-5)) < 150)
check_true("log 150 < 6", log(150) < 6)
check("Levy constant", pi ** 2 / (12 * log(2)), 1.1866, 1e-4)

# law of a_n on a cylinder: lambda(a=k) = 1/(k(k+1)); lambda(a>=k) = 1/k
check_true("lambda(a_1=1)=1/2, quarter bound", Fraction(1, 2) * Fraction(1, 2) == Fraction(1, 4))

# bounded distortion on all cylinders of rank <= 6 with digits <= 6, B=(0,1/k)
import itertools
ok = True
for n in range(1, 5):
    for w in itertools.product(range(1, 6), repeat=n):
        pm, p_, qm, q_ = 1, 0, 0, 1   # p_{-1},p_0 ; q_{-1},q_0 for [0;...]
        for a in w:
            pm, p_ = p_, a * p_ + pm
            qm, q_ = q_, a * q_ + qm
        length = Fraction(1, q_ * (q_ + qm))
        ends = (Fraction(p_, q_), Fraction(p_ + pm, q_ + qm))
        ok &= abs(ends[0] - ends[1]) == length
        for k in range(1, 6):
            # psi((0,1/k)) has ends psi(0), psi(1/k)
            e2 = Fraction(k * p_ + pm, k * q_ + qm)
            ratio = abs(ends[0] - e2) / length
            ok &= Fraction(1, 2 * k) <= ratio <= Fraction(2, k)
check_true("cylinder length and 1/(2k) <= P(a_{n+1}>=k | I) <= 2/k", ok)

# Problem econt: digits of e, bounds on q_3k, the nine integer solutions
def e_digits(n):
    d = [2]
    k = 1
    while len(d) < n + 1:
        d += [1, 2 * k, 1]; k += 1
    return d[: n + 1]
d = e_digits(60)
ps, qs = [1, d[0]], [0, 1]
for a in d[1:]:
    ps.append(a * ps[-1] + ps[-2]); qs.append(a * qs[-1] + qs[-2])
ps, qs = ps[1:], qs[1:]
from math import factorial, e
ok = all(2 ** k * factorial(k) <= qs[3 * k] <= 3 ** (3 * k) * factorial(k + 1) for k in range(1, 20))
check_true("2^k k! <= q_3k <= 3^3k (k+1)!", ok)
check_true("digits of e: a_m <= (2m+2)/3", all(3 * d[m] <= 2 * m + 2 for m in range(1, 60)))
from decimal import Decimal, getcontext
getcontext().prec = 80
E = Decimal(1).exp()
sols = []
for q in range(2, 8):
    center = E * q
    for p in range(int(center) - 3, int(center) + 4):
        if abs(E - Decimal(p) / q) < 1 / (Decimal(q) ** 2 * Decimal(q).ln()): sols.append((p, q))
for p, q in zip(ps, qs):
    if q >= 8 and abs(E - Decimal(p) / q) < 1 / (Decimal(q) ** 2 * Decimal(q).ln()): sols.append((p, q))
printed = [(5, 2), (6, 2), (8, 3), (11, 4), (19, 7), (193, 71), (2721, 1001), (49171, 18089), (1084483, 398959)]
check_true(f"nine solutions for e: {sols}", sols == printed)

# Problem etwo
phi = (1 + sqrt(5)) / 2
check("log2/(2 log phi)", log(2) / (2 * log(phi)), 0.7202, 1e-4)
check("log2/(2 log(1+sqrt2))", log(2) / (2 * log(1 + sqrt(2))), 0.3932, 1e-4)
al, be = (sqrt(3) - 1) / 2, sqrt(3) - 1
check_true("alpha root", abs(2 * al * al + 2 * al - 1) < 1e-12 and abs(be - 1 / (1 + al)) < 1e-12)
check("gap g", 1 / (1 + be) - 1 / (2 + al), 2 / sqrt(3) - 1, 1e-12)
check("gap g printed", 2 / sqrt(3) - 1, 0.1547, 1e-4)
check_true("J1,J2 ends", abs(1 / (1 + be) - 1 / sqrt(3)) < 1e-12 and abs(1 / (2 + al) - (1 - 1 / sqrt(3))) < 1e-12 and abs(1/(2+be) - al) < 1e-12)

# Problem eggleston
H = lambda p: -p * log(p) - (1 - p) * log(1 - p)
check("dim B_1/3", H(1 / 3) / log(2), 0.9182, 1e-4)
check("dim B_1/3 closed form", H(1 / 3) / log(2), log(3) / log(2) - 2 / 3, 1e-12)
check("H(1/3)", H(1 / 3), 0.6365, 1e-4)
check("log 2", log(2), 0.6931, 1e-4)

# Problem cantorfourier
prod = 1.0
for k in range(1, 60): prod *= cos(2 * pi * 3.0 ** -k)
check("|mu^(1)|", abs(prod), 0.37143, 1e-5)

# Problem similar (b)
check("measure of A >= 1/3", 1 - sum(2 * 4.0 ** -n for n in range(1, 60)), 1 / 3, 1e-12)
# Problem del: c_rho ; koksma lemma constants are symbolic
finish()
