import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import release_assets


class ReleaseAssetsTest(unittest.TestCase):
    def test_upload_and_restore_spaced_filename(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'Volume 0 - Mathematical Maturity.pdf'
            path.write_bytes(b'pdf')
            asset = {'id': 2, 'name': path.name.replace(' ', '.'), 'label': path.name, 'size': 3}
            restored = dict(asset, name=path.name)
            with patch.object(release_assets, 'gh', side_effect=[
                '', json.dumps({'id': 1}), json.dumps([[asset]]), json.dumps(restored)
            ]) as gh:
                release_assets.upload('owner/repo', 'books', directory)
            self.assertIn(f'{path}#{path.name}', gh.call_args_list[0].args)
            self.assertIn(f'name={path.name}', gh.call_args_list[-1].args)

    def test_filename_mismatch_stops_publication(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'Volume 0 - Mathematical Maturity.pdf'
            path.write_bytes(b'pdf')
            asset = {'id': 2, 'name': 'wrong.pdf', 'label': path.name, 'size': 3}
            with patch.object(release_assets, 'gh', side_effect=[
                '', json.dumps({'id': 1}), json.dumps([[asset]]), json.dumps(asset)
            ]), self.assertRaisesRegex(ValueError, 'filename/size mismatch'):
                release_assets.upload('owner/repo', 'books', directory)
