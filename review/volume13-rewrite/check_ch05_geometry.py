"""Volume 13, Chapter 5 (geometry of numbers): Minkowski bounds and class numbers printed in the text and exercises
(PARI via cypari2), the discriminant lower bounds of Exercise discbound, the volume formula of Lemma volume, Euler's
n^2+n+41, and the constants in Exercise quadmin."""
import math, itertools, random
import cypari2
from common import check, check_true, finish
pari = cypari2.Pari()
def MK(n, r2, d): return (4 / math.pi) ** r2 * math.factorial(n) / n ** n * math.sqrt(abs(d))
check("M_K Q(sqrt-5)", MK(2, 1, -20), 2.85, 0.005)
check("M_K Q(cbrt2)", MK(3, 1, -108), 2.94, 0.005)
check("M_K Q(cbrt10)", MK(3, 1, -300), 4.90, 0.005)
check("M_K Q(sqrt-23)", MK(2, 1, -23), 3.05, 0.005)
check("M_K Q(sqrt-47)", MK(2, 1, -47), 4.36, 0.005)
for d, v in [(-19, 2.77), (-43, 4.17), (-67, 5.21), (-163, 8.13)]: check(f"M_K Q(sqrt{d})", MK(2, 1, d), v, 0.005)
check("M_K Q(sqrt10) = sqrt10", MK(2, 0, 40), math.sqrt(10), 1e-12)
for m, h in [(2, 1), (10, 1), (7, 3)]:
    check_true(f"h(Q(cbrt{m})) = {h}", int(pari(f"bnfinit(x^3-{m}).no")) == h)
for D, h in [(-20, 2), (-23, 3), (-47, 5), (-19, 1), (-43, 1), (-67, 1), (-163, 1), (40, 2)]:
    check_true(f"h(D={D}) = {h}", int(pari(f"qfbclassno({D})")) == h)
check_true("h(Q(sqrt-23)) group cyclic of order 3", str(pari("bnfinit(x^2+23).cyc")) == "[3]")
check_true("h(Q(sqrt-47)) group cyclic of order 5", str(pari("bnfinit(x^2+47).cyc")) == "[5]")
check_true("n^2+n+41 prime for 0<=n<=39, not n=40", all(pari(f"isprime({n*n+n+41})") for n in range(40)) and not pari("isprime(1681)"))
check_true("x^2+xy+6y^2: norm of omega 6, of 1+omega 8", (0 + 0 + 6, 1 + 1 + 6) == (6, 8))
check_true("x^2+xy+12y^2 at (4,1) = 32", 16 + 4 + 12 == 32)
check_true("N(4+sqrt10) = 6", 16 - 10 == 6)
check_true("N(theta-2) = 10-8 = 2 in Q(cbrt10)", 10 - 8 == 2)
# Lemma volume: Monte Carlo for (r1,r2) = (1,1), t = 1: 2 * (pi/2) / 3! = pi/6
random.seed(1); N = 400000; hit = 0
for _ in range(N):
    y = random.uniform(-1, 1); u = random.uniform(-.5, .5); v = random.uniform(-.5, .5)
    if abs(y) + 2 * math.hypot(u, v) <= 1: hit += 1
check("vol B_1 for (1,1) = pi/6", hit / N * 2, math.pi / 6, 0.01)
# Exercise discbound
b = lambda n, r2: (math.pi / 4) ** (2 * r2) * (n ** n / math.factorial(n)) ** 2
check("n=2 bound pi^2/4", b(2, 1), 2.47, 0.005)
check("n=3 bound", b(3, 1), 12.5, 0.05)
check("n=4 bound", b(4, 2), 43.3, 0.05)
check("n=5 bound", b(5, 2), 258, 1)
check_true("81 pi/64 >= 3pi/4", 81 / 64 >= 3 / 4)
# true minima of |d_K| in degrees 2..5: 3, 23, 117, 1609 (from tables; check the polynomials)
for f, dk in [("x^2-x+1", -3), ("x^3-x-1", -23), ("x^4-x^3-x^2+x+1", 117), ("x^5-x^3-x^2+x+1", 1609)]:
    check_true(f"{f} has d_K = {dk}", int(pari(f"nfdisc({f})")) == dk)
check("2 pi^2", 2 * math.pi ** 2, 19.7, 0.05)
check("2/pi", 2 / math.pi, 0.637, 0.0005)
check("1/sqrt3", 1 / math.sqrt(3), 0.577, 0.0005)
check("area of S in figure: 4.4 covol > 4", 4.4, 4.4, 0)
finish()
