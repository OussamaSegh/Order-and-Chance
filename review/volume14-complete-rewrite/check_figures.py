#!/usr/bin/env python3
"""Check all added figure sources and chapter references; not visual QA."""
from pathlib import Path
V = Path(__file__).resolve().parents[2] / "volume14-primes"
FILES = (
    "ch01-zeros", "ch02-siegel", "ch03-sieves", "ch04-largesieve", "ch05-expsums",
    "waring", "three-primes", "ch08-gpy", "ch09-maynard", "ch10-halasz",
    "ch11-additive", "ch12-roth", "ch13-gowers", "ch14-critical",
)
PLATES = {
    1: ("v14c01-cost", "v14c01-theta"),
    2: ("v14c02-trig", "v14c02-class"),
    3: ("v14c03-parity", "v14c03-artin"),
    4: ("v14c04-product", "v14c04-level"),
    5: ("v14c05-kloosterman", "v14c05-bounds"),
    6: ("v14c06-gamma", "v14c06-arcs"),
    7: ("v14c07-local", "v14c07-count"),
    8: ("v14c08-admissible", "v14c08-diameter"),
    9: ("v14c09-simplex", "v14c09-ratio"),
    10: ("v14c10-distance", "v14c10-decay"),
    11: ("v14c11-sets", "v14c11-line"),
    12: ("v14c12-spheres", "v14c12-bound"),
    13: ("v14c13-phase", "v14c13-wtrick"),
    14: ("v14c14-moments", "v14c14-pair"),
}
for i, name in enumerate(FILES, 1):
    src = (V / "chapters" / (name + ".tex")).read_text()
    for x, stem in zip("ab", PLATES[i]):
        art = V / "figures" / (stem + ".tex")
        assert art.is_file(), f"Missing {art}"
        s = art.read_text()
        assert s.count(r"\begin{tikzpicture}") == 1 and s.count(r"\end{tikzpicture}") == 1, stem
        assert src.count(r"\fig{" + stem + "}") == 1, stem
        assert src.count(r"\label{fig:v14-extra-" + f"{i:02}-{x}" + "}") == 1, stem
        assert len(s) > 80, stem
        assert not any(ord(c) < 32 and c not in "\n\t" for c in s), stem
    print(f"chapter {i:02}: 2 external TikZ plates and labels present")
print("PASS: 28 external TikZ assets referenced once (rendered inspection still required)")
