import math
def T_short(n): return n//2 if n%2==0 else (3*n+1)//2
def T_std(n): return n//2 if n%2==0 else 3*n+1
def tree(N,ae,ao,L=1.0,shrink=1.0,std=False,upright=True):
    T=T_std if std else T_short
    parent={};count={}
    for n in range(2,N+1):
        m=n
        while m!=1:
            count[m]=count.get(m,0)+1
            p=T(m); parent[m]=p; m=p
    count[1]=N
    pos={1:(0.0,0.0)};ang={1:math.pi/2};depth={1:0}
    for m0 in list(parent):
        stack=[];m=m0
        while m not in pos: stack.append(m); m=parent[m]
        for k in reversed(stack):
            p=parent[k]; a=ang[p]+(ae if k%2==0 else -ao); d=depth[p]+1
            l=L*shrink**d; x,y=pos[p]
            pos[k]=(x+l*math.cos(a),y+l*math.sin(a)); ang[k]=a; depth[k]=d
    if upright:  # rotate about the root so the orbit-weighted centre of mass is straight above 1
        W=sum(count.get(m,1) for m in pos); cx=sum(pos[m][0]*count.get(m,1) for m in pos)/W; cy=sum(pos[m][1]*count.get(m,1) for m in pos)/W
        th=math.pi/2-math.atan2(cy,cx); c,s=math.cos(th),math.sin(th)
        pos={m:(c*x-s*y,s*x+c*y) for m,(x,y) in pos.items()}
    return parent,count,pos
