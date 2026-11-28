# V7-R1-010 second review

Verdict: **approve**. The fix was not changed.

Reviewed the fix at `d5a77e1593a5f34c699e1c23873f3a6186081f0a`.

## What was checked

The issue is real. Membership in \(E_n\) bounds right difference quotients at one point. It does not produce a derivative. The old last sentence said the complement of the meagre set was exactly the set of nowhere differentiable functions.

Takagi's function is nowhere differentiable by Theorem `thm:takagi`. At \(x=\frac13\), its right difference quotient is at most \(7\) for every \(h>0\). While \(2^nh<\frac16\), the term of index \(n\) contributes the slope \((-1)^n\), and a partial sum of alternating \(\pm 1\) has absolute value at most \(1\). The tail, using \(|\phi(a)-\phi(b)|\le\frac12\) and \(2^{N+1}h\ge\frac16\), is at most \(6\). Thus \(T\in E_n\) for every \(n\ge 7\), since \(\frac13\le 1-\frac1n\). The complement of \(\bigcup_n E_n\) therefore misses a nowhere differentiable function.

The new sentence says the complement is a comeagre, hence dense, set of nowhere differentiable functions. Comeagre is defined as the complement of a meagre set. The argument still puts every somewhere-differentiable function into the union of the two meagre sets, so the complement consists of nowhere differentiable functions. Theorem `thm:banachmaz` asks for that meagre set, and for density of the nowhere differentiable functions. Both remain. The false equality is gone. The label is unchanged.

The diff is one sentence in `volume7-spaces/chapters/ch05-baire.tex`. No caption or diagram command changed. This file is not edited by another fix branch. The nineteen branches merge onto `main` with no conflict.

## What was not checked

`./build.sh` was not run. Volume 7 was not compiled. GitHub Actions was not opened. The proof that each \(E_n\) is closed and has empty interior was not re-derived. The Takagi series was not summed numerically.

## Issue log

| Problem | Resolution |
| --- | --- |
| None. | The fix stands. This note is the only addition. |
