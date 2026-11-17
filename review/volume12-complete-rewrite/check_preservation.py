#!/usr/bin/env python3
"""Source-preservation audit, not mathematical proof verification."""
import argparse
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = "a685eb79a5551d0ee8a7b05074b3d01fc7677530"
VOLUME = "volume12-random-motion"
CHAPTERS = (
    "ch01-gaussian", "ch02-paths", "ch03-martingales", "ch04-ito",
    "ch05-analysis", "ch06-sde", "ch07-levy", "ch08-networks",
    "ch09-semicircle", "ch10-cue", "ch11-logcorrelated", "spectral",
)
FORMAL = ("theorem", "proposition", "lemma", "corollary", "definition",
          "example", "theoremx", "propositionx", "lemmax", "corollaryx",
          "definitionx", "examplex")
STATEMENT = re.compile(r"\\begin\{(" + "|".join((*FORMAL, "exercise", "problem")) + r")\}(?:\[[^\]]*\])?[\s\S]*?\\end\{\1\}")
FIGURE = re.compile(r"\\begin\{figure\}(?:\[[^\]]*\])?[\s\S]*?\\end\{figure\}")
LABEL = re.compile(r"\\label\{([^}]+)\}")

def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)

def old(path):
    return git("show", BASE + ":" + path).decode()

def new(path):
    return (ROOT / path).read_text()

def subsequence(a, b):
    iterator = iter(b)
    return all(any(x == y for y in iterator) for x in a)

def statements(source):
    return [(m.group(1), (z.group(1) if (z := LABEL.search(m.group())) else None))
            for m in STATEMENT.finditer(source)]

def exercise_keys(source, kind):
    return re.findall(r"\\begin\{" + kind + r"\}\{([^}]+)\}", source)

def audit(require_final):
    problems = []
    main = VOLUME + "/main.tex"
    if new(main) != old(main):
        problems.append("main.tex chapter/part/appendix structure changed")
    for chapter in CHAPTERS:
        path = VOLUME + "/chapters/" + chapter + ".tex"
        a, b = old(path), new(path)
        af, bf = statements(a), statements(b)
        orig_formal = [x for x in af if x[0] in FORMAL]
        fresh_formal = [x for x in bf if x[0] in FORMAL]
        orig_ex = [x for x in af if x[0] in ("exercise", "problem")]
        fresh_ex = [x for x in bf if x[0] in ("exercise", "problem")]
        orig_fig, fresh_fig = FIGURE.findall(a), FIGURE.findall(b)
        if orig_formal != fresh_formal:
            problems.append(path + ": original numbered formal statements changed")
        # Compare entire original statement and exercise environments, not just labels.
        # The only changed original statement is the documented correction of
        # the sigma=0 boundary case in Chapter 7's Levy--Ito theorem.
        def original_blocks(text, kinds):
            result = []
            for match in STATEMENT.finditer(text):
                if match.group(1) in kinds:
                    label_match = LABEL.search(match.group())
                    result.append((label_match.group(1) if label_match else None, match.group()))
            return result
        for kinds, group in ((FORMAL, "formal"), (("exercise", "problem"), "exercise")):
            before = original_blocks(a, kinds)
            after = original_blocks(b, kinds)
            for (label, raw), (new_label, fresh_raw) in zip(before, after):
                if label != new_label:
                    problems.append(path + ": original " + group + " label changed in body inventory")
                if raw != fresh_raw and not (chapter == "ch07-levy" and label == "thm:levyito"):
                    problems.append(path + ": original " + group + " text changed: " + str(label))
        # C0 control bytes are invalid in the TeX source. Ordinary newline and
        # horizontal tab do not count as errors.
        if any(ord(ch) < 32 and ch not in "\n\t" for ch in b):
            problems.append(path + ": invalid TeX control character")
        if fresh_ex[:len(orig_ex)] != orig_ex:
            problems.append(path + ": original exercises lost or reordered")
        if fresh_fig[:len(orig_fig)] != orig_fig:
            problems.append(path + ": original artwork environments changed")
        if not subsequence(LABEL.findall(a), LABEL.findall(b)):
            problems.append(path + ": original label order changed")
        for kind in ("hint", "solution"):
            # Every original full hint/solution block survives unchanged.
            pattern = re.compile(r"\\begin\{" + kind + r"\}\{[^}]+\}[\s\S]*?\\end\{" + kind + r"\}")
            if not subsequence(pattern.findall(a), pattern.findall(b)):
                problems.append(path + ": original " + kind + " *body text* changed or lost")
            oa, nb = exercise_keys(a, kind), exercise_keys(b, kind)
            if not subsequence(oa, nb):
                problems.append(path + ": original " + kind + " keys changed")
            for _, label in fresh_ex[len(orig_ex):]:
                if label is None or nb.count(label) != 1:
                    problems.append(path + ": exercise " + str(label) + " requires exactly one " + kind)
        for p in (r"\\section\{", r"\\subsection\{", r"\\begin\{equation\}"):
            if len(re.findall(p, a)) != len(re.findall(p, b)):
                problems.append(path + ": original numbered section/equation count changed")
        added_fig, added_ex = len(fresh_fig)-len(orig_fig), len(fresh_ex)-len(orig_ex)
        if require_final and (added_fig, added_ex) != (2, 4):
            problems.append(path + f": expected +2 figs/+4 exercises, got +{added_fig}/+{added_ex}")
        print(f"{chapter}: {len(orig_formal)} original statements; {len(orig_ex)} original exercises; {len(orig_fig)} original figures; added {added_fig} figures and {added_ex} exercises")
    nested = VOLUME + "/chapters/brw-halfmoment.tex"
    if new(nested) != old(nested):
        problems.append("nested Ch11 BRW section differs from original frozen source")
    original_art = git("ls-tree", "-r", "--name-only", BASE, "--", VOLUME+"/figures/").decode().splitlines()
    for path in original_art:
        if not (ROOT / path).is_file() or (ROOT / path).read_bytes() != git("show", BASE+":"+path):
            problems.append(path + ": historical artwork modified or missing")
    # Catch duplicate new names, including both 11 + Appendix.
    paths = [VOLUME+"/chapters/"+x+".tex" for x in CHAPTERS]
    all_labels = [label for p in paths for label in LABEL.findall(new(p))]
    if len(all_labels) != len(set(all_labels)):
        problems.append("duplicate labels in printed units")
    print(f"Frozen original illustration assets: {len(original_art)} files")
    if problems:
        raise SystemExit("\n".join(problems))
    print("PASS: immutable-baseline structural preservation (not mathematical or production acceptance)")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--final", action="store_true")
    audit(p.parse_args().final)
