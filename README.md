# Numbers, Structures and Chance

A series of books of beautiful mathematics, written for pleasure by a former MPSI/MP\* student coming back
to mathematics, with Claude. Every chapter has graded exercises with complete solutions and a Python
companion notebook with computer-science applications.

| Tome | Title | Theme | Status |
| --- | --- | --- | --- |
| 0 | Back in Shape | The MP toolkit, relearned through problems | Complete draft (8 chapters) |
| 1 | The Integers | Elementary and algebraic number theory | Chapter 1 drafted |
| 2 | Structures | Groups, rings, fields, Galois, representations | Planned |
| 3 | Chance | Probability, from counting to martingales | Planned |
| 4 | The Art of Calculation | Series, integrals, special functions, asymptotics | Planned |
| 5 | Where It All Meets | Analytic and probabilistic number theory | Planned |

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

Every push builds the PDF and EPUB on GitHub Actions; download them from the run's **books** artifact.

## Writing conventions

- Exercises: `\begin{exercise}[$\star$]\label{ex:name} ... \end{exercise}`, graded $\star$ to $\star\star\star$.
- Solutions: `\begin{solution}{ex:name} ... \end{solution}` in the chapter's last section.
- Boxes: `reminder` (optional title), `beauty` (links to other tomes).
