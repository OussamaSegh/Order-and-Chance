"""Generate the approved black/gold series' content-specific vector artwork.

Run from any directory with the build's Python (numpy is needed for matrix plates).
Geometry primitives in cover_motifs are reused as mathematical algorithms, with
fresh parameters and new compositions. No generated raster mathematics is used.
"""
import math
from pathlib import Path
import cover_motifs as g
ROOT=Path(__file__).resolve().parent.parent

def point(x,y): return f'({x:.5f}in,{y:.5f}in)'
def line(points,style='accent,line width=.65pt'):
    return r'\draw['+style+'] '+'--'.join(point(*p) for p in points)+';'
def dot(x,y,r=.026,style='accent'):
    return r'\fill['+style+'] '+point(x,y)+f' circle ({r}in);'
def text(x,y,value,size=14):
    return r'\node[accent,font=\fontsize{'+str(size)+'}{'+str(size+2)+r'}\selectfont] at '+point(x,y)+' {'+value+'};'
def circle(r,style='accent,line width=.55pt'):
    return r'\draw['+style+f'] (0,0) circle ({r}in);'
def formula(value): return text(0,0,'$'+value+'$',24)

def fibonacci():
    # Exact Fibonacci square tiling, successive squares 1,1,2,3,5.
    squares=[(0,0,1),(1,0,1),(0,1,2),(-3,0,3),(-3,-5,5)]
    out=['% Fibonacci squares 1,1,2,3,5; exact quarter-circle spiral.']
    P=lambda x,y:((x+.5)*.21,(y+1)*.21)
    for x,y,s in squares:
        out.append(line([P(x,y),P(x+s,y),P(x+s,y+s),P(x,y+s),P(x,y)],'accent,opacity=.65,line width=.45pt'))
    # Quarter circles join (1,0),(2,1),(0,3),(-3,0),(2,-5).
    for cx,cy,r,a,b in [(1,1,1,-90,0),(0,1,2,0,90),(0,0,3,90,180),(2,0,5,180,270)]:
        out.append(line([P(cx+r*math.cos(math.radians(t)),cy+r*math.sin(math.radians(t))) for t in [a+(b-a)*i/80 for i in range(81)]],'accent,line width=.85pt'))
    return r'\begin{scope}[rotate=90]'+'\n'+'\n'.join(out)+'\n'+r'\end{scope}'

def gaussian_surface():
    """A graph z=exp(-(x²+y²)), with exact projected samples (V0 calculus/normal law)."""
    P=lambda x,y,z:(.73*(x-y),.30*(x+y)+1.8*z-.52)
    out=['% Graph z = exp(-x^2-y^2), a Gaussian bell, in a fixed parallel projection.']
    values=[-2.1+4.2*i/18 for i in range(19)]
    # Back grid is quiet; crest and front are brighter without fake geometry.
    for a in values:
        for swap in [False,True]:
            pts=[]
            for j in range(101):
                b=-2.1+4.2*j/100;x,y=(b,a) if swap else (a,b)
                pts.append(P(x,y,math.exp(-x*x-y*y)))
            out.append(line(pts,f'accent,line width={.4 if abs(a)>1 else .65}pt,opacity={.4 if abs(a)>1.5 else .9}'))
    out += [line([P(-2.3,0,0),P(2.3,0,0)],'accent,opacity=.45,line width=.5pt,->'),line([P(0,-2.3,0),P(0,2.3,0)],'accent,opacity=.45,line width=.5pt,->')]
    return '\n'.join(out)

def integer_circle():
    """Radius-5 lattice circle and exact 3-4-5 triangle: Chapter 7 sums of squares."""
    out=['% Integer points a^2+b^2=25, with exact triangle (0,0),(3,0),(3,4).']
    u=.38
    for k in range(-5,6):
        out += [line([(u*k,-5*u),(u*k,5*u)],'accent,opacity=.21,line width=.3pt'),line([(-5*u,u*k),(5*u,u*k)],'accent,opacity=.21,line width=.3pt')]
    out += [circle(5*u,'accent,line width=1pt'),line([(-5.5*u,0),(5.5*u,0)],'accent,opacity=.7,line width=.6pt,->'),line([(0,-5.5*u),(0,5.5*u)],'accent,opacity=.7,line width=.6pt,->')]
    for x in range(-5,6):
        for y in range(-5,6):
            if x*x+y*y==25:out.append(dot(x*u,y*u,.045))
    out.append(line([(0,0),(3*u,0),(3*u,4*u),(0,0)],'accent,line width=1.3pt'))
    out.append(line([(2.65*u,0),(2.65*u,.35*u),(3*u,.35*u)],'accent,line width=.6pt'))
    assert 3*3+4*4==25
    return '\n'.join(out)

def dyson():
    """Fresh Hermitian Brownian eigenvalue paths, computed with numpy.linalg.eigvalsh."""
    import numpy as np
    rng=np.random.default_rng(202611); n=10; steps=110;dt=1/steps
    H=np.zeros((n,n),dtype=complex);paths=[np.zeros(n)]
    for _ in range(steps):
        Z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
        dH=(Z+Z.conj().T)*math.sqrt(dt/(4*n))
        H+=dH;paths.append(np.linalg.eigvalsh(H))
    out=['% Eigenvalues of a Hermitian Brownian motion; ordered at each time step.']
    for j in range(n):out.append(line([(-2.4+4.8*k/steps,.78*float(v[j])) for k,v in enumerate(paths)],f'accent,line width={.6+.4*(1-abs(j-4.5)/4.5):.2f}pt,opacity=.9'))
    assert all(np.all(np.diff(v)>=0) for v in paths)
    return '\n'.join(out)

def gem_bands():
    """Five independent GEM(1) stick-breakings, shown as separated proportional bands."""
    import random
    rng=random.Random(202610);out=['% Exact GEM(1) stick-breaking samples, one proportional band per row.']
    for j in range(6):
        left=1.;start=-2.4;y=1.25-.5*j
        for _ in range(14):
            f=left*rng.random();left-=f;w=4.8*f
            if w>.015:
                out.append(r'\filldraw[fill=accent,fill opacity='+f'{.3+.6*min(1,f*4):.3f}'+r',draw=navy,line width=.8pt] '+point(start,y-.16)+' rectangle '+point(start+w,y+.16)+';')
            start+=w
        assert 0<=left<=1
    return '\n'.join(out)

def ellipse_mark():
    out=[]
    for r in (.3,.5,.7):out.append(line([(r*math.cos(t),.45*r*math.sin(t)) for t in [2*math.pi*i/80 for i in range(81)]],'accent,line width=.6pt,opacity=.8'))
    return '\n'.join(out)
def tree_mark():
    out=[]
    for level in range(3):
        for j in range(2**level):
            x=(j-(2**level-1)/2)/2**level;y=.45-.33*level
            if level:
                par=(j//2-(2**(level-1)-1)/2)/2**(level-1)
                out.append(line([(par,y+.33),(x,y)],'accent,opacity=.8,line width=.7pt'))
            out.append(dot(x,y,.035))
    return '\n'.join(out)
def polygon_mark(n=5):
    p=[(.65*math.cos(math.pi/2+2*math.pi*i/n),.65*math.sin(math.pi/2+2*math.pi*i/n)) for i in range(n)]
    return circle(.65,'accent,opacity=.35,line width=.4pt')+'\n'+line(p+[p[0]],'accent,line width=.85pt')
def cantor_mark():
    out=[]
    for level in range(3):
        seg=[(-.8,.8)]
        for _ in range(level):seg=[q for a,b in seg for q in [(a,a+(b-a)/3),(b-(b-a)/3,b)]]
        for a,b in seg:out.append(line([(a,.3-.3*level),(b,.3-.3*level)],'accent,line width=1.7pt'))
    return '\n'.join(out)
def elliptic_mark():
    out=[]
    for a,b in [(-1,0),(1,1.55)]:
        for sign in [-1,1]:
            out.append(line([(.55*x,.5*sign*math.sqrt(max(0,x**3-x))) for x in [a+(b-a)*j/100 for j in range(101)]],'accent,line width=.8pt'))
    return '\n'.join(out)
def young_mark():
    return '\n'.join(line([(.25*x-.5,.25*y-.25),(.25*(x+1)-.5,.25*y-.25),(.25*(x+1)-.5,.25*(y+1)-.25),(.25*x-.5,.25*(y+1)-.25),(.25*x-.5,.25*y-.25)],'accent,line width=.65pt') for y,n in enumerate([4,3,1]) for x in range(n))
def prime_mark():
    out=[line([(-.9,0),(.9,0)],'accent,opacity=.5,line width=.4pt')]
    for p in [2,3,5,7,11,13]:out += [dot(-.9+1.8*(p-2)/11,0,.035),line([(-.9+1.8*(p-2)/11,-.12),(-.9+1.8*(p-2)/11,.12)],'accent,line width=.5pt')]
    return '\n'.join(out)
def wave_mark():return line([(i/50-.8,.26*math.sin(2*math.pi*i/80)) for i in range(81)],'accent,line width=.8pt')
def lattice_mark():return '\n'.join(dot(x*.25,y*.25,.022) for x in range(-2,3) for y in range(-1,2))
def rotation_mark():return circle(.55)+'\n'+'\n'.join(dot(.55*math.cos(t),.55*math.sin(t),.032) for t in [2*math.pi*(j*(math.sqrt(5)-1)/2%1) for j in range(8)])
def normal_mark():return line([(.75*x,.5*math.exp(-x*x*2)-.2) for x in [-1.5+3*j/100 for j in range(101)]],'accent,line width=.8pt')

# Main plate, smaller supporting mark, mathematical subject and chapter evidence.
PLATES={
 'tome0-back-in-shape':(gaussian_surface,fibonacci,'Gaussian wireframe surface','ch06-integrals-taylor.tex; ch08-counting-probability.tex'),
 'tome1-integers':(integer_circle,fibonacci,'Lattice circle and 3–4–5 triangle','ch07-sums-of-squares.tex'),
 'tome2-structures':(g.buckyball,lambda:polygon_mark(5),'Truncated icosahedron, rotations and A5','ch11-characters.tex; ch12-quaternions.tex'),
 'tome3-chance':(lambda:g.galton_board(rows=10,balls=18),tree_mark,'Binomial board and Gaussian approximation','ch02-discrete.tex; ch06-clt.tex'),
 'tome4-calculation':(lambda:g.fourier_square((1,3,11,31)),wave_mark,'Fourier partial sums and Gibbs overshoot','ch06-fourier.tex'),
 'tome5-meets':(lambda:g.zeta_critical_line(t_max=35,steps=1600),lambda:formula(r'\zeta(s)=\prod_p(1-p^{-s})^{-1}'),'Critical-line zeta curve','ch06-zeros.tex'),
 'tome6-spaces':(lambda:g.sierpinski_carpet(level=3),cantor_mark,'Sierpinski carpet and Cantor construction','ch11-metricmeasures.tex'),
 'tome7-analysis':(lambda:g.confocal_grid(Y=1.3,n_ell=7,n_hyp=6),ellipse_mark,'Image of an orthogonal grid under sin(z)','ch09-complex.tex'),
 'tome8-shapes':(lambda:g.farey_tessellation(depth=6,nmax=25),lambda:polygon_mark(3),'Farey tessellation of the hyperbolic disk','ch09-hyperbolic.tex'),
 'tome9-structures2':(lambda:g.plancherel_young(n=900,seed=202609),young_mark,'Young diagram and Plancherel limit shape','ch09-symmetric.tex'),
 'tome10-chance2':(gem_bands,lambda:formula(r'V_k=U_k\prod_{j<k}(1-U_j)'),'GEM(1) proportional stick-breaking bands','ch12-permutations.tex'),
 'tome11-motion':(dyson,wave_mark,'Hermitian Brownian eigenvalue trajectories','ch10-semicircle.tex'),
 'tome12-arithmetic':(lambda:g.ford_circles(qmax=28),elliptic_mark,'Ford circles over reduced rationals','ch14-modular.tex; ch12-elliptic.tex'),
 'tome13-primes':(lambda:g.prime_constellations(rings=32,r0=.42),prime_mark,'Prime residues, twins and constellations','Prime distribution and progressions'),
 'tome14-random':(lambda:g.multiplicative_walks(N=1800,walks=3,seed=202614),lambda:formula(r'f(mn)=f(m)f(n)'),'Steinhaus multiplicative partial-sum walks','ch05-randommult.tex'),
 'tome15-workshop':(lambda:g.brw_barrier(depth=9,seed=202615),tree_mark,'Branching random walk and critical barrier','ch06-chaos.tex'),
 'tomeC1-discrete':(lambda:g.boolean_lattice(n=4),lambda:polygon_mark(4),'Boolean lattice and symmetric chains','Orders and combinatorics'),
 'tomeC2-algorithms':(lambda:g.bitonic_network(n=8),lambda:formula(r'O(n\log n)'),'Eight-wire bitonic sorting network','Sorting networks'),
 'tomeC3-complexity':(g.mod3_automaton,lambda:formula(r'\{0,1\}^{*}'),'Finite automaton for divisibility by three','ch01-automata.tex'),
 'tomeC4-information':(g.entropy_plate,lambda:formula(r'H(X)=-\sum_x p_x\log_2p_x'),'Binary entropy and symmetric-channel capacity','ch01-entropy.tex; ch03-channels.tex'),
 'tomeC5-learning':(g.conjugate_gradient_plate,ellipse_mark,'Quadratic contours and conjugate gradients','ch02-krylov.tex'),
 'tomeS1-linear':(lambda:g.lozenge_tiling(a=16,sweeps=3500,seed=202601),lambda:formula(r'A v=\lambda v'),'Lozenge tiling and determinant geometry','ch02-volume.tex'),
 'tomeS2-geometry':(lambda:g.apollonian_gasket(rmin=.018,label_r=.2),lambda:polygon_mark(3),'Apollonian circle packing and integer curvatures','Circle geometry and inversion'),
 'tomeS3-conjectures':(lambda:g.collatz_coral(N=1100,even_turn=.14,odd_turn=-.25),lambda:formula(r'n\mapsto\begin{cases}n/2&2\mid n\\3n+1&2\nmid n\end{cases}'),'Computed Collatz orbit tree','Collatz iteration'),
 'tomeS4-companion':(g.series_chords,lambda:polygon_mark(6),'Actual cross-volume mathematical citation map','data/series.json'),
 'tomeP1-crossroads':(lambda:g.gaussian_primes(N=18),lattice_mark,'Gaussian primes in a bounded integer lattice','Gaussian integers and number theory'),
 'tomeP2-machinery':(g.irrational_rotation,rotation_mark,'Golden-ratio rotation and equidistribution','ch01-almost.tex; ch02-hilbert.tex'),
 'tomeP3-frontiers':(g.binomial_limits,normal_mark,'Exact scaled binomial masses and Gaussian limit','ch01-pieces.tex'),
}

def main():
    import hashlib,json
    from series_metadata import main as sync_metadata
    sync_metadata()
    manifest=[]
    for book,(make,mark,subject,evidence) in PLATES.items():
        content='% Approved black/gold vector plate: '+subject+'\n'+make()
        # Fresh geometry/parameters + a common engraving vocabulary; no decoration
        # that claims additional mathematical content is appended to the plate.
        content=content.rstrip()+'\n'
        (ROOT/book/'cover-motif.tex').write_text(content)
        (ROOT/book/'cover-motif-mark.tex').write_text('% Supporting mark: '+subject+'\n'+mark().rstrip()+'\n')
        manifest.append(dict(book=book,subject=subject,evidence=evidence,sha256=hashlib.sha256(content.encode()).hexdigest()))
        print('generated',book,flush=True)
    assert len(set(m['sha256'] for m in manifest))==len(manifest)==28
    (ROOT/'docs/cover-art-manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
if __name__=='__main__':main()
