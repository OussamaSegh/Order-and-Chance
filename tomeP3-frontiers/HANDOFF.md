# Problem Book P3 "Frontiers": handoff (paused 2026-10-26)

Paused at the user's request (only the Tome 11-15 threads keep working).

- Plan: https://claude.ai/artifact/UvbVTWYTe6fQHLyiCcNRMo (14 chapters, 22 problems each, Ch14 = 16 Journeys).
- Series plan: https://claude.ai/artifact/WW5b9cRQvQXnp6teDxibAU
- Format: same as P1/P2 (statements never name the tool; solutions with \idea, \writeup, \tools, \leads; map table; sources;
  >= 2 figures; one notebook per chapter in python/tomeP3 that recomputes every number). No Fable review: self-check only.

## Done
- Front matter: main.tex, preface, blurb.tex, cover motif (CUE eigenvalues vs zeta zeros) in tools/cover_motifs.py.
- Chapter 1 "Sums of Random Pieces" (Tome 10 ch2-4, 6): 22 problems, 3 figures, notebook ch01-pieces.ipynb (0 errors),
  pointer check clean. Builds (./build.sh tomeP3-frontiers).

## In progress
- Chapter 2 "Rare Events and Concentration" (Tome 10 ch7-8): chapters/ch02-rare.tex is a FIRST DRAFT, all 22 problems,
  hints, solutions, map and sources written. It is NOT yet \input in main.tex. Before including it:
  1. Clean up rough passages: pb:discrepancy (a) strictness remark and (b) the HH^T line; pb:blowup (c) (state
     d(A,B) <= ceil(sqrt(2ns)) cleanly); pb:lundberg (c) ("for u large enough that..." sentence);
     pb:markovld (e) ("p/something" sentence).
  2. Write figs_p3c02.py: figures ch02-rem (REM free energy, n=12,16,20 vs f(beta)) and ch02-markovrate
     (sticky-chain rate functions, p=0.5, 0.1, 0.02), both already referenced in the tex.
  3. Write mknb_p3c02.py -> python/tomeP3/ch02-rare.ipynb recomputing every number in the chapter.
     Values already checked by scratch scripts (problem-scripts/checks_p3c02a.py, checks_p3c02b.py in the project files).
  4. Add \input{chapters/ch02-rare}, build, run ptrcheck.py, check overfull/undefined, README "2 of 14".

## Not started
- Chapters 3-9 and 11 can be written now.
- Chapter 10 waits on Tome 11 ch6-9; Chapter 12 on Tome 13 ch8-13; Chapters 13-14 on Tome 14 (and Tome 11 ch10-12, Tome 13 ch14).
- Avoid in Ch4: Erdős-Kac sharp forms (now in Tome 14 ch3).
- At the end: kdp.md, final self-checks, clean build, publish, email the user the links.
