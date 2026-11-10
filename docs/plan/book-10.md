# Volume 10 — Abstraction

*Categories, Algebra and Homology.*

**Status of this file.** Blueprint of Volume 10 under the [master plan](MASTER-PLAN-V5-V15.md), 2026-11-10. It replaces the earlier specification. No proof named here has been verified.

**Series part.** III. Analysis and Geometry. **Directory.** `volume10-abstraction`.

## Central question

What is the frame common to all the structures met so far? An object is known by the maps into it, a module by its presentations, a failure of exactness by a homology group.

## Prerequisites

| From | What is used |
| --- | --- |
| Volume 3 | Groups, rings, fields, modules over a principal ideal domain, characters of finite groups, Maschke |
| Volume 7 | Topology and measure, for compact groups |
| Volume 8 | Hilbert spaces and compact operators (for Peter–Weyl); Appendices A–E (for the Kronecker product chapter) |
| Volume 9 | Homology as the motivating example; the unitary group and Weyl's integration formula |

No statement of Volumes 11–15 is used as a premise. Mentions of Volume 13 in Chapter 6 are previews, except one example treated below.

## Structure

Unchanged.

| Ch. | Title | File | Action |
| --- | --- | --- | --- |
| | **Part I. Categories** | | |
| 1 | Categories | `ch01-categories.tex` | Keep |
| 2 | Tensors and the Cost of Multiplying Matrices | `linear-ch10-tensors.tex` | Keep |
| 3 | Tensors and Exactness | `ch02-tensors.tex` | Keep |
| | **Part II. Commutative Algebra** | | |
| 4 | Noetherian Rings and Hilbert's Theorems | `ch03-noetherian.tex` | Keep |
| 5 | Localisation and Dimension | `ch04-localisation.tex` | Keep |
| 6 | Dedekind Domains | `ch05-dedekind.tex` | Keep. Declared home of ideal factorisation (D-22) |
| 7 | Homological Algebra | `ch06-homological.tex` | Keep |
| | **Part III. Representations** | | |
| 8 | Group Cohomology | `ch07-groupcoh.tex` | Keep |
| 9 | Semisimple Algebras and Induction | `ch08-semisimple.tex` | Keep |
| 10 | The Symmetric Group | `ch09-symmetric.tex` | Keep |
| 11 | Compact Groups | `ch11-compact.tex` | Keep |

Chapter 2 treats tensors of vector spaces concretely (Kronecker products, Strassen's algorithm) and Chapter 3 treats tensors of modules. Each says in its first paragraph how it relates to the other.

## Flagship theorems, proved in this volume

| Theorem | Label | Chapter |
| --- | --- | --- |
| Yoneda's lemma; uniqueness of adjoints; right adjoints preserve limits | | 1 |
| Strassen's algorithm; Sylvester's equation | | 2 |
| The snake lemma; tensor–Hom adjunction; Baer's criterion | | 3 |
| Hilbert's basis theorem; the Nullstellensatz; Buchberger's criterion | | 4 |
| Nakayama; going up; Noether normalisation; primary decomposition (Lasker–Noether) | `thm:assprimes` | 5 |
| Discrete valuation rings; unique factorisation of ideals in a Dedekind domain; the integral closure of a Dedekind domain in a finite separable extension is Dedekind; the fundamental identity \(\sum e_if_i=n\) | `thm:dvr`, `thm:dedekind`, `thm:intclosure`, `thm:fundid` | 6 |
| Long exact sequences; universal coefficients for finitely generated free complexes over a principal ideal domain | | 7 |
| Hilbert's Theorem 90; Schur–Zassenhaus | | 8 |
| Wedderburn; Frobenius reciprocity; Mackey; Burnside's \(p^aq^b\) theorem | | 9 |
| Specht modules; Robinson–Schensted; the hook length formula; the character of a transposition | | 10 |
| Schur orthogonality; Peter–Weyl; Weyl's character formula for \(U(n)\); moments of traces of random unitary matrices | `thm:peterweyl`, `thm:weylchar`, `thm:traces` | 11 |

## Stated without proof

| Statement | Heading must say |
| --- | --- |
| Schur–Weyl duality | Stated, not proved |
| Spectral sequences; derived categories; schemes | One sentence each, as a pointer |
| Universal coefficients for singular chains | Not claimed: the theorem is for finitely generated free complexes |
| Bounds on the exponent of matrix multiplication beyond Strassen | Quoted, with date |

## Climax

Chapter 6 for Part II: in a Dedekind domain ideals factor uniquely, the theorem Volume 13 is built on. Chapter 11 for the volume: Peter–Weyl and Weyl's character formula, where the algebra of Part III meets the Haar measure of Volume 9.

## Motivation and history

Eilenberg and Mac Lane, Hilbert and Gordan's "theology", Emmy Noether's 1927 axioms, Dedekind and Kummer, Young and Frobenius, Weyl. Each attribution sourced; the Gordan quotation is cited to its actual source.

## Examples and exercises

Free groups, abelianisation and the double dual as adjunctions. \(\mathbb Z[\sqrt{-5}]\) as the running example of Chapter 6. Young diagrams for \(S_4\) and \(S_5\) computed in full. Six exercises per chapter at three levels; Chapter 2 has twelve.

## Figures and experiments

Commutative diagrams throughout. Young diagrams with hook lengths. No printed number depends on a computation.

## Changes from the current manuscript

**Preserve.** All eleven chapters in their order.

**Rewrite.** Chapter 6 says \(\mathbb Z[\sqrt{-5}]\) is Dedekind "by Volume 13, Chapter 4". Justify it by `thm:intclosure`, which is in this chapter. Other mentions of Volume 13 become previews with current chapter numbers by label.

**Label.** Schur–Weyl duality as stated only.

**Remove.** Nothing.

**Missing.** A sentence at the head of Chapter 6 saying that this is where the series proves unique factorisation of ideals, and that Volume 13 applies it to number fields. The inflation–restriction sequence in low degrees in Chapter 8, if it is still absent and if Volume 13's class field theory chapter states it; otherwise it stays out.

## Links

**From Volume 9.** Homology and the unitary group.
**To Volume 11.** The character of a transposition and the dimension formula, for the shuffling chapter.
**To Volume 12.** Peter–Weyl and the moments of traces, for the unitary ensemble.
**To Volume 13.** `thm:dedekind`, `thm:intclosure` and `thm:fundid`: Volume 13 cites them and does not reprove them (D-22). Hilbert 90, for Kummer theory.

## Size

About 4,880 source lines. **Estimate, not measured:** 140–160 printed pages. This is the shortest volume. It is dense, and nothing is added for length.

## Mathematical risks

1. `thm:dedekind` now carries Volume 13. Its hypotheses must match exactly what Volume 13 needs: Noetherian, integrally closed, dimension one.
2. `thm:intclosure`: separability is used; number fields have characteristic zero, so the hypothesis holds, and Volume 13 must say so.
3. Lasker–Noether: uniqueness statements.
4. Weyl's character formula: the passage from the integration formula of Volume 9 to orthogonality of the candidates.
5. Burnside's theorem: the algebraic-integer step.

## Acceptance requirements

- No premise from Volumes 11–15.
- Verification records for: Yoneda, the snake lemma, the Nullstellensatz, `thm:assprimes`, `thm:dvr`, `thm:dedekind`, `thm:intclosure`, `thm:fundid`, Hilbert 90, Wedderburn, the hook length formula, `thm:peterweyl`, `thm:weylchar`, `thm:traces`.
- The equivalence table with Volume 13's ideal theorems (master plan, PR 2.4) filed before Volume 13 changes.
- The ten editorial standards of the master plan, section 6.5.
