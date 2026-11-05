"""Exact matrix/table and curricular-order regressions supporting the C7 review."""
import itertools
import math
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/'volume3-symmetry/chapters/ch07-modules.tex'


def matmul(a,b,p=None):
    n=len(a);m=len(b[0]) if b else 0;k=len(b)
    result=[[sum(a[i][z]*b[z][j] for z in range(k)) for j in range(m)] for i in range(n)]
    return [[x%p for x in row] for row in result] if p else result


def rank(a,p):
    a=[row[:] for row in a];r=0
    for c in range(len(a[0]) if a else 0):
        pivot=next((j for j in range(r,len(a)) if a[j][c]%p),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r];u=pow(a[r][c]%p,-1,p);a[r]=[x*u%p for x in a[r]]
        for j in range(len(a)):
            if j!=r:
                u=a[j][c];a[j]=[(x-u*y)%p for x,y in zip(a[j],a[r])]
        r+=1
    return r


def determinant(a):
    n=len(a)
    return sum((-1)**sum(s[i]>s[j] for i in range(n) for j in range(i+1,n))*math.prod(a[i][s[i]] for i in range(n)) for s in itertools.permutations(range(n)))


def check_actual_smith_and_table():
    plate=(ROOT/'volume3-symmetry/figures/ch07-smith.tex').read_text()
    blocks=re.findall(r'\\begin\{pmatrix\}(.*?)\\end\{pmatrix\}',plate)
    matrices=[[[int(v) for v in row.split('&')] for row in b.split(r'\\')] for b in blocks]
    assert len(matrices)==5
    a=[row[:] for row in matrices[0]]
    a[1]=[x+3*y for x,y in zip(a[1],a[0])];a[2]=[x-5*y for x,y in zip(a[2],a[0])]
    for row in a:row[1]-=2*row[0];row[2]-=2*row[0]
    assert a==matrices[1]
    a[2]=[x+y for x,y in zip(a[2],a[1])];assert a==matrices[2]
    a[1],a[2]=a[2],a[1];a[2]=[x+3*y for x,y in zip(a[2],a[1])]
    for row in a:row[2]-=2*row[1]
    assert a==matrices[3]
    a[1]=[-x for x in a[1]];a[2]=[-x for x in a[2]];assert a==matrices[4]
    gcds=[]
    for k in range(1,4):
        minors=[determinant([[matrices[0][i][j] for j in cols] for i in rows]) for rows in itertools.combinations(range(3),k) for cols in itertools.combinations(range(3),k)]
        gcds.append(math.gcd(*minors))
    assert gcds==[2,12,144]
    table=re.search(r'\\begin\{tabular\}\{ll\}(.*?)\\end\{tabular\}',SOURCE.read_text(),re.S)[1]
    signatures=[]
    for line in table.splitlines():
        if '&' not in line or not line.startswith('$'):continue
        left,right=line.split('&');elementary=list(map(int,re.findall(r'\d+',left)));invariants=list(map(int,re.findall(r'\\Z/(\d+)',right)))
        assert math.prod(elementary)==math.prod(invariants)==360
        assert all(y%x==0 for x,y in zip(invariants,invariants[1:]))
        def exponents(values,p):
            result=[]
            for x in values:
                k=0
                while x%p==0:k+=1;x//=p
                if k:result.append(k)
            return sorted(result)
        signature=tuple(tuple(exponents(invariants,p)) for p in (2,3,5))
        assert signature==tuple(tuple(exponents(elementary,p)) for p in (2,3,5))
        signatures.append(signature)
    assert len(set(signatures))==6


def partitions(n,least=1):
    if n==0:yield []
    for k in range(least,n+1):
        for tail in partitions(n-k,k):yield [k]+tail


def check_jordan_and_units():
    for n in range(8):
        recovered=set()
        for blocks in partitions(n):
            a=[[0]*n for _ in range(n)];offset=0
            for size in blocks:
                for j in range(size-1):a[offset+j][offset+j+1]=1
                offset+=size
            signatures=[]
            for p in (2,3,5):
                power=[[int(i==j) for j in range(n)] for i in range(n)];h=[0]
                for k in range(1,n+2):
                    power=matmul(power,a,p);h.append(n-rank(power,p))
                counts=[2*h[k]-h[k-1]-h[k+1] for k in range(1,n+1)]
                assert [k for k,c in enumerate(counts,1) for _ in range(c)]==blocks
                signatures.append(tuple(h))
            assert len(set(signatures))==1;recovered.add(signatures[0])
        assert len(recovered)==sum(1 for _ in partitions(n))
    units=[a for a in range(360) if math.gcd(a,360)==1]
    assert len(units)==96
    assert next(e for e in range(1,97) if all(pow(a,e,360)==1 for a in units))==12
    for k in range(3,14):
        modulus=2**k;powers={pow(5,j,modulus) for j in range(2**(k-2))}
        assert len(powers)==2**(k-2) and powers.isdisjoint({(-x)%modulus for x in powers})
        assert powers|{(-x)%modulus for x in powers}==set(range(1,modulus,2))


def check_migration_and_zero_scope():
    source=SOURCE.read_text();target=(ROOT/'volume3-symmetry/chapters/ch10-galois.tex').read_text()
    assert 'pb:kronecker' not in source
    for kind in ('exercise','hint','solution'):
        start=lambda key:target.index((r'\label{'+key+'}') if kind=='exercise' else (r'\begin{'+kind+'}{'+key+'}'))
        assert start('ex:phin')<start('pb:kronecker')
    problem=re.search(r'\\begin\{solution\}\{pb:kronecker\}(.*?)\\end\{solution\}',target,re.S)[1]
    assert 'algebraic integers (Chapter' not in problem
    theorem=re.search(r'\\begin\{theorem\}\[rational canonical form; Frobenius\](.*?)\\end\{theorem\}',source,re.S)[1]
    assert 'n=0' in theorem and r'n\ge1' in theorem


def check_cyclic_vectors_and_power_example():
    """Exact zero/small-field probes; these support the general module proof."""
    checked=0
    for p in (2,3):
        for n in range(3):
            for flat in itertools.product(range(p),repeat=n*n):
                a=[list(flat[i*n:(i+1)*n]) for i in range(n)]
                identity=[[int(i==j) for j in range(n)] for i in range(n)]
                powers=[identity]
                for _ in range(n):powers.append(matmul(powers[-1],a,p))
                def kills(coefficients):
                    return all(sum(c*powers[k][i][j] for k,c in
                                   enumerate(coefficients))%p==0
                               for i in range(n) for j in range(n))
                minimal=None
                for degree in range(n+1):
                    for coefficients in itertools.product(range(p),repeat=degree):
                        candidate=(*coefficients,1)
                        if kills(candidate):minimal=candidate;break
                    if minimal is not None:break
                characteristic=((1,) if n==0 else ((-a[0][0])%p,1)
                                if n==1 else
                                (determinant(a)%p,(-a[0][0]-a[1][1])%p,1))
                cyclic=False
                for v in itertools.product(range(p),repeat=n):
                    vectors=[];w=list(v)
                    for _ in range(n):
                        vectors.append(w)
                        w=[sum(a[i][j]*w[j] for j in range(n))%p for i in range(n)]
                    columns=[[vectors[j][i] for j in range(n)] for i in range(n)]
                    if rank(columns,p)==n:cyclic=True;break
                assert (minimal==characteristic)==cyclic
                roots=[x for x in range(p) if sum(c*pow(x,k,p)
                       for k,c in enumerate(minimal))%p==0]
                split=[1]
                for root in roots:
                    out=[0]*(len(split)+1)
                    for k,c in enumerate(split):
                        out[k]=(out[k]-root*c)%p;out[k+1]=(out[k+1]+c)%p
                    split=out
                eigenvectors=[]
                for eigenvalue in roots:
                    for v in itertools.product(range(p),repeat=n):
                        if all(sum(a[i][j]*v[j] for j in range(n))%p==eigenvalue*v[i]%p
                               for i in range(n)):eigenvectors.append(v)
                eigenbasis_rank=rank([[v[i] for v in eigenvectors] for i in range(n)],p)
                assert (tuple(split)==minimal)==(eigenbasis_rank==n)
                if n==0:
                    assert minimal==characteristic==(1,) and cyclic
                    # The old unqualified hint's r=1 conclusion fails here:
                    # the invariant-factor list is empty, although mu=chi.
                checked+=1
    assert checked==104
    a=[[1,1],[0,1]];power=[[1,0],[0,1]]
    for t in range(21):
        assert power==[[1,t],[0,1]]
        power=matmul(power,a)
    # Hatcher2.4 gives relations -a+b+c and a-b+c in basis(a-b,c).
    # The independent algebraic Smith invariants are1,2, agreeing with the
    # one-cell relation(2) in his2.42. Geometric identifications are external.
    relations=[[-1,1],[1,1]]
    assert math.gcd(*(x for row in relations for x in row))==1
    assert abs(determinant(relations))==2


if __name__=='__main__':
    check_actual_smith_and_table()
    check_jordan_and_units()
    check_migration_and_zero_scope()
    check_cyclic_vectors_and_power_example()
    print('PASS: every actual Smith arrow/minor; all360 table rows; Jordan kernels n0..7,char2/3/5; units/exponent; complete curricular migration')
