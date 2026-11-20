# Series sequential review, Volume VNUM of 15 (Order and Chance)

Repo: https://github.com/OussamaSegh/Order-and-Chance. Main is at `c115ca60` (all 15 volumes as currently published). This is part VNUM of a sequential review of the whole series, one volume at a time, V1 to V15. You review Volume VNUM only: `VDIR/`.

Work on the single shared branch `cursor/series-sequential-review` (create it from main `c115ca60` if it does not exist; otherwise check it out and continue on it). Write only under `docs/review/series-sequential-review/`. **Do not edit any book source.** This is a review, not a fix pass; fixes come later as small PRs once the author approves. Keep the one draft PR for this branch (open it if it does not exist, title "Series sequential review (V1–V15)"); do not merge; do not touch other branches or PRs.

Read first: `AGENTS.md`, `docs/WRITING-STYLE.md`, `docs/agents/mathematician-writer.md`, `docs/SERIES-STRUCTURE.md`, the master plan in `docs/plan/`, and the files already in `docs/review/series-sequential-review/` (especially `CONCEPT-LEDGER.md`, written by the reviews of Volumes 1–(VNUM-1)).

## What to check, reading the volume in book order (main.tex order), every chapter, section, exercise, hint, solution, figure and caption, the preface, appendices, blurb and kdp.md
1. **Nothing used before it is introduced.** Every definition, notation, theorem, lemma, technique and fact used in Volume VNUM must be either introduced earlier in Volume VNUM, or introduced in an earlier volume (check against CONCEPT-LEDGER.md and verify the cited label really exists and says what is claimed), or explicitly flagged in the text as quoted without proof from outside the series. Flag: forward uses inside the volume, uses of things never introduced anywhere earlier, citations to wrong volume/chapter/label, notation that conflicts with earlier volumes, exercises or solutions needing tools the reader does not yet have.
2. **Writing style respected** per `docs/WRITING-STYLE.md` and the mathematician-writer brief: voice, plain step-by-step English, no padding or AI-sounding phrasing, no notebook/companion-file mentions (AGENTS.md policy), consistent terminology. Quote the offending sentence and say which rule it breaks. Report systematic patterns once with a list of locations rather than hundreds of rows.
3. **Mathematical correctness**: statements true, proofs complete with no gaps or circularity, hypotheses stated, numbers right (recompute with scripts, kept separate from the proofs). Cross-check against reliable sources online when uncertain, and cite them.
4. **Cross-references and promises**: forward pointers to later volumes that are false (check the later volume actually does it), stale "as we saw in Volume k" references, broken \ref/\cite, preface claims the volume does not deliver.
5. **Figures and captions**: correct, matching their caption and the text. Do not judge or change typography.
6. **Exercises**: solvable with the material so far, stars honest, solutions correct.

## Output (commit and push as you go, at least after each chapter)
- `docs/review/series-sequential-review/volumeVNUM.md`: a score /10 with one paragraph of justification; counts by severity (critical = false statement or broken proof; major = genuine gap, use-before-introduction of something substantive, wrong citation of a needed result; minor = local slip, style, small clarity issue); then one row per issue: ID `VVNUM-NNN`, file:line and label, category (prerequisite / style / math / reference / figure / exercise), severity, evidence (quote), suggested fix. Then a "Verified correct" summary per chapter and a "Not checked" list.
- **Append** to `docs/review/series-sequential-review/CONCEPT-LEDGER.md` a section "Volume VNUM" listing every concept, notation and named result Volume VNUM introduces, with its label and file, so later reviews can check prerequisites. Keep it complete but terse (one line each). Also list notation clashes with earlier entries.
- Update `docs/review/series-sequential-review/README.md` with a one-line status per volume (score, counts).

Never fabricate a check: if you did not verify something, put it under "Not checked". Do not stop early: read the whole volume. Do not end your run until every chapter is reviewed, the ledger section is appended, and everything is pushed.

## Final message
Score, severity counts, the 10 most important issues (one line each), the number of prerequisite (use-before-introduction) issues, the branch head SHA and the PR URL.
