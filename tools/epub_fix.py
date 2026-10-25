"""Post-process an EPUB written by pandoc: pandoc names SVG images *.svgz although they are
plain (uncompressed) SVG, which some readers refuse. Rename them to *.svg in place."""
import sys
import zipfile
from pathlib import Path


def main(path: str) -> None:
    src = Path(path)
    tmp = src.with_suffix(".tmp")
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(tmp, "w") as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            name = item.filename
            if name.endswith(".svgz"):
                name = name[:-1]
            if name.endswith((".xhtml", ".opf", ".ncx")):
                data = data.replace(b".svgz\"", b".svg\"")
            compress = zipfile.ZIP_STORED if name == "mimetype" else zipfile.ZIP_DEFLATED
            zout.writestr(zipfile.ZipInfo(name, item.date_time), data, compress_type=compress)
    tmp.replace(src)


if __name__ == "__main__":
    main(sys.argv[1])
