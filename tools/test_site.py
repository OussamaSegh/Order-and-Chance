"""Run with python -m unittest discover -s tools -p test_site.py."""
from html.parser import HTMLParser
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import importlib.util
from public_names import filename
from urllib.parse import unquote

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
    def test_every_volume_uses_the_shared_master_including_earlier_concepts(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            dist, out = root / "dist", root / "site"
            dist.mkdir()
            books = [("1", "volume1-first-principles", "First Principles"),
                     ("2", "volume2-integers", "The Integers"),
                     ("3", "volume3-symmetry", "Symmetry")]
            for number, book, title in books:
                (root / book).mkdir()
                (root / book / "main.tex").write_text(
                    f"% epub-title: Order and Chance. Volume {number}: {title}\n")
                (dist / filename(book, "pdf", root)).write_bytes(b"fixture")
                (root / "build" / book).mkdir(parents=True)
                (root / "build" / book / "cover.pdf").write_bytes(b"fixture")
            def write_preview(command, **kwargs):
                Path(command[-1]+".png").write_bytes(b"shared-master-render")
            with patch.object(site, "ROOT", root), patch.object(site.subprocess, "run", side_effect=write_preview) as render:
                site.main(str(dist), str(out))
                self.assertEqual(render.call_count, 3)
            for number, book, _ in books:
                with self.subTest(volume=number):
                    self.assertEqual((out / filename(book, "thumbnail", root)).read_bytes(), b"shared-master-render")

    def test_available_formats_collections_and_retired_outputs(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            dist, out = root / "dist", root / "site"
            dist.mkdir()
            for name in ["volume10-chance2", "volume2-structures", "volumeC1-discrete", "volumeS1-linear"]:

                if not name.startswith(("volumeC", "volumeS")):
                    (root / name).mkdir()
                    (root / name / "main.tex").write_text("fixture")
                    (dist / filename(name, "pdf", root)).write_bytes(b"fixture")
            (dist / "volume2-structures-phone.pdf").write_bytes(b"retired")
            (dist / "volume2-structures-kindle.pdf").write_bytes(b"fixture")
            (dist / "volume2-structures-a4.pdf").write_bytes(b"retired")
            (dist / "kdp").mkdir()
            (dist / "kdp/Volume 2 - Structures - Print.pdf").write_bytes(b"print interior")
            (dist / "Volume 2 - Structures.epub").write_bytes(b"fixture")
            out.mkdir()
            (out / "volumeC1-discrete.pdf").write_bytes(b"stale download")
            for suffix in ['a4', 'kindle', 'phone', 'print']:
                (out / f'volume2-structures-{suffix}.pdf').write_bytes(b'stale download')
            (out / "read/volumeS1-linear").mkdir(parents=True)
            (out / "read/volumeS1-linear/index.html").write_text("stale reader")
            with patch.object(site, "ROOT", root):
                site.main(str(dist), str(out))
            text = (out / "index.html").read_text()
            tags = Tags()
            tags.feed(text)
            cards = [a for t, a in tags.tags if t == "article"]
            self.assertEqual([a["data-collection"] for a in cards], ["main", "main"])
            self.assertLess(text.index('data-search="volume2-'), text.index('data-search="volume10-'))
            self.assertEqual(text.count('>EPUB</a>'), 1)
            self.assertNotIn('-phone.pdf', text)
            self.assertNotIn('-kindle.pdf', text)
            self.assertIn('href="Volume%202%20-%20Structures%20-%20Print.pdf"', text)
            self.assertIn('>Print PDF</a>', text)
            self.assertNotIn('A4', text)
            self.assertIn('7 × 10 in PDF with cover', text)
            self.assertIn('>PDF with cover</a>', text)
            for suffix in ['a4', 'kindle', 'phone']:
                self.assertFalse((out / f'volume2-structures-{suffix}.pdf').exists())
            self.assertEqual((out / 'Volume 2 - Structures - Print.pdf').read_bytes(), b'print interior')
            self.assertNotIn('volumeC1-discrete', text)
            self.assertNotIn('volumeS1-linear', text)
            self.assertFalse((out / 'volumeC1-discrete.pdf').exists())
            self.assertFalse((out / 'read/volumeS1-linear').exists())
            self.assertFalse((out / "volume2-structures-phone.pdf").exists())
            for tag, attrs in tags.tags:
                if tag == 'a' and attrs.get('href', '').endswith(('.pdf', '.epub')):
                    self.assertTrue((out / unquote(attrs['href'])).exists())

    def test_published_reader_urls_redirect(self):
        from legacy_urls import OLD_STEMS
        old, new = next(pair for pair in OLD_STEMS.items() if pair[1] == "volume1-first-principles")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            dist, out = root / "dist", root / "site"
            dist.mkdir()
            (root / new).mkdir()
            (root / new / "main.tex").write_text(
                "% epub-title: Order and Chance. Volume 1: First Principles\n")
            (dist / filename(new, "pdf", root)).write_bytes(b"fixture")
            reader = dist / "html" / new
            reader.mkdir(parents=True)
            (reader / "index.html").write_text("current index")
            (reader / "preface.html").write_text("current preface")
            with patch.object(site, "ROOT", root):
                site.main(str(dist), str(out))
            index = (out / "read" / old / "index.html").read_text()
            preface = (out / "read" / old / "preface.html").read_text()
            self.assertIn(f"../{new}/index.html", index)
            self.assertIn(f"../{new}/preface.html", preface)
            self.assertIn("http-equiv=\"refresh\"", index)
            self.assertIn(f"read/{new}/", (out / "index.html").read_text())

    def test_former_part_pages_redirect_to_the_part_page(self):
        with tempfile.TemporaryDirectory() as directory:
            reader = Path(directory)
            (reader / "index.html").write_text('<a href="preface.html">P</a><a href="part-divisibility.html">I</a>'
                                               '<a href="1-ch-divisibility.html">1</a><a href="part-the-primes.html">II</a>')
            (reader / "preface.html").write_text("<h1>Preface</h1>")
            for name in ("part-divisibility.html", "part-the-primes.html"):
                (reader / name).write_text('<h1 class="oc-part">Part</h1>')
            (reader / "1-ch-divisibility.html").write_text('<h1 class="oc-chapter">Divisibility</h1>')
            site.write_part_redirects(reader)
            self.assertIn('url=part-divisibility.html', (reader / "1-divisibility.html").read_text())
            self.assertIn('url=part-divisibility.html', (reader / "divisibility.html").read_text())
            self.assertIn('url=part-the-primes.html', (reader / "2-the-primes.html").read_text())
            self.assertIn('oc-chapter', (reader / "1-ch-divisibility.html").read_text())
            self.assertFalse((reader / "1-preface.html").exists())

    def test_titles_are_escaped_in_text_and_search_attributes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "dist").mkdir()
            (root / "volume0-test").mkdir()
            (root / "dist/Volume 0 - Safe Title.pdf").write_bytes(b"fixture")
            (root / "volume0-test/main.tex").write_text('% epub-title: A < B & "C". Volume 0: Safe Title\n')
            with patch.object(site, "ROOT", root):
                site.main(str(root / "dist"), str(root / "out"))
            text = (root / "out/index.html").read_text()
            self.assertIn('a &lt; b &amp; &quot;c&quot;', text)
            self.assertNotIn('A < B', text)


if __name__ == '__main__':
    unittest.main()
