# Series structure (27 October 2026)

The author's revised identity is one mathematical narrative, in sixteen numbered
volumes, from Mathematical Maturity to The Research Workshop. The definitive
catalog is `common/series.tex`. The README roadmap uses the author's short subject
names (including Advanced Probability for the graduate probability stage); full
bibliographic titles are retained except for the two explicit renames.

Volume 0 is **Mathematical Maturity**; its aims are learning to prove, calculate,
solve problems and think mathematically. Its source and download stem is
`tome0-mathematical-maturity`. Volume 9 is **Higher Structures**, introducing
categories, commutative algebra and homological algebra; its stem is
`tome9-higher-structures`. Volume identifiers, ISBNs and editions are preserved.

The five computing volumes and four companion volumes are deleted as standalone
books, including their covers, metadata, notebook shelves and generated indexes.
The three problem books remain additional exercises for the main sequence.

## Mathematics integrated into the main sequence

Supporting proofs must remain available where retained books use them. Imported
material is part of the owning volume, with appendix numbering, distinct labels,
figure filenames and corresponding notebooks.

| Main volume | Integrated material |
| --- | --- |
| 2 Structures | Appendices A–L: duality, determinants, spectral theory, SVD, positive matrices, graph spectra, symmetry, tensors, inequalities and dynamics. Appendix M: linear algebra in combinatorics, including Cauchy–Davenport. |
| 3 Chance | Appendix A: orders, chains, antichains and monotone subsequences; Appendix B: extremal combinatorics and Ramsey theory. Includes the short closure-rule and infinite-tree prerequisites. |
| 8 Shapes | Appendices A–L: Euclidean, transformation, projective, algebraic, lattice, hyperbolic and convex geometry, ending with curvature. |
| 11 Random Motion | Appendix A: spectral graph theory, matrix-tree formulas, expansion and mixing; Appendix B: random matrices, the moment proof and the connection with zeta zeros. |
| 15 The Research Workshop | Appendices A–L: conjecture case studies in arithmetic, probability, geometry and algebra. Appendix E directs readers to the proofs and experiments in Volume 11, Appendix B. |

The former Companion's series catalog is supplied by the shared series page;
its separate book, citation database, index generator and cover dependency are
removed. Optional references promising later computing books are rewritten as
mathematical context. Cited companion results now name their main-volume appendix.
Review records and archived design discussions remain historical evidence, not an
active catalog.

## Publishing behavior

The library has main-series and problem-book filters. The site generator serves
only books with an existing `main.tex`, so stale PDFs cannot resurrect a removed
volume. The cache planner deletes removed and renamed book outputs when assembling
the next library; the rolling release is recreated from that complete assembly.
The art and subtitle generators contain nineteen books. A push to main is still
required for live release and Pages updates; local verification does not publish.

## Verification

The following checks were completed locally.

- All **15 publishing tests** pass, including stale download/reader removal,
  independent book caching, and appendix chapter/section/theorem/exercise numbering
  and reference links in digital editions.
- Volumes **0, 2, 3, 8, 9, 11 and 15** compiled through three PDF passes with no
  undefined or multiply defined references. All integrated labels, hint and
  solution targets were checked against their owning books.
- Both renamed covers compiled and passed text extraction in all **five sizes**;
  their rendered covers were visually reviewed.
- The nineteen-book cover-art generator and canonical subtitle check pass.
- **Higher Structures** completed the production pipeline: A4 and Kindle PDF,
  EPUB, reader, ebook covers, KDP listing and 184-page paperback with actual spine.
- A full Structures digital conversion confirms alphabetic appendix headings,
  theorem and exercise numbers. Its inherited unbraced binomial expressions still
  produce Pandoc math-conversion warnings; a complete production rebuild of every
  integrated EPUB was not performed in this session.
- `git diff --check` passes. Live release/Pages publication has not been triggered.
