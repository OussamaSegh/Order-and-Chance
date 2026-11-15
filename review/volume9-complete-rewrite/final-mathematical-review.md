# Final mathematical review — author-directed assistant review

Reviewer: Codex, in a separate review phase after the complete rewrite. The
author's latest instruction is **“You review and merge.”** No other agent or
person performed this review. The plan's §6.4 says that the reviewer “is not the
writer”; the author's explicit direction supersedes that staffing rule. This
record therefore uses **CHECKED — AUTHOR-DIRECTED ASSISTANT REVIEW**, never the
plan's independent **VERIFIED** designation.

Book sources: `fb4502e3acda521b598c5bc3cd5e46e2f0e028d0`.

## Scope and evidence

The comparison starts at `9cd86c15bd386d59e7a1c6f96fb0ea5ed808c26b`.
Every one of the 302 original numbered formal statements was compared side by
side with its rewrite, including unlabelled definitions and examples. This
comparison found R15 and R16: two short wording changes had lost a necessary
qualification and a stronger conclusion. Both are restored in `2c0fccc8`.

The complete post-draft source pass covered all 22 units and all 288 original
and added exercise/hint/solution sets. Its actual unit-specific proof checks,
including empty, zero-dimensional, degenerate and boundary cases, are recorded
in [the full-source audit](postrewrite-writer-audit.md). The final comparison
also rechecked the Jordan–Brouwer nested-cube argument, invariance of domain,
the projective-space transfer at top degree, odd degree and ham-sandwich null
cases directly in their complete source proofs.

[The statement review](final-statement-review.json) gives the original and
reviewed statement, explicit premise labels, a following proof when present,
the matching-hypothesis check, boundary/constant records, standard reading
sources, status, correcting unit commit and the absence of a second reader.
Unit notes contain the concrete checks; extracted labels are reading aids,
not a claim that a parser can certify mathematical dependencies. Sources listed
in the book remain accurate bibliographic records. No newly consulted page or
unseen reference is invented by this review.

## Findings from the final statement comparison

| ID | Finding | Repair in `2c0fccc8` |
| --- | --- | --- |
| R15 | Definition 3.7 says pairwise compatible charts; ordinary smooth compatibility permits negative Jacobians and does not define orientation. | Restore **orientation-compatible** in the definition and its use in the volume-form proof. |
| R16 | Lemma 5.22(b) says a tree retracts to a vertex; the original valid conclusion is the stronger deformation retraction. | Restore **deformation retracts**; the leaf-collapse proof already proves it. |
| R17 | Some hypotheses rely on an adjacent paragraph although the baseline repeats them. | Name the covering in Proposition 5.11, chain complexes in Lemma 6.2, abelian groups in Lemma 6.3 and the finite-field curve in Proposition G.8. Preserve all contextual assumptions. |
| R18 | Euler's and Descartes' polyhedral formulas need a bounded full-dimensional polyhedron. A half-space, for example, is a convex polyhedron under the broader definition and does not satisfy the displayed formulas. | Define the bounded convention locally and repeat boundedness in Theorems K.6–K.7 and the two counting exercises. |
| R19 | The new Hesse caption should explicitly specify complex parameters and restrict flex language to smooth members. | Clarify the field and split the shared-basepoint sentence from the smooth-member flex conclusion (`21ca4d5a`). |
| R20 | Example 1.13 and Corollary J.8 use conclusions of exercises printed later. | Supply the implicit-curve obstruction at the Cassini crossing and the polygon parallel-area/fixed-epsilon squeeze before use (`fb4502e3`). |

Earlier findings R01–R14 and the initial substantive mathematical corrections
are tracked in [the findings register](postrewrite-review-findings.md) and
[the unit and fixing-commit index](delivery-review-index.md). A false baseline
claim is corrected explicitly rather than silently replaced by a weaker
theorem. Examples include infinite-component de Rham H0, Ptolemy coincidences,
the equilateral Feuerbach exception, dimensional endpoints, and local
Gauss-map area at zero curvature.

## Prerequisites and scope of proved results

The printed order remains the order in `main.tex`. Local proofs replace uses
of later material: contraction and smooth flow regularity; boundary bumps and
one-dimensional boundary signs; the Gauss lemma and Morse existence before
Euler characteristic; bouquet and graph arguments before homology; polar
coordinates before later Lie-group applications; joint incidence measurability
and the local isoperimetric step; and the spherical cosine-law estimate in
Appendix I. The Volume 15 SU2 density citation is corrected in the same PR to
Volume 9, Example 8.5.

Strong Whitney, classification/genus constructions, general de Rham,
rectifiable/kinematic extensions, the full exceptional-point elliptic group law
and other advanced statements retain their quoted or preview status where
their full proofs are outside the taught prerequisites. In particular, the
proved cubic associativity theorem retains its nine-distinct-point hypothesis.
Numerical illustration scripts supply no proof status.

## Production validation

Source review is complete after the listed repairs. Both final source builds,
rendered-page checks and EPUB checks pass, as documented from actual commands
in [final-validation.md](final-validation.md). The named Weyl and Poncelet proofs
follow their preparatory lemmas: those lemmas are proved before use and do not
use the theorem they prepare. All 245 proved formal statements have their full
proofs recorded in the statement review, including those named proofs.
There is no independent second-reader certificate. No Amazon KDP upload is
part of this work.
