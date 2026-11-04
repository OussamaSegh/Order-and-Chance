"""Reject unreviewed forward references; classifications are manual, not proofs."""

import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from tools.volume2_review_inventory import inventory

REVIEW = ROOT/'docs/reviews/volume2-forward-reference-review-2026-11-04.json'


def forward_references(data):
    order = {f['path']: i for i, f in enumerate(data['source_files'])}
    sources, result = {}, []
    for edge in data['reference_edges']:
        destination = edge['destination']
        if (order[edge['path']], edge['line']) >= (order[destination['path']], destination['line']):
            continue
        if edge['path'] not in sources:
            sources[edge['path']] = (ROOT/edge['path']).read_text().splitlines()
        context = sources[edge['path']][edge['line']-1].strip()
        result.append({'path': edge['path'], 'line': edge['line'], 'target': edge['target'],
                       'context_sha256': hashlib.sha256(context.encode()).hexdigest()})
    return result


def check(data=None, review=None):
    data = inventory() if data is None else data
    review = json.loads(REVIEW.read_text()) if review is None else review
    for source in review['toolkit_sources']:
        if hashlib.sha256((ROOT/source['path']).read_bytes()).hexdigest() != source['sha256']:
            raise ValueError('Volume1 toolkit source changed: rereview affected prerequisite sites')
    actual = forward_references(data)
    registered = []
    for row in review['edge_reviews']:
        if row.get('role') not in {'navigation', 'diagram', 'outlook', 'practice', 'alternate-proof'}:
            raise ValueError('A forward reference has no permitted, explicit role')
        if not row.get('reason', '').strip():
            raise ValueError('A forward reference has no manual explanation')
        registered.append({k: row[k] for k in ('path', 'line', 'target', 'context_sha256')})
    if actual != registered:
        raise ValueError('Forward-reference review is stale: manually review new/changed uses before updating it')
    return {'references': len(data['reference_edges']), 'reviewed_forward_uses': len(actual),
            'scope': 'Reference/context guard only; no automatic prerequisite or proof certification.'}


if __name__ == '__main__':
    print(json.dumps(check(), sort_keys=True))
