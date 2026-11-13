# Volume 6 — Crossroads

*Arithmetic Meets Analysis.*

**Status of this file.** Blueprint of Volume 6 under the [master plan](MASTER-PLAN-V5-V15.md), 2026-11-10. It replaces the earlier specification. No proof named here has been verified.

**Series part.** II. Bridges. **Directory.** `volume6-crossroads`.

## Central question

What laws do the primes obey in bulk, and where does the picture of the primes as coin tosses first fit and first fail?

## Prerequisites

| From | What is used |
| --- | --- |
| Volume 2 | Dirichlet characters, Möbius inversion, Chebyshev's bounds, the Legendre sieve |
| Volume 3 | Orthogonality of characters of a finite abelian group |
| Volume 4 | Mean, variance, characteristic functions, the method of moments, Borel–Cantelli |
| Volume 5 | Partial summation, \(\zeta(2k)\), Stirling, Weyl's criterion, the Gauss sum, residues and the identity theorem, the Euler product and functional equation of \(\zeta\), Euler–Maclaurin, the transformation of \(\eta\) |

**Admitted, discharged later.** The functional equation of a primitive Dirichlet \(L\)-function, used only in the identity for Chebyshev's bias in Chapter 7 (`prop:biasidentity`); proved in Volume 13, Chapter 12. Tonelli's theorem where an interchange needs it; proved in Volume 7.

## Structure

Unchanged. The numbering of this volume is frozen: it is the most cited volume of the series.

| Ch. | Title | File | Action |
| --- | --- | --- | --- |
| | **Part I. Counting Primes** | | |
| 1 | Mertens's Theorems | `ch01-mertens.tex` | Keep |
| 2 | Arithmetic Functions on Average | `ch02-averages.tex` | Keep |
| 3 | Dirichlet Characters and \(L\)-Functions | `ch03-characters.tex` | Keep |
| 4 | Dirichlet's Theorem | `ch04-dirichlet.tex` | Keep |
| 5 | The Prime Number Theorem | `ch05-pnt.tex` | Keep |
| | **Part II. Zeros and Explicit Formulas** | | |
| 6 | The Zeros of \(\zeta\) | `ch06-zeros.tex` | Keep |
| 7 | The Explicit Formula and the Riemann Hypothesis | `ch07-explicit.tex` | Keep; one label |
| | **Part III. Sieves and Randomness** | | |
| 8 | Sieves | `ch08-sieves.tex` | Keep |
| 9 | The Erdős–Kac Theorem | `ch09-erdoskac.tex` | Keep |
| 10 | Random Models of the Primes | `ch10-random.tex` | Keep |
| 11 | Exponential Sums | `ch11-sums.tex` | Keep |
| 12 | A Taste of Modular Forms | `ch12-modular.tex` | Keep; two changes below |

No fourth part. Chapters 11 and 12 close Part III as they do now.

## Flagship theorems, proved in this volume

| Theorem | Label | Chapter |
| --- | --- | --- |
| Mertens's three theorems | | 1 |
| \(L(1,\chi)\ne0\); Dirichlet's theorem | | 3–4 |
| No zero of \(\zeta\) on \(\mathrm{Re}\,s=1\); Newman's tauberian theorem; the prime number theorem; the mean of \(\mu\); the prime number theorem in progressions | `thm:line`, `thm:newman`, `thm:pnt`, `thm:mobiussum`, `thm:pntap` | 5 |
| Stirling in the complex plane; Jensen; Borel–Carathéodory; local zero count; Hadamard's product for \(\xi\); Riemann–von Mangoldt; the classical zero-free region | `thm:stirlingc`, `thm:jensen`, `lem:borel`, `lem:localzeros`, `thm:hadamard`, `thm:rvm`, `thm:zerofree` | 6 |
| The explicit formula; the prime number theorem with error; von Koch's equivalence | `thm:explicit`, `thm:pnterror`, `thm:rhequiv` | 7 |
| Selberg's sieve; Brun–Titchmarsh; the large sieve inequality | `thm:selberg`, `thm:bt`, `thm:largesieve` | 8 |
| Turán–Kubilius; Erdős–Kac | `thm:tk`, `thm:erdoskac` | 9 |
| Weyl differencing; Weyl's inequality for squares; van der Corput; Pólya–Vinogradov | `thm:weylineq`, `thm:pv` | 11 |
| The fundamental domain of \(SL_2(\mathbb Z)\), both halves; dimension of spaces of modular forms; Hecke's multiplicativity of \(\tau\) | `thm:fundamental`, `thm:dimension`, `thm:hecke` | 12 |

## Stated without proof

| Statement | Heading must say |
| --- | --- |
| Maier's theorem (Chapter 10) | Quoted here, proved in Volume 15, Chapter 2 |
| The Poisson law for primes in short intervals | Conditional on the Hardy–Littlewood conjecture |
| Any percentage of zeros on the critical line (Chapter 6) | Quoted, with source and date, or removed |
| The functional equation of \(L(s,\chi)\) (Chapter 7) | Admitted, proved in Volume 13 |
| Modularity; the general theory of Hecke operators | Preview of Volume 13 |

## Climax

Two summits. The prime number theorem at the end of Part I. Then, in Parts II and III, the two faces of the series question: the explicit formula writes the primes as a sum of waves, one for each zero, and Erdős–Kac writes the number of prime factors as a Gaussian. Chapter 10 then states the first failure of the coin model.

## Motivation and history

Euler and Mertens, Dirichlet's 1837 memoir, Gauss's table of primes, Riemann, Hadamard and de la Vallée Poussin in 1896, Newman's 1980 proof, Selberg and Erdős, Kac's "primes play a game of chance", Cramér's model, Ramanujan's \(\tau\). Sources for every quotation.

## Examples and exercises

Each chapter carries a table or a count the reader can reproduce: Mertens's product to \(10^6\), the average order of \(d(n)\), the characters modulo 5 and 8, primes in the classes modulo 4, \(\pi(x)\) against \(\mathrm{Li}(x)\), the first zeros and the wave picture, twin-prime counts against the sieve bound, a histogram of \(\omega(n)\), gaps against the exponential law, \(\tau(n)\) modulo 691.

The long problem section that closes Chapter 12 is kept. Each problem names the chapters it uses and none uses a later volume.

## Figures and experiments

The staircase \(\psi(x)\) rebuilt from the first 10, 50 and 200 zeros. The histogram of \(\omega(n)\) near \(10^{9}\) against the bell curve, with the honest remark that convergence is slow. Every such figure is produced by a script in the repository and listed in the numerical-claims ledger.

## Changes from the current manuscript

**Preserve.** All twelve chapters and their order.

**Rewrite.** In Chapter 12, the theorem on \(\eta\) (`thm:eta`) cites Volume 5, Chapter 12. Its present proof may stay if it uses a different method and is headed "second proof". In Chapter 12, `thm:fundamental` gains its second half: two interior points of the domain are never equivalent, and boundary points are identified only by \(T\) and \(S\) (decision D-20).

**Label.** `prop:biasidentity` as resting on an admitted functional equation. The remark on Maier as quoted. The percentage of zeros on the line.

**Remove.** Hand-typed citations of "Volume 13, Chapter 1" and other stale numbers. The claim, if present, that Buchstab's function was "met in sieve theory" earlier.

**Missing.** One sentence at the first \(q=e^{2\pi i\tau}\). One sentence in the preface stating the series question in the form this volume can touch.

## Links

**From Volume 5.** Every instrument.
**To Volume 8.** The zero-free line is the input of the second proof of the prime number theorem.
**To Volume 9.** The fundamental domain.
**To Volume 13.** Dirichlet \(L\)-functions and the taste of modular forms.
**To Volume 14.** This volume stops at the classical zero-free region, Selberg's sieve and Weyl sums for smooth phases. Volume 14 starts there.
**To Volume 15.** The Maier remark and Cramér's model are the questions Volume 15 answers. Volume 15 gives a second proof of Erdős–Kac.

## Size

About 8,250 source lines, of which about 2,000 are the closing problems. **Estimate, not measured:** 230–260 printed pages.

## Mathematical risks

1. The chain in Chapter 6 from Jensen to the zero-free region reads complete and is long. It carries Volumes 8, 14 and 15. It is the first verification target of the whole series.
2. Newman's theorem: the contour and the bound on the truncated integral.
3. The explicit formula: convergence of the sum over zeros and the meaning of the symmetric limit.
4. Erdős–Kac: the truncation of primes and the moment comparison, with uniformity.
5. Brun–Titchmarsh: the constant, and which form is used later by Volume 14.

## Acceptance requirements

- Structure and numbering unchanged.
- Verification records for every label in the flagship table, Chapter 5–7 first.
- The admitted functional equation labelled at its single use, and the ledger row pointing to Volume 13, `cor:dirichletFE`.
- Second half of `thm:fundamental` written and verified; Volumes 9 and 13 cite it.
- Every problem of the closing section checked against rule R1.
- The ten editorial standards of the master plan, section 6.5.
