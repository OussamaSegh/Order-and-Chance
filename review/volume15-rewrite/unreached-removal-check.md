# Written check before removing the unreached files of Volume 15

Decision D-29 of the master plan: Volume 15 is the fourteen chapters reached from `main.tex`. The files in `volume15-order-and-chance/chapters/` that `main.tex` does not reach never printed. Each is removed only after the check below: its unique content is printed elsewhere in the series, or it is listed as dropped with the reason the blueprint gives. `python3 review/volume15-rewrite/reached.py --unreached` lists them; after this commit it prints nothing.

| File | Content | Where it lives now, or why it is dropped |
| --- | --- | --- |
| `ch01-research.tex` | How research works; dissociated sets, the counting bound, Erdős–Moser | Dropped (blueprint: not this meeting). The research method survives as the reading section of Chapter 14 |
| `ch02-reading.tex` | How to read a paper; Dubroff–Fox–Xu | The three-pass reading is Chapter 14, Section "Three passes", practised on Maier and on Selberg (both proved in this volume). The Dubroff–Fox–Xu paper is dropped |
| `ch03-shuffling.tex` | Bayer–Diaconis riffle cutoff | Printed in Volume 11, Chapter 13 (`riffle-cutoff.tex`), and Volume 4, Theorem 9.9 (`thm:bayerdiaconis`) |
| `ch04-selberg.tex` | Selberg's theorem at many points: the covariance of prime sums, a multipoint CLT | The covariance becomes an exercise of Chapter 11 (`ex:multipoint`), as the blueprint asks |
| `ch05-sandpiles.tex` | Random groups: cokernel moments, corank law, sandpile groups | The symmetric-cokernel moments and the corank law are in Chapter 7 (`ra-symmoments.tex`); the sandpile tour is dropped |
| `ch06-chaos.tex` | Better than square root: the critical branching random walk | The proved half-moment is printed in Volume 12 (`brw-halfmoment.tex`); Harper's reading map is dropped |
| `ch07-experiments.tex` | BBP digit extraction, LLL | BBP is printed in Volume 5, Chapter 4 (`bbp-borwein.tex`). LLL is dropped |
| `ch08-heuristics.tex` | Three cubes: Verebrusov–Mahler identities, local densities | The identities are printed in Volume 13, Chapter 5 (`ch05-cyclotomic.tex`); Heath-Brown's prediction is a labelled conjecture there |
| `ch09-lean.tex` | Proof assistants, Curry–Howard | Dropped: no volume of the series is about proof assistants |
| `ch10-writing.tex` | Writing mathematics; the polygonal Jordan theorem | The polygonal Jordan theorem is printed in Volume 7 (`jordan-polygon.tex`); the essay is dropped |
| `ch11-problems.tex` | Problems to work on (Singmaster, Rosa, Kelly, Lehmer, Gauss–Lucas) | Dropped, except the two projects kept in Chapter 14 |
| `ch12-projects.tex` | Five projects | Project 2 (prime factors in short intervals) is Chapter 14's first project; the others are dropped |
| `conjectures-ch01-born.tex` | Borwein integrals, Pólya, Mertens, π(x) − li(x) | Borwein integrals and BBP: Volume 5, `bbp-borwein.tex`. Mertens' and Skewes' story: Volume 6. Pólya's conjecture is dropped |
| `conjectures-ch02-twins.tex` | Twins and gaps tour | Volumes 6 and 14 own the theorems (Brun, GPY, Maynard, the proved bound 4580 of Volume 14, Theorem 9.8); Westzynthius is Exercise `ex:westzynthius` of Chapter 2 |
| `conjectures-ch03-goldbach.tex` | Goldbach tour, Schnirelmann | Vinogradov's theorem is Volume 14, Corollary 7.5; Schnirelmann is a remark in Chapter 6 |
| `conjectures-ch04-riemann.tex` | RH tour: Robin, Lagarias | Dropped; Volume 6 states the Riemann hypothesis and its prime-counting form |
| `conjectures-ch05-zetarmt.tex` | A two-line pointer | Dropped; Chapter 9 replaces it |
| `conjectures-ch06-collatz.tex` | Collatz | Dropped (no title asks for it) |
| `conjectures-ch07-hadamard.tex` | Hadamard matrices; Sylvester, Paley | Sylvester and Paley are printed in Volume 3 (`paley.tex`); the tour is dropped |
| `conjectures-ch08-geometric.tex` | Unit distances, Erdős–Szekeres, Gilmer | Gilmer's method is printed in Volume 4 (`gilmer.tex`); Erdős–Szekeres in Volume 1; the rest is dropped |
| `conjectures-ch09-abc.tex` | abc, Mason–Stothers | Mason–Stothers and Fermat for polynomials are printed in Volume 13, Chapter 5 |
| `conjectures-ch10-bsd.tex`, `conjectures-ch11-random.tex`, `conjectures-ch12-algebra.tex` | Tours | Dropped. Volume 13 and Chapters 4, 7 and 8 of this volume state what is proved and what is not |

Figures. The 35 files in `volume15-order-and-chance/figures/` that no reached chapter inputs (`reached.py --figures`) go with them.

Tests. `tools/test_cross_volume_citations.py` checked one citation inside `ch09-lean.tex` and one inside `ch08-heuristics.tex`; those two assertions are removed with the files. The other assertions of the same tests are unchanged.

Notebooks in `python/volume15/` are not part of the book and are not touched by this pass.
