# Volume 4 — Chance, round 6

**Score: 9/10.**

**Counts.** 0 critical, 0 major, 1 minor. `V4-R6-001`.

**Round-5 follow-up.** 2 resolved, 0 regressed. The clip of \(Q^2\) is the sum of two monotone clips, and the product expands into four bounded products. The hitting shell is no longer priced by subtracting outer contents.

**How this was read.** The two paragraphs changed by #306, on main at `9d546181`. No full LaTeX build was run. Chapters that #306 did not edit were not re-opened.

## Issues

| ID | Location | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- |
| V4-R6-001 | `chapters/ch11-brownian.tex:346` | minor | “The cubes are coordinate rectangles, and that proof turns their total Gaussian mass into an outer content.” | Theorem `thm:levy` writes that comparison for one interval condition on a linear image. The shell is the set where the maximum of several partial sums lies in an interval. The text already says a cube moves every partial sum, so a cube that meets the shell sits in the enlarged shell. It does not say that subadditivity bounds the outer content of the union of those cubes by their total mass. That mass is at most the integral over the enlarged shell, which is the small quantity. One sentence closes it. |

## Not checked

- A LaTeX build.
- Chapters that #306 did not edit.
