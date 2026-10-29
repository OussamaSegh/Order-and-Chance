"""Finite regression aids for Batch C; these do not certify universal proofs."""
from pathlib import Path
from collections import Counter
from itertools import combinations, product
from math import comb
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
DRAFT = ROOT/'volume0-mathematical-maturity/chapters'
SOURCE = DRAFT
files = ['ch01-sums.tex', 'ch02-counting.tex', 'ch09-probability.tex']
new = '\n'.join((DRAFT / f).read_text() for f in files)
import json
units=json.loads((Path(__file__).parent/'baseline-inventory.json').read_text())['units']
selected=[u for u in units if Path(u['file']).name in ['ch01-sums.tex','ch08-counting-probability.tex']]
old=''.join('\\label{'+l+'}' for u in selected for l in u['labels'])
old_ex=Counter(l for u in selected if u['kind']=='exercise' for l in u['labels'])

def labels(s):
    return Counter(re.findall(r'\\label\{([^}]+)\}', s))

def exercises(s):
    return Counter(re.findall(r'\\begin\{exercise\}(?:\[[^]]*\])?\\label\{([^}]+)\}', s))

assert not labels(old) - labels(new)
assert all(n == 1 for n in labels(new).values())
assert not old_ex - exercises(new)
for filename in files:
    s = (DRAFT / filename).read_text()
    hints = Counter(re.findall(r'\\begin\{hint\}\{([^}]+)\}', s))
    solutions = Counter(re.findall(r'\\begin\{solution\}\{([^}]+)\}', s))
    assert exercises(s) == hints == solutions
    print(filename, len(exercises(s)), 'complete exercise triples')
print(len(labels(old)), 'original explicit labels retained exactly once')

assert sum(a + b + c == 6 for a, b, c in product((0, 2, 4), (0, 1, 2, 3), (0, 3))) == 3
v = [1, 1, 1]
for n in range(3, 20):
    v.append(v[n - 1] + v[n - 3])
assert v[6] == 6
checks = 1
for n in range(3, 13):
    for k in range(n + 1):
        actual = sum(all((a + 1) % n not in S for a in S) for S in combinations(range(n), k))
        if k == 0:
            expected = 1
        elif 2 * k > n:
            expected = 0
        else:
            expected = comb(n - k, k) + comb(n - k - 1, k - 1)
        assert actual == expected, (n, k, actual, expected)
        checks += 1
print(checks, 'enumeration/recurrence checks passed; coefficient example also passed')
