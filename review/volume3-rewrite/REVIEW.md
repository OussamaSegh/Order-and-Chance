# Volume 3: Critical editorial review and mathematical audit

**Work branch:** editorial/volume3-comprehensive-review-rewrite-20261102  
**Book:** Order and Chance — Volume 3: Symmetry — Groups, Rings and Fields  
**Audit date:** 2 November 2026  
**Contents:** 12 main chapters and 4 appendices.  
**Important status:** **This is a substantive editorial revision, not a certified complete rewrite or formal verification of all mathematics.** Many inherited proofs and exercise solutions remain intact and require a distinct line-by-line independent pass.

## Overall evaluation

The central arc is sound. Groups and actions (Chapters 1–5) build the machinery needed to explain parity, simple groups and solvability. Rings, modules and extensions (6–8) provide the algebraic language; finite fields (9) give an accessible application; Galois theory (10) answers a problem the reader has been preparing for. Character tables (11) and rotations (12) bring symmetry into matrices and geometry. The two summits are worth keeping: the obstruction to solving the quintic x^5−4x+2 by radicals and the identity 24=1²+1²+2²+3²+3² for irreducible representation degrees of the cube's rotation group.

The strongest part of this edition is its selection of mathematical examples and worked proofs. The weakest part was its teaching continuity. Some chapter openings led with historical claims rather than a small problem; transitions between definitions and theorems sometimes assumed too much of the reader; and the 13th chapter conflicted with the preface's twelve-chapter outline. The goal is to preserve rigor while letting the reader feel why each construction is necessary.

## Changes made in this branch

1. Rewrote the preface and back-cover copy around the quintic and the cube's representation degrees.
2. Rewrote opening teaching prose in all twelve main chapters and the four appendices, with small examples before abstract definitions.
3. Added connective explanations ahead of major internal sections throughout all twelve chapters.
4. Moved the Paley constructions into Appendix D, preserving the existing appendix designations A–C; corrected the title-page subtitle to agree with the catalogue and updated the book plan.
5. Added an afterword deriving a two-state random walk on Z/2Z and connecting finite-group Fourier ideas to Volume 4.
6. Added source figures for the kernel fibres of reduction modulo three and the graph of the quintic; retained appropriate existing figures.
7. Proved the necessary Hadamard order condition n>2 implies 4 divides n, and added graded exercises with hints and complete solutions, including the explicit 4×4 Paley matrix.
8. Corrected a QR-code error-correction statement, the ground field of a cyclotomic theorem, the Rubik-cube move convention, and the assumptions behind the Pohlig–Hellman statement.
9. Updated the Hadamard conjecture's 2026 status and corrected a cross-volume pointer in Volume 8. A primary arXiv study dated 19 October 2026 independently verifies constructions including the formerly unresolved order 668.

Each of these changes is isolated in reviewable small commits. These edits do **not** yet amount to a complete rewriting of every inherited proof, example or exercise.

## Detailed critical review

| Chapter | Strength | Risk or defect | Action and outstanding verification |
| --- | --- | --- | --- |
| 1. Groups as Symmetries | A visual route through dihedral and cube symmetries into Lagrange and cyclic groups | Historical opening obscured the mathematical hook; “20 moves” did not define the move metric | New square-to-cube narrative and transitions; 20 face-turn metric clarified. The small-group exercise solutions merit another independent pass. |
| 2. Morphisms and Quotients | Natural progression from kernel to normal subgroup to first isomorphism theorem | Cosets feel purely symbolic if the reader cannot see what is forgotten | New reduction modulo three example and fibre diagram; section bridges. Order-eight classification in the final solution remains to audit. |
| 3. Group Actions and Counting | Orbit–stabiliser and Burnside are connected by double counting | Naively dividing the 64 bead strings by six is incorrect because stabilisers differ | New six-bead explanation; independently checked 14 rotation classes. Check every diagram's colour/rotation convention. |
| 4. The Symmetric Group | Puzzle parity supplies a tangible obstruction; simplicity of A5 loads the later quintic proof | The rectangle-loop converse to the fifteen-puzzle theorem is long and coordinate-sensitive | Rewritten hook and bridges. The full rectangle enumeration and the entire A_n simplicity proof require separate independent scrutiny. |
| 5. Sylow Theorems | Good counting examples, especially order thirty | Unqualified Pohlig–Hellman claim was false for arbitrary groups | Restricted statement to finite cyclic groups with factored order. Recomputed allowable order-30 Sylow counts; the classifications of groups of orders pq, 8 and 12 need re-derivation. |
| 6. Rings and Ideals | Failure of unique factorisation of six in Z[sqrt(-5)] motivates ideals | Readers may confuse prime elements, irreducibles, prime ideals and maximal ideals | New mathematical hook and stepwise conceptual transitions. Gauss's lemma and UFD proofs remain on the priority audit list. |
| 7. Modules over a PID | Smith form unifies abelian-group classification and matrix normal forms | Multiple canonical forms can feel like separate theorems with no common motivation | New introduction computes six abelian groups of order 360; transitions foreground invariant factors. Check Jordan form and field-splitting assumptions. |
| 8. Field Extensions | Tower law makes ruler-and-compass impossibility accessible | The degree test for constructibility is a necessary obstruction, not a free-standing converse | New trisection via u=2cos20°, u³−3u−1=0. Primitive-element argument inspected under characteristic zero; full geometric-construction audit remains. |
| 9. Finite Fields | Excellent combination of Frobenius and Reed–Solomon coding | “Lose one third of the squares” was incorrect: QR correction thresholds concern codewords, not arbitrary covered printed modules | Fixed wording using QR designer's documentation; new F4 quotient example. Exhaustively computed distance five of the small six-symbol, two-coefficient code over F7. |
| 10. Galois Theory | A specific quintic makes the abstraction worthwhile; fundamental theorem gives the payoff | Cyclotomic extension was quantified over arbitrary fields although the selected roots of unity live inside C; the radical-tower argument is demanding | Restricted K to a subfield of C; refined polygon statement; added real-roots graph. Galois-group argument independently checked in its main steps. Full audit of both radical-solvability directions remains. |
| 11. Representations and Characters | Character tables make hidden group structure computational | Beginning with matrices/traces alone risks losing readers before the orthogonality relations | New S3 and S4 representation-degree hook and Fourier bridge. Verify every S4 and A5 table entry by independent exact arithmetic. |
| 12. Quaternions and Rotations | Concrete rotation interpretation closes the volume and connects A4, S4, A5 | Finite-subgroup classification proof is long, with delicate stabiliser and conjugacy counts | New non-commuting-rotations opening. The poles proof structure was inspected; every step needs independent mathematical sign-off. |

## Appendices

**A — Positive Matrices.** A strong advanced connection to Markov chains and spectra. The new introduction distinguishes strictly positive from merely non-negative matrices. Audit primitivity, irreducibility, periodicity and eigenvalue multiplicity assumptions.

**B — Symmetry Diagonalises.** Circulants and characters give an excellent demonstration that a symmetry may supply a common eigenbasis. The new opening starts with a shifted row and Fourier vectors. Review the Delsarte bound, Paley graph computations and group determinant independently.

**C — The Linear Algebra Method.** Oddtown is an ideal introductory example; the new opening includes the F2 dot-product proof. The polynomial-method and cap-set arguments deserve independent checking rather than being assumed correct from Oddtown.

**D — Hadamard Matrices from Finite Fields.** Paley's constructions fit as a specialist application after finite fields. The new obstruction proof, q=3 example, exercises and solutions improve self-containment. The general Hadamard conjecture remains open, although independent work in October 2026 verified the August 2026 constructions for the previously unresolved orders below 2000.

## Numerical and mathematical verification ledger

**Independently checked by finite enumeration, exact rational arithmetic or direct calculation:**

- Six binary beads up to rotation: 14 classes; fixed-word counts over the six rotations are 64, 2, 4, 8, 4, 2.
- Cube's orientation-preserving signed-coordinate permutations: exactly 24.
- Sylow counts at order 30: n_5 is 1 or 6; n_3 is 1 or 10. If both counts were larger, disjoint prime-order subgroup contributions would exceed the group.
- Number of abelian groups of order 360 up to isomorphism: p(3)p(2)p(1)=3×2×1=6.
- Quintic: f(-2)=-22, f(0)=2, f(1)=-1, f(2)=26; three real roots approximately −1.51851215, 0.50849948, 1.24359639; two non-real roots form a conjugate pair.
- Reed–Solomon evaluation code from linear polynomials over F7 at positions 1 through 6: exactly 49 codewords, minimum distance 5.
- Two-state random walk in the afterword: u_t=(1+(1−2p)^t)/2 agrees with the recurrence for p=0, 1/4, 1/2, 3/4, 1 over twenty steps.
- Paley I for q=3: 4×4 sign matrix has HHᵀ=4I. Paley II for q=5: 12×12 sign matrix has HHᵀ=12I.

**Proofs inspected for overall structure, but NOT fully formally verified:** quotient and isomorphism theorem, fifteen-puzzle parity argument, primitive-element theorem over complex subfields, Berlekamp–Welch decoding, cyclotomic degree/construction argument, quintic Galois group, Paley constructions, and finite rotation group classification.

**Static manuscript scan:** after the main editorial edits, the included sources had no duplicate theorem labels, no unresolved internal reference targets, and no unmatched counts of common LaTeX proof, exercise, solution or figure environments. The manuscript used 22 source figure references, including the two additions. A repeatable script has been committed at **review/volume3-rewrite/check_volume3.py**.

**Not yet verified:** all proofs word by word, all hints and exercise solutions, every historical attribution and bibliography item, all external cross-volume references, full XeLaTeX typography and EPUB rendering. It would be inaccurate to say the entire volume is mathematically certified.

## Independently checked external sources

- **Rubik's cube:** T. Rokicki, H. Kociemba, M. Davidson and J. Dethridge, *The Diameter of the Rubik's Cube Group Is Twenty*, SIAM J. Discrete Math. 27 (2013), 1082–1105. https://doi.org/10.1137/120867366
- **QR error correction:** DENSO WAVE, *Error Correction Feature*, percentages measured by total codewords; level H approximately 30%. https://www.qrcode.com/en/about/error_correction.html
- **Quintic:** F. Gotti, Algebra 1 lecture notes (exercise on x^5−4x+2) as an independent comparison for the irreducibility and Galois group reasoning. https://math.mit.edu/~fgotti/docs/Courses/Algebra%201/Algebra%201.pdf
- **Hadamard updates:** R. Egan, I. Kotsireas, S. London, P. Ó Catháin, *Recent progress in the construction of Hadamard matrices*, arXiv:2610.27175 (19 October 2026). https://arxiv.org/abs/2610.27175

The list is targeted fact verification, not a comprehensive bibliography audit.

## Sign-off criteria still outstanding

1. **Build and visual QA.** Compile Volume 3 with the repository's real XeLaTeX toolchain, check all figures and page breaks, and validate EPUB/phone layouts. Run the committed checker. The connected GitHub interface cannot execute the repository's build environment directly.
2. **Full mathematical proof audit.** Give every proof and exercise a verification result recording hypotheses, computations, implications, equality cases, and prior theorems. Prioritise the fifteen-puzzle converse, the A_n simplicity proof, PID structure and Jordan form, radical solvability, character tables, polyhedral rotation classification, and the polynomial method.
3. **Full body rewrite.** The chapter and appendix openings and internal transitions are rewritten, but much inherited main-body theorem prose, examples and solutions have not yet been independently rewritten. Finish this section by section while preserving numbered references and complete worked solutions.
4. **References and second reader.** Audit all bibliographic details and cross-volume claims; compare the compiled book against the canonical style and prerequisites; use an independent critical reader on the final version.

**Conclusion:** The current branch materially improves the pedagogical arc and fixes substantive errors, but it is **not a finished, fully rewritten and multiply verified Volume 3**. That status must remain explicit until the remaining sign-off criteria have been met.


## Second pass: volume continuity and full proof rewrites (2 November 2026)

A further editorial pass made these changes in addition to the initial audit:

- Read the actual main.tex chapter order of Volumes 1 and 2 instead of inferring it from filenames. The first volume currently contains The Language of Mathematics (1), Sums (2), Counting (3), Sequences (4), Orders (5), Complex Numbers (6), Polynomials (7), Linear Algebra (8), Calculus (9), Inequalities (10) and Probability (11). Corrected the old Volume 3 pointers to these subjects, including references to polynomials, roots of unity, linear algebra, calculus and Fibonacci proofs. Replaced two brittle numeric citations with topical references.
- Re-read the end of Volume 2, including its Dirichlet-character chapter and field guide, and introduced an explicit conceptual bridge from its unit groups and characters to the homomorphisms of Volume 3.
- Rewrote the complete proofs of Lagrange's theorem, the first isomorphism theorem, Burnside's lemma, Sylow I, Gauss's lemma, the tower law, Berlekamp--Welch decoding, the quintic Galois-group argument, Maschke's theorem, and the quaternion double-cover theorem. Each rewritten proof makes its assumptions, constructions and logical steps explicit.
- Added 28 substantive proof explanations across twelve main chapters and four appendices. They have numerical examples and assumptions rather than stock summaries.
- Verified that all **163 graded exercises** have a corresponding hint and a solution with both a discovery idea and a write-up. Added this requirement to the regression script. This checks the presence of solutions, NOT their mathematical correctness.
- Expanded reproducible checks: enumerate the 60 elements of A5 and their conjugacy classes (sizes 1, 12, 12, 15, 20), verify all row and column orthogonality identities for the S4 character table, build F4 and test the Frobenius/inverses, check the fifteen-puzzle parity invariant under hundreds of legal moves, verify every specific rectangle-loop growth step in its converse, and test quaternion norm multiplicativity. Earlier checks for necklaces, cube rotations, Sylow arithmetic, the quintic's real roots, Reed--Solomon distance and the two-state walk remain.
- Preserved all existing theorem and exercise labels. GitHub Actions executes the enlarged audit before the book builds.

### Second-pass limitations

These edits are substantial, but the entire inherited mathematical body has **not** yet been rewritten word for word. Most of the original remaining theorem proofs and 151 of the 163 exercise solutions remain inherited; 12 have been fully rewritten and checked in the third pass. Numerical checks cannot certify all the logic in those proofs. An independent line-by-line mathematical sign-off, source and bibliography audit, complete editorial voice review, and final visual PDF/EPUB inspection are still outstanding. PR #91 must remain a draft until these criteria are actually fulfilled.


## Third pass: full worked solutions and structural proof audit (2 November 2026)

This continuation includes **12 complete rewrites of graded exercise solutions**, one in each main chapter, with the original labels, discovery ideas and full write-ups retained. The selected worked examples cover:

1. Order-four group classification: corrected the previous mismatch between a request for **two geometric examples** and a non-geometric unit-group answer. Now gives both rectangle symmetries and the coordinate-axis half-turn group.
2. Automorphisms of a cyclic group: full proof that every endomorphism is multiplication by one residue, and that it is an automorphism precisely for a unit.
3. Cube face colourings: full five-row rotation inventory and Burnside calculation giving 57.
4. Landau maximum orders in S7 and S10: justified the prime-power budget reduction and enumerated the maximal choices, giving 12 and 30.
5. Groups of orders 56, 200 and 36: separate Sylow counts, forced normal subgroups, and a nontrivial action kernel.
6. The nonprincipal maximal ideal in Z[sqrt(-5)]: norm obstruction, explicit quotient map to F2, and an irreducible-but-not-prime element.
7. All six abelian groups of order 360: elementary divisors, invariant factors and one full Chinese-remainder reconstruction.
8. Constructible 7-, 9- and 17-gons: irreducible cubic obstructions and the exact degree-eight calculation, with the degree bound clearly described as necessary rather than sufficient.
9. All irreducible polynomials of degree at most four over F2: explicit tests in the quadratic quotient and factorisation of X^16-X.
10. The intermediate fields of Q(zeta7): exact subgroup listing and the nine-term Gauss-period product identifying Q(sqrt(-7)).
11. The six-point permutation representation of S4: fixed-pair counts, character inner products and a dimensional check.
12. The quaternion-to-rotation matrix: derived the vector formula and checked all three columns and the trace.

**Further complete theorem-proof rewrites:** Smith normal form (including strict termination of the pivot algorithm and uniqueness from ideals of minors), Sylow II–III (all coset, normaliser, congruence steps), finite-field existence and uniqueness via X^q-X, and the fundamental theorem of Galois theory (including both directions of the normality criterion). In Artin's fixed-field lemma the previously implicit separability justification for using the primitive element theorem is now explicit.

**New exact test coverage** in the integrated Python checker: exhaustive partition searches for maximum element order in S7 and S10, enumeration of all 729 three-colour cube-face assignments under the full rotation group, enumeration and irreducibility testing of all monic F2 polynomials through degree four and reconstruction of X^16-X, exact seven-th cyclotomic-period exponent counts, and exact quaternion-matrix products. These checks are **evidence for the audited examples**, not machine proofs of the general theorems.

**Still outstanding:** 151 inherited graded solution write-ups, much of the remaining general exposition and theorem proof body, full independent formal scrutiny of all claims and bibliography, and final visual PDF/EPUB page-by-page QA. PR remains draft; no claim of a finished volume is justified at this stage.
