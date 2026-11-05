"""Exact finite probes supporting, never replacing, the Chapter 5 proofs."""
import itertools
import math
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]


def compose(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def generated(generators, identity, multiply):
    seen = {identity}
    todo = [identity]
    while todo:
        a = todo.pop()
        for b in generators:
            c = multiply(a, b)
            if c not in seen:
                seen.add(c)
                todo.append(c)
    return frozenset(seen)


def check_sylow_and_derived():
    group = list(itertools.permutations(range(4)))
    identity = tuple(range(4))
    inverse = lambda a: tuple(a.index(i) for i in range(4))
    cyclic = {generated([g], identity, compose) for g in group}
    assert len({h for h in cyclic if len(h) == 3}) == 4
    partitions = [frozenset((frozenset((0,i)), frozenset(set(range(4))-{0,i}))) for i in (1,2,3)]
    image = lambda g, p: frozenset(frozenset(g[i] for i in part) for part in p)
    stabilizers = {frozenset(g for g in group if image(g,p) == p) for p in partitions}
    assert len(stabilizers) == 3 and {len(h) for h in stabilizers} == {8}
    for h in stabilizers:
        assert {g for g in group if frozenset(compose(compose(g,x),inverse(g)) for x in h) == h} == set(h)
    derived = lambda h: generated([compose(compose(compose(a,b),inverse(a)),inverse(b)) for a in h for b in h], identity, compose)
    a4 = derived(group)
    v4 = derived(a4)
    assert [len(a4),len(v4),len(derived(v4))] == [12,4,1]
    a,b = (1,2,0,3),(1,3,2,0)
    assert compose(compose(compose(a,b),inverse(a)),inverse(b)) == (1,0,3,2)
    for p in (2,3,5,7):
        for a in range(4):
            for m in range(1,10):
                assert math.comb(p**a*m,p**a) % p == m % p


def check_gl2():
    for p in (2,3,5,7):
        def mul(a,b):
            x,y,z,w=a;v,r,s,t=b
            return ((x*v+y*s)%p,(x*r+y*t)%p,(z*v+w*s)%p,(z*r+w*t)%p)
        def inverse(a):
            x,y,z,w=a;d=pow((x*w-y*z)%p,-1,p)
            return (w*d%p,-y*d%p,-z*d%p,x*d%p)
        group=[a for a in itertools.product(range(p),repeat=4) if (a[0]*a[3]-a[1]*a[2])%p]
        u=frozenset((1,x,0,1) for x in range(p))
        conjugate=lambda g:frozenset(mul(mul(g,x),inverse(g)) for x in u)
        conjugates={conjugate(g) for g in group}
        normalizer={g for g in group if conjugate(g)==u}
        assert normalizer == {g for g in group if g[2]==0}
        assert len(normalizer)==p*(p-1)**2 and len(conjugates)==p+1
        lines=set()
        for h in conjugates:
            fixed=frozenset((x,y) for x,y in itertools.product(range(p),repeat=2)
                            if all(((a*x+b*y)%p,(c*x+d*y)%p)==(x,y) for a,b,c,d in h))
            assert len(fixed)==p
            lines.add(fixed)
        assert len(lines)==p+1


def check_order12_and_plate():
    # Five explicit models, with orders of elements independently calculated.
    cyclic = lambda n: (list(range(n)),0,lambda a,b:(a+b)%n)
    c12=cyclic(12)
    c6c2=(list(itertools.product(range(6),range(2))),(0,0),lambda a,b:((a[0]+b[0])%6,(a[1]+b[1])%2))
    a4=([g for g in itertools.permutations(range(4)) if sum(g[i]>g[j] for i in range(4) for j in range(i+1,4))%2==0],tuple(range(4)),compose)
    d6=(list(itertools.product(range(6),range(2))),(0,0),lambda a,b:((a[0]+(-1)**a[1]*b[0])%6,(a[1]+b[1])%2))
    c3c4=(list(itertools.product(range(3),range(4))),(0,0),lambda a,b:((a[0]+(-1)**a[1]*b[0])%3,(a[1]+b[1])%4))
    signatures=[]
    for elements,identity,multiply in (c12,c6c2,a4,d6,c3c4):
        assert len(elements)==12
        orders=[]
        for a in elements:
            power=identity
            for k in range(1,13):
                power=multiply(power,a)
                if power==identity:
                    orders.append(k);break
            else:raise AssertionError('not a finite group model')
        signatures.append(tuple(sorted(orders)))
        assert all(multiply(multiply(a,b),c)==multiply(a,multiply(b,c)) for a,b,c in itertools.product(elements,repeat=3))
    assert len(set(signatures))==5
    plate=(ROOT/'volume3-symmetry/figures/ch05-small.tex').read_text()
    counts={n:len(re.findall(r'\(g'+str(n)+r'x\d+\)',plate)) for n in range(1,16)}
    assert list(counts.values())==[1,1,1,2,1,2,1,5,2,2,1,5,1,2,1]
    # The stale published count is now replaced by the documented correction.
    source=(ROOT/'volume3-symmetry/chapters/ch05-sylow.tex').read_text()
    assert r'49\,487\,367\,289' in source and r'49\,487\,365\,422' not in source


def check_small_order_arguments():
    source=(ROOT/'volume3-symmetry/chapters/ch05-sylow.tex').read_text()
    table=source.split(r'\label{tool:smallest-simple}',1)[1].split(r'\end{tabular}',1)[0]
    rows=re.findall(r'\$(\d+)\$ & \$([\d,]+)\$',table)
    def factor(n):
        out={};p=2
        while p*p<=n:
            while n%p==0:
                out[p]=out.get(p,0)+1;n//=p
            p+=1
        if n>1:out[n]=out.get(n,0)+1
        return out
    def possibilities(n,p):
        m=n//p**factor(n)[p]
        return [d for d in range(1,m+1) if m%d==0 and d%p==1]
    covered=set()
    for p,orders in rows:
        for n in map(int,orders.split(',')):
            assert n not in covered and possibilities(n,int(p))==[1]
            covered.add(n)
    exceptions={12,24,30,36,48,56}
    assert len(covered)==27
    assert covered|exceptions=={n for n in range(2,60) if len(factor(n))>1}
    assert not covered&exceptions
    assert all(possibilities(n,3)==[1,4] for n in [12,24,36])
    assert possibilities(48,3)==[1,4,16] and 48-16*2==16
    assert possibilities(56,7)==[1,8] and 56-8*6==8
    assert possibilities(30,5)==[1,6] and possibilities(30,3)==[1,10]
    assert 6*4+10*2>29
    assert [possibilities(60,p) for p in [2,3,5]]==[[1,3,5,15],[1,4,10],[1,6]]
    assert 60>math.factorial(4)>math.factorial(3)
    assert 60-1-6*4-10*2==15 and 15*2>15 and 15*3>15
    assert [d for d in range(5,61) if 60%d==0 and d%4==0]==[12,20,60]
    group=[g for g in itertools.permutations(range(5))
           if sum(g[i]>g[j] for i in range(5) for j in range(i+1,5))%2==0]
    identity=tuple(range(5))
    cyclic={generated([g],identity,compose) for g in group}
    assert len([h for h in cyclic if len(h)==5])==6
    assert len([h for h in cyclic if len(h)==3])==10
    involutions=[g for g in group if g!=identity and compose(g,g)==identity]
    sylows={generated([a,b],identity,compose) for a,b in itertools.combinations(involutions,2)
            if compose(a,b)==compose(b,a)}
    assert len(involutions)==15 and len(sylows)==5 and {len(h) for h in sylows}=={4}
    for a in involutions:
        assert sum(a in h for h in sylows)==1
        assert len([g for g in group if compose(g,a)==compose(a,g)])==4


if __name__=='__main__':
    check_sylow_and_derived()
    check_gl2()
    check_order12_and_plate()
    check_small_order_arguments()
    print('PASS: S4 Sylows/derived; binomial boundaries; GL2 p2,3,5,7; order12 models/plate/count; all27 new table orders/six exceptions and exact A5 Sylows/centralizers')
