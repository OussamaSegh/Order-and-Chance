"""Trace approved cover artwork into print-only vector masters.

Regeneration needs Inkscape, libpotrace0 and requirements-cover-art.txt. CI uses
the reviewed, committed PDF assets; these extra art tools are not build deps.
Original PNGs remain immutable. Text is traced separately to preserve thin strokes.
The original antialiasing guides subpixel contour fitting; no new detail is claimed.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
import gzip
import hashlib
import json
from pathlib import Path
import subprocess

import numpy as np
from PIL import Image
from pypdf import PdfReader, PdfWriter

from potrace_paths import trace

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / 'tools/assets/print'
WORK = ROOT / 'build/print-cover-vectors'
BG = (21, 21, 22)
NUMBERS = ('0', '1', '2')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def svg_document(elements):
    # Half a source pixel of horizontal padding retains the original proportions
    # inside a true 7:10 page. The approved 1049x1500 raster is never stretched.
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="7in" height="10in" '
            'viewBox="-0.5 0 1050 1500">\n' + '\n'.join(elements) + '\n</svg>\n')


def lettering(a, region):
    h, w = a.shape[:2]
    # Sample the approved glyph antialiasing at subpixel contour precision.
    alpha = Image.fromarray(np.where(region, np.min(a, axis=2), 0).astype('uint8'))
    mask = np.array(alpha.resize((w * 3, h * 3), Image.Resampling.LANCZOS)) >= 132
    path = trace(mask, tolerance=.2)
    ink = np.median(a[region & (np.min(a, axis=2) > 230)], axis=0).astype(int)
    color = '#' + ''.join(f'{v:02x}' for v in ink)
    return (f'<path fill="{color}" fill-rule="evenodd" '
            f'transform="scale(0.3333333333333333)" d="{path}"/>')


def frame(a):
    elements = []
    # Fit the two intentionally straight borders, eliminating raster edge noise.
    for lo, hi in ((24, 33), (33, 41)):
        sample = a[80:1420, lo:hi].astype(float)
        alpha = np.clip((sample[:, :, 0] - BG[0]) / (255 - BG[0]), 0, 1)
        coverage = np.median(alpha, axis=0)
        center = lo + float(np.dot(coverage, np.arange(hi - lo)) / coverage.sum())
        width = float(coverage.sum())
        valid = alpha > .6
        color = np.median((sample[valid] - np.array(BG) * (1-alpha[valid, None])) /
                          alpha[valid, None], axis=0).clip(0, 255).astype(int)
        ink = '#' + ''.join(f'{v:02x}' for v in color)
        elements.append(f'<rect x="{center:.3f}" y="{center:.3f}" '
                        f'width="{1049-2*center:.3f}" height="{1500-2*center:.3f}" '
                        f'fill="none" stroke="{ink}" stroke-width="{width:.3f}"/>')
    return elements


def artwork(a, region):
    v = a.astype(int)
    active = region & (((v[:, :, 0] - v[:, :, 2] > 5) & (v[:, :, 0] > 28)) |
                       (np.min(v, axis=2) > 80))
    sample = Image.fromarray(a[active].reshape((-1, 1, 3)))
    quantized = sample.quantize(colors=64, method=Image.Quantize.MEDIANCUT, kmeans=3)
    palette = np.array(quantized.getpalette(), dtype='uint8').reshape(-1, 3)
    palette = palette[np.unique(np.array(quantized))]
    colors = sorted(set(map(tuple, palette.tolist())), key=lambda rgb: (sum(rgb), rgb))
    result = []
    for color in colors:
        # Nested source-color contours keep the glow without raster filters or
        # interlocking color-patch gaps. Tiny isolated tracing noise is discarded.
        mask = active & np.all(v >= np.array(color) - 2, axis=2)
        if not mask.any():
            continue
        path = trace(mask, tolerance=.35, speckle=3)
        ink = '#' + ''.join(f'{value:02x}' for value in color)
        result.append(f'<path fill="{ink}" fill-rule="evenodd" d="{path}"/>')
    return result


def export(name, elements):
    svg = svg_document(elements)
    source = WORK / f'{name}.svg'
    source.write_text(svg)
    raw = WORK / f'{name}-raw.pdf'
    subprocess.run(['inkscape', str(source), '--export-type=pdf',
                    f'--export-filename={raw}'], check=True, capture_output=True)
    reader = PdfReader(raw)
    if len(reader.pages) != 1 or reader.pages[0].images.keys():
        raise ValueError(f'{name}: print vector master contains raster images')
    writer = PdfWriter(clone_from=reader)
    writer.metadata = {'/Creator': 'Order and Chance print vector preparation',
                       '/Title': name}
    writer.generate_file_identifiers()
    target = ASSETS / f'{name}.pdf'
    with target.open('wb') as stream:
        writer.write(stream)
    editable = ASSETS / f'{name}.svgz'
    editable.write_bytes(gzip.compress(svg.encode(), compresslevel=9, mtime=0))
    return {p.name: sha(p) for p in (target, editable)}


def generate(number):
    source = ROOT / f'tools/assets/approved-volume-{number}.png'
    a = np.array(Image.open(source).convert('RGB'))
    if a.shape != (1500, 1049, 3):
        raise ValueError('Unexpected approved master dimensions')
    y, x = np.indices(a.shape[:2])
    header = (y >= 75) & (y < 205) & (x > 50) & (x < 1000)
    footer = (y > 1340) & (y < 1430) & (x > 55) & (x < 550)
    titles = (y >= 205) & (y < 670) & (x > 50) & (x < 1000)
    art = (y >= 680) & (y < 1462) & (x > 40) & (x < 1010) & ~footer
    borders = frame(a)
    common = [*borders, lettering(a, header | footer)]
    identity_files = export(f'identity-{number}', common)
    full = [*artwork(a, art), *common, lettering(a, titles)]
    full_files = export(f'volume-{number}', full)
    print(f'Generated vector masters for Volume {number}', flush=True)
    return number, {'source': str(source.relative_to(ROOT)), 'source_sha256': sha(source),
                    'files': {**identity_files, **full_files}, 'artwork_layers': len(full)-len(common)-1,
                    'raster_images': 0, 'trim_in': [7, 10]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--jobs', type=int, default=2)
    args = parser.parse_args()
    ASSETS.mkdir(parents=True, exist_ok=True)
    WORK.mkdir(parents=True, exist_ok=True)
    paper = Image.open(ROOT / 'tools/assets/approved-charcoal-paper.png').convert('RGB')
    Image.blend(Image.new('RGB', paper.size, BG), paper, .35).save(ASSETS / 'paper-muted.png')
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        masters = dict(pool.map(generate, NUMBERS))
    manifest = {'schema': 1, 'method': 'Source-derived Bezier contours; no bitmap enlargement',
                'digital_originals': 'unchanged', 'minimum_raster_ppi': 300,
                'paper_tile_width_logical_in': 2.5, 'masters': masters,
                'paper_muted_sha256': sha(ASSETS / 'paper-muted.png')}
    (ASSETS / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')


if __name__ == '__main__':
    main()
