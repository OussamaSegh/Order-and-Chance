"""Individually selected mathematical subjects; all styling lives in the renderer."""
import math
import random
from cover_surfaces import Scene, height_mesh, parametric_mesh, linspace


def combine(*scenes):
    result=Scene()
    for scene in scenes:
        result.faces.update(len(result)+i for i in getattr(scene,'faces',()))
        result.extend(scene)
    return result


def fourier_interference():
    return height_mesh(lambda x,y:sum(math.sin(k*math.pi*x)*math.cos(k*math.pi*y)/(k*k)
                                    for k in range(1,6)),n=35)


def logarithm_helicoid():
    def point(a,b):
        theta=-.75*math.pi+3*math.pi*a;r=.12+.72*b
        return r*math.cos(theta),r*math.sin(theta),-.45+1.1*a
    return parametric_mesh(point,n=(61,21))


def entropy_bowl():
    def rate(x):
        p=(1+x)/2
        return p*math.log(2*p)+(1-p)*math.log(2*(1-p))
    def point(a,b):
        theta=2*math.pi*a;r=.925*b
        x,y=r*math.cos(theta),r*math.sin(theta)
        return x,y,1.35*(rate(x)+rate(y))-.25
    return parametric_mesh(point,n=(65,27))


def dyson_ribbons():
    import numpy as np
    rng=np.random.default_rng(202611);n=7;steps=64
    matrix=np.diag(np.linspace(-.9,.9,n)).astype(complex);values=[]
    for _ in range(steps+1):
        values.append(np.linalg.eigvalsh(matrix))
        z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
        matrix+=(z+z.conj().T)/math.sqrt(4*n*steps)
    lo=min(float(v[0]) for v in values);hi=max(float(v[-1]) for v in values)
    scenes=[]
    for lane in range(n):
        def point(a,b,lane=lane):
            t=a*steps;i=min(steps-1,int(t));f=t-i
            # Positive cubic B-spline weights smooth the display while preserving
            # eigenvalue ordering. The sampled matrix process itself is unchanged.
            weights=((1-f)**3/6,(3*f**3-6*f*f+4)/6,(-3*f**3+3*f*f+3*f+1)/6,f**3/6)
            z=float(sum(w*values[min(steps,max(0,i+offset))][lane]
                        for w,offset in zip(weights,(-1,0,1,2))))
            # Time stands upright; the spectral coordinates fan into separate ribbons.
            return 1.8*(z-lo)/(hi-lo)-.9,.24-.48*lane/(n-1)+.16*(b-.5),1.25*a-.48
        scenes.append(parametric_mesh(point,n=(65,5)))
    return combine(*scenes)


def voxel_shell(cells, scales, offset):
    """Only exposed unit-box faces, preserving the exact combinatorial object."""
    cells=set(cells);curves=Scene()
    definitions=[((-1,0,0),[(0,0,0),(0,1,0),(0,1,1),(0,0,1)]),
      ((1,0,0),[(1,0,0),(1,0,1),(1,1,1),(1,1,0)]),
      ((0,-1,0),[(0,0,0),(0,0,1),(1,0,1),(1,0,0)]),
      ((0,1,0),[(0,1,0),(1,1,0),(1,1,1),(0,1,1)]),
      ((0,0,-1),[(0,0,0),(1,0,0),(1,1,0),(0,1,0)]),
      ((0,0,1),[(0,0,1),(0,1,1),(1,1,1),(1,0,1)])]
    for cell in sorted(cells):
        for neighbor,corners in definitions:
            if tuple(cell[d]+neighbor[d] for d in range(3)) in cells:continue
            points=[tuple(offset[d]+scales[d]*(cell[d]+p[d]) for d in range(3)) for p in corners]
            curves.faces.add(len(curves));curves.append(points+[points[0]])
    return curves


def plancherel_partition():
    rng=random.Random(202609);permutation=list(range(600));rng.shuffle(permutation);rows=[]
    for value in permutation:
        for row in rows:
            place=next((i for i,v in enumerate(row) if v>value),None)
            if place is None:row.append(value);break
            row[place],value=value,row[place]
        else:rows.append([value])
    return [len(row) for row in rows]


def young_ferrers_wall():
    partition=plancherel_partition();sx=1.65/partition[0];sz=1.15/len(partition)
    cells=[(j,0,i) for i,length in enumerate(partition) for j in range(length)]
    return voxel_shell(cells,(sx,.28,sz),(-.825,-.14,-.4))


def cyclotomic_crown():
    """Seven outer tips are seventh roots of unity; a hollow star prism has C7 symmetry."""
    vertices=[((.76 if k%2==0 else .31)*math.cos(math.pi*k/7),
               (.76 if k%2==0 else .31)*math.sin(math.pi*k/7)) for k in range(14)]
    def border(t):
        q=(t%1)*14;i=int(q);f=q-i;a,b=vertices[i],vertices[(i+1)%14]
        return (1-f)*a[0]+f*b[0],(1-f)*a[1]+f*b[1]
    def side(a,b):
        x,z=border(a);return x,-.16+.32*b,z+.15
    scenes=[parametric_mesh(side,n=(71,9))]
    for depth in (-.16,.16):
        def cap(a,b,depth=depth):
            x,z=border(a);r=math.hypot(x,z);f=.20/r+(1-.20/r)*b
            return x*f,depth,z*f+.15
        scenes.append(parametric_mesh(cap,n=(71,8)))
    scenes.append(parametric_mesh(lambda a,b:(.20*math.cos(2*math.pi*a),-.16+.32*b,.15+.20*math.sin(2*math.pi*a)),n=(57,7)))
    return combine(*scenes)


def sobolev_kernel():
    # Exact H^1 reproducing kernel in Machinery, Problem pb:sobolev, with L=2.
    def kernel(x,y):
        x+=1;y+=1
        return math.cosh(min(x,y))*math.cosh(2-max(x,y))/math.sinh(2)
    return height_mesh(kernel,n=41)


def bernoulli_convolutions():
    """Finite sign-sum laws, kernel-smoothed for display, not a claimed limiting density."""
    import numpy as np
    cache={};sigma=.045
    def law(lam):
        key=round(lam,10)
        if key in cache:return cache[key]
        sums=np.array([0.])
        for k in range(10):
            step=(1-lam)*lam**k;sums=np.concatenate((sums-step,sums+step))
        cache[key]=sums
        return sums
    def function(x,y):
        lam=.34+.34*(y+1)/2;sums=law(lam)
        return float(np.exp(-.5*((1.08*x-sums)/sigma)**2).mean()/(sigma*math.sqrt(2*math.pi)))
    return height_mesh(function,n=41)


def collatz_tree(depth=13):
    children={};levels={1:0};front=[1]
    for level in range(depth):
        following=[]
        for n in front:
            choices=[2*n]
            if n%6==4 and (n-1)//3>1:choices.append((n-1)//3)
            children[n]=choices
            for child in choices:
                assert (child//2 if child%2==0 else 3*child+1)==n
                levels[child]=level+1;following.append(child)
        front=following
    slots={};counter=0
    def place(n):
        nonlocal counter
        if n not in children:slots[n]=float(counter);counter+=1
        else:slots[n]=sum(place(c) for c in children[n])/len(children[n])
        return slots[n]
    place(1)
    points={n:(1.6*slot/max(1,counter-1)-.8,
               .14*math.sin(math.log2(n)), -.48+1.2*levels[n]/depth) for n,slot in slots.items()}
    return children,points,levels


def collatz_sculpture():
    children,points,levels=collatz_tree();scenes=[]
    for n,descendants in children.items():
        for child in descendants:
            a,b=points[n],points[child];radius=.009+.010*(1-levels[n]/13)
            def point(t,u,a=a,b=b,radius=radius):
                # A gently bowed branch, with endpoints at the exact genealogical layout.
                f=t*t*(3-2*t)
                c=tuple(a[d]+(b[d]-a[d])*(t if d==2 else f) for d in range(3))
                tangent=(b[0]-a[0],b[1]-a[1],b[2]-a[2]);length=math.sqrt(sum(v*v for v in tangent));v=[k/length for k in tangent]
                normal=(-v[2],0,v[0]);length=math.hypot(normal[0],normal[2]);normal=[k/length for k in normal]
                binormal=(v[1]*normal[2]-v[2]*normal[1],v[2]*normal[0]-v[0]*normal[2],v[0]*normal[1]-v[1]*normal[0])
                theta=2*math.pi*u
                return tuple(c[d]+radius*(math.cos(theta)*normal[d]+math.sin(theta)*binormal[d]) for d in range(3))
            scenes.append(parametric_mesh(point,n=(4,7)))
    return combine(*scenes)
