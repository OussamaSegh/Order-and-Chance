"""Exact finite support for Paley/Sylvester; never general proof or approval."""
from itertools import product
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT/'volume3-symmetry/chapters/paley.tex'


def finite_field(p, modulus):
    """Polynomial-coordinate arithmetic; modulus is monic, constant first."""
    d = len(modulus)-1
    q = p**d
    def digits(a):
        answer = []
        for _ in range(d):
            answer.append(a % p)
            a //= p
        return answer
    def encode(a):
        return sum((x % p)*p**i for i, x in enumerate(a))
    def add(a, b):
        return encode([x+y for x, y in zip(digits(a), digits(b))])
    def neg(a):
        return encode([-x for x in digits(a)])
    def mul(a, b):
        coeff = [0]*(2*d-1)
        for i, x in enumerate(digits(a)):
            for j, y in enumerate(digits(b)):
                coeff[i+j] = (coeff[i+j]+x*y) % p
        for k in range(2*d-2, d-1, -1):
            leading = coeff[k]
            for j in range(d+1):
                coeff[k-d+j] = (coeff[k-d+j]-leading*modulus[j]) % p
        return encode(coeff[:d])
    def power(a, exponent):
        value = 1
        while exponent:
            if exponent & 1:
                value = mul(value, a)
            a = mul(a, a)
            exponent //= 2
        return value
    # Actual finite verification of chosen moduli: each nonzero element has an
    # explicit inverse in this quotient. General field existence is proved C9.
    assert modulus[-1] == 1
    for a in range(1, q):
        assert power(a, q-1) == 1
        assert mul(a, power(a, q-2)) == 1
    assert all(add(a, neg(a)) == 0 for a in range(q))
    return q, add, neg, mul, power


def gram(a):
    return [[sum(x*y for x, y in zip(row, other)) for other in a] for row in a]


def is_hadamard(a):
    n = len(a)
    return n >= 1 and all(len(row) == n and set(row) <= {-1, 1} for row in a) and \
        gram(a) == [[n*int(i == j) for j in range(n)] for i in range(n)]


def check_sylvester_and_source_examples():
    a = [[1]]
    for k in range(7):
        assert len(a) == 2**k and is_hadamard(a)
        assert a == [[(-1)**((i & j).bit_count()) for j in range(2**k)] for i in range(2**k)]
        a = [row+row for row in a]+[row+[-x for x in row] for row in a]
    source = SOURCE.read_text()
    for key, expected in [
        ('ex:paley-h4',[[1,1,1,1],[1,-1,1,-1],[1,1,-1,-1],[1,-1,-1,1]]),
        ('ex:paley-f3',[[1,1,1,1],[-1,1,-1,1],[-1,1,1,-1],[-1,-1,1,1]])]:
        solution = re.search(r'\\begin\{solution\}\{'+re.escape(key)+r'\}(.*?)\\end\{solution\}',source,re.S).group(1)
        block = re.search(r'H_4=\s*\\begin\{pmatrix\}(.*?)\\end\{pmatrix\}',solution,re.S) if key.endswith('h4') else \
            re.search(r'H=\\begin\{pmatrix\}(.*?)\\end\{pmatrix\}',solution,re.S)
        actual = [[int(x.strip()) for x in row.split('&')] for row in block.group(1).strip().split(r'\\')]
        assert actual == expected and is_hadamard(actual)
    # All sign rows for n1..7: a normalized first row can extend to n
    # orthogonal rows only for n1/2/4 in this range. This finite support does
    # not replace the four-column-type divisibility proof.
    for n in range(1,8):
        balanced = [r for r in product((-1,1),repeat=n) if sum(r)==0]
        if n > 2 and n % 4:
            assert not any(sum(x*y for x,y in zip(r,s)) == 0 for r in balanced for s in balanced)
    left = [[1,1],[1,-1]]; right = [[1,-1],[-1,-1]]
    multiply = lambda a,b:[[sum(x*y for x,y in zip(row,column)) for column in zip(*b)] for row in a]
    assert multiply(left,left) == multiply(right,right) == [[2,0],[0,2]]
    ab,ba = multiply(left,right),multiply(right,left)
    assert all(ab[i][j]+ba[i][j] == 0 for i,j in product(range(2),repeat=2))


def check_prime_power_character_and_paley():
    fields=[(p,(0,1)) for p in (3,5,7,11,13,17,19,23,29,31)]
    fields += [(3,(1,0,1)),(5,(2,0,1)),(3,(1,2,0,1)),(7,(1,0,1))]
    for p,modulus in fields:
        q,add,neg,mul,power = finite_field(p,modulus)
        squares={mul(a,a) for a in range(1,q)}
        chi=lambda a:0 if a==0 else 1 if a in squares else -1
        assert len(squares)==(q-1)//2 and sum(chi(a) for a in range(q))==0
        assert chi(neg(1)) == (-1)**((q-1)//2)
        for a,b in product(range(q),repeat=2):
            assert chi(mul(a,b))==chi(a)*chi(b)
        for c in range(1,q):
            correlation=sum(chi(x)*chi(add(x,c)) for x in range(q))
            assert correlation == -1
            conic=sum(mul(u,u)==mul(t,add(t,c)) for t,u in product(range(q),repeat=2))
            assert conic==q-1==q+correlation
        Q=[[chi(add(x,neg(y))) for y in range(q)] for x in range(q)]
        assert all(sum(row)==0 for row in Q) and all(sum(col)==0 for col in zip(*Q))
        assert gram(Q)==[[q*int(x==y)-1 for y in range(q)] for x in range(q)]
        assert all(Q[y][x]==chi(neg(1))*Q[x][y] for x,y in product(range(q),repeat=2))
        n=q+1; epsilon=chi(neg(1)); S=[[0]+[1]*q]+[[epsilon]+row for row in Q]
        assert gram(S)==[[q*int(x==y) for y in range(n)] for x in range(n)]
        if q%4==3:
            H=[[x+int(i==j) for j,x in enumerate(row)] for i,row in enumerate(S)]
            assert len(H)==q+1 and is_hadamard(H)
        else:
            plus=[[x+int(i==j) for j,x in enumerate(row)] for i,row in enumerate(S)]
            minus=[[x-int(i==j) for j,x in enumerate(row)] for i,row in enumerate(S)]
            H=[a+b for a,b in zip(plus,minus)]+[a+[-x for x in b] for a,b in zip(minus,plus)]
            assert len(H)==2*(q+1) and is_hadamard(H)
            assert not is_hadamard(plus)  # Wrong congruence branch cannot use I+S.
        assert len(H)%4==0


def check_local_contract(source=None):
    source=SOURCE.read_text() if source is None else source
    assert 'For a positive integer $n$' in source
    assert 'Then $S_{2^k}$ is Hadamard of order $2^k$' in source
    assert 'for every integer $k\\ge0$' in source
    assert 'matrix products below are taken over $\\R$' in source
    assert 'independently verified in October' not in source
    assert 'arXiv:2610.27175v1' in source
    assert '\\sum_{j,s}a_{ij}b_{rs}c_{jk}d_{st}' in source


if __name__=='__main__':
    check_sylvester_and_source_examples()
    check_prime_power_character_and_paley()
    check_local_contract()
    print('Exact Sylvester/Paley examples and14 odd prime-power fields pass; no approval generated.')
