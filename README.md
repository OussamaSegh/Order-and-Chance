# Order and Chance

*Number theory, algebra and probability, all proved.* By SEGHAIER Oussama & Claude Opus 5.5.

A series of books of beautiful mathematics, written for pleasure. Every chapter has graded exercises with complete solutions and a Python
companion notebook with computer-science applications.

## Download the books

- **Download page:** https://oussamasegh.github.io/numbers-structures-chance/
- **Direct links (latest build):**

  | Tome | PDF (A4) | PDF for phones | PDF for Kindle | EPUB |
  |---|---|---|---|---|
  | 0. Back in Shape | [PDF](https://github.com/OussamaSegh/numbers-structures-chance/releases/download/books/tome0-back-in-shape.pdf) | [phone](https://github.com/OussamaSegh/numbers-structures-chance/releases/download/books/tome0-back-in-shape-phone.pdf) | [Kindle](https://github.com/OussamaSegh/numbers-structures-chance/releases/download/books/tome0-back-in-shape-kindle.pdf) | [EPUB](https://github.com/OussamaSegh/numbers-structures-chance/releases/download/books/tome0-back-in-shape.epub) |
  | 1. The Integers | [PDF](https://github.com/OussamaSegh/numbers-structures-chance/releases/download/books/tome1-integers.pdf) | [phone](https://github.com/OussamaSegh/numbers-structures-chance/releases/download/books/tome1-integers-phone.pdf) | [Kindle](https://github.com/OussamaSegh/numbers-structures-chance/releases/download/books/tome1-integers-kindle.pdf) | [EPUB](https://github.com/OussamaSegh/numbers-structures-chance/releases/download/books/tome1-integers.epub) |
  | 2. Structures | [PDF](https://github.com/OussamaSegh/numbers-structures-chance/releases/download/books/tome2-structures.pdf) | [phone](https://github.com/OussamaSegh/numbers-structures-chance/releases/download/books/tome2-structures-phone.pdf) | [Kindle](https://github.com/OussamaSegh/numbers-structures-chance/releases/download/books/tome2-structures-kindle.pdf) | [EPUB](https://github.com/OussamaSegh/numbers-structures-chance/releases/download/books/tome2-structures.epub) |
  | 3. Chance | [PDF](https://github.com/OussamaSegh/numbers-structures-chance/releases/download/books/tome3-chance.pdf) | [phone](https://github.com/OussamaSegh/numbers-structures-chance/releases/download/books/tome3-chance-phone.pdf) | [Kindle](https://github.com/OussamaSegh/numbers-structures-chance/releases/download/books/tome3-chance-kindle.pdf) | [EPUB](https://github.com/OussamaSegh/numbers-structures-chance/releases/download/books/tome3-chance.epub) |
  | 4. The Art of Calculation | [PDF](https://github.com/OussamaSegh/numbers-structures-chance/releases/download/books/tome4-calculation.pdf) | [phone](https://github.com/OussamaSegh/numbers-structures-chance/releases/download/books/tome4-calculation-phone.pdf) | [Kindle](https://github.com/OussamaSegh/numbers-structures-chance/releases/download/books/tome4-calculation-kindle.pdf) | [EPUB](https://github.com/OussamaSegh/numbers-structures-chance/releases/download/books/tome4-calculation.epub) |
  | 5. Where It All Meets (in progress) | [PDF](https://github.com/OussamaSegh/numbers-structures-chance/releases/download/books/tome5-meets.pdf) | [phone](https://github.com/OussamaSegh/numbers-structures-chance/releases/download/books/tome5-meets-phone.pdf) | [Kindle](https://github.com/OussamaSegh/numbers-structures-chance/releases/download/books/tome5-meets-kindle.pdf) | [EPUB](https://github.com/OussamaSegh/numbers-structures-chance/releases/download/books/tome5-meets.epub) |

Each tome comes as three PDFs and an EPUB: A4 pages for a computer, tablet or printing; pages sized
for a large phone screen (Galaxy S25 Ultra, 9:19.5); pages sized for a 7-inch e-reader (Kindle
Paperwhite); and a reflowable EPUB with its cover, for any e-reader.

Every push to `main` rebuilds all the books and republishes them, both on the download page and on the
[`books` release](https://github.com/OussamaSegh/numbers-structures-chance/releases/tag/books).

## The series

| Tome | Title | Theme | Status |
| --- | --- | --- | --- |
| 0 | Back in Shape | The MP toolkit, relearned through problems | Complete draft (8 chapters) |
| 1 | The Integers | Elementary and algebraic number theory | Complete draft (12 chapters) |
| 2 | Structures | Groups, rings, fields, Galois, representations | Complete draft (12 chapters) |
| 3 | Chance | Probability, from counting to martingales | Complete draft (12 chapters) |
| 4 | The Art of Calculation | Series, integrals, special functions, asymptotics | Complete draft (12 chapters) |
| 5 | Where It All Meets | Analytic and probabilistic number theory | In progress (2 of 12 chapters) |
| 6 | Spaces | Sets, topology, measure and integration | In progress (5 of 11 chapters) |
| 7 | Analysis in Depth | Functional, harmonic and complex analysis | Planned |
| 8 | Shapes | Manifolds, algebraic topology, Lie groups | Planned |
| 9 | Structures II | Categories, commutative and homological algebra, representations | Planned |
| 10 | Chance II | Graduate probability: limit theorems, large deviations, concentration, ergodic theory | Planned |
| 11 | Random Motion | Brownian motion, stochastic calculus, random walks, random matrices | Planned |
| 12 | Arithmetic | Algebraic number theory, elliptic curves, modular forms | Planned |
| 13 | Primes in Depth | Analytic and additive number theory | Planned |
| 14 | Random Arithmetic | Probabilistic number theory and arithmetic statistics | Planned |
| 15 | The Research Workshop | Reading papers, experimenting, conjecturing, writing | Planned |
| C1 | Discrete Structures | Logic, combinatorics, graph theory, orders | Planned |
| C2 | Algorithms | Design and analysis, graph algorithms, linear programming, randomised and algebraic algorithms | Planned |
| C3 | Computation and Complexity | Automata, computability, Gödel, complexity classes, type theory | Planned |
| C4 | Information, Codes and Secrets | Information theory, error-correcting codes, cryptography, quantum computing | Planned |
| C5 | Data, Optimisation and Learning | Numerical linear algebra, convex optimisation, learning theory | Planned |

Tomes 0–5 are the foundations, 6–9 the graduate toolbox, and 10–15 the road to research in probability,
probabilistic number theory and algebra. The Computing track C1–C5 runs alongside and treats the
mathematics of computer science in the same spirit. The detailed plan of every tome lives in the series plan document.

## Layout

```
common/                 shared LaTeX preamble (PDF) and EPUB preamble
tome0-back-in-shape/    main.tex + chapters/*.tex (solutions at the end of each chapter)
tome1-integers/         same layout, one folder per tome
python/tomeN/           one Jupyter notebook per chapter
tools/                  EPUB conversion helpers (pandoc filter, CSS)
build.sh                builds dist/<tome>.pdf, -phone.pdf, -kindle.pdf and .epub
```

## Building

Requires `pdflatex` (TeX Live with `latex-extra` and `fonts-recommended`), `pandoc` 3 and Python 3.

```
./build.sh                       # every tome
./build.sh tome0-back-in-shape   # one tome
pip install -r requirements.txt  # for the notebooks
```

Every push builds the PDF and EPUB on GitHub Actions (the run's **books** artifact); pushes to `main` also publish them
to the download page and the `books` release. Figures are TikZ files in `<tome>/figures/`, converted to SVG for the EPUB. Each tome has a cover (`tools/cover.tex`, with the central picture written by `tools/cover_motifs.py` into `<tome>/cover-motif.tex`); it is the first page of the PDF and the EPUB cover image shown by e-readers. A new tome needs a picture in `tools/cover_motifs.py`.

## Writing conventions

- Exercises: `\begin{exercise}[$\star$]\label{ex:name} ... \end{exercise}`, graded $\star$ to $\star\star\star$.
- Solutions: `\begin{solution}{ex:name} ... \end{solution}` in the chapter's last section.
- Boxes: `reminder` (optional title), `beauty` (links to other tomes).
