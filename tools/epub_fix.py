"""Repair Pandoc EPUB resource names and MathML for conforming EPUB readers."""
import posixpath
import re
import sys
import zipfile
from pathlib import Path
from urllib.parse import unquote
import xml.etree.ElementTree as ET


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


def fix_manifest(data: bytes, package_path: str, resources: dict[str, bytes]) -> bytes:
    """Declare MathML on all XHTML resources, including the generated TOC."""
    root = ET.fromstring(data)
    changed = False
    for item in root.findall(f"{{{OPF}}}manifest/{{{OPF}}}item"):
        if item.get("media-type") != "application/xhtml+xml":
            continue
        target = posixpath.normpath(posixpath.join(posixpath.dirname(package_path), unquote(item.get("href", ""))))
        contents = resources.get(target, b"")
        if b"http://www.w3.org/1998/Math/MathML" not in contents:
            continue
        properties = item.get("properties", "").split()
        if "mathml" not in properties:
            item.set("properties", " ".join(properties + ["mathml"]))
            changed = True
    if not changed:
        return data
    ET.register_namespace("", OPF)
    ET.register_namespace("dc", "http://purl.org/dc/elements/1.1/")
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def main(path: str) -> None:
    src = Path(path)
    tmp = src.with_suffix(".tmp")
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(tmp, "w") as zout:
        resources = {item.filename: zin.read(item.filename) for item in zin.infolist()}
        for item in zin.infolist():
            data = resources[item.filename]
            name = item.filename
            if name.endswith(".svgz"):
                name = name[:-1]
            if name.endswith((".xhtml", ".opf", ".ncx")):
                data = data.replace(b".svgz\"", b".svg\"")
            if name.endswith(".xhtml"):
                data = re.sub(r"<math\b[^>]*>.*?</math>", fix_mathml, data.decode("utf-8"), flags=re.S).encode("utf-8")
            elif name.endswith(".opf"):
                data = fix_manifest(data, item.filename, resources)
            compress = zipfile.ZIP_STORED if name == "mimetype" else zipfile.ZIP_DEFLATED
            zout.writestr(zipfile.ZipInfo(name, item.date_time), data, compress_type=compress)
    tmp.replace(src)


if __name__ == "__main__":
    main(sys.argv[1])
