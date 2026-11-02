# Volume 1 — high-school-entry prerequisite audit
2 November 2026 | `volume1-first-principles`

## Scope and standard

The **foundations route** must start from secondary-school algebra and elementary geometry, plus the starting assumptions explicitly listed in the preface. Readers should not be required to know proof-writing, group theory, abstract algebra, linear algebra, calculus, probability or set theory before meeting their definitions in Volume 1. Advanced problems can use later tools **only when the dependency is clearly signposted and the problem is optional**. The difficulty level is not itself a prerequisite warning.

This pass audited the actual chapter order in `main.tex`, first use of technical terms in the main exposition, and references/dependencies in **all 192 exercise statements and their solutions**. It is an editorial dependency and structural audit, **not** a new independent line-by-line mathematical verification of all proofs or a KDP preview.

## Results in reading order

| Place | Finding | Disposition |
|---|---|---|
| Ch. 0, Language of Mathematics | Logic, quantifiers, functions, equivalence and order are explicitly introduced. Future uses of the intermediate-value theorem are identified as later material. | No prerequisite edit |
| Ch. 1, Sums and induction | Formal sums, induction, binomial coefficients and elementary divisibility are built. The optional bilinear-sum exercise already names its later Cauchy–Schwarz prerequisite. | No prerequisite edit |
| Ch. 2, Counting | Counting rules, permutations, inclusion–exclusion and generating functions are explained. The Erdős–Szekeres exercise is solved with pigeonhole, not future Dilworth theory; that later reference is only a consequence. | No prerequisite edit |
| Ch. 3, Sequences and limits | Limits, completeness, derivatives on an interval, continuity and series are introduced. An elementary description of fields occurs late in a clearly optional polynomial reminder, which cannot be the sole foundation for required later chapters. | Definition repeated where needed |
| Ch. 4, Orders | Used *ordered field* before the required field definition. Later illustrated the lattice of vector subspaces before vector spaces/subspaces are introduced. | Replace the first with a direct sign-rule argument; label and explain the second as a preview of Ch. 7 |
| Ch. 5, Complex numbers | Asserted “C is a field” without local axioms. Also invoked Hermitian orthogonality and a Fourier basis before linear algebra. | Define field before computing reciprocals; give Q/R/Z examples; define the finite sum for orthogonality and explicitly label Fourier vectors as a later-chapter preview |
| Ch. 6, Polynomials | Uses the two-element field in the explanation of formal polynomials, though the only prior construction was in an optional reminder. | Construct F_2 by explicit arithmetic modulo 2 before the illustrative example |
| Ch. 7, Linear algebra | Defines vector spaces, bases, maps and matrices before required use. Cayley–Hamilton proof invoked an undefined *commutative ring* when extending the adjugate identity to polynomial entries. A covariance-matrix preview came before the probability definition. | Give the actual polynomial-algebra reason rather than assuming ring vocabulary; explain and label covariance as a preview |
| Ch. 8, Calculus | Builds derivative rules, integration toolkit, Taylor/Wallis/Gamma after the explicit calculus assumptions from the preface. | No new prerequisite edit |
| Ch. 9, Inequalities | Convexity, means and inequality tools are derived in the text; higher-level connections are downstream. | No new prerequisite edit |
| Ch. 10, Probability | Starts with finite outcome spaces and definitions for conditioning, expectation, variance and covariance. Several late challenges rely on the crossing lemma, matrix-tree theorem or a supplied tree-function identity from later mathematics. | Label these as optional advanced bridges and state external premises; explicitly mark the dependency chain |

## Individual exercise corrections

- **Linear algebra, `pb:tanroots`**: one-star designation obscured an asymptotic/Taylor prerequisite. Change to two stars and explicitly split accessible part (a) from the later-calculus parts (b)–(c).
- **Complex numbers, `ex:cardano`**: the solution cites future Viète formulas only as an additional check; state that the exercise itself needs only the complex arithmetic already taught.
- **Polynomials, `pb:bellasym`**: assumes Dobiński's formula, proved in Volume 5. Label the problem as an optional advanced bridge and state that the formula is a supplied premise.
- **Probability, `pb:szemereditrotter`**: assumes the crossing lemma from Volume 4. It is now explicitly an optional advanced bridge and the lemma is given rather than silently presumed proved.
- **Probability, `pb:sumproduct`**: solution depends on `pb:szemereditrotter` and hence Volume 4's crossing lemma. Mark the dependency in the question.
- **Probability, `pb:treebound`**: requires Kirchhoff's matrix-tree theorem from Volume 12. Mark optional, state its needed formula, and define graph Laplacian/adjacency/degree terms so the statement can be understood without prior graph spectral theory.
- **Probability, `pb:parking`**: later parts take the tree-function identity as given. Mark optional and distinguish earlier counting parts from later asymptotics.
- **Probability, `pb:sinesecond`**: depends on Taylor expansions from Chapter 8. Mark an optional return-after-calculus bridge.

## Structural and dependency checks after edits

Scanned the 11 main chapter sources plus the preface, field guide and image credits **on this PR branch**:

- **192 exercises, 192 hints and 192 solutions**, counts equal in each chapter.
- **452 distinct source labels** and **945 local \ref/\eqref/\pageref/\autoref/\cref occurrences**; no duplicate labels or unresolved local references.
- Balanced counts of standard LaTeX begin/end environments in all eleven main chapters.
- No chapter reorder, exercise deletion, theorem renumbering or source figure change.
- Targeted scan confirms no remaining main-text *ordered field* or *commutative ring* wording in the affected chapters.
- Every explicit forward reference found in an exercise statement was a marked future tool, or the exercise's problem required no future theorem; problematic unmarked dependencies from the solutions were corrected above.

## Honest limits and release gate

This is a source-first review; a static reference scan cannot prove there are no implicit conceptual gaps in every sentence, and the existence of a complete solution is not a certificate of mathematical correctness. Advanced optional problems remain genuinely advanced and are **not** expected to be solvable by a high-school reader on a first pass. They must not be required by subsequent main-text proofs.

Run the full Volume 1 PDF/EPUB production workflow for the final PR head, and inspect output layout after the new text changes. Keep the first-edition Git tag pending the current KDP publication gate, including ISBN association and publisher-side Print/Kindle Previewer checks.
