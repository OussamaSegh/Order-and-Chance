#!/usr/bin/env python3
"""Volume 9, Chapter 2: recompute the formulas printed in the examples and solutions."""
import sympy as sp
from common import check_true, finish

s, t, x, y, x0 = sp.symbols('s t x y x0', real=True)
# Loop of Theorem bracketloop for X = d/dx, Y = x d/dy: exactly p + s^2 e_y
def fX(p, t): return (p[0] + t, p[1])
def fY(p, t): return (p[0], p[1] + t*p[0])
q = fY(fX(fY(fX((x, y), s), s), -s), -s)
check_true("loop of X=dx, Y=x dy is (x, y+s^2)", sp.simplify(q[0] - x) == 0 and sp.simplify(q[1] - y - s**2) == 0)
# Flow of x^2 d/dx
phi = x0/(1 - t*x0)
check_true("flow of x^2: d/dt phi = phi^2", sp.simplify(sp.diff(phi, t) - phi**2) == 0)
# Linear fields: loop e^{-sB} e^{-sA} e^{sB} e^{sA} = I + s^2(BA-AB) + O(s^3)
A = sp.Matrix([[0, -1], [1, 0]]); B = sp.Matrix([[1, 0], [0, -1]])
expo = lambda M: sum(((M**k)/sp.factorial(k) for k in range(5)), sp.zeros(2))
L = (expo(-s*B)*expo(-s*A)*expo(s*B)*expo(s*A)).applyfunc(lambda e: sp.series(sp.expand(e), s, 0, 3).removeO())
check_true("linear loop = I - 2 s^2 [[0,1],[1,0]] + O(s^3)", sp.simplify(L - (sp.eye(2) - 2*s**2*sp.Matrix([[0, 1], [1, 0]]))) == sp.zeros(2))
check_true("AB and BA as printed", A*B == sp.Matrix([[0, 1], [1, 0]]) and B*A == sp.Matrix([[0, -1], [-1, 0]]))
# Parallel parking: (s cos s - s, s sin s) = (-s^3/2, s^2) + O(s^4)
check_true("parking x", sp.series(s*sp.cos(s) - s, s, 0, 4).removeO() == -s**3/2)
check_true("parking y", sp.series(s*sp.sin(s), s, 0, 4).removeO() == s**2)
# x' = x log x: x(t) = exp(e^t log x0)
xs = sp.exp(sp.exp(t)*sp.log(x0))
check_true("x' = x log x solution", sp.simplify(sp.diff(xs, t) - xs*sp.log(xs).expand(force=True)) == 0)
# x_c(t) = (t-c)^2/4 solves x' = sqrt(x) for t > c
c = sp.symbols('c', real=True)
check_true("x_c solves x'=sqrt|x| for t>c", sp.simplify(sp.diff((t-c)**2/4, t) - (t-c)/2) == 0)
# Adams: number of fields on S^{n-1} is 2^b+8a-1 for n = 2^{4a+b} odd; only n=2,4,8 reach n-1
def rho(n):
    v = 0
    while n % 2 == 0: n //= 2; v += 1
    a, b = divmod(v, 4); return 2**b + 8*a - 1
check_true("Adams: n-1 fields only for n in {1,2,4,8} up to 4096", [n for n in range(1, 4097) if rho(n) == n - 1] == [1, 2, 4, 8])
finish()
