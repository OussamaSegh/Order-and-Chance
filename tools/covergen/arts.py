"""Exact illustrations for Volumes 2-15 (model units; scene.py fits and centres them)."""
import math, cmath, json
from pathlib import Path
import numpy as np
from scene import Scene
HERE = Path(__file__).resolve().parent
IV='ocCoverTitle'
def isprime(n):
    if n<2: return False
    if n%2==0: return n==2
    r=int(n**.5)
    for d in range(3,r+1,2):
        if n%d==0: return False
    return True

# 2 The Integers -- Ulam spiral of 1..71^2
def v2():
    s=Scene(); N=71*71; x=y=0; pts=[(0,0)]; dx,dy=1,0; step=1; n=1
    while n<N:
        for _ in range(2):
            for _ in range(step):
                if n>=N: break
                x+=dx;y+=dy;n+=1;pts.append((x,y))
            dx,dy=-dy,dx
        step+=1
    Rd=35.5
    for i,(a,b) in enumerate(pts,1):
        r=math.hypot(a,b)
        if isprime(i) and r<Rd: s.dot(a,b,0.30,op=0.95*(1-0.75*(r/Rd)**2),halo=0.5*(1-r/Rd))
    s.dot(0,0,0.42,col=IV,halo=1.0)
    return s,'bbox'

# 3 Symmetry -- icosahedron, its rotation axes and its 15 mirror circles
def v3():
    s=Scene(); f=(1+5**.5)/2
    V=[]
    for a in (-1,1):
        for b in (-f,f): V+=[(0,a,b),(a,b,0),(b,0,a)]
    V=np.array(V,float)
    E=[(i,j) for i in range(12) for j in range(i+1,12) if abs(np.linalg.norm(V[i]-V[j])-2)<1e-9]
    F=[(i,j,k) for (i,j) in E for k in range(j+1,12) if (i,k) in E and (j,k) in E]
    def R(ax,ang):
        ax=np.array(ax,float); ax/=np.linalg.norm(ax); c,s_=math.cos(ang),math.sin(ang); x,y,z=ax
        return np.array([[c+x*x*(1-c),x*y*(1-c)-z*s_,x*z*(1-c)+y*s_],[y*x*(1-c)+z*s_,c+y*y*(1-c),y*z*(1-c)-x*s_],[z*x*(1-c)-y*s_,z*y*(1-c)+x*s_,c+z*z*(1-c)]])
    M=R((1,0,0),-0.42)@R((0,0,1),0.30)@R((0,1,0),0.55)
    W=V@M.T; view=np.array([0,0,1.0])
    front={}
    for t in F:
        n=np.cross(W[t[1]]-W[t[0]],W[t[2]]-W[t[0]]); c=W[list(t)].mean(0)
        if n@c<0: n=-n
        vis=n@view>0
        for e in ((t[0],t[1]),(t[0],t[2]),(t[1],t[2])):
            e=tuple(sorted(e)); front[e]=front.get(e,False) or vis
    Rc=math.sqrt(1+f*f)
    # mirror planes are perpendicular to the 15 two-fold axes (edge midpoints)
    mids=[(W[i]+W[j])/2 for i,j in E]; axes2=[]
    for m in mids:
        u=m/np.linalg.norm(m)
        if not any(abs(abs(u@a)-1)<1e-6 for a in axes2): axes2.append(u)
    t=np.linspace(0,2*np.pi,361)
    for u in axes2:
        a=np.cross(u,[0.3,0.5,0.8]); a/=np.linalg.norm(a); b=np.cross(u,a)
        C=Rc*(np.outer(np.cos(t),a)+np.outer(np.sin(t),b))
        s.line(C[:,:2],w=0.25,op=0.10)
    s.line(np.stack([Rc*np.cos(t),Rc*np.sin(t)],1),w=0.45,op=0.35)
    for (i,j),vis in front.items():
        if vis: s.line(W[[i,j],:2],w=0.95,op=1.0,glow=1.0)
        else: s.line(W[[i,j],:2],w=0.40,op=0.28)
    # one axis of each kind, in ivory: 5-fold (vertices), 3-fold (faces), 2-fold (edges)
    v5=W[0]/np.linalg.norm(W[0]); fc=W[list(F[3])].mean(0); v3_=fc/np.linalg.norm(fc); v2_=axes2[4]
    for u,L in ((v5,1.32),(v3_,1.32),(v2_,1.32)):
        s.line(np.array([-u[:2]*Rc*L,u[:2]*Rc*L]),w=0.45,op=0.75,col=IV)
    for i in range(12):
        z=W[i,2]; s.dot(W[i,0],W[i,1],0.055 if z>0 else 0.035,col=IV if z>0 else 'ocCoral',op=1 if z>0 else .4,halo=.6 if z>0 else 0)
    return s,'bbox'

# 4 Chance -- Galton board, binomial(12,1/2) bins and the normal limit
def v4():
    s=Scene(); n=12; dy=0.82; rng=np.random.default_rng(7)
    top=n*dy+0.6
    for i in range(n):
        for j in range(i+1): s.dot(j-i/2,top-i*dy,0.085,op=.9,halo=.5)
    floor=-0.2; H=7.5
    for k in range(n+1):
        p=math.comb(n,k)/2**n; x=k-n/2; h=H*p/ (math.comb(n,n//2)/2**n)
        Q=[(x-0.42,floor),(x-0.42,floor+h),(x+0.42,floor+h),(x+0.42,floor)]
        s.fill(Q,op=0.10); s.line(Q,w=0.7,op=.95,glow=.8)
    sig=math.sqrt(n)/2; xs=np.linspace(-n/2-0.6,n/2+0.6,400)
    peak=math.comb(n,n//2)/2**n
    s.line(np.stack([xs,floor+H*np.exp(-xs**2/(2*sig*sig))/(math.sqrt(2*math.pi)*sig)/peak],1),w=0.8,op=.9,col=IV)
    s.line([(-n/2-0.7,floor),(n/2+0.7,floor)],w=0.5,op=.6)
    for b in range(0):
        x=0.0; path=[(0,top+0.7)]
        for i in range(n):
            x+= 0.5 if rng.random()<0.5 else -0.5; path.append((x,top-i*dy-dy/2))
        path.append((x,floor+H*math.comb(n,int(x+n/2))/2**n/peak+0.15))
        s.line(path,w=0.45,op=.55,col=IV)
    return s,'bbox'

# 5 Calculation -- Euler spiral (Fresnel integrals) with osculating circles
def v5():
    s=Scene(); dt=1e-4; T=4.2
    t=np.arange(0,T+dt,dt); c=np.cos(np.pi*t*t/2); si=np.sin(np.pi*t*t/2)
    x=np.concatenate([[0],np.cumsum((c[1:]+c[:-1])/2*dt)]); y=np.concatenate([[0],np.cumsum((si[1:]+si[:-1])/2*dt)])
    X=np.concatenate([-x[::-1],x[1:]]); Y=np.concatenate([-y[::-1],y[1:]]); tt=np.concatenate([-t[::-1],t[1:]])
    s.line(np.stack([X,Y],1)[::5],w=1.0,op=1,glow=1.0)
    for t0 in (0.5,0.8,1.15,1.6,2.2,-0.5,-0.8,-1.15,-1.6,-2.2):
        i=int(round(abs(t0)/dt)); px,py=(x[i],y[i]) if t0>0 else (-x[i],-y[i])
        k=np.pi*t0; th=np.pi*t0*t0/2; nx,ny=-math.sin(th),math.cos(th)
        R=1/k; cx,cy=px+nx*R,py+ny*R
        a=np.linspace(0,2*np.pi,240); s.line(np.stack([cx+abs(R)*np.cos(a),cy+abs(R)*np.sin(a)],1),w=0.3,op=0.30)
        s.dot(px,py,0.012,col=IV,op=.9)
    s.dot(0.5,0.5,0.018,col=IV,halo=1); s.dot(-0.5,-0.5,0.018,col=IV,halo=1)
    return s,'mass'

# 6 Crossroads -- Ford circles and the Farey tessellation
def v6():
    s=Scene(); from math import gcd
    fr=sorted({(p/q,p,q) for q in range(1,25) for p in range(q+1) if gcd(p,q)==1})
    for i,(a,p,q) in enumerate(fr):
        for (b,r,t) in fr[i+1:]:
            if abs(p*t-q*r)==1: s.arc((a+b)/2,0,(b-a)/2,0,180,w=0.22,op=0.24,col=IV)
    s.arc(0,0.5,0.5,-90,0,w=0.95,op=1,glow=1); s.arc(1,0.5,0.5,180,270,w=0.95,op=1,glow=1)
    for q in range(2,81):
        for p in range(1,q):
            if gcd(p,q)!=1: continue
            r=1/(2*q*q); lw=max(0.16,0.95-0.19*math.log2(q)); op=max(0.35,1-0.11*math.log2(q))
            s.circle(p/q,r,r,w=lw,op=op,glow=1 if q<=12 else 0)
    s.line([(-0.02,0),(1.02,0)],w=0.5,op=.7,col=IV)
    return s,'bbox'

# 7 Spaces -- the Cantor function as the limit of its iterates, over the Cantor set
def v7():
    s=Scene()
    def it(P):
        A=[(x/3,y/2) for x,y in P]; B=[(2/3+x/3,0.5+y/2) for x,y in P]; return A+B
    P=[(0.0,0.0),(1.0,1.0)]; iters=[P]
    for _ in range(11): P=it(P); iters.append(P)
    for n,Q in enumerate(iters[:6]):
        s.line(Q,w=0.35,op=0.10+0.06*n,col=IV if n==0 else 'ocCoral')
    s.line(iters[-1],w=0.95,op=1,glow=1)
    ivs=[(0.0,1.0)]
    for lev in range(8):
        y=-0.10-0.075*lev
        for a,b in ivs: s.line([(a,y),(b,y)],w=max(0.5,2.6-0.3*lev),op=max(0.35,1-0.09*lev),glow=.6 if lev<3 else 0,cap='butt')
        ivs=[(a,a+(b-a)/3) for a,b in ivs]+[(b-(b-a)/3,b) for a,b in ivs]
    s.line([(0,0),(1,0),(1,1),(0,1),(0,0)],w=0.3,op=.25)
    return s,'bbox'

# 8 Analysis -- Fourier partial sums of the square wave, and its spectrum
def v8():
    s=Scene(); x=np.linspace(-math.pi,math.pi,1600)
    def S(N): return sum(4/math.pi*np.sin(k*x)/k for k in range(1,N+1,2))
    for j,N in enumerate((1,3,5,7,9,13,19,27)):
        s.line(np.stack([x,S(N)],1),w=0.35,op=0.12+0.07*j)
    s.line(np.stack([x,S(81)],1),w=0.9,op=1,glow=1)
    s.line([(-math.pi,0),(-math.pi,-1),(0,-1),(0,1),(math.pi,1),(math.pi,0)],w=0.45,op=.75,col=IV)
    base=-3.1; sc=1.25
    s.line([(-math.pi,base),(math.pi,base)],w=0.4,op=.5)
    for k in range(1,40,2):
        for sg in (1,-1):
            xx=sg*k*math.pi/40; h=sc*4/(math.pi*k)
            s.line([(xx,base),(xx,base+h)],w=0.8,op=.95,glow=.6)
            s.dot(xx,base+h,0.035,col=IV,halo=.6)
    return s,'bbox'

# 9 Shapes -- the hyperbolic {7,3} tiling of the Poincare disk
def v9():
    s=Scene(); p,q=7,3
    r0=math.sqrt(math.cos(math.pi/p+math.pi/q)/math.cos(math.pi/p-math.pi/q))
    def circ3(a,b,c):
        ax,ay,bx,by,cx,cy=a.real,a.imag,b.real,b.imag,c.real,c.imag
        d=2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
        if abs(d)<1e-12: return None
        ux=((ax*ax+ay*ay)*(by-cy)+(bx*bx+by*by)*(cy-ay)+(cx*cx+cy*cy)*(ay-by))/d
        uy=((ax*ax+ay*ay)*(cx-bx)+(bx*bx+by*by)*(ax-cx)+(cx*cx+cy*cy)*(bx-ax))/d
        return complex(ux,uy)
    def geo(a,b):
        if abs(a)<1e-9: return None
        c=circ3(a,b,a/abs(a)**2)
        return None if c is None or abs(c)>1e6 else (c,abs(c-a))
    def reflect(z,g,a,b):
        if g is None:
            u=(b-a)/abs(b-a); return a+u*u*(z-a).conjugate()
        c,R=g; return c+R*R/(z-c).conjugate()
    P0=[r0*cmath.exp(2j*math.pi*k/p) for k in range(p)]
    seen={0j:True}; queue=[P0]; edges={}
    while queue:
        P=queue.pop(0)
        for i in range(p):
            a,b=P[i],P[(i+1)%p]; key=tuple(sorted([(round(a.real,7),round(a.imag,7)),(round(b.real,7),round(b.imag,7))]))
            if key in edges: continue
            L=abs(a-b)
            edges[key]=(a,b,L)
            if L<0.010 or len(edges)>9000: continue
            g=geo(a,b); Q=[reflect(z,g,a,b) for z in P]; c=sum(Q)/p; ck=complex(round(c.real,6),round(c.imag,6))
            if ck not in seen: seen[ck]=True; queue.append(Q)
    for a,b,L in edges.values():
        g=geo(a,b)
        if g is None: pts=[a,b]
        else:
            c,R=g; t0=cmath.phase(a-c); t1=cmath.phase(b-c); d=(t1-t0+math.pi)%(2*math.pi)-math.pi
            n=max(3,int(abs(d)*R/0.004)); pts=[c+R*cmath.exp(1j*(t0+d*k/n)) for k in range(n+1)]
        w=0.22+0.75*min(1,L/0.35); op=0.30+0.70*min(1,L/0.25)
        s.line([(z.real,z.imag) for z in pts],w=w,op=op,glow=1 if L>0.12 else 0)
    s.fill([(r0*math.cos(2*math.pi*k/p),r0*math.sin(2*math.pi*k/p)) for k in range(p)],op=0.08)
    t=np.linspace(0,2*np.pi,721); s.line(np.stack([np.cos(t),np.sin(t)],1),w=0.5,op=.6,col=IV)
    return s,'bbox'

# 10 Abstraction -- the snake lemma: two exact rows, kernels, cokernels and the connecting map
def v10():
    s=Scene(); xs=[0,1.7,3.4]; Y={'ker':3.0,'top':2.0,'bot':1.0,'cok':0.0}
    for gx in np.arange(-2.6,6.01,0.425):
        for gy in np.arange(-0.85,3.86,0.425):
            d=math.hypot(gx-1.7,gy-1.5); s.dot(gx,gy,0.012,op=max(0.05,0.32-0.06*d),scaled=True)
    def arrow(a,b,w=0.7,op=1,col='ocCoral',glow=.7,gap=0.16):
        a=np.array(a,float); b=np.array(b,float); u=(b-a)/np.linalg.norm(b-a); a2=a+u*gap; b2=b-u*gap
        s.line([a2,b2],w=w,op=op,col=col,glow=glow)
        n=np.array([-u[1],u[0]]); h=0.10
        s.line([b2-u*h+n*h*0.55,b2,b2-u*h-n*h*0.55],w=w,op=op,col=col)
    nodes=[(x,Y[r]) for x in xs for r in Y]+[(-1.7,1.0),(5.1,2.0)]
    for r in ('ker','top','bot','cok'):
        arrow((xs[0],Y[r]),(xs[1],Y[r])); arrow((xs[1],Y[r]),(xs[2],Y[r]))
    arrow((-1.7,1.0),(xs[0],1.0),op=.6); arrow((xs[2],2.0),(5.1,2.0),op=.6)
    for x in xs:
        arrow((x,3.0),(x,2.0)); arrow((x,2.0),(x,1.0),w=0.9,glow=1); arrow((x,1.0),(x,0.0))
    for x,y in nodes: s.dot(x,y,0.07,col='ocCoral',op=1,halo=.8)
    # the snake: ker c -> coker a, a smooth S through the gap between the rows
    def bez(P0,P1,P2,P3,n=200):
        t=np.linspace(0,1,n)[:,None]; return (1-t)**3*P0+3*(1-t)**2*t*P1+3*(1-t)*t*t*P2+t**3*P3
    A=bez(np.array([3.4,3.0]),np.array([5.6,3.0]),np.array([5.4,1.5]),np.array([1.7,1.5]))
    B=bez(np.array([1.7,1.5]),np.array([-2.0,1.5]),np.array([-2.2,0.0]),np.array([-0.17,0.0]))
    S=np.vstack([A,B[1:]]); s.line(S,w=0.85,op=.95,col=IV,glow=.8)
    u=np.array([1.0,0]); b2=S[-1]; n=np.array([0,1.0]); h=0.11
    s.line([b2-u*h+n*h*.55,b2,b2-u*h-n*h*.55],w=0.85,op=.95,col=IV)
    s.dot(xs[2],3.0,0.08,col=IV,halo=1); s.dot(xs[0],0.0,0.08,col=IV,halo=1)
    return s,'avg'

# 11 Randomness -- 200 simple random walks, the 2*sqrt(n) envelope and the Gaussian limit
def v11():
    s=Scene(); rng=np.random.default_rng(11); T=240; M=200; ux=4.0/T; uy=0.50/math.sqrt(T)
    steps=rng.choice([-1,1],size=(M,T)); W=np.concatenate([np.zeros((M,1)),np.cumsum(steps,1)],1)
    t=np.arange(T+1)
    for w in W: s.line(np.stack([t*ux,w*uy],1),w=0.25,op=0.10)
    for i in (17,103): s.line(np.stack([t*ux,W[i]*uy],1),w=0.45,op=.85,glow=.7)
    tt=np.linspace(0,T,400)
    for sg in (1,-1): s.line(np.stack([tt*ux,sg*2*np.sqrt(tt)*uy],1),w=0.55,op=.75,col=IV)
    y=np.linspace(-3.4*math.sqrt(T),3.4*math.sqrt(T),300); d=np.exp(-y*y/(2*T)); x0=T*ux+0.05
    s.line(np.stack([x0+0.55*d,y*uy],1),w=0.7,op=.9,col=IV,glow=.5)
    s.dot(0,0,0.016,col=IV,halo=1)
    return s,'bbox'

# 12 Random Motion -- one planar Brownian path from the centre to its first exit from the disc
def v12():
    s=Scene(); rng=np.random.default_rng(2026); sd=0.010
    seed=947; rng=np.random.default_rng(seed); st=rng.normal(0,sd,(40000,2))
    z=np.concatenate([[0],np.cumsum(st[:,0]+1j*st[:,1])]); z=z[:np.nonzero(abs(z)>=1)[0][0]+1]   # stopped at first exit
    # planar Brownian motion is rotation invariant: turn the path so its ink (covered cells) is balanced left/right
    # ink weight = the drawn opacity of the last chunk that crosses each cell
    op=0.35+0.55*np.minimum(11,np.arange(len(z))*12//len(z))/11
    key=np.round(np.stack([z.real,z.imag],1)/0.012).astype(int); last={}
    for i,(kx,ky) in enumerate(map(tuple,key)): last[(kx,ky)]=op[i]
    K=np.array(list(last.keys()),float)*0.012; Wt=np.array(list(last.values())); c=complex(*(K*Wt[:,None]).sum(0)/Wt.sum())
    if abs(c)>1e-9: z=z*np.exp(1j*(-np.pi/2-np.angle(c)))
    P=np.stack([z.real,z.imag],1)
    n=len(P); chunks=12
    for c in range(chunks):
        a=c*n//chunks; b=min(n,(c+1)*n//chunks+1)
        s.line(P[a:b],w=0.32,op=0.35+0.55*c/(chunks-1),glow=.25)
    t=np.linspace(0,2*np.pi,721); s.line(np.stack([np.cos(t),np.sin(t)],1),w=0.5,op=.6,col=IV)
    e=z[-1]/abs(z[-1]); s.dot(0,0,0.022,col=IV,halo=1); s.dot(e.real,e.imag,0.026,col=IV,halo=1)
    s.seed=seed; return s,'bbox'

# 13 Arithmetic -- y^2 = x^3 - x + 1, its level-set pencil, and P + Q by chord and reflection
def v13():
    s=Scene(); Ymax=2.25
    def curve(k):
        g=lambda x:x**3-x+k; xs=np.linspace(-2.0,2.2,20001); ok=g(xs)>=0; segs=[]; i=0
        while i<len(xs):
            if ok[i]:
                j=i
                while j+1<len(xs) and ok[j+1]: j+=1
                segs.append((xs[i],xs[j])); i=j+1
            else: i+=1
        out=[]
        for a,b in segs:
            u=np.linspace(0,math.pi,1500); x=a+(b-a)*(1-np.cos(u))/2; y=np.sqrt(np.maximum(g(x),0))
            m=y<=Ymax; x,y=x[m],y[m]
            out.append(np.vstack([np.stack([x[::-1],y[::-1]],1),np.stack([x,-y],1)]))
        return out
    for k in (-0.35,0.0,0.2,0.39,0.6,1.5,2.2):
        for C in curve(k): s.line(C,w=0.28,op=.18)
    for C in curve(1.0): s.line(C,w=1.0,op=1,glow=1)
    s.line([(-1.65,1),(1.55,1)],w=0.5,op=.75,col=IV)
    s.line([(1,1.12),(1,-1.12)],w=0.4,op=.5,col=IV)
    for (x,y) in ((-1,1),(0,1),(1,1)): s.dot(x,y,0.045,col=IV,halo=1)
    s.dot(1,-1,0.06,col='ocCoral',halo=1.4); s.dot(1,-1,0.03,col=IV)
    return s,'bbox'

# 14 The Primes -- the critical-line curve t -> zeta(1/2 + i t), through the origin at every zero
def v14():
    s=Scene(); curve=json.loads((HERE/'zeta-curve.json').read_text())
    Z=np.array(curve['re'])+1j*np.array(curve['im'])
    P=np.stack([Z.real,Z.imag],1); n=len(P); ch=14
    for c in range(ch):
        a=c*n//ch; b=min(n,(c+1)*n//ch+1)
        s.line(P[a:b],w=0.45+0.45*c/(ch-1),op=0.45+0.55*c/(ch-1),glow=0.3+0.7*c/(ch-1))
    s.dot(0,0,0.05,col=IV,halo=1.2)
    return s,'avg'

# 15 Order and Chance -- pair correlation of zeta zeros (Montgomery) against GUE and Poisson
def v15():
    s=Scene(); g=np.array(json.loads((HERE/'zeros.json').read_text()))
    u=g/(2*np.pi)*np.log(g/(2*np.pi*np.e))+7/8          # unfolded zeros (mean spacing 1)
    D=u[None,:]-u[:,None]; D=D[(np.abs(D)<3)&(D!=0)]
    bins=np.arange(-3,3.001,0.1); h,_=np.histogram(D,bins=bins); h=h/(len(u)*0.1)
    W=5.2/6; H=1.35
    st=[(bins[0]*W,0)]
    for i,v in enumerate(h):
        a_,b_=bins[i]*W,bins[i+1]*W; st+= [(a_,v*H),(b_,v*H)]
    st.append((bins[-1]*W,0)); s.fill(st,op=0.07); s.line(st,w=0.7,op=1,glow=.8)
    x=np.linspace(-3,3,801); xs=np.where(x==0,1e-9,x)
    gue=1-(np.sin(np.pi*xs)/(np.pi*xs))**2
    s.line(np.stack([x*W,gue*H],1),w=0.9,op=.95,col=IV,glow=.6)
    s.line([(-3*W,H),(3*W,H)],w=0.45,op=.40,col=IV)
    s.line([(-3*W-0.05,0),(3*W+0.05,0)],w=0.45,op=.6)
    # barcodes: 90 consecutive unfolded zeros (rigid) above 90 Poisson points (clumped)
    rng=np.random.default_rng(15); z=u[400:491]-u[400]; p=np.cumsum(rng.exponential(1,90)); p=p*z[-1]/p[-1]
    L=6*W
    for row,(pts,col,op) in enumerate(((z,'ocCoral',1.0),(p,IV,.6))):
        y0=2.05-row*0.40
        for t in pts: s.line([(-3*W+t*L/z[-1],y0),(-3*W+t*L/z[-1],y0+0.26)],w=0.55,op=op,col=col,glow=.4 if row==0 else 0)
    return s,'bbox'

ARTS={2:v2,3:v3,4:v4,5:v5,6:v6,7:v7,8:v8,9:v9,10:v10,11:v11,12:v12,13:v13,14:v14,15:v15}
