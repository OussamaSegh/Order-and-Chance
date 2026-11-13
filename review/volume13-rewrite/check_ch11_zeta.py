"""Volume 13, Chapter 11 (zeta functions): the opening series L(1,(./23)) = 3pi/sqrt23, sum of a(a/23) = -69, B_32,
h(Q(sqrt-p)) for p = 7, 23, 47, L(1,chi_8) and h(Q(sqrt2)) = 1, r_2(n), split densities, X^3-3X+1, the polynomial with
roots modulo every prime, the class number formula for small fields (PARI)."""
import math
import mpmath, sympy, cypari2
from common import check, check_true, finish
pari = cypari2.Pari()
leg = lambda a, p: sympy.legendre_symbol(a % p, p) if a % p else 0
signs = [leg(n, 23) for n in range(1, 11)]
check_true("signs of the opening series", signs == [1, 1, 1, 1, -1, 1, -1, 1, 1, -1])
L = float(pari("lfun(lfuncreate(-23),1)"))
check("L(1, chi_-23) = 3 pi / sqrt 23", L, 3 * math.pi / math.sqrt(23), 1e-12)
check_true("sum a (a/23) = -69", sum(a * leg(a, 23) for a in range(1, 23)) == -69)
check_true("B_32 = -7709321041217/510, 37 | numerator", sympy.bernoulli(32) == sympy.Rational(-7709321041217, 510) and 7709321041217 % 37 == 0)
for p, h in [(7, 1), (23, 3), (47, 5)]:
    check_true(f"h(Q(sqrt-{p})) = {h} = -(1/p) sum a(a/p)", -sum(a * leg(a, p) for a in range(1, p)) == p * h == p * int(pari(f"qfbclassno(-{p})")))
    small = sum(leg(a, p) for a in range(1, (p + 1) // 2))
    check_true(f"more residues than non-residues below {p}/2", small > 0)
L8 = float(pari("lfun(lfuncreate(8),1)"))
check("L(1,chi_8) = log(1+sqrt2)/sqrt2", L8, math.log(1 + math.sqrt(2)) / math.sqrt(2), 1e-12)
check("class number formula Q(sqrt2): 2^2 h R / (2 sqrt8) = L(1,chi_8) with h=1", 4 * math.log(1 + math.sqrt(2)) / (2 * math.sqrt(8)), L8, 1e-12)
r2 = lambda n: sum(1 for a in range(-int(n**.5) - 1, int(n**.5) + 2) for b in range(-int(n**.5) - 1, int(n**.5) + 2) if a*a + b*b == n)
chi4 = lambda d: 0 if d % 2 == 0 else (1 if d % 4 == 1 else -1)
check_true("r_2(n) = 4 sum chi_-4(d), n <= 300", all(r2(n) == 4 * sum(chi4(d) for d in sympy.divisors(n)) for n in range(1, 301)))
X = 200000
S = sum(1 for a in range(-448, 449) for b in range(-448, 449) if a*a + b*b <= X)
check("sum r_2(n), n<=x, over pi x (x=2e5)", (S - 1) / (math.pi * X), 1.0, 0.002)
# Q(cbrt2): primes splitting completely, density 1/6
ps = list(sympy.primerange(5, 200000))
spl = [p for p in ps if p % 3 == 1 and pow(2, (p - 1) // 3, p) == 1]
check("density of primes where X^3-2 has 3 roots (1/6)", len(spl) / len(ps), 1 / 6, 0.005)
# X^3-3X+1
def nroots(p): return sum(1 for x in range(p) if (x**3 - 3*x + 1) % p == 0)
ok = all((nroots(p) == 3) == (p % 9 in (1, 8)) and nroots(p) in (0, 3) for p in sympy.primerange(5, 3000))
check_true("X^3-3X+1: 3 roots iff p = +-1 mod 9, else 0", ok)
check_true("roots 2cos(2pi k/9)", all(abs((2*math.cos(2*math.pi*k/9))**3 - 3*2*math.cos(2*math.pi*k/9) + 1) < 1e-12 for k in (1, 2, 4)))
check_true("(X^2-2)(X^2-3)(X^2-6) has a root mod every prime < 5000",
           all(any(((x*x - 2) * (x*x - 3) * (x*x - 6)) % p == 0 for x in range(p)) for p in sympy.primerange(2, 5000)))
# residues at s=1 via PARI for Q(cbrt2), Q(zeta_5)
for pol in ["x^3-2", "polcyclo(5)", "x^2+23"]:
    bnf = pari(f"bnfinit({pol},1)")
    r1, r2_ = [int(t) for t in bnf.nf_get_sign()] if hasattr(bnf, 'nf_get_sign') else [int(t) for t in pari("(b)->b.sign")(bnf)]
    h = int(pari("(b)->b.no")(bnf)); R = float(pari("(b)->b.reg")(bnf)); w = int(pari("(b)->b.tu[1]")(bnf)); d = abs(int(pari("(b)->b.disc")(bnf)))
    res = 2**r1 * (2 * math.pi)**r2_ * h * R / (w * math.sqrt(d))
    lres = float(pari(f"(b)->lfun(lfuncreate(b), 1+1e-12)*1e-12")(bnf))
    check(f"class number formula residue for {pol}", res, lres, 1e-6)
finish()
