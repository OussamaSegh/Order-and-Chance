"""Audit Volume 11 source preservation against the immutable pre-rewrite commit.

Run from any working directory:
    python3 review/volume11-complete-rewrite/check_preservation.py
    python3 review/volume11-complete-rewrite/check_preservation.py --final

This is a structural guard, not a mathematical proof or typesetting review.
"""
import argparse
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = "b005c4a0a33409f443594f3bb1efe3e955e95468"
VOL = "volume11-randomness/"
STATEMENTS = re.compile(
    r"\\begin\{(theorem|lemma|proposition|corollary|definition|example|exercise|problem|theoremx|lemmax|propositionx|corollaryx|definitionx|examplex)\}"
    r"[\s\S]*?\\end\{\1\}"
)
LABEL = re.compile(r"\\label\{([^}]+)\}")
FIGURE = re.compile(r"\\begin\{figure\}[\s\S]*?\\end\{figure\}")
INPUT = re.compile(r"\\input\{(chapters/[^}]+)\}")
EXERCISES = {"exercise", "problem"}

def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)

def original(path):
    return git("show", f"{BASE}:{path}").decode("utf-8")

def current(path):
    return (ROOT / path).read_text(encoding="utf-8")

def keys(text):
    result = []
    for m in STATEMENTS.finditer(text):
        label = LABEL.search(m.group())
        result.append((m.group(1), label.group(1) if label else None))
    return result

def subsequence(old, new):
    remaining = iter(new)
    return all(any(a == b for b in remaining) for a in old)

def chapter_inputs(text):
    return [VOL + p + ".tex" for p in INPUT.findall(text) if p != "chapters/preface"]

def keyed_blocks(text, kind):
    return re.findall(r"\\begin\{" + kind + r"\}\{([^}]+)\}", text)

def audit():
    parser = argparse.ArgumentParser()
    parser.add_argument("--final", action="store_true", help="require exactly 2 figures and 4 exercises per chapter")
    args = parser.parse_args()
    main = VOL + "main.tex"
    old_order = chapter_inputs(original(main))
    errors = []
    if chapter_inputs(current(main)) != old_order or len(old_order) != 14:
        errors.append("printed chapter order changed")
    # The riffle section is part of Chapter 13, not an extra printed chapter.
    units = {path: [path] for path in old_order}
    shuffle = VOL + "chapters/shuffling.tex"
    riffle = VOL + "chapters/riffle-cutoff.tex"
    units[shuffle].append(riffle)
    if r"\input{chapters/riffle-cutoff}" not in current(shuffle):
        errors.append("Chapter 13 lost its riffle include")
    totals = [0, 0]
    baseline = [0, 0, 0]
    all_labels = set()
    for index, (chapter, files) in enumerate(units.items(), 1):
        additions = [0, 0]
        for path in files:
            old, new = original(path), current(path)
            old_labels, new_labels = LABEL.findall(old), LABEL.findall(new)
            if not subsequence(old_labels, new_labels):
                errors.append(f"{path}: original labels lost or reordered")
            for label in new_labels:
                if label in all_labels:
                    errors.append(f"{path}: duplicate label {label}")
                all_labels.add(label)
            old_keys, new_keys = keys(old), keys(new)
            old_formal = [x for x in old_keys if x[0] not in EXERCISES]
            new_formal = [x for x in new_keys if x[0] not in EXERCISES]
            if new_formal != old_formal:
                errors.append(f"{path}: original formal statement inventory changed")
            old_ex = [x for x in old_keys if x[0] in EXERCISES]
            new_ex = [x for x in new_keys if x[0] in EXERCISES]
            if new_ex[:len(old_ex)] != old_ex:
                errors.append(f"{path}: original exercises lost or reordered")
            added_ex = new_ex[len(old_ex):]
            old_fig, new_fig = FIGURE.findall(old), FIGURE.findall(new)
            if new_fig[:len(old_fig)] != old_fig:
                errors.append(f"{path}: original figure blocks altered or reordered")
            # Preserve the number of numbered sections/equations; their prose may change.
            for pattern in (r"\\section\{", r"\\subsection\{", r"\\begin\{equation\}"):
                if len(re.findall(pattern, old)) != len(re.findall(pattern, new)):
                    errors.append(f"{path}: numbered structural count changed: {pattern}")
            for kind in ("hint", "solution"):
                old_h, new_h = keyed_blocks(old, kind), keyed_blocks(new, kind)
                if not subsequence(old_h, new_h):
                    errors.append(f"{path}: original {kind} keys lost or reordered")
                for _, label in added_ex:
                    if label is None or new_h.count(label) != 1:
                        errors.append(f"{path}: new exercise {label} needs exactly one {kind}")
            baseline[0] += len(old_formal)
            baseline[1] += len(old_ex)
            baseline[2] += len(old_fig)
            additions[0] += len(new_fig) - len(old_fig)
            additions[1] += len(added_ex)
        if args.final and additions != [2, 4]:
            errors.append(f"Chapter {index}: expected +2 figures/+4 exercises, got {additions}")
        totals = [a+b for a,b in zip(totals, additions)]
        print(f"Chapter {index:02d}: +{additions[0]} figures, +{additions[1]} exercises")
    # Check every original figure source, including unprinted assets.
    old_figures = git("ls-tree", "-r", "--name-only", BASE, "--", VOL + "figures/").decode().splitlines()
    for path in old_figures:
        if not (ROOT / path).is_file() or (ROOT / path).read_bytes() != git("show", f"{BASE}:{path}"):
            errors.append(f"{path}: original artwork changed")
    print(f"Baseline: {baseline[0]} formal blocks, {baseline[1]} exercises, {baseline[2]} printed figure blocks")
    print(f"Additions: {totals[0]} figures, {totals[1]} exercises")
    if errors:
        raise SystemExit("\n".join(errors))
    print("Source preservation PASS (not mathematical or build acceptance)")

if __name__ == "__main__":
    audit()
