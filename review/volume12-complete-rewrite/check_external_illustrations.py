#!/usr/bin/env python3
"""Prevent illustrations from disappearing in EPUB / online reader.

Only external \fig{name} sources are compiled to SVG/PNG by build.sh.
This tests the digital-source pipeline, not visual appearance of artifacts.
"""
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VOL = ROOT / "volume12-random-motion"
NAMES = ("ch01-gaussian", "ch02-paths", "ch03-martingales", "ch04-ito",
         "ch05-analysis", "ch06-sde", "ch07-levy", "ch08-networks",
         "ch09-semicircle", "ch10-cue", "ch11-logcorrelated", "spectral")
new = {}
for chapter in NAMES:
    s = (VOL / "chapters" / (chapter + ".tex")).read_text()
    if r"\begin{tikzpicture}" in s:
        raise SystemExit(chapter + ": inline TikZ is not delivered in EPUB/HTML")
    labels = re.findall(r"\\label\{fig:(v12[^}]+)\}", s)
    if len(labels) != 2:
        raise SystemExit(chapter + ": expected exactly 2 new labelled illustrations")
    for label in labels:
        path = VOL / "figures" / (label + ".tex")
        if not path.is_file():
            raise SystemExit(str(path) + " is missing")
        text = path.read_text()
        if r"\begin{tikzpicture}" not in text or r"\end{tikzpicture}" not in text:
            raise SystemExit(label + " cannot compile as a standalone picture")
        if s.count(r"\fig{" + label + "}") != 1:
            raise SystemExit(chapter + ": non-canonical figure call for " + label)
        if label in new:
            raise SystemExit("duplicate figure " + label)
        new[label] = chapter
assert len(new) == 24
with tempfile.TemporaryDirectory() as tmp:
    target = Path(tmp) / "epub.tex"
    figdir = Path(tmp) / "figures"
    figdir.mkdir()
    subprocess.run(["python3", str(ROOT / "tools" / "epub_prep.py"),
                    str(VOL / "main.tex"), str(target), str(figdir)],
                   check=True, cwd=ROOT)
    epub_tex = target.read_text()
    for label in new:
        if (str(figdir.resolve() / (label + ".svg"))) not in epub_tex:
            raise SystemExit(label + ": SVG missing from pandoc EPUB input")
print("PASS: 24 figures canonical for PDF/print, SVG EPUB prep and web reader")
