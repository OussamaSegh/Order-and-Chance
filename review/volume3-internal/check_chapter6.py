"""Boundary and example computations for the ring review; not general proofs."""
from fractions import Fraction
import itertools
import math
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/'volume3-symmetry/chapters/ch06-rings.tex'


def check_zero_ring_source(source=None):
    source=SOURCE.read_text() if source is None else source
    example=re.search(r'\\begin\{example\}\\label\{ex:rings\}(.*?)\\end\{example\}',source,re.S)[1]
    assert 'never a domain' not in example, 'False when one factor is the zero ring'
    quotient=re.search(r'\\begin\{proposition\}\[quotient rings\](.*?)\\begin\{enumerate\}',source,re.S)[1]
    assert r'I\ne R' not in quotient, 'Unit-ideal quotient is needed for zero-target homomorphisms'


def check_residue_and_crt():
    def is_domain(n,m):
        elements=list(itertools.product(range(n),range(m)))
        zero=(0,0)
        return len(elements)>1 and not any(((a[0]*b[0])%n,(a[1]*b[1])%m)==zero
                for a in elements if a!=zero for b in elements if b!=zero)
    prime=lambda n:n>1 and all(n%d for d in range(2,math.isqrt(n)+1))
    for n,m in itertools.product(range(1,10),repeat=2):
        assert is_domain(n,m)==((n==1 and prime(m)) or (m==1 and prime(n)))
        if math.gcd(n,m)==1:
            assert {(x%n,x%m) for x in range(n*m)}==set(itertools.product(range(n),range(m)))
    assert [a for a in range(12) if math.gcd(a,12)==1]==[1,5,7,11]
    assert [a for a in range(1,12) if any(a*b%12==0 for b in range(1,12))]==[2,3,4,6,8,9,10]
    for n in range(1,13):
        ideals={frozenset(a*k%n for k in range(n)) for a in range(n)}
        assert len(ideals)==sum(n%d==0 for d in range(1,n+1))
        assert {len(i) for i in ideals}=={n//d for d in range(1,n+1) if n%d==0}


def multiply(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out


def check_polynomials():
    # Three exact identities with parameter s; reduce only after multiplication.
    for p in range(2,101):
        if not all(p%d for d in range(2,math.isqrt(p)+1)):continue
        if p==2:
            assert [x%2 for x in multiply(multiply([1,1],[1,1]),multiply([1,1],[1,1]))]==[1,0,0,0,1]
            continue
        factors=[]
        for s in range(p):
            if s*s%p==p-1:factors.append(([-s,0,1],[s,0,1]))
            if s*s%p==2:factors.append(([1,s,1],[1,-s,1]))
            if s*s%p==(-2)%p:factors.append(([-1,s,1],[-1,-s,1]))
        assert factors
        assert all([c%p for c in multiply(a,b)]==[1,0,0,0,1] for a,b in factors)
    polynomial=[1,-4,3]
    assert polynomial[0]==1 and sum(polynomial)==0 and polynomial[1]+2*polynomial[2]==2
    # Distinct-route dual-number square-zero and idempotent equations over Q.
    for a,b in itertools.product(map(Fraction,range(-4,5)),repeat=2):
        if (a*a,2*a*b)==(0,0):assert a==0
        if (a*a,2*a*b)==(a,b):assert b==0 and a in (0,1)


def check_lattice():
    source=(ROOT/'volume3-symmetry/figures/ch06-lattice.tex').read_text()
    points=re.findall(r'\\fill\[([^]]+)\] \(([-\d.]+),([-\d.]+)\) circle',source)
    assert len(points)==21
    norms=set()
    for colour,x,y in points:
        a=round(float(x)/.75);b=round(float(y)/(.75*math.sqrt(5)))
        assert abs(float(x)-.75*a)<.0006 and abs(float(y)-.75*math.sqrt(5)*b)<.0006
        norm=a*a+5*b*b;norms.add(norm)
        assert colour=={4:'MidnightBlue',6:'ForestGreen',9:'BurntOrange'}.get(norm,'black')
    assert not ({2,3}&norms)
    radii=[float(v) for v in re.findall(r'circle \(([\d.]+)\);',source)]
    assert all(abs(radius-.75*math.sqrt(n))<.0006 for radius,n in zip(radii,[2,3,4,6,9]))
    for m,n in itertools.product(range(-8,9),repeat=2):
        assert (1-2*m)**2+5*(1-2*n)**2>=6
    # I²=(2) follows both inclusions from explicit generators.
    w=lambda a,b:(a[0]*b[0]-5*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
    assert w((1,1),(1,-1))==(6,0)
    generators=[(4,0),(2,2),(-4,2)]
    assert all(a%2==b%2==0 for a,b in generators)
    assert tuple(generators[1][i]-generators[2][i]-generators[0][i] for i in (0,1))==(2,0)


if __name__=='__main__':
    check_zero_ring_source()
    check_residue_and_crt()
    check_polynomials()
    check_lattice()
    print('PASS: zero/unit-ideal scope; finite ring products/ideals/CRT; all-prime factor probes<=100; actual lattice points/radii/norms')
