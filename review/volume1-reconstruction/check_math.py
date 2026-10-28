"""Independent exact/symbolic checks supporting, never replacing, source proofs."""
import json, math, re
from collections import deque
from fractions import Fraction as F
from pathlib import Path
import sympy as S
from sympy.matrices.normalforms import hermite_normal_form
OUT=Path(__file__).resolve().parent
results={}
def check(group,condition):
    assert condition,group
    results[group]=results.get(group,0)+1
primes=list(S.primerange(2,241))
def val(n,p):
    if n==0:return math.inf
    n=abs(n);v=0
    while n%p==0:v+=1;n//=p
    return v

def run():
    for a in range(-24,25):
        for b in range(1,25):
            q,r=divmod(a,b);check('division_signed',a==q*b+r and 0<=r<b)
    for n in range(0,150):
        check('gcd_polynomial',math.gcd(n*n+1,(n+1)**2+1)==(5 if n%5==2 else 1))
    for a in range(1,13):
        for b in range(1,13):
            check('mersenne_gcd',math.gcd(2**a-1,2**b-1)==2**math.gcd(a,b)-1)
            if math.gcd(a,b)==1:
                bound=a*b-a-b
                # Includes a=1, b=1: largest missing integer is -1.
                representable={a*x+b*y for x in range(max(2,b+2)) for y in range(max(2,a+2))}
                check('coin_boundary',bound not in representable and all(t in representable for t in range(max(0,bound+1),a*b+1)))
    for p in primes[:15]:
        for n in range(0,80):
            check('legendre_factorial',val(math.factorial(n),p)==sum(n//p**j for j in range(1,10)))
        for m in range(0,18):
            for n in range(0,18):
                carries=sum((m+n)//p**j-m//p**j-n//p**j for j in range(1,8))
                check('binomial_carries',val(math.comb(m+n,m),p)==carries)
    for n in range(2,140):check('n_not_divides_2n_minus1',(2**n-1)%n!=0)
    for n in range(1,180):
        c=math.comb(2*n,n)
        check('central_binomial',4**n<=2*n*c and c<=4**n)
        for p,e in S.factorint(c).items():check('binomial_primepower',p**e<=2*n)
        check('bertrand',any(S.isprime(p) for p in range(n+1,2*n+1)))
    for n in range(1,100):
        units=[a for a in range(n) if math.gcd(a,n)==1]
        check('euler_all_units',all(pow(a,len(units),n)==1%n for a in units))
        roots=[a for a in units if all(pow(a,len(units)//q,n)!=1%n for q in S.factorint(len(units)))]
        f=S.factorint(n)
        cyclic=n in (1,2,4) or (len(f)==1 and n%2==1) or (f.get(2)==1 and len(f)==2)
        check('cyclic_classification',bool(roots)==cyclic)
    for p in primes[1:]:
        squares={a*a%p for a in range(1,p)}
        for a in range(0,p):
            chi=0 if a==0 else 1 if a in squares else -1
            check('euler_criterion',pow(a,(p-1)//2,p)==chi%p)
        check('supplementary_two',int(S.legendre_symbol(2,p))==(-1)**((p*p-1)//8))
        count=sum(a in squares and a+1 in squares for a in range(1,p-1))
        check('consecutive_squares',count==(p-4-int(S.legendre_symbol(-1,p)))//4)
        for q in primes[1:]:
            if p!=q:check('reciprocity',int(S.legendre_symbol(p,q)*S.legendre_symbol(q,p))==(-1)**(((p-1)//2)*((q-1)//2)))
        for a in range(1,p):
            signed=[((k*a+p//2)%p)-p//2 for k in range(1,(p+1)//2)]
            check('gauss_signed',(-1)**sum(r<0 for r in signed)==int(S.legendre_symbol(a,p)))
    check('jacobi_worked',S.jacobi_symbol(1001,9907)==-1)
    check('reciprocity_root',pow(219,96,383)==169 and 169**2%383==219)
    for n in range(1,200):
        ds=S.divisors(n)
        check('totient_divisor_sum',sum(S.totient(d) for d in ds)==n)
        check('mobius_divisor_sum',sum(S.mobius(d) for d in ds)==(1 if n==1 else 0))
        check('mobius_tau',sum(S.mobius(d)*S.divisor_count(d) for d in ds)==(-1)**len(S.factorint(n)))
        check('sigma_parity',int(S.divisor_sigma(n))%2==int(math.isqrt(n)**2==n or n%2==0 and math.isqrt(n//2)**2==n//2))
    for N in range(1,50):
        C=sum(math.gcd(a,b)==1 for a in range(1,N+1) for b in range(1,N+1))
        formula=sum(int(S.mobius(d))*(N//d)**2 for d in range(1,N+1))
        check('coprime_exact',C==formula)
        check('coprime_error',abs(C-N*N*6/math.pi**2)<=2*N*sum(1/d for d in range(1,N+1))+N)
    for n in range(1,301):
        points=sum(x*x+y*y==n for x in range(-math.isqrt(n),math.isqrt(n)+1) for y in range(-math.isqrt(n),math.isqrt(n)+1))
        rhs=4*sum(0 if d%2==0 else 1 if d%4==1 else -1 for d in S.divisors(n))
        check('jacobi_r2',points==rhs)
        check('two_square_criterion',bool(points)==all(e%2==0 for p,e in S.factorint(n).items() if p%4==3))
    aa=S.symbols('a:4');bb=S.symbols('b:4');a,b,c,d=aa;e,f,g,h=bb
    zz=[a*e+b*f+c*g+d*h,a*f-b*e+c*h-d*g,a*g-c*e+d*f-b*h,a*h-d*e+b*g-c*f]
    check('four_square_symbolic',S.expand(sum(v*v for v in zz)-sum(v*v for v in aa)*sum(v*v for v in bb))==0)
    check('four_square_descent_example', [int(v.subs(dict(zip(aa+bb,[4,2,1,0,1,-1,1,0])))) for v in zz]==[3,-6,3,3])
    for R in (1,1.1,math.sqrt(2),2,6,10):
        n=sum(x*x+y*y<=R*R for x in range(-math.ceil(R),math.ceil(R)+1) for y in range(-math.ceil(R),math.ceil(R)+1))
        check('circle_bound',abs(n-math.pi*R*R)<=2*math.sqrt(2)*math.pi*R+2*math.pi)
    x,y=S.symbols('x y')
    for branch in [(x+2*y,y)]:pass
    for p in [5,13,17,29,37,41,53,61,73,89,97]:
        triples={(x,y,z) for x in range(1,math.isqrt(p)+1) for y in range(1,p//4+1) for z in range(1,p//4+1) if x*x+4*y*z==p}
        def invol(t):
            x,y,z=t
            if x<y-z:return x+2*z,z,y-x-z
            if x<2*y:return 2*y-x,y,x-y+z
            return x-2*y,x-y+z,y
        check('zagier',all(invol(t) in triples and invol(invol(t))==t for t in triples) and sum(invol(t)==t for t in triples)==1)
    for d in (2,3,5,7,13,61):
        # Integer recurrence for sqrt(d), avoiding decimal coefficient inference.
        a0=math.isqrt(d);m=0;den=1;a=a0;pn2,pn1=0,1;qn2,qn1=1,0
        for k in range(32):
            pn=a*pn1+pn2;qn=a*qn1+qn2
            check('cf_determinants',pn*qn1-pn1*qn==(-1)**(k-1))
            pn2,pn1=pn1,pn;qn2,qn1=qn1,qn
            m=den*a-m;den=(d-m*m)//den;a=(a0+m)//den
        if d==61:check('pell61',1766319049**2-61*226153980**2==1)
    # Ideal arithmetic as independent Z-lattice multiplication.
    def norm(v,d):a,b=v;return a*a-d*b*b
    def mul(v,w,d):a,b=v;c,e=w;return(a*c+d*b*e,a*e+b*c)
    def lattice(gens,d):
        cols=[S.Matrix(v) for v in gens]+[S.Matrix(mul(v,(0,1),d)) for v in gens]
        return hermite_normal_form(S.Matrix.hstack(*cols))
    def product(A,B,d):return lattice([mul(tuple(A[:,i]),tuple(B[:,j]),d) for i in range(2) for j in range(2)],d)
    P=lattice([(2,0),(1,1)],-5);Q=lattice([(3,0),(1,1)],-5);QB=lattice([(3,0),(1,-1)],-5)
    for A,B,gens in [(P,P,[(2,0)]),(Q,QB,[(3,0)]),(P,Q,[(1,1)]),(P,QB,[(1,-1)])]:
        check('ideal_products_six',product(A,B,-5)==lattice(gens,-5))
    for d in (-1,-2,-5,-6,-7,2,3,6,7,10):
        # Applies to integral basis 1,sqrt(d) when d=2,3 mod4.
        if d%4==1:continue
        for p in [2,3,5,7,11,13]:
            for a in range(p):
                if (a*a-d)%p:continue
                A=lattice([(p,0),(a,1)],d);AB=lattice([(p,0),(a,-1)],d)
                check('ideal_conjugate_norm',product(A,AB,d)==lattice([(abs(int(A.det())),0)],d))
                check('ideal_index_p',abs(int(A.det()))==p)
    check('inert_two_norm',abs(int(lattice([(2,0)],5).det()))==4)
    # Lambda divisibility in Z[omega] via norm and exact coefficient quotients.
    def emul(v,w):a,b=v;c,d=w;return(a*c-b*d,a*d+b*c-b*d)
    def eadd(v,w):return tuple(a+b for a,b in zip(v,w))
    def epow(v,k):
        r=(1,0)
        for _ in range(k):r=emul(r,v)
        return r
    lam=(1,-1);l4=epow(lam,4)
    def ediv(v,w):
        a,b=v;c,d=w;N=c*c-c*d+d*d
        z=emul(v,(c-d,-d))
        return all(t%N==0 for t in z)
    for a in range(-8,9):
        for b in range(-8,9):
            if (a+b)%3:
                cube=epow((a,b),3)
                check('eisenstein_cube',ediv(eadd(cube,(-1,0)),l4) or ediv(eadd(cube,(1,0)),l4))
    for p in (2,3,5,7):
        for k in range(1,5):
            mod=p**k
            for u in range(mod):
                if u%p==0:continue
                roots=any(x*x%mod==u for x in range(mod))
                criterion=(u%8==1) if p==2 and k>=3 else (u%4==1) if p==2 and k==2 else True if p==2 else pow(u,(p-1)//2,p)==1
                check('finite_square_criteria',roots==criterion)
    mod=256;roots=[a for a in range(mod) if (a*a+7)%mod==0]
    check('singular_root_candidates',roots==[53,75,181,203])
    check('singular_root_survival',[a for a in roots if any((b*b+7)%512==0 for b in (a,a+256))]==[75,181])
    for start,expected in [(1,181),(3,75)]:
        a=F(start)
        for _ in range(5):a=(a*a-7)/(2*a)
        check('newton_root',a.numerator*pow(a.denominator,-1,256)%256==expected)
    check('teich_precision',pow(2,125,125)==57 and pow(57,4,125)==1)
    # Original numerical data in generated figures, parsed independently.
    root=OUT.parents[1]/'tome1-integers/figures'
    ruler=(root/'ch12-ruler.tex').read_text()
    for n,v in re.findall(r'\((\d+),([0-9.]+)\)',ruler):
        n=int(n)
        if n:check('figure_ruler',float(v)==2**(-val(n,2)))
    split=(root/'ch11-split.tex').read_text()
    for color,n in re.findall(r'\\node\[fill=([^,]+),[^\n]+\{(\d+)\};',split):
        n=int(n)
        expected='Plum' if n in (2,5) else 'ForestGreen' if n%20 in (1,9) else 'Orange' if S.legendre_symbol(-5,n)==1 else 'gray!45'
        check('figure_splitting',color==expected)
    result=dict(groups=results,total=sum(results.values()),scope='Finite tests and exact symbolic identities; universal proofs are reviewed separately.')
    (OUT/'mathematical-check-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':run()
