# Volume 13 — Arithmetic

*From Equations to Hidden Worlds.*

**Status of this file.** Blueprint of Volume 13 under the [master plan](MASTER-PLAN-V5-V15.md), 2026-11-10. It replaces the earlier specification, which described fourteen chapters; the manuscript prints eighteen. Chapter numbers below are the numbers after decision D-24 is applied; Chapters 1–17 keep the numbers they have today. No proof named here has been verified.

**Series part.** V. Number. **Directory.** `volume13-arithmetic`.

## Central question

What arithmetic was hidden inside the integers? An equation that cannot be solved in \(\mathbb Z\) opens a larger world: a number field, a completion, the adèles, a curve. Each chapter starts from one equation.

## Prerequisites

| From | What is used |
| --- | --- |
| Volume 2 | Quadratic reciprocity, sums of squares, continued fractions and Pell, Gaussian integers |
| Volume 3 | Galois theory, finite fields, modules over a principal ideal domain, characters |
| Volume 5 | Poisson summation, the Gamma function, the functional equation of \(\zeta\), residues |
| Volume 6 | Dirichlet \(L\)-functions and \(L(1,\chi)\ne0\), partial summation, the fundamental domain and the first modular forms |
| Volume 7 | \(\mathbb Q_p\) as a complete, locally compact field (Chapter 2); measure and Fubini |
| Volume 8 | Haar measure, self-duality and Fourier inversion on \(\mathbb Q_p\) (Chapter 13); Fourier analysis on finite abelian groups |
| Volume 10 | Unique factorisation of ideals in a Dedekind domain; integral closure; the fundamental identity; Hilbert 90 |

No statement of Volumes 14–15 is used.

## Structure

| Ch. | Title | File | Action |
| --- | --- | --- | --- |
| | **Part I. Number Fields** | | |
| 1 | Quadratic Fields and Their Integers | `ch11-algebraic.tex` | Keep |
| 2 | Ideals, Prime Splitting and Class Groups | `ch12-ideals-quadratic.tex` | Keep. Title gains "in Quadratic Fields". Its factorisation proof is headed a second proof |
| 3 | Number Fields and Their Integers | `ch01-number-fields.tex` | Keep |
| 4 | Ideals and the Splitting of Primes | `ch02-ideals.tex` | Consolidate: cite Volume 10 (D-22) |
| 5 | The Geometry of Numbers | `ch03-geometry.tex` | Keep |
| 6 | Units | `ch04-units.tex` | Keep |
| 7 | Cyclotomic Fields and Fermat | `ch05-cyclotomic.tex`, with `polyfermat.tex` as its last section | Absorbs the short chapter |
| | **Part II. Local and Global** | | |
| 8 | The \(p\)-adic Numbers | `ch12-padic.tex` | Keep. Cites Volume 7 for the construction |
| 9 | Local Fields | `ch06-local.tex` | Keep |
| 10 | Quadratic Forms and the Local–Global Principle | `ch07-hasse.tex` | Keep |
| 11 | Zeta Functions and Densities | `ch08-zeta.tex` | Keep; one heading |
| | **Part III. Adèles and Tate's Thesis** | | |
| 12 | Adèles, Idèles and Tate's Thesis | `ch09-tate.tex` | Consolidate: cite Volume 8 (D-23) |
| 13 | Class Field Theory | `ch10-cft.tex` | Keep |
| | **Part IV. Elliptic Curves and Modular Forms** | | |
| 14 | Algebraic Curves | `ch11-curves.tex` | Keep; Goppa codes become an exercise |
| 15 | Elliptic Curves | `ch12-elliptic.tex` | Keep |
| 16 | Curves over Finite Fields | `ch13-finite.tex` | Keep |
| 17 | Modular Forms and \(L\)-functions | `ch14-modular.tex` | Keep; cites Volume 6 for the fundamental domain |

**Why two quadratic chapters stay.** They are the worked case: every idea of Part I appears first where it can be computed by hand. Merging them into the general chapters would save pages and lose the volume's opening.

## Flagship theorems, proved in this volume

| Theorem | Label | Chapter |
| --- | --- | --- |
| Integers of a quadratic field; ideals factor uniquely in a quadratic field, by Hurwitz's norm lemma (second proof); splitting of primes; finiteness of the class group | `thm:dedekind`, `thm:split`, `thm:classfinite` | 1–2 |
| Integral bases; discriminant; Stickelberger | | 3 |
| \(\mathcal O_K\) is Noetherian; unique factorisation of ideals, deduced from Volume 10; the Kummer–Dedekind theorem; splitting in cyclotomic fields | `prop:noeth`, `thm:ufi`, `thm:kd` | 4 |
| Minkowski's convex body theorem and bound; Hermite's finiteness theorem | | 5 |
| Dirichlet's unit theorem | | 6 |
| Kummer's lemma; the first case of Fermat for regular primes; Mason–Stothers and Fermat for polynomials | | 7 |
| Hensel's lemma; squares in \(\mathbb Q_p\); Ostrowski | | 8 |
| The product formula; unramified and Eisenstein extensions | | 9 |
| Hilbert reciprocity; Hasse–Minkowski; Legendre's theorem; sums of three squares | `thm:hm`, `thm:threesq` | 10 |
| The analytic class number formula; Kummer's criterion; Dirichlet's theorem over a number field; Chebotarev in Dirichlet density | `thm:cnf`, `thm:kummercrit`, `thm:dirichletF`, `thm:chebotarev` | 11 |
| Adelic Poisson summation; Tate's thesis for \(\mathbb Q\); the functional equation of primitive Dirichlet \(L\)-functions; Fujisaki's lemma, and from it second proofs of class number finiteness and the unit theorem | `thm:adelicpoisson`, `thm:tate`, `cor:dirichletFE`, `thm:fujisaki` | 12 |
| Kronecker–Weber; class field theory over \(\mathbb Q\); cubic reciprocity | `thm:kw` | 13 |
| Bézout; Noether's \(AF+BG\); Riemann–Roch for smooth plane curves | `thm:bezout`, `thm:rr` | 14 |
| The group law; Nagell–Lutz; Mordell's theorem | `thm:grouplaw`, `thm:mordell` | 15 |
| Rationality and functional equation of the zeta function of a curve; Stepanov–Bombieri; Hasse's bound | `thm:bombieri`, `cor:hasse` | 16 |
| The valence formula; Hecke operators; Hecke's functional equation for the \(L\)-function of a cusp form | | 17 |

## Stated without proof

The list is fixed by decision D-25. Each item's heading carries the word shown.

| Statement | Heading must say |
| --- | --- |
| Artin reciprocity; the existence theorem; the Hilbert class field (`thm:artin`, `thm:cftexistence`, `thm:hcf`) | Admitted, not proved in this series |
| Primes of the form \(x^2+ny^2\) in general (`thm:xnyy`) | Assuming the Hilbert class field |
| Functional equation of \(\zeta_K\) for a general number field | Sketch |
| Chebotarev in natural density | Not proved. Dirichlet density is proved |
| Weil's bound for a general curve; modularity; Mazur's torsion theorem; Sato–Tate | Quoted |
| The second case of Fermat for regular primes | Quoted |
| Canonical heights as a quadratic form; general Selmer groups | Named, not developed |
| The three-cubes heuristic | Heuristic |

## Climax

Chapter 12. Riemann proved the functional equation by Poisson summation on the line. Tate proves it by Poisson summation on the adèles, and the same proof gives every Dirichlet \(L\)-function, which pays the debt Volume 6 left. Part IV has its own summit in Mordell's theorem.

## Motivation and history

Fermat and Euler on \(x^2+ny^2\), Kummer's ideal numbers and Lamé's failed proof, Dedekind, Minkowski, Hensel, Hasse, Tate's 1950 thesis, Kronecker's Jugendtraum, Mordell and Weil, Hasse's 1933 theorem, Hecke, Ramanujan. Each sourced.

## Examples and exercises

\(6=2\cdot3=(1+\sqrt{-5})(1-\sqrt{-5})\) carried from Chapter 1 to Chapter 13. Class groups computed for small discriminants. \(x^2-61y^2=1\). The seven quadratic extensions of \(\mathbb Q_2\). \(2x^2+7y^2=3z^2\). \(p=x^2+27y^2\). Two complete 2-descents. Point counts on \(y^2+y=x^3-x^2\) against the coefficients of \(\eta(\tau)^2\eta(11\tau)^2\).

Seven to twelve exercises per chapter at three levels. Chapter 8 receives from Volume 8 the exercise on the Haar measure of the squares in \(\mathbb Z_p\).

## Figures and experiments

Lattices of rings of integers; the tree of \(\mathbb Z_p\); real points of cubics; point counts against Hasse's interval. Class number tables and point counts are produced by scripts in the repository and listed in the ledger.

## Changes from the current manuscript

**Preserve.** All chapters except the short last one, in their order.

**Consolidate.** Chapter 4: `thm:ufi` is deduced in a few lines from Volume 10, `thm:dedekind` and `thm:intclosure`, with `prop:noeth` kept. Its present long proof is removed after the equivalence table is filed. Chapter 12: the construction of Haar measure on \(\mathbb Q_p\) (`prop:haarQp`) and the local self-duality are replaced by citations of Volume 8, unless the comparison finds a different normalisation, in which case one normalising lemma stays.

**Relocate.** `polyfermat.tex` into Chapter 7 as its closing section.

**Rewrite.** Chapter 17's fundamental-domain theorem cites Volume 6. Chapter 8 opens by citing Volume 7 for the construction and goes straight to Hensel.

**Remove.** Goppa codes as a numbered theorem (kept as an exercise). Any attribution of the bound \(\lvert c_p\rvert\le2\sqrt p\) for a modular form to the curve's Riemann hypothesis without the modularity statement beside it.

**Missing.** In the heading of Mordell's theorem, which half is proved in general and which under a hypothesis on 2-torsion, after inspection. One paragraph in the preface linking the end of Volume 12 to this volume.

## Links

**From Volume 12.** The zeros of \(\zeta\) were set beside a random spectrum. This volume shows \(\zeta\) is one of a family.
**From Volumes 7, 8, 10.** Completion, local harmonic analysis, Dedekind domains: cited, not rebuilt.
**To Volume 14.** Class numbers and \(L(1,\chi)\) for Siegel's theorem; Chebotarev; the functional equation of \(L(s,\chi)\).
**To Volume 15.** Class groups, one 2-descent, the class number formula, point counts: the arithmetic whose statistics Volume 15 studies.
**Back to Volume 6.** `cor:dirichletFE` discharges the admitted functional equation.

## Size

About 11,440 source lines today; about 11,000 after consolidation. **Estimate, not measured:** 320–350 printed pages. The earlier target of 250–270 pages described a shorter manuscript and is withdrawn.

## Mathematical risks

1. Removing the long proof of `thm:ufi` may remove lemmas that later chapters cite (`lem:missing` and others). The equivalence table lists every label cited elsewhere before anything is deleted.
2. Normalisation of measures and characters between Volume 8 and Chapter 12. A factor here changes the functional equation.
3. Tate's thesis: convergence and the interchange in the global zeta integral.
4. Mordell's theorem: the height inequality and the weak theorem's scope.
5. Chebotarev: the reduction to the cyclotomic case.
6. Stepanov–Bombieri: the construction of the auxiliary function.
7. Three squares: the 2-adic step, repaired once.
8. `thm:xnyy` depends on an admitted theorem; no later result may use it as proved.

## Acceptance requirements

- Structure equals the table above; Chapters 1–17 keep today's numbers.
- No premise from Volumes 14–15. Volumes 7, 8 and 10 are cited where this plan says.
- Equivalence tables for D-22 and D-23 filed before the consolidating pull requests.
- Verification records for every label in the flagship table, Chapters 4, 11, 12 and 15 first.
- Every item of the "without proof" table carries its heading; the preface's claim about what is proved matches the table.
- The ten editorial standards of the master plan, section 6.5.
