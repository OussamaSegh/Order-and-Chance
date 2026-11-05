"""Substantive finite probes for global C1 reasoning/actual geometry, not proof approval."""
from fractions import Fraction as Q
from collections import Counter
from itertools import product, permutations, combinations
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[2]


def check_field_power_and_actual_axes():
    # Both additive C4 and nonzero multiplicative C3 satisfy the old abbreviated
    # listed properties, yet distributivity fails. Intended genuine fields are
    # not counterexamples; the reader-facing axiom list needed completion.
    units=(1,2,3)
    def times(a,b):
        return 0 if not a or not b else units[(units.index(a)+units.index(b))%3]
    assert all(times(a,times(b,c))==times(times(a,b),c) for a,b,c in product(range(4),repeat=3))
    assert all(times(a,b)==times(b,a) for a,b in product(range(4),repeat=2))
    assert all(any(times(a,b)==1 for b in units) for a in units)
    assert times(2,(1+1)%4)==3 != (times(2,1)+times(2,1))%4
    determinant=lambda a:(times(a[0][0],a[1][1])-times(a[0][1],a[1][0]))%4
    a=((2,0),(0,2));b=((1,1),(1,0))
    ab=tuple(tuple(sum(times(a[i][k],b[k][j]) for k in range(2))%4
                   for j in range(2)) for i in range(2))
    assert determinant(ab)==1 != times(determinant(a),determinant(b))==2
    compose=lambda a,b:tuple(a[b[i]] for i in range(len(a)))
    def power(g,n):
        if n<0:
            g=tuple(g.index(i) for i in range(len(g)));n=-n
        result=tuple(range(len(g)))
        for _ in range(n):result=compose(result,g)
        return result
    for g in permutations(range(3)):
        for m,n in product(range(-7,8),repeat=2):
            assert compose(power(g,m),power(g,n))==power(g,m+n)
            assert power(power(g,m),n)==power(g,m*n)
    for p in (2,3,5,7,11):
        by_polynomial=Counter(((a+d)%p,(a*d-b*c)%p)
                              for a,b,c,d in product(range(p),repeat=4))
        root_counts=Counter()
        for t,d in product(range(p),repeat=2):
            roots=sum((x*x-t*x+d)%p==0 for x in range(p))
            root_counts[roots]+=1
            assert by_polynomial[t,d]==p*(p-1)+p*roots
        assert root_counts=={0:p*(p-1)//2,1:p,2:p*(p-1)//2}
    source=(ROOT/'volume3-symmetry/figures/ch01-symmetries.tex').read_text()
    cells=re.findall(r'\\node\[font=\\tiny,text=(?:black|white)\] at \(([-.\d]+),([-.\d]+)\) \{\$(.*?)\$\};',source)
    labels=['e','r','r^2','r^3','s','sr','sr^2','sr^3']
    assert len(cells)==64
    for x,y,label in cells:
        row=round((-float(y)-.31)/.62);column=round((float(x)-.31)/.62)
        e,k=divmod(row,4);f,l=divmod(column,4)
        result=4*((e+f)%2)+(((-1)**f*k+l)%4)
        assert label==labels[result]
    # Independent affine projection of all cube vertices/12 edges. No source
    # claim of an orthographic/isometric projection is made.
    project=lambda u,v,w:(Q('6.6')+Q('2.5')*u+Q('1.1')*w,
                          Q('-4.25')+Q('2.5')*v+Q('.8')*w)
    vertices={bits:project(*bits) for bits in product((0,1),repeat=3)}
    expected={frozenset((vertices[a],vertices[b])) for a,b in combinations(vertices,2)
              if sum(x!=y for x,y in zip(a,b))==1}
    cube=source.split(r'\begin{scope}')[2]
    segments=re.findall(r'\\draw\[(?:black|gray,dashed)\] \(([-\d.]+),([-\d.]+)\) -- \(([-\d.]+),([-\d.]+)\);',cube)
    actual={frozenset(((Q(a),Q(b)),(Q(c),Q(d)))) for a,b,c,d in segments}
    assert len(segments)==12 and actual==expected
    center=project(Q(1,2),Q(1,2),Q(1,2))
    axis_points={
        'MidnightBlue':(project(Q(1,2),0,Q(1,2)),project(Q(1,2),1,Q(1,2))),
        'BrickRed':(project(0,0,0),project(1,1,1)),
        'ForestGreen':(project(1,0,Q(1,2)),project(0,1,Q(1,2)))}
    for color,(u,v) in axis_points.items():
        match=re.search(r'\\draw\['+color+r',very thick\] \(([-\d.]+),([-\d.]+)\) -- \(([-\d.]+),([-\d.]+)\)',cube)
        a,b,c,d=map(Q,match.groups());dx,dy=c-a,d-b
        # Node coordinates rounded to3 decimals; normalize cross error by
        # line L1 length, bounding geometric distance by0.001 model unit.
        for x,y in (u,v,center):
            assert abs(dx*(y-b)-dy*(x-a)) <= Q(1,1000)*(abs(dx)+abs(dy))
    for label in ('$3\\times3=9$','$4\\times2=8$','$6\\times1=6$','$1+9+8+6=24$'):
        assert label in cube


if __name__=='__main__':
    check_field_power_and_actual_axes()
    print('C1 exact field countermodel,all S3 mixed powers,64D4 cells/12cube edges/3axes pass; no approval generated.')
