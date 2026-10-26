# Tome 0 expansion: handoff

Working notes for the thread that continues the expansion of Tome 0 ("Back in Shape").
Delete this file (and `handoff-*`) when the expansion is finished and published.

Plan document (chapter by chapter, with the design rules): https://claude.ai/artifact/85jfRcfjmrcnmwSnTLonEK

## State of the chapters

| Chapter | Status | What changed |
|---|---|---|
| 1 Sums, binomials, induction | **done** | Sourced story (Sartorius 1856, Nicomachus, Levi ben Gershon 1321, Pascal 1654/65); "Sums, and how to write them"; three flavours of induction, trominoes; telescoping; binomials, Vandermonde, hockey stick; new numbered sections: polynomials in the binomial basis (Prop 1.7, Thm 1.8 Newton forward differences, Cor 1.9), lattice paths (Prop 1.10); exercises 1.10–1.17 with hints/solutions; challenge box; 5 figures |
| 2 Complex numbers, roots of unity | **done** | Story (Cardano 1545, Bombelli 1572, Euler's i 1777, Wessel 1797, Argand 1806, Gauss 1831); complex numbers from scratch; exponential form; roots of unity; filter; new: geometry with complex numbers (Prop 2.7 equilateral criterion, Napoleon), cyclotomic polynomials (Def 2.8, Prop 2.9, Migotti); exercises 2.9–2.15; challenge box; 5 figures |
| 3 Polynomials | **done** | Story (Mengoli 1650, J. Bernoulli 1689, Euler 1734/35, Chebyshev 1854); polynomials from scratch (Horner, formal derivative); long division; multiple roots; d'Alembert–Gauss history; Viète (now labelled `prop:viete`); Lagrange + Shamir secret sharing; Chebyshev closed form, equioscillation; reduction mod p; new numbered sections: symmetric functions (Prop 3.10 Newton's identities, Thm 3.11 fundamental theorem of symmetric polynomials), real roots (Thm 3.12 Descartes' rule, Thm 3.13 Gauss–Lucas); exercises 3.9–3.18 (incl. discriminant of the cubic, log-concavity, Mason–Stothers + Fermat for polynomials); challenge box; 5 figures |
| 4 Inequalities | **done** | Story (Cauchy 1821, Bunyakovsky 1859, Schwarz 1885, Jensen 1906); inequalities from scratch (rules, squares, triangle inequality, Bernoulli); examples; new numbered section "More means, more norms": Thm 4.6 power means (monotone in p, limits), Prop 4.7 Chebyshev's sum inequality, Thm 4.8 Minkowski; exercises 4.10–4.18 (means, Bernoulli, Lagrange identity, Cauchy's forward–backward induction, Heron, entropy, Chebyshev application, Schur); challenge box (e optimal in Carleman, Hardy, regular polygon); 4 figures |
| 5 Sequences and series | to do | Plan: story (Cauchy, Weierstrass, Zeno/Oresme), from-scratch section on limits (epsilon definition explained slowly), prove IVT, EVT, Heine, Rolle, MVT (currently admitted in the preface), Abel summation and the Dirichlet test, comparison/ratio/root tests, examples; figures: epsilon-strip, Cesàro, harmonic series blocks (Oresme), alternating series, Gamma; exercises 5.8–5.15 |
| 6 Integration and Taylor | to do | Plan: L'Hôpital (proved), Gamma function properties, trapezoid error, Stirling next term, Niven's proof that π is irrational; figures: Riemann sums, Taylor polynomials of sin/exp, Wallis, trapezoid; exercises 6.8–6.15 |
| 7 Linear algebra | to do | Plan: determinant as volume (figure), Gram–Schmidt, adjugate and Cayley–Hamilton, Cauchy determinant, Vandermonde use; story (Cayley, Hamilton, Sylvester); exercises 7.9–7.16 |
| 8 Counting and probability | to do | Plan: binomial/geometric/hypergeometric laws, Markov and Chebyshev inequalities, weak law of large numbers, Ramsey bound R(k,k) > 2^{k/2}, Monty Hall, birthday problem; story (Pascal–Fermat 1654, de Moivre, Erdős); exercises 8.9–8.16 |
| Preface | to do | Reduce the list of admitted facts (IVT, EVT, MVT now proved in Ch. 5 once written); mention the new sections; only content/goal/beauty |
| blurb.tex, kdp.md | to do | Update page count, new topics; keep ISBN 9798165526770 |

## Rules followed so far (keep them)

- **Numbering stays stable.** Every numbered theorem/proposition/example/exercise of the first edition keeps its number (later tomes cite ~55 Tome 0 results by number). New numbered results only *after* the last existing number of each chapter. Insertions earlier in a chapter use the unnumbered environments `theoremx`, `propositionx`, `lemmax`, `corollaryx`, `definitionx`, `examplex` (defined in `main.tex`). New exercises go under `\subsection*{Further exercises}` after the last existing one. Figures are renumbered freely.
- `handoff-numbering-first-edition.txt` is the label → number map of the first edition; `handoff-quick.sh` builds A4 and print into `/home/claude/b0` and reports pages, overfull boxes > 10pt, multiply defined labels, undefined references and any numbering change (adjust the paths at the top). Last result: A4 113 pages, print 174 pages, no overfull, "numbering changes vs first edition: none".
- Unlabelled numbered items that must keep their place: Example 1.2, 1.4, 2.2, 2.6, Prop 3.4 (now `prop:viete`), Example 7.8, 8.5.
- `challenge` tcolorbox (defined in `main.tex`) holds 3 harder problems per chapter, with `\subsection*{Notes on the challenges}` after the solutions.
- Every theorem fully proved; solutions start with `\idea` then `\writeup`; "Pause and think" boxes before key results; every quote/date/anecdote sourced in "Sources and further reading" (MacTutor checked for dates).
- Shared files touched: `tools/epub.lua` (title for `challenge`; strips pandoc's numbering from the unnumbered environments), `tools/epub.css`, `tools/reader.css` (`.challenge` style). The EPUB pipeline was tested on Chapter 1 after these changes.
- Figure generators live in `/mnt/project-files/math-book/tome0-scripts/figs_t0c0N.py` (project Library); they write TikZ into `tome0-back-in-shape/figures/`. Copies are not in the repo.
- All numbers in new examples/exercises were checked in Python (sympy/numpy).

## Photo wishlist (public domain or free licence; credit on the figure)

The previous thread's network blocked Commons. Use `https://commons.wikimedia.org/wiki/Special:FilePath/<File>?width=1200` and check the licence on each file page. Place each portrait as a small `wrapfigure` or a `figure` next to the story paragraph that names the person, with a caption "Name (dates). Painter/photographer, year. Public domain, via Wikimedia Commons" (or the CC licence and author).

- Ch. 1: Carl Friedrich Gauss (`Carl Friedrich Gauss.jpg`, Jensen 1840); Blaise Pascal (`Blaise Pascal Versailles.JPG`); Pascal's triangle as printed in the 1665 *Traité* (`TrianguloPascal.jpg` or similar).
- Ch. 2: Gerolamo Cardano (`Gerolamo Cardano.jpg`); Leonhard Euler (`Leonhard Euler.jpg`, Handmann 1753); Caspar Wessel's 1797 figure if a scan exists; Gauss's 17-gon diary page (`Gauss Tagebuch.jpg`?).
- Ch. 3: Pafnuty Chebyshev (`Pafnuty Chebyshev.jpg`); Jean le Rond d'Alembert (de La Tour pastel); René Descartes (Frans Hals, `Frans Hals - Portret van René Descartes.jpg`); Euler.
- Ch. 4: Augustin-Louis Cauchy (`Augustin-Louis Cauchy 1901.jpg`); Johan Jensen (check Commons); Hermann Minkowski (`Hermann Minkowski.jpg`); Viktor Bunyakovsky.
- Ch. 5: Cauchy; Karl Weierstrass; Nicole Oresme (manuscript miniature); Niels Henrik Abel.
- Ch. 6: Brook Taylor; James Stirling / John Wallis; Bernhard Riemann.
- Ch. 7: Arthur Cayley; William Rowan Hamilton; James Joseph Sylvester; Alexandre-Théophile Vandermonde.
- Ch. 8: Pascal and Fermat (1654 letters); Abraham de Moivre; Jacob Bernoulli; Paul Erdős (`Erdos head budapest fall 1992.jpg`, CC BY-SA 2.5, credit Kmhkmh).

## Finishing steps (unchanged from the plan)

1. Chapters 5–8 as above, each: story, from-scratch section, new numbered sections after the last existing number, 3–5 figures, 6–8 new exercises with hints and full solutions, challenge box with notes, extended sources.
2. Preface, `blurb.tex`, `kdp.md`.
3. Run the notebooks in `python/tome0/` (unchanged so far; add cells for the new material if useful).
4. `./build.sh tome0-back-in-shape`; check logs (no multiply defined labels, no overfull > 10pt in A4, pandoc clean); note the print page count: the wrap cover spine is rebuilt from it.
5. Push to main (pull --rebase first), wait for GitHub Actions, verify release "books" and Pages, email the user the links from Gmail, and tell them to re-upload **both** the print PDF and the cover wrap to KDP (the spine width changed).
