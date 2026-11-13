"""Volume 13, Chapter 6 (units): Pell for 61, regulators of Q(sqrt2), Q(sqrt61), Q(cbrt2) and the cyclic cubic of
conductor 7 (PARI), Artin's bound for Q(cbrt2), the powers of 1+cbrt2+cbrt4 in Exercise thue."""
import math
import cypari2
from fractions import Fraction as F
from common import check, check_true, finish
pari = cypari2.Pari()
check_true("1766319049^2 - 61*226153980^2 = 1", 1766319049**2 - 61 * 226153980**2 == 1)
e = (F(39, 2), F(5, 2))
mul = lambda a, b: (a[0]*b[0] + 61*a[1]*b[1], a[0]*b[1] + a[1]*b[0])
e3 = mul(mul(e, e), e); e6 = mul(e3, e3)
check_true("eps^3 = 29718 + 3805 sqrt61", e3 == (29718, 3805))
check_true("eps^6 = 1766319049 + 226153980 sqrt61", e6 == (1766319049, 226153980))
check_true("N(eps) = -1", e[0]**2 - 61*e[1]**2 == -1)
check("fundamental unit of Q(sqrt61): PARI regulator = log eps", float(pari("quadregulator(61)")), math.log((39 + 5 * 61**0.5) / 2), 1e-12)
check("R(Q(sqrt2))", math.log(1 + 2**0.5), 0.881, 0.0005)
check("R(Q(sqrt61))", math.log((39 + 5 * 61**0.5) / 2), 3.664, 0.0005)
check("R(Q(cbrt2)) = log(1+cbrt2+cbrt4)", math.log(1 + 2**(1/3) + 4**(1/3)), 1.3474, 0.00006)
check("PARI regulator Q(cbrt2)", float(pari("bnfinit(x^3-2).reg")), 1.3474, 0.0001)
check("eps(cbrt2) = 3.847", 1 + 2**(1/3) + 4**(1/3), 3.847, 0.0005)
check("Artin: eta > 2.63", ((108 - 35) / 4) ** (1/3), 2.63, 0.005)
check_true("eta^2 > 6.9 > eps", 2.633**2 > 6.9 > 3.847)
R7 = float(pari("bnfinit(x^3+x^2-2*x-1).reg"))
check("regulator cyclic cubic conductor 7", R7, 0.5255, 0.00006)
check("sqrt3 * R = 0.910", 3**0.5 * R7, 0.910, 0.0005)
t = 2 * math.cos(2 * math.pi / 7); t2 = 2 * math.cos(4 * math.pi / 7)
det = math.log(abs(t)) * math.log(abs(1 + t2)) - math.log(abs(t2)) * math.log(abs(1 + t))
check("determinant in Exercise cyclic7", abs(det), 0.5255, 0.00006)
check("theta, theta2, theta3", t, 1.2470, 0.00005); check("theta2", t2, -0.4450, 0.00005); check("theta3", 2*math.cos(6*math.pi/7), -1.8019, 0.00005)
# Thue powers in Z[cbrt2]
def m3(a, b):  # (a0,a1,a2)*(b0,b1,b2), t^3 = 2
    c = [0]*5
    for i in range(3):
        for j in range(3): c[i+j] += a[i]*b[j]
    return (c[0] + 2*c[3], c[1] + 2*c[4], c[2])
E = (1, 1, 1); Ei = (-1, 1, 0)
check_true("eps * eps^-1 = 1", m3(E, Ei) == (1, 0, 0))
check_true("eps^2 = 5+4t+3t^2", m3(E, E) == (5, 4, 3))
check_true("eps^3 = 19+15t+12t^2", m3(m3(E, E), E) == (19, 15, 12))
check_true("eps^-2 = 1-2t+t^2", m3(Ei, Ei) == (1, -2, 1))
check_true("eps^-3 = 1+3t-3t^2", m3(m3(Ei, Ei), Ei) == (1, 3, -3))
check_true("x^3-2y^3=1: only (1,0),(-1,-1) for |x|,|y|<=1000", sorted((x, y) for x in range(-1000, 1001) for y in [round(((x**3 - 1) / 2) ** (1/3)) if x**3 >= 1 else -round(((1 - x**3) / 2) ** (1/3))] if x**3 - 2*y**3 == 1) == [(-1, -1), (1, 0)])
# Exercise unitbound: d = a^2+4, a odd -> equality; R >= 1/2 log d - 10/(3d)
for d in [5, 8, 12, 13, 17, 21, 24, 28, 29, 33, 37, 40, 41, 44, 53, 56, 57, 60, 61, 65, 69, 73, 76, 77, 85, 88, 89, 92, 93, 97]:
    R = float(pari(f"quadregulator({d})"))
    check_true(f"d={d}: R={R:.4f} >= bound", R >= 0.5 * math.log(d) - 10 / (3 * d) - 1e-12)
finish()
