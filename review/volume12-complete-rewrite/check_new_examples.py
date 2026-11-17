#!/usr/bin/env python3
"""Twelve independently recomputable, deterministic example checks.

Numerical checks cannot certify any of the manuscript's general theorems.
"""
import math
import unittest

class NewExamples(unittest.TestCase):
    def almost(self, x, y, eps=1e-8):
        self.assertLess(abs(x-y), eps, (x,y))
    def test_ch01_bridge(self):
        for t in (0.0,.25,.5,.75,1.0):
            self.almost(t-2*t*t+t*t,t*(1-t))
        self.almost(.5-1/3,1/6)
    def test_ch02_reflection(self):
        a,t,h=1.25,2.0,1e-5
        F=lambda x:math.erfc(a/math.sqrt(2*x))
        density=a/math.sqrt(2*math.pi*t**3)*math.exp(-a*a/(2*t))
        self.almost((F(t+h)-F(t-h))/(2*h),density)
    def test_ch03_martingale(self):
        for t in (.25,1,2):
            self.almost(3*t*t-2*t*t+t*t,2*t*t)
            self.almost(t*t,t**2)
    def test_ch04_ito(self):
        t=1.7
        self.almost(t**3/3, t*t*t/3)
        self.almost((3*t*t-2*t*t+t*t)/4,t*t/2)
    def test_ch05_heat_and_cameron_martin(self):
        t,h=1.2,1e-3
        for x in (-3,0,2):
            f=lambda y:y*y+t
            self.almost((f(x+h)-2*f(x)+f(x-h))/(2*h*h),1)
        c=.8
        self.almost(math.exp(-c*c/2)*math.exp(c*c/2),1)
        self.almost(math.exp(-c*c/2)*c*math.exp(c*c/2),c)
    def test_ch06_ou_dyson(self):
        a,sigma,t=2.0,.7,1.5
        self.almost(sigma*sigma*(1-math.exp(-2*a*t))/(2*a), .49*(1-math.exp(-6))/4)
        gap=2.0
        self.almost((2/gap)/math.sqrt(2),1/(gap/math.sqrt(2)))
    def test_ch07_poisson_and_levy(self):
        lam,t,m,v=3.0,1.25,.7,1.4
        self.almost(lam*t*(v+m*m),lam*t*v+lam*t*m*m)
        for alpha in (.5,1.,1.5):
            self.assertTrue(math.isfinite(1/(2-alpha)))
        self.assertTrue(math.isinf(sum([math.inf])))
    def test_ch08_networks_kesten(self):
        self.almost(1/(1+1/2),2/3)
        self.almost(6*(2/3),4)
        self.almost(math.sqrt(2*1-1)/1,1)
        self.almost(math.sqrt(3)/2, 0.8660254037844386)
    def test_ch09_semicircle(self):
        n=20000
        du=math.pi/n
        m2=sum((8/math.pi)*math.sin(-math.pi/2+(i+.5)*du)**2*
               math.cos(-math.pi/2+(i+.5)*du)**2*du for i in range(n))
        self.almost(m2,1)
        C=[1]
        for i in range(3):
            C.append(sum(C[j]*C[i-j] for j in range(i+1)))
        self.assertEqual(C,[1,1,2,5])
        theta=1.07
        self.almost(theta+1/theta-2,(theta-1)**2/theta)
    def test_ch10_cue(self):
        for n in (1,2,5,25,100):
            product=1
            for k in range(1,n+1): product*=(k+1)/k
            self.almost(product,n+1)
        u=1e-3
        S=math.sin(math.pi*u)/(math.pi*u)
        self.almost((1-S*S)/(u*u),math.pi**2/3,2e-5)
    def test_ch11_log_gmc(self):
        for n in (10,100,1000):
            h=sum(1/k for k in range(1,n+1))
            self.assertTrue(math.log(n+1)<=h<=1+math.log(n))
        for gamma in (.3,1,1.4):
            self.assertLess(gamma*gamma/2,1)
        self.assertGreater(2**2/2,1)
    def test_appendix_matrix_tree(self):
        self.assertEqual(2*1-1,1)
        self.almost(1*3/3,1)
        self.almost(3*3/3,3)

if __name__ == "__main__":
    unittest.main(verbosity=2)
