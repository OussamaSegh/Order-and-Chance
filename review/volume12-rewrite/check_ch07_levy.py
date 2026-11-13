"""Chapter 7 numbers: half-stable subordinator, gamma subordinator, excursion counts."""
import mpmath as mp
from common import check, check_true, finish

lam = mp.mpf('1.7')
# int_0^inf (1-e^{-lam x}) x^{-3/2} dx = 2 sqrt(pi lam)
I = mp.quad(lambda x: (1 - mp.e**(-lam*x)) * x**mp.mpf(-1.5), [0, 1, mp.inf])
check("int (1-e^{-lx}) x^{-3/2}", I, 2*mp.sqrt(mp.pi*lam), 1e-7)
# Phi(lam) = sqrt(2 lam) with Pi = dx/(sqrt(2pi) x^{3/2})
check("Laplace exponent", I/mp.sqrt(2*mp.pi), mp.sqrt(2*lam), 1e-7)
# Pi(]x,inf[) = sqrt(2/(pi x))
x = mp.mpf('0.3')
tail = mp.quad(lambda y: 1/(mp.sqrt(2*mp.pi)*y**mp.mpf(1.5)), [x, mp.inf])
check("tail of Pi", tail, mp.sqrt(2/(mp.pi*x)), 1e-7)
# E e^{-lam T_a} = e^{-a sqrt(2 lam)}: hitting density a/sqrt(2 pi t^3) e^{-a^2/2t}
a = mp.mpf('0.8')
L = mp.quad(lambda t: a/mp.sqrt(2*mp.pi*t**3)*mp.e**(-a*a/(2*t) - lam*t), [0, 1, mp.inf])
check("Laplace of T_a", L, mp.e**(-a*mp.sqrt(2*lam)), 1e-7)
# Gamma subordinator: int (1-e^{-lam x}) e^{-x}/x dx = log(1+lam)
G = mp.quad(lambda y: (1 - mp.e**(-lam*y))*mp.e**(-y)/y, [0, 1, mp.inf])
check("gamma Laplace exponent", G, mp.log(1+lam), 1e-7)
# Poisson process triple: psi = i lam xi + lam(e^{i xi}-1-i xi) = lam(e^{i xi}-1)
xi = mp.mpf('0.9'); r = mp.mpf(2)
psi = 1j*r*xi + r*(mp.e**(1j*xi) - 1 - 1j*xi)
check("Poisson exponent", abs(psi - r*(mp.e**(1j*xi)-1)), 0, 1e-7)
# E J^beta finite iff beta<1/2: P(J>x) ~ sqrt(2/pi) x^{-1/2}
X = mp.mpf(10)**8
check("tail of J", (1-mp.e**(-mp.sqrt(2/(mp.pi*X))))*mp.sqrt(X), mp.sqrt(2/mp.pi), tol=1e-3)
finish()
