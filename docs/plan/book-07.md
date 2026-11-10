# Volume 7 — Spaces

*Topology, Measure and Limits.*

**Status of this file.** Blueprint of Volume 7 under the [master plan](MASTER-PLAN-V5-V15.md), 2026-11-10. It replaces the earlier specification. No proof named here has been verified.

**Series part.** III. Analysis and Geometry. **Directory.** `volume7-spaces`.

## Central question

What were "limit", "length" and "typical" all along? The earlier volumes used these words on trust. This volume builds the rooms they live in, and pays the debts.

## Prerequisites

Volume 1: completeness of the real numbers as a working fact, calculus, sequences. Volume 4 is motivation, not a premise: nothing here uses a theorem of probability. No later volume is used.

## Structure

Unchanged except inside the last chapter.

| Ch. | Title | File | Action |
| --- | --- | --- | --- |
| | **Part I. Metric and Topological Spaces** | | |
| 1 | Sets, Choice and the Real Numbers | `ch01-sets.tex` | Keep |
| 2 | Metric Spaces and Completeness | `ch02-metric.tex` | Keep; one corollary added |
| 3 | Topological Spaces | `ch03-topology.tex` | Keep |
| 4 | Compactness | `ch04-compact.tex` | Keep |
| 5 | Baire's Theorem | `ch05-baire.tex` | Keep |
| 6 | The Jordan Curve Theorem | `jordan.tex`, `jordan-polygon.tex` | Keep |
| | **Part II. Measure and Integration** | | |
| 7 | Measures | `ch06-measures.tex` | Keep |
| 8 | The Lebesgue Integral | `ch07-integral.tex` | Keep |
| 9 | Product Measures and Change of Variables | `ch08-products.tex` | Keep |
| 10 | \(L^p\) Spaces | `ch09-lp.tex` | Keep |
| | **Part III. Measures on Spaces** | | |
| 11 | Differentiation and Radon–Nikodym | `ch10-radon.tex` | Keep |
| 12 | Measures on Metric Spaces | `ch11-metricmeasures.tex` | Keep |
| 13 | Almost Every Number (problems) | `ch12-harder.tex` | Split (D-15) |

## Essential definitions and results

The real numbers from sets. Metric, completion, compactness, connectedness. \(\sigma\)-algebra, outer measure, measurable function, integral. Product measure. \(L^p\). Absolute continuity. Weak convergence of measures, tightness. Hausdorff measure and dimension.

## Flagship theorems, proved in this volume

| Theorem | Label | Chapter |
| --- | --- | --- |
| Completion of a metric space; \(\mathbb Q_p\) as the completion of \(\mathbb Q\), with \(\mathbb Z_p\) and digit expansions; \(\mathbb Z_p\) is compact | `thm:Qp`, new corollary | 2 |
| Tychonoff for countable products; Arzelà–Ascoli; Stone–Weierstrass | | 4 |
| Baire's theorem and its consequences | | 5 |
| The Jordan curve theorem | | 6 |
| Carathéodory's extension; Lebesgue measure and its uniqueness | | 7 |
| Monotone and dominated convergence | | 8 |
| Fubini–Tonelli; change of variables | | 9 |
| Hölder, Minkowski, completeness of \(L^p\) | | 10 |
| Lebesgue differentiation; Radon–Nikodym; conditional expectation and the tower property | `thm:rn`, `thm:condexp`, `thm:tower` | 11 |
| Riesz representation on a compact metric space; portmanteau; Prokhorov; Kolmogorov extension | `thm:riesz`, `thm:portmanteau`, `thm:prokhorov`, `thm:kolmogorov` | 12 |

## Stated without proof

| Statement | Heading must say |
| --- | --- |
| That Hausdorff measure is a Borel measure with \(\mathcal H^d=c_d\lambda_d\), if still cited to the literature | Quoted, with source. No later chapter may then use \(\mathcal H^d\) as a measure built here |
| The Banach–Tarski paradox and similar landmarks | Quoted |

## Climax

Chapter 9: Fubini and Tonelli, the theorem three earlier volumes borrowed. Then Chapter 12: a limit of measures, which is what every limit theorem of Volumes 11 and 12 will be.

## Motivation and history

Cantor and Dedekind, Hausdorff, Baire's thesis, Lebesgue's coins sorted by value, Vitali's set, Radon and Nikodym, Kolmogorov's 1933 foundations, Mandelbrot's coast of Britain. Hensel's \(p\)-adic numbers appear in Chapter 2 as the completion nobody expects.

## Examples and exercises

The Cantor set and the devil's staircase run through Parts I to III as one example. The \(p\)-adic integers as a compact metric space that is not a subset of \(\mathbb R^n\). A typical continuous function is nowhere differentiable. The Sierpiński carpet of the cover has dimension \(\log8/\log3\).

Three levels of exercises in each chapter. Chapter 13 is the volume's problem chapter.

## Figures and experiments

The staircase; a nowhere differentiable function; the carpet; boxes covering a coastline. No printed number in this volume depends on a computation except the dimension estimates in Chapter 12's figure, which are listed in the ledger.

## Changes from the current manuscript

**Preserve.** Chapters 1–12.

**Add.** In Chapter 2, after `thm:Qp`: \(\mathbb Z_p\) is compact, and \(\mathbb Q_p\) is locally compact. Half a page. This is the statement Volume 8's Haar chapter needs (decisions D-14, D-17). In the preface: a table of the debts this volume pays, listing each admitted fact of Volumes 4–6 and the theorem that proves it.

**Split.** Chapter 13 has 22 problems. Those whose solutions use the Gauss map, Birkhoff's theorem or Lévy's theorem from Volume 11, Chapter 10 move to Volume 11. Dirichlet's approximation, Liouville numbers, Khinchin's theorem (both halves, by Borel–Cantelli and a second-moment argument) and the comparison of category with measure stay. The chapter's title stays.

**Remove.** The pointers "Volume 13, Chapter 2" and "Volume 2, Chapter 13" in Chapter 2: the construction is here, and the arithmetic of \(\mathbb Q_p\) is Volume 13, Chapter 8.

**Missing.** A line of finite additivity before Kolmogorov's extension, if still absent. The case \(\mu^*(A_n)=\infty\) in the subadditivity of outer measure, if still absent.

## Links

**From Volume 6.** A deliberate change of register. The preface says what was borrowed and that it will now be proved.
**To Volume 8.** Everything. Volume 8 puts operators in these spaces and Haar measure on \(\mathbb Z_p\).
**To Volumes 11 and 12.** Conditional expectation, Prokhorov, Kolmogorov extension, Radon–Nikodym.
**To Volume 13.** \(\mathbb Q_p\) as a space.

## Size

About 7,100 source lines before the split, about 6,700 after. **Estimate, not measured:** 200–230 printed pages.

## Mathematical risks

1. Which problems of Chapter 13 truly need Volume 11. A problem that needs only "the Gauss measure is invariant", which is a change of variables, may stay if that is proved in the solution.
2. The divergence half of Khinchin's theorem without ergodic theory needs a quasi-independence estimate. Confirm the proof given is complete.
3. The Jordan curve theorem: the passage from polygons to general curves.
4. Kolmogorov's extension: the compactness argument that gives countable additivity.
5. The Hausdorff-measure citation.

## Acceptance requirements

- No citation of a later volume as a premise anywhere, including solutions.
- Verification records for: `thm:Qp` and its corollary, Fubini–Tonelli, change of variables, `thm:rn`, `thm:condexp`, `thm:tower`, `thm:prokhorov`, `thm:kolmogorov`, the Jordan curve theorem.
- The debts table in the preface agrees with the admitted-and-discharged ledger of the master plan.
- A list of the problems moved to Volume 11, in the PR that moves them.
- The ten editorial standards of the master plan, section 6.5.
