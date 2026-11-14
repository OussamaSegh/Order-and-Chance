# Volume 8 rewrite — handoff

Branch: `cursor/volume8-complete-rewrite-3faf`. Base: `main` at `e9711ffe`. The folder is `volume8-analysis`. Do not edit any other volume. Do not merge, and do not edit, PR #157. Read the blueprint with `git show origin/claude/project-thread-khh5pi:docs/plan/book-08.md`. The structural pass (sixteen chapters, six appendices, random-matrix chapters in Volume 12) is already on `main`. Where the blueprint disagrees with the older `docs/plan/book-08.md` on `main`, the blueprint wins. This pass does not renumber.

## What “rewritten” means

A sentence counts when it has at least 40 characters and at least 25 characters outside mathematics. It is rewritten when it is not identical to the sentence in `origin/main`. Target: at least 90% in every chapter, in the main text and again from the exercises onward (hints and solutions included). Quotations inside quotation marks may stay. A displayed formula that was already checked may stay. The English around it may not.

## Style

`docs/WRITING-STYLE.md`, Sound human. Short sentences. A small case before the general claim. “You” when the reader should check a case. No “delve”, “robust”, “landscape”, “tapestry”, “journey”, “it is important to note”, “in this section we will”, “in conclusion”. The volume already has that voice. This pass still rewrites the sentences. It does not replace the voice with a generic textbook.

## Numbering lock

Do not insert a theorem, proposition, lemma, corollary, definition, or example except nothing: no new numbered statement in the middle. Four new exercises go at the **end** of each chapter’s exercise list. Keep every `\label`. Keep the order of numbered environments. Later volumes cite Volume 8 by hand-typed numbers. A new statement in the middle would shift those numbers. New exercises use fresh labels `ex:v8c01a` through `ex:v8c16d` for the sixteen chapters and `ex:v8cAa` through `ex:v8cFd` for the appendices.

No proof or solution may use a later chapter or a later volume as a premise. A forward pointer is a preview. Proofs use only what Volumes 1–8 have already taught, in the printed order of `main.tex`. Numerical checks are not proofs. Do not weaken a theorem.

Do not change fonts, sizes, or the text inside an existing diagram. New figures are new files. Do not regenerate cover motifs or lettering. The paperback ISBN stays blank.

## Portraits

`\portrait` is defined in `volume8-analysis/main.tex`, the same macro Volumes 5 and 7 use. Credits live in `volume8-analysis/photos/CREDITS.md`. Place a portrait at the first real mention. Caption pattern repeats the credit. Short photographs are capped so the print height keeps the short side at about 300 ppi.

## Figures

Each chapter includes two new TikZ figures, colours `MidnightBlue` and `BurntOrange` (and `BrickRed` where a third ink helps), by `\fig{...}` inside `\begin{figure}[ht]`. Captions state the takeaway. No existing figure file is overwritten. No pixel width is set. New files are named `chNN-rw-*.tex` or `appX-rw-*.tex`.

## Exercises

Four new exercises per chapter, after the last existing exercise, each with a hint and a solution (`\idea` then `\writeup`). Solvable from this chapter and earlier volumes. Stars as in the series.

## Scope of files

- `volume8-analysis/`
- `docs/handoffs/volume8-rewrite.md`
- the Volume 8 sentence in `common/cover-notes.json`, and the hashes `tools/series_cover.py --check` needs (`volume8-analysis/about-the-cover.tex`, `docs/COVER-NOTES.md`, `tools/assets/series/manifest.json`)
- if the cover-note hash moves, the Volume 3 inventory and conceptual snapshot get a hash-only refresh, because `inventory.py --check` and `registers.py` compare those hashes

## Chapter map

| Ch. | Title | File | Label |
| --- | --- | --- | --- |
| 1 | Banach Spaces | `ch01-banach.tex` | `ch:banach` |
| 2 | Hilbert Spaces | `ch02-hilbert.tex` | `ch:hilbert` |
| 3 | The Spectral Theorem and Its Relatives | `linear-ch05-spectral.tex` | `linear:ch:spectral` |
| 4 | Singular Values | `linear-ch06-svd.tex` | `linear:ch:svd` |
| 5 | Graphs through Their Eigenvalues | `linear-ch08-graphs.tex` | `linear:ch:graphs` |
| 6 | Cuts, Mixing and Expansion | `spectral-expansion.tex` | `ch:cheeger` |
| 7 | Expanders and Ramanujan Graphs | `ch09-expanders.tex` | `ch:expanders` |
| 8 | Operators, Spectra and Banach Algebras | `ch03-operators.tex` | `ch:operators` |
| 9 | The Spectral Theorem for Compact Operators | `ch04-spectral.tex` | `ch:spectral` |
| 10 | The Fourier Transform | `ch05-fourier.tex` | `ch:fourier` |
| 11 | Distributions and Sobolev Spaces | `ch06-distributions.tex` | `ch:distributions` |
| 12 | Fourier Analysis on Finite Abelian Groups | `ch07-finite.tex` | `ch:finite` |
| 13 | Haar Measure, Duality and the p-adic Numbers | `ch08-haar.tex` | `ch:haar` |
| 14 | Cauchy's Theorem, Growth and Mellin Inversion | `ch09-complex.tex` | `ch:complex` |
| 15 | Tauberian Theorems | `ch10-tauberian.tex` | `ch:tauberian` |
| 16 | The Values of Zeta | `ch11-harder.tex` | `ch:harder` |
| A | Spaces, Quotients and Duality | `linear-ch01-duality.tex` | `linear:ch:duality` |
| B | Determinants as Volume | `linear-ch02-volume.tex` | `linear:ch:volume` |
| C | Eigenvalues and Invariant Subspaces | `linear-ch03-eigen.tex` | `linear:ch:eigen` |
| D | Inner Products and Projections | `linear-ch04-inner.tex` | `linear:ch:inner` |
| E | Inequalities between Matrices | `linear-ch11-inequalities.tex` | `linear:ch:inequalities` |
| F | Linear Dynamics | `linear-ch12-dynamics.tex` | `linear:ch:dynamics` |

## Progress

| Ch. | State |
| --- | --- |
| — | Draft pull request opened: https://github.com/OussamaSegh/Order-and-Chance/pull/242 |
| — | Preface, blurb, `kdp.md`, About the Cover, portrait macro and credits | Done |
| 1–7 | Sentence rewrite, two figures, four exercises | Done; final review and full-format validation pending |
| 8–16, A–F | Sentence rewrite, two figures, four exercises | In progress |

Portraits on disk, not yet placed in the chapters: Banach, Hilbert, Cayley, Kirchhoff, Fredholm, Fourier, Poisson, Gauss, Haar, Hadamard, Cauchy, Tauber, Riemann, Jordan, Frobenius, Schwarz, Lyapunov. Credits are in `volume8-analysis/photos/CREDITS.md`. Place each at the first real mention. Do not invent a caption.

The Volume 8 cover note changed `common/cover-notes.json`. `tools/series_cover.py --check` passes. The Volume 3 inventory and conceptual snapshot were restamped for that one hash. No Volume 3 anchor or status changed.

## Build

Not yet. When the manuscript is in, `./build.sh --pdf-only volume8-analysis` and the EPUB. No overfull boxes, no undefined references. Page count must stay between 300 and 600.

## Remains

Every chapter, the preface, the blurb, `kdp.md`, the About the Cover note, portraits, two new figures per chapter, four new exercises per chapter. Then the local build, then CI.

The independent review is a separate agent. This file does not contain that review.

## Continuation, 14 November 2026

Started from the latest remote head `32d7aa9a`. No chapter had been rewritten there. Merged current main (`328316fd`) normally in `4eb1a166`; resolved the shared cover-note inventory and conceptual-snapshot conflicts by retaining current main's Volume 3 review evidence and refreshing only the combined cover-note hash. `4f6c165a` aligns the Volume 8 About the Cover hash. No cover motif or lettering was regenerated.

The baseline `./build.sh --pdf-only volume8-analysis` exited 0: 431 print pages, 575 whole boxes, maximum height 298.0 pt, no overflow or undefined reference. This is a baseline count, not the final rewritten count.

Chapter 1 is rewritten, including the real and complex Lp-duality proof, all exercises, hints and solutions. Banach's credited portrait is placed. Two new plates (`ch01-rw-dual`, `ch01-rw-coordinates`) follow the existing figures so their numbers stay fixed. Four exercises `ex:v8c01a`–`d` are appended: a diagonal operator and its inverse, powers in C[0,1] with no weakly convergent subsequence, an explicit separating form, and the unit vectors in c0 versus l1. Each has a hint and a complete solution. Existing figure environments and captions remain byte-for-byte unchanged.

### Explicit mathematical corrections in Chapter 1

- The norm-one clause of `cor:hbnorm` is impossible on the zero space. It now assumes E is nonzero for that clause, retains the dual norm formula for every E including zero, and proves the x0=0 case on nonzero E. This is an explicit correction of a false edge case, not a silent weakening. The label and number do not change.
- The Riesz–Markov proof uses inner regularity from Volume 7, Theorem 12.1, rather than Lemma 11.10, which is stated on Euclidean space. Zero Jordan parts are handled with constant test functions before constructing distance functions to two nonempty closed sets.
- Bounded dual sets are relatively weak-star compact; they need not be compact themselves. The compact-set assertion is now made for the closed dual ball. The reflexive-space consequence is stated for the closed unit ball.
- Sigma-finite Lp densities are patched on the measurable disjoint rings E_n minus E_(n-1); their almost-everywhere agreement is retained. The q=infinity bound is handled separately from monotone convergence.
- The oscillation estimate is justified by its triangular primitive, avoiding the claim that an arbitrary interval leaves only one incomplete half-period.

The source audit in `/tmp/v8_audit.py` checks original numbered-environment order, labels, duplicate labels, frozen figure environments/captions, and the counts of added exercises and figures. At Chapter 1 it passes, and `tools/cross_volume_citations.py` exits 0. The full build and prose-share audit remain to be run after all chapters are rewritten.

Chapter 2 is rewritten, including projection, Riesz, orthonormal bases, Fourier and Legendre expansions, Kronecker–Weyl, the mean ergodic theorem, von Neumann's Radon–Nikodym proof, and Moore–Aronszajn. Hilbert's credited portrait is placed. New figures `ch02-rw-tail` and `ch02-rw-kernel` show Parseval tails and a two-point kernel's geometry. New exercises `ex:v8c02a`–`d` compute a projection, a geometric coefficient tail, two operator averages, and a finite RKHS norm. Frozen figure environments and captions remain byte-identical; the source-order/label audit and cross-volume checker pass.

Chapter 2 clarifies three existing claims without moving any number: only infinite-dimensional separable Hilbert spaces are identified with l2 indexed by all positive integers; a bounded set need only be relatively weakly sequentially compact; kernel positivity alone does not guarantee that any specified data become linearly separable. The mean-ergodic proof now introduces the adjoint and derives its norm and double-adjoint identities before using them. The Radon–Nikodym proof first chooses a representative with 0 <= g <= 1 everywhere, and explicitly removes the null set where g=1 when defining the density. The no-nearest-point solution treats complex functions by a phase rotation and a real-part argument. The Legendre proof uses n integrations by parts, correcting its undefined k. The RKHS completion is realised injectively as functions via the evaluation vectors, with the original theorem unchanged.

Chapter 3 is rewritten through all original exercises and solutions. Cauchy's credited portrait is placed. The two added plates show the Schur–Horn hexagon for eigenvalues 3, 2, 1, and scalar shifts attaining both spectral perturbation bounds. Exercises `ex:v8c03a`–`d` cover spectral projections and matrix powers, a two-dimensional compression, prescribed diagonals of rank-one projections, and sharp versus quadratic perturbations. Original statement order, labels and frozen figure environments pass the source audit.

Schur triangularisation is proved locally before the spectral theorem, using the fundamental theorem of algebra, an eigenvector and Gram–Schmidt, so the main proof no longer needs an appendix as a premise. The equality case in the Hermitian trace inequality now includes its converse: plane variations force commutation across unequal eigenspaces, and swapping an inverted eigenvalue pairing would increase the trace. The rank-one perturbation solution handles dimension one separately. The real normal-form solution makes the conjugate-pair basis and reducing complement explicit.

The checkpoint PDF after Chapters 1 and 2 exits 0 at 437 print pages, with no overflow or unresolved references. Fredholm's and Schwarz's credited portraits are also placed in Chapter 2. The prose audit counts all eligible narrative sentences as rewritten in Chapters 1–3; retained source titles account for the remaining identical strings in the exercise-side audit. Cross-volume citations match 4915 numbered statements. These are checkpoint results, not final Volume 8 validation.

Chapter 4 is rewritten, with Jordan's credited portrait, two new plates on truncation error and conditioning, and exercises `ex:v8c04a`–`d` on a rectangular pseudo-inverse, a storage budget, sharp conditioning and an exact PCA fit. All original labels, numbered-environment order and figure environments pass the audit. The prose audit's unchanged strings are bibliographic entries. The cross-volume checker passes at 4919 numbered statements.

The SVD proof now proves the kernel identity directly instead of assuming the later appendix's least-squares theorem. The polar proof proves uniqueness of the positive square root locally. The geometry distinguishes the image of a ball from the image of a sphere, including a nontrivial kernel. The truncation theorem makes its index range and zero-extension convention explicit, and proves the full-rank endpoint separately. PCA also handles zero appended directions. The nuclear-norm solution uses diagonal entry bounds, valid over both fields, instead of invoking complex unitary factors in a real argument. The Penrose uniqueness proof identifies projections by image and kernel. Statements about conditioning describe sensitivity rather than guaranteeing an algorithm's numerical stability.

Chapter 5 is rewritten, with Frobenius's and Kirchhoff's credited portraits, new plates on a sharp independent set and signed-square cancellation, and four exercises `ex:v8c05a`–`d`. These compute bipartite spectra, analyse equality in Hoffman's bound, multiply Huang's signed square exactly, and recover complete graphs and odd-cycle obstructions from traces. All original labels, statement order and frozen plates pass; the citation checker passes at 4923 statements.

The friendship theorem now explicitly includes the single-vertex windmill. The strongly regular definition still permits complete graphs; the spectral theorem handles them separately rather than applying a potentially meaningless two-root formula to a vacuous parameter. This is an explicit repair of that edge case, not a hidden restriction of the definition. Hoffman's proof separates the empty independent set before dividing. The bipartite-spectrum proof handles a singleton and proves the sign argument directly. The inertia proof uses intersecting non-negative subspaces and covers the case in which their codimension bound exceeds the dimension. Huang's sharpness solution gives exact neighbour lists rather than relying on an asserted computer enumeration; its original requested examples and conclusions are retained.

The PDF checkpoint through Chapter 4 exits 0 at 445 print pages, with 595 whole boxes and no overflow or unresolved references. A new Chapter 4 plate initially used an undefined colour name; both new plates now use the existing BurntOrange palette name, and the successful checkpoint includes that correction. No existing figure file was changed.

Chapter 6 is rewritten, including Cheeger's level-set proof, mixing, Nilli's Alon–Boppana proof and every exercise. New plates show the level-set integrals and bipartite alternation. Exercises `ex:v8c06a`–`d` treat complete-graph cuts, exact lazy mixing on a square, finite level-set identities and the general lazy spectral bound. Original numbered-environment order, labels and figure environment pass; cross-volume citations pass at 4927 statements.

The chapter explicitly assumes at least two vertices wherever mu_2 is used, defines D−A before the nonregular path exercise, and requires positive degree for transition probabilities. The Ramanujan definition excludes both trivial eigenvalues, including −d in bipartite graphs; the earlier text's lambda includes −d, so it cannot describe bipartite Ramanujan bounds or imply ordinary-walk mixing there. This distinction is now made explicit without changing Cheeger or mixing claims. Nilli's proof includes k=0, zero cross terms between supports, and a separate degree-two asymptotic, avoiding logarithms to base d−1=1. The girth-count solution permits boundary edges while excluding repeated vertices, which are what the count actually needs. The walk bound now proves its stated assertion for arbitrary initial laws, rather than only point starts.

Chapter 7 is rewritten through every proof, exercise, hint and solution. Cayley's credited portrait is placed at the Cayley-graph explanation. Two new plates illustrate four-step tree returns and a signed triangle's double cover. Exercises `ex:v8c07a`–`d` compute an exact hitting probability, the bipartite K_3,3 zeta counts, endpoint moment growth and the spectral splitting of a signed double cover. All original labels, numbered-environment order and frozen figure environments pass the source audit. The prose audit, restricted to narrative and exercises/hints/solutions rather than bibliographic records, finds every eligible sentence rewritten in Chapters 1–7, in each category separately. Bibliographic titles and quoted material remain intact. Cross-volume citations pass at 4931 statements.

The random-graph claim was checked against Huang–McKenzie–Yau, arXiv:2412.20263v2 (2 February 2025), Theorem 1.2 and Corollary 1.3, and Sloman's Quanta account (18 April 2025). It is for each fixed d >= 3 and uniformly random simple graphs as admissible size grows; both edge distributions and asymptotic independence are relevant to the roughly 69% probability. The source entry now identifies that version and those results. The concentration proof retains the full two-variable recurrence and the constant 20, with its restrictions and exponential estimates explicit. The Kesten proof defines the needed Chebyshev polynomials locally and justifies the series integrals by uniform convergence. Return growth is proved from endpoint mass, without assuming an infinite-dimensional spectral theorem. Random short-cycle counts are described as bounded in probability, not deterministically O(1).

Explicit corrections: `ex:amplify` originally demanded an exact fractional-bit budget for arbitrary degree, and its solution's ceiling did not produce an exact uniform sample. The exact budget now specifies power-of-two degree; the exercise also asks for the obstruction and a rejection sampler at other degrees, whose expected cost is proved. The point-start condition is made explicit when claiming a bipartite walk fails to converge; a uniform start is stationary. Bass's determinant identity retains graphs with m < n by explaining removable factors, while the subsequent extra-eigenvalue list assumes degree at least two. The cycle-zeta hint uses polynomial factorisation rather than a complex-modulus formula invalid for complex u. The SL_2 remark excludes p=2 from its four-regular assertion; the group generation exercise retains all primes.

The checkpoint PDF through Chapter 6 exits 0 at 451 print pages, 603 whole boxes, with no overflow or unresolved references. The Chapter 7 checkpoint build is running; this handoff does not claim its result.
