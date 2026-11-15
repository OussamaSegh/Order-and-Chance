# Book 10 — Abstraction

*Categories, Algebra and Homology.* Actual directory: `volume10-abstraction`.
The printed source order in `main.tex` is authoritative. This plan supersedes the
obsolete blueprint that numbered the tensor chapter differently and still included
shuffling, which belongs to Volume 11.

## Reader and promise

A serious reader studying independently should be able to calculate with the
objects before depending on their abstract properties. The volume joins maps,
tensors, rings, resolutions and representations. Its capstones prove three
connections in usable detail: regular sequences give computable resolutions;
cochains and derived functors describe the same group cohomology; commuting
symmetries explain the decomposition of tensor powers.

Prerequisites are the actual earlier-series algebra/characters, topology and
integration, Hilbert spaces, and geometry/homology cited in the current preface.
Every new proof checks its dependencies in printed order. No proof uses Volume 11
or later. No general schemes, spectral sequences or derived categories are added.
Schur–Weyl is proved over the complex numbers; no modular extension is promised.

## Printed contents and teaching additions

| Part | Chapter | Subject and added worked-example focus |
| --- | --- | --- |
| I Categories | 1 Categories | Explicit universal maps and naturality |
| I | 2 Tensors and the Cost of Multiplying Matrices | Vectorisation, rank and Strassen calculations |
| I | 3 Tensors and Exactness | Presentations and what tensoring loses |
| II Commutative Algebra | 4 Noetherian Rings and Hilbert’s Theorems | Polynomial systems, reduction and zero sets |
| II | 5 Localisation and Dimension | Elements/primes under localisation and dimension |
| II | 6 Dedekind Domains | Fractional ideals and explicit prime factorisation |
| II | 7 Homological Algebra | Choosing resolutions, maps, kernels, Tor and Ext |
| III Representations | 8 Group Cohomology | Cocycles, sections and multiplication laws |
| III | 9 Semisimple Algebras and Induction | Induction, restriction and double cosets |
| III | 10 The Symmetric Group | Tableaux, dimensions, characters and operators |
| III | 11 Compact Groups | Weights, characters and finite trace moments |
| IV Abstraction at Work | 12 Resolutions You Can Compute | Mapping cones, regular sequences and general Koszul complexes |
| IV | 13 Group Cohomology Through Resolutions | Bar/periodic resolutions, derived-functor comparison and inflation–restriction |
| IV | 14 Tensor Powers and Schur–Weyl Duality | Commuting actions, double centralisers, tensor decomposition and moments |

There are no appendices. Existing chapter, section, statement, exercise, equation
and figure numbers stay unchanged. Two integrated unnumbered worked examples and
four appended exercises strengthen each of Chapters 1–11. No new numbered formal
statement or section is inserted there. Existing theorem/proof/exercise text is
protected unless a genuine correction is explicitly recorded and reviewed.

## New chapter contracts

### 12. Resolutions You Can Compute

Use Chapter 7's already proved comparison and homotopy theorems. Introduce mapping
cones, exterior-power signs and regular sequences, with a proper-ideal convention.
Prove Koszul exactness by induction, and compute Tor with the residue field and
Ext into the polynomial ring, including zero variables and arbitrary
characteristic. Distinguish vector-space identifications from unproved algebra
structure. Give zero-divisor counterexamples. The final multipart exercise builds
the three-variable residue-field resolution and computes its consequences.

### 13. Group Cohomology Through Resolutions

For discrete groups and left integral group-ring modules, construct the free
unnormalised bar resolution; its contracting homotopy is on underlying abelian
groups. Prove the natural H^n=Ext comparison in all degrees, including degree zero.
Prove the cyclic periodic resolution, including the trivial group, and calculate
trivial and sign actions. For a normal subgroup and trivial coefficient module,
prove the low-degree five-term inflation–restriction sequence directly from
cochains, including choice independence and exactness. No terminal surjectivity
or spectral-sequence machinery is claimed. The final exercise compares split and
nonsplit cyclic extensions.

### 14. Tensor Powers and Schur–Weyl Duality

Work over C, dimension n≥1 and tensor degree d≥0. Prove the commuting actions and
finite-dimensional semisimple double-centraliser theorem. Prove the full joint
decomposition, supplying local identification lemmas for Specht and unitary
factors rather than quoting unproved highest-weight/invariant theory. Include
d=0, n=1 and n<d. The final exercise decomposes (C²) tensor 4, constructs character
projectors, verifies dimensions 5+9+2=16 and derives the eighth trace moment 14.
The final bridge names Volume 11, Randomness, with its correct series subtitle.

## Exercises, illustrations and reading routes

Add exactly 68 exercises: four in each existing chapter and eight in each new
chapter. Existing additions mix calculation, conceptual proof, hypothesis-testing
counterexample and application, with one basic/two intermediate/one advanced.
Each new chapter has two basic/three intermediate/three advanced exercises; its
last advanced exercise is the guided multipart capstone. Every exercise has a
fresh label, stars, useful hint and full idea/writeup solution. Append all additions
after current lists, preserving all 116 existing exercise numbers. Final total 184.

Retain all 34 existing mathematical figures and the credited Hilbert photograph.
Add two figures in each capstone: Koszul signs and zero-divisor obstruction;
resolution comparison and extension/transgression; commuting tensor actions and
joint decomposition blocks. Final mathematical figure total 40. No decorative
photographs, cover art or typography changes.

Front matter supplies a prerequisite map and commutative-algebra, homological and
representation reading routes. Paths name all needed earlier chapters; they do
not invite skipping an unproved prerequisite. Preface, blurb and listing describe
the actual expanded contents. Reader-facing copy presents the book as a first
edition, without revision history or companion-notebook promises.

## Production and evidence

Target 380–450 print pages, with 600 as the hard ceiling. Aim for 32–36 pages in
each new chapter including examples/exercises/hints/solutions, and roughly 4–5
added pages per existing chapter. Do not pad or compress typography to force a
count. Preserve all identifiers and leave an unassigned paperback ISBN blank.

Keep the published PR #245 baseline and historical review scripts intact. New
expansion audits compare the current immutable baseline with 14 chapters, 184
exercises, 40 figures, stable existing numbers and unchanged protected blocks.
CI runs that audit after building Volume 10. Separate reviewers read all additions
and affected old arguments, and every finding is fixed before acceptance.

Complete both exact volume builds, repository citation/register checks, rendered
PDF/figure/photo/cover/EPUB checks, exact-head green Actions, normal merge and
exact-merge release/Pages downloads. Record source SHAs, commands/exit codes,
actual page counts, sizes and hashes. Remote receipts stay on the PR without an
unnecessary publication source-change cycle. No Amazon KDP upload.
