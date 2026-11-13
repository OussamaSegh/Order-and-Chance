#!/usr/bin/env python3
"""List the chapter files reached from volume15 main.tex (recursively), and the unreached ones.

Usage: python3 review/volume15-rewrite/reached.py [--unreached] [--figures]
"""
import re, sys, pathlib
vol = pathlib.Path(__file__).resolve().parents[2] / "volume15-order-and-chance"
seen, todo = [], ["main"]
while todo:
    name = todo.pop(0)
    p = vol / (name if name.endswith(".tex") else name + ".tex")
    if not p.exists() or p in seen: continue
    seen.append(p)
    src = re.sub(r"(?<!\\)%.*", "", p.read_text())
    todo += re.findall(r"\\input\{([^}]+)\}", src)
reached = [p for p in seen if p.parent.name == "chapters"]
if "--unreached" in sys.argv:
    for p in sorted((vol / "chapters").glob("*.tex")):
        if p not in reached: print(p.relative_to(vol.parent))
elif "--figures" in sys.argv:
    figs = sorted({f for p in reached for f in re.findall(r"\\fig\{([^}]+)\}", p.read_text())})
    used = set(figs)
    for f in sorted((vol / "figures").glob("*.tex")):
        print(("used    " if f.stem in used else "UNUSED  ") + f.name)
else:
    for p in reached: print(p.relative_to(vol.parent))
