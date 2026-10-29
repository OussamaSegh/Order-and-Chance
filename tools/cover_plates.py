"""Generate every cover illustration with one locked Volume-0 master.

Original approval PNGs are retained as references; they never bypass the shared
font/layout. Every volume receives one content-specific world-space 3D model,
using the same camera, wire material and glow, including Volumes 0 and 1.
"""
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent

PLATES = {'volume1-first-principles': 'ch06-integrals-taylor.tex; ch08-counting-probability.tex',
 'volume2-integers': 'ch02-primes.tex',
 'volume3-symmetry': 'ch11-characters.tex; ch12-quaternions.tex',
 'volume4-chance': 'ch01-counting.tex; ch02-discrete.tex; ch07-walks.tex',
 'volume5-calculation': 'ch06-fourier.tex; ch08-transform.tex',
 'volume6-crossroads': 'ch06-zeros.tex',
 'volume7-spaces': 'ch11-metricmeasures.tex',
 'volume8-analysis': 'ch09-complex.tex: holomorphic logarithms and continuation',
 'volume9-shapes': 'ch09-hyperbolic.tex',
 'volume10-abstraction': 'ch09-symmetric.tex',
 'volume11-randomness': 'ch07-ldp.tex: Bernoulli relative-entropy rate function',
 'volume12-random-motion': 'ch10-semicircle.tex',
 'volume13-arithmetic': 'ch14-modular.tex; ch12-elliptic.tex',
 'volume14-primes': 'Prime distribution and progressions',
 'volume15-order-and-chance': 'ch04-multiplicative.tex'}

def main():
    import hashlib,json
    from cover_surfaces import model
    from cover_surface_renderer import render
    from series_cover import settings,tex_source,check_titles,subtitle_cap_top
    from series_metadata import main as sync_metadata
    sync_metadata()
    (ROOT/'tools/cover-template.tex').write_text(tex_source())
    check_titles()
    config=settings()
    directions=json.loads((ROOT/'tools/assets/cover-art-direction.json').read_text())
    manifest=[]
    subjects={
      '1':'Gaussian dome in the shared native wireframe material',
      '2':'Ulam prime lattice with lower, broader triangulated relief',
      '3':'Icosahedral symmetry as a triangulated 3D wireframe',
      '4':'Galton branching lattice feeding exact binomial probability columns',
      '5':'Smooth interference of five Fourier harmonics',
      '6':'Riemann zeta modulus landscape',
      '7':'Sierpinski carpet as a shallow solid with exposed hole walls',
      '8':'Helicoid of the multivalued complex logarithm',
      '9':'Pseudosphere and hyperbolic geometry',
      '10':'A 600-box Plancherel Young diagram as a solid Ferrers wall',
      '11':'Bernoulli large-deviation entropy bowl',
      '12':'Seven Hermitian Brownian eigenvalue ribbons',
      '13':'Elliptic-curve complex torus',
      '14':'Locally averaged normalised prime-counting error surface',
      '15':'Phase projections of a Steinhaus multiplicative walk',
    }
    for book,evidence in PLATES.items():
        number=book.split('-',1)[0].removeprefix('volume')
        geometry,info=render(model(number),config,directions[number])
        content='% Shared-master 3D wireframe: '+subjects[number]+'\n'+geometry
        info['renderer']='shared-camera-vector'
        (ROOT/book/'cover-motif.tex').write_text(content)
        manifest.append(dict(book=book,number=number,subject=subjects[number],evidence=evidence,
            sha256=hashlib.sha256(content.encode()).hexdigest(),**info))
        print('generated shared-master illustration',book,flush=True)
    assert len(manifest)==15
    (ROOT/'docs/cover-art-manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
    files=[config['identity'],config['reference_illustration'],config['title_font'],
           config['subtitle_font'],'tools/assets/print/paper-muted.png','tools/assets/series-template.json',
        'tools/cover-template.tex','tools/cover-editorial-front.tex','tools/cover-colors.tex',
        'tools/cover-back.tex','tools/cover-wrap.tex','tools/cover-front.tex','tools/cover.tex',
        'tools/series_cover.py','tools/cover_surface_renderer.py','tools/cover_surfaces.py','tools/cover_sculptures.py',
        'tools/assets/cover-art-direction.json',
        'tools/cover_plates.py',*[f'tools/assets/approved-volume-{n}.png' for n in range(3)]]
    hashes={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in files}
    (ROOT/'tools/assets/series/manifest.json').write_text(json.dumps({'schema':1,
        'master':'Volume 0','variable_fields':['title','subtitle','volume number','illustration'],
        'files':hashes,'subtitle_placement':'below-last-title-line',
        'subtitle_cap_top_source_px':{n:subtitle_cap_top(n) for n in check_titles()},
        'artwork':manifest},indent=2)+'\n')
if __name__=='__main__':main()
