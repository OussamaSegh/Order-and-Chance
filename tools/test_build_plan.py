"""Exercise invalidation and complete-library assembly without TeX or network."""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('build_plan', Path(__file__).with_name('build_plan.py'))
bp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bp)


class PlanningTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.cache = self.root / '.book-cache'
        checker = patch.object(bp, 'check_interior', return_value=233)
        self.pdf_check = checker.start()
        self.addCleanup(checker.stop)
        pair_checker = patch.object(bp, 'check_pair', return_value=233)
        self.pair_check = pair_checker.start()
        self.addCleanup(pair_checker.stop)
        cover_checker = patch.object(bp, 'check_print_cover', return_value={'status': 'pass'})
        self.cover_check = cover_checker.start()
        self.addCleanup(cover_checker.stop)
        self.books = ['tome0-basics', 'tome1-integers', 'tome9-higher-structures']
        subprocess.run(['git', 'init', '-q', str(self.root)], check=True)
        for name in self.books:
            self.write(name + '/main.tex', name)
        for path in ['common/preamble.tex', 'common/print-layout.json', 'tools/epub_prep.py', 'build.sh',
                     'tools/site.py', 'tools/site-template.html', 'python/tome0/example.ipynb',
                     'tools/assets/paper.jpg', 'tools/requirements-build.txt']:
            self.write(path, 'original')
        subprocess.run(['git', 'add', '.'], cwd=self.root, check=True)
        for book in self.books:
            self.outputs(self.cache, book)
        (self.cache / 'manifest.json').write_text(json.dumps({'schema': bp.SCHEMA, 'books': bp.fingerprints(self.root)}))

    def write(self, path, text):
        p = self.root / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)

    def outputs(self, target, book):
        for path in [f'dist/{book}.pdf', f'dist/{book}.epub',
                     f'dist/html/{book}/index.html', f'build/{book}/cover.pdf'] + [
                         f'dist/kdp/{book}-{suffix}' for suffix in
                         ['print.pdf', 'cover-wrap.pdf', 'ebook-cover.jpg', 'listing.md', 'print-metadata.json']]:
            p = target / path
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(b'valid fixture')
        (target / f'dist/kdp/{book}-print-metadata.json').write_text(json.dumps(bp.specification(233)))

    def test_both_pdf_editions_and_epub_are_required(self):
        self.assertTrue(bp.complete(self.cache, self.books[0]))
        self.assertFalse(list((self.cache / 'dist').glob('*-kindle.pdf')))
        self.assertTrue((self.cache / 'dist/kdp' / (self.books[0] + '-print.pdf')).exists())
        (self.cache / 'dist/kdp' / (self.books[0] + '-print.pdf')).unlink()
        self.assertFalse(bp.complete(self.cache, self.books[0]))

    def test_unchanged_site_and_notebooks_do_not_rebuild_books(self):
        for path in ['tools/site.py', 'tools/site-template.html', 'python/tome0/example.ipynb']:
            self.write(path, 'updated')
        self.assertEqual(bp.plan(self.root, self.cache)['changed'], [])

    def test_one_book_invalidates_only_itself(self):
        self.write('tome0-basics/main.tex', 'new theorem')
        self.assertEqual(bp.plan(self.root, self.cache)['changed'], ['tome0-basics'])

    def test_shared_sources_and_converter_rebuild_all(self):
        for path in ['common/preamble.tex', 'common/print-layout.json', 'tools/epub_prep.py', 'build.sh', 'tools/assets/paper.jpg', 'tools/requirements-build.txt']:
            with self.subTest(path=path):
                self.write(path, 'updated')
                self.assertEqual(bp.plan(self.root, self.cache)['changed'], self.books)
                self.write(path, 'original')

    def test_missing_cache_missing_file_and_force(self):
        self.assertEqual(bp.plan(self.root, self.root / 'missing')['changed'], self.books)
        self.assertEqual(bp.plan(self.root, self.cache, force=True)['changed'], self.books)
        (self.cache / 'dist/tome1-integers.epub').unlink()
        self.assertEqual(bp.plan(self.root, self.cache)['changed'], ['tome1-integers'])

    def test_old_trim_cache_and_missing_print_spec_force_rebuild(self):
        manifest = self.cache / 'manifest.json'
        data = json.loads(manifest.read_text())
        data['schema'] = bp.SCHEMA - 1
        manifest.write_text(json.dumps(data))
        self.assertEqual(bp.plan(self.root, self.cache)['changed'], self.books)
        data['schema'] = bp.SCHEMA
        manifest.write_text(json.dumps(data))
        (self.cache / 'dist/kdp/tome1-integers-print-metadata.json').unlink()
        self.assertEqual(bp.plan(self.root, self.cache)['changed'], ['tome1-integers'])

    def test_overlay_preserves_unchanged_and_drops_stale_chapters(self):
        self.write('tome0-basics/main.tex', 'changed')
        stale = self.cache / 'dist/html/tome0-basics/deleted-chapter.html'
        stale.write_text('stale')
        retired = ['dist/tome1-integers-kindle.pdf', 'dist/tome1-integers-a4.pdf',
                   'dist/tome1-integers-phone.pdf']
        for path in retired:
            (self.cache / path).write_bytes(b'old variant')
        data = bp.plan(self.root, self.cache)
        bp.prepare(self.root, self.cache, data)
        self.assertTrue((self.root / 'dist/tome1-integers.pdf').exists())
        self.assertFalse((self.root / 'dist/html/tome0-basics').exists())
        for path in retired:
            self.assertFalse((self.root / path).exists())
        for book in data['changed']:
            self.outputs(self.root, book)
        bp.snapshot(self.root, self.cache, data)
        self.assertEqual(bp.plan(self.root, self.cache)['changed'], [])
        self.assertFalse(stale.exists())
        self.assertEqual(self.pdf_check.call_count, 2 * len(self.books))
        self.assertEqual(self.pair_check.call_count, len(self.books))

    def test_retired_pdf_cannot_enter_snapshot(self):
        data = bp.plan(self.root, self.cache)
        bp.prepare(self.root, self.cache, data)
        self.write('dist/tome0-basics-kindle.pdf', 'stale')
        with self.assertRaisesRegex(ValueError, 'Retired PDF'):
            bp.snapshot(self.root, self.cache, data)

    def test_a4_pdf_with_canonical_filename_cannot_enter_snapshot(self):
        data = bp.plan(self.root, self.cache)
        bp.prepare(self.root, self.cache, data)
        self.pdf_check.side_effect = ValueError('page 1 is not the approved paperback trim')
        with self.assertRaisesRegex(ValueError, 'page 1'):
            bp.snapshot(self.root, self.cache, data)

    def test_metadata_must_match_the_standard_pdf(self):
        data = bp.plan(self.root, self.cache)
        bp.prepare(self.root, self.cache, data)
        self.write('dist/kdp/tome0-basics-print-metadata.json', json.dumps(bp.specification(234)))
        with self.assertRaisesRegex(ValueError, 'metadata disagree'):
            bp.snapshot(self.root, self.cache, data)

    def test_coverless_or_mismatched_download_cannot_enter_snapshot(self):
        data = bp.plan(self.root, self.cache)
        bp.prepare(self.root, self.cache, data)
        self.pair_check.side_effect = ValueError('Download must contain one front cover')
        with self.assertRaisesRegex(ValueError, 'front cover'):
            bp.snapshot(self.root, self.cache, data)

    def test_schema_migration_also_removes_deleted_books(self):
        subprocess.run(['git', 'rm', '-qrf', 'tome1-integers'], cwd=self.root, check=True)
        manifest = self.cache / 'manifest.json'
        old = json.loads(manifest.read_text())
        old['schema'] = bp.SCHEMA - 1
        manifest.write_text(json.dumps(old))
        data = bp.plan(self.root, self.cache)
        self.assertEqual(data['removed'], ['tome1-integers'])
        self.assertEqual(data['changed'], ['tome0-basics', 'tome9-higher-structures'])
        bp.prepare(self.root, self.cache, data)
        self.assertFalse((self.root / 'dist/tome1-integers.pdf').exists())

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
