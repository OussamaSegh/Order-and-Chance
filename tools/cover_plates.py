"""Generate the approved charcoal/coral series' content-specific vector artwork.

Run from any directory with the build's Python (numpy is needed for matrix plates).
Geometry primitives in cover_motifs are reused as mathematical algorithms, with
fresh parameters and new compositions. Volumes 0 and 1 use immutable author-approved images; other mathematical plates remain vectors.
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
def circle(r,style='accent,line width=.55pt'):
    return r'\draw['+style+f'] (0,0) circle ({r}in);'

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

# One main plate per book, mathematical subject and chapter evidence.
PLATES={
 'tome0-mathematical-maturity':(None,'Gaussian wireframe surface','ch06-integrals-taylor.tex; ch08-counting-probability.tex'),
 'tome1-integers':(None,'Approved Ulam-inspired prime lattice artwork','ch02-primes.tex'),
 'tome2-structures':(g.buckyball,'Truncated icosahedron, rotations and A5','ch11-characters.tex; ch12-quaternions.tex'),
 'tome3-chance':(lambda:g.galton_board(rows=10,balls=18),'Binomial board and Gaussian approximation','ch02-discrete.tex; ch06-clt.tex'),
 'tome4-calculation':(lambda:g.fourier_square((1,3,11,31)),'Fourier partial sums and Gibbs overshoot','ch06-fourier.tex'),
 'tome5-meets':(lambda:g.zeta_critical_line(t_max=35,steps=1600),'Critical-line zeta curve','ch06-zeros.tex'),
 'tome6-spaces':(lambda:g.sierpinski_carpet(level=3),'Sierpinski carpet and Cantor construction','ch11-metricmeasures.tex'),
 'tome7-analysis':(lambda:g.confocal_grid(Y=1.3,n_ell=7,n_hyp=6),'Image of an orthogonal grid under sin(z)','ch09-complex.tex'),
 'tome8-shapes':(lambda:g.farey_tessellation(depth=6,nmax=25),'Farey tessellation of the hyperbolic disk','ch09-hyperbolic.tex'),
 'tome9-higher-structures':(lambda:g.plancherel_young(n=900,seed=202609),'Young diagram and Plancherel limit shape','ch09-symmetric.tex'),
 'tome10-chance2':(gem_bands,'GEM(1) proportional stick-breaking bands','ch12-permutations.tex'),
 'tome11-motion':(dyson,'Hermitian Brownian eigenvalue trajectories','ch10-semicircle.tex'),
 'tome12-arithmetic':(lambda:g.ford_circles(qmax=28),'Ford circles over reduced rationals','ch14-modular.tex; ch12-elliptic.tex'),
 'tome13-primes':(lambda:g.prime_constellations(rings=32,r0=.42),'Prime residues, twins and constellations','Prime distribution and progressions'),
 'tome14-random':(lambda:g.multiplicative_walks(N=1800,walks=3,seed=202614),'Steinhaus multiplicative partial-sum walks','ch05-randommult.tex'),
 'tome15-workshop':(lambda:g.brw_barrier(depth=9,seed=202615),'Branching random walk and critical barrier','ch06-chaos.tex'),
 'tomeP1-crossroads':(lambda:g.gaussian_primes(N=18),'Gaussian primes in a bounded integer lattice','Gaussian integers and number theory'),
 'tomeP2-machinery':(g.irrational_rotation,'Golden-ratio rotation and equidistribution','ch01-almost.tex; ch02-hilbert.tex'),
 'tomeP3-frontiers':(g.binomial_limits,'Exact scaled binomial masses and Gaussian limit','ch01-pieces.tex'),
}

def main():
    import hashlib,json
    from series_metadata import main as sync_metadata
    sync_metadata()
    manifest=[]
    for book,(make,subject,evidence) in PLATES.items():
        if make is None:
            number=book.split('-',1)[0].removeprefix('tome')
            asset=f'tools/assets/approved-volume-{number}.png'
            content=(ROOT/asset).read_bytes()
            manifest.append(dict(book=book,subject=subject,evidence=evidence,
                renderer='approved-image',source=asset,sha256=hashlib.sha256(content).hexdigest()))
            print('preserved exact approved master',book,flush=True)
            continue
        content='% Approved charcoal/coral vector plate: '+subject+'\n'+make()
        # Fresh geometry/parameters + a common engraving vocabulary; no decoration
        # that claims additional mathematical content is appended to the plate.
        content=content.rstrip()+'\n'
        (ROOT/book/'cover-motif.tex').write_text(content)
        manifest.append(dict(book=book,subject=subject,evidence=evidence,sha256=hashlib.sha256(content.encode()).hexdigest()))
        print('generated',book,flush=True)
    assert len(set(m['sha256'] for m in manifest))==len(manifest)==19
    (ROOT/'docs/cover-art-manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
if __name__=='__main__':main()
