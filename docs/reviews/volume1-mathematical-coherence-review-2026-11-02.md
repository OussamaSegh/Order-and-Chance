# Volume 1 — mathematical correctness, coherence, and high-school-entry review

**Date:** 2026-11-02  
**Manuscript:** `volume1-first-principles/main.tex`, eleven included chapters, reviewed on the current main branch and corrected on `review/volume1-proof-and-sequence-audit-20261102`.  
**Decision:** **Not yet certified for first-edition publication.** The corrections below are proposed, structural checks pass, and representative rigorous proofs were inspected; an independent line-by-line verification of **every** worked example, exercise solution and theorem proof, plus a clean PDF build, remains necessary before asserting that *all mathematics* is correct.

## Review standard

The reader knows only secondary-school arithmetic, fractions, powers, polynomial algebra, elementary equations, inequalities, graphs and geometry. Everything beyond that must be (1) defined and proved before use on the foundations route, (2) explicitly named as a foundational axiom, or (3) signposted as an optional preview/bridge. Results in a later chapter cannot silently justify an earlier theorem.

The preface states the starting axioms and introduces the completeness of the reals, four basic properties of integration, and the elementary real exponential/logarithmic/trigonometric identities and derivatives as **declared foundations**, not as concealed university prerequisites. These are clear but should be evaluated in a reader trial with someone who has not studied calculus: the text promises no prerequisite calculus, although it takes these elementary-function and integration facts as a starting point.

## Scope of this pass

- Independently inspected chapter sequence, principal theorem statements, all **160 exercise statements**, definitions at selected first uses, and substantial proofs in counting, order theory, real/complex analysis, polynomials, linear algebra, integration and probability.
- Traced forward references in the main chapter text: **42** point to later material. Examined their contexts; they are signposted as a preview, explicit deferred proof or later optional application, not an unannounced main-path dependency.
- Re-ran repository-wide structural checks over the eleven chapter files on the review branch: **160 exercises, 160 matching hints, 160 matching solutions; 406 unique LaTeX labels; 768 cross-references; zero duplicate labels and zero unresolved references**. Counts exclude `main.tex` and ancillary front/back matter, so they are not claims about a full PDF build.
- Checked for references to removed numbered specialist challenges. Only the **retained** challenges in the Language chapter remain; no dangling numbered references to removed challenges remain in the other ten chapter files.
- Compared several non-trivial statements with their proofs/solutions, including alternating-series remainder, EKR double count, Dilworth's proof, the fundamental theorem of algebra, the real spectral theorem, Gaussian integral from Wallis, Cauchy product, a stochastic-matrix convergence exercise, Cauchy/Hilbert determinants, the Ramsey first-moment argument, and the records-variance exercise.
- These checks are **not** a computer-verified or independent proof-by-proof certification of all 160 exercise solutions and every display, illustration or historical statement.

## Corrections made on the review branch

### 1. Alternating series remainder — mathematical statement clarified

In `ch05-sequences-series.tex`, the theorem formerly said that the remainder lies between zero and "the first omitted term," while the bound was written in terms of the unsigned number `a_{n+1}`. For a series starting with a positive term, the remainder after an even index is typically *negative*. The proof already used the correct signed bound. The statement now explicitly says that `R_n` lies between `0` and `(-1)^{n+1}a_{n+1}`, hence `|R_n| <= a_{n+1}`.

**Check:** For `1 - 1/2 + 1/3 - ...`, after the first term the remainder equals `ln(2)-1 < 0`; it is between `-1/2` and `0`, not between `0` and `1/2`.

### 2. Erdős–Ko–Rado — missing domain restriction

In `orders.tex`, the theorem formerly declared only `n >= 2k` without specifying `k >= 1`, while the proof counts nonempty cyclic arcs and writes `binom(n-1,k-1)`. It now explicitly assumes integers `1 <= k` and `n >= 2k`.

### 3. Erdős–Ko–Rado — overly strong necessity claim

The text formerly asserted that `n >= 2k` is **necessary for the bound**. It is necessary for the **general theorem as stated without further cases**, but not for every parameter pair; for instance `n=k=2` has the bound `1 <= 1` even though `n < 2k`. The sentence now reads that the assumption "cannot be dropped in general", followed by the existing `n=3, k=2` counterexample. This is mathematically precise.

### 4. Dangling references after deletion of specialist challenges — editorial coherence

The previous prerequisite reduction removed many specialist challenges, but prose and bibliography still referred to them, notably in Sums, Sequences, Complex Numbers, Linear Algebra, Inequalities and Probability. Replaced fourteen references in those six chapter files with self-contained explanations, accurate research/source descriptions, or explicit later-volume previews. In Inequalities, the sharpness of Carleman's constant is now explained with the previously established Stirling asymptotic instead of sending the reader to a deleted challenge.

### 5. Modular arithmetic notation — high-school prerequisite clarity

An optional Gauss-sum solution previously invoked `Z/pZ` and “the field” without describing how residue representatives were used. It now reindexes the sum explicitly with the high-school remainder classes `0,...,p-1`. The first finite-field application in Polynomials now defines addition and multiplication modulo a prime and derives inverses from the Bézout identity already proved in Sums. The circular-lamps exercise now spells out its labels `0,...,n-1` and wraparound instead of assuming familiarity with `Z/nZ`. These are instructional clarifications, not changes to the mathematical outcomes.

## Sequential chapter assessment

| Reading order | Chapter | Entry and dependency assessment |
| --- | --- | --- |
| 1 | The Language of Mathematics | Introduces logic, sets, functions, relations, elementary proof language. The distinction between a field and ordinary numbers is eventually made explicit before the polynomial chapter needs it; early invocations of real-analysis results point ahead transparently. |
| 2 | Sums, Binomials and Induction | Builds induction, finite sums, divisibility, binomial coefficients and finite-difference methods. Polynomial examples use high-school algebra and do not invoke the later polynomial theory. Removed dead challenge pointers. |
| 3 | Counting and Discrete Reasoning | Builds basic combinatorics, inclusion–exclusion, derangements, paths and introductory generating-function reasoning from prior sums and sets. Probability is explicitly deferred. |
| 4 | Sequences, Series and Limits | Defines sequences, completeness-based convergence, continuity and differentiation, develops convergence tests, and establishes Stirling's *shape* with an undetermined constant. Does not rely on the later Wallis coefficient. Corrected signed alternating-series remainder. |
| 5 | Orders | Builds posets, chains, antichains, Dilworth/Mirsky, and finite-order arguments on prior counting. Corrected EKR hypothesis and necessity wording. The proofs are challenging but intended as learned material, not assumed knowledge. |
| 6 | Complex Numbers and Roots of Unity | Constructs complex arithmetic before geometric/exponential forms; defines groups before the roots-of-unity theorem; labels later algebra/linear-algebra applications as previews. Removed references to deleted construction challenges. |
| 7 | Polynomials | Defines fields in ordinary language, formal polynomials, division, roots, factorisation, interpolation and key proofs. The proof of the fundamental theorem of algebra explicitly uses already-established sequential compactness and complex arithmetic. |
| 8 | Linear Algebra | Introduces vector spaces, bases, linear maps, determinants, eigenvalues and orthogonality before spectral/Cayley–Hamilton applications. Later probability examples are marked as forward connections. Removed dead specialist references. |
| 9 | Differential and Integral Calculus | Builds derivatives and integrals from declared starting properties, proves Taylor/Wallis/Gaussian/Stirling's constant and Gamma in sequence. Earlier asymptotic statements point here for deferred constants and integral tools. |
| 10 | Inequalities, Convexity and Estimates | Uses calculus and algebra already established; develops Jensen, Cauchy–Schwarz, power means, Hölder etc. Sharpness of Carleman now has an in-text derivation. |
| 11 | First Probability | Builds finite probability after counting and analysis; introduces expectations/variance and the weak law, marking countable models explicitly. Deleted challenge references no longer interrupt the route. |

## Remaining publication gate

1. **Proof-level certification:** Independently re-derive every theorem and all 160 solutions (including equality cases, empty/zero cases, convergence hypotheses, and displayed intermediate identities). A matching solution label only proves that a solution *exists*, not that it is correct.
2. **Calculus-naive reader trial:** Give the preface and first use of a derivative/integral to a reader with only secondary-school algebra and geometry. Ensure that the declared axioms, not a past calculus course, suffice. Consider adding short geometric explanations of the four integral properties if the target audience includes readers with no school calculus.
3. **Build and print checks:** Run a clean LaTeX build with warnings treated seriously; check reference resolution, fonts, page overflow, figure legibility, image licences, cover/interior KDP settings and print-proof legibility. No clean build or PDF visual check was performed as part of *this* repository-access pass.
4. **First edition gate:** Do not label this mathematical review as an unconditional guarantee of correctness; merge the reviewed fixes after CI and address any remaining release gate in the separate KDP checklist.

## Verdict

The **chapter order is coherent** for the foundations route, and the earlier high-school prerequisite cleanup has materially improved accessibility. **Three precise mathematical statements/qualifications, fourteen dangling references and three prerequisite-notation explanations** were fixed on this branch. The chapter-wide exercise/hint/solution and cross-reference structure is consistent. The manuscript should **not yet receive an unconditional "all mathematics is correct" certification** without the remaining proof-by-proof review and clean production build.
