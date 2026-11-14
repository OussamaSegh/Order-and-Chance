#!/usr/bin/env python3
"""Resolve the bare numbers inside reminder boxes against the volume the box names.

Usage: python3 review/volume14-rewrite/reminder_citations.py volume14-primes/chapters/ch01-zeros.tex ...
A reminder headed [from Volume~6] cites "(Theorem~6.9)" without the volume. Inside a box
that names one volume, each bare number is looked up in that volume's printed order.
A box that names several volumes is split at each "Volume~N" mention, and the numbers
that follow a mention are resolved against that volume. A human reads the columns.
"""
import re, sys, pathlib
sys.argv, files = sys.argv[:1], sys.argv[1:]
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import importlib.util
spec = importlib.util.spec_from_file_location("rc", pathlib.Path(__file__).parent / "resolve_citations.py")
rc = importlib.util.module_from_spec(spec); spec.loader.exec_module(rc)
kinds = r"(Chapters?|Theorems?|Propositions?|Lemmas?|Corollar(?:y|ies)|Exercises?|Definitions?|Examples?)"
num = re.compile(kinds + r"~([\dA-Z]+(?:\.\d+)?)((?:(?:, |,? and~|--)[\dA-Z]+\.\d+)*)")
for f in files:
    text = pathlib.Path(f).read_text()
    for m in re.finditer(r"\\begin\{reminder\}(\[[^\]]*\])?(.*?)\\end\{reminder\}", text, re.S):
        head = m.group(1) or ""
        vols = [int(v) for v in re.findall(r"Volumes?[~ ](\d+)", head)]
        body = m.group(2)
        cur = vols[0] if vols else None
        pos = 0
        for tok in re.finditer(r"Volume~(\d+)|" + num.pattern, body):
            if tok.group(1):
                cur = int(tok.group(1)); continue
            kind = tok.group(2).lower(); x = tok.group(3)
            nums = [x] + re.findall(r"[\dA-Z]+\.\d+", tok.group(4) or "")
            line = text[:m.start(2) + tok.start()].count("\n") + 1
            for y in nums:
                if cur is None:
                    print(f"{pathlib.Path(f).name}:{line}: ?? {tok.group(2)} {y} (no volume)"); continue
                key = ("chapter", y) if kind.startswith("chapter") else ("exercise" if kind.startswith("exercise") else "stmt", y)
                print(f"{pathlib.Path(f).name}:{line}: V{cur} {tok.group(2)} {y} -> {rc.table(cur).get(key, 'MISSING')}")
