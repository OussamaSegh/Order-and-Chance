# Tome C4, Information, Codes and Secrets: handoff (paused 2026-10-26)

Paused at the user's request (all computing-track threads paused).

Plan (12 chapters, promises table, conventions): https://claude.ai/artifact/Ez2z1vnNAfWswgD92i9WPG

## Status per chapter

| Ch | File | State |
|----|------|-------|
| 1 Measuring information | chapters/ch01-entropy.tex | Done: text, figures, notebook python/tomeC4/ch01-entropy.ipynb, all formats clean |
| 2 Compression | chapters/ch02-compression.tex | Done: text, figures, notebook, all formats clean |
| 3 Noisy channels | chapters/ch03-channels.tex | Done: text, figure, notebook (numbers diffed), all formats clean |
| 4 Kolmogorov complexity | chapters/ch04-kolmogorov.tex, figures/ch04-landscape.tex | Drafted and fact-checked; builds cleanly in all four formats. NOT yet in main.tex (its \input line is commented out). To do: notebook ch04-kolmogorov (compression proxies, pi bits, 57 letters of the Berry phrase, runs, sorting bound, p_k <= A k (log k)^2 ratios), then uncomment the \input line |
| 5–12 | — | Not started; see the plan |

Front matter, preface, blurb.tex, kdp.md and the E8 cover motif (tools/cover_motifs.py, e8_roots) are done.

## Chapter numbers other tomes cite (keep them)

- Ch 5 linear codes (MacWilliams, Hadamard/Reed–Muller, extended Hamming, generator/parity-check): cited by Tome S1 Ch 9, Tome P1 Ch 1, Tome C1 Ch 10–11.
- Ch 6 algebraic codes.
- Ch 8 secrecy and pseudorandomness: PRFs (GGM, HILL quoted), privacy amplification, average-case hardness; cited by Tome C3 Ch 9, 11, 12 and C1 Ch 3.
- Ch 9 public keys (RSA, ECC): cited by Tome C2 Ch 10.
- Ch 10 lattices / LWE: cited by the Tome 9 notebook.
- Ch 12 Shor: cited by Tome C2 Ch 10.
- Ch 1 owns KL divergence, Pinsker (Thm 1.8) and Fano (Thm 1.9); Tome C5 may cite them.

Cross-tome references are plain numbers ("Tome C3, Theorem 7.23"), never \ref.

## Tooling

Scripts in the project files under math-book/computing-scripts/: mknb_c4chNN.py (notebook generators, refs resolved from main.aux by companion-scripts/nbref.py), c4check.sh (build all formats, report errors/overfull/shrinks), c4push.sh (pull --rebase, README row, push to main).
