"""Volume 13, Chapter 17 (modular forms): j expansion, e^{pi sqrt 163}, T_2 on S_24, Delta*E_4 coefficients, the level-11 form
against y^2+y=x^3-x^2 (table and all p<10^5), L(E,1), torsion, first zeros, Chudnovsky digits."""
import cypari2, mpmath
from common import check, check_true, finish
pari = cypari2.Pari(); pari.allocatemem(4 * 10**8, silent=True)
pari.default("seriesprecision", 12)

j = [int(x) for x in pari("Vec((1+240*sum(n=1,6,sigma(n,3)*x^n)+O(x^6))^3/(eta(x+O(x^6))^24))")]
check_true("j = 1/q+744+196884q+21493760q^2", j[:4] == [1, 744, 196884, 21493760])
mpmath.mp.dps = 60
d = mpmath.e ** (mpmath.pi * mpmath.sqrt(163)) - (640320 ** 3 + 744)
check_true("e^{pi sqrt163} within 1e-12 of 640320^3+744", abs(d) < 1e-12)
check("j((1+sqrt-163)/2) = -640320^3 (Hilbert class polynomial x - j)", -int(pari("polcoef(polclass(-163),0)")), -640320 ** 3, 0)

# T_2 on S_24
mf = pari("mfinit([1,24],1)")
P = pari(f"charpoly(mfheckemat({mf},2))")
check_true("charpoly T_2 on S_24 = x^2-1080x-20468736", P == pari("x^2-1080*x-20468736"))
check("disc", int(pari.poldisc(P)), 2 ** 6 * 3 ** 2 * 144169, 0)
check_true("144169 squarefree, not square", pari.issquarefree(144169) and not pari.issquare(144169))

# Delta*E_4
DE4 = [int(x) for x in pari("Vec(x*eta(x+O(x^8))^24*(1+240*sum(n=1,7,sigma(n,3)*x^n)+O(x^8)))")]
check_true("Delta E_4 = q+216q^2-3348q^3+13888q^4+52110q^5-723168q^6", DE4[:6] == [1, 216, -3348, 13888, 52110, -723168])
check_true("c6=c2c3, c4=c2^2-2^15", DE4[5] == DE4[1] * DE4[2] and DE4[3] == DE4[1] ** 2 - 2 ** 15)

# level 11
E = pari.ellinit([0, -1, 1, 0, 0])
check("disc E", int(pari("ellinit([0,-1,1,0,0]).disc")), -11, 0)
tab = {2: 5, 3: 5, 5: 5, 7: 10, 13: 10, 17: 20, 19: 20, 23: 25, 29: 30, 31: 25}
for p, N in tab.items():
    check(f"N_{p}", p + 1 - int(pari.ellap(E, p)), N, 0)
B = 10 ** 5
pari.default("seriesprecision", B + 5)
f = pari(f"Vec(x*eta(x+O(x^{B}))^2*eta(x^11+O(x^{B}))^2)")
bad = [p for p in pari.primes(pari.primepi(B - 1)) if int(p) != 11 and int(f[int(p) - 1]) != int(pari.ellap(E, p))]
check("primes p<10^5, p!=11, with a_p != c_p", len(bad), 0, 0)
check("L(E,1)", round(float(pari.lfun(E, 1)), 4), 0.2538, 0)
check("torsion order", int(pari.elltors(E)[0]), 5, 0)
check_true("(0,0) has order 5", int(pari.ellorder(E, [0, 0])) == 5)
z1 = float(pari("lfunzeros(lfuncreate(ellinit([0,-1,1,0,0])),[0,7])")[0])
check("first zero of L(f,s)", round(z1, 4), 6.3626, 0)
zD = float(pari("lfunzeros(lfunmf(mfinit([1,12],1),mfDelta()),[0,10])")[0])
check("first zero of L(Delta,s) (centre 6)", round(zD, 4), 9.2224, 0)
# Chudnovsky: 10^5 digits of pi from the series built on j((1+sqrt-163)/2) = -640320^3
def bs(a, b):
    if b - a == 1:
        P = Q = 1 if a == 0 else None
        if a: P, Q = (6 * a - 5) * (2 * a - 1) * (6 * a - 1), a ** 3 * (640320 ** 3 // 24)
        T = P * (13591409 + 545140134 * a)
        return P, Q, (-T if a & 1 else T)
    m = (a + b) // 2
    P1, Q1, T1 = bs(a, m); P2, Q2, T2 = bs(m, b)
    return P1 * P2, Q1 * Q2, Q2 * T1 + P1 * T2
D = 10 ** 5
_, Q, T = bs(0, D // 14 + 2)
mpmath.mp.dps = D + 20
check_true("Chudnovsky series gives 10^5 digits of pi", abs(426880 * mpmath.sqrt(10005) * Q / T - mpmath.pi) < mpmath.mpf(10) ** (-D))
finish()
