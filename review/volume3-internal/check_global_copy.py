"""Finite support for the actual final-matter model/cover; no review approval."""
from fractions import Fraction as Q
from itertools import product, combinations
from pathlib import Path
from check_chapter12 import icosa_vertices, dot, minus

ROOT = Path(__file__).resolve().parents[2]


def check_afterword_and_cover():
    # Each marginal move can be fair while two moves are completely dependent:
    # repeat one fair bit twice. Position at t2 is then always0, disproving the
    # independent-model answer1/2 if the joint-model hypothesis is dropped.
    correlated_records=((0,0),(1,1))
    assert all(sum(record[i] for record in correlated_records)==1 for i in (0,1))
    assert sum(sum(record)%2==0 for record in correlated_records)==2
    assert Q(2,2) != (1+(1-2*Q(1,2))**2)/2
    for p in (Q(0),Q(1,10),Q(1,2),Q(3,4),Q(1)):
        previous=Q(1)
        for t in range(9):
            even=Q(0)
            for record in product((0,1),repeat=t):
                mass=Q(1)
                for move in record:
                    mass*=p if move else 1-p
                if sum(record)%2==0:
                    even+=mass
            formula=(1+(1-2*p)**t)/2
            assert even==formula
            if t:assert even==p+(1-2*p)*previous
            previous=even
        matrix=((1-p,p),(p,1-p))
        for v,eigenvalue in [((1,1),1),((1,-1),1-2*p)]:
            assert tuple(sum(x*y for x,y in zip(row,v)) for row in matrix)==tuple(eigenvalue*x for x in v)
    phi,vertices=icosa_vertices()
    edges=[(i,j) for i,j in combinations(range(12),2)
           if dot(minus(vertices[i],vertices[j]),minus(vertices[i],vertices[j]))==4]
    faces=[t for t in combinations(range(12),3)
           if all(tuple(sorted(p)) in edges for p in combinations(t,2))]
    assert (len(vertices),len(edges),len(faces))==(12,30,20)
    normals=set()
    for i,j in edges:
        m=tuple((x+y)/2 for x,y in zip(vertices[i],vertices[j]))
        first=next(x for x in m if x!=0);m=tuple(x/first for x in m)
        normals.add(m)
        assert {tuple(x-2*dot(m,v)*y/dot(m,m) for x,y in zip(v,m)) for v in vertices}==set(vertices)
    assert len(normals)==15


if __name__=='__main__':
    check_afterword_and_cover()
    print('Exact afterword finite records/eigenvalues/endpoints and cover geometry pass; no approval generated.')
