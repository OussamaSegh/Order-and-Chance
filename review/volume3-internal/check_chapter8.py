"""Exact example/diagram and prerequisite-boundary checks for field extensions."""
from fractions import Fraction as F
import itertools
import math
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/'volume3-symmetry/chapters/ch08-extensions.tex'


def mul(a,b):
    # Q(sqrt2,cuberoot2), basis s^i t^j (i<2,j<3).
    result=[F(0)]*6
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            u,v=i//3+j//3,i%3+j%3
            result[(u%2)*3+v%3]+=x*y*2**(u//2+v//3)
    return result


def evaluate(coeffs,a):
    result=[F(0)]*6;power=[F(1),0,0,0,0,0]
    for c in coeffs:
        result=[x+c*y for x,y in zip(result,power)];power=mul(power,a)
    return result


def check_exact_radicals():
    one=[F(1),0,0,0,0,0];s=[0,0,0,F(1),0,0];t=[0,F(1),0,0,0,0]
    alpha=[x+y for x,y in zip(s,t)]
    assert evaluate([-4,-24,12,-4,-6,0,1],alpha)==[0]*6
    numerator=evaluate([-2,6,0,1],alpha);denominator=evaluate([2,0,3],alpha)
    assert mul(s,denominator)==numerator
    assert mul([x+y for x,y in zip(one,t)],[F(1,3),F(-1,3),F(1,3),0,0,0])==one
    assert mul([1,1,1,0,0,0],[-1,1,0,0,0,0])==one
    # Distinct Q(sqrt2,sqrt3) model for constructive primitive-element recovery.
    def quadratic_mul(a,b):
        result=[F(0)]*4
        for i,x in enumerate(a):
            for j,y in enumerate(b):
                u,v=(i%2)+(j%2),(i//2)+(j//2)
                result[(u%2)+2*(v%2)]+=x*y*2**(u//2)*3**(v//2)
        return result
    for c in (F(-7),F(-1),F(1,5),F(1),F(2),F(9,4)):
        gamma=[0,1,c,0];partner=[0,1,-c,0];d=2-3*c*c
        assert d!=0 and quadratic_mul(gamma,partner)==[d,0,0,0]
        assert [(x+y)/2 for x,y in zip(gamma,partner)]==[0,1,0,0]


def check_pentagon_plate():
    source=(ROOT/'volume3-symmetry/figures/ch08-pentagon.tex').read_text()
    path=re.search(r'\\draw\[thick,MidnightBlue\](.*?)cycle;',source,re.S)[1]
    points=[tuple(map(float,x)) for x in re.findall(r'\(([-\d.]+),([-\d.]+)\)',path)]
    assert len(points)==5
    for j,(x,y) in enumerate(points):
        assert abs(x-1.9*math.cos(2*math.pi*j/5))<.0006
        assert abs(y-1.9*math.sin(2*math.pi*j/5))<.0006
    assert abs(2.124-1.9*math.sqrt(5)/2)<.0006
    assert abs(1.174-1.9*(math.sqrt(5)-1)/2)<.0006
    assert abs(.587-1.9*(math.sqrt(5)-1)/4)<.0006
    # Three distinct quadratic nodes and six quadratic inclusion labels.
    for label in (r'\Q(\sqrt2)',r'\Q(\sqrt3)',r'\Q(\sqrt6)'):assert label in source
    assert len(re.findall(r'\{\$2\$\}',source))==6


def check_characteristic_probes():
    # Frobenius on multivariate polynomials: a second exact expansion of small
    # nontrivial sums, with cross-terms retained until reduction.
    def poly_mul(a,b,p):
        out={}
        for (i,j),x in a.items():
            for (k,l),y in b.items():out[i+k,j+l]=(out.get((i+k,j+l),0)+x*y)%p
        return {k:v for k,v in out.items() if v}
    for p in (2,3,5,7):
        a={(0,0):1,(1,0):1,(0,1):p-1,(2,3):2%p};a={k:v for k,v in a.items() if v}
        power={(0,0):1}
        for _ in range(p):power=poly_mul(power,a,p)
        assert power=={(i*p,j*p):x for (i,j),x in a.items()}
    source=SOURCE.read_text()
    assert 'isolated intersections of two distinct such curves' in source
    assert 'through two distinct points already constructed' in source
    assert 'm(n-1)' in source and 'p^2' in source
    assert 'if the gcd were $1$' in source
    assert 'opposite of the $n$th listed subset' in source


if __name__=='__main__':
    check_exact_radicals()
    check_pentagon_plate()
    check_characteristic_probes()
    print('PASS: exact degree6 equation/inverses/recovery; actual pentagon/tower; multivariate Frobenius; local prerequisite/geometry guards')
