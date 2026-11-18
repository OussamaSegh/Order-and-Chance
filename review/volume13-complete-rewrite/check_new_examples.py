#!/usr/bin/env python3
"""Deterministic example checks for seventeen new Chapter 1–17 teaching sets.

Numerical checks do not establish general theorems or replace proof review.
"""
import cmath
import math
import unittest

class Volume13Examples(unittest.TestCase):
    def test_ch01_quadratic(self):
        a = 2 + math.sqrt(5)
        b = 2 - math.sqrt(5)
        self.assertAlmostEqual(a+b,4)
        self.assertAlmostEqual(a*b,-1)
        phi=(1+math.sqrt(5))/2
        vals=[round(phi**n+((1-math.sqrt(5))/2)**n) for n in range(5)]
        self.assertEqual(vals,[2,1,3,4,7])

    def test_ch02_ideal_norms(self):
        classes={(a+b)%2 for a in range(2) for b in range(2)}
        self.assertEqual(classes,{0,1})
        self.assertEqual(2*2,4)
        self.assertEqual(2**2*3*3,6**2)

    def test_ch03_embeddings(self):
        theta=2**(1/3)
        w=complex(-.5,math.sqrt(3)/2)
        roots=[theta,theta*w,theta*w*w]
        self.assertAlmostEqual(sum(roots).real,0,places=12)
        self.assertAlmostEqual((roots[0]*roots[1]*roots[2]).real,2)
        self.assertEqual(-27*(-2)**2,-108)
        self.assertEqual(3*2,6)
        self.assertEqual(2**3,8)

    def test_ch04_gaussian(self):
        self.assertEqual((2+1j)*(2-1j),5)
        self.assertEqual((1+1j)**2,2j)
        self.assertFalse(any((x*x+1)%3==0 for x in range(3)))

    def test_ch05_lattice(self):
        self.assertGreater((22/10)**2,4)
        self.assertEqual(2*3,6)
        self.assertGreater(2*math.pi,4)
        self.assertEqual(sum(x*x for x in (1,1)),2)

    def test_ch06_units(self):
        self.assertAlmostEqual((2+math.sqrt(3))*(2-math.sqrt(3)),1)
        u=2**(1/3)
        self.assertAlmostEqual((u-1)*(u*u+u+1),1,places=12)
        self.assertAlmostEqual(math.log(1+math.sqrt(2))+math.log(math.sqrt(2)-1),0)

    def test_ch07_cyclotomic(self):
        self.assertEqual(sum(1 for _ in range(7)),7)
        self.assertEqual(sum(2**i for i in range(3)),2**3-1)
        self.assertEqual(pow(2,4,5),1)
        self.assertTrue(all(pow(2,k,5)!=1 for k in (1,2)))
        for m in range(1,5):
            self.assertGreater(3*m,3*m-1)

    def test_ch08_padic(self):
        self.assertEqual(2*5%9,1)
        self.assertEqual(2*14%27,1)
        self.assertEqual(14%9,5)
        self.assertEqual(27+18,45)
        self.assertEqual(45%9,0)
        self.assertNotEqual(45%27,0)
        self.assertTrue(all((r*r+1)%5==0 for r in (2,3)))

    def test_ch09_local_fields(self):
        self.assertEqual(12*(1/4)*(1/3),1)
        self.assertFalse(any((x*x+1)%3==0 for x in range(3)))
        self.assertEqual(3**2,9)
        self.assertEqual(5-1,4)

    def test_ch10_local_global(self):
        residues={x*x%8 for x in range(8)}
        self.assertEqual(residues,{0,1,4})
        self.assertNotIn(7,{(a+b+c)%8 for a in residues for b in residues for c in residues})
        self.assertEqual(3**2+4**2,5**2)
        self.assertEqual(1**2+2**2+3**2,14)

    def test_ch11_zeta(self):
        s=2
        lhs=1/(1-3**(-2*s))
        rhs=1/(1-3**(-s))*1/(1+3**(-s))
        self.assertAlmostEqual(lhs,rhs)
        self.assertAlmostEqual((1-5**(-s))**(-2),(1-5**(-s))**(-1)*(1-5**(-s))**(-1))
        self.assertEqual([1,-1,1,-1],[1 if n%4==1 else -1 for n in (1,3,5,7)])

    def test_ch12_adelic_fourier(self):
        self.assertAlmostEqual(5*(1/5),1)
        self.assertAlmostEqual(25*(1/25),1)
        theta=lambda y:sum(math.exp(-math.pi*n*n*y) for n in range(-30,31))
        for y in (.5,1,2,3):
            self.assertAlmostEqual(theta(y),theta(1/y)/math.sqrt(y),places=12)

    def test_ch13_frobenius(self):
        self.assertFalse(any((x*x+1)%3==0 for x in range(3)))
        self.assertEqual({x for x in range(7) if (x*x+x+1)%7==0},{2,4})
        self.assertEqual([pow(2,k,5) for k in range(1,5)],[2,4,3,1])

    def test_ch14_conic(self):
        for s,t in ((1,0),(0,1),(1,1),(2,3)):
            x,y,z=s*s,s*t,t*t
            self.assertEqual(x*z,y*y)
        self.assertEqual([(d-1)*(d-2)//2 for d in range(1,5)],[0,0,1,3])

    @staticmethod
    def count_curve(p):
        residues={y*y%p for y in range(p)}
        return 1+sum(sum((y*y-x*x*x+x)%p==0 for y in range(p)) for x in range(p))

    def test_ch15_elliptic(self):
        self.assertEqual(-16*(4*(-1)**3+27*0),64)
        self.assertEqual(self.count_curve(5),8)
        self.assertEqual([x for x in range(5) if (x**3-x)%5==0],[0,1,4])

    def test_ch16_finite_fields(self):
        self.assertEqual(self.count_curve(5),8)
        self.assertEqual(self.count_curve(7),8)
        self.assertEqual(5+1-8,-2)
        self.assertEqual(7+1-8,0)
        self.assertEqual(5**2+1-((-2)**2-2*5),32)

    def test_ch17_modular(self):
        self.assertEqual(240*(1+2**3),2160)
        self.assertEqual(-504*(1+2**5),-16632)
        self.assertEqual(720-(-1008),1728)
        self.assertEqual(179280+720*24+324,196884)

if __name__=="__main__":
    unittest.main(verbosity=2)
