"""Volume 13, Chapter 1 (quadratic fields): fundamental units and Pell solutions printed in the text and the exercises,
the Fibonacci parity of Exercise goldenunit, and the d mod 8 claim of Exercise t1-cube."""
import math
from common import check, check_true, finish

def fund_unit(d):
    """least unit > 1 of the ring of integers of Q(sqrt d), as (2x, 2y) with x + y sqrt d."""
    half = d % 4 == 1
    for k in range(1, 10**6):          # k = 2y (half) or y
        for sgn in (-1, 1):
            if half:
                m2 = d * k * k + 4 * sgn
                m = math.isqrt(m2) if m2 > 0 else -1
                if m > 0 and m * m == m2 and (m - k) % 2 == 0:
                    return (m, k, sgn)
            else:
                x2 = d * k * k + sgn
                x = math.isqrt(x2) if x2 > 0 else -1
                if x > 0 and x * x == x2:
                    return (2 * x, 2 * k, sgn)
check_true("d=2: 1+sqrt2, norm -1", fund_unit(2) == (2, 2, -1))
check_true("d=5: golden ratio, norm -1", fund_unit(5) == (1, 1, -1))
check_true("d=13: (3+sqrt13)/2, norm -1", fund_unit(13) == (3, 1, -1))
check_true("d=3: 2+sqrt3, norm 1", fund_unit(3) == (4, 2, 1))
check_true("d=6: 5+2sqrt6, norm 1", fund_unit(6) == (10, 4, 1))
check_true("d=34: 35+6sqrt34, norm 1", fund_unit(34) == (70, 12, 1))

def mul(a, b, d):  # (x, y) = x + y sqrt d with rationals as fractions of 2
    from fractions import Fraction as F
    return (a[0] * b[0] + d * a[1] * b[1], a[0] * b[1] + a[1] * b[0])
from fractions import Fraction as F
e = (F(3, 2), F(1, 2))
e3 = mul(mul(e, e, 13), e, 13); e6 = mul(e3, e3, 13)
check_true("eps^3 = 18 + 5 sqrt13", e3 == (18, 5))
check_true("eps^6 = 649 + 180 sqrt13", e6 == (649, 180) and 649**2 - 13 * 180**2 == 1)
check_true("least Pell solution d=13 is (649,180)", all(math.isqrt(13 * y * y + 1) ** 2 != 13 * y * y + 1 for y in range(1, 180)))
check_true("2^2-5=-1, 9^2-5*4^2=1, 38^2-5*17^2=-1", (4 - 5, 81 - 80, 38**2 - 5 * 17**2) == (-1, 1, -1))
fib = [0, 1]
for _ in range(60): fib.append(fib[-1] + fib[-2])
check_true("F_n even iff 3|n", all((fib[n] % 2 == 0) == (n % 3 == 0) for n in range(60)))
check_true("phi^3 = 2 + sqrt5", mul(mul((F(1,2),F(1,2)),(F(1,2),F(1,2)),5),(F(1,2),F(1,2)),5) == (2, 1))
# Exercise t1-cube: eps^3 in Z[sqrt d] for d = 1 mod 4; eps in Z[sqrt d] when d = 1 mod 8
for d in [5, 13, 17, 21, 29, 33, 37, 41, 53, 57, 61, 65, 69, 73, 77, 89, 93, 97]:
    if any(d % (q * q) == 0 for q in range(2, 10)): continue
    m, k, _ = fund_unit(d)
    e = (F(m, 2), F(k, 2))
    c3 = mul(mul(e, e, d), e, d)
    check_true(f"d={d}: eps^3 integral coords", c3[0].denominator == 1 and c3[1].denominator == 1)
    if d % 8 == 1:
        check_true(f"d={d} = 1 mod 8: eps itself in Z[sqrt d]", k % 2 == 0)
# matrices
check_true("det [[1,-5],[1,1]] = 6", 1 * 1 - (-5) * 1 == 6)
check_true("det [[1,2],[1,1]] = -1", 1 - 2 == -1)
finish()
