# Volume 8 rewrite: final review and validation

PR: [#242](https://github.com/OussamaSegh/Order-and-Chance/pull/242).
Branch: `cursor/volume8-complete-rewrite-3faf`.
Review baseline: main at `328316fdac0a44f97eddfc5204033d9eb1c133a0`;
continuation began at `32d7aa9af67678e6c4d013a97ace9f5d5c46291e`.

This is the implementing agent's review, performed under the author's subsequent
instruction, “You review and merge.” It does not claim a separate reviewer's
approval. The [handoff](../handoffs/volume8-rewrite.md) records the mathematical
changes in detail, including explicit corrections of false edge cases.

## Scope and invariants

All sixteen chapters and six appendices have rewritten narrative, proofs,
exercises, hints and solutions. Each unit has two new TikZ plates and four
exercises appended after its original exercise list: 44 plates and 88 exercises.
Each new exercise has a hint and a complete idea/writeup solution. The preface,
blurb, KDP listing and About the Cover copy are complete. All seventeen credited
portraits are placed exactly once. The paperback ISBN is blank.

The source comparison against main verifies all **505 original printed
statement/exercise triples** (environment kind, number and label), in their original
order. Every original label survives, with no duplicate label in a chapter.
All **46 original figure files are byte-identical**, as are all original figure
environments and captions. Added plates follow the original plates in each unit,
so original figure numbers also stay fixed. No cross-volume number repair is
needed.

The sentence comparison follows the handoff's eligibility rule (at least forty
characters and twenty-five letters outside mathematics). Every eligible narrative
and exercise/hint/solution sentence is rewritten, apart from literal quotations,
frozen figures and bibliographic records. The retained Maxwell epigraph is a
quotation, including its two sentences outside quotation marks. This comparison
is an editorial coverage check; it is not a proof of mathematical correctness.

## Chapter and appendix changes

Every row includes two new figures and four appended exercises with hints and
solutions. The commit column identifies the main rewrite commit; later proof-copy
and export fixes apply on top.

| Unit | Rewrite and mathematical focus | Commit |
| --- | --- | --- |
| 1. Banach spaces | Separation, duality and weak convergence; zero-space norming clause, regularity and almost-everywhere density patching made explicit. | `9711f370` |
| 2. Hilbert spaces | Projection, series, mean ergodic theorem, Radon–Nikodym and RKHS; adjoints introduced before use and kernel completion realised injectively. | `e037c73c` |
| 3. Finite spectral theorem | Local Schur proof, min–max and perturbation; trace-inequality equality case and real normal blocks justified. | `4e8a696d` |
| 4. Singular values | SVD, polar factors, truncation, PCA and conditioning; kernel/full-rank endpoints and complex phases checked. | `d3c2b687` |
| 5. Graph spectra | Walk counts, strongly regular graphs, friendship, Hoffman and sensitivity; complete-graph and empty-family edge cases checked. | `4aae17fe` |
| 6. Cuts and mixing | Cheeger cuts, walks and expansion; degree/dimension hypotheses, bipartite oscillation and two-sided mixing distinguished. | `4e18ae4c` |
| 7. Expanders | Tree return moments, constructions and graph zeta; exact sampling, Bass cancellations and dated random-graph theorem verified. | `66fa52b6` |
| 8. Operators and algebras | Fredholm, resolvents, spectra and characters; measurable kernel sections and the Laurent/UBP argument supplied. | `500d53b2` |
| 9. Compact spectra | Eigenvectors, strings, positive kernels and Brownian covariance; IVP uniqueness, Mercer interval and functional-calculus kernel cases repaired. | `8abdce79` |
| 10. Fourier transform | Plancherel, interpolation, characteristic functions, sampling and Poisson; locally uniform lattice summation and the global sharp Hausdorff–Young theorem distinguished. | `1071c0dd` |
| 11. Distributions | Weak derivatives, fundamental solutions, Sobolev estimates and Galerkin; boundary regularity, convolution and exact layer scaling checked. | `204e3f49` |
| 12. Finite Fourier analysis | Characters, reciprocity, uncertainty, FFT and additive methods; characteristic-free rank arguments and exact cap-set constant supplied. | `3f6684dd` |
| 13. Haar and duality | Means, paradoxical actions, Haar uniqueness and p-adic inversion; countability scope and both directions of self-duality topology checked. | `0d98f246` |
| 14. Complex growth | Cycles, strips, entire products and Mellin inversion; proper-domain, constant-function and zero-product cases handled with local factorisation proof. | `47dd5253` |
| 15. Tauberian theorems | Density/inversion, Wiener–Ikehara, PNT and two squares; zero residue, negative smoothing arguments and partial-summation implication repaired. | `2b30d2a4` |
| 16. Zeta problems | All 22 original linked problems and research leads; strict boundary positivity, endpoint evaluation kernels and exact constants proved. | `ba80b397` |
| A. Duality | Bases, quotients, annihilators and compatibility; exact Lights Out recurrence and dimension-free factorisation replace unsupported checks. | `8198a744` |
| B. Determinants | Exterior powers, minors, condensation and paths; Pluecker proof works in characteristic two, and generic perturbations repair the condensation algorithm. | `3e9a6b58` |
| C. Eigenvalues | Primary decomposition, Jordan chains and functions; zero-dimensional cases, arbitrary-characteristic substitution and local uniqueness proofs supplied. | `cef8b527` |
| D. Inner products | Projections, least squares, Gram determinants and quadrature; interval hypotheses, positive recurrence and compact-closure approximation checked. | `faba5c2a` |
| E. Matrix inequalities | Loewner order, Schur complements, Gaussian kernels and Hilbert inequality; exact counterexamples and proof of the sharp constant added. | `4119af9d` |
| F. Dynamics | Powers, energy, acceleration, control and cubic stability; singleton spectral intervals, nilpotent heavy-ball block and exact transient/energy calculations handled. | `7e5f0512` |

## Mathematical review

The pass compares numbered statements with main as well as checking their proofs.
Changes that restrict an originally false assertion are recorded explicitly in the
handoff, rather than hidden as stylistic edits. Examples include the zero-space
norm-one functional, the nondegenerate Mercer interval, global versus local
uniformity in Poisson summation, continuity on the closure for quadrature
convergence, and the singleton Chebyshev interval. Valid conclusions and all
printed numbers remain intact.

Proofs use results available earlier in the printed order. Local arguments replace
forward dependencies for Schur triangularisation, positive-square-root uniqueness,
Fredholm's alternative, IVP uniqueness, characteristic-free exterior independence,
and simultaneous diagonalisation. Advanced context such as Beckner's sharp
inequality, the general Haar/duality theorems and recent graph results is clearly
quoted with sources. Numerical illustrations are not substituted for proofs.
The recent graph, cap-set and Hadamard claims were checked against their primary
papers; their dates and scope are stated explicitly.

## Validation

The local review checks completed before this report was committed are:

- All 20 citation unit tests pass on manuscript source `16c6d0d6`.
- `tools/cross_volume_citations.py` matches 4991 numbered statements.
- `review/volume3-internal/registers.py` exits 0, reporting 1177
  accepted-internal and 19 pending entries. Those pending entries are the existing
  register state; this rewrite does not approve or change them.
- Number, label, exercise/hint/solution, frozen-figure and prose audits pass.
  A second prose comparison also covers short sentences below the handoff's
  coverage threshold; remaining identical fragments are titles and quotations.
- All 44 added plates compile independently. Four contact sheets were inspected;
  two label collisions were corrected, rendered and inspected again.
- The complete-manuscript PDF checkpoint exits 0 at 491 print pages, with 659
  whole boxes, maximum height 391.2 pt, no overflow and no unresolved references.
  Its reading/print navigation, fonts, bleed and cover export checks pass.
- `git diff --check` passes.

The **final exact-head** PDF-only build, full PDF/EPUB export, EPUB size, visual
export review and all GitHub Actions run IDs are recorded in the
[PR completion record](https://github.com/OussamaSegh/Order-and-Chance/pull/242).
That record is updated after each check actually finishes, before merge. Keeping
run IDs there avoids making a new commit merely to name the head just checked.
