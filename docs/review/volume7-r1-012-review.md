# V7-R1-012 second review

Verdict: **approve**. The fix was not changed.

Reviewed the fix at `bb9036c432c9743476321889b3e84f36804b705c`.

## What was checked

The issue is real. The integer \(n+1\) lies in both \([n,n+1]\) and \([n+1,n+2]\).

For a fixed \(x\), the integers \(n\) with \(x\in[n,n+1]\) are the integers in \([x-1,x]\), hence at most two. So \(f_n(x)=0\) for all large \(n\), and \(f_n(x)\to 0\). Each integral remains \(1\). The bound \(0\le f_n\le 1\), the failure of domination, and the strict Fatou inequality \(0\le 1\) are unchanged. The integral values are separate from the overlap sentence.

The diff is one sentence in `volume7-spaces/chapters/ch07-integral.tex`. No label, caption, or diagram command changed. It does not meet V7-R1-011, V7-R1-013, or V7-R1-014. The nineteen branches merge onto `main` with no conflict.

## What was not checked

`./build.sh` was not run. Volume 7 was not compiled. GitHub Actions was not opened. The statement of Fatou's lemma was not re-proved.

## Issue log

| Problem | Resolution |
| --- | --- |
| None. | The fix stands. This note is the only addition. |
