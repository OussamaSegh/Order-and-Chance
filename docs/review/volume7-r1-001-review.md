# V7-R1-001 second review

Verdict: **approve**. The fix was not changed.

Reviewed the fix at `0e59353677fd1e13297ec7bf9f8cebd59fa59468`.

## What was checked

The issue is real. On \([0,1]\), the function with value \(1\) at \(0\) and value \(0\) on \((0,1]\) has derivative \(0\) on the interior, and it is not non-decreasing, not constant, and not Lipschitz. Part (c) already requires continuity on the closed segment. The old part (d) applied part (c) on every \([x,y]\subset I\) without that hypothesis.

The new statement requires continuity on \(I\) and differentiability on the interior. For \(x<y\) in an interval, \([x,y]\subset I\), so part (c) applies. The three conclusions are the same identity. The label `thm:mvt` is unchanged, and no environment was added.

Every use of `thm:mvt`, and every phrase "mean value theorem", in `volume7-spaces/` was read. The part (d) uses are the cosine bound on \([0,1]\) in Chapter 2 and in the sentence after the theorem, Newton's map \(N(x)=\frac12(x+a/x)\) on \([\sqrt a,+\infty[\) in the solution of `ex:newton`, and the polynomials in the proof of `thm:banachmaz` and in the solution of `ex:monotone2`. Each of those functions is continuous on the interval where the bound is used. The other citations use the equality in part (c), on a function that is \(C^1\) or \(C^\infty\) on a neighbourhood of the segment: \(\varphi'\) in Young's inequality, the parameter derivative in `thm:parameter`, the segments in the change-of-variables lemma, the polynomial in the Liouville solution, sine on \([0,1]\), and the derivatives of the \(C^\infty\) function in `ex:polynomial`.

The diff is only `volume7-spaces/chapters/ch04-compact.tex`. No `\label`, `\caption`, figure command, or font command is in the diff. A sequential merge of all nineteen fix branches onto `main` produced no conflict.

## What was not checked

`./build.sh` was not run. Volume 7 was not compiled. GitHub Actions was not opened. The proofs of Taylor's formula, l'Hôpital's rule, the monotonicity of \(\exp\), and the convex inequalities in Volume 1 were not re-read. Those are the results named in the paragraph after the theorem, and the functions in that list are continuous, but that is not a line-by-line check of Volume 1.

## Issue log

| Problem | Resolution |
| --- | --- |
| None. | The fix stands. This note is the only addition. |
