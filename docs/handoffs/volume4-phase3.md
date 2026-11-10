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
