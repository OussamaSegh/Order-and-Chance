# Numbers, Structures and Chance

A series of books of beautiful mathematics, written for pleasure by a former MPSI/MP\* student coming back
to mathematics, with Claude. Every chapter has graded exercises with complete solutions and a Python
companion notebook with computer-science applications.

## Download the books

- **Download page:** https://oussamasegh.github.io/numbers-structures-chance/
- **Direct links (latest build):** [Tome 0 PDF](https://github.com/OussamaSegh/numbers-structures-chance/releases/download/books/tome0-back-in-shape.pdf) ·
  [Tome 0 EPUB](https://github.com/OussamaSegh/numbers-structures-chance/releases/download/books/tome0-back-in-shape.epub) ·
  [Tome 1 PDF](https://github.com/OussamaSegh/numbers-structures-chance/releases/download/books/tome1-integers.pdf) ·
  [Tome 1 EPUB](https://github.com/OussamaSegh/numbers-structures-chance/releases/download/books/tome1-integers.epub)

Every push to `main` rebuilds all the books and republishes them, both on the download page and on the
[`books` release](https://github.com/OussamaSegh/numbers-structures-chance/releases/tag/books).

## The series

| Tome | Title | Theme | Status |
| --- | --- | --- | --- |
| 0 | Back in Shape | The MP toolkit, relearned through problems | Complete draft (8 chapters) |
| 1 | The Integers | Elementary and algebraic number theory | Chapters 1–11 drafted |
| 2 | Structures | Groups, rings, fields, Galois, representations | Planned |
| 3 | Chance | Probability, from counting to martingales | Planned |
| 4 | The Art of Calculation | Series, integrals, special functions, asymptotics | Planned |
| 5 | Where It All Meets | Analytic and probabilistic number theory | Planned |
| 6 | Spaces | Sets, topology, measure and integration | Planned |
| 7 | Analysis in Depth | Functional, harmonic and complex analysis | Planned |
| 8 | Shapes | Manifolds, algebraic topology, Lie groups | Planned |
| 9 | Structures II | Categories, commutative and homological algebra, representations | Planned |
| 10 | Chance II | Graduate probability: limit theorems, large deviations, concentration, ergodic theory | Planned |
| 11 | Random Motion | Brownian motion, stochastic calculus, random walks, random matrices | Planned |
| 12 | Arithmetic | Algebraic number theory, elliptic curves, modular forms | Planned |
| 13 | Primes in Depth | Analytic and additive number theory | Planned |
| 14 | Random Arithmetic | Probabilistic number theory and arithmetic statistics | Planned |
| 15 | The Research Workshop | Reading papers, experimenting, conjecturing, writing | Planned |

Tomes 0–5 are the foundations, 6–9 the graduate toolbox, and 10–15 the road to research in probability,
probabilistic number theory and algebra. The detailed plan of every tome lives in the series plan document.

## Layout

```
common/                 shared LaTeX preamble (PDF) and EPUB preamble
tome0-back-in-shape/    main.tex + chapters/*.tex (solutions at the end of each chapter)
tome1-integers/         same layout, one folder per tome
python/tomeN/           one Jupyter notebook per chapter
tools/                  EPUB conversion helpers (pandoc filter, CSS)
build.sh                builds dist/<tome>.pdf and dist/<tome>.epub
```

## Building

Requires `pdflatex` (TeX Live with `latex-extra` and `fonts-recommended`), `pandoc` 3 and Python 3.

```
./build.sh                       # every tome
./build.sh tome0-back-in-shape   # one tome
pip install -r requirements.txt  # for the notebooks
```

Every push builds the PDF and EPUB on GitHub Actions (the run's **books** artifact); pushes to `main` also publish them
to the download page and the `books` release. Figures are TikZ files in `<tome>/figures/`, converted to SVG for the EPUB.

## Writing conventions

- Exercises: `\begin{exercise}[$\star$]\label{ex:name} ... \end{exercise}`, graded $\star$ to $\star\star\star$.
- Solutions: `\begin{solution}{ex:name} ... \end{solution}` in the chapter's last section.
- Boxes: `reminder` (optional title), `beauty` (links to other tomes).
