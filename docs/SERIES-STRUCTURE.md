# Series structure (29 October 2026)

The author's structure is one mathematical narrative in fifteen numbered volumes,
from Mathematical Maturity through Order and Chance, plus one problem book.
The definitive catalog is `common/series.tex`. The README roadmap uses the
author's short subject names; full bibliographic titles are retained.

Volume 0 is **Mathematical Maturity**; its source stem is
`tome0-mathematical-maturity`. Volume 9 is **Higher Structures**; its stem is
`tome9-higher-structures`. Volume 14 is **Order and Chance**, subtitle
*Where Number Meets Randomness*, stem `tome14-order-and-chance`. It keeps the
Volume 14 slot. Parts I–IV are the arithmetic. Eight chapters keep complete
proofs; five openings cover short intervals, sieves, ranks, random matrices and
the zeros, and pseudorandomness. Part V is the research workshop, twelve
chapters, and appendices A–L are the conjecture case studies. Volume
identifiers, ISBNs and editions of the surviving books are preserved.

Volume 1 closes with Dirichlet characters, Euler products and Legendre’s sieve.
Volumes 0 and 2–13 include the corrected arguments from the October 2026 errata.

Crossroads (P1) is the only problem book. The two further problem books are not
in the series. Their written chapters sit at the end of the volumes whose
tools they use:

| Former chapter | New home |
| --- | --- |
| Almost Every Number | Volume 6, Harder problems |
| Hilbert Spaces at Work | Volume 7, Harder problems |
| Sums of Random Pieces | Volume 10, Harder problems |

Unpublished drafts that were never in those books were not added to a volume.

## Mathematics integrated into the main sequence

Supporting proofs remain where the books use them. Imported material is part of
the owning volume, with its own labels, figure filenames and notebooks.

| Main volume | Integrated material |
| --- | --- |
| 2 Structures | Appendices A–L: duality, determinants, spectral theory, SVD, positive matrices, graph spectra, symmetry, tensors, inequalities and dynamics. Appendix M: linear algebra in combinatorics, including Cauchy–Davenport. |
| 3 Chance | Appendix A: orders, chains, antichains and monotone subsequences; Appendix B: extremal combinatorics and Ramsey theory. Includes the short closure-rule and infinite-tree prerequisites. |
| 6 Spaces | Harder problems: almost every real number, from Borel–Cantelli and Hausdorff dimension. |
| 7 Analysis in Depth | Harder problems: Hilbert space at work. |
| 8 Shapes | Appendices A–L: Euclidean, transformation, projective, algebraic, lattice, hyperbolic and convex geometry, ending with curvature. |
| 10 Chance II | Harder problems: sums of random pieces. |
| 11 Random Motion | Appendix A: spectral graph theory, matrix-tree formulas, expansion and mixing; Appendix B: random matrices, the moment proof and the connection with zeta zeros. |
| 14 Order and Chance | Part V: the twelve workshop chapters. Appendices A–L: conjecture case studies in arithmetic, probability, geometry and algebra. Appendix E directs readers to the proofs and experiments in Volume 11, Appendix B. |

The five computing volumes and four companion volumes remain deleted as
standalone books. Optional references promising later computing books stay
rewritten as mathematical context.

## Publishing behavior

The library has main-series and problem-book filters. The site generator serves
only books with an existing `main.tex`, so stale PDFs cannot resurrect a removed
volume. The cache planner deletes removed and renamed book outputs when assembling
the next library; the rolling release is recreated from that complete assembly.
The art and subtitle generators contain sixteen books. A push to main is still
required for live release and Pages updates; local verification does not publish.

The cover of Volume 14 keeps the existing Steinhaus illustration. Title text
follows the shared master; the illustration, frame, type and material are unchanged.
