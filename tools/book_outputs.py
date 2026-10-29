"""Remove retired PDF variants and prevent them from entering a release."""
import argparse
from pathlib import Path
from legacy_urls import OLD_PREFIX


RETIRED_SUFFIXES = ('-a4.pdf', '-kindle.pdf', '-phone.pdf')


def retired_pdfs(directory):
    directory = Path(directory)
    return sorted(p for folder in (directory, directory / 'kdp')
                  for p in folder.glob('*.pdf') if p.name.endswith(RETIRED_SUFFIXES))


def machine_files(directory):
    directory = Path(directory)
    found = []
    for folder in (directory, directory / "kdp"):
        if not folder.is_dir():
            continue
        for pattern in ("volume*", OLD_PREFIX + "*"):
            found.extend(p for p in folder.glob(pattern) if p.is_file())
    return found


def clean(directory):
    for path in [*retired_pdfs(directory), *machine_files(directory)]:
        path.unlink(missing_ok=True)


def check(directory):
    retired = retired_pdfs(directory)
    if retired:
        raise ValueError('Retired PDF editions in output: ' + ', '.join(map(str, retired)))
    legacy = machine_files(directory)
    if legacy:
        raise ValueError('Obsolete machine filenames in output: ' + ', '.join(map(str, legacy)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['clean', 'check'])
    parser.add_argument('directory', type=Path)
    args = parser.parse_args()
    {'clean': clean, 'check': check}[args.action](args.directory)
