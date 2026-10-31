# Volume 1 voice rewrite

This file is the live execution tracker for the Volume 1 rewrite. The book is `volume1-first-principles`. One chapter, or the named pair, is one pull request, written in the shared voice.

Cold-start snapshot: 2026-10-31. Steps 0 through 13 are DONE on main. Preface #71 is squash-merged at `4b67ea9` (`4b67ea9e80115c9dfaeb4cf5e30b74258bef3dd6`). The opener-page swap #72 is squash-merged at `7fae5a8` (`7fae5a8c6724c29dca4132fa7284525a3334f6dd`). Global consistency #69 is squash-merged at `fbeecfd` (`fbeecfd611b68271476ee5a37e94e6362c91ae85`). The final PDF review is #73 (Grok), squash-merged at `4aa4e3f` (`4aa4e3f3d42334f1c165e622ca8a67f6b39a5cf1`). The review file on main is `docs/reviews/volume1-final-grok-review.md`, of the reading PDF at `7fae5a8`. Verdict: publish after fixes. Step 14 applied those fixes and was squash-merged as #74 at `3f264ba` (`3f264bab27ae57146e73e635c86685526eff1e48`) on 2026-10-30, before the independent re-review this file asked for. That re-review is `docs/reviews/volume1-step14-rereview.md`, pull request https://github.com/OussamaSegh/Order-and-Chance/pull/79. The same pull request caps interword shrink so the PDF text layer keeps word spaces, and it replaces the CC BY-NC launch photograph. This file does not mark Volume 1 first-edition ready. Do not start Volume 2.

Standing series goal. When Volume 1 is done, the series continues with Volumes 2 through 15 in order, one volume after another, under the same house voice and the same bar: one chapter per pull request, and an independent review before every merge. That handoff is for another bot. Nori owns Volume 1 only. Volume 2 waits until Volume 1 is marked first-edition ready. This file does not set that mark. Step 14 has merged. The independent re-review was not done before that merge; it is recorded in `docs/reviews/volume1-step14-rereview.md`. The PDF text-layer spacing and the launch-photograph licence are in that same pull request. The nice-to-have voice notes from review #73 are still notes, not a rewrite.

Nori owns the Volume 1 end-state: free to launch, review, and merge Volume 1. One chapter is one pull request. An independent review comes before every merge. Oussama asked Nori to finish Volume 1 quickly with many agents. Steps 0 through 13 are DONE on main. Steps 7 through 12 are the reviewed chapters from #58, #59, #64, #62, #60, and #61, squash-merged together as #67 at `78f27d33c7e605282d8ca1673f73e19f57206adf`. Independent review of each of those six returned MERGE before the stack. The stack did not rewrite chapter prose. The only chapter-file edit in the stack was in probability: the figure label `fig:signs` is `fig:pairsigns`, because polynomials already uses `fig:signs`. The layout check rejects a multiply-defined label. Step 13, the global consistency review, is DONE on main at `fbeecfd611b68271476ee5a37e94e6362c91ae85` (#69). Preface #71 is DONE at `4b67ea9`. The opener swap #72 is DONE at `7fae5a8`. Final review #73 is squash-merged at `4aa4e3f`. Do not merge #58, #59, #64, #62, #60, or #61 as a second copy. Step 14 is merged at `3f264ba`. The re-review was not done before that merge. Do not start Volume 2. Do not mark Volume 1 first-edition ready from this file.

The remake runs from the start, in this order: cover, preface and language, sums, counting, sequences, orders, complex numbers, polynomials, linear algebra, calculus, inequalities, probability, field guide.

Each rewrite step is a profound pass, with liberty to reorder for clarity and to add figures, photos, history points, and math jokes that teach, not a thin copyedit. The mathematics stays correct.

The voice is [docs/WRITING-STYLE.md](../WRITING-STYLE.md), including the [Sound human](../WRITING-STYLE.md#sound-human) pass: a friend who loves mathematics, never AI-sounding. Run that pass before each chapter pull request, and again on each independent review. The house-voice rule merged in [#52](https://github.com/OussamaSegh/Order-and-Chance/pull/52) at `bc67b65fad39f1ecdfbe0228f7362070bb75211c` on 2026-10-30. The role is [docs/agents/mathematician-writer.md](../agents/mathematician-writer.md). The editor (Nori) reviews each Volume 1 pull request independently. Later chapters may be drafted in parallel. Steps 7 through 12 landed together in #67. Do not merge their source pull requests one by one.

Edition 1 catalog and content moves, old steps 0–21, are finished. They are kept in [Archive: Edition 1 plan (complete)](#archive-edition-1-plan-complete) at the bottom of this file. That archive is not the resume target.

Chapter order follows the `\input` order in `volume1-first-principles/main.tex`. Image credits are not a rewrite step. The cover note is step 0.

## Open pull requests

#65 and #63 are squash-merged and gone from the manuscript queue. Orders (step 5) is DONE at `f4577dac0251078aa500c001114aa27cb8a2a782` on 2026-10-30 Europe/Paris. Independent review of #65 returned MERGE, and its CI was green. Complex numbers (step 6) is DONE at `1d307a186bad0f9d5d077e8d3a326bbb4ba99032` on 2026-10-30 Europe/Paris.

#67 squash-merged the six remaining chapter rewrites onto main at `78f27d33c7e605282d8ca1673f73e19f57206adf`. Each source pull request had already returned MERGE from independent review. The chapter files and their new figures on main are those reviewed tips, except probability's figure label `fig:signs`, renamed `fig:pairsigns` so it does not collide with polynomials. Do not merge #58, #59, #64, #62, #60, or #61 as a second copy.

- **#58, polynomials, step 7.** https://github.com/OussamaSegh/Order-and-Chance/pull/58. Branch `cursor/polynomials-profound-d617`. Reviewed tip `16f05d21dd03a2ebe6dd3d98074153b23b48a04c`. Author agent `bc-c52d7dd1`. Independent review: MERGE. Landed in #67.
- **#59, linear algebra, step 8.** https://github.com/OussamaSegh/Order-and-Chance/pull/59. Branch `cursor/linear-algebra-chapter-9af6`. Reviewed tip `3b128dd2d127e3a30879f0526b2ce47172e097e8`. Author agent `bc-c15e0fbb`. Independent review: MERGE. Landed in #67.
- **#64, integrals and Taylor, step 9.** https://github.com/OussamaSegh/Order-and-Chance/pull/64. Branch `cursor/integrals-taylor-profound-2e8a`. Reviewed tip `3842c235e41e27ab5495635870ef436e04771680`. Author agent `bc-82f7cfae`. Independent review: MERGE. Landed in #67.
- **#62, inequalities, step 10.** https://github.com/OussamaSegh/Order-and-Chance/pull/62. Branch `cursor/inequalities-profound-756b`. Reviewed tip `997c747e6bd4d30ab6ecb1aa9e6de03847a52f7a`. Author agent `bc-12cf9ce1`. Independent review: MERGE. Landed in #67.
- **#60, probability, step 11.** https://github.com/OussamaSegh/Order-and-Chance/pull/60. Branch `cursor/probability-chapter-ac3e`. Reviewed tip `9b46858a5da87e69f6963182593633737ee3633c`. Author agent `bc-1faa35de`. Independent review: MERGE. Landed in #67, with the figure label `fig:pairsigns`.
- **#61, field guide, step 12.** https://github.com/OussamaSegh/Order-and-Chance/pull/61. Branch `cursor/volume1-field-guide-4cf2`. Reviewed tip `b55dfd64f5e96943e8a89eed484d3bfe9f053265`. Author agent `bc-31e0beff`. Independent review: MERGE. Landed in #67.

Step 13 is DONE. #69 squash-merged the global consistency review at `fbeecfd611b68271476ee5a37e94e6362c91ae85`.

Preface #71 is squash-merged at `4b67ea9e80115c9dfaeb4cf5e30b74258bef3dd6`. The opener-page swap #72 is squash-merged at `7fae5a8c6724c29dca4132fa7284525a3334f6dd`. Do not open a second preface pull request.

The final PDF review #73 is squash-merged at `4aa4e3f3d42334f1c165e622ca8a67f6b39a5cf1`. The file is `docs/reviews/volume1-final-grok-review.md`. https://github.com/OussamaSegh/Order-and-Chance/pull/73. Verdict: publish after fixes. That review does not apply the fixes. Step 14 applied them and is squash-merged as #74 at `3f264ba`: https://github.com/OussamaSegh/Order-and-Chance/pull/74. The independent re-review is `docs/reviews/volume1-step14-rereview.md`.

## Resume protocol

1. Read this file, including the open-pull-request list. Steps 0 through 14 are on main. Preface #71 is squash-merged at `4b67ea9`. Opener swap #72 is squash-merged at `7fae5a8`. Global consistency #69 is squash-merged at `fbeecfd`. Step 14 is squash-merged at `3f264ba`. The re-review of that merge is `docs/reviews/volume1-step14-rereview.md`. Do not open another preface pull request. Do not start Volume 2. Do not mark Volume 1 first-edition ready from this file.
2. Do not open a second pull request for any Volume 1 chapter. Do not merge #58, #59, #64, #62, #60, or #61 separately. Their texts landed in #67.
3. If a later step is TODO, search the open pull requests for that chapter before creating a branch. If a branch or pull request already exists, use it. No Volume 1 chapter step is TODO. Step 13 is DONE. Step 14 is merged at `3f264ba`. Review #73 is squash-merged at `4aa4e3f`; do not treat it as the fix. The re-review of the fix is `docs/reviews/volume1-step14-rereview.md`.
4. One step is one pull request and one chapter file. Step 0 is the jacket: `blurb.tex`, `about-the-cover.tex`, `kdp.md`, and the Volume 1 entry in `common/cover-notes.json`. Step 1 is the preface and the language chapter together. Step 13 may touch several chapter files, but only where a cross-reference, handoff, label, or voice bug breaks the book as one volume.
5. In the same pull request, set the row to IN REVIEW and fill the PR link. Leave the merge sha and the date blank until merge. Steps 7 through 12 are DONE. Do not set them back to IN REVIEW.
6. Steps 7 through 12 record the squash sha of #67. A blank merge sha on those rows is not a reason to redraft the chapter.
7. Step 13 is DONE at `fbeecfd611b68271476ee5a37e94e6362c91ae85`. Preface #71 and opener swap #72 are on main. Step 14 is merged at `3f264ba`. Volume 2 waits until Volume 1 is marked first-edition ready. This file does not set that mark. Step 0 is DONE. The PDF text-layer spacing and the launch-photograph licence are handled with the re-review, not left as a silent pass. The nice-to-have voice notes from review #73 are still notes.
8. Acceptance always includes a match to `docs/WRITING-STYLE.md`, including the Sound human pass, fact-check notes in the pull request, and `git diff --check`. A chapter step also needs a Volume 1 typeset and layout check. Run `./build.sh volume1-first-principles`, or the equivalent XeLaTeX pass plus `tools/check_book_layout.py`, as the earlier chapter pull requests did. Step 0 checks the cover note (80 to 150 words), `python3 tools/series_cover.py --check`, and the back-cover measure.
9. Scope is the assigned file or files under `volume1-first-principles/`, plus the cover-note source when the step is the jacket, plus figures that a chapter needs. Do not edit other volumes in that pull request.

## Steps

### 0. Cover copy

- **Status:** DONE
- **Depends on:** none
- **Books and files:** `volume1-first-principles/blurb.tex`, `volume1-first-principles/about-the-cover.tex`, `volume1-first-principles/kdp.md`, and the Volume 1 text in `common/cover-notes.json`. The TeX colophon is generated from that JSON. `docs/COVER-NOTES.md` and `tools/assets/series/manifest.json` follow the cover check. Jacket copy only. No chapter rewrite.
- **Acceptance:** The jacket texts match `docs/WRITING-STYLE.md`. Fact-check notes are in the pull request. `git diff --check`. The cover note is 80 to 150 words. `python3 tools/series_cover.py --check` passes. The back-cover blurb fits the shared measure.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/54
- **Merge sha:** 0bbf558903e96149998a0d71c2e49b1a82a66544
- **Date:** 2026-10-30
- **Notes:** Squash-merged. Back cover and About the Cover. Agent `bc-74380fd7`. Do not open another jacket pull request.

### 1. Preface and language

- **Status:** DONE
- **Depends on:** 0
- **Books and files:** `volume1-first-principles/chapters/preface.tex` and `volume1-first-principles/chapters/ch00-language.tex`. Both files in one pull request.
- **Acceptance:** Both files match `docs/WRITING-STYLE.md`. Fact-check notes are in the pull request. `git diff --check`. Volume 1 typesets and the layout check passes.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/51
- **Merge sha:** 1d97799a0e12a6b91f562dc7e88ad0ec4c788a3a
- **Date:** 2026-10-30
- **Notes:** Deepen pass, squash-merged. The first pass merged in https://github.com/OussamaSegh/Order-and-Chance/pull/43 at `0212bbee89ccb4e7fb291a2c20b18be724eb3949` on 2026-10-30. The approved preface body is #71, squash-merged at `4b67ea9e80115c9dfaeb4cf5e30b74258bef3dd6`. Step 1 stays DONE. Do not open a second preface pull request.

### 2. Sums, binomials, induction

- **Status:** DONE
- **Depends on:** 1
- **Books and files:** `volume1-first-principles/chapters/ch01-sums.tex`. Sums, binomials, induction.
- **Acceptance:** The chapter matches `docs/WRITING-STYLE.md`. Fact-check notes are in the pull request. `git diff --check`. Volume 1 typesets and the layout check passes.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/50
- **Merge sha:** 586f056b3fd86af06e8839c137c34d52f78d821e
- **Date:** 2026-10-30
- **Notes:** Deepen pass, squash-merged. The first pass merged in https://github.com/OussamaSegh/Order-and-Chance/pull/46 at `69d90ccedce7f02ac26b8737fd09a88bc8459215` on 2026-10-30. Do not open another sums pull request.

### 3. Counting and discrete reasoning

- **Status:** DONE
- **Depends on:** 2
- **Books and files:** `volume1-first-principles/chapters/ch02-counting.tex`. Counting and discrete reasoning.
- **Acceptance:** The chapter matches `docs/WRITING-STYLE.md`. Fact-check notes are in the pull request. `git diff --check`. Volume 1 typesets and the layout check passes.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/53
- **Merge sha:** fe390f2a814e84bac91a7bc3d3c1ee2495115e96
- **Date:** 2026-10-30
- **Notes:** Human-voice pass, squash-merged. The counting rewrite merged in https://github.com/OussamaSegh/Order-and-Chance/pull/47 at `83dff2be79404b68ee6c45d620ee574432302c4e` on 2026-10-30. Do not open another counting pull request.

### 4. Sequences, series, limits

- **Status:** DONE
- **Depends on:** 3
- **Books and files:** `volume1-first-principles/chapters/ch05-sequences-series.tex`. Sequences, series, limits. New figures: `figures/ch05-zeno.tex`, `figures/ch05-grandi.tex`, `figures/ch05-floor.tex`, `figures/ch05-integral.tex`, `figures/ch05-uniform.tex`.
- **Acceptance:** The chapter matches `docs/WRITING-STYLE.md`. Fact-check notes are in the pull request. `git diff --check`. Volume 1 typesets and the layout check passes.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/55
- **Merge sha:** 6b63e54ca0b9dd0722b71bef1171af60670bf8e3
- **Date:** 2026-10-30
- **Notes:** Squash-merged. Sequences, series, and limits. Author agent `bc-3a95942d`. Fix agent `bc-5e590679`. Profound pass: concrete partial sums first, the floor and the positive square root of 2 from completeness, new figures for Zeno, Grandi, the floor, the integral test, and uniform continuity. Do not open another sequences pull request.

### 5. Orders

- **Status:** DONE
- **Depends on:** 4
- **Books and files:** `volume1-first-principles/chapters/orders.tex`. Orders.
- **Acceptance:** The chapter matches `docs/WRITING-STYLE.md`. Fact-check notes are in the pull request. `git diff --check`. Volume 1 typesets and the layout check passes.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/65
- **Merge sha:** f4577dac0251078aa500c001114aa27cb8a2a782
- **Date:** 2026-10-30
- **Notes:** Squash-merged on 2026-10-30 Europe/Paris. Independent review returned MERGE. CI green. Orders. Author agent `bc-4b2e8304-6f89-5e0e-ada6-f6141c8d6e98`. Do not open another orders pull request.

### 6. Complex numbers and roots

- **Status:** DONE
- **Depends on:** 5
- **Books and files:** `volume1-first-principles/chapters/ch02-complex-roots.tex`. Complex numbers and roots.
- **Acceptance:** The chapter matches `docs/WRITING-STYLE.md`. Fact-check notes are in the pull request. `git diff --check`. Volume 1 typesets and the layout check passes.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/63
- **Merge sha:** 1d307a186bad0f9d5d077e8d3a326bbb4ba99032
- **Date:** 2026-10-30
- **Notes:** Squash-merged on 2026-10-30 Europe/Paris. Complex numbers and roots. Author agent `bc-f3b455e9-b90e-5689-bbac-a6a41db1c8c2`. Do not open another complex-numbers pull request.

### 7. Polynomials

- **Status:** DONE
- **Depends on:** 6
- **Books and files:** `volume1-first-principles/chapters/ch03-polynomials.tex`. Polynomials. New figures: `figures/ch03-horner.tex`, `figures/ch03-values.tex`, `figures/ch03-signs.tex`, `figures/ch03-cotsqueeze.tex`.
- **Acceptance:** The chapter matches `docs/WRITING-STYLE.md`. Fact-check notes are in the pull request. `git diff --check`. Volume 1 typesets and the layout check passes.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/58
- **Merge sha:** 78f27d33c7e605282d8ca1673f73e19f57206adf
- **Date:** 2026-10-30
- **Notes:** Squash-merged in #67, not redrafted. Source pull request #58, branch `cursor/polynomials-profound-d617`, reviewed tip `16f05d21dd03a2ebe6dd3d98074153b23b48a04c`. Independent review returned MERGE. Author agent `bc-c52d7dd1-180f-5218-a11a-bfbbebc4d617`. The chapter file and its four new figures on main match that tip byte for byte. Do not open another polynomials pull request. Do not merge #58 separately.

### 8. Linear algebra

- **Status:** DONE
- **Depends on:** 7
- **Books and files:** `volume1-first-principles/chapters/ch07-linear-algebra.tex`. Linear algebra. New figures: `figures/ch07-bases.tex`, `figures/ch07-orientation.tex`.
- **Acceptance:** The chapter matches `docs/WRITING-STYLE.md`. Fact-check notes are in the pull request. `git diff --check`. Volume 1 typesets and the layout check passes.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/59
- **Merge sha:** 78f27d33c7e605282d8ca1673f73e19f57206adf
- **Date:** 2026-10-30
- **Notes:** Squash-merged in #67, not redrafted. Source pull request #59, branch `cursor/linear-algebra-chapter-9af6`, reviewed tip `3b128dd2d127e3a30879f0526b2ce47172e097e8`. Independent review returned MERGE. Author agent `bc-c15e0fbb-1991-5081-8f39-7fd016849af6`. The chapter file and its two new figures on main match that tip byte for byte. Do not open another linear-algebra pull request. Do not merge #59 separately.

### 9. Integrals and Taylor

- **Status:** DONE
- **Depends on:** 8
- **Books and files:** `volume1-first-principles/chapters/ch06-integrals-taylor.tex`. Integrals and Taylor. New figures: `figures/ch06-parts.tex`, `figures/ch06-quarter.tex`, `figures/ch06-zoom.tex`.
- **Acceptance:** The chapter matches `docs/WRITING-STYLE.md`. Fact-check notes are in the pull request. `git diff --check`. Volume 1 typesets and the layout check passes.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/64
- **Merge sha:** 78f27d33c7e605282d8ca1673f73e19f57206adf
- **Date:** 2026-10-30
- **Notes:** Squash-merged in #67, not redrafted. Source pull request #64, branch `cursor/integrals-taylor-profound-2e8a`, reviewed tip `3842c235e41e27ab5495635870ef436e04771680`. Independent review returned MERGE. Author agent `bc-82f7cfae-e852-5f08-b758-b9624f422e8a`. The chapter file and its three new figures on main match that tip byte for byte. Do not open another integrals pull request. Do not merge #64 separately. This is the calculus step.

### 10. Inequalities

- **Status:** DONE
- **Depends on:** 9
- **Books and files:** `volume1-first-principles/chapters/ch04-inequalities.tex`. Inequalities. New figures: `figures/ch04-align.tex`, `figures/ch04-frame.tex`, `figures/ch04-rearrange.tex`.
- **Acceptance:** The chapter matches `docs/WRITING-STYLE.md`. Fact-check notes are in the pull request. `git diff --check`. Volume 1 typesets and the layout check passes.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/62
- **Merge sha:** 78f27d33c7e605282d8ca1673f73e19f57206adf
- **Date:** 2026-10-30
- **Notes:** Squash-merged in #67, not redrafted. Source pull request #62, branch `cursor/inequalities-profound-756b`, reviewed tip `997c747e6bd4d30ab6ecb1aa9e6de03847a52f7a`. Independent review returned MERGE. Author agent `bc-12cf9ce1-c1d3-59a2-b6c7-538fcb05756b`. The chapter file and its three new figures on main match that tip byte for byte. Do not open another inequalities pull request. Do not merge #62 separately.

### 11. Probability

- **Status:** DONE
- **Depends on:** 10
- **Books and files:** `volume1-first-principles/chapters/ch09-probability.tex`. Probability. New figures: `figures/ch09-dice.tex`, `figures/ch09-even.tex`, `figures/ch09-geometric.tex`, `figures/ch09-signs.tex`.
- **Acceptance:** The chapter matches `docs/WRITING-STYLE.md`. Fact-check notes are in the pull request. `git diff --check`. Volume 1 typesets and the layout check passes.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/60
- **Merge sha:** 78f27d33c7e605282d8ca1673f73e19f57206adf
- **Date:** 2026-10-30
- **Notes:** Squash-merged in #67, not redrafted. Source pull request #60, branch `cursor/probability-chapter-ac3e`, reviewed tip `9b46858a5da87e69f6963182593633737ee3633c`. Independent review returned MERGE. Author agent `bc-1faa35de-1adb-5586-9407-5b3740c7ac3e`. The chapter file and its four new figures match that tip except one label: `fig:signs` is `fig:pairsigns`, because the polynomials chapter already uses `fig:signs`. Do not open another probability pull request. Do not merge #60 separately.

### 12. Field guide

- **Status:** DONE
- **Depends on:** 11
- **Books and files:** `volume1-first-principles/chapters/field-guide.tex`. Field guide, and the handoff to Volume 2. New figures: `figures/field-circle.tex`, `figures/field-euler.tex`.
- **Acceptance:** The chapter matches `docs/WRITING-STYLE.md`. Fact-check notes are in the pull request. `git diff --check`. Volume 1 typesets and the layout check passes.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/61
- **Merge sha:** 78f27d33c7e605282d8ca1673f73e19f57206adf
- **Date:** 2026-10-30
- **Notes:** Squash-merged in #67, not redrafted. Source pull request #61, branch `cursor/volume1-field-guide-4cf2`, reviewed tip `b55dfd64f5e96943e8a89eed484d3bfe9f053265`. Independent review returned MERGE. Author agent `bc-31e0beff-efcb-5e76-9580-a38f144d4cf2`. The chapter file and its two new figures on main match that tip byte for byte. Do not open another field-guide pull request. Do not merge #61 separately. Step 13 is DONE at `fbeecfd611b68271476ee5a37e94e6362c91ae85`. Preface #71 is on main at `4b67ea9`. Step 14 is merged at `3f264ba`.

### 13. Global consistency and transitions

- **Status:** DONE
- **Depends on:** 12
- **Books and files:** the reader-facing text of `volume1-first-principles` (preface, chapters, field guide) and this progress file. No new chapter. No other volume.
- **Acceptance:** Cross-references resolve, chapter closings hand to the next opening, the field guide names Volume 2 by its current title and subtitle, labels stay unique, and the prose that changed still matches `docs/WRITING-STYLE.md`. Fact-check notes are in the pull request. `git diff --check`. Volume 1 typesets and the layout check passes.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/69
- **Merge sha:** fbeecfd611b68271476ee5a37e94e6362c91ae85
- **Date:** 2026-10-30
- **Notes:** Squash-merged as #69 at `fbeecfd611b68271476ee5a37e94e6362c91ae85`. Handoffs, findable pointers, and the Volume 2 door. It does not redraft a chapter that already returned MERGE. The #69 preface closing is superseded by preface #71, squash-merged at `4b67ea9`. Do not start Volume 2. Step 14 is merged at `3f264ba`.

### 14. Final-review repairs

- **Status:** DONE
- **Depends on:** 13, and on preface #71 and opener swap #72, both on main
- **Books and files:** local repairs in Volume 1 only: `chapters/preface.tex`, `chapters/ch00-language.tex`, `chapters/ch01-sums.tex`, `chapters/ch07-linear-algebra.tex`, `chapters/field-guide.tex`, `chapters/ch09-probability.tex`, and the Volume 1 copyright credit in `common/cover-notes.json` (with the generated credit line and the manifest hash). No chapter rewrite. No other volume's prose.
- **Acceptance:** Review #73's must-fix and should-fix items are in the source. The new sentences match `docs/WRITING-STYLE.md`. Fact-check notes are in the pull request. `git diff --check`. The PDF text-layer spacing and the launch-photograph licence were outside this step. They are handled with the re-review, not by this merge.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/74
- **Merge sha:** 3f264bab27ae57146e73e635c86685526eff1e48
- **Date:** 2026-10-30
- **Notes:** Squash-merged as #74 at `3f264ba`. Review #73 (Grok) is squash-merged at `4aa4e3f3d42334f1c165e622ca8a67f6b39a5cf1`. It read the PDF at `7fae5a8`. Verdict there: publish after fixes. This step applied the must-fix and should-fix items. The independent re-review this file required was not done before the merge. That reading is `docs/reviews/volume1-step14-rereview.md`, pull request https://github.com/OussamaSegh/Order-and-Chance/pull/79. It found the repairs hold, corrected one loose sentence in the bilinear solution and one over-strong sentence in the field guide, capped interword shrink in `common/preamble.tex`, and replaced the CC BY-NC launch photograph with NASA image 6900556. This file does not mark Volume 1 first-edition ready. Do not start Volume 2.

## Archive: Edition 1 plan (complete)

Complete. Not the resume target. Edition 1 steps 0–21 below are finished. Their statuses are the historical record. Resume from the Volume 1 voice rewrite at the top of this file.

### Implementation tracker

This is the execution list for Edition 1. The reasoning lives in [SERIES-CONTENT-PLAN.md](SERIES-CONTENT-PLAN.md) and the chapter plans beside it. Titles and subtitles are frozen. Part names stay the catalog's, except the two renames in steps 5 and 8.

Paths below, and the paths in the other files under `docs/plan/`, are the directory names `volume1-first-principles` through `volume15-order-and-chance`. The retired names (`tome0-mathematical-maturity`, `tome9-higher-structures`, `tome14-order-and-chance`, and the other pre-renumbering stems) are gone. Step 2 does not revive them.

| Book | Directory |
| --- | --- |
| 1 First Principles | `volume1-first-principles` |
| 2 The Integers | `volume2-integers` |
| 3 Symmetry | `volume3-symmetry` |
| 4 Chance | `volume4-chance` |
| 5 Calculation | `volume5-calculation` |
| 6 Crossroads | `volume6-crossroads` |
| 7 Spaces | `volume7-spaces` |
| 8 Analysis | `volume8-analysis` |
| 9 Shapes | `volume9-shapes` |
| 10 Abstraction | `volume10-abstraction` |
| 11 Randomness | `volume11-randomness` |
| 12 Random Motion | `volume12-random-motion` |
| 13 Arithmetic | `volume13-arithmetic` |
| 14 The Primes | `volume14-primes` |
| 15 Order and Chance | `volume15-order-and-chance` |

### Retired resume protocol (Edition 1)

This protocol applied while Edition 1 was open. Do not resume from it.

1. Read this file. Find the first step whose status is not DONE.
2. If that step is IN REVIEW or IN PROGRESS, open its PR link. Continue that branch. Do not open a second PR for the same step.
3. If that step is TODO, search the open pulls for its id (for example `step 5`) before creating a branch. If a branch or PR already exists, use it.
4. Do the step. In the same PR, set this row to IN REVIEW, fill the PR link, and leave merge sha and date blank.
5. The editor marks the row DONE, with the merge sha and the date, after the PR merges. If the editor has not done that when the next step starts, the next step's PR marks the previous row DONE from the merge commit.
6. Do not start step \(n+1\) while step \(n\) is TODO, IN PROGRESS, or IN REVIEW.
7. Do not edit a book a later step has not reached, and do not reopen a move this file marks DONE.
8. Leave the repaired proofs alone. They are listed under "Already repaired" in the series plan. The exception is the second reading of three squares, which is part of step 5.

A step is one PR. A content step is one book, or one move between books. Step 2 is the rename: it touches every book and does not change the mathematics. Acceptance always includes `git diff --check` and `./build.sh` on every stem the step touches.

### Edition 1 steps

### 0. Merge PR #26 renumbering + final titles

- **Status:** DONE
- **Depends on:** none
- **Books and files:** the whole catalog. New stems `tome1-first-principles` through `tome15-order-and-chance`. `common/series-catalog.json`, `docs/SERIES-STRUCTURE.md`.
- **Acceptance:** Books 1–15 use the frozen titles. There is no P1 volume. Book 6 is Crossroads, *Arithmetic Meets Analysis*. The old problem book's problems are appended to Books 1–6.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/26
- **Merge sha:** 68aff65f87b4e37a5c0e45d4d866842897749c5c
- **Date:** 2026-10-29
- **Notes:** Squash-merged. Do not re-implement the renumbering.

### 1. Merge this plan

- **Status:** DONE
- **Depends on:** 0
- **Books and files:** `docs/plan/` only. No manuscript.
- **Acceptance:** `SERIES-CONTENT-PLAN.md`, `book-01.md` through `book-15.md`, and this file are on `main`. Part names in the plan are the catalog's. The two proposed renames are marked as proposals.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/27
- **Merge sha:** 2c5c7811f0d884dec5430b8facd7fc8a6e8b862c
- **Date:** 2026-10-29
- **Notes:** Squash-merged. Do not re-implement the plan files.

### 2. Harmonize Tome to Volume

- **Status:** DONE
- **Depends on:** 1
- **Books and files:** the whole repository. Names only. No mathematical text, no title, no subtitle, and no part name.
  - Reader-visible text, covers, and spines: Tome becomes Volume, and tome becomes volume. Do not redraw artwork, frames, or any lettering that does not spell that word.
  - LaTeX macros: `\seriestome` becomes `\seriesvolume`, `\TOMENUM` becomes `\VOLUMENUM`, and `\TOMETITLE` becomes `\VOLUMETITLE`, including `common/frontmatter.tex`, `common/series.tex`, and the lines `tools/series_metadata.py` writes.
  - Directories: `tome1-first-principles` becomes `volume1-first-principles`, and the same replacement through `tome15-order-and-chance`. `python/tome1` through `python/tome15` become `python/volume1` through `python/volume15`.
  - `build.sh`, `tools/build_plan.py`, `.github/workflows/build.yml`, `.github/workflows/notebooks.yml`, and the `stem` fields in `common/series-catalog.json`. Shell variables, the workflow matrix key, and the build-plan field that are still named tome change with them.
  - PDF, EPUB, and release asset names, and the reader routes under `read/`, wherever they still contain `tome`. Public basenames that already read `Volume N - …` (`tools/PUBLISHING.md`) stay in that form.
  - The site and the download page, including `tools/site.py` and the `.tome` card class in `tools/site-template.html`.
  - The README and the docs.
  - Old download and reader URLs that used a `tome` stem keep working. There is no redirect table today; add one where a published URL used the old stem.
- **Acceptance:** `git diff --check`. A search for `tome` or `Tome` is empty except where the old spelling has to remain: step 0's record of the names PR #26 created, the retired-name list at the top of this file, this step's statement of those old names, and a redirect that names an old URL. The temporary sentences in `docs/plan/` that tell a reader to swap the prefix are removed once the directories exist. The catalog stems match the directories. `./build.sh` succeeds for every `volumeN-` stem. An old reader or download URL that used a `tome` stem still resolves. Cover artwork is the same picture.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/28
- **Merge sha:** 5266fdff2a92cc0ee18a3b708bf595f3096807bc
- **Date:** 2026-10-29
- **Notes:** Squash-merged. Do this before any content step. It supersedes the earlier rule that directory names and TeX macro names stayed `tome` while the English word was already Volume. Do not revive `tome0-mathematical-maturity`, `tome9-higher-structures`, `tome14-order-and-chance`, or the other pre-renumbering stems. The `volumeN-` paths in `docs/plan/` become directories when this step merges.

### 3. Spaces: conditional expectation, and the almost-every chapter

- **Status:** DONE
- **Depends on:** 2
- **Books and files:** `volume7-spaces`. Promote conditional expectation, including the tower property, from the exercise in `chapters/ch10-radon.tex` to a numbered theorem. Retitle `chapters/ch12-harder.tex` to Almost every number, still inside Measures on Spaces.
- **Acceptance:** Books 11 and 12 can cite the tower as a theorem of Book 7. The problem chapter's title is no longer "Harder problems". `./build.sh volume7-spaces`.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/29
- **Merge sha:** 832e24bed70693dba9b3aa48fbdc9406062a1eb1
- **Date:** 2026-10-29
- **Notes:** Squash-merged. Do this before any edit to Randomness or Random Motion.

### 4. Orders, from Chance to First Principles

- **Status:** DONE
- **Depends on:** 3
- **Books and files:** `volume4-chance/chapters/orders.tex` moves into `volume1-first-principles`, inside Algebra, Limits and Functions. Appendix B of Chance stays.
- **Acceptance:** Dilworth, Sperner, and partial orders are in Book 1. Book 4's Random Structures no longer contains that appendix. Both books build.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/30
- **Merge sha:** 3335f6f01eea9a77ea9774c7f93aac3e91d16825
- **Date:** 2026-10-29
- **Notes:** Squash-merged. Do not re-implement the move.

### 5. Hidden worlds, from The Integers to Arithmetic

- **Status:** DONE
- **Depends on:** 4
- **Books and files:** `volume2-integers` (`ch11-algebraic.tex`, `ch12-ideals.tex`, `ch12-padic.tex`) and `volume13-arithmetic`. Hensel's lemma for a congruence stays in Book 2. One section keeps \(6=2\cdot 3=(1+\sqrt{-5})(1-\sqrt{-5})\). While Arithmetic is open, read the repaired three-squares test in `ch07-hasse.tex` once.
- **Acceptance:** Those three chapters are in Book 13's Number Fields and Local and Global parts. Book 2 still proves Pell, the Gaussian integers, and reciprocity. Apply the proposed part rename in `common/series-catalog.json`: Book 2, Part IV, **Equations and Characters**. Regenerate the series files from that catalog. Both books build.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/31
- **Merge sha:** 57ec8496f3afa57b505c1604f12ff1f7d18af141
- **Date:** 2026-10-29
- **Notes:** Squash-merged. This is the only PR that renames Book 2's part.

### 6. The adèles, from Analysis to Arithmetic

- **Status:** DONE
- **Depends on:** 5
- **Books and files:** `volume8-analysis/chapters/ch08-haar.tex` and `volume13-arithmetic` (local fields and Tate). Haar measure and Pontryagin duality stay in Fourier and Tauberian Methods.
- **Acceptance:** The construction of \(\mathbb Q_p\) and the adèles, beyond Haar measure, is in Book 13. Book 8 still states the duality it uses. Both books build.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/32
- **Merge sha:** 921c260b7829a1bbd8947fe8e6d86423eb53c2a7
- **Date:** 2026-10-29
- **Notes:** Squash-merged. Do not move Jordan or the Riemann mapping theorem in this PR.

### 7. Symmetry's extra linear algebra

- **Status:** DONE
- **Depends on:** 6
- **Books and files:** `volume3-symmetry` appendices, `volume8-analysis`, `volume10-abstraction`. Spectral theorem, SVD, graph spectra, matrix inequalities, linear dynamics, and the linear algebra that repeats Book 1 go to Analysis. Tensors go to Abstraction, Categories. Circulants, Perron roots of a symmetry, and the linear algebra method stay in Book 3.
- **Acceptance:** Book 3's contents are Groups, Rings and Polynomials, and Fields and Galois Theory, plus the appendices that still count by symmetry. Analysis and Abstraction build with the new files. No part rename.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/33
- **Merge sha:** b6e61fa17d66389b466c3fd6019cde5e5ef46e64
- **Date:** 2026-10-29
- **Notes:** Squash-merged. Do not re-implement the move.

### 8. Still spectra, from Random Motion to Analysis

- **Status:** DONE
- **Depends on:** 7
- **Books and files:** `volume12-random-motion` (`ch09-expanders.tex`, `ch10-semicircle.tex`, `ch11-cue.tex`, the expander half of `chapters/spectral.tex`) and `volume8-analysis` Spectral Theory. Dyson Brownian motion stays in Stochastic Calculus. The zeta narrative in `moments.tex` stays until step 19.
- **Acceptance:** The semicircle, the sine kernel, and the graph-theoretic Riemann hypothesis are theorems of Book 8. Book 12's third part is walks on graphs, resistance, and the matrix-tree theorem. Apply the proposed part rename: Book 12, Part III, **Networks**. Regenerate the series files. Both books build.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/34
- **Merge sha:** a4934a3358d481119923201228beeca6ccc6200f
- **Date:** 2026-10-29
- **Notes:** Squash-merged. This is the only PR that renames Book 12's part. Later books cite the sine kernel as Book 8. The branching random walk stays in Book 12, in Stochastic Calculus.

### 9. Jordan to Spaces, Riemann mapping to Shapes

- **Status:** DONE
- **Depends on:** 8
- **Books and files:** `volume8-analysis/chapters/ch09-complex.tex`, `volume7-spaces`, `volume9-shapes`. Phragmén–Lindelöf, Hadamard factorisation, and Dixon stay in Analysis.
- **Acceptance:** Jordan's theorem is in Metric and Topological Spaces. The Riemann mapping theorem is in Groups and Geometry. All three books build.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/35
- **Merge sha:** 4be04914e2d49400eb7482b46723653aca424b5c
- **Date:** 2026-10-29
- **Notes:** Squash-merged. Do not re-implement the move.

### 10. Shapes: the connection pass

- **Status:** DONE
- **Depends on:** 9
- **Books and files:** `volume9-shapes`. Fold the Euclid appendix: Ceva and the Euler line into the transformations appendix; the rest of that appendix leaves the main text. Mark the general de Rham sentence as the punctured-plane case. Rename the second curvature chapter so it is not a second "Curvature". Point the cubic group law at Book 13.
- **Acceptance:** A reader of *The Geometry of Connection* does not meet a second chapter with the same title, or a Euclidean gallery that does not connect. `./build.sh volume9-shapes`.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/36
- **Merge sha:** 5586cb822895f37682f988c513fd4e80e3c356e5
- **Date:** 2026-10-29
- **Notes:** Squash-merged. The unused Euclid chapter file is removed in Step 11. Do not re-implement the pass.

### 11. Formulas that are not primes

- **Status:** DONE
- **Depends on:** 10
- **Books and files:** `volume14-primes` (`ch06-partitions.tex`, the Waring half of `ch07-waring.tex`) and `volume5-calculation`, Series and Products. Three primes stays in Additive Problems and Bounded Gaps.
- **Acceptance:** The Hardy–Ramanujan asymptotic and Waring for large \(s\) are in Book 5. Book 14's part name stays Additive Problems and Bounded Gaps. Both books build.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/38
- **Merge sha:** afd199cf1a46b91de37bc6a7cf62119442ce4acd
- **Date:** 2026-10-29
- **Notes:** Squash-merged. Do not rename Book 14's part. Do not re-implement the move.

### 12. The shuffle cutoff, from Abstraction to Randomness

- **Status:** DONE
- **Depends on:** 11
- **Books and files:** `volume10-abstraction/chapters/ch10-shuffling.tex` and `volume11-randomness`, Martingales and Ergodic Theory. Retitle `volume11-randomness/chapters/ch13-harder.tex` to Sums of random pieces. The Fourier analysis of \(S_n\) stays in Representations.
- **Acceptance:** The cutoff is a theorem of Book 11. Book 10's part is still named Representations. Both books build. The tower property cited here is the theorem from step 3.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/39
- **Merge sha:** 7228f2d4a37363d3cdeb1576cc8be6fd73674e7e
- **Date:** 2026-10-29
- **Notes:** Squash-merged. Do not re-implement the move.

### 13. Say that the repeated theorems are returns

- **Status:** DONE
- **Depends on:** 12
- **Books and files:** `volume11-randomness` (Roth in the ergodic chapter; the mod-\(\varphi\) chapter) and `volume14-primes` (Roth). Each Roth introduction names the other proof. The mod-\(\varphi\) chapter labels Selberg–Delange as quoted from Book 15 until step 15, then the next edit of that sentence may name the chapter.
- **Acceptance:** A reader of either Roth proof is told the other exists. The uniform-integer mod-\(\varphi\) statement is not presented as proved in Book 11. Both books build.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/40
- **Merge sha:** f28ae2b927d7fc922327922e3df83e6b1b1b8608
- **Date:** 2026-10-29
- **Notes:** Squash-merged. Do not re-implement the cross-references.

### 14. Abstraction: primary decomposition

- **Status:** DONE
- **Depends on:** 13
- **Books and files:** `volume10-abstraction`, in Commutative Algebra, before Dedekind domains.
- **Acceptance:** Primary decomposition and associated primes are a numbered section. Dedekind domains cite them. Book 13 is not rewritten to depend on them. `./build.sh volume10-abstraction`.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/41
- **Merge sha:** 07992d9b6e133f0b5357f5baa76a613623b2acb3
- **Date:** 2026-10-29
- **Notes:** Squash-merged. The section is in `chapters/ch04-localisation.tex`, and Dedekind domains cite Theorem `thm:assprimes`. Book 13 was not rewritten.

### 15. Book 15: the chapters the series already quotes

- **Status:** DONE
- **Depends on:** 14
- **Books and files:** `volume15-order-and-chance` only. Finish The Question and the start of Arithmetic Statistics from `ra-largemoduli.tex`, `ra-gaps.tex`, `ra-additive.tex`, `ra-selbergdelange.tex`, and `ra-erdoskac.tex`, and Spectra's value-distribution chapter from `ra-bohrjessen.tex` and `ra-selberg.tex`. Shrink the second Erdős–Kac write-up to a comparison with Book 6. Gallagher's hypothesis stays in the heading of Maier's theorem.
- **Acceptance:** Buchstab, Maier, the Erdős–Rankin bound, Kubilius, Selberg–Delange, Bohr–Jessen, and Selberg's central limit theorem are proved in Book 15 and cited as such. Erdős–Kac is not founded a second time. `./build.sh volume15-order-and-chance`.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/44
- **Merge sha:** 6b6eda63a60723562e693a4794467ecbeef7722f
- **Date:** 2026-10-30
- **Notes:** Manuscript done in this pull request. The quoted chapters are the live includes; the second Erdős–Kac write-up is a comparison with Volume 6. Gallagher's hypothesis stays in the heading. Merge sha left blank until this pull request merges. Interior XeLaTeX of Volume 15 was checked (three passes, references resolved, layout check passed). The full `./build.sh` press export was not finished.

### 16. Book 15: the five openings

- **Status:** DONE
- **Depends on:** 15, and step 8 for the sine kernel's address
- **Books and files:** `volume15-order-and-chance`: `ch05-short.tex`, `ch06-sieves.tex`, `ch08-ranks.tex`, `ch09-gue.tex`, `ch12-pseudorandom.tex`.
- **Acceptance:** Each file is a chapter, not a fifteen-line opening. Each cites a theorem from Books 6–14 and proves only the sentence those books did not prove. The form factor cites Book 8. Green–Tao stays quoted. `./build.sh volume15-order-and-chance`.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/44
- **Merge sha:** 6b6eda63a60723562e693a4794467ecbeef7722f
- **Date:** 2026-10-30
- **Notes:** Manuscript done. The five files are chapters. The form factor is proved here and cites Volume 8. Green–Tao is quoted. The pair-second-moment chapter proves the logarithmic term; the coefficient \(\gamma+\log 2\pi-1\) is identified through \(\zeta'(0)=-\frac12\log(2\pi)\), not expanded into a separate residue calculation.

### 17. Book 15: class groups, moments, and bias

- **Status:** DONE
- **Depends on:** 16
- **Books and files:** `volume15-order-and-chance`: Cohen–Lenstra (`ra-cohenlenstra.tex` and the cokernel argument in `ch05-sandpiles.tex`), moments (`ra-moments.tex`), bias (`ra-bias.tex`).
- **Acceptance:** The cokernel theorem lives in the class-group chapter, not in two chapters. The moments chapter either proves the approximate functional equation or marks every use of it. Chebyshev's bias names its hypotheses. The heuristic headings say heuristic. The book builds.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/44
- **Merge sha:** 6b6eda63a60723562e693a4794467ecbeef7722f
- **Date:** 2026-10-30
- **Notes:** Manuscript done. Symmetric cokernels are proved once in the class-group chapter (`ra-symmoments.tex`). The sandpile tour is not in `main.tex`. The old file `ch05-sandpiles.tex` still contains that proof and is not included. Approximate-functional-equation uses are marked. The bias chapter names GRH and linear independence. The zeta-spacing picture in Spectra is a non-floating center, not a `figure`.

### 18. Park the workshop proofs that belong elsewhere

- **Status:** DONE
- **Depends on:** 17
- **Books and files:** `volume15-order-and-chance` and the destinations in `book-15.md`: BBP and Borwein integrals to `volume5-calculation`; Gilmer to `volume4-chance`; Mason–Stothers, polynomial Fermat, and the three-cubes identities to `volume13-arithmetic`; the polygonal Jordan theorem to `volume7-spaces`; Paley and Sylvester to `volume3-symmetry`; the branching-random-walk half-moment to `volume12-random-motion`.
- **Acceptance:** Each moved proof builds in its new book. Book 15 no longer contains a second copy. The reading method and the two projects are not deleted in this PR.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/44
- **Merge sha:** 6b6eda63a60723562e693a4794467ecbeef7722f
- **Date:** 2026-10-30
- **Notes:** Manuscript done. The proofs now live in Calculation, Chance, Arithmetic, Spaces, Symmetry, and Random Motion. The riffle cutoff is in Randomness. Those destinations were typeset with XeLaTeX. Book 15's `main.tex` no longer includes a second copy. The old workshop sources remain on disk and are not input.

### 19. The Research Workshop, reduced to the meeting

- **Status:** DONE
- **Depends on:** 18
- **Books and files:** `volume15-order-and-chance` only. Cut the tours listed in `book-15.md` (Collatz, the empty zeta pointer, Goldbach, the Riemann-hypothesis appendix, BSD, the randomness tour, the algebra tour, Curry–Howard, and the conjecture surveys already owned by Books 6 and 14). Keep the part name The Research Workshop. What remains is the reading method, practised on Maier or Selberg, and the two projects.
- **Acceptance:** Appendix E is gone. The part is still named The Research Workshop. The book builds, and a reader can see the meeting of structure and randomness in every chapter that remains.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/44
- **Merge sha:** 6b6eda63a60723562e693a4794467ecbeef7722f
- **Date:** 2026-10-30
- **Notes:** Manuscript done. The part is still The Research Workshop. What `main.tex` includes is the reading method and two projects (`ch14-meeting.tex`). The zeta narrative is in Spectra. `volume12-random-motion/chapters/moments.tex` is no longer input. The cut workshop files and conjecture appendices are still in the tree.

### 20. The leftover sentences

- **Status:** DONE
- **Depends on:** 19
- **Books and files:** `volume8-analysis` (the blurb matches the compact spectral theorem; the zeta-problem chapter is retitled), `volume14-primes` (the discriminant of \(\mathbb Q(\sqrt 2)\) points at Book 13's figure, not at the ramification theorem).
- **Acceptance:** The public blurb does not claim the unbounded spectral theorem. The primes citation resolves. Both books build.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/44
- **Merge sha:** 6b6eda63a60723562e693a4794467ecbeef7722f
- **Date:** 2026-10-30
- **Notes:** Manuscript done. The blurb states the compact spectral theorem. The former problem chapter is titled The values of zeta. The discriminant of $\mathbb Q(\sqrt 2)$ points at Volume 13's lattice. Volumes 8 and 14 were typeset with XeLaTeX.

### 21. The story pass

- **Status:** DONE
- **Depends on:** 20
- **Books and files:** the preface of each `volume1-first-principles` through `volume15-order-and-chance`. One paragraph names the series question and the floor's element. Part names are not edited again.
- **Acceptance:** A reader of any preface can say which floor this is and what the next floor takes up. No title or subtitle changes. The books whose prefaces changed still build.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/44
- **Merge sha:** 6b6eda63a60723562e693a4794467ecbeef7722f
- **Date:** 2026-10-30
- **Notes:** Manuscript done. Each preface names the series question, this floor, and the next floor. No title or subtitle was changed. First-edition copy check passed on all fifteen volumes. Interior XeLaTeX was run for every volume whose body changed, not only the prefaces.
