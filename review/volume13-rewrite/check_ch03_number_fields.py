"""Volume 13, Chapter 3 (number fields): discriminants of the polynomials and fields in the text and exercises,
the minimal polynomial of sqrt2 + cbrt2, the units of Z[cbrt2], Davenport-Heilbronn's constant."""
from sympy import symbols, discriminant, minimal_polynomial, sqrt, cbrt, Poly, isprime, factorint, Rational, zeta, N, cos, pi, expand, Matrix
from common import check, check_true, finish
X = symbols("X")
d = lambda f: discriminant(f, X)
check_true("disc X^3-2 = -108", d(X**3 - 2) == -108)
check_true("disc X^3-X-1 = -23", d(X**3 - X - 1) == -23)
check_true("disc X^3-3X+1 = 81", d(X**3 - 3*X + 1) == 81)
check_true("disc X^3+X+1 = -31", d(X**3 + X + 1) == -31)
check_true("disc X^3-10 = -2700", d(X**3 - 10) == -2700)
check_true("disc Dedekind cubic = -2012 = -4*503, 503 prime", d(X**3 - X**2 - 2*X - 8) == -2012 and isprime(503))
check_true("disc X^4-10X^2+1 = 147456 = 2304*64", d(X**4 - 10*X**2 + 1) == 147456 == 2304 * 64)
check_true("2304 = 2^8 3^2", factorint(2304) == {2: 8, 3: 2})
check_true("min poly sqrt2+cbrt2", minimal_polynomial(sqrt(2) + cbrt(2), X) == X**6 - 6*X**4 - 4*X**3 + 12*X**2 - 24*X - 4)
check_true("min poly of beta=(1+t+t^2)/3, t^3=10", minimal_polynomial((1 + cbrt(10) + cbrt(10)**2) / 3, X) == X**3 - X**2 - 3*X - 3)
check_true("min poly sqrt2+sqrt3", minimal_polynomial(sqrt(2) + sqrt(3), X) == X**4 - 10*X**2 + 1)
check_true("min poly 2cos(2pi/9)", minimal_polynomial(2 * cos(2 * pi / 9), X) == X**3 - 3*X + 1)
a, b, c = symbols("a b c")
M = Matrix([[a, 2*c, 2*b], [b, a, 2*c], [c, b, a]])
check_true("norm form of Q(cbrt2)", expand(M.det() - (a**3 + 2*b**3 + 4*c**3 - 6*a*b*c)) == 0)
nf = lambda a, b, c: a**3 + 2*b**3 + 4*c**3 - 6*a*b*c
check_true("(cbrt2-1)^3 = 1+3t-3t^2 has norm 1", nf(1, 3, -3) == 1 and nf(-1, 1, 0) == 1)
check("|cbrt2 - 1| = 0.26", float(2 ** (1 / 3) - 1), 0.26, 0.005)
q = [D for D in range(-15, 25) if D not in (0, 1) and (D % 4 == 1 and all(D % (p*p) for p in (3, 5, 7)) or D % 4 == 0 and (D // 4) % 4 in (2, 3) and all((D // 4) % (p*p) for p in (3, 5)))]
check_true(f"quadratic discriminants {q}", [x for x in q if x > 0][:7] == [5, 8, 12, 13, 17, 21, 24] and sorted([x for x in q if x < 0], reverse=True)[:6] == [-3, -4, -7, -8, -11, -15])
check("Davenport-Heilbronn 1/12+1/4 = 1/3", 1/12 + 1/4, 1/3, 1e-15)
# cbrt(m) index: squarefree m = +-1 mod 9 -> beta = (1 + m t + t^2)/3 type integral; check disc of field via sympy for a few
from sympy.polys.numberfields import round_two
from sympy import QQ
for m in [2, 3, 5, 6, 7, 10, 11, 17, 19, 26, 28]:
    if any(m % (p*p) == 0 for p in (2, 3, 5)): continue
    ZK, dK = round_two(Poly(X**3 - m, X, domain=QQ))
    idx2 = d(X**3 - m) // dK
    check_true(f"m={m}: index^2 = {idx2}, expected {'9' if m % 9 in (1, 8) else '1'}", idx2 == (9 if m % 9 in (1, 8) else 1))
ZK, dK = round_two(Poly(X**3 - X**2 - 2*X - 8, X, domain=QQ)); check_true("Dedekind field d_K = -503", dK == -503)
ZK, dK = round_two(Poly(X**4 - 10*X**2 + 1, X, domain=QQ)); check_true("Q(sqrt2,sqrt3) d_K = 2304", dK == 2304)
finish()
