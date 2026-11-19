#!/usr/bin/env python3
"""Immutable source-preservation gate; no proof certification is implied."""
import argparse
import re
import subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
BASE = "60ce094742a84e3da028ad2c9d31d535db656344"
VOL = "volume14-primes"
CHAPTERS = [
    "ch01-zeros", "ch02-siegel", "ch03-sieves", "ch04-largesieve", "ch05-expsums",
    "waring", "three-primes", "ch08-gpy", "ch09-maynard", "ch10-halasz",
    "ch11-additive", "ch12-roth", "ch13-gowers", "ch14-critical",
]
OTHERS = [
    "volume1-first-principles", "volume2-integers", "volume3-symmetry", "volume4-chance",
    "volume5-calculation", "volume6-crossroads", "volume7-spaces", "volume8-analysis",
    "volume9-shapes", "volume10-abstraction", "volume11-randomness", "volume12-random-motion",
    "volume13-arithmetic", "volume15-order-and-chance",
]
ALLOWED = (
    "volume14-primes/",
    "review/volume14-complete-rewrite/",
    ".github/workflows/volume14-rewrite-audit.yml",
)
FORMAL = ("theorem", "proposition", "lemma", "corollary", "definition", "example",
          "theoremx", "propositionx", "lemmax", "corollaryx", "definitionx", "examplex")
STATEMENT = re.compile(r"\\begin\{(" + "|".join((*FORMAL, "exercise", "problem")) + r")\}(?:\[[^\]]*\])?[\s\S]*?\\end\{\1\}")
FIGURE = re.compile(r"\\begin\{figure\}(?:\[[^\]]*\])?[\s\S]*?\\end\{figure\}")
LABEL = re.compile(r"\\label\{([^}]+)\}")

def git(*args):
    return subprocess.check_output(("git", *args), cwd=ROOT)

def past(path):
    return git("show", BASE + ":" + path).decode()

def now(path):
    return (ROOT / path).read_text()

def is_subsequence(a, b):
    it = iter(b)
    return all(any(x == y for y in it) for x in a)

def blocks(s, kinds):
    return [m.group() for m in STATEMENT.finditer(s) if m.group(1) in kinds]

def allowed(path):
    return any(path == item.rstrip("/") or path.startswith(item) for item in ALLOWED)

def audit(final):
    errors = []
    if past(VOL + "/main.tex") != now(VOL + "/main.tex"):
        errors.append("main.tex chapter architecture altered")
    all_labels = []
    for name in CHAPTERS:
        path = VOL + "/chapters/" + name + ".tex"
        a, b = past(path), now(path)
        af, bf = blocks(a, FORMAL), blocks(b, FORMAL)
        ae, be = blocks(a, ("exercise", "problem")), blocks(b, ("exercise", "problem"))
        av, bv = FIGURE.findall(a), FIGURE.findall(b)
        for kind, original, new in (("formal", af, bf), ("exercise", ae, be), ("figure", av, bv)):
            if not is_subsequence(original, new):
                errors.append(name + ": original " + kind + " environments changed or moved")
        if not is_subsequence(LABEL.findall(a), LABEL.findall(b)):
            errors.append(name + ": original labels lost or reordered")
        new_keys = []
        if len(be) < len(ae):
            errors.append(name + ": exercises removed")
        else:
            for block in be[len(ae):]:
                m = LABEL.search(block)
                if not m:
                    errors.append(name + ": new exercise missing label")
                else:
                    new_keys.append(m.group(1))
        for kind in ("hint", "solution"):
            rx = re.compile(r"\\begin\{" + kind + r"\}\{[^}]+\}[\s\S]*?\\end\{" + kind + r"\}")
            if not is_subsequence(rx.findall(a), rx.findall(b)):
                errors.append(name + ": original " + kind + " body lost or edited")
            for k in new_keys:
                if len(re.findall(r"\\begin\{" + kind + r"\}\{" + re.escape(k) + r"\}", b)) != 1:
                    errors.append(name + ": new " + k + " lacks exactly one " + kind)
        added_ex = len(be) - len(ae)
        added_fig = len(bv) - len(av)
        if final and (added_ex, added_fig) != (4, 2):
            errors.append(f"{name}: expected 4 exercises/2 figures; got {added_ex}/{added_fig}")
        all_labels.extend(LABEL.findall(b))
        print(f"{name}: original {len(af)} formal, {len(ae)} exercises, {len(av)} figures; +{added_ex} exercises, +{added_fig} figures")
    old_figures = git("ls-tree", "-r", "--name-only", BASE, "--", VOL + "/figures/").decode().splitlines()
    for path in old_figures:
        if not (ROOT / path).is_file() or (ROOT / path).read_bytes() != git("show", BASE + ":" + path):
            errors.append("historical art changed: " + path)
    old_files = git("ls-tree", "-r", "--name-only", BASE, "--", VOL).decode().splitlines()
    for path in old_files:
        if path.endswith(".tex") and "/chapters/" in path and Path(path).stem in CHAPTERS:
            continue
        if path.startswith(VOL + "/figures/"):
            continue
        if not (ROOT / path).is_file() or (ROOT / path).read_bytes() != git("show", BASE + ":" + path):
            errors.append("non-chapter volume file changed: " + path)
    new_figs = sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / VOL / "figures").glob("v14c*.tex"))
    if final and len(new_figs) != 28:
        errors.append(f"expected 28 new plates, found {len(new_figs)}")
    for volume in OTHERS:
        if git("ls-tree", "-r", "HEAD", "--", volume) != git("ls-tree", "-r", BASE, "--", volume):
            errors.append("other volume modified: " + volume)
    changed = git("diff", "--name-only", BASE).decode().splitlines()
    untracked = git("ls-files", "--others", "--exclude-standard").decode().splitlines()
    for path in changed + untracked:
        if path and not allowed(path):
            errors.append("path outside the Volume 14 addition allowlist: " + path)
    if len(all_labels) != len(set(all_labels)):
        errors.append("duplicate labels in the printed chapter files")
    if errors:
        raise SystemExit("\n".join(errors))
    print("PASS: immutable source preservation, NOT mathematical signoff")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--final", action="store_true")
    audit(p.parse_args().final)
