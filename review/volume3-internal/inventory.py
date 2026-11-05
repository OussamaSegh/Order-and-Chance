"""Index the complete Volume 3 review surface, without assigning proof status.

Run from any directory: python3 review/volume3-internal/inventory.py [--check]
The JSON contains source hashes, semantic blocks, all remaining prose chunks,
figure inputs, and local reference edges. It is an inventory, not a correctness
or dependency-order certificate. Review evidence belongs in the strict ledger.
"""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
BOOK = ROOT / 'volume3-symmetry'
DESTINATION = Path(__file__).with_name('inventory.json')
SEMANTIC = {
    'theorem', 'proposition', 'lemma', 'corollary', 'definition', 'example',
    'theoremx', 'propositionx', 'lemmax', 'corollaryx', 'definitionx', 'examplex',
    'tabular', 'tabularx', 'note', 'challenge', 'proof', 'exercise', 'hint', 'solution', 'reminder', 'think', 'beauty', 'figure', 'remark',
}
TOKEN = re.compile(r'\\(begin|end)\{('+'|'.join(sorted(SEMANTIC))+r')\}')
LABEL = re.compile(r'\\label\{([^}]+)\}')


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def uncomment(source):
    # Preserve offsets/line numbers, including escaped percent signs.
    return re.sub(r'(?<!\\)%[^\n]*', lambda m: ' '*len(m.group()), source)


def inventory():
    route = re.findall(r'\\input\{(chapters/[^}]+)\}', (BOOK / 'main.tex').read_text())
    route = ['main'] + route + ['about-the-cover', 'blurb', 'kdp.md']
    files, items, edges, figures, portraits, targets = [], [], [], [], [], {}
    chapter = 0
    for stem in route:
        path = BOOK / (stem if stem.endswith('.md') else stem+'.tex')
        raw = path.read_text()
        source = uncomment(raw)
        if re.search(r'\\chapter\{', source):
            chapter += 1
        position = chapter if re.match(r'ch\d', path.stem) else path.stem
        relative = str(path.relative_to(ROOT))
        files.append({'path': relative, 'chapter': position, 'sha256': digest(raw),
                      'lines': len(raw.splitlines())})
        line = lambda offset: source.count('\n', 0, offset)+1
        stack, spans = [], []
        for token in TOKEN.finditer(source):
            operation, kind = token.groups()
            if operation == 'begin':
                stack.append((kind, token.start(), token.end()))
            else:
                if not stack or stack[-1][0] != kind:
                    raise ValueError(f'Unbalanced semantic block: {relative}:{line(token.start())}')
                _, start, content_start = stack.pop()
                spans.append((start, token.end(), kind, content_start))
        if stack:
            raise ValueError(f'Unclosed semantic block: {relative}')
        spans.sort()
        ordinals = Counter()
        for start, end, kind, content_start in spans:
            ordinals[kind] += 1
            body = source[content_start:end]
            labels = LABEL.findall(body)
            # Hint/solution keys are positional arguments, not label commands.
            key = re.match(r'\{([^}]+)\}', body) if kind in ('hint', 'solution') else None
            label = key.group(1) if key else (labels[0] if labels else None)
            identifier = f'{position}.{kind}.{label or ordinals[kind]}'
            items.append({'id': identifier, 'path': relative, 'line': line(start),
                          'end_line': line(end), 'kind': kind, 'key': label,
                          'sha256': digest(raw[start:end]),
                          'preview': ' '.join(body.split())[:180]})
        # Bibliography items need their own stable identities, even where an
        # entire itemize list is one prose paragraph in the TeX source.
        bibliography = re.search(r'\\section\*\{Sources and further reading\}', source)
        if bibliography:
            tail = source[bibliography.end():]
            for number, match in enumerate(re.finditer(
                    r'\\item\s+([\s\S]*?)(?=\\item|\\end\{itemize\})', tail), 1):
                a = bibliography.end()+match.start()
                b = bibliography.end()+match.end()
                # End coordinates are inclusive source lines: trailing whitespace
                # must not make one item claim the next item's first line.
                while b > a and source[b-1].isspace():
                    b -= 1
                normalized = ' '.join(source[a:b].split())
                items.append({'id': f'{position}.bibliography.{number}', 'path': relative,
                              'line': line(a), 'end_line': line(b), 'kind': 'bibliography',
                              'key': None, 'sha256': digest(raw[a:b]), 'preview': normalized[:180]})
        # Every nonempty gap outside semantic blocks is retained. This includes
        # epigraph/history, definitions made in prose, displays and transitions.
        occupied = [(a, b) for a, b, _, _ in spans]
        cursor, gaps = 0, []
        for start, end in occupied:
            if start > cursor:
                gaps.append((cursor, start))
            cursor = max(cursor, end)
        gaps.append((cursor, len(source)))
        occurrences = Counter()
        for start, end in gaps:
            for match in re.finditer(r'\S(?:[^\n]|\n(?!\s*\n))*', source[start:end]):
                a, b = start+match.start(), start+match.end()
                body = raw[a:b]
                normalized = ' '.join(source[a:b].split())
                h = digest(normalized)[:16]
                occurrences[h] += 1
                items.append({'id': f'{position}.prose.{h}.{occurrences[h]}', 'path': relative,
                              'line': line(a), 'end_line': line(b), 'kind': 'prose',
                              'key': None, 'sha256': digest(body), 'preview': normalized[:180]})
        for match in LABEL.finditer(source):
            key = match.group(1)
            if key in targets:
                raise ValueError(f'Duplicate label: {key}')
            targets[key] = {'path': relative, 'line': line(match.start()), 'chapter': position}
        for match in re.finditer(r'\\(?:ref|eqref|autoref|pageref)\{([^}]+)\}', source):
            edges.append({'path': relative, 'line': line(match.start()), 'target': match.group(1)})
        for match in re.finditer(r'\\fig\{([^}]+)\}', source):
            figure_path = BOOK / 'figures' / (match.group(1)+'.tex')
            figures.append({'key': match.group(1), 'use_path': relative,
                            'use_line': line(match.start()), 'path': str(figure_path.relative_to(ROOT)),
                            'sha256': digest(figure_path.read_text())})
        for match in re.finditer(r'\\portrait\{([^}]+)\}\{((?:[^{}]|\{[^{}]*\})*)\}', source):
            image_path = BOOK / 'photos' / (match.group(1)+'.jpg')
            portraits.append({'key': match.group(1), 'use_path': relative,
                              'use_line': line(match.start()), 'credit': match.group(2),
                              'path': str(image_path.relative_to(ROOT)),
                              'sha256': hashlib.sha256(image_path.read_bytes()).hexdigest()})
    route_index = {f['path']: i for i, f in enumerate(files)}
    items.sort(key=lambda item: (route_index[item['path']], item['line'], item['end_line']))
    for edge in edges:
        edge['destination'] = targets.get(edge['target'])
        if edge['destination'] is None:
            raise ValueError(f"Unresolved target: {edge['target']}")
    supporting = ['volume3-symmetry/main.tex', 'volume3-symmetry/kdp.md',
                  'common/cover-notes.json', 'common/series-catalog.json']
    return {'schema': 1, 'baseline': '7f87c2ab00fdb0c7791dc833423b98bef0870f01', 'scope': 'Inventory only; no generated verification statuses. Synthetic IDs are file/semantic ordinal or normalized-content SHA prefixes; edits invalidate hashes and require manual reconciliation. Prose blocks cover unlabelled arguments as well as transitions; their mathematical roles require manual review.',
            'supporting_sources': [{'path': p, 'sha256': digest((ROOT / p).read_text())}
                                   for p in supporting],
            'source_files': files, 'counts': dict(sorted(Counter(i['kind'] for i in items).items())),
            'items': items, 'figure_inputs': figures, 'historical_images': portraits,
            'reference_edges': edges}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Reject a stale checked-in inventory')
    args = parser.parse_args()
    data = inventory()
    rendered = json.dumps(data, ensure_ascii=False, indent=2)+'\n'
    if args.check:
        if not DESTINATION.exists() or DESTINATION.read_text() != rendered:
            raise SystemExit('Volume 3 review inventory is stale; regenerate and review affected items.')
    else:
        DESTINATION.write_text(rendered)
    print(json.dumps({'files': len(data['source_files']), 'items': len(data['items']),
                      'figures': len(data['figure_inputs']), 'counts': data['counts']}, sort_keys=True))


if __name__ == '__main__':
    main()
