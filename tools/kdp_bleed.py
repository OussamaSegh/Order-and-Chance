"""Add KDP's top, bottom and mirrored outside bleed without scaling the body.

The typeset/reading source stays at trim size. A solid full-page background can
be continued as a vector underlay; arbitrary pictures cannot be extrapolated.
"""
import argparse
from pathlib import Path

import numpy as np
import pymupdf
from pypdf import PdfReader, PdfWriter, Transformation
from pypdf.generic import DecodedStreamObject, RectangleObject

from print_layout import interior_size, interior_trim


def rectangle_path(drawing):
    """Accept PDF rectangle operators or TikZ's four straight rectangle edges."""
    items = drawing['items']
    if len(items) == 1 and items[0][0] == 're':
        return True
    if len(items) != 4 or any(item[0] != 'l' for item in items):
        return False
    rect = drawing['rect']
    corners = [(rect.x0, rect.y0), (rect.x0, rect.y1),
               (rect.x1, rect.y1), (rect.x1, rect.y0)]
    expected = {frozenset((corners[i], corners[(i + 1) % 4])) for i in range(4)}
    actual = {frozenset((tuple(item[1]), tuple(item[2]))) for item in items}
    return actual == expected


def solid_background(page, trim):
    """Recognise an opaque rectangular background painted before any content."""
    paint = page.get_bboxlog()
    if not paint or paint[0][0] != 'fill-path':
        return None
    for drawing in page.get_drawings():
        if drawing['seqno'] != 0:
            continue
        rect = drawing['rect']
        if (drawing['type'] != 'f' or drawing['fill'] is None
                or drawing['fill_opacity'] != 1
                or not rectangle_path(drawing)):
            return None
        if (rect.x0 <= trim.x0 + .12 and rect.y0 <= trim.y0 + .12
                and rect.x1 >= trim.x1 - .12 and rect.y1 >= trim.y1 - .12):
            return drawing['fill']
    return None


def set_bleed_boxes(page, index):
    width, height = interior_size(bleed=True)
    page.mediabox = RectangleObject((0, 0, width, height))
    page.cropbox = RectangleObject(page.mediabox)
    page.bleedbox = RectangleObject(page.mediabox)
    page.trimbox = RectangleObject(interior_trim(index))
    page.artbox = RectangleObject(page.trimbox)


def add_bleed(source, output):
    """Expand a clean trim-size PDF, preserving every trim-relative position."""
    writer = PdfWriter(clone_from=PdfReader(source))
    width, height = interior_size(bleed=True)
    trim_width, trim_height = interior_size()
    backgrounds = []
    with pymupdf.open(source) as rendered:
        for index, page in enumerate(writer.pages):
            if (tuple(page.mediabox) != (0, 0, trim_width, trim_height)
                    or page.cropbox != page.mediabox or page.rotation):
                raise ValueError(f'Bleed source page {index + 1} must be uncropped, unrotated trim size')
            colour = solid_background(rendered[index], rendered[index].rect)
            if colour is None:
                # A photo/diagram that reaches the cut needs authored image
                # bleed. Refuse to manufacture its missing pixels or leave a
                # white extension that would repeat the KDP rejection.
                edges = [(0, 0, trim_width, 1), (0, trim_height - 1, trim_width, trim_height),
                         (0, 0, 1, trim_height) if index % 2
                         else (trim_width - 1, 0, trim_width, trim_height)]
                for edge in edges:
                    pix = rendered[index].get_pixmap(clip=pymupdf.Rect(edge), dpi=72,
                                                     alpha=False, colorspace=pymupdf.csGRAY)
                    if np.any(np.frombuffer(pix.samples, dtype=np.uint8) < 245):
                        raise ValueError(f'Page {index + 1}: edge-reaching artwork needs authored bleed; '
                                         'only solid full-page backgrounds can be extended automatically')
            trim = interior_trim(index)
            page.add_transformation(Transformation().translate(trim[0], trim[1]))
            if colour is not None:
                # Underpaint only a proven solid full-page background. The body
                # and its embedded vector lettering remain the original content.
                stream = DecodedStreamObject()
                rgb = ' '.join(f'{value:.9f}' for value in colour)
                underlay = f'q {rgb} rg 0 0 {width:g} {height:g} re f Q\n'.encode('ascii')
                stream.set_data(underlay + page.get_contents().get_data())
                page.replace_contents(stream)
                backgrounds.append({'page': index + 1, 'rgb': list(colour)})
            set_bleed_boxes(page, index)
    writer.write(output)
    return backgrounds


def check_bleed_geometry(path):
    """Check every canvas and mirrored trim box, including GS roundoff."""
    width, height = interior_size(bleed=True)
    reader = PdfReader(path)
    for index, page in enumerate(reader.pages):
        expected = {'media': (0, 0, width, height), 'crop': (0, 0, width, height),
                    'bleed': (0, 0, width, height), 'trim': interior_trim(index)}
        for name, box in expected.items():
            actual = getattr(page, name + 'box')
            if any(abs(float(a) - b) > .02 for a, b in zip(actual, box)):
                raise ValueError(f'{path}: page {index + 1} has incorrect {name} box for KDP bleed')
        if page.rotation:
            raise ValueError(f'{path}: page {index + 1} is rotated')
    return len(reader.pages)


def check_bleed(path, backgrounds=None):
    """Check every canvas/trim box and the actual extended divider ink."""
    pages = check_bleed_geometry(path)
    width, height = interior_size(bleed=True)
    with pymupdf.open(path) as doc:
        if backgrounds is None:
            backgrounds = []
            for index, page in enumerate(doc):
                colour = solid_background(page, pymupdf.Rect(interior_trim(index)))
                if colour is not None:
                    backgrounds.append({'page': index + 1, 'rgb': list(colour)})
        for background in backgrounds:
            index = background['page'] - 1
            page = doc[index]
            trim = pymupdf.Rect(interior_trim(index))
            bands = [(0, 0, width, trim.y0), (0, trim.y1, width, height)]
            bands.append((0, 0, trim.x0, height) if index % 2
                         else (trim.x1, 0, width, height))
            for band in bands:
                pix = page.get_pixmap(clip=pymupdf.Rect(band), dpi=72, alpha=False,
                                      colorspace=pymupdf.csRGB)
                pixels = np.frombuffer(pix.samples, dtype=np.uint8).reshape(-1, 3).astype(float)
                if np.max(np.abs(pixels - np.array(background['rgb']) * 255)) > 3:
                    raise ValueError(f'{path}: page {index + 1} background does not fill the bleed')
    return pages


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf', type=Path)
    args = parser.parse_args()
    print(f'KDP bleed checked: {check_bleed(args.pdf)} pages, 7.125 x 10.25 in, mirrored trim and extended backgrounds')
