# Tome C5 handoff (paused 2026-10-26)

Work was paused at the user's request. This note says where the tome stands so that a later thread can resume.

- Plan (12 chapters, cites, promises, production rules): https://claude.ai/artifact/6PLh3w9Fqg9BodeG5Acvzj
- Notebook and figure generators: project folder `math-book/learning-scripts/`
  (`figs_c5ch0N.py figures/`, `mknb_c5ch0N.py out.ipynb main.aux`, helper `nbref.py`,
  label numbers of cited tomes in `labels-cited-tomes.txt`).

## Status per chapter

| Ch | Title | Status |
|---|---|---|
| 1 | Computing with Matrices | Done: text, 2 figures, notebook (7 s), builds clean in all formats |
| 2 | Krylov Spaces and Random Sketches | Done: text, 3 figures, notebook (10 s), numbers checked, builds clean |
| 3 | Convexity and Duality | Draft text in `chapters/ch03-convexity.tex`, NOT yet in `main.tex`. Missing: figures `ch03-fermat`, `ch03-conjugate`, `ch03-waterfilling`; notebook; number check; overfull check |
| 4–12 | see plan | Not started |

Front matter, preface, blurb.tex, kdp.md and the cover motif (`gd_nesterov` in tools/cover_motifs.py) are done.

## Chapter 3 draft: what to do on resume

1. Figures: Fermat point of towns (0,0), (4,0), (1,3) with Fasbender's equilateral triangle; conjugate of x^4/4 - x with the tangent line of slope 1; water-filling bars for alpha = (0.5,1.6,0.9,2.5,0.3,1.2,3.0,0.8), P = 5.
2. Numbers the text states, to recompute in the notebook: x* ≈ (1.302, 1.047), f(x*) ≈ 6.541, centroid 6.611, triangle angles 71.6/45/63.4; water level w = 10.3/6 ≈ 1.717 (already corrected in the text); Jaynes' die theta ≈ 0.371 and p ≈ 0.054, 0.079, 0.114, 0.165, 0.240, 0.347; finger game value -1/12.
3. Add `\input{chapters/ch03-convexity}` to main.tex, build a4/phone/kindle/print, fix overfull boxes over 10 pt.
4. Sources cite Kuhn 1974 ("Steiner's" problem revisited) and Mordukhovich–Nam 2019; venue details of the latter to double-check.

## Labels other tomes may cite

None yet: no other tome cites C5 by number. Promises C5 keeps: S1 Ch6 numerical SVD and S1 Ch4 Householder (Ch 1, Thm 1.13 qrstable and Sec. svdcompute), S1 Ch12 CG optimal polynomial (Ch 2, Thm 2.5 cgconv), C1 Ch9 Shi–Malik (Ch 2, Thm 2.8 ncut); still to keep: C2 Ch7 Karmarkar/interior points (Ch 6), C2 Ch12 multiplicative weights as online learning (Ch 7), Jerrum–Sinclair conductance and Jerrum colourings (Ch 10).

No review has been done (writer self-check only).
