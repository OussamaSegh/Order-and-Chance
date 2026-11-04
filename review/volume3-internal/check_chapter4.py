"""Actual rectangle-loop data, permutation/rotation boundaries and a bounded constant."""
import itertools
import math
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT/'volume3-symmetry/chapters/ch04-symmetric.tex'


def rectangle(corner):
    r, c = divmod(corner-1, 4)
    path = [(3,3)]+[(3,j) for j in range(2,c-1,-1)]+[(i,c) for i in range(2,r-1,-1)]
    path += [(r,j) for j in range(c+1,4)]+[(i,3) for i in range(r+1,4)]
    board = list(range(1,17))
    for (a,b),(u,v) in zip(path,path[1:]):
        assert abs(a-u)+abs(b-v) == 1
        x,y = 4*a+b,4*u+v
        assert board[x] == 16
        board[x],board[y] = board[y],board[x]
    assert board[15] == 16
    return {tile:board.index(tile)+1 for tile in range(1,16)}


def check_puzzle():
    source = SOURCE.read_text()
    for corner, cycle in re.findall(r'Corner \$(\d+)\$: \$([^$]+)\$', source):
        actual = rectangle(int(corner))
        points = list(map(int,re.findall(r'\d+',cycle)))
        if points[-1] == points[0]: points.pop()
        claimed = dict(zip(points,points[1:]+points[:1]))
        assert {k:v for k,v in actual.items() if k != v} == claimed
    seed = rectangle(11)
    assert {k:v for k,v in seed.items() if k != v} == {15:12,12:11,11:15}
    s = {11,12,15}
    h = rectangle(10)
    assert len({h[x] for x in s} & s) == 2
    s |= {h[x] for x in s}
    stages = [(10,11,12,[10]),(9,11,12,[10]),(9,10,11,[9]),
              (7,11,15,[12,8]),(3,11,15,[8,4]),(5,13,14,[7,6]),(1,13,14,[3,2])]
    for corner,x,y,zs in stages:
        h = rectangle(corner)
        for z in zs:
            assert len({x,y,z}) == 3 and {x,y,z} <= s and len(s) >= 4
            assert h[x] in s and h[y] in s and h[z] not in s
            s.add(h[z])
    assert s == set(range(1,16))


def check_edge_orientations():
    # Coordinates: x=R,y=U,z=F. Work on facets of positions, independent of
    # which cubie or orientation occupies a position in a scrambled cube.
    normals = [(a,sign) for a in range(3) for sign in (-1,1)]
    edges = [frozenset((x,y)) for x,y in itertools.combinations(normals,2) if x[0] != y[0]]
    primary = lambda e: next((x for x in e if x[0] == 1), next(x for x in e if x[0] == 2))
    # Avoid eager default evaluation when the edge contains U/D but not F/B.
    def primary(e):
        return next(x for x in e if x[0] == (1 if any(a==1 for a,_ in e) else 2))
    for axis,side in normals:
        other = [a for a in range(3) if a != axis]
        def rotate(facet):
            a,sign = facet
            if a == axis:return facet
            return (other[1],sign) if a == other[0] else (other[0],-sign)
        changed = []
        for e in edges:
            if (axis,side) not in e:continue
            dest = frozenset(map(rotate,e))
            changed.append(rotate(primary(e)) != primary(dest))
        assert len(changed) == 4
        assert changed == [axis == 2]*4
        # Toggling 4 arbitrary bits changes the total by an even integer.
        for bits in itertools.product((0,1),repeat=4):
            assert (sum(1-b for b in bits)-sum(bits)) % 2 == 0


def check_permutation_cases():
    compose = lambda a,b: tuple(a[b[i]] for i in range(len(a)))
    def inverse(a):
        return tuple(a.index(i) for i in range(len(a)))
    def cycles(a):
        seen=set(); result=[]
        for x in range(len(a)):
            if x in seen:continue
            c=[];y=x
            while y not in seen:
                seen.add(y);c.append(y);y=a[y]
            if len(c)>1:result.append(c)
        return result
    def cycle(n,pts):
        a=list(range(n))
        for x,y in zip(pts,pts[1:]+pts[:1]):a[x]=y
        return tuple(a)
    def comm(a,b):return compose(compose(compose(a,b),inverse(a)),inverse(b))
    for n in range(5,9):
        for sigma in itertools.permutations(range(n)):
            cs=cycles(sigma)
            if not cs or sum(len(c)-1 for c in cs)%2:continue
            long=next((c for c in cs if len(c)>=4),None)
            threes=[c for c in cs if len(c)==3]
            if long:
                result=comm(cycle(n,long[:3]),sigma)
                assert sorted(map(len,cycles(result))) == [3]
            elif len(threes)>=2:
                a,b=threes[:2]
                result=comm(cycle(n,[a[0],a[1],b[0]]),sigma)
                assert sorted(map(len,cycles(result))) == [5]
            elif len(threes)==1:
                result=compose(sigma,sigma)
                assert sorted(map(len,cycles(result))) == [3]
            else:
                a,b=cs[:2]
                rho=comm(cycle(n,[a[0],a[1],b[0]]),sigma)
                assert sorted(map(len,cycles(rho))) == [2,2]
                rs=cycles(rho);outside=next(i for i in range(n) if rho[i]==i)
                result=comm(cycle(n,rs[0]+[outside]),rho)
                assert sorted(map(len,cycles(result))) == [3]
    assert pow(2,8,51)==1 and all(pow(2,k,51)!=1 for k in (1,2,4))
    assert pow(2,26,53)==52 and pow(2,4,53)!=1
    # n=1 is a counterexample to the old unrestricted splitting lemma.
    lemma=re.search(r'\\begin\{lemma\}\\label\{lem:split\}(.*?)\\end\{lemma\}',SOURCE.read_text(),re.S)[1]
    assert r'n\ge2' in lemma


def check_probability_constant():
    import mpmath as mp
    mp.iv.dps=45;v=mp.iv;lower=v.mpf(1);upper=v.mpf(1)
    for j in range(1,1001):
        term=v.mpf(1);subtotal=term
        for k in range(1,13):
            term=term/(j*j*k*k);subtotal+=term
        tail=(term/(j*j*13*13))/(1-v.mpf(1)/(j*j*14*14))
        lower*=subtotal;upper*=subtotal+tail
    lower*=v.exp(v.mpf(1)/1001-v.mpf(1)/(6*1000**3))
    upper*=v.exp(v.mpf(1)/1000)
    assert float(lower.a)>4.263401 and float(upper.b)<4.263406


if __name__=='__main__':
    check_puzzle()
    check_edge_orientations()
    check_permutation_cases()
    check_probability_constant()
    print('PASS: actual puzzle rectangle data/growth; every edge-facet convention; An cases n5..8; shuffles; outward constant bounds')
