"""Content-specific 3D wireframes for one shared Volume-0 cover treatment.

All models return world-space curves. Camera, viewport and material are shared;
there are no per-book fonts, line styles, glow strengths or layout overrides.
"""
import cmath
import itertools
import math
import random


class Scene(list):
    def __init__(self, curves=(), faces=()):
        super().__init__(curves)
        self.faces=set(faces)


def linspace(a, b, n):
    return [a + (b-a)*i/(n-1) for i in range(n)]


def height_mesh(function, n=35, samples=71):
    cache = {}
    def point(x, y):
        key = (round(x, 9), round(y, 9))
        if key not in cache:
            cache[key] = function(x, y)
        return x, y, cache[key]
    grid=linspace(-1,1,n);curves=[]
    for x0,x1 in zip(grid,grid[1:]):
        for y0,y1 in zip(grid,grid[1:]):
            corners=[(x0,y0),(x1,y0),(x1,y1),(x0,y1),(x0,y0)]
            curve=[]
            for (xa,ya),(xb,yb) in zip(corners,corners[1:]):
                curve += [point(xa+(xb-xa)*t,ya+(yb-ya)*t) for t in (0,1/3,2/3)]
            curves.append(curve+[point(x0,y0)])
    lo = min(p[2] for c in curves for p in c)
    hi = max(p[2] for c in curves for p in c)
    return Scene([[(x,y,.93*(z-lo)/(hi-lo or 1)) for x,y,z in c] for c in curves],range(len(curves)))


def parametric_mesh(function, n=33, samples=71):
    na,nb=(n,n) if isinstance(n,int) else n
    aa,bb=linspace(0,1,na),linspace(0,1,nb);curves=[]
    for a0,a1 in zip(aa,aa[1:]):
        for b0,b1 in zip(bb,bb[1:]):
            corners=[(a0,b0),(a1,b0),(a1,b1),(a0,b1),(a0,b0)];curve=[]
            for (xa,ya),(xb,yb) in zip(corners,corners[1:]):
                curve += [function(xa+(xb-xa)*t,ya+(yb-ya)*t) for t in (0,1/3,2/3)]
            curves.append(curve+[function(a0,b0)])
    return Scene(curves,range(len(curves)))


def primality(n):
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n)+1))


def gaussian_dome():
    """Keep the Gaussian subject while using the series' native wire mesh."""
    mesh=height_mesh(lambda x,y:math.exp(-3.8*((x-.30)**2+(y+.20)**2)))
    return Scene([[(x,y,z*1.42) for x,y,z in curve] for curve in mesh],mesh.faces)


def prime_lattice(gaussian=False):
    curves = [[(x, y, .02) for x in (-1, 1)] for y in linspace(-1, 1, 35)]
    curves += [[(x, y, .02) for y in (-1, 1)] for x in linspace(-1, 1, 35)]
    curves=Scene(curves)
    spiral = {(0, 0): 1}
    x = y = 0
    value = 1
    for length in range(1, 18):
        for dx, dy in ((1, 0), (0, 1)) if length % 2 else ((-1, 0), (0, -1)):
            for _ in range(length):
                x += dx; y += dy; value += 1
                spiral[x, y] = value
    for i in range(-7, 8):
        for j in range(-7, 8):
            prime = (primality(i*i+j*j) if i and j else
                     primality(abs(i or j)) and abs(i or j) % 4 == 3) if gaussian else primality(spiral.get((i, j), 1))
            if not prime:
                continue
            x, y = i/8, j/8
            h = .16 + .22*math.exp(-2*(x*x+y*y))
            top = (x, y, h)
            base = [(x+dx, y+dy, .02) for dx, dy in ((-.055,-.055),(.055,-.055),(.055,.055),(-.055,.055))]
            for p,q in zip(base,base[1:]+base[:1]):
                def point(i,j):return tuple(p[d]+(q[d]-p[d])*i/3+(top[d]-p[d])*j/3 for d in range(3))
                for a in range(3):
                    for b in range(3-a):
                        triangle=[point(a,b),point(a+1,b),point(a,b+1)]
                        curves.faces.add(len(curves));curves.append(triangle+[triangle[0]])
                        if a+b<2:
                            triangle=[point(a+1,b),point(a+1,b+1),point(a,b+1)]
                            curves.faces.add(len(curves));curves.append(triangle+[triangle[0]])
    return curves


def symmetry_mesh():
    phi = (1+math.sqrt(5))/2
    vertices = [(0, a, b*phi) for a in (-1,1) for b in (-1,1)]
    vertices += [(a, b*phi, 0) for a in (-1,1) for b in (-1,1)]
    vertices += [(b*phi, 0, a) for a in (-1,1) for b in (-1,1)]
    faces = [t for t in itertools.combinations(vertices, 3)
             if all(abs(math.dist(a,b)-2)<1e-6 for a,b in itertools.combinations(t,2))]
    assert len(faces) == 20
    curves = Scene()
    scale = .70/math.sqrt(1+phi*phi)
    def transform(p):
        x,y,z = p
        return scale*x, scale*y, scale*z+.2
    for a,b,c in faces:
        def p(i,j):return transform(tuple(a[d]+(b[d]-a[d])*i/8+(c[d]-a[d])*j/8 for d in range(3)))
        for i in range(8):
            for j in range(8-i):
                curves.append([p(i,j),p(i+1,j),p(i,j+1),p(i,j)])
                if i+j<7:curves.append([p(i+1,j),p(i+1,j+1),p(i,j+1),p(i+1,j)])
    curves.faces=set(range(len(curves)))
    return curves


def binomial(n, x, p=.5):
    if x < 0 or x > n:
        return 0.
    # Smooth gamma continuation; identical to the exact PMF at integer x.
    return math.exp(math.lgamma(n+1)-math.lgamma(x+1)-math.lgamma(n-x+1)+x*math.log(p)+(n-x)*math.log1p(-p))


def galton_lattice(n=8):
    """A shallow 3D Pascal lattice feeding exact binomial probability columns."""
    curves=Scene()
    def point(row,k,back=0):
        u=.92*(2*k-row)/n
        return u/math.sqrt(2)+back,-u/math.sqrt(2)+back,1.35-1.15*row/n
    for row in range(n):
        for k in range(row+1):
            for child in (k,k+1):
                curves.append([point(row,k),point(row+1,child)])
                if k in (0,row) and child in (0,row+1):
                    curves.append([point(row,k,.14),point(row+1,child,.14)])
    for row in range(n+1):
        for k in (0,row):curves.append([point(row,k),point(row,k,.14)])
    peak=binomial(n,n//2)
    for k in range(n+1):
        u=.92*(2*k-n)/n;h=.52*binomial(n,k)/peak
        def p(du,d,z):return ((u+du)/math.sqrt(2)+d,-(u+du)/math.sqrt(2)+d,z)
        base=[p(-.065,0,-.55),p(.065,0,-.55),p(.065,.14,-.55),p(-.065,.14,-.55)]
        top=[(x,y,z+h) for x,y,z in base]
        for i in range(4):
            j=(i+1)%4
            curves.faces.add(len(curves));curves.append([base[i],base[j],top[j],top[i],base[i]])
        curves.faces.add(len(curves));curves.append(top+[top[0]])
        curves.append([point(n,k),p(0,0,-.55+h)])
    return curves


def projection_saddle():
    """An indefinite quadratic-form patch in orthogonal principal coordinates."""
    # Orthogonal principal axes of the indefinite quadratic form u^2-v^2.
    def point(a,b):
        u,v=2*a-1,2*b-1
        x,y=(u+v)/math.sqrt(2),(v-u)/math.sqrt(2)
        return .65*x,.65*y,.46*(u*u-v*v)+.18
    return parametric_mesh(point,n=35)


def zeta(s):
    n=40
    value=sum(k**-s for k in range(1,n+1))+n**(1-s)/(s-1)-n**-s/2
    rising=s
    for k,b in enumerate((1/6,-1/30,1/42,-1/30,5/66,-691/2730),1):
        value += b/math.factorial(2*k)*rising*n**(1-s-2*k)
        rising *= (s+2*k-1)*(s+2*k)
    return value


def block_surface(heights):
    n=len(heights); step=2/n; curves=Scene()
    def face(points):curves.faces.add(len(curves));curves.append(points+[points[0]])
    for i,row in enumerate(heights):
        for j,z in enumerate(row):
            if not z: continue
            x,y=-1+i*step,-1+j*step
            corners=[(x,y,z),(x+step,y,z),(x+step,y+step,z),(x,y+step,z)]
            face(corners)
            for edge,(di,dj) in enumerate(((0,-1),(1,0),(0,1),(-1,0))):
                other=heights[i+di][j+dj] if 0<=i+di<n and 0<=j+dj<n else 0
                if other<z:
                    a,b=corners[edge],corners[(edge+1)%4]
                    face([(a[0],a[1],other),(b[0],b[1],other),b,a])
    return curves


def carpet():
    def occupied(i,j):
        for _ in range(3):
            if i%3==j%3==1:return False
            i//=3; j//=3
        return True
    return block_surface([[.15 if occupied(i,j) else 0 for j in range(27)] for i in range(27)])


def young_solid():
    rng=random.Random(202609); permutation=list(range(600));rng.shuffle(permutation);rows=[]
    for value in permutation:
        for row in rows:
            place=next((i for i,v in enumerate(row) if v>value),None)
            if place is None:row.append(value);break
            row[place],value=value,row[place]
        else:rows.append([value])
    partition=[len(r) for r in rows];n=16
    h=[[.85*min(partition[min(i*len(partition)//n,len(partition)-1)],
                       partition[min(j*len(partition)//n,len(partition)-1)])/partition[0]
        for j in range(n)] for i in range(n)]
    return block_surface(h)


def gem_surface():
    rng=random.Random(202610);bands=[]
    for _ in range(7):
        left=1.;start=0.;row=[]
        for _ in range(18):
            piece=left*rng.random();left-=piece;row.append((start,start+piece,piece));start+=piece
        bands.append(row)
    def function(x,y):
        t=(y+1)*3;row=min(5,int(t));alpha=t-row
        value=lambda r:next((h for lo,hi,h in bands[r] if lo<=(x+1)/2<=hi),0)
        return (1-alpha)*value(row)+alpha*value(row+1)
    return height_mesh(function)


def dyson_surface():
    import numpy as np
    rng=np.random.default_rng(202611);n=10;steps=70;matrix=np.zeros((n,n),complex);values=[]
    for _ in range(steps+1):
        values.append(np.linalg.eigvalsh(matrix))
        z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));matrix+=(z+z.conj().T)/math.sqrt(4*n*steps)
    def function(x,y):
        t=(x+1)*steps/2;i=min(steps-1,int(t));f=t-i
        q=(y+1)*(n-1)/2;j=min(n-2,int(q));g=q-j
        return float((1-f)*((1-g)*values[i][j]+g*values[i][j+1])+f*((1-g)*values[i+1][j]+g*values[i+1][j+1]))
    return height_mesh(function)


def torus(winding=False):
    def point(a,b):
        a*=2*math.pi;b*=2*math.pi;r=.52+.16*math.cos(b)
        # Stand the torus in a vertical plane; the camera remains unchanged.
        return r*math.cos(a), .16*math.sin(b), .2+r*math.sin(a)
    curves=parametric_mesh(point,n=29)
    if winding:
        phi=(1+math.sqrt(5))/2
        curves.append([point(t,phi*t) for t in linspace(0,12,1601)])
    return curves


def prime_error_surface():
    import numpy as np
    limit=20000;sieve=[True]*(limit+1);sieve[0]=sieve[1]=False
    for k in range(2,math.isqrt(limit)+1):
        if sieve[k]:
            for q in range(k*k,limit+1,k):sieve[q]=False
    counts=[];total=0
    for prime in sieve:total+=prime;counts.append(total)
    def li(n):
        x=math.log(n);term=1.;value=.5772156649015329+math.log(x)
        for k in range(1,70):term*=x/k;value+=term/k
        return value
    raw=np.array([(counts[n]-li(n))/math.sqrt(n) for n in range(100,limit+1)])
    # A local average preserves the arithmetic error signal while removing the
    # distracting one-prime staircase at cover scale. No invented oscillations.
    window=np.arange(-450,451);kernel=np.exp(-.5*(window/150)**2);kernel/=kernel.sum()
    smooth=np.convolve(np.pad(raw,(450,450),mode='edge'),kernel,mode='valid')
    def function(x,y):
        t=(x+1)/2*(limit-100);i=min(len(smooth)-2,int(t));a=t-i
        return float(((1-a)*smooth[i]+a*smooth[i+1])*(1-.6*y*y))
    return height_mesh(function)


def steinhaus_surface():
    rng=random.Random(202614);n=1800;values=[0j,1+0j];phases={};sums=[0j]
    for k in range(2,n+1):
        divisor=next((d for d in range(2,math.isqrt(k)+1) if k%d==0),None)
        if divisor is None:phases[k]=cmath.exp(2j*math.pi*rng.random());values.append(phases[k])
        else:values.append(values[divisor]*values[k//divisor])
    total=0j
    for k in range(1,n+1):total+=values[k];sums.append(total/math.sqrt(k))
    def field(x,y):
        t=1+(x+1)/2*(n-1);i=min(n-1,int(t));a=t-i
        return (((1-a)*sums[i]+a*sums[i+1])*cmath.exp(1j*math.pi*y)).real
    return height_mesh(field)


def branching_tree():
    # Show genealogy in space-time, rather than flattening 1,022 spatial edges
    # into a tangled bundle. All siblings and the random increments remain.
    rng=random.Random(202615);level=[(0.,0.,1.2)];edges=[]
    for generation in range(1,8):
        following=[]
        for x,y,z in level:
            for direction in (-1,1):
                q=(x+direction*.16+rng.gauss(0,.055),y+rng.gauss(0,.12),1.2-1.3*generation/7)
                edges.append([(x,y,z),q]);following.append(q)
        level=following
    return edges


def model(number):
    number=str(number)
    from cover_sculptures import (fourier_interference, logarithm_helicoid, entropy_bowl,
        dyson_ribbons, young_ferrers_wall, cyclotomic_crown)
    if number=='1':return gaussian_dome()
    if number=='2':return prime_lattice()
    if number=='3':return symmetry_mesh()
    if number=='4':return galton_lattice()
    if number=='5':return fourier_interference()
    if number=='6':return height_mesh(lambda x,y:math.log1p(abs(zeta(complex(.2+(x+1)*.5,10+(y+1)*12.5)))))
    if number=='7':return carpet()
    if number=='8':return logarithm_helicoid()
    if number=='9':
        def pseudosphere(a,b):
            t=.12+2.1*b;r=.70/math.cosh(t);theta=2*math.pi*a
            return r*math.cos(theta),r*math.sin(theta),-.4+.85*(t-math.tanh(t))
        return parametric_mesh(pseudosphere)
    if number=='10':return young_ferrers_wall()
    if number=='11':return entropy_bowl()
    if number=='12':return dyson_ribbons()
    if number=='13':return torus()
    if number=='14':return prime_error_surface()
    if number=='15':return steinhaus_surface()
    raise ValueError(f'No 3D cover model for Volume {number}')
