"""Check manual conceptual/earlier-source evidence freshness; never approve it."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

from inventory import ROOT, inventory, uncomment

HERE = Path(__file__).resolve().parent
CHAIN = ('first_appearance', 'definition', 'example', 'proof',
         'earliest_valid_invocation', 'earlier_tools_and_proof_sites')
LATER = ('later_use_locations', 'later_use_reconstruction',
         'adversarial_later_check', 'later_use_boundaries', 'whole_volume_scope')


def conceptual_snapshot(data=None):
    """Hash the actual review surface, without making any review decision."""
    data = inventory() if data is None else data
    paths = {row['path'] for key in ('source_files', 'figure_inputs',
                                    'historical_images', 'supporting_sources')
             for row in data[key]}
    paths.update(str(p.relative_to(ROOT)) for p in (ROOT / 'common').glob('*.tex'))
    paths.update(('common/volume-subtitles.json', 'common/print-layout.json'))
    for name in ('prerequisite-sources', 'seam-sources'):
        paths.update(row['path'] for row in
                     json.loads((HERE / f'{name}.json').read_text())['sources'])
    sources = [{'path': path,
                'sha256': hashlib.sha256((ROOT / path).read_bytes()).hexdigest()}
               for path in sorted(paths)]
    encoded = json.dumps(sources, sort_keys=True, separators=(',', ':')).encode()
    return {'sources': sources, 'sha256': hashlib.sha256(encoded).hexdigest()}


def earlier_occurrences(data):
    """Literal singular V1/2 mentions only; concepts also need manual review."""
    rows = []
    for source in data['source_files']:
        path = source['path']
        raw = (ROOT / path).read_text()
        clean = uncomment(raw)
        counts = Counter()
        for match in re.finditer(r'Volume[~ ]+([12])(?!\d)', clean):
            volume = int(match.group(1))
            counts[volume] += 1
            line = clean.count('\n', 0, match.start()) + 1
            context = raw.splitlines()[line-1]
            rows.append(dict(id=f'{path}::V{volume}::{counts[volume]}',
                             path=path, line=line, volume=volume,
                             ordinal=counts[volume], context=context,
                             context_sha256=hashlib.sha256(context.encode()).hexdigest()))
    return rows


def reconcile_earlier(data=None):
    """Preserve identical manual contexts; new/changed mentions stay pending."""
    data = inventory() if data is None else data
    dest = HERE / 'earlier-references.json'
    document = json.loads(dest.read_text())
    old = {r['id']: r for r in document['entries']}
    rows = []
    for fresh in earlier_occurrences(data):
        prior = old.pop(fresh['id'], None)
        if prior and prior['context_sha256'] == fresh['context_sha256']:
            rows.append({**prior, **fresh})
        else:
            rows.append({**fresh, 'role': 'unclassified',
                         'actual_earlier_proof_sites': '',
                         'reconstruction_and_availability': '', 'status': 'pending'})
    if any(r['status'] != 'pending' for r in old.values()):
        raise ValueError('Do not silently remove/rekey accepted earlier-source evidence')
    document['entries'] = rows
    dest.write_text(json.dumps(document, ensure_ascii=False, indent=2)+'\n')


def check(data=None, require_complete=False, documents=None):
    data = inventory() if data is None else data
    documents = {} if documents is None else documents
    read = lambda name: documents.get(name) or json.loads((HERE / f'{name}.json').read_text())
    earlier = read('earlier-references')['entries']
    fields = ('id', 'path', 'line', 'volume', 'ordinal', 'context', 'context_sha256')
    identity = lambda row: {k: row[k] for k in fields}
    if [identity(r) for r in earlier] != earlier_occurrences(data):
        raise ValueError('Earlier-volume occurrence/context evidence is stale; reopen affected uses')
    for row in earlier:
        if row['status'] == 'accepted-internal':
            if (row.get('role') in ('', 'unclassified', None) or
                    any(not row.get(k, '').strip() for k in
                        ('actual_earlier_proof_sites', 'reconstruction_and_availability'))):
                raise ValueError(f"Incomplete earlier-source reconstruction: {row['id']}")
        elif require_complete:
            raise ValueError(f"Earlier-source review incomplete: {row['id']}")

    concepts = read('concepts')
    current = {r['id']: r for r in data['items']}
    seen = set()
    for row in concepts['entries']:
        if row['id'] in seen:
            raise ValueError(f"Duplicate conceptual ID: {row['id']}")
        seen.add(row['id'])
        if row['first_use_status'] == 'reviewed-internal':
            if any(not row.get(k, '').strip() for k in CHAIN) or not row.get('anchors'):
                raise ValueError(f"Incomplete conceptual chain: {row['id']}")
        for anchor in row.get('anchors', []):
            actual = current.get(anchor['id'])
            if not actual or any(anchor[k] != actual[k] for k in
                                 ('path', 'line', 'end_line', 'sha256')):
                raise ValueError(f"Stale conceptual anchor: {row['id']} / {anchor['id']}")
        if (row['status'] == 'accepted-internal' or
                row['later_use_status'] == 'reviewed-internal'):
            if (row['first_use_status'] != 'reviewed-internal' or
                    any(not isinstance(row.get(k), str) or not row[k].strip()
                        for k in LATER)):
                raise ValueError(f"Incomplete substantive later-use review: {row['id']}")
            snapshot = concepts.get('reviewed_snapshot')
            if (not snapshot or row.get('reviewed_snapshot_sha256') != snapshot['sha256']
                    or snapshot != conceptual_snapshot(data)):
                raise ValueError(f"Whole-volume conceptual source/figure drift: {row['id']}")
        if require_complete and (row['status'] != 'accepted-internal' or
                                 row['first_use_status'] != 'reviewed-internal' or
                                 row['later_use_status'] != 'reviewed-internal'):
            raise ValueError(f"Whole-volume conceptual review incomplete: {row['id']}")
    if require_complete and concepts['coverage_status'] != 'complete-manual-whole-volume':
        raise ValueError('Manual whole-volume conceptual coverage remains incomplete')
    for source in read('seam-sources')['sources']:
        if hashlib.sha256((ROOT / source['path']).read_bytes()).hexdigest() != source['sha256']:
            raise ValueError(f"Seam source drift; reread the actual boundary: {source['path']}")
    return {'earlier_occurrences': dict(Counter(r['status'] for r in earlier)),
            'conceptual_first_uses': dict(Counter(r['first_use_status'] for r in concepts['entries'])),
            'conceptual_whole_volume': dict(Counter(r['status'] for r in concepts['entries']))}


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--require-complete', action='store_true')
    parser.add_argument('--reconcile-earlier', action='store_true')
    args = parser.parse_args()
    if args.reconcile_earlier:
        reconcile_earlier()
    print(json.dumps(check(require_complete=args.require_complete), sort_keys=True))
