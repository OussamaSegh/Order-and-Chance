# Volume 1 — high-school-entry and introductory-scope review

2 November 2026 | Book: *First Principles* | PR #94

## Editorial contract

Volume 1 is the **entry point** of *Order and Chance*. Its first-reading path assumes secondary-school arithmetic, algebra, elementary functions and geometry, plus only the explicit foundational assumptions in the preface. Proof methods, notation and the mathematical structures actually needed to continue to Volume 2 must be explained **before** they are used.

A warm-up volume is not a catalogue of every interesting result accessible with those tools. Specialist results, professional research techniques, advanced estimates, and problems whose solutions require later volumes belong in those volumes, not in this introduction. Preserve the stories, examples, worked arguments, proof-finding workshops and foundational exercise progression.

## Audit and corrective edits

The initial audit examined the 11 chapters in their actual reading order, checked first uses of technical terms, and inspected all 192 exercise statements with their supplied solutions. It found and repaired:
- **Orders:** use of *ordered field* before a main-path field definition; early use of vector subspaces before linear algebra. The sign argument is now elementary; the subspace example was recast as a preview.
- **Complex numbers:** “C is a field” without the local definition. The text now defines a field before computing reciprocals, with Q/R examples and Z as a counterexample. Hermitian orthogonality and the Fourier basis are explained as a linear-algebra preview.
- **Polynomials:** F₂ is constructed by addition and multiplication modulo 2 before being used to distinguish formal polynomials from functions.
- **Linear algebra:** the Cayley–Hamilton proof no longer assumes the reader knows “commutative ring”; its polynomial-identity justification is spelled out. The covariance-matrix allusion is explained as a later probability preview.

## Introductory-scope reduction

**32 advanced numbered exercises, each with its hint and complete solution, were removed.** The decisions were based on dependency, specialist depth and pedagogical value—not merely on a three-star rating. Advanced but *self-contained* exercises that reinforce the book's main story have deliberately been retained.

| Chapter | Exercises removed | Rationale |
|---|---|---|
| Sums and induction | `pb:millin`, `pb:erdosheil`, `pb:sauer`, `pb:bilinear` | Later-volume polynomial method, exponential-sum estimates or specialist combinatorics |
| Sequences and limits | `pb:schwartz`, `pb:nullstellensatz`, `pb:newton` | Optional research-style polynomial bridges unrelated to the foundations route |
| Orders | `orders:ex:ackermannvalues`, `orders:ex:hydra`, `orders:ex:fixedpoints`, `orders:ex:konig`, `orders:ex:divisorscd`, `orders:ex:hansel` | Abstract recursion, proof-theoretic hydras, complete-lattice fixed points or non-introductory enumeration |
| Complex numbers | `ex:cotsum` | Optional post-polynomial specialist Basel bridge |
| Polynomials | `ex:logconcave`, `ex:sos`, `ex:mason`, `pb:bellasym` | Advanced real-root conditions, polynomial Fermat analogue and Volume 5 asymptotics |
| Linear algebra | `pb:tanroots` | Later-calculus asymptotic exercise unrelated to linear-algebra foundations |
| Calculus | `ex:trapezoid`, `ex:sophomore`, `pb:hyperplanes`, `pb:kakeya` | Advanced numerical asymptotics, specialised integral manipulation and finite-field geometry |
| Inequalities | `pb:stanley` | Non-introductory partition enumeration |
| Probability | `pb:cauchydav`, `pb:distances`, `pb:incidences`, `pb:szemereditrotter`, `pb:sumproduct`, `pb:treebound`, `pb:parking`, `pb:sinesecond` | Polynomial method, combinatorial geometry, advanced asymptotics, Volume 4 crossing lemma or Volume 12 matrix-tree theorem |

**Two substantial detours in Orders were removed** from the main chapter: complete lattices/abstract fixed-point theory, and Ackermann–Péter recursion, nested multiset ordering and the Kirby–Paris hydra. The chapter still teaches partial orders, chains and antichains, important finite-poset arguments, well-founded induction and lexicographic termination through a concrete rewriting example.

**Eight research-level challenge boxes and their matching notes were removed** from later chapters. The introductory challenge in *The Language of Mathematics* remains. Both `pb:benford` and `pb:lightsout` had their complete solutions preserved/restored in the course of removing challenge notes.

Remaining high-value hard problems—including the Catalan paths, interesting roots-of-unity sums, the spectral-theorem applications and probability counting questions—are presented after their necessary foundations. They are optional for a first reading and retain hints and solutions.

## Post-edit structural checks

Verified from the final changed chapter sources and the preface/field guide/image credits:

- **160 exercises, 160 named hints, 160 named complete solutions**. The IDs pair one-to-one, not just by count.
- **409 unique LaTeX labels, 801 local source references**; **no duplicate labels or unresolved reference targets**.
- `\begin{...}` / `\end{...}` environment counts balanced in these sources.
- The original 192 exercises and their historic source audits are a **pre-reduction baseline**, not the current edition.
- Volume 2 main chapters were sampled for removed specialist concepts: Volume 2 recalls elementary groups, fields and roots of unity, all retained in Volume 1; no new first-reading assumption was introduced by the cuts.

## Boundaries and release gate

A static dependency audit does not establish that every proof is independently correct or that every page is visually polished. **Full PDF and EPUB rebuilds and KDP previews are still required.** Because the paperback page count can change materially after these cuts, **do not reuse an old paperback cover/spine**; regenerate the KDP interior and matching wrap together after the final source changes, then recheck the correct ISBN and vendor previews.

This review changes the introductory scope, not the Volume 1 edition tag. **Do not create `volume1-first-edition` until the final build is successful and the publisher has confirmed KDP file and ISBN readiness.**
