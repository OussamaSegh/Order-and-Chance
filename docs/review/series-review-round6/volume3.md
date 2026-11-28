# Volume 3 — Symmetry

**Score: 9/10.**

The round-5 outlook now cites Volume 13, Chapter 4, and still says the theorem is not a premise. The round-4 arithmetic was recomputed and holds. Two local sentences remain.

**Counts.** 0 critical, 0 major, 2 minor. `V3-R6-001` and `V3-R6-002`.

**Round-5 follow-up.** 1 resolved, 0 partial, 0 open, 0 regressed.

**How this was read.** Book order in `volume3-symmetry/main.tex`, on main at `e712991e`, including the appendices and the afterword. Every chapter file was read, including exercises, hints, solutions, and captions. No full LaTeX build was run.

## Issues

Paths are relative to `volume3-symmetry/`.

| ID | Location | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- |
| V3-R6-001 | `chapters/ch01-groups.tex:309` | minor | “These \(9+8+6=23\) non-identity rotations are visibly distinct.” | A non-identity rotation is determined by the line it fixes and by its angle. The three face axes, four diagonals and six edge axes are different lines, and the two angles about one diagonal are different. The count is what shows there are \(24\) rotations, so the distinctness is load-bearing. The conclusion is the standard one. |
| V3-R6-002 | `chapters/ch12-quaternions.tex:1644` | minor | “Theorem~1.6 (unique prime factorisation)”. | The number is Volume 2’s. Chapter 6 of this volume already writes “Volume~2’s Theorem~1.6” for the same fact. The index of Volume 2 sends Theorem 1.6 to `thm:fta`. The tools line omits the volume. |

## Not checked

- A LaTeX build.
- Figures were not re-rendered.
