# Volume 8 — Analysis

*Operators, Spectra and Transforms.*

**Status of this file.** Blueprint of Volume 8 under the [master plan](MASTER-PLAN-V5-V15.md), 2026-11-10. It replaces the earlier specification, which described ten chapters; the manuscript prints twenty-five. Chapter numbers below are the numbers after decisions D-16 and D-18 are applied. No proof named here has been verified.

**Series part.** III. Analysis and Geometry. **Directory.** `volume8-analysis`.

## Central question

What lives in a space of functions? A matrix has eigenvalues. An operator has a spectrum, and a group has a Fourier transform. The volume follows the word "spectrum" from a symmetric matrix, through a graph, to a compact operator, and then follows "transform" from the line to a finite group, to \(\mathbb Q_p\), to the prime number theorem.

## Prerequisites

| From | What is used |
| --- | --- |
| Volume 7 | All of it. In particular Baire, \(L^p\), Fubini, Radon–Nikodym, Riesz representation, and \(\mathbb Q_p\) with \(\mathbb Z_p\) compact (Chapter 2) |
| Volume 5 | Fourier series, the Fourier transform of Chapter 8, residues and the identity theorem, the functional equation of \(\zeta\) |
| Volume 3 | Groups, characters of finite abelian groups, the linear algebra of its appendices |
| Volume 6 | The zero-free line `thm:line`, as the input of Chapter 15. Zero counts, in the problems of Chapter 16 |
| Volume 1 | Linear algebra |

No statement of Volumes 9–15 is used as a premise. Today the volume uses Volume 9 (Weyl integration) and Volume 11 (Stein's lemma, Gaussian concentration, Lyapunov's theorem) in the two random-matrix chapters; those chapters leave.

## Structure

| Ch. | Title | File | Action |
| --- | --- | --- | --- |
| | **Part I. Banach and Hilbert Spaces** | | |
| 1 | Banach Spaces | `ch01-banach.tex` | Keep |
| 2 | Hilbert Spaces | `ch02-hilbert.tex` | Keep |
| | **Part II. Spectral Theory** | | |
| 3 | The Spectral Theorem and Its Relatives | `linear-ch05-spectral.tex` | Keep, moved to the head of the part |
| 4 | Singular Values | `linear-ch06-svd.tex` | Keep |
| 5 | Graphs through Their Eigenvalues | `linear-ch08-graphs.tex` | Keep |
| 6 | Cuts, Mixing and Expansion | `spectral-expansion.tex` | Keep |
| 7 | Expanders and Ramanujan Graphs | `ch09-expanders.tex` | Keep |
| 8 | Operators, Spectra and Banach Algebras | `ch03-operators.tex` | Keep |
| 9 | The Spectral Theorem for Compact Operators | `ch04-spectral.tex` | Keep. Title made distinct from Chapter 3 |
| | **Part III. Fourier and Tauberian Methods** | | |
| 10 | The Fourier Transform | `ch05-fourier.tex` | Keep |
| 11 | Distributions and Sobolev Spaces | `ch06-distributions.tex` | Keep |
| 12 | Fourier Analysis on Finite Abelian Groups | `ch07-finite.tex` | Keep |
| 13 | Haar Measure, Duality and the \(p\)-adic Numbers | `ch08-haar.tex` | Keep here (D-17). Rewrite one section opening |
| 14 | Cauchy's Theorem, Growth and Mellin Inversion | `ch09-complex.tex` | Keep |
| 15 | Tauberian Theorems | `ch10-tauberian.tex` | Keep |
| 16 | The Values of Zeta (problems) | `ch11-harder.tex` | Keep; audit against rule R1 |
| | **Appendices** | | |
| A | Spaces, Quotients and Duality | `linear-ch01-duality.tex` | Becomes an appendix |
| B | Determinants as Volume | `linear-ch02-volume.tex` | Becomes an appendix |
| C | Eigenvalues and Invariant Subspaces | `linear-ch03-eigen.tex` | Becomes an appendix |
| D | Inner Products and Projections | `linear-ch04-inner.tex` | Becomes an appendix |
| E | Inequalities between Matrices | `linear-ch11-inequalities.tex` | Becomes an appendix |
| F | Linear Dynamics | `linear-ch12-dynamics.tex` | Becomes an appendix |

**Leaves the volume.** "Random Matrices I: The Semicircle" (`ch10-semicircle.tex`) and "Random Matrices II: Unitary Matrices and the Zeros of Zeta" (`ch11-cue.tex`) go to Volume 12, Chapters 9 and 10 (D-16).

**The appendices are premises.** They are part of the volume and may be cited by any chapter and by later volumes (rule R1). Appendices A–D hold the linear algebra Chapters 3–9 assume beyond Volume 1; Appendices E and F are cited by Volumes 9, 10 and 12. Each appendix opens with one line saying what it assumes and who uses it. A reader who knows linear algebra reads the main path of sixteen chapters.

**Why the graphs stay.** The three graph chapters need only the finite-dimensional spectral theorem and Courant–Fischer. A Ramanujan graph is one whose spectrum satisfies a Riemann hypothesis, with a zeta function and a prime number theorem. It is the volume's subtitle in miniature, and it prepares the reader for the infinite-dimensional case that follows.

## Essential definitions and results

Banach space, dual, weak topologies. Hilbert space, orthonormal basis, reproducing kernel. Spectrum, resolvent, compact operator. Schwartz space, tempered distribution, Sobolev space. Dual group, Haar measure. Order of an entire function, Mellin transform. Summability methods.

## Flagship theorems, proved in this volume

| Theorem | Label | Chapter |
| --- | --- | --- |
| Hahn–Banach; uniform boundedness; open mapping; closed graph; the dual of \(L^p\); Banach–Alaoglu | | 1 |
| Projection theorem; Riesz–Fréchet; von Neumann's mean ergodic theorem | | 2 |
| Spectral theorem for normal matrices; Courant–Fischer; Cauchy interlacing; Weyl's inequalities; Hoffman–Wielandt | | 3 |
| Singular value decomposition; Eckart–Young | | 4 |
| Hoffman's ratio bound; Huang's theorem | | 5 |
| Cheeger's inequality; Alon–Boppana | | 6 |
| Expander mixing; Ihara–Bass; the prime number theorem for graphs | | 7 |
| Fredholm alternative; Gelfand's spectral radius formula; Wiener's lemma | | 8 |
| Spectral theorem for compact self-adjoint operators; Sturm–Liouville; Mercer; the continuous functional calculus | `thm:spectralcompact` | 9 |
| Fourier inversion; Plancherel; Hausdorff–Young; Poisson summation for lattices | | 10 |
| Sobolev embedding; Rellich; Lax–Milgram | | 11 |
| Duality for finite abelian groups; uncertainty (Donoho–Stark, Tao); quadratic reciprocity by Fourier analysis; Meshulam's bound | `thm:qr`, `thm:meshulam` | 12 |
| Existence and uniqueness of Haar measure in the cases the chapter constructs; Haar measure on \(\mathbb Q_p\); \(\mathbb Q_p\) is self-dual; Fourier inversion on \(\mathbb Q_p\) | `prop:haarqp`, `thm:qpselfdual`, `thm:qpfourier` | 13 |
| Cauchy's theorem in homology form; Phragmén–Lindelöf; Hadamard factorisation; Mellin inversion | `thm:hadamardgen`, `thm:mellininv` | 14 |
| Tauber; Hardy–Littlewood–Karamata; Wiener's tauberian theorem; Wiener–Ikehara; the prime number theorem, second proof | `thm:ikehara`, `cor:pntikehara` | 15 |

## Stated without proof

| Statement | Heading must say |
| --- | --- |
| The spectral theorem for general bounded or unbounded self-adjoint operators | Quoted. The blurb and preface must not claim it |
| The converse direction of Bochner's theorem | Not proved here |
| Existence of Ramanujan graphs of every degree; Friedman's theorem | Quoted |
| Kesten's theorem; the matrix-tree theorem | Preview of Volume 12 |
| Bohr–Jessen's limiting distribution (Chapter 16) | Preview of Volume 15. No problem may assert it |
| Carleson's theorem | Quoted |

## Climax

Part II ends on the compact spectral theorem: the vibrating string has a list of frequencies for the same reason a symmetric matrix has eigenvalues. Part III ends on Wiener–Ikehara: the prime number theorem a second time, from the same zero-free line and a different machine.

## Motivation and history

Banach's Lwów school, Hilbert's 1906 spectral theory, von Neumann, Schwartz, Wiener's 1932 tauberian memoir and Ikehara, Hensel and Tate for the \(p\)-adic dual, Lubotzky–Phillips–Sarnak and Margulis for Ramanujan graphs, Harald Bohr for the values of \(\zeta\).

## Examples and exercises

A discontinuous linear map; weak convergence without norm convergence; the Petersen graph's spectrum; a string's modes; the Gaussian and the Hermite functions; a corner differentiated as a distribution; a cap set; the measure of the squares in \(\mathbb Z_p\) (moved, see below); a Mellin inversion that recovers a sum; an Abel summable series that does not converge.

Three levels of exercises in each chapter and each appendix. Chapter 16 is the problem chapter.

## Figures and experiments

Spectra of a random regular graph against the Ramanujan interval; eigenfunctions of a string; the cloud of values \(\zeta(2+it)\). Each from a script in the repository and listed in the ledger.

## Changes from the current manuscript

**Preserve.** Every chapter that stays, as written.

**Relocate.** The two random-matrix chapters to Volume 12. Six linear-algebra chapters to the appendices. Within Part II, the order of the table above.

**Rewrite.** Chapter 13, section on \(\mathbb Q_p\): the sentences "Volume 13 constructs \(\mathbb Q_p\)" are wrong. The construction is Volume 7, Chapter 2, which is all the section needs. The exercise that computes the measure of the squares in \(\mathbb Z_p\) uses the criterion for squares, which is Volume 13; it moves to Volume 13, Chapter 8, as an exercise there.

**Remove.** Citations of Volumes 9 and 11 that leave with the matrix chapters. "Perron's formula" from the preface if the name is not used. Any claim of the unbounded spectral theorem in the blurb.

**Missing.** The opening line of each appendix. One sentence in Chapter 14 and one in Volume 5, Chapter 9, saying which complex analysis each owns. In Chapter 1, the complex case of the \(L^p\) dual written out if it is still a one-line reduction.

## Links

**From Volume 7.** The spaces.
**To Volume 9.** Haar measure and the complex analysis the Riemann mapping theorem uses. Nothing flows back.
**To Volume 10.** Compact operators, for compact groups.
**To Volume 11.** The mean ergodic theorem and compact operators, for Furstenberg's proof of Roth's theorem.
**To Volume 12.** Hoffman–Wielandt and the graph spectra, for the semicircle and for walks on networks.
**To Volume 13.** Haar measure, self-duality and Fourier inversion on \(\mathbb Q_p\), cited by the chapter on Tate's thesis (D-23).
**To Volumes 14 and 15.** Meshulam's bound; Mellin inversion; Hadamard factorisation.

## Size

About 12,870 source lines after the matrix chapters leave: about 8,700 in the main path and about 4,160 in the appendices. **Estimates, not measured:** 250–280 printed pages for the main path, 110–130 for the appendices, 360–400 in all. This will be the longest volume of the series. That is accepted (D-19): no theorem is removed for length, and the reader's path is of ordinary length.

## Mathematical risks

1. A main chapter may use an appendix result whose own proof uses a later main chapter. The dependency checker must show there is none. The likeliest place is Appendix D against Chapters 3–4.
2. Chapter 13 re-read against Volume 7 only: every property of \(\mathbb Q_p\) used must be in `thm:Qp` or its corollary.
3. Wiener's tauberian theorem and the local inverse lemma, repaired once already.
4. The \(L^p\) dual in the complex case.
5. Chapter 16's solutions: 22 problems citing Volumes 5, 6 and 7 heavily and Volumes 14 and 15 a few times. Each forward citation must be a preview.
6. Ihara–Bass and the graph prime number theorem: the counting of primitive cycles.
7. Chapter 7 states a theorem of Kesten that Volume 12, Chapter 8 also proves (`thm:kesten`). Compare the two statements. The home is Volume 12; here it is a preview, or a distinct statement with its own name.
8. Von Neumann's mean ergodic theorem appears in Chapter 2 and again in Volume 11, Chapter 10. The home is here; Volume 11 cites it.

## Acceptance requirements

- Structure equals the table above. The catalog part names are unchanged.
- No premise from Volumes 9–15. The dependency ledger shows none.
- Verification records for: Hahn–Banach, the three Baire theorems, `thm:spectralcompact`, Plancherel, `thm:qr`, `thm:meshulam`, `prop:haarqp`, `thm:qpselfdual`, `thm:qpfourier`, `thm:hadamardgen`, `thm:mellininv`, `thm:ikehara`, `cor:pntikehara`, Cheeger, Alon–Boppana, Hoffman–Wielandt.
- Every citation of this volume from Volumes 9–15 resolves by label after the reorder.
- Measured pages recorded for the main path and for the appendices separately.
- Blurb and preface checked against the list of statements not proved.
- The ten editorial standards of the master plan, section 6.5.
