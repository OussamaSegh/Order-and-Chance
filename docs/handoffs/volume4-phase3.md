# Volume 4 Phase 3 handoff

**Updated:** 10 November 2026.
**Tracker:** https://github.com/OussamaSegh/Order-and-Chance/issues/139
**Reviewer:** the designated validator (an AI reviewer). Not an external referee, and not a publication approval.

## Baseline

| Item | Observed value |
| --- | --- |
| `main` at inspection | `2655cf5ac02c0a1c510c0da13f8c6b223c4d9c5f` |
| PR #135 | MERGED. Head `199ef70b50333da61e6cc6aeb9b8fbc74eb91ef5`. Merge `1778324959ba8e7d027cd5384d9ccdc9065fec20`. |
| PR #136 | MERGED. Head `5d12f8e1fdc423dae9e8ccf2f1325a848817007b`. Merge `070b9e00a5afadbe3d4153339cfd99cd72329d24`. |
| PR #137 | MERGED. Head `049e451c413257eeab70579b665ebf63fe91238c`. Merge `2655cf5ac02c0a1c510c0da13f8c6b223c4d9c5f`. |
| Issue #138 | CLOSED. Owner comment: Actions billing was the cause and has been fixed. Later exact-head runs of #135–#137 executed steps and succeeded. |
| Open PRs at start | #113 and #114, both draft and conflicting. Left untouched. |
| Volume 4 sources | `volume4-chance/`. Four parts, fourteen chapters, Appendix B. `main.tex` is the inclusion order. |
| Figure inventory | 41 `\fig` names, pinned in `tools/test_volume4_route.py`. |

`git diff 5d12f8e1fdc423dae9e8ccf2f1325a848817007b 2655cf5ac02c0a1c510c0da13f8c6b223c4d9c5f -- volume4-chance common` was empty. PR #137 changed only the acceptance register.

## After publication — 10 November 2026

Author authorization, 11:37 Europe/Paris: “Yes you merge and publish, then go to next phase, dont wait for me.”

Published source `22e9d49410eb95dad6d505c1e568a21b7fd4d828`. Release https://github.com/OussamaSegh/Order-and-Chance/releases/tag/books from Build books [42806203843](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42806203843). Downloaded Volume 4 asset hashes match the release digests. Site https://oussamasegh.github.io/Order-and-Chance/ lists Volume 4.

No next numbered phase is defined. The excellence plan stops at Phase F. The series plan’s next floor is Book 5, and `docs/plan/PROGRESS.md` is a Volume 1 tracker. Do not invent a phase. KDP upload of the print PDF and paperback cover remains the author’s account.

## Open drafts #113 and #114 — closed as superseded, 10 November 2026

Author instruction, 17:11 Europe/Paris: finish the open Volume 4 pull requests before any next phase. The only open pull requests were the two drafts below. Both still target `cursor/volume4-rewrite-ee7f`, the branch of merged #111, and both conflict with current `main`. No replacement pull request was opened, because neither draft still changes the published tree correctly.

### #113, head `f6960dd6ed70fa3dd5696cd9e7158399df1da150`

The manuscript commits restore proofs in Volumes 11, 12, 14 and 15 on the assumption that the Volume 4 rewrite had deleted them, and they retarget citations to that deleted numbering. The published Volume 4 still contains the results. Numbered on current `main` by walking `theorem`, `proposition`, `lemma`, `corollary`, `definition` and `example` in `main.tex` order (`theoremx` does not step the counter; exercises have their own counter; the appendix is letter B):

| Cited now | Label | What it states |
| --- | --- | --- |
| Theorem 6.8 | `thm:inversion` | Uniqueness, and the density formula when the characteristic function is integrable |
| Theorem 6.10 | `thm:lindeberg` | Lindeberg |
| Theorem 8.6 | `thm:arcsine` | First-return convolution, the nonnegative-path identity \(P(S_1\ge0,\ldots,S_{2m}\ge0)=u_{2m}\), and \(P(L_{2n}=2k)=u_{2k}u_{2n-2k}\) |
| Theorem 8.8 | `thm:arcsinelimit` | The arcsine limit of those weights |
| Lemma 9.7 | `lem:tvcontract` | Total variation does not increase |
| Definition 9.8, Theorem 9.9, Proposition 9.10 | `def:ashuffle`, `thm:bayerdiaconis`, `prop:rifflecompose` | The \(a\)-shuffle, the exact mass, and composition |
| Proposition 9.11 | `prop:untouched` | The untouched-card lower bound \(1-6e^{1-2c}\) |
| Exercise 9.8 | `ex:risingmean` | Mean \((n+1)/2\) and variance \((n+1)/12\), which is \(\mathbb E[h^2]\) for \(h=r-(n+1)/2\) |
| Theorem 11.9 | `thm:doob` | The probability bound and \(\mathbb E[(Y_n^*)^2]\le 4\mathbb E[Y_n^2]\), on finite partitions |
| Theorem 11.10 | `thm:azuma` | Azuma |
| Theorem 11.12 | `thm:L2conv` | \(L^2\) convergence on interval partitions |
| Theorem 11.14 | `thm:asconv` | Almost-sure convergence on interval partitions |
| Theorem 12.12 | `thm:reflection` | The maximum has the law of \(\lvert B_t\rvert\) |
| Exercise 12.3 | `ex:zeros` | The zero set has outer length 0 and is uncountable |
| Exercise 8.8 | `ex:electric` | Hitting probabilities as voltages |
| Theorem B.7 | `thm:vdw` | Van der Waerden for every length and every finite number of colours |

The current sentences in the files #113 edited already use these numbers. Volumes 11 and 12 already say that Theorems 11.12 and 11.14 are the interval-partition cases, and they send the general filtration to Volume 11. Copying #113 onto `main` would replace those citations with new local proofs and, for van der Waerden, would delete a citation of Theorem B.7 that is the theorem the sentence describes. The oxipng retry in that branch is already on `main`; the Cargo fallback was a workaround for a download that the current workflow retries. The draft’s own body says its mathematical review was not finished.

### #114, head `3191fa4646f1c12707fe6df46ed54cdf17dc9357`

The draft folds a one-line Stirling note into the de Moivre item so that note will not sit alone on a print page. On current `main` that note is already inside the de Moivre item, and item 4 is Lévy’s *Calcul des probabilités*, which the draft’s diff would delete. The published print interior is `Volume 4 - Chance - Print.pdf`, 289 pages, 513×738 pt, SHA-256 `b7ff97461a4afe2838aeccf2a84ce9bf7cd6cd82dfd2b4a5d93847485e57ae50`. Print page 143 carries the end of the Chapter 6 cycle solution and all four source items. Print page 144 is the opening of Chapter 7. There is no bibliography orphan. Volume 4 was not rebuilt.

No other Volume 4 pull request is open. The other `volume4` branches on the remote are tips of pull requests already merged or, for #115, closed. Their commits are not ancestors of `main` only because those pulls were squash-merged. Nothing on them was ported. The `books` release was not replaced.

## Gate status after the #140 merge

| Gate | Status | Why |
| --- | --- | --- |
| 3A | PASS on the merged tree | #140 head `cfe5d152a8aa2bc74b7b96f5824369a86e175b92` merged as `3cc07e8673490b9922db9d9d29fee0551e2d8a12`. The two commits have an empty diff. Build books [42783238606](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42783238606) and native QA [42783238907](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42783238907) both succeeded on that head before the SHA-guarded squash. The PR `publish` job was skipped. The merge push started Build books [42786721619](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42786721619) on `main`. |
| 3B | PASS | Source audit plus rendered captions on reading pages 205, 211, 249 and the matching print pages. |
| 3C | PASS | `docs/review/volume4-phase3-pedagogy-2026-11-10.md`. No critical defect, so no further chapter edit. |
| 3D | PASS for Volume 4 and DEP-12..29 | Proposals #141, #142, #143 stay open. Tonelli in Volume 5 was not edited. |
| 3E | PASS for opened files | `docs/review/volume4-phase3-production-qa-2026-11-10.md`. No device. |
| 3F | CANDIDATE | `docs/review/volume4-phase3-release-candidate.json`. Not author approval. |

## Merged and left open

- Merged: #140, squash `3cc07e8673490b9922db9d9d29fee0551e2d8a12`.
- Open for the author: #141 Volume 6, #142 Volume 5, #143 Volume 11. Do not merge them in this phase.
- Drafts #113 and #114 were not touched.

## If this run stops

1. Read the conclusion of Build books [42786721619](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42786721619) on `3cc07e86`. If it failed, the failure is the next defect. If it succeeded, the candidate tree has a `main` integration build.
2. Do not edit issue #139. Updates return HTTP 403. Use this file and the pull-request body.
3. Do not tag a release and do not upload to KDP.

## Permission limits

Workflow dispatch on `main` returned HTTP 403. Issue edit and issue comment on #139 returned HTTP 403. The issue body is still the placeholder created at open.
