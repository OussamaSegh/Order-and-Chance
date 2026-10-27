"""Exercise invalidation and complete-library assembly without TeX or network."""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('build_plan', Path(__file__).with_name('build_plan.py'))
bp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bp)


class PlanningTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.cache = self.root / '.book-cache'
        self.books = ['tome0-basics', 'tome1-integers', 'tome9-higher-structures']
        subprocess.run(['git', 'init', '-q', str(self.root)], check=True)
        for name in self.books:
            self.write(name + '/main.tex', name)
        for path in ['common/preamble.tex', 'tools/epub_prep.py', 'build.sh',
                     'tools/site.py', 'tools/site-template.html', 'python/tome0/example.ipynb',
                     'tools/assets/paper.jpg']:
            self.write(path, 'original')
        subprocess.run(['git', 'add', '.'], cwd=self.root, check=True)
        for book in self.books:
            self.outputs(self.cache, book)
        (self.cache / 'manifest.json').write_text(json.dumps({'schema': 1, 'books': bp.fingerprints(self.root)}))

    def write(self, path, text):
        p = self.root / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)

    def outputs(self, target, book):
        for path in [f'dist/{book}.pdf', f'dist/{book}-kindle.pdf', f'dist/{book}.epub',
                     f'dist/html/{book}/index.html', f'build/{book}/cover.pdf'] + [
                         f'dist/kdp/{book}-{suffix}' for suffix in
                         ['print.pdf', 'cover-wrap.pdf', 'ebook-cover.jpg', 'listing.md']]:
            p = target / path
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(b'valid fixture')

    def test_unchanged_site_and_notebooks_do_not_rebuild_books(self):
        for path in ['tools/site.py', 'tools/site-template.html', 'python/tome0/example.ipynb']:
            self.write(path, 'updated')
        self.assertEqual(bp.plan(self.root, self.cache)['changed'], [])

    def test_one_book_invalidates_only_itself(self):
        self.write('tome0-basics/main.tex', 'new theorem')
        self.assertEqual(bp.plan(self.root, self.cache)['changed'], ['tome0-basics'])

    def test_shared_sources_and_converter_rebuild_all(self):
        for path in ['common/preamble.tex', 'tools/epub_prep.py', 'build.sh', 'tools/assets/paper.jpg']:
            with self.subTest(path=path):
                self.write(path, 'updated')
                self.assertEqual(bp.plan(self.root, self.cache)['changed'], self.books)
                self.write(path, 'original')

    def test_missing_cache_missing_file_and_force(self):
        self.assertEqual(bp.plan(self.root, self.root / 'missing')['changed'], self.books)
        self.assertEqual(bp.plan(self.root, self.cache, force=True)['changed'], self.books)
        (self.cache / 'dist/tome1-integers.epub').unlink()
        self.assertEqual(bp.plan(self.root, self.cache)['changed'], ['tome1-integers'])

    def test_overlay_preserves_unchanged_and_drops_stale_chapters(self):
        self.write('tome0-basics/main.tex', 'changed')
        stale = self.cache / 'dist/html/tome0-basics/deleted-chapter.html'
        stale.write_text('stale')
        data = bp.plan(self.root, self.cache)
        bp.prepare(self.root, self.cache, data)
        self.assertTrue((self.root / 'dist/tome1-integers.pdf').exists())
        self.assertFalse((self.root / 'dist/html/tome0-basics').exists())
        for book in data['changed']:
            self.outputs(self.root, book)
        bp.snapshot(self.root, self.cache, data)
        self.assertEqual(bp.plan(self.root, self.cache)['changed'], [])
        self.assertFalse(stale.exists())

    def test_incomplete_library_cannot_be_snapshotted(self):
        with self.assertRaisesRegex(ValueError, 'Incomplete output'):
            bp.snapshot(self.root, self.cache, bp.plan(self.root, self.cache))

    def test_removed_book_is_not_republished(self):
        subprocess.run(['git', 'rm', '-qrf', 'tome1-integers'], cwd=self.root, check=True)
        data = bp.plan(self.root, self.cache)
        self.assertEqual(data['removed'], ['tome1-integers'])
        bp.prepare(self.root, self.cache, data)
        self.assertFalse((self.root / 'dist/tome1-integers.pdf').exists())
        self.assertTrue((self.root / 'dist/tome0-basics.pdf').exists())


if __name__ == '__main__':
    unittest.main()
