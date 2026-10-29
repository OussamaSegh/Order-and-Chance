"""Independent checks of new bridges and mathematical figure data."""
from fractions import Fraction as F
from pathlib import Path
import json,math,re
import sympy as S
import mpmath as mp
OUT=Path(__file__).resolve().parent
FIG=OUT.parents[1]/'volume1-integers/figures'
counts={}
def check(group,value):
    assert value,group
    counts[group]=counts.get(group,0)+1
for p in list(S.primerange(3,80)):
    chi=lambda a:0 if a%p==0 else 1 if any(x*x%p==a%p for x in range(1,p)) else -1
    X=[chi(a) for a in range(p)];Y=[chi(a+1) for a in range(p)]
    check('residue_probability',sum(X)==sum(Y)==0 and sum(a*b for a,b in zip(X,Y))==-1 and sum(a*a for a in X)==p-1)
for p in (2,3,5,7):
    for N in range(1,5):
        def v(n):
            if n==0:return N
            k=0
            while n%p==0:k+=1;n//=p
            return min(k,N)
        vs=[v(n) for n in range(p**N)]
        for k in range(N+1):check('valuation_tail',F(sum(x>=k for x in vs),len(vs))==F(1,p**k))
        check('valuation_expectation',F(sum(vs),len(vs))==(1-F(1,p**N))/(p-1))
a,b,d,w=S.symbols('a b d w')
M=S.Matrix([[a,d*b],[b,a]])
check('norm_matrix_sqrt',M.det()==a*a-d*b*b and S.trace(M)==2*a)
c=S.symbols('c');M=S.Matrix([[a,b*c],[b,a+b]])
check('norm_matrix_half',S.expand(M.det()-(a*a+a*b-c*b*b))==0 and S.trace(M)==2*a+b)
reduce=lambda x:S.rem(S.expand(x),w*w-w-3,w)
check('unit13_cube',reduce((1+w)**3)==13+10*w)
check('unit13_six',reduce((1+w)**6)==469+360*w and 649**2-13*180**2==1)
u,v=S.symbols('u v')
check('binary_form_identity',S.expand((2*u+v)**2+5*v*v-2*(2*u*u+2*u*v+3*v*v))==0)
for n in range(-1000,1001):
    digits=list(map(int,str(abs(n))))[::-1];sgn=-1 if n<0 else 1
    check('signed_digit_rules',(n-sgn*sum(digits))%9==0 and (n-sgn*sum((-1)**i*x for i,x in enumerate(digits)))%11==0)
# Exact Gauss-square calculation in the cyclotomic quotient, independent of floating roots.
z=S.symbols('z')
for p in (3,5,7,11,13,17,19):
    squares={a*a%p for a in range(1,p)}
    g=sum((1 if a in squares else -1)*z**a for a in range(1,p))
    phi=sum(z**a for a in range(p))
    check('gauss_sum_square',S.rem(S.expand(g*g),phi,z)==(-1)**((p-1)//2)*p)
    for q in (3,5,7):
        if q==p:continue
        chiq=1 if q%p in squares else -1
        rem=S.Poly(S.rem(S.expand(g**q-chiq*g),phi,z),z)
        check('gauss_frobenius',all(int(c)%q==0 for c in rem.all_coeffs()))
# All plotted Gaussian/Eisenstein prime positions and their classifications.
s=(FIG/'ch10-primes.tex').read_text()
panels=s.split(r'\begin{scope}')
for index,part in enumerate(panels[1:3]):
    for color,x,y in re.findall(r'\\fill\[([^]]+)\] \((-?[0-9.]+),(-?[0-9.]+)\) circle',part):
        x,y=float(x),float(y)
        if index==0:
            aa,bb=round(x),round(y);norm=aa*aa+bb*bb
            expected='ForestGreen' if norm==2 else 'MidnightBlue' if S.isprime(norm) and norm%4==1 else 'BrickRed' if (aa==0 or bb==0) and S.isprime(abs(aa or bb)) and abs(aa or bb)%4==3 else None
        else:
            bb=round(2*y/math.sqrt(3));aa=round(x+bb/2);norm=aa*aa-aa*bb+bb*bb
            check('eisenstein_coordinates',abs(x-(aa-bb/2))<=.00051 and abs(y-bb*math.sqrt(3)/2)<=.00051)
            expected='ForestGreen' if norm==3 else 'MidnightBlue' if S.isprime(norm) and norm%3==1 else 'BrickRed' if math.isqrt(norm)**2==norm and S.isprime(math.isqrt(norm)) and math.isqrt(norm)%3==2 else None
        check('figure_prime_classification',1<norm<=225 and color==expected)
# High-precision comparison of all forty continued-fraction quality samples.
mp.mp.dps=140
values=[(1+mp.sqrt(5))/2,mp.sqrt(2),mp.e,mp.pi]
s=(FIG/'ch08-quality.tex').read_text()
data=re.findall(r'coordinates \{([^}]+)\}',s)
for x,block in zip(values,data):
    xx=x;pn2,pn1=0,1;qn2,qn1=1,0;qualities={}
    for n in range(11):
        ak=int(mp.floor(xx));pn=ak*pn1+pn2;qn=ak*qn1+qn2
        qualities[n]=qn*qn*abs(x-mp.mpf(pn)/qn)
        pn2,pn1=pn1,pn;qn2,qn1=qn1,qn;xx=1/(xx-ak)
    for n,y in re.findall(r'\((\d+),([0-9.]+)\)',block):
        check('figure_cf_quality',abs(float(qualities[int(n)])-float(y))<.00000051)
# Hyperbola and Eisenstein region point sets, not merely their caption totals.
s=(FIG/'ch04-hyperbola.tex').read_text()
pts=[(int(a),int(b)) for a,b in re.findall(r'\\fill\[[^]]+\] \((\d+),(\d+)\)',s)]
check('figure_hyperbola_complete',set(pts)=={(a,b) for a in range(1,31) for b in range(1,31) if a*b<=30} and len(pts)==111)
s=(FIG/'ch06-eisenstein.tex').read_text()
pts=[]
for color,x,y in re.findall(r'\\fill\[([^]]+)\] \((\d+),(\d+)\)',s):
    x,y=int(x),int(y);pts.append((x,y))
    check('figure_reciprocity_region',color==('MidnightBlue' if 7*y<11*x else 'ForestGreen'))
check('figure_reciprocity_rectangle',set(pts)=={(x,y) for x in range(1,4) for y in range(1,6)})
result=dict(groups=counts,total=sum(counts.values()),scope='Exact and finite checks, not a proof certificate.')
(OUT/'new-check-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
