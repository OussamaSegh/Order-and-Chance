"""Prepend a front cover while preserving the print interior and PDF navigation."""
import argparse
from pathlib import Path

from pypdf import PdfReader, PdfWriter

from print_layout import LAYOUT


def _labels(node):
    """Read every leaf of a PDF page-label number tree."""
    node = node.get_object()
    values = node.get('/Nums', [])
    for index in range(0, len(values), 2):
        yield int(values[index]), values[index + 1].get_object()
    for child in node.get('/Kids', []):
        yield from _labels(child)


def make_download(front, interior, output):
    front, interior, output = map(Path, (front, interior, output))
    if output.resolve() in {front.resolve(), interior.resolve()}:
        raise ValueError('Download output must be separate from cover and print interior')
    cover, body = PdfReader(front), PdfReader(interior)
    if len(cover.pages) != 1:
        raise ValueError('Expected exactly one front cover page')
    # Clone the complete interior catalog so annotations, named destinations,
    # outlines and document metadata keep their original object relationships.
    writer = PdfWriter(clone_from=body)
    page = cover.pages[0]
    width, height = LAYOUT['trim_width_in'] * 72, LAYOUT['trim_height_in'] * 72
    if abs(float(page.mediabox.width) / float(page.mediabox.height) - width / height) > .001:
        raise ValueError('Cover aspect ratio differs from the standard 7x10 page')
    page.scale_by(width / float(page.mediabox.width))
    writer.insert_page(page, index=0)
    writer.set_page_label(0, 0, prefix='Cover')
    tree = body.trailer['/Root'].get('/PageLabels')
    labels = sorted(_labels(tree)) if tree else [(0, {'/S': '/D', '/St': 1})]
    for index, (start, settings) in enumerate(labels):
        end = labels[index + 1][0] if index + 1 < len(labels) else len(body.pages)
        writer.set_page_label(start + 1, end, style=settings.get('/S'),
                              prefix=settings.get('/P'), start=settings.get('/St', 1))
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('wb') as stream:
        writer.write(stream)
    check_pair(output, interior)


def _contents(page):
    stream = page.get_contents()
    return stream.get_data() if stream is not None else b''


def _annotation_count(page):
    annotations = page.get('/Annots')
    return len(annotations.get_object()) if annotations is not None else 0


def check_pair(download, interior):
    """Reject missing covers, changed body pages, broken labels or destinations."""
    download, interior = PdfReader(download), PdfReader(interior)
    count = len(interior.pages)
    if len(download.pages) != count + 1:
        raise ValueError('Download must contain one front cover plus the print interior')
    width, height = LAYOUT['trim_width_in'] * 72, LAYOUT['trim_height_in'] * 72
    for document in (download, interior):
        for number, page in enumerate(document.pages, 1):
            if (abs(float(page.mediabox.width) - width) > .12 or
                    abs(float(page.mediabox.height) - height) > .12):
                raise ValueError(f'PDF page {number} is not the standard 7x10 size')
    for number, (printed, reading) in enumerate(zip(interior.pages, download.pages[1:]), 1):
        if (_contents(printed) != _contents(reading) or printed.cropbox != reading.cropbox or
                printed.rotation != reading.rotation or
                _annotation_count(printed) != _annotation_count(reading)):
            raise ValueError(f'Download body differs from print interior on page {number}')
    if download.page_labels[1:] != interior.page_labels:
        raise ValueError('Download changed the interior page labels')
    destinations = download.named_destinations
    for name, target in interior.named_destinations.items():
        if (name not in destinations or download.get_destination_page_number(destinations[name]) !=
                interior.get_destination_page_number(target) + 1):
            raise ValueError(f'Download changed the reference destination: {name}')
    return count


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('front', type=Path)
    parser.add_argument('interior', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    make_download(args.front, args.interior, args.output)
    print('Download PDF checked: front cover, unchanged print body, labels and destinations')
