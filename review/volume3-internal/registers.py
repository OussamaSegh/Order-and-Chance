"""Create pending registers or check evidence freshness; never approve an item.

Run with --initialize once; all subsequent entries and decisions are manual.
--require-complete is the final acceptance gate, not the inventory gate.
"""
import argparse
from collections import Counter
import json
from pathlib import Path
from inventory import inventory

HERE = Path(__file__).resolve().parent
NAMED = {'theorem', 'proposition', 'lemma', 'corollary'}
CORE = ('hypotheses_domain', 'claim', 'earlier_tools_and_proof_sites',
        'reconstruction_A', 'adversarial_check_B', 'boundary_probes',
        'defects_and_corrections', 'source_revision')


def basis(item):
    return {key: item[key] for key in ('id', 'path', 'line', 'end_line', 'kind', 'key', 'sha256')}


def initialize(data):
    groups = {'proofs': [], 'exercises': [], 'exposition': [], 'dependencies': []}
    for item in data['items']:
        row = basis(item)
        if item['kind'] in NAMED:
            row.update({key: '' for key in CORE})
            row['status'] = 'pending'
            proofs = [x for x in data['items'] if x['path'] == item['path']
                      and x['kind'] == 'proof' and x['line'] > item['end_line']]
            if not proofs:
                raise ValueError(f"Named result lacks a following proof: {item['id']}")
            row['related'] = [basis(proofs[0])]
            groups['proofs'].append(row)
        elif item['kind'] == 'exercise':
            row.update({key: '' for key in CORE})
            row.update({'independent_solution_before_comparison': '',
                        'hint_idea_writeup_comparison': '', 'star_assessment': '',
                        'status': 'pending'})
            related = [basis(x) for x in data['items']
                       if x['key'] == item['key'] and x['kind'] in ('hint', 'solution')]
            row['related'] = related
            groups['exercises'].append(row)
        elif item['kind'] not in ('proof', 'hint', 'solution'):
            row.update({'role': 'unclassified', 'reconstruction_A': '',
                        'adversarial_check_B': '', 'boundary_probes': '',
                        'earlier_tools_and_proof_sites': '',
                        'history_source_evidence': '', 'source_revision': '',
                        'defects_and_corrections': '', 'status': 'pending'})
            groups['exposition'].append(row)
    # Edges are occurrences, not only targets; duplicate references on a line
    # remain distinguishable by ordinal. Context hashes guard stale decisions.
    occurrences = Counter()
    root = HERE.parents[1]
    import hashlib
    for edge in data['reference_edges']:
        identity = (edge['path'], edge['target'])
        occurrences[identity] += 1
        context = (root / edge['path']).read_text().splitlines()[edge['line']-1]
        groups['dependencies'].append(dict(edge,
            id=f"{edge['path']}::{edge['target']}::{occurrences[identity]}",
            context_sha256=hashlib.sha256(context.encode()).hexdigest(),
            role='unclassified', reason='', status='pending'))
    for group, entries in groups.items():
        dest = HERE / f'{group}.json'
        if dest.exists():
            raise ValueError(f'Refusing to overwrite manual evidence: {dest}')
        dest.write_text(json.dumps({'scope': 'Pending internal AI review; generated inventory is not approval.',
                                    'entries': entries}, ensure_ascii=False, indent=2)+'\n')


def check(data, require_complete=False):
    current = {x['id']: x for x in data['items']}
    seen, statuses = set(), Counter()
    for group in ('proofs', 'exercises', 'exposition'):
        entries = json.loads((HERE / f'{group}.json').read_text())['entries']
        for row in entries:
            if row['id'] in seen:
                raise ValueError(f"Duplicate register ID: {row['id']}")
            seen.add(row['id'])
            item = current.get(row['id'])
            if not item or row['sha256'] != item['sha256']:
                raise ValueError(f"Stale/removed evidence; manually reopen {row['id']}")
            for related in row.get('related', []):
                actual = current.get(related['id'])
                if not actual or actual['sha256'] != related['sha256']:
                    raise ValueError(f"Changed hint/solution: {related['id']}")
            statuses[row['status']] += 1
            if row['status'] == 'accepted-internal':
                needed = CORE if group in ('proofs', 'exercises') else (
                    'role', 'reconstruction_A', 'adversarial_check_B', 'source_revision')
                if any(not row.get(k, '').strip() for k in needed):
                    raise ValueError(f"Incomplete substantive evidence: {row['id']}")
            elif require_complete:
                raise ValueError(f"Review incomplete: {row['id']} ({row['status']})")
    expected = {x['id'] for x in data['items'] if x['kind'] not in ('proof', 'hint', 'solution')}
    if expected != seen:
        raise ValueError(f'Exact register coverage differs: {expected ^ seen}')
    return dict(statuses)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--initialize', action='store_true')
    parser.add_argument('--require-complete', action='store_true')
    args = parser.parse_args()
    data = inventory()
    if args.initialize:
        initialize(data)
    print(json.dumps(check(data, args.require_complete), sort_keys=True))
