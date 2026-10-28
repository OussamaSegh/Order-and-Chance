"""Generate every cover illustration with one locked Volume-0 master.

Original approval PNGs are retained as references; they never bypass the shared
font/layout. Volume 0 keeps its traced Gaussian art; every other volume receives
one content-specific world-space 3D model, using the same camera and material.
"""
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent

PLATES = {'tome0-mathematical-maturity': 'ch06-integrals-taylor.tex; ch08-counting-probability.tex',
 'tome1-integers': 'ch02-primes.tex',
 'tome2-structures': 'ch11-characters.tex; ch12-quaternions.tex',
 'tome3-chance': 'ch02-discrete.tex; ch06-clt.tex',
 'tome4-calculation': 'ch06-fourier.tex',
 'tome5-meets': 'ch06-zeros.tex',
 'tome6-spaces': 'ch11-metricmeasures.tex',
 'tome7-analysis': 'ch09-complex.tex',
 'tome8-shapes': 'ch09-hyperbolic.tex',
 'tome9-higher-structures': 'ch09-symmetric.tex',
 'tome10-chance2': 'ch12-permutations.tex',
 'tome11-motion': 'ch10-semicircle.tex',
 'tome12-arithmetic': 'ch14-modular.tex; ch12-elliptic.tex',
 'tome13-primes': 'Prime distribution and progressions',
 'tome14-random': 'ch05-randommult.tex',
 'tome15-workshop': 'ch06-chaos.tex',
 'tomeP1-crossroads': 'Gaussian integers and number theory',
 'tomeP2-machinery': 'ch01-almost.tex; ch02-hilbert.tex',
 'tomeP3-frontiers': 'ch01-pieces.tex'}

def main():
    import hashlib,json
    from cover_surfaces import model
    from cover_surface_renderer import render
    from series_cover import settings,tex_source,check_titles
    from series_metadata import main as sync_metadata
    sync_metadata()
    (ROOT/'tools/cover-template.tex').write_text(tex_source())
    check_titles()
    config=settings()
    manifest=[]
    subjects={
      '0':'Approved Gaussian wireframe surface',
      '1':'Ulam prime lattice as raised wire pyramids',
      '2':'Icosahedral symmetry as a triangulated 3D wireframe',
      '3':'Joint binomial probability surface',
      '4':'Fourier partial-sum surface and Gibbs ridges',
      '5':'Riemann zeta modulus landscape',
      '6':'Extruded Sierpinski carpet',
      '7':'Real part of the complex sine as a surface',
      '8':'Pseudosphere and hyperbolic geometry',
      '9':'Plane-partition solid from a Young partition',
      '10':'GEM stick-breaking probability terraces',
      '11':'Hermitian Brownian eigenvalue surface',
      '12':'Elliptic-curve complex torus',
      '13':'Normalised prime-counting error surface',
      '14':'Phase projections of a Steinhaus multiplicative walk',
      '15':'Spatial branching random walk',
      'P1':'Gaussian prime lattice as raised wire pyramids',
      'P2':'Irrational winding on a torus',
      'P3':'Scaled binomial probability surfaces approaching the Gaussian'
    }
    for book,evidence in PLATES.items():
        number=book.split('-',1)[0].removeprefix('tome')
        if number=='0':
            content='% Volume 0 keeps its approved traced Gaussian illustration.\n'
            info={'space':'3D','renderer':'reference-vector','source':config['reference_illustration']}
        else:
            geometry,info=render(model(number),config)
            content='% Shared-master 3D wireframe: '+subjects[number]+'\n'+geometry
            info['renderer']='shared-camera-vector'
        (ROOT/book/'cover-motif.tex').write_text(content)
        manifest.append(dict(book=book,number=number,subject=subjects[number],evidence=evidence,
            sha256=hashlib.sha256(content.encode()).hexdigest(),**info))
        print('generated shared-master illustration',book,flush=True)
    assert len(manifest)==19
    (ROOT/'docs/cover-art-manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
    files=[config['identity'],config['reference_illustration'],config['title_font'],
           config['subtitle_font'],'tools/assets/print/paper-muted.png','tools/assets/series-template.json',
        'tools/cover-template.tex','tools/cover-editorial-front.tex','tools/cover-colors.tex',
        'tools/cover-back.tex','tools/cover-wrap.tex','tools/cover-front.tex','tools/cover.tex',
        'tools/series_cover.py','tools/cover_surface_renderer.py','tools/cover_surfaces.py',
        'tools/cover_plates.py',*[f'tools/assets/approved-volume-{n}.png' for n in range(3)]]
    hashes={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in files}
    (ROOT/'tools/assets/series/manifest.json').write_text(json.dumps({'schema':1,
        'master':'Volume 0','variable_fields':['title','subtitle','volume number','illustration'],
        'files':hashes,'subtitle_top_source_px':600,'artwork':manifest},indent=2)+'\n')
if __name__=='__main__':main()
