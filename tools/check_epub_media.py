"""Reject an EPUB whose figures are fixed-width or whose math has no baseline.

EPUB figures fill the text column: a PNG at least 1600 px wide, with
``width: 100%``, ``max-width: 100%`` and ``height: auto`` on the image itself.
Inline mathematics uses an em width and an em ``vertical-align`` equal to the
formula's depth. ``tools/epub_fix.py`` writes both. Kindle ignores ``max-width``
and SVG viewBox sizing, so a stylesheet rule alone is not enough: the ``img``
style has to carry the size.

Run: python3 tools/check_epub_media.py path/to/book.epub
"""
from __future__ import annotations

import posixpath
import re
import struct
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote


MIN_PLATE_PX = 1600
PLATE_RULE = "figureimg,img.oc-plate{width:100%;max-width:100%;height:auto;}"
LENGTH = re.compile(r"\d+(?:\.\d+)?(?:px|pt)\b")
EM_WIDTH = re.compile(r"width:\d+(?:\.\d+)?em")
EM_SHIFT = re.compile(r"vertical-align:-?\d+(?:\.\d+)?em")
IMG_RE = re.compile(r"<img\b[^>]*/?>", re.I)
FIGURE_RE = re.compile(r"<figure\b[^>]*>.*?</figure>", re.S)


def compact(css: str) -> str:
    return re.sub(r"\s+", "", css)


def stylesheet_errors(css: str) -> list[str]:
    errors = []
    folded = compact(css)
    if PLATE_RULE not in folded:
        errors.append(
            "EPUB stylesheet is missing the full-width figure rule "
            "(figure img, img.oc-plate { width: 100%; max-width: 100%; height: auto; })")
    if "img.oc-math-inline" not in css:
        errors.append("EPUB stylesheet is missing img.oc-math-inline")
    return errors


def png_width(data: bytes) -> int:
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG")
    return struct.unpack(">I", data[16:20])[0]


def parse_attrs(tag: str) -> dict[str, str]:
    import html
    return {key: html.unescape(value) for key, value in re.findall(r'([\w:-]+)="([^"]*)"', tag)}


def resolve(page: str, src: str) -> str:
    path = unquote(src.split("#", 1)[0].split("?", 1)[0])
    return posixpath.normpath(posixpath.join(posixpath.dirname(page), path))


def _fixed_attr(attrs: dict[str, str]) -> str | None:
    for key in ("width", "height"):
        if key in attrs:
            return f'{key}="{attrs[key]}"'
    return None


def _plate_errors(where: str, attrs: dict[str, str], pngs: dict[str, bytes], page: str) -> list[str]:
    errors = []
    style = attrs.get("style", "").replace(" ", "")
    src = attrs.get("src", "")
    if src.lower().endswith(".svg"):
        errors.append(f"{where} is still an SVG ({src})")
    fixed = _fixed_attr(attrs)
    if fixed:
        errors.append(f"{where} has a fixed {fixed}")
    if LENGTH.search(style):
        errors.append(f"{where} style sets a px/pt size ({style})")
    if "width:100%" not in style or "max-width:100%" not in style or "height:auto" not in style:
        errors.append(f"{where} is missing width:100%, max-width:100%, height:auto")
    if src and not src.lower().endswith(".svg"):
        target = resolve(page, src)
        data = pngs.get(target)
        if data is None:
            errors.append(f"{where} PNG is missing ({target})")
        else:
            try:
                width = png_width(data)
            except ValueError:
                errors.append(f"{where} is not a PNG ({target})")
            else:
                if width < MIN_PLATE_PX:
                    errors.append(
                        f"{where} is {width}px wide; plates must be at least {MIN_PLATE_PX}px "
                        "so labels stay sharp across the text column")
    return errors


def png_size(data: bytes) -> tuple[int, int]:
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG")
    return struct.unpack(">II", data[16:24])


def _math_errors(where: str, attrs: dict[str, str], inline: bool, pngs: dict[str, bytes], page: str) -> list[str]:
    errors = []
    style = attrs.get("style", "").replace(" ", "")
    if "display:block" in style:
        errors.append(f"{where} is display:block, so the following punctuation starts a new line")
    for key in ("width", "height"):
        value = attrs.get(key, "")
        if not re.fullmatch(r"\d+", value) or int(value) < 1:
            errors.append(f"{where} needs an explicit HTML {key} in CSS pixels")
    if "max-height:" not in style:
        errors.append(f"{where} is missing max-height")
    if not re.search(r"height:\d+(?:\.\d+)?em", style) and "height:auto" not in style:
        errors.append(f"{where} needs an em height or height:auto")
    if inline:
        if not EM_WIDTH.search(style):
            errors.append(f"{where} width is not in em, so it will not follow the body font")
        if not EM_SHIFT.search(style):
            errors.append(f"{where} has no em vertical-align, so the baseline will not meet the text")
    else:
        if not EM_WIDTH.search(style):
            errors.append(f"{where} needs its natural em width to avoid stretching on wide screens")
        if "height:auto" not in style:
            errors.append(f"{where} needs height:auto to preserve aspect ratio when constrained")
    src = attrs.get("src", "")
    height_attr = attrs.get("height", "")
    if src and re.fullmatch(r"\d+", height_attr):
        target = resolve(page, src)
        data = pngs.get(target)
        if data:
            try:
                _, png_h = png_size(data)
            except ValueError:
                errors.append(f"{where} is not a PNG")
            else:
                if png_h > int(height_attr) * 3.5:
                    errors.append(
                        f"{where} bitmap is {png_h}px tall but displays at {height_attr}px; "
                        "Moon+ will draw the intrinsic size")
    return errors


OPF = "http://www.idpf.org/2007/opf"
DC = "http://purl.org/dc/elements/1.1/"
SVG = "http://www.w3.org/2000/svg"


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def kindle_structure_errors(pages: list[tuple[str, str]], opf: bytes | None) -> list[str]:
    """Reject EPUB packaging that Kindle's current guidelines say can fail conversion.

    An HTML cover page on top of a declared cover image, an SVG content image,
    and a second dc:title with no title-type main are the patterns named in
    the Kindle cover, image and enhanced-typesetting pages. EPUBCheck does
    not treat the first or the third as errors.
    """
    errors = []
    parsed: dict[str, ET.Element] = {}
    for name, text in pages:
        try:
            document = ET.fromstring(text)
        except ET.ParseError:
            continue
        parsed[name] = document
        if any(_local(node.tag) == "svg" or node.tag.startswith("{" + SVG + "}") for node in document.iter()):
            errors.append(
                f"{name} contains SVG. Kindle's reflowable image rules say SVG tags "
                "can cause errors; use an HTML img instead")
    if not opf:
        return errors
    try:
        package = ET.fromstring(opf)
    except ET.ParseError as error:
        return errors + [f"package document is malformed: {error}"]
    metadata = package.find(f"{{{OPF}}}metadata")
    manifest = package.find(f"{{{OPF}}}manifest")
    spine = package.find(f"{{{OPF}}}spine")
    if metadata is not None:
        titles = metadata.findall(f"{{{DC}}}title")
        typed = {
            (meta.get("refines"), (meta.text or "").strip())
            for meta in metadata.findall(f"{{{OPF}}}meta")
            if meta.get("property") == "title-type"
        }
        mains = [title for title in titles if (f"#{title.get('id')}", "main") in typed]
        if len(titles) > 1 and len(mains) != 1:
            errors.append(
                "package has more than one dc:title and does not mark exactly one "
                "title-type main. Kindle Previewer E2006 treats that as a conversion failure")
    if manifest is None or spine is None:
        return errors
    items = {item.get("id"): item for item in manifest.findall(f"{{{OPF}}}item")}
    cover_hrefs = {
        unquote(item.get("href", ""))
        for item in items.values()
        if "cover-image" in item.get("properties", "").split()
    }
    for name, document in parsed.items():
        # Pages are zip paths. Manifest hrefs are relative to the OPF, which
        # lives in the same directory as nav.xhtml in this pipeline (EPUB/).
        href = name.split("/", 1)[-1] if name.startswith("EPUB/") else name
        if not cover_hrefs:
            break
        body = next((node for node in document.iter() if _local(node.tag) == "body"), None)
        if body is None or re.sub(r"\s+", "", "".join(body.itertext())):
            continue
        for node in body.iter():
            src = node.get("src") or node.get("href") or node.get("{http://www.w3.org/1999/xlink}href") or ""
            if not src:
                continue
            resolved = posixpath.normpath(posixpath.join(posixpath.dirname(href), unquote(src.split("#", 1)[0])))
            names = {posixpath.basename(item) for item in cover_hrefs}
            if resolved in cover_hrefs or posixpath.basename(resolved) in names:
                errors.append(
                    f"{name} is an HTML cover page in addition to the declared cover "
                    "image. Kindle's cover rules say that can fail conversion")
                break
    for ref in package.findall(f"{{{OPF}}}guide/{{{OPF}}}reference"):
        if ref.get("type") != "cover" or not cover_hrefs:
            continue
        target = unquote(ref.get("href", ""))
        if target.lower().endswith((".xhtml", ".html", ".htm")):
            errors.append(
                f"guide cover reference points at {target} while a cover image is "
                "already declared. Kindle's cover rules say not to add that HTML page")
    return errors


def check(path: Path) -> list[str]:
    errors = []
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        css = "\n".join(
            archive.read(name).decode("utf-8", "replace")
            for name in names if name.endswith(".css"))
        errors.extend(stylesheet_errors(css))
        pngs = {name: archive.read(name) for name in names if name.endswith(".png")}
        pages = [
            (name, archive.read(name).decode("utf-8"))
            for name in names if name.endswith((".xhtml", ".html"))
        ]
        opf_name = next((name for name in names if name.endswith(".opf")), None)
        opf = archive.read(opf_name) if opf_name else None
        errors.extend(kindle_structure_errors(pages, opf))
    for name, text in pages:
        try:
            document = ET.fromstring(text)
        except ET.ParseError as error:
            errors.append(f"{name} has malformed XHTML: {error}")
        else:
            # XML parsing alone permits div in p; an HTML browser repairs it
            # silently. EPUB XHTML forbids that flow/phrasing mismatch.
            phrasing = {'p', 'span', 'em', 'strong', 'b', 'i', 'small', 'mark', 'sub', 'sup'}
            for container in document.iter():
                if container.tag.rsplit('}', 1)[-1] not in phrasing:
                    continue
                if any(node.tag.rsplit('}', 1)[-1] == 'div'
                       and 'oc-math-block' in node.attrib.get('class', '').split()
                       for node in container.iter()):
                    errors.append(f"{name} has block mathematics inside phrasing content")
                    break
        if "<math" in text or 'class="math inline"' in text or 'class="math display"' in text:
            errors.append(f"{name} still contains MathML or unrendered TeX; Kindle will mis-align it")
        for match in IMG_RE.finditer(text):
            attrs = parse_attrs(match.group(0))
            kind = attrs.get("class", "")
            if "oc-plate" in kind.split():
                errors.extend(_plate_errors(f"{name} plate", attrs, pngs, name))
            elif "oc-math-inline" in kind.split():
                errors.extend(_math_errors(f"{name} inline math", attrs, True, pngs, name))
            elif "oc-math-display" in kind.split():
                errors.extend(_math_errors(f"{name} display math", attrs, False, pngs, name))
        if re.search(r"<p\b[^>]*>\s*[.,;:!?]", text):
            errors.append(f"{name} has a paragraph that starts with punctuation torn off a formula")
        for figure in FIGURE_RE.finditer(text):
            for match in IMG_RE.finditer(figure.group(0)):
                attrs = parse_attrs(match.group(0))
                kind = attrs.get("class", "")
                if "oc-math-inline" in kind.split() or "oc-math-display" in kind.split():
                    continue
                if "oc-plate" in kind.split():
                    continue
                errors.extend(_plate_errors(f"{name} figure", attrs, pngs, name))
    return errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: check_epub_media.py book.epub", file=sys.stderr)
        return 2
    errors = check(Path(argv[1]))
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        print(f"{len(errors)} EPUB problem(s)", file=sys.stderr)
        return 1
    print("EPUB figures are full width and math carries an em baseline")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
