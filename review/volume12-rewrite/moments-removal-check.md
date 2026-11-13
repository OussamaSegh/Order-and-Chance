# Written check before removing `volume12-random-motion/chapters/moments.tex`

`moments.tex` ("Zeta and Random Matrices") was not input by `volume12-random-motion/main.tex`, so it never printed.
Volume 15 prints the same text as `volume15-order-and-chance/chapters/moments-zeta.tex`, input by `ch09-gue.tex`.

Statement by statement (labels are identical in both files):

| Item | In Volume 15 `moments-zeta.tex` |
| --- | --- |
| Epigraph, history (Montgomery, Dyson, Odlyzko, Keating–Snaith) | yes, same text |
| "The evidence" section, unfolding, figure `moments:fig:spacings` | yes (figure `moments-ch05-spacings` exists in Volume 15's figures) |
| `moments:prop:surmise` (Wigner surmises for 2×2 matrices) | yes |
| `moments:lem:zetaapprox`, `moments:lem:dirmeanvalue`, `moments:thm:meansquare` | yes |
| `moments:rem:keatingsnaith` | yes |
| "Why it is hard", "Reading a paper", "Open doors" | yes |
| Exercises `moments:ex:poissonsp` … `moments:ex:unfold`, hints, solutions, sources | yes |

`diff` of the two files shows only differences of cross-reference wording, all of which concern Volume 15's own rewrite:
the Volume 12 copy cites "Volume 6, Theorem 6.9" for the zero count (twice) and "Volume 8, Theorem 10.4" for Plancherel where the Volume 15 copy says
"Volume 6, the zero-counting formula" and "Volume 8". These precise numbers are recorded in `docs/handoffs/volume12-rewrite.md` for the Volume 15 rewrite to check
against the printed order of Volumes 6 and 8 at that time.

Nothing unique is lost. The figure `volume12-random-motion/figures/moments-ch05-spacings.tex` was used only by `moments.tex` and is removed with it;
`moments-ch05-semicircle.tex` stays (Chapter 9 uses it).
