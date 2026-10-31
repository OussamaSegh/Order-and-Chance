"""Repair Pandoc EPUB resource names, then fit figures and math to a Kindle.

Figure plates become full-column PNGs. Mathematics becomes a transparent PNG
with an em width and an em vertical-align taken from the TeX depth. See
tools/epub_math.py and tools/epub_plates.py.
"""
import html as html_lib
import posixpath
import re
import sys
import zipfile
from pathlib import Path
from urllib.parse import unquote
import xml.etree.ElementTree as ET

import epub_math
import epub_plates


MATHML = "http://www.w3.org/1998/Math/MathML"
OPF = "http://www.idpf.org/2007/opf"


def fix_mathml(match: re.Match) -> str:
    """Move style attributes to elements that permit them in MathML Core.

    Pandoc 3.1's texmath puts displaystyle on mfrac for \\dfrac/\\tfrac,
    and uses mi for a sized slash (\\big/). EPUBCheck rejects both forms.
    Serialize just the affected formula, leaving the surrounding XHTML intact.
    """
    source = match.group(0)
    if not re.search(r'<(?:mfrac\b[^>]*\bdisplaystyle|mi\b[^>]*\b(?:minsize|maxsize))=', source):
        return source
    root = ET.fromstring(source)
    for parent in list(root.iter()):
        for index, child in enumerate(list(parent)):
            if child.tag == f"{{{MATHML}}}mfrac" and "displaystyle" in child.attrib:
                style = ET.Element(f"{{{MATHML}}}mstyle", {"displaystyle": child.attrib.pop("displaystyle")})
                style.tail, child.tail = child.tail, None
                parent.remove(child)
                style.append(child)
                parent.insert(index, style)
            elif child.tag == f"{{{MATHML}}}mi" and ("minsize" in child.attrib or "maxsize" in child.attrib):
                # minsize/maxsize belong to operators, not identifiers.
                child.tag = f"{{{MATHML}}}mo"
    ET.register_namespace("", MATHML)
    return ET.tostring(root, encoding="unicode")


def fix_volume_subtitle(root: ET.Element) -> bool:
    """Keep a volume's subtitle as EPUB 3 subtitle metadata, separate from its title.

    Pandoc renders --metadata subtitle on the title page but omits it from OPF.
    Recognise only this series' canonical numbered titles, leaving other EPUBs alone.
    """
    dc = "http://purl.org/dc/elements/1.1/"
    metadata = root.find(f"{{{OPF}}}metadata")
    if metadata is None:
        return False
    titles = metadata.findall(f"{{{dc}}}title")
    main_title = next((t for t in titles if "Order and Chance" in (t.text or "")), None)
    match = re.search(r"Volume ([0-9A-Z]+):", main_title.text or "") if main_title is not None else None
    if not match:
        return False
    from series_metadata import subtitle
    value = subtitle(match.group(1))
    if not value:
        return False
    marker = metadata.find(f"{{{OPF}}}meta[@property='title-type'][.='subtitle']")
    changed = False
    target = None
    if marker is not None:
        target = next((t for t in titles if "#" + t.get("id", "") == marker.get("refines")), None)
    if target is None:
        target = ET.SubElement(metadata, f"{{{dc}}}title", {"id": "oc-volume-subtitle"})
        marker = ET.SubElement(metadata, f"{{{OPF}}}meta", {"refines": "#oc-volume-subtitle", "property": "title-type"})
        marker.text = "subtitle"
        changed = True
    if target.text != value:
        target.text = value
        changed = True
    return changed


def fix_manifest(data: bytes, package_path: str, resources: dict[str, bytes],
                 add_items: list[tuple[str, str, str]] | None = None,
                 drop_hrefs: set[str] | None = None) -> bytes:
    """Declare MathML only where it remains, and list the PNG plates and formulas."""
    root = ET.fromstring(data)
    changed = fix_volume_subtitle(root)
    manifest = root.find(f"{{{OPF}}}manifest")
    for item in root.findall(f"{{{OPF}}}manifest/{{{OPF}}}item"):
        if item.get("media-type") != "application/xhtml+xml":
            continue
        target = posixpath.normpath(posixpath.join(posixpath.dirname(package_path), unquote(item.get("href", ""))))
        contents = resources.get(target, b"")
        has_math = b"http://www.w3.org/1998/Math/MathML" in contents
        properties = item.get("properties", "").split()
        if has_math and "mathml" not in properties:
            item.set("properties", " ".join(properties + ["mathml"]))
            changed = True
        elif not has_math and "mathml" in properties:
            properties = [token for token in properties if token != "mathml"]
            if properties:
                item.set("properties", " ".join(properties))
            else:
                item.attrib.pop("properties", None)
            changed = True
    if manifest is not None and drop_hrefs:
        for item in list(manifest):
            href = unquote(item.get("href", ""))
            if href in drop_hrefs and "cover-image" not in item.get("properties", ""):
                manifest.remove(item)
                changed = True
    if manifest is not None and add_items:
        existing = {unquote(item.get("href", "")): item for item in manifest}
        used_ids = {item.get("id") for item in manifest}
        for href, media_type, item_id in add_items:
            if href in existing:
                if existing[href].get("media-type") != media_type:
                    existing[href].set("media-type", media_type)
                    changed = True
                continue
            candidate = item_id
            suffix = 2
            while candidate in used_ids:
                candidate = f"{item_id}-{suffix}"
                suffix += 1
            used_ids.add(candidate)
            ET.SubElement(manifest, f"{{{OPF}}}item", {
                "id": candidate, "href": href, "media-type": media_type,
            })
            changed = True
    if not changed:
        return data
    ET.register_namespace("", OPF)
    ET.register_namespace("dc", "http://purl.org/dc/elements/1.1/")
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def fix_fragment_links(texts: dict[str, str]) -> dict[str, str]:
    """Point a same-file link (href="#id") at the chapter file that defines the id.

    Pandoc resolves cross-chapter references, but not those inside figure captions.
    """
    owner = {}
    for name, text in texts.items():
        for ident in re.findall(r'\bid="([^"]+)"', text):
            owner.setdefault(ident, name)
    fixed = {}
    for name, text in texts.items():
        # A label after two tabulars in one table gives pandoc two divs with the same id; keep the first.
        seen = set()

        def once(match, seen=seen):
            if match.group(1) in seen:
                return ""
            seen.add(match.group(1))
            return match.group(0)
        text = re.sub(r' id="([^"]+)"', once, text)
        local = set(re.findall(r'\bid="([^"]+)"', text))

        def repoint(match, name=name, local=local):
            ident = match.group(1)
            if ident in local or ident not in owner:
                return match.group(0)
            return f'href="{Path(owner[ident]).name}#{ident}"'
        fixed[name] = re.sub(r'href="#([^"]+)"', repoint, text)
    return fixed


IMG_RE = re.compile(r"<img\b[^>]*/?>", re.I)


def _attrs(tag: str) -> dict[str, str]:
    return {key: html_lib.unescape(value) for key, value in re.findall(r'([\w:-]+)="([^"]*)"', tag)}


def _resolve(page: str, src: str) -> str:
    path = unquote(src.split("#", 1)[0].split("?", 1)[0])
    return posixpath.normpath(posixpath.join(posixpath.dirname(page), path))


def _package_root(resources: dict[str, bytes]) -> str:
    return posixpath.dirname(next(name for name in resources if name.endswith(".opf")))


def _href(package_path: str, zip_name: str) -> str:
    return posixpath.relpath(zip_name, posixpath.dirname(package_path))


def _xml_id(prefix: str, stem: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9_.-]", "-", stem)
    if not safe or not safe[0].isalpha():
        safe = "p" + safe
    return f"{prefix}-{safe}"[:80]


def _plate_tag(src: str, alt: str) -> str:
    alt_attr = html_lib.escape(alt or "Figure", quote=True)
    src_attr = html_lib.escape(src, quote=True)
    return (
        f'<img class="oc-plate" src="{src_attr}" alt="{alt_attr}" '
        'style="width:100%;max-width:100%;height:auto"/>'
    )


def normalize_svgz(resources: dict[str, bytes]) -> dict[str, bytes]:
    """Pandoc names plate files ``.svgz`` even when the bytes are plain SVG."""
    renamed = {}
    for name, data in resources.items():
        new = name[:-1] if name.endswith(".svgz") else name
        if new.endswith((".xhtml", ".html", ".opf", ".ncx", ".css")):
            data = data.replace(b'.svgz"', b'.svg"')
        renamed[new] = data
    return renamed


def apply_math(resources: dict[str, bytes], cache: Path | None) -> dict[str, bytes]:
    pages = [name for name in resources if name.endswith((".xhtml", ".html"))]
    texts = {name: resources[name].decode("utf-8") for name in pages}
    keys = []
    for text in texts.values():
        keys.extend(epub_math.collect_keys(text))
    if not keys:
        return resources
    unique = list(dict.fromkeys(keys))
    print(f"EPUB math: {len(keys)} formulas ({len(unique)} unique)", flush=True)
    glyphs = epub_math.render_formulas(unique, cache)
    root = _package_root(resources)
    for name, text in texts.items():
        text, media = epub_math.replace_math(text, glyphs, name, root)
        resources[name] = text.encode("utf-8")
        resources.update(media)
    return resources


def apply_plates(resources: dict[str, bytes], figures: Path) -> tuple[dict[str, bytes], list[tuple[str, str, str]], set[str]]:
    by_hash = epub_plates.index_svgs(figures)
    package = next(name for name in resources if name.endswith(".opf"))
    added: dict[str, tuple[str, str, str]] = {}
    drop_zip: set[str] = set()
    replaced = 0
    for name in [item for item in resources if item.endswith((".xhtml", ".html"))]:
        text = resources[name].decode("utf-8")

        def repl(match: re.Match, page: str = name) -> str:
            nonlocal replaced
            tag = match.group(0)
            attrs = _attrs(tag)
            src = attrs.get("src", "")
            if not src.lower().split("?")[0].endswith(".svg"):
                return tag
            if "oc-math" in attrs.get("class", ""):
                return tag
            zip_src = _resolve(page, src)
            data = resources.get(zip_src)
            if data is None:
                raise FileNotFoundError(f"{page} points at missing figure {zip_src}")
            svg = epub_plates.match_svg(data, by_hash)
            if svg is None:
                preview = data[:80]
                raise FileNotFoundError(
                    f"{src} does not match a figure SVG in {figures} ({preview!r})")
            png_zip = posixpath.join(posixpath.dirname(zip_src), f"oc-plate-{svg.stem}.png")
            if png_zip not in resources:
                resources[png_zip] = epub_plates.rasterize(svg.with_suffix(".pdf"))
            href = _href(package, png_zip)
            added[href] = (href, "image/png", _xml_id("plate", svg.stem))
            drop_zip.add(zip_src)
            replaced += 1
            return _plate_tag(posixpath.relpath(png_zip, posixpath.dirname(page)), attrs.get("alt", ""))

        resources[name] = IMG_RE.sub(repl, text).encode("utf-8")
    if replaced:
        print(f"EPUB figures: {replaced} plates at {epub_plates.PLATE_PX} px", flush=True)
    # Drop the SVG once the pages no longer point at it. The manifest still names it;
    # that reference is removed with the file, so it must not count as a use.
    blob = b"\n".join(
        data for key, data in resources.items()
        if key.endswith((".xhtml", ".html", ".ncx", ".css")))
    drop_hrefs = set()
    for zip_name in drop_zip:
        href = _href(package, zip_name)
        if href.encode("utf-8") not in blob and zip_name.encode("utf-8") not in blob:
            resources.pop(zip_name, None)
            drop_hrefs.add(href)
    return resources, list(added.values()), drop_hrefs


def main(path: str, figures: str | None = None, *, render_math: bool = True) -> None:
    src = Path(path)
    tmp = src.with_suffix(".tmp")
    with zipfile.ZipFile(src) as zin:
        dates = {item.filename: item.date_time for item in zin.infolist()}
        resources = {item.filename: zin.read(item.filename) for item in zin.infolist()}
    resources = normalize_svgz(resources)
    pages = fix_fragment_links({
        name: data.decode("utf-8") for name, data in resources.items()
        if name.endswith(".xhtml") and "/text/" in name
    })
    for name, text in pages.items():
        resources[name] = text.encode("utf-8")
    cache = Path(figures).parent / "epub-math-cache" if figures else None
    if render_math:
        resources = apply_math(resources, cache)
    added: list[tuple[str, str, str]] = []
    dropped: set[str] = set()
    if figures:
        resources, added, dropped = apply_plates(resources, Path(figures))
    for name in list(resources):
        if name.endswith(".xhtml"):
            resources[name] = re.sub(
                r"<math\b[^>]*>.*?</math>", fix_mathml, resources[name].decode("utf-8"), flags=re.S,
            ).encode("utf-8")
    package = next(name for name in resources if name.endswith(".opf"))
    # Media added above is not in the original manifest. Plates and formulas both need entries.
    media_items = list(added)
    known_hrefs = set()
    root = ET.fromstring(resources[package])
    for item in root.findall(f"{{{OPF}}}manifest/{{{OPF}}}item"):
        known_hrefs.add(unquote(item.get("href", "")))
    for zip_name in resources:
        if not zip_name.endswith(".png") or "oc-math-" not in posixpath.basename(zip_name):
            continue
        href = _href(package, zip_name)
        if href not in known_hrefs:
            media_items.append((href, "image/png", _xml_id("math", Path(zip_name).stem)))
    resources[package] = fix_manifest(resources[package], package, resources, media_items, dropped)
    stamp = next(iter(dates.values()), (2026, 1, 1, 0, 0, 0))
    with zipfile.ZipFile(tmp, "w") as zout:
        names = ["mimetype"] + [name for name in resources if name != "mimetype"] if "mimetype" in resources else list(resources)
        for name in names:
            info = zipfile.ZipInfo(name, dates.get(name, stamp))
            compress = zipfile.ZIP_STORED if name == "mimetype" else zipfile.ZIP_DEFLATED
            zout.writestr(info, resources[name], compress_type=compress)
    tmp.replace(src)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
