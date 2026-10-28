"""Upload release assets with readable labels and verify GitHub storage names."""
import argparse
import json
from pathlib import Path
import subprocess


def gh(*args):
    return subprocess.check_output(['gh', *args], text=True)


def upload(repository, tag, directory):
    directory = Path(directory)
    files = sorted([*directory.glob('*.pdf'), *directory.glob('*.epub'),
                    *(p for p in (directory / 'kdp').glob('*') if p.is_file())])
    if not files or len({p.name for p in files}) != len(files):
        raise ValueError('Release assets are empty or have duplicate filenames')
    # Labels let us identify uploads even if GitHub normalizes the initial name.
    for path in files:
        gh('release', 'upload', tag, f'{path}#{path.name}', '--repo', repository)
    release = json.loads(gh('api', f'repos/{repository}/releases/tags/{tag}'))
    assets = json.loads(gh('api', '--paginate', '--slurp',
                          f'repos/{repository}/releases/{release["id"]}/assets?per_page=100'))
    assets = [asset for page in assets for asset in page]
    for path in files:
        matches = [asset for asset in assets if asset.get('label') == path.name]
        if len(matches) != 1:
            raise ValueError(f'Cannot identify uploaded release asset: {path.name}')
        asset = matches[0]
        # GitHub normalizes spaces to dots on both upload and PATCH. Pages keeps
        # the literal filename; release labels retain the human-readable name.
        allowed_names = {path.name, path.name.replace(' ', '.')}
        if (asset['name'] not in allowed_names or asset['size'] != path.stat().st_size
                or asset.get('state', 'uploaded') != 'uploaded'):
            raise ValueError(f'Release filename/size mismatch: {path.name}')
        if asset.get('digest'):
            import hashlib
            expected = 'sha256:' + hashlib.sha256(path.read_bytes()).hexdigest()
            if asset['digest'] != expected:
                raise ValueError(f'Release content digest mismatch: {path.name}')



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('repository')
    parser.add_argument('tag')
    parser.add_argument('directory', type=Path)
    args = parser.parse_args()
    upload(args.repository, args.tag, args.directory)
