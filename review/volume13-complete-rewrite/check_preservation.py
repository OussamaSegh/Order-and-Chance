#!/usr/bin/env python3
"""Immutable source-preservation gate; no proof certification is implied."""
import argparse
import re
import subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
BASE = "480cbe195022977a04bdcb78255ab6a1eb12720b"
VOL = "volume13-arithmetic"
CHAPTERS = ["ch11-algebraic","ch12-ideals-quadratic","ch01-number-fields","ch02-ideals","ch03-geometry","ch04-units","ch05-cyclotomic","ch12-padic","ch06-local","ch07-hasse","ch08-zeta","ch09-tate","ch10-cft","ch11-curves","ch12-elliptic","ch13-finite","ch14-modular"]
FORMAL = ("theorem","proposition","lemma","corollary","definition","example","theoremx","propositionx","lemmax","corollaryx","definitionx","examplex")
STATEMENT = re.compile(r"\\begin\{(" + "|".join((*FORMAL,"exercise","problem")) + r")\}(?:\[[^\]]*\])?[\s\S]*?\\end\{\1\}")
FIGURE = re.compile(r"\\begin\{figure\}(?:\[[^\]]*\])?[\s\S]*?\\end\{figure\}")
LABEL = re.compile(r"\\label\{([^}]+)\}")
def git(*args):
    return subprocess.check_output(("git",*args),cwd=ROOT)
def past(path):
    return git("show",BASE+":"+path).decode()
def now(path):
    return (ROOT/path).read_text()
def is_subsequence(a,b):
    it=iter(b)
    return all(any(x==y for y in it) for x in a)
def blocks(s,kinds):
    return [m.group() for m in STATEMENT.finditer(s) if m.group(1) in kinds]
def audit(final):
    errors=[]
    if past(VOL+"/main.tex") != now(VOL+"/main.tex"):
        errors.append("main.tex chapter architecture altered")
    all_labels=[]
    for name in CHAPTERS:
        path=VOL+"/chapters/"+name+".tex"
        a,b=past(path),now(path)
        af,bf=blocks(a,FORMAL),blocks(b,FORMAL)
        ae,be=blocks(a,("exercise","problem")),blocks(b,("exercise","problem"))
        av,bv=FIGURE.findall(a),FIGURE.findall(b)
        for kind,original,new in (("formal",af,bf),("exercise",ae,be),("figure",av,bv)):
            if not is_subsequence(original,new):
                errors.append(name+": original "+kind+" environments changed or moved")
        if not is_subsequence(LABEL.findall(a),LABEL.findall(b)):
            errors.append(name+": original labels lost or reordered")
        new_keys=[]
        for block in be[len(ae):]:
            m=LABEL.search(block)
            if not m: errors.append(name+": new exercise missing label")
            else: new_keys.append(m.group(1))
        for kind in ("hint","solution"):
            rx=re.compile(r"\\begin\{"+kind+r"\}\{[^}]+\}[\s\S]*?\\end\{"+kind+r"\}")
            if not is_subsequence(rx.findall(a),rx.findall(b)):
                errors.append(name+": original "+kind+" body lost or edited")
            for k in new_keys:
                if len(re.findall(r"\\begin\{"+kind+r"\}\{"+re.escape(k)+r"\}",b))!=1:
                    errors.append(name+": new "+k+" lacks exactly one "+kind)
        added_ex=len(be)-len(ae)
        added_fig=len(bv)-len(av)
        if final and (added_ex,added_fig)!=(4,2):
            errors.append(f"{name}: expected 4 exercises/2 figures; got {added_ex}/{added_fig}")
        all_labels.extend(LABEL.findall(b))
        print(f"{name}: original {len(af)} formal, {len(ae)} exercises, {len(av)} figures; +{added_ex} exercises, +{added_fig} figures")
    for path in git("ls-tree","-r","--name-only",BASE,"--",VOL+"/figures/").decode().splitlines():
        if not (ROOT/path).is_file() or (ROOT/path).read_bytes()!=git("show",BASE+":"+path):
            errors.append("historical art changed: "+path)
    for volume in ("volume1-first-principles","volume2-integers","volume3-symmetry","volume4-chance","volume5-calculation","volume6-crossroads","volume7-spaces","volume8-analysis","volume9-shapes","volume10-abstraction","volume11-randomness","volume12-random-motion"):
        if git("ls-tree","-r","HEAD","--",volume)!=git("ls-tree","-r",BASE,"--",volume):
            errors.append("accepted earlier volume modified: "+volume)
    if len(all_labels)!=len(set(all_labels)):
        errors.append("duplicate labels in the printed chapter files")
    if errors: raise SystemExit("\n".join(errors))
    print("PASS: immutable source preservation, NOT mathematical signoff")
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--final",action="store_true")
    audit(p.parse_args().final)
