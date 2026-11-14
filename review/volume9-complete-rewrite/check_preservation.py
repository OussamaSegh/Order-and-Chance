#!/usr/bin/env python3
"""Compare a completed Volume 9 build with the immutable starting inventory.

This checks preservation, not mathematical correctness or prose coverage.
Run after building: python3 review/volume9-complete-rewrite/check_preservation.py
Add --require-additions when all units have their new figures and exercises.
"""

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def group(text, start):
    """Read a balanced TeX group, allowing nested and escaped braces."""
    if start >= len(text) or text[start] != "{":
        raise ValueError(f"Expected a TeX group at {start}")
    depth = 0
    for i in range(start, len(text)):
        if text[i] not in "{}":
            continue
        j = i - 1
        while j >= 0 and text[j] == "\\":
            j -= 1
        if (i - 1 - j) % 2:
            continue
        depth += 1 if text[i] == "{" else -1
        if depth == 0:
            return text[start + 1:i], i + 1
    raise ValueError("Unclosed TeX group")


def labels_from_aux(path):
    text = path.read_text()
    labels = {}
    for match in re.finditer(r"\\newlabel\{", text):
        name, pos = group(text, match.end() - 1)
        body, _ = group(text, pos)
        values, pos = [], 0
        while pos < len(body):
            if body[pos].isspace():
                pos += 1
                continue
            value, pos = group(body, pos)
            values.append(value)
        if name in labels:
            raise ValueError(f"Duplicate label: {name}")
        labels[name] = dict(zip(("number", "page", "title", "anchor"), values[:4]))
    return labels


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-additions", action="store_true")
    args = parser.parse_args()
    baseline = json.loads((HERE / "starting-source.json").read_text())
    original_labels = json.loads((HERE / "starting-printed-labels.json").read_text())
    current = labels_from_aux(ROOT / "build/volume9-shapes/main.aux")
    errors = []
    for name, original in original_labels.items():
        if name not in current:
            errors.append(f"Missing original label: {name}")
            continue
        if current[name]["number"] != original["number"]:
            errors.append(f"Number changed for {name}: {original['number']} -> {current[name]['number']}")
        if original["anchor"].startswith("figure.") and current[name]["title"] != original["title"]:
            errors.append(f"Original figure caption changed: {name}")
    figures = 0
    for name, digest in baseline["tracked_file_sha256"].items():
        if "/figures/" not in name:
            continue
        figures += 1
        path = ROOT / name
        if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            errors.append(f"Original figure file changed: {name}")
    if args.require_additions:
        for unit in baseline["printed_units"]:
            text = (ROOT / unit["path"]).read_text()
            text = re.sub(r"(?m)(?<!\\)%.*$", "", text)
            for environment, key, required in (("figure", "figures", 2), ("exercise", "exercises", 4)):
                added = len(re.findall(r"\\begin\{" + environment + r"\}", text)) - unit[key]
                if added != required:
                    errors.append(f"{unit['path']}: {added} added {environment}s; expected {required}")
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        return 1
    print(f"Preserved {len(original_labels)} original printed labels, captions and {figures} figure files.")
    print("Mathematics, prose, unlabelled statements and visual placement require separate review.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
