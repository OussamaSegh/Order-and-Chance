"""Regression checks for EPUB anchors, MathML, and resource declarations.

Run: python3 -m unittest discover -s tools -p test_epub.py
Requires Pandoc. Set EPUBCHECK_JAR to also validate the generated miniature EPUB.
"""
from collections import Counter
from html.parser import HTMLParser
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
import xml.etree.ElementTree as ET
import zipfile

import epub_fix
import epub_prep


TOOLS = Path(__file__).resolve().parent
SAMPLE = r"""
\documentclass{book}
\begin{document}
\chapter{Counting $p$}
\begin{exercise}\label{ex:sample}
Compare $\dfrac{1}{2}$ and $\tfrac{1}{2}$, and $x\big/y$.
\end{exercise}
\begin{hint}{ex:sample}Use a common denominator.\end{hint}
\begin{solution}{ex:sample}They are equal.\end{solution}
See Exercise~\ref{ex:sample}.
\begin{figure}
\includegraphics{diagram.svg}
\includegraphics[alt={An explicitly described square.}]{diagram.svg}
\caption{A square with four equal sides.}
\end{figure}
\end{document}
"""


class Tags(HTMLParser):
    def __init__(self):
        super().__init__()
        self.attributes = []

    def handle_starttag(self, tag, attrs):
        self.attributes.append((tag, dict(attrs)))


@unittest.skipUnless(shutil.which("pandoc"), "Pandoc is required")
class EpubRegression(unittest.TestCase):
    def convert(self, target, *arguments, cwd=None):
        return subprocess.run(
            ["pandoc", "-f", "latex", "-t", target, "--mathml",
             "--lua-filter", str(TOOLS / "epub.lua"), *arguments],
            input=SAMPLE, text=True, capture_output=True, check=True, cwd=cwd)

    def test_online_anchors(self):
        output = self.convert("html5").stdout
        tags = Tags()
        tags.feed(output)
        ids = [attrs["id"] for _, attrs in tags.attributes if "id" in attrs]
        self.assertEqual(ids.count("ex:sample"), 1)
        self.assertEqual(len(ids), len(set(ids)))
        self.assertFalse(any("label" in attrs for _, attrs in tags.attributes))
        links = [attrs.get("href") for tag, attrs in tags.attributes if tag == "a"]
        self.assertEqual(links.count("#ex:sample"), 3)  # hint, solution, reference
        alternatives = [attrs.get("alt") for tag, attrs in tags.attributes if tag == "img"]
        self.assertEqual(alternatives, ["A square with four equal sides.", "An explicitly described square."])

    def test_portrait_alternative(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "main.tex"
            destination = Path(directory) / "epub.tex"
            source.write_text(r"\portrait{fermat}{Pierre de Fermat (1601--1665). Historical portrait.}" + "\n")
            epub_prep.main(str(source), str(destination), directory)
            result = subprocess.run(["pandoc", "-f", "latex", "-t", "html5", str(destination)],
                                    capture_output=True, text=True, check=True)
            tags = Tags()
            tags.feed(result.stdout)
            alternatives = [attrs.get("alt") for tag, attrs in tags.attributes if tag == "img"]
            self.assertEqual(alternatives, ["Portrait of Pierre de Fermat (1601–1665)."])

    def test_reader_index_has_unique_contents_ids(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "reader"
            (Path(directory) / "diagram.svg").write_text(
                '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20"/>')
            self.convert("chunkedhtml", "--toc", "--split-level=1",
                         "--template", str(TOOLS / "reader-template.html"),
                         "--metadata", "booktitle=Arithmetic", "-o", str(output), cwd=directory)
            tags = Tags()
            tags.feed((output / "index.html").read_text())
            ids = [attrs["id"] for _, attrs in tags.attributes if "id" in attrs]
            self.assertEqual(len(ids), len(set(ids)))
            self.assertIn("contents", ids)
            self.assertTrue(any(attrs.get("href") == "#contents"
                                for _, attrs in tags.attributes))

    def test_epub_math_and_manifest(self):
        with tempfile.TemporaryDirectory() as directory:
            book = Path(directory) / "sample.epub"
            (Path(directory) / "diagram.svg").write_text(
                '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20">'
                '<rect x="1" y="1" width="18" height="18"/></svg>')
            self.convert("epub3", "--toc", "--metadata", "title=Arithmetic",
                         "--metadata", "lang=en", "-o", str(book), cwd=directory)
            epub_fix.main(str(book))
            with zipfile.ZipFile(book) as archive:
                contents = {name: archive.read(name) for name in archive.namelist()}
                package_name = next(name for name in contents if name.endswith(".opf"))
                package = ET.fromstring(contents[package_name])
                items = package.findall(f"{{{epub_fix.OPF}}}manifest/{{{epub_fix.OPF}}}item")
                nav = next(item for item in items if "nav" in item.get("properties", "").split())
                self.assertIn("mathml", nav.get("properties", "").split())
                styles = []
                for name, data in contents.items():
                    if not name.endswith(".xhtml"):
                        continue
                    root = ET.fromstring(data)
                    ids = [node.attrib["id"] for node in root.iter() if "id" in node.attrib]
                    self.assertFalse([key for key, count in Counter(ids).items() if count > 1])
                    for node in root.iter():
                        self.assertNotIn("label", node.attrib)
                        if node.tag == f"{{{epub_fix.MATHML}}}mfrac":
                            self.assertNotIn("displaystyle", node.attrib)
                        if node.tag == f"{{{epub_fix.MATHML}}}mi":
                            self.assertNotIn("minsize", node.attrib)
                            self.assertNotIn("maxsize", node.attrib)
                        if node.tag == f"{{{epub_fix.MATHML}}}mstyle":
                            styles.append(node.get("displaystyle"))
                self.assertIn("true", styles)
                self.assertIn("false", styles)
            epub_fix.main(str(book))
            with zipfile.ZipFile(book) as archive:
                self.assertEqual(contents, {name: archive.read(name) for name in archive.namelist()})
            jar = os.environ.get("EPUBCHECK_JAR")
            if jar:
                subprocess.run(["java", "-jar", jar, str(book)], capture_output=True, check=True)


if __name__ == "__main__":
    unittest.main()
