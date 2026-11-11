#!/usr/bin/env python3
"""Number every formal statement and exercise of a volume in printed order.

Usage: python3 review/volume6-rewrite/statements.py volume5-calculation [regex]
Reads main.tex, follows \\input{chapters/...} in order, and counts the shared
theorem counter and the exercise counter per chapter, as common/interior-boxes.tex
does. Unlabelled statements are listed too, which the .aux file cannot do.
Appendices are lettered. Output: number, kind, label, optional title, first words.
"""
import re, sys, pathlib
root = pathlib.Path(__file__).resolve().parents[2]
vol = root / sys.argv[1]
pat = re.compile(sys.argv[2]) if len(sys.argv) > 2 else None
main = (vol / "main.tex").read_text()
main = re.sub(r"(?m)^\s*%.*$", "", main)
env = re.compile(r"\\begin\{(theorem|proposition|lemma|corollary|definition|example|exercise)\}(\[[^\]]*\])?|\\chapter(\*)?\{|\\appendix\b")
ch, thm, exo, app = 0, 0, 0, False
def walk(text):
    global ch, thm, exo, app
    for m in env.finditer(text):
        if m.group(0).startswith("\\appendix"):
            app, ch = True, 0; continue
        if m.group(0).startswith("\\chapter"):
            if m.group(3): continue
            ch += 1; thm = exo = 0
            name = chr(64 + ch) if app else str(ch)
            title = text[m.end():text.find("\n", m.end())][:70]
            line = f"== {name} {title}"
            if pat is None or pat.search(line): print(line)
            continue
        kind = m.group(1)
        if kind == "exercise": exo += 1; n = exo
        else: thm += 1; n = thm
        name = chr(64 + ch) if app else str(ch)
        rest = text[m.end():m.end() + 400]
        lab = re.search(r"\\label\{([^}]+)\}", rest[:120])
        body = re.sub(r"\\label\{[^}]+\}", "", rest).strip().replace("\n", " ")[:110]
        line = f"{name}.{n:<3} {kind:11} {lab.group(1) if lab else '-':22} {m.group(2) or ''} {body}"
        if pat is None or pat.search(line): print(line)
for m in re.finditer(r"\\appendix\b|\\(?:input|include)\{([^}]+)\}", main):
    if m.group(0).startswith("\\appendix"):
        app, ch = True, 0; continue
    p = vol / (m.group(1) + ("" if m.group(1).endswith(".tex") else ".tex"))
    if p.exists() and "chapters" in m.group(1):
        t = p.read_text()
        # nested inputs (a chapter that inputs a section file)
        t = re.sub(r"\\input\{(chapters/[^}]+)\}", lambda k: (vol / (k.group(1) + ".tex")).read_text() if (vol / (k.group(1) + ".tex")).exists() else "", t)
        walk(re.sub(r"(?m)(?<!\\)%.*$", "", t))
