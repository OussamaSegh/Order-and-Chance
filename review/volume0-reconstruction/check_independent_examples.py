"""Independent finite checks of reconstructed examples; never a proof certificate."""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb, factorial
from pathlib import Path
import json

checks=0

def require(ok, name):
    global checks
    if not ok: raise AssertionError(name)
    checks+=1

# Chapter 0: exhaustive small functions and all domain-subset pairs.
for ne in range(4):
    E=set(range(ne))
    subsets=[{i for i in E if bits>>i&1} for bits in range(2**ne)]
    for nf in range(4):
        F=set(range(nf))
        for values in product(range(nf),repeat=ne):
            image=lambda A: {values[i] for i in A}
            injective=len(set(values))==ne
            preserves=True
            for A in subsets:
                recovered={i for i in E if values[i] in image(A)}
                require(A<=recovered,'image/preimage inclusion')
                require((recovered==A) or not injective,'injective image/preimage')
                require(image(E-A)>=image(E)-image(A),'image complement inclusion')
                if injective:
                    require(image(E-A)==image(E)-image(A),'injective image complement')
                for B in subsets:
                    equality=image(A&B)==image(A)&image(B)
                    preserves=preserves and equality
                    require(image(A&B)<=image(A)&image(B),'image intersection inclusion')
            require(preserves==injective,'exact workshop injectivity characterization')
            if ne==nf and all(values[values[i]]==values[i] for i in E):
                fixed={i for i in E if values[i]==i}
                require(image(E)==fixed,'idempotent image=fixed points')
                for i in E:
                    fibre={j for j in E if values[j]==values[i]}
                    require(len(fibre&fixed)==1,'unique fixed point per fibre')
                if injective or len(image(E))==ne:
                    require(all(values[i]==i for i in E),'injective/surjective idempotent')

# Final workshop: independently enumerate circular binary words.
M=((1,1),(1,0))
A=((1,0),(0,1))
for n in range(1,17):
    A=tuple(tuple(sum(A[i][k]*M[k][j] for k in range(2)) for j in range(2)) for i in range(2))
    valid=sum(not any(word[i] and word[(i+1)%n] for i in range(n)) for word in product((0,1),repeat=n))
    require(valid==A[0][0]+A[1][1],'circular words trace')

# New covariance/sampling bridge: exact finite-space moments, including k=0,n.
for n in range(2,9):
    for k in range(n+1):
        samples=list(combinations(range(n),k)); size=len(samples)
        p=Q(k,n)
        for i in range(n):
            mean=Q(sum(i in S for S in samples),size)
            require(mean==p,'sampling marginal')
            for j in range(n):
                cov=Q(sum(i in S and j in S for S in samples),size)-p*p
                expected=p*(1-p)*(n*int(i==j)-1)/(n-1)
                require(cov==expected,'sampling covariance')
        # Direct expected variance of the invariant sum.
        require(all(len(S)==k for S in samples),'sampling zero variance invariant')

# New arithmetic bridge: exact inclusion-exclusion and finite error estimate.
for primes in ((2,), (2,3),(2,3,5)):
    q=1
    for p in primes:q*=p
    target=Q(1)
    for p in primes:target*=1-Q(1,p)
    for N in range(1,91):
        empirical=Q(sum(all(a%p for p in primes) for a in range(1,N+1)),N)
        require(abs(empirical-target)<=Q(2**len(primes)-1,N),'arithmetic density error')
        if N%q==0:
            for mask in range(2**len(primes)):
                selected=[p for i,p in enumerate(primes) if mask>>i&1]
                d=1
                for p in selected:d*=p
                require(Q(sum(a%d==0 for a in range(1,N+1)),N)==Q(1,d),'mutual divisibility independence')

# Revised periodic quadrature's rational certificate.
certificate=Q(16*44,43*2**10*factorial(10))+Q(48,factorial(20))
require(certificate==Q(9602693143,2179474715658240000),'quadrature certificate exact value')
require(certificate<Q(5,10**9),'quadrature certificate half-unit bound')
result={'checks_passed':checks,'scope':'Small finite functions and set identities; circular binary words; exact finite sampling covariance; arithmetic densities; rational Taylor/filter certificate. Finite checks support the written arguments and do not prove universal claims.'}
Path(__file__).with_name('independent-example-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
