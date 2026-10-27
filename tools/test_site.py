"""Run with python -m unittest discover -s tools -p test_site.py."""
from html.parser import HTMLParser
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import importlib.util

spec = importlib.util.spec_from_file_location("book_site", Path(__file__).with_name("site.py"))
site = importlib.util.module_from_spec(spec)
spec.loader.exec_module(site)


class Tags(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


class LibraryTest(unittest.TestCase):
    def test_approved_cover_pngs_are_copied_without_rasterization(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            dist, out = root / "dist", root / "site"
            dist.mkdir()
            books = [("0", "tome0-mathematical-maturity", "Mathematical Maturity"),
                     ("1", "tome1-integers", "The Integers")]
            for number, book, title in books:
                (root / book).mkdir()
                (root / book / "main.tex").write_text(
                    f"% epub-title: Order and Chance. Tome {number}: {title}\n")
                (dist / f"{book}.pdf").write_bytes(b"fixture")
                (root / "build" / book).mkdir(parents=True)
                (root / "build" / book / "cover.pdf").write_bytes(b"fixture")
            with patch.object(site, "ROOT", root), patch.object(site.subprocess, "run") as render:
                site.main(str(dist), str(out))
                render.assert_not_called()
            assets = Path(site.__file__).parent / "assets"
            for number, book, _ in books:
                with self.subTest(volume=number):
                    self.assertEqual((out / f"{book}-cover.png").read_bytes(),
                                     (assets / f"approved-volume-{number}.png").read_bytes())

    def test_available_formats_collections_and_retired_outputs(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            dist, out = root / "dist", root / "site"
            dist.mkdir()
            for name in ["tome10-chance2", "tome2-structures", "tomeC1-discrete", "tomeS1-linear", "tomeP1-crossroads"]:
                (dist / (name + ".pdf")).write_bytes(b"fixture")
                if not name.startswith(("tomeC", "tomeS")):
                    (root / name).mkdir()
                    (root / name / "main.tex").write_text("fixture")
            (dist / "tome2-structures-phone.pdf").write_bytes(b"retired")
            (dist / "tome2-structures-kindle.pdf").write_bytes(b"fixture")
            (dist / "tome2-structures-a4.pdf").write_bytes(b"retired")
            (dist / "kdp").mkdir()
            (dist / "kdp/tome2-structures-print.pdf").write_bytes(b"print interior")
            (dist / "tome2-structures.epub").write_bytes(b"fixture")
            out.mkdir()
            (out / "tomeC1-discrete.pdf").write_bytes(b"stale download")
            for suffix in ['a4', 'kindle', 'phone', 'print']:
                (out / f'tome2-structures-{suffix}.pdf').write_bytes(b'stale download')
            (out / "read/tomeS1-linear").mkdir(parents=True)
            (out / "read/tomeS1-linear/index.html").write_text("stale reader")
            with patch.object(site, "ROOT", root):
                site.main(str(dist), str(out))
            text = (out / "index.html").read_text()
            tags = Tags()
            tags.feed(text)
            cards = [a for t, a in tags.tags if t == "article"]
            self.assertEqual([a["data-collection"] for a in cards], ["main", "main", "problems"])
            self.assertLess(text.index('data-search="tome2-'), text.index('data-search="tome10-'))
            self.assertEqual(text.count('>EPUB</a>'), 1)
            self.assertNotIn('-phone.pdf', text)
            self.assertNotIn('-kindle.pdf', text)
            self.assertIn('href="tome2-structures-print.pdf"', text)
            self.assertIn('>Print PDF</a>', text)
            self.assertNotIn('A4', text)
            self.assertIn('7 × 10 in PDF with cover', text)
            self.assertIn('>PDF with cover</a>', text)
            for suffix in ['a4', 'kindle', 'phone']:
                self.assertFalse((out / f'tome2-structures-{suffix}.pdf').exists())
            self.assertEqual((out / 'tome2-structures-print.pdf').read_bytes(), b'print interior')
            self.assertNotIn('tomeC1-discrete', text)
            self.assertNotIn('tomeS1-linear', text)
            self.assertFalse((out / 'tomeC1-discrete.pdf').exists())
            self.assertFalse((out / 'read/tomeS1-linear').exists())
            self.assertFalse((out / "tome2-structures-phone.pdf").exists())
            for tag, attrs in tags.tags:
                if tag == 'a' and attrs.get('href', '').endswith(('.pdf', '.epub')):
                    self.assertTrue((out / attrs['href']).exists())

    def test_titles_are_escaped_in_text_and_search_attributes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "dist").mkdir()
            (root / "tome0-test").mkdir()
            (root / "dist/tome0-test.pdf").write_bytes(b"fixture")
            (root / "tome0-test/main.tex").write_text('% epub-title: Series. A < B & "C"\n')
            with patch.object(site, "ROOT", root):
                site.main(str(root / "dist"), str(root / "out"))
            text = (root / "out/index.html").read_text()
            self.assertIn('A &lt; B &amp; &quot;C&quot;', text)
            self.assertNotIn('A < B', text)


if __name__ == '__main__':
    unittest.main()
