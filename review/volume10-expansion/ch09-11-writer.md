# Chapters 9–11 teaching expansion: writer record

Base: current main `b005c4a0a33409f443594f3bb1efe3e955e95468`.
Branch: `codex/volume10-teaching-expansion`.
Scope: only `chapters/ch08-semisimple.tex`, `ch09-symmetric.tex`, `ch11-compact.tex` and this record. The current immutable inventory is `review/volume10-expansion/starting-source.json`; it records ten exercises and three figures in each assigned chapter. The printed order was read from `main.tex`. The root agent owns changes to the main file, reading route, covers and final production.

## Additions

Exactly two substantial worked examples per chapter carry `% V10-EXPANSION WORKED EXAMPLE 1` and `2`. They use unnumbered subsection headings and no formal numbered environment. Four exercises per chapter are appended after all ten current exercises, followed by four appended hints and four complete idea/writeup solutions. The star distribution in each chapter is one basic, two intermediate, one advanced. No figures are added or altered.

### Chapter 9

Worked examples:

1. Inducing the nontrivial character of a transposition subgroup of S3. Exact three-coset matrices give sign plus standard; restriction and Frobenius reciprocity check both multiplicities.
2. The six two-element subsets of four points. Three double cosets have sizes 4,16,4; the permutation character decomposes as 1 plus standard plus the two-dimensional representation. Intersection size explains the failure of double transitivity.

Exercises:

- `ex:v10exp-ch09-restriction` — basic calculation of standard restriction to C3 and induction of its three characters.
- `ex:v10exp-ch09-faithfulind` — intermediate counterexample: a faithful character of C2 induces faithfully but reducibly to C4; explicit matrix and Mackey obstruction.
- `ex:v10exp-ch09-orderedpairs` — intermediate application: ordered distinct pairs for S4, character multiplicities 1,0,2,1,1 and seven stabiliser orbits.
- `ex:v10exp-ch09-commutant` — advanced conceptual calculation: the full intertwiner algebra from multiplicity spaces, orbit-matrix basis, and two concrete commutants.

### Chapter 10

Worked examples:

1. The (2,1) Specht module in a coordinate-difference basis. Explicit cycle/transposition matrices, character, hook count and invariant Gram matrix distinguish a unitary representation from a nonorthonormal matrix presentation.
2. Every block of the S4 transposition average, exact two-step return probability 1/6, parity obstruction, and the lazy average with return 7/24 and convergence proved directly by finite spectral powers.

Exercises:

- `ex:v10exp-ch10-fivefillings` — basic listing of five (3,2) tableaux, hook count and transposition character 1.
- `ex:v10exp-ch10-threecycles` — intermediate counterexample/application: three-cycle averaging has an extra stationary parity direction, without eigenvalue −1; exact spectrum and limits within parity classes.
- `ex:v10exp-ch10-reverse` — intermediate insertion and all reverse steps for 425163; distinguishes time labels from carried values.
- `ex:v10exp-ch10-foursteps` — advanced group-word count giving an exact fourth moment of contents and four-step return probability. The local identity coefficient is N²+18 binom(n,3)+12 binom(n,4), including n=2.

### Chapter 11

Worked examples:

1. Negative U(2) weight (2,−1), its determinant twist, four Laurent monomials, central action, SU(2) values and the two summands after tensoring with the standard representation. No Schur–Weyl joint action is used.
2. Exact fourth trace-power decomposition and eighth absolute moments 14,23,24 at sizes 2,3,4. The real eighth moment at size two is 245/4 versus the standard Gaussian value 105. This explains the range in which moment equality is exact.

Exercises:

- `ex:v10exp-ch11-weight27` — basic weight/dimension/central-character calculation for (3,1,−1) on U(3).
- `ex:v10exp-ch11-matrixcov` — intermediate application: exact covariance of tr(AU), an unbiased squared-norm estimate and matrix-unit/identity checks.
- `ex:v10exp-ch11-dependent` — intermediate counterexample: the first two U(2) power traces are uncorrelated but not independent; their product has squared mean 1 instead of 2. The size-three comparison does not claim independence.
- `ex:v10exp-ch11-fourthpowertrace` — advanced alternant expansion of p2², with fourth absolute moments 1,6,7,8 at sizes 1,2,3,≥4 and a precise comparison with a variance-two complex Gaussian.

The existing unnumbered Schur–Weyl remark now says the isomorphism is **quoted here and proved in Chapter 14**. Its full formula is unchanged. The local character argument remains independent of that later proof. Chapter 11's ending points to the new three-chapter Part IV and to Chapter 14 for the representation route; the final capstone owns the next-volume bridge.

## Mathematical and prerequisite checks

Read the complete current assigned sources, the style/mathematician-writer instructions, actual main file and applicable blueprint. Chapters 9–10 were also fully reviewed by this agent in the preceding rewrite phase; their exact baseline texts are the reviewed sources. Chapter 11 was freshly read in full, including all ten existing exercises/hints/solutions.

All additions use established finite character theory, the local induction/Mackey formulas, the proved Specht/tableau/content results, or the proved compact character and trace formulas. No new premise from Chapters 6–8 is introduced. The character tables actually used are the S3/S4 tables already in Volume 3 and referenced in the current chapter. General multiplicity-space endomorphisms are proved directly using the existing Schur lemma. The central-walk convergence calculations are finite-dimensional diagonalisation, not an appeal to the later mixing theorem. The U(n) calculations use finite alternants and orthogonality, not the future joint Schur–Weyl theorem or a numerical approximation to an integral.

Boundary checks include n=1 for unitary covariance and fourth power traces, n=2 for the content return identity, finite row-count truncations, determinant twists of negative weights, repeated eigenvalue extension by polynomial identities, nonzero multiplicity spaces in the commutant exercise, and the distinction between covariance and independence. No genuine correction to an existing formal statement was necessary. No new historical attribution or bibliographic record is introduced; the mathematical calculations are derived on the page using the chapter's already cited sources.

## Checks actually run

1. A Python source check compared every baseline formal statement, exercise, hint, solution and figure block with the current source as an exact substring. Totals checked were 49 protected blocks in Chapter 9, 49 in Chapter 10, and 43 in Chapter 11. All passed. All numbered section headings remain identical in order, and counts of numbered formal environments remain identical. Original exercise counts rise only from 10 to 14; figure counts remain 3.
2. Label uniqueness and retention were checked in all three sources. Each has exactly two worked-example markers, and four new uniquely labelled exercises with matching hints/solutions.
3. Ran `source /workspace/order-chance-system/activate.sh && python3 - <<'PY' ... PY` with exact rational/SymPy checks of the S3 induced group relations, both invariant Gram matrices, S4 ordered-pair character multiplicities, forward insertion of 425163, the two-variable identity p1 p2 = h3, the real eighth moment 245/4 and the S4 four-step return value 5/54. The command exited 0 and printed: “Exact matrix relations, invariant Gram matrices, S4 character multiplicities, RSK pair, two-variable character and rational moment/return calculations passed.” These illustrate arithmetic checks; the proofs are in the manuscript.
4. `git diff --check -- volume10-abstraction/chapters/ch08-semisimple.tex volume10-abstraction/chapters/ch09-symmetric.tex volume10-abstraction/chapters/ch11-compact.tex` exited 0.

No TeX build, rendered layout, EPUB inspection, CI or publication check was run by this writing agent. No commit, staging or push was performed.

Source SHA-256 at handoff:

- Chapter 9: `849b2be9e564a6268f2d963e8e0b8aa4b3b6dbb2acc1f05755c71c3daf6cc804`.
- Chapter 10: `567a0efa22b6f7e56e07ba855ecdea3fefdce6817e93653e3eb8b7b8897437f2`.
- Chapter 11: `48a51189c83f623b8a467d80c878c461e05372767d3ee99822f2a6c744534db1`.

This record describes the writer's source checks, not independent certification. A separate reviewer must read the new material and the parent must perform production validation.
