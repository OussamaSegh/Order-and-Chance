"""Finite independent checks supporting the probability draft; not proof certification."""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb, prod, gcd
from pathlib import Path
import json, re

DRAFT=Path(__file__).resolve().parent
s=(DRAFT/'ch09-probability.tex').read_text()
baseline=Path('/workspace/volume0-drafts/discrete/ch09-probability.tex').read_text()
checks=0

def check(ok,what):
    global checks
    if not ok:raise AssertionError(what)
    checks+=1

ex=lambda x:re.findall(r'\\begin\{exercise\}(?:\[[^\]]*\])?\s*\\label\{([^}]+)\}',x)
old,new=ex(baseline),ex(s)
check(len(old)==11,'11 existing split exercises')
check(set(old)<=set(new),'all 11 exercise IDs retained')
check(len(new)==13,'exactly 2 new bridge exercises')
check(Counter(new)==Counter(re.findall(r'\\begin\{hint\}\{([^}]+)\}',s))==Counter(re.findall(r'\\begin\{solution\}\{([^}]+)\}',s)),'13 complete triples')
for label in new:
    sol=re.search(r'\\begin\{solution\}\{'+re.escape(label)+r'\}(.+?)\\end\{solution\}',s,re.S)[1]
    check('\\idea' in sol and '\\writeup' in sol,label+' discovery and writeup')
for n in range(2,9):
    for k in range(n+1):
        subsets=list(combinations(range(n),k));den=len(subsets)
        mean=[sum(i in a for a in subsets)*Q(1,den) for i in range(n)]
        p=Q(k,n)
        check(all(v==p for v in mean),f'sampling means n{n} k{k}')
        for i in range(n):
            for j in range(n):
                cov=sum(Q((i in a)*(j in a),den) for a in subsets)-p*p
                wanted=p*(1-p) if i==j else -p*(1-p)/Q(n-1)
                check(cov==wanted,f'sampling covariance {n} {k} {i} {j}')
        # Matrix has zero row sum and a common positive eigenvalue on differences.
        a=p*(1-p)
        diagonal=a;off=-a/Q(n-1)
        check(diagonal+(n-1)*off==0,'sum direction zero')
        check(diagonal-off==n*a/Q(n-1),'perpendicular eigenvalue')

primes=[2,3,5,7]
for r in range(1,5):
    ps=primes[:r];q=prod(ps)
    for N in range(1,301):
        prob=Q(sum(gcd(u,q)==1 for u in range(1,N+1)),N)
        limit=prod(1-Q(1,p) for p in ps)
        check(abs(prob-limit)<=Q(2**r-1,N),f'arithmetic error r{r} N{N}')
        if N%q==0:
            for m in range(1,r+1):
                for subset in combinations(ps,m):
                    actual=Q(sum(all(u%p==0 for p in subset) for u in range(1,N+1)),N)
                    check(actual==prod(Q(1,p) for p in subset),'mutual prime divisibility independence')

# Enumerate every stopped coupon word of length <=8, for n<=4.
# This validates the tuple mass/count formula exactly for these cases.
for n in range(1,5):
    hist=Counter()
    for length in range(n,9):
        for word in product(range(n),repeat=length):
            seen=set();waits=[0]*n
            terminal=True
            for i,v in enumerate(word):
                if len(seen)==n:
                    terminal=False;break
                waits[len(seen)]+=1;seen.add(v)
            if terminal and len(seen)==n:hist[tuple(waits)]+=1
    for waits,count in hist.items():
        wanted=prod(k**(t-1)*(n-k) for k,t in enumerate(waits))
        check(count==wanted,f'coupon phase count n{n} t{waits}')
    for M in range(0,9):
        stopped=sum(Q(count,n**sum(waits)) for waits,count in hist.items() if sum(waits)<=M)
        # inclusion-exclusion count for all coupons present in M positions
        finite=Q(sum((-1)**j*comb(n,j)*(n-j)**M for j in range(n+1)),n**M)
        check(stopped==finite,f'coupon finite-truncation equivalence n{n} M{M}')

# Pairwise-independent signs example, including all joint pairs.
outcomes=[(a,b,a*b) for a,b in product((-1,1),repeat=2)]
for i,j in combinations(range(3),2):
    check(set(Counter((v[i],v[j]) for v in outcomes).values())=={1},'pairwise uniform signs')
check(Counter(outcomes)[(1,1,1)]==1,'joint-sign dependence count')

# Brace/environment shape check (not a TeX parser or a compilation).
for env in set(re.findall(r'\\begin\{([^}]+)\}',s)):
    check(s.count('\\begin{'+env+'}')==s.count('\\end{'+env+'}'),env+' environment counts')
res={'checks_passed':checks,'original_probability_exercises':old,'current_exercises':new,
     'scope':'finite exact enumerations and source structure only; no universal proof certification or PDF compilation'}
(DRAFT/'verification.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2))
