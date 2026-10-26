# Problem Book II: Machinery, handoff (paused 2026-10-26)

Paused at the user's request (only the Tome 11 to 15 threads keep working). Resume from here.

- Plan (chapter headlines for all 14 chapters, section "P2"): https://claude.ai/artifact/UVGXXYeZ1nXLUUkzxtF7LC
- Scope: Tomes 6 to 9, 14 chapters, about 300 problems (Chapters 1 to 13 have 22 problems, Chapter 13 has 20, Chapter 14 has 16 Journeys). Write Chapters 1 to 9 first, then 10 to 14 (Tome 9 material).
- Format: the same as Problem Book I (sourced story, epigraph, think box; statements never name the tool; hints before solutions; solutions with \idea, \writeup, \tools, \leads; map table and sources; at least 2 figures; companion notebook in python/tomeP2 with Part A checking every number and Part B a lab).
- Cover motif: Hilbert curve (tools/cover_motifs.py, hilbert_curve).
- Figure and notebook generator scripts live outside the repo, in the project files folder math-book/problem-scripts (figs_p2cNN.py, mknb_p2cNN.py).

## Status per chapter

| Chapter | Title | State |
|---|---|---|
| 1 | Almost Every Number | done, in the book, notebook python/tomeP2/ch01 |
| 2 | Hilbert Spaces at Work | done, in the book, notebook python/tomeP2/ch02-hilbert.ipynb |
| 3 | Operators and Spectra | text complete in drafts/ch03-operators.tex (not yet in main.tex) |
| 4 to 14 | see the plan | not started |

## Chapter 3, what is left

The draft has the story, 22 problems in five sections, all hints, all solutions, the map table and the sources. Every number in it was checked numerically in scratch scripts. Still to do:

1. Figures: figures/ch03-szego.tex (sorted eigenvalues of T_400(f), f = 1 + cos 2πθ + ½ cos 6πθ, against the increasing rearrangement of f), figures/ch03-weyl.tex (N_D, N_N, Weyl term and two-term curves for the rectangle 1 × √2), figures/ch03-slepian.tex (eigenvalues of the sinc kernel for c = 20 and 40). Keep under 3000 TikZ dots per figure.
2. Notebook python/tomeP2/ch03-operators.ipynb. Use exact sympy for the Redheffer eigenvalue-1 multiplicity (numpy is unreliable there because of Jordan blocks).
3. Move the draft to chapters/ch03-operators.tex, add \input{chapters/ch03-operators} after ch02 in main.tex, build, check 0 "??", overfull boxes and duplicate labels; set the README line to "3 of 14".
4. Re-read the solutions of §3 to §5 once more before merging; they were written last.

## Numbers other books cite

None. No other book cites Problem Book II yet.
