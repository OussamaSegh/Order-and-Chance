# Volume 3 — Symmetry

**Score: 9/10.**

The round-4 repairs hold, including the cap-set products \(27552\cdot102=2810304>2810245=19381\cdot145\) and \(3048625\cdot3481=10612263625>10612080000\). The cube count, the groups of order \(8\), the Sylow census, the cyclotomic minimal polynomial, the quaternion trace, Wielandt’s bound, and the Paley block products were read as proofs and hold. One outlook names the wrong chapter of Volume 13.

**Counts.** 0 critical, 0 major, 1 minor. `V3-R5-001`.

**Round-4 follow-up.** 7 resolved, 0 partial, 0 open, 0 regressed.

**How this was read.** Book order in `volume3-symmetry/main.tex`, on main at `2612a86c`, including the appendices and the afterword. Every chapter file was read, including exercises, hints, solutions, and captions. The Volume 13 pointer was checked against that volume’s `main.tex` order. No full LaTeX build was run.

## Issues

Paths are relative to `volume3-symmetry/`.

| ID | Location | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- |
| V3-R5-001 | `chapters/ch06-rings.tex:930` | minor | “Volume~13, Chapters~1 and~2, will prove … in the ring of integers of a number field every nonzero ideal factors uniquely into prime ideals.” | In Volume 13’s own order, Chapters 1 and 2 are the quadratic field and its ideals. The general statement is Chapter 4, Theorem `thm:ufi`. The sentence says the theorem is an outlook, not a premise, so the wrong number does not enter a proof. |

## Round-4 follow-up

The empty product is the left side only. \(GL_2(\Z)\) carries the column lattice of \(T\) onto that of \(UT\). The positive root of \(t^2+t-1=0\) is \((\sqrt5-1)/2\). The trace sum is \(3a^2-\lvert x\rvert^2\), then \(4a^2-1\). The quintic sentence has no vanishing-denominator proviso. Fisher uses \(\lambda\le\lvert A_i\rvert\). The cap-set constant uses \(145/102\).

## Not checked

- A LaTeX build.
- Figures were not re-rendered.
