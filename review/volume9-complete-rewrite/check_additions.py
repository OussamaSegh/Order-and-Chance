#!/usr/bin/env python3
"""Audit source additions and unchanged original blocks; this does not check proofs."""
import json
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ENV = r'theorem|proposition|lemma|corollary|definition|example'


def blocks(text, kind):
    return re.findall(r'\\begin\{' + kind + r'\}.*?\\end\{' + kind + r'\}', text, re.S)


def label(block):
    match = re.search(r'\\label\{([^}]+)\}', block)
    return match.group(1) if match else None


def main():
    baseline = json.loads((HERE / 'starting-source.json').read_text())
    errors, units, all_labels = [], [], []
    old_labels = {name for unit in baseline['printed_units'] for name in unit['labels']}
    for unit in baseline['printed_units']:
        path = unit['path']
        old = subprocess.check_output(['git', 'show', baseline['starting_sha'] + ':' + path], cwd=ROOT, text=True)
        new = (ROOT / path).read_text()
        old_ex, new_ex = blocks(old, 'exercise'), blocks(new, 'exercise')
        old_labs, new_labs = list(map(label, old_ex)), list(map(label, new_ex))
        if new_labs[:len(old_labs)] != old_labs:
            errors.append(path + ': original exercises changed order or label')
        added = new_ex[len(old_ex):]
        if len(added) != 4:
            errors.append(path + ': expected four appended exercises')
        for exercise in added:
            name = label(exercise)
            if not name or name in old_labels:
                errors.append(path + ': missing or reused new exercise label')
                continue
            if not re.match(r'\\begin\{exercise\}\[[^]]*\\star', exercise):
                errors.append(name + ': missing difficulty rating')
            hints = re.findall(r'\\begin\{hint\}\{' + re.escape(name) + r'\}(.*?)\\end\{hint\}', new, re.S)
            solutions = re.findall(r'\\begin\{solution\}\{' + re.escape(name) + r'\}(.*?)\\end\{solution\}', new, re.S)
            if len(hints) != 1 or len(hints[0].strip()) < 20:
                errors.append(name + ': expected one substantive hint')
            if len(solutions) != 1 or not all(x in solutions[0] for x in ('\\idea', '\\writeup')):
                errors.append(name + ': expected one idea/writeup solution')
        old_fig = blocks(old, 'figure')
        new_fig = blocks(new, 'figure')
        old_fig_labels = list(map(label, old_fig))
        if list(map(label, new_fig[:len(old_fig)])) != old_fig_labels:
            errors.append(path + ': original figure order changed')
        for original in old_fig:
            if original not in new:
                errors.append(path + ': original figure block changed: ' + str(label(original)))
        if len(new_fig) - len(old_fig) != 2:
            errors.append(path + ': expected two appended figure blocks')
        old_formal = re.findall(r'\\begin\{(' + ENV + r')\}', old)
        new_formal = re.findall(r'\\begin\{(' + ENV + r')\}', new)
        if old_formal != new_formal:
            errors.append(path + ': original formal-environment sequence changed')
        all_labels += re.findall(r'\\label\{([^}]+)\}', new)
        units.append({'path': path, 'original_formal_statements': len(old_formal), 'original_exercises': len(old_ex),
                      'added_exercises': len(added), 'added_figures': len(new_fig) - len(old_fig)})
    duplicates = sorted({x for x in all_labels if all_labels.count(x) > 1})
    if duplicates:
        errors.append('duplicate labels: ' + ', '.join(duplicates))
    for error in errors:
        print('FAIL', error)
    if errors:
        return 1
    print(json.dumps({'units': units, 'totals': {k: sum(u[k] for u in units) for k in
          ('original_formal_statements', 'original_exercises', 'added_exercises', 'added_figures')},
          'checks': 'Original figure blocks exact; formal kinds/order exact; original exercises first; unique labels; new difficulty/hint/idea/writeup present.'}, indent=2))
    print('This is a source audit, not mathematical or editorial verification.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
