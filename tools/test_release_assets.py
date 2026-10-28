import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import release_assets


class ReleaseAssetsTest(unittest.TestCase):
    def test_content_digest_and_size_must_match(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'Volume 0 - Mathematical Maturity.pdf'
            path.write_bytes(b'pdf')
            asset = {'id': 2, 'name': path.name.replace(' ', '.'),
                     'label': path.name, 'size': 3, 'state': 'uploaded',
                     'digest': 'sha256:' + hashlib.sha256(b'pdf').hexdigest()}
            for changes, error in [({}, None), ({'size': 4}, 'filename/size'),
                                   ({'digest': 'sha256:wrong'}, 'content digest')]:
                with self.subTest(changes=changes), patch.object(release_assets, 'gh', side_effect=[
                    '', json.dumps({'id': 1}), json.dumps([[dict(asset, **changes)]])
                ]):
                    if error:
                        with self.assertRaisesRegex(ValueError, error):
                            release_assets.upload('owner/repo', 'books', directory)
                    else:
                        release_assets.upload('owner/repo', 'books', directory)

    def test_upload_accepts_github_normalization_with_readable_label(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'Volume 0 - Mathematical Maturity.pdf'
            path.write_bytes(b'pdf')
            asset = {'id': 2, 'name': path.name.replace(' ', '.'), 'label': path.name, 'size': 3}
            with patch.object(release_assets, 'gh', side_effect=[
                '', json.dumps({'id': 1}), json.dumps([[asset]])
            ]) as gh:
                release_assets.upload('owner/repo', 'books', directory)
            self.assertIn(f'{path}#{path.name}', gh.call_args_list[0].args)
            self.assertEqual(gh.call_count,3)

    def test_filename_mismatch_stops_publication(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'Volume 0 - Mathematical Maturity.pdf'
            path.write_bytes(b'pdf')
            asset = {'id': 2, 'name': 'wrong.pdf', 'label': path.name, 'size': 3}
            with patch.object(release_assets, 'gh', side_effect=[
                '', json.dumps({'id': 1}), json.dumps([[asset]])
            ]), self.assertRaisesRegex(ValueError, 'filename/size mismatch'):
                release_assets.upload('owner/repo', 'books', directory)
