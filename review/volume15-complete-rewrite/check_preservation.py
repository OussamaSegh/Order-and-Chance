#!/usr/bin/env python3
"""Immutable source-preservation gate for Volume 15. No proof certification."""
import argparse
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = "60ce094742a84e3da028ad2c9d31d535db656344"
VOL = "volume15-order-and-chance"
# Printed order. Each tuple is the chapter file and the section files it inputs.
UNITS = [
    ("ch01-integers", ["ra-anatomy"]),
    ("ch02-cramer", ["ra-largemoduli", "ra-gaps"]),
    ("ch03-divisors", ["ra-additive", "ra-selbergdelange", "ra-erdoskac"]),
    ("ch04-multiplicative", ["ra-randommult", "ra-polynomials"]),
    ("ch05-short", []),
    ("ch06-sieves", []),
    ("ch07-classgroups", ["ra-cohenlenstra", "ra-symmoments"]),
    ("ch08-ranks", []),
    ("ch09-gue", ["moments-zeta"]),
    ("ch10-moments", ["ra-moments"]),
    ("ch11-values", ["ra-bohrjessen", "ra-selberg"]),
    ("ch12-pseudorandom", []),
    ("ch13-bias", ["ra-bias"]),
    ("ch14-meeting", []),
]
FORMAL = (
    "theorem", "proposition", "lemma", "corollary", "definition", "example",
    "theoremx", "propositionx", "lemmax", "corollaryx", "definitionx", "examplex",
)
STATEMENT = re.compile(
    r"\\begin\{(" + "|".join((*FORMAL, "exercise", "problem")) + r")\}(?:\[[^\]]*\])?[\s\S]*?\\end\{\1\}"
)
FIGURE = re.compile(r"\\begin\{figure\}(?:\[[^\]]*\])?[\s\S]*?\\end\{figure\}")
LABEL = re.compile(r"\\label\{([^}]+)\}")
INPUT = re.compile(r"\\input\{chapters/([^}]+)\}")


def git(*args):
    return subprocess.check_output(("git", *args), cwd=ROOT)


def past(path):
    return git("show", f"{BASE}:{path}").decode()


def now(path):
    return (ROOT / path).read_text()


def is_subsequence(old, new):
    it = iter(new)
    return all(any(x == y for y in it) for x in old)


def blocks(text, kinds):
    return [m.group() for m in STATEMENT.finditer(text) if m.group(1) in kinds]


def expand(name, getter):
    text = getter(f"{VOL}/chapters/{name}.tex")
    return INPUT.sub(lambda m: expand(m.group(1), getter), text)


def audit(final):
    errors = []
    if past(f"{VOL}/main.tex") != now(f"{VOL}/main.tex"):
        errors.append("main.tex chapter architecture altered")
    all_labels = []
    for name, _includes in UNITS:
        old = expand(name, past)
        new = expand(name, now)
        of, nf = blocks(old, FORMAL), blocks(new, FORMAL)
        oe, ne = blocks(old, ("exercise", "problem")), blocks(new, ("exercise", "problem"))
        ov, nv = FIGURE.findall(old), FIGURE.findall(new)
        if of != nf:
            errors.append(name + ": a formal environment was edited")
        for kind, original, current in (("exercise", oe, ne), ("figure", ov, nv)):
            if not is_subsequence(original, current):
                errors.append(name + ": original " + kind + " environments changed or reordered")
        if not is_subsequence(LABEL.findall(old), LABEL.findall(new)):
            errors.append(name + ": original labels lost or reordered")
        new_keys = []
        if len(ne) < len(oe) or ne[:len(oe)] != oe:
            errors.append(name + ": new exercises are not a suffix of the original list")
        else:
            for block in ne[len(oe):]:
                m = LABEL.search(block)
                if not m:
                    errors.append(name + ": new exercise missing label")
                else:
                    new_keys.append(m.group(1))
        for kind in ("hint", "solution"):
            rx = re.compile(r"\\begin\{" + kind + r"\}\{[^}]+\}[\s\S]*?\\end\{" + kind + r"\}")
            if not is_subsequence(rx.findall(old), rx.findall(new)):
                errors.append(name + ": original " + kind + " body lost or edited")
            for key in new_keys:
                if len(re.findall(r"\\begin\{" + kind + r"\}\{" + re.escape(key) + r"\}", new)) != 1:
                    errors.append(name + ": new " + key + " lacks exactly one " + kind)
        added_ex, added_fig = len(ne) - len(oe), len(nv) - len(ov)
        if final and (added_ex, added_fig) != (4, 2):
            errors.append(f"{name}: expected 4 exercises/2 figures; got {added_ex}/{added_fig}")
        all_labels.extend(LABEL.findall(new))
        print(f"{name}: original {len(of)} formal, {len(oe)} exercises, {len(ov)} figures; +{added_ex} exercises, +{added_fig} figures")
    for path in git("ls-tree", "-r", "--name-only", BASE, "--", f"{VOL}/figures/").decode().splitlines():
        if not (ROOT / path).is_file() or (ROOT / path).read_bytes() != git("show", f"{BASE}:{path}"):
            errors.append("historical art changed: " + path)
    earlier = (
        "volume1-first-principles", "volume2-integers", "volume3-symmetry",
        "volume4-chance", "volume5-calculation", "volume6-crossroads",
        "volume7-spaces", "volume8-analysis", "volume9-shapes",
        "volume10-abstraction", "volume11-randomness", "volume12-random-motion",
        "volume13-arithmetic", "volume14-primes",
    )
    for volume in earlier:
        if git("ls-tree", "-r", "HEAD", "--", volume) != git("ls-tree", "-r", BASE, "--", volume):
            errors.append("accepted earlier volume modified: " + volume)
    frozen = (
        "preface.tex", "about-the-cover.tex", "blurb.tex", "kdp.md",
        "cover-lettering.tex", "cover-motif.tex",
    )
    for name in frozen:
        path = f"{VOL}/{name}" if name != "preface.tex" else f"{VOL}/chapters/preface.tex"
        if name == "preface.tex":
            path = f"{VOL}/chapters/preface.tex"
        if past(path) != now(path):
            errors.append("frozen file changed: " + path)
    if len(all_labels) != len(set(all_labels)):
        seen = set()
        for lab in all_labels:
            if lab in seen:
                errors.append("duplicate label: " + lab)
            seen.add(lab)
    if errors:
        raise SystemExit("\n".join(errors))
    print("PASS: immutable source preservation, NOT mathematical signoff")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--final", action="store_true")
    audit(parser.parse_args().final)
