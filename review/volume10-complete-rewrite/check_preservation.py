#!/usr/bin/env python3
"""Compare a completed Volume 10 build with the immutable starting inventory.

This checks preservation, not mathematical correctness or prose coverage.
Run after building: python3 review/volume10-complete-rewrite/check_preservation.py
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



def numbered_contents(path):
    """Return every printed part/chapter/section number, ignoring changed pages."""
    result = []
    text = path.read_text()
    for match in re.finditer(r"\\contentsline\s*\{", text):
        kind, pos = group(text, match.end() - 1)
        while text[pos].isspace():
            pos += 1
        title, _ = group(text, pos)
        number = re.match(r"\\numberline\s*\{", title)
        if number:
            value, _ = group(title, number.end() - 1)
            result.append((kind, value))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-additions", action="store_true")
    args = parser.parse_args()
    baseline = json.loads((HERE / "starting-source.json").read_text())
    original_labels = json.loads((HERE / "starting-printed-labels.json").read_text())
    current = labels_from_aux(ROOT / "build/volume10-abstraction/main.aux")
    errors = []
    for name, original in original_labels.items():
        if name not in current:
            errors.append(f"Missing original label: {name}")
            continue
        if current[name]["number"] != original["number"]:
            errors.append(f"Number changed for {name}: {original['number']} -> {current[name]['number']}")
        if original["anchor"].startswith("figure.") and current[name]["title"] != original["title"]:
            errors.append(f"Original figure caption changed: {name}")
    original_contents = numbered_contents(HERE / "starting-contents.tex")
    current_contents = numbered_contents(ROOT / "build/volume10-abstraction/main.toc")
    if current_contents != original_contents:
        errors.append("Printed part/chapter/section numbering or order changed")
    for unit in baseline["printed_units"]:
        text = (ROOT / unit["path"]).read_text()
        for block in unit["original_figure_blocks"]:
            if block not in text:
                errors.append(f"Original figure block changed: {unit['path']}")
    for name, digest in baseline["protected_shared_art_sha256"].items():
        if hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != digest:
            errors.append(f"Protected shared artwork changed: {name}")
    figures = 0
    artwork = 0
    for name, digest in baseline["tracked_file_sha256"].items():
        if "/figures/" in name:
            figures += 1
        elif name.endswith(("/cover-motif.tex", "/cover-lettering.tex")):
            artwork += 1
        else:
            continue
        path = ROOT / name
        if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            errors.append(f"Original figure or cover artwork file changed: {name}")
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
    print(f"Preserved {len(original_contents)} printed part/chapter/section numbers in order and {artwork} cover artwork files.")
    print("Mathematics, prose, unlabelled statements and visual placement require separate review.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
