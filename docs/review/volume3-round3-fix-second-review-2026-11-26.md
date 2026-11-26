# Volume 3 round-3 fix, second review — 26 November 2026

Independent reading of the Volume 3 fix at `ada42f6b6e8374e204627107ff5b84109a9251b5`, on `cursor/fix-v3-round3-3de4`, based on `main` at `68261d60`. The first commit was `49a22f41`. The corrections below are the later commit. The reader of this note did not write the first commit.

## Verdicts

**Correctness.** The first commit left two defects, listed below. After `ada42f6b`, each of `V3-R3-001` through `V3-R3-009` is fixed in the sentence the round-3 log named. The second reading of the correction commit closed both defects and found no new false step.

**Dropped or weakened proofs.** No numbered proof was shortened. The Smith-form ideal inclusion is still `I_k(PAQ)=I_k(A)`. The diagonal remains unique up to a unit, which the theorem already said. The minor expansion no longer says "up to sign". A new minor is an `R`-multiple of old minors, which is what an `r`-multiple of a row produces. Replacing that phrase by "up to a unit" would have been false, and it was not done.

**Labels.** Compared with `68261d60`, the TeX files under `volume3-symmetry/` have the same `\label` names. No numbered environment was added or removed.

**Caption and diagram typography.** No plate was edited.

**Voice.** The new sentences name the object and the step. The banned fillers do not appear in the diff.

**Checked identities.** With `\varphi=(1+\sqrt5)/2`, one has `1/\varphi=(\sqrt5-1)/2=(-1+\sqrt5)/2` and `-\varphi=(-1-\sqrt5)/2`. The pentagon eigenvalues `(-1\pm\sqrt5)/2` are those two numbers, together with the degree `2`.

## Findings, closed in `ada42f6b`

| ID | Location | Problem | Fix |
| --- | --- | --- | --- |
| SR-001 | `ch12-quaternions.tex`, the trace paragraph | The proved identity is `(x\times y)\times z=y(x\cdot z)-x(y\cdot z)`. The first commit treated it as `x\times(x\times w)=(x\cdot w)x-\lvert x\rvert^2 w` without the reversal. The coefficient `-\lvert x\rvert^2`, and therefore the trace, depends on that sign. | The identity is applied as `(x\times w)\times x=\lvert x\rvert^2 w-(x\cdot w)x`. Antisymmetry reverses the order. |
| SR-002 | `linear-ch07-perron.tex`, the period paragraph | "A simple cycle's length is one of the lengths in the gcd" names no gcd yet. A gcd is not a set of lengths. | If the walk is a simple cycle, the gcd of the simple-cycle lengths divides its length, and that is the base of the induction. |

## Issue-by-issue

| ID | Where the repair sits |
| --- | --- |
| V3-R3-001 | `ch12-quaternions.tex`. The pure-term collection gives `R_q(w)=(a^2-\lvert x\rvert^2)w+2(x\cdot w)x+2a(x\times w)`. The diagonal sum is `3a^2-\lvert x\rvert^2=4a^2-1`. The difference `R_{32}-R_{23}` is `4ab`, and the cycled pairs are `4ac` and `4ad`. Closed by SR-001. |
| V3-R3-002 | `ch12-quaternions.tex`, the plane rotation. The first column is a unit vector. Orthogonality leaves `\pm(-\sin\theta,\cos\theta)`. Determinant `1` selects `(-\sin\theta,\cos\theta)`. |
| V3-R3-003 | `ch07-modules.tex`, `thm:smith`. Each remaining term in the minor expansion is an `R`-multiple of an old minor. |
| V3-R3-004 | `linear-ch09-symmetry.tex`. The pentagon eigenvalues are `2`, `1/\varphi` and `-\varphi`. |
| V3-R3-005 | `linear-ch09-symmetry.tex`. `J` is the all-ones matrix. `B` and `J` both vanish on the sum-zero vectors, and `B\mathbf 1=\frac{p-1}{4}J\mathbf 1` is computed before `B=cJ`. |
| V3-R3-006 | `linear-ch09-symmetry.tex`, Hoffman's bound. The rearrangement `0\ge \tau s+(k-\tau)s^2/v` comes before the division. Since `\tau<0`, the inequality becomes `-\tau s\ge (k-\tau)s^2/v` before dividing by the positive numbers `s` and `k-\tau`. |
| V3-R3-007 | `linear-ch07-perron.tex`. A non-simple closed walk has length equal to the sum of two strictly shorter closed walks. Closed by SR-002. |
| V3-R3-008 | `linear-ch07-perron.tex`, solution of `linear:ex:diagpos`. A shortest path has no repeated vertex, because deleting the directed cycle between two visits would leave a shorter path. |
| V3-R3-009 | `paley.tex`, `prop:hadamard-four`. The counts of `+1` and `-1` satisfy `p+m=n` and `p-m=0`, so `2p=n`. The count `n/2` is used only after that. |

## What this review did not check

- A LaTeX build. XeLaTeX is not installed in the review environment.
- EPUB rendering.
- Proofs the diff does not touch, beyond the sentences needed to see that each repair cites an earlier result.
