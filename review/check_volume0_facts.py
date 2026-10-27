#!/usr/bin/env python3
"""Independent exact/symbolic and high-precision checks for the Volume 0 review.

Run from any directory: python3 review/check_volume0_facts.py
Requires the repository's sympy, mpmath, numpy and scipy dependencies.
These finite checks support the written review; they are not proof certification.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import permutations, combinations, product
from math import comb, factorial, gcd
from pathlib import Path
import re
import json
import mpmath as mp
import numpy as np
import sympy as sp
from scipy.interpolate import BarycentricInterpolator

mp.mp.dps = 240
ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / 'tome0-mathematical-maturity/chapters'
checks = 0
results = {}

def require(ok, name):
    global checks
    if not ok:
        raise AssertionError(name)
    checks += 1

def record(name, value):
    results[name] = str(value)

x, n = sp.symbols('x n')
fib = [0, 1]
for _ in range(1001):
    fib.append(fib[-1] + fib[-2])

# Coverage: every numbered exercise has exactly one hint and one solution.
coverage = {}
for path in sorted(CHAPTERS.glob('ch*.tex')):
    text = path.read_text()
    exercises = re.findall(r'\\begin\{exercise\}(?:\[[^\]]*\])?\s*\\label\{([^}]+)\}', text)
    hints = re.findall(r'\\begin\{hint\}\{([^}]+)\}', text)
    solutions = re.findall(r'\\begin\{solution\}\{([^}]+)\}', text)
    require(Counter(exercises) == Counter(hints) == Counter(solutions), path.name + ' exercise/hint/solution coverage')
    require(len(set(exercises)) == len(exercises), path.name + ' unique exercise IDs')
    coverage[path.stem] = len(exercises)
require(sum(coverage.values()) == 130, '130 exercises retained')
results['exercise_coverage'] = coverage

# 1. Sums, finite differences, arithmetic and Catalan counting.
for m in range(6):
    S = sp.summation(x**(2*m+1), (x, 1, n))
    require(sp.expand(S.subs(n, -1-n) - S) == 0, 'Faulhaber reflection ' + str(m))
require(sp.expand(sp.summation(x**5,(x,1,n)) - (4*(n*(n+1)/2)**3-(n*(n+1)/2)**2)/3) == 0, 'fifth-power formula')
for k in range(1, 41):
    require(sum(j**3 for j in range(k+1)) == (k*(k+1)//2)**2, 'cube sum')
    require(sum(j*(j+1) for j in range(k+1)) == k*(k+1)*(k+2)//3, 'workshop 1')
    require(sum(comb(k,j) % 2 for j in range(k+1)) == 2**k.bit_count(), 'odd Pascal entries')
    require((comb(2*k,k) & -comb(2*k,k)).bit_length()-1 == k.bit_count(), 'central binomial valuation')
for a in range(1,30):
    for b in range(1,30):
        require(gcd(fib[a],fib[b]) == fib[gcd(a,b)], 'Fibonacci gcd')
for k in range(1,8):
    good = sum(all(2*sum(steps[:j])-j <= 0 for j in range(1,2*k+1))
               for steps in product((0,1),repeat=2*k) if sum(steps)==k)
    require(good == comb(2*k,k)//(k+1), 'Catalan reflection')
require([sum(comb(k,j) for j in range(5)) for k in range(7)] == [1,2,4,8,16,31,57], 'workshop 1 graph')

# 2. Complex arithmetic, cyclotomy and the triangle isometry.
require([(2+1j)**k for k in range(4)] == [1,2+1j,3+4j,2+11j], 'spiral powers')
positions = [0j]
for k in range(4): positions.append(positions[-1] + (1+1j)**k)
require(positions == [0,1,2+1j,2+3j,5j], 'workshop 2 robot')
for k in range(1,105):
    require(max(abs(a) for a in sp.Poly(sp.cyclotomic_poly(k,x),x).all_coeffs()) <= 1, 'cyclotomic coefficients <=104')
p = sp.Poly(sp.cyclotomic_poly(105,x),x)
require([k for k in range(p.degree()+1) if p.nth(k)==-2] == [7,41], 'Phi105 exceptional coefficients')
for k in range(2,31):
    value = mp.fprod(2*mp.sin(mp.pi*j/k) for j in range(1,k))
    require(abs(value-k)<mp.mpf('1e-140'), 'regular polygon distance product')
a,b,c=sp.symbols('a b c');g=(a+b+c)/3
require(sp.expand(3*g-c-(a+b))==0, 'triangle congruence map')

# 3. Wronskian sign, interpolation and actual secrecy distributions.
A=x*x+2*x+3; B=x**3-x+5; C=A+B; W=A*sp.diff(B,x)-sp.diff(A,x)*B
require(sp.expand(W-(A*sp.diff(C,x)-sp.diff(A,x)*C))==0, 'Mason identity A,C')
require(sp.expand(W-(sp.diff(B,x)*C-B*sp.diff(C,x)))==0, 'Mason identity B,C')
require(sp.interpolate([(1,8),(2,15),(3,24)],x)==x*x+4*x+3, 'secret 3 interpolation')
for i,j in combinations(range(1,6),2):
    distributions=[]
    for secret in range(7):
        d=Counter(((secret+a*i+b*i*i)%7,(secret+a*j+b*j*j)%7) for a,b in product(range(7),repeat=2))
        require(len(d)==49 and set(d.values())=={1}, 'Shamir uniform share pair')
        distributions.append(d)
    require(all(d==distributions[0] for d in distributions), 'Shamir secret-independent distribution')
for k in range(1,10):
    T=sp.chebyshevt(k,x)
    require(sp.LC(sp.Poly(T,x))==2**(k-1), 'Chebyshev leading coefficient')
for label,nodes in [('uniform',np.linspace(-1,1,11)),('Chebyshev',np.cos((2*np.arange(11)+1)*np.pi/22))]:
    grid=np.linspace(-1,1,20001)
    # Explicit weights make this deterministic across SciPy versions.
    weights=np.array([1/np.prod(v-np.delete(nodes,j)) for j,v in enumerate(nodes)])
    interp=BarycentricInterpolator(nodes,1/(1+25*nodes**2),wi=weights)
    error=max(abs(interp(grid)-1/(1+25*grid**2)))
    require((1.9<error<1.93) if label=='uniform' else (.109<error<.111), 'Runge '+label)
    record('Runge '+label+' maximum error (grid)',error)

# The sensitivity workshop has exact rational roots after perturbation.
require(sp.factor((x-1)**2-sp.Rational(1,25)) == (5*x-6)*(5*x-4)/25, 'workshop 3 perturbed roots')

# 4. Mean geometry, Carleman constants, optimisation and entropy.
require(Q(2*1*4,1+4) == Q(8,5), 'harmonic mean projection')
for k,target in [(10,'1.52'),(100,'1.94'),(10000,'2.29')]:
    ratio=sum(mp.exp(-mp.loggamma(j+1)/j) for j in range(1,k+1))/mp.harmonic(k)
    require(abs(ratio-mp.mpf(target))<mp.mpf('.005'), 'Carleman numeric ratio')
    record('Carleman N='+str(k),mp.nstr(ratio,14))
require(sp.expand(x*(10-x)-(25-(x-5)**2))==0, 'workshop 4 area deficit')

# 5. Error certificates, continued-fraction denominator and local bounds.
xs=mp.mpf(1)
for k in range(1,9):
    xs=(xs+2/xs)/2
    error=xs-mp.sqrt(2)
    require(error>=0 and error < mp.mpf('2.83')*mp.mpf('.03034')**(2**(k-1)), 'Newton upper bound')
    record('Newton step '+str(k)+' absolute error',mp.nstr(error,14))
require(mp.mpf('2.83')*mp.mpf('.03034')**128 < mp.mpf('1e-100'), '100 decimal Newton guarantee')
require(fib[1001]>10**208, 'continued-fraction length lower bound')
ln2six=2*sum(Q(1,(2*k+1)*3**(2*k+1)) for k in range(6))
ln2error=abs(mp.mpf(ln2six.numerator)/ln2six.denominator-mp.log(2))
require(ln2error<mp.mpf(9)/(4*13*3**13)<mp.mpf('1e-6'), 'workshop 5 six-term log2 certificate')
record('six-term accelerated log2 error',mp.nstr(ln2error,15))

# 6. Taylor, Gaussian sandwich, quadrature and Hermite's integral.
for degree,target,tol in [(1,'3.14','.005'),(5,'.524','.0005'),(9,'.0069','.00005'),(13,'.00002','.000005')]:
    val=sum((-1)**j*mp.pi**(2*j+1)/mp.factorial(2*j+1) for j in range((degree+1)//2))
    require(abs(val-mp.mpf(target))<mp.mpf(tol), 'sin Taylor caption')
I=mp.quad(lambda t:mp.exp(-t*t),[0,1])
R=sum(mp.exp(-(mp.mpf(k)/8)**2) for k in range(1,9))/8
require(abs((I-R)-mp.mpf('.040'))<mp.mpf('.0005'), 'Riemann actual error')
Wn=lambda k:mp.sqrt(mp.pi)*mp.gamma((k+1)/2)/(2*mp.gamma((k+2)/2))
for k in range(1,10):
    require(mp.sqrt(k)*Wn(2*k+1)<mp.sqrt(mp.pi)/2<mp.sqrt(k)*Wn(2*k-2), 'Gaussian sandwich')
require(abs(mp.sqrt(3)*Wn(7)-mp.mpf('.792'))<mp.mpf('.0005'), 'Gaussian lower caption')
require(abs(mp.sqrt(3)*Wn(4)-mp.mpf('1.020'))<mp.mpf('.0005'), 'Gaussian upper caption')
require(16*mp.mpf(5)**-15/15+4*mp.mpf(239)**-5/5 < mp.mpf('1e-10'), 'Machin 7+2 error including factors')
rotated=4*mp.quad(lambda t:t,[0,mp.pi/6])+4*mp.quad(lambda t:mp.pi/4-t/2,[mp.pi/6,mp.pi/2])
require(abs(rotated-mp.pi**2/6)<mp.mpf('1e-145'), 'Basel rotated integral')
f=x**2*(x-1)**3/2
F=sum(sp.diff(f,x,k) for k in range(sp.degree(f)+1))
require(sp.expand(F-sp.diff(F,x)-f)==0, 'Hermite integration-by-parts identity')

require(all(1+v+v*v/2 <= mp.exp(v) <= 1+v+v*v/2+v**3/2
            for v in [mp.mpf(k)/100 for k in range(101)]), 'workshop 6 exponential envelopes')

# 7. Symmetric factors, determinants, PageRank, least squares and Hilbert.
S1=sp.Matrix([[1,2],[2,3]]);S2=sp.Matrix([[3,1],[1,4]]);P=sp.Matrix([[1,2],[0,1]])
L=P.inv()*S1*P.inv().T;R=P.T*S2*P
require(L==L.T and R==R.T and L*R==P.inv()*S1*S2*P, 'correct similarity symmetric factors')
require((P.T*S1*P)*(P.inv()*S2*P.inv().T)!=P.inv()*S1*S2*P, 'old similarity identity counterexample')
Pweb=sp.Matrix([[0,0,1,Q(1,2)],[Q(1,2),0,0,0],[Q(1,2),1,0,Q(1,2)],[0,0,0,0]])
G=sp.Rational(17,20)*Pweb+sp.ones(4)*sp.Rational(3,80)
pi=sp.Matrix([sp.Rational(2687,7076),sp.Rational(56293,283040),sp.Rational(108653,283040),sp.Rational(3,80)])
require(G*pi==pi and sum(pi)==1, 'PageRank exact vector')
require(sp.factor(G.charpoly(x).as_expr()-x*(x-1)*(x*x+sp.Rational(17,20)*x+sp.Rational(289,800)))==0, 'PageRank characteristic polynomial')
H=sp.Matrix(12,12,lambda i,j:sp.Rational(1,i+j+1))
det=H.det();record('det H12',sp.N(det,14))
require(mp.mpf('2.6e-78')<mp.mpf(str(sp.N(det,50)))<mp.mpf('2.7e-78'), 'Hilbert determinant caption')
D=sp.Matrix([[1,0],[1,1],[1,2]]);y=sp.Matrix([1,2,2]);theta=sp.Matrix([sp.Rational(7,6),sp.Rational(1,2)])
require(D.T*(y-D*theta)==sp.zeros(2,1), 'workshop 7 normal equations')

# 8. Sieve, derangements, birthdays, menages, ballot, records and Bayes.
survivors=[k for k in range(1,101) if gcd(k,30)==1]
require(len(survivors)==26 and [k for k in survivors if k>1 and not sp.isprime(k)]==[49,77,91], 'sieve counterexamples')
require(sum(sp.isprime(k) for k in survivors)==22, '22 surviving primes')
regions=Counter(tuple(k%p==0 for p in (2,3,5)) for k in range(1,101))
require(sorted(regions.values())==[3,3,7,7,13,14,26,27], 'seven Venn regions and outside')
Dcount=lambda n:sum((-1)**j*factorial(n)//factorial(j) for j in range(n+1))
require(abs(mp.mpf(Dcount(10))/factorial(10)-1/mp.e)<mp.mpf('3e-8'), 'derangement 10 error')
for k in range(11):
    exact=mp.mpf(comb(10,k)*Dcount(10-k))/factorial(10)
    approx=mp.exp(-1)/mp.factorial(k)
    require(round(float(exact),4)==round(float(approx),4), 'fixed point Poisson four decimals')
for k in (22,23,56,57):
    p=mp.fprod(1-mp.mpf(j)/365 for j in range(k))
    record('birthday collision '+str(k),mp.nstr(1-p,15))
    require((1-p<mp.mpf('.5')) if k==22 else ((1-p>mp.mpf('.5')) if k==23 else ((1-p<mp.mpf('.99')) if k==56 else 1-p>mp.mpf('.99'))), 'birthday threshold')
wait=sum(mp.fprod(1-mp.mpf(j)/365 for j in range(k)) for k in range(366))
require(abs(wait-mp.mpf('24.6'))<mp.mpf('.05'),'birthday waiting time')
record('birthday expected first repeat',mp.nstr(wait,16))
for nmen in range(3,9):
    exact=sum(all(p[j]!=j and p[j]!=(j+1)%nmen for j in range(nmen)) for p in permutations(range(nmen)))
    formula=sum((-1)**k*Q(2*nmen,2*nmen-k)*comb(2*nmen-k,k)*factorial(nmen-k) for k in range(nmen+1))
    require(exact==formula, 'Touchard fixed-women normalisation')
for a in range(1,8):
    for b in range(a):
        good=0
        for ups in combinations(range(a+b), a):
            steps=[1 if j in ups else -1 for j in range(a+b)]
            good += all(sum(steps[:j])>0 for j in range(1,a+b+1))
        require(Q(good,comb(a+b,a))==Q(a-b,a+b),'strict ballot including b=0')
mu=mp.harmonic(1000);lo=mu+mp.log(mp.mpf(1000001)/1001);hi=mu+mp.log(1000)
varhi=hi-sum(mp.mpf(1)/k**2 for k in range(1,1001))
require(mp.mpf('14.392')<lo<hi<mp.mpf('14.394') and varhi<mp.mpf('12.75'),'records finite-sum bounds')
require(Q(1275,100)/Q(12769,100)<Q(1,10),'records Chebyshev guarantee')
record('record mean enclosure',mp.nstr(lo,18)+' < mean < '+mp.nstr(hi,18))
record('record variance upper bound',mp.nstr(varhi,18))
require(Q(1,100)*Q(99,100)**2/(Q(1,100)*Q(99,100)**2+Q(99,100)*Q(5,100)**2)==Q(99,124),'workshop 8 independent tests')
require(Q(2500,9*5556)<=Q(1,20) and Q(2500,9*5555)>Q(1,20),'poll sufficient size')
multinom=mp.factorial(600)/(mp.factorial(100)**6*mp.mpf(6)**600)
require(abs(multinom-mp.mpf('2.46e-7'))<mp.mpf('.005e-7'),'multinomial peak caption')
record('multinomial peak n600',mp.nstr(multinom,16))
print(json.dumps({'checks_passed':checks,**results},indent=2))
