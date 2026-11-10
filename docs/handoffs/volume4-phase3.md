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

## Gate status (do not upgrade without new evidence)

| Gate | Status | Why |
| --- | --- | --- |
| 3A | IN_PROGRESS | Build books [42736422791](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42736422791) on exact `2655cf5a`: list job `Ran 616 tests` `OK (skipped=32)`; `changed: []`; cache restored from `library-v9-070b9e00…42727299179`; site job validated print preflight for Volumes 1–15 and uploaded Pages artifact `sha256:a30a2b83de26a3beca8bc28d5509ea14d96b2a7871309f43a157a9e58c754152` (557 MB). `publish` job 129571188268 was skipped with zero steps. That did not publish a new release. Native QA [42723990578](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42723990578) succeeded on `5d12f8e1`, whose `volume4-chance` and `common` trees match this baseline. `gh workflow run` of native QA on `main` returned HTTP 403. A pull request that touches `volume4-chance/**` or `tools/**` is what starts a fresh native run. |
| 3B | IN_PROGRESS | Source audit written. Three charcoal-called-blue defects corrected on this branch. Rendered recheck of those plates is the next figure action. |
| 3C | UNASSESSED | Chapter reading for teaching defects has not been written up. |
| 3D | IN_PROGRESS | Eighteen repairs intact. Volumes 1–3 frozen. Four critical downstream citations are demonstrated and not yet patched. See the dependency audit. |
| 3E | UNASSESSED | No inspection yet of a PDF built from the colour-word repair. No physical device. |
| 3F | UNASSESSED | No release-candidate manifest. |

## This branch

`cursor/volume4-phase3-qa-5cfc`

- Ink-word repairs in the Poisson clock, the queue legend, and the Brownian reflection caption.
- Route test pins the 41 names. Figure test pins the corrected words.
- Audits: `docs/review/volume4-phase3-figure-audit-2026-11-10.md`, `docs/review/volume4-phase3-dependency-audit-2026-11-10.md`.
- Register section “Phase 3 book-wide QA”.

## Next executable actions

1. Open the pull request for this branch. Required checks: Build books, and Volume 4 native QA (the path filter includes `volume4-chance` and `tools`). Do not merge until both are green on the exact head.
2. Download that native artifact and inspect the three corrected plates in the print PDF and the EPUB. Record page geometry, font embedding, and checksums. Do not claim a Kindle or a paper proof.
3. Read Volume 4 chapter by chapter for teaching defects. Patch only a demonstrated critical defect in Volume 4. Leave subjective voice notes in the pedagogy report.
4. Open separate unmerged proposal branches for the four critical downstream citations (Volume 6 Theorem 2.11 and the Hoeffding repair of `ex:shortmodel`; Volume 5 `ex:ritelli`; Volume 11 Theorem 10.21). Do not edit Volumes 1–3. Do not merge Volumes 5–15 source changes.
5. After the final `main` commit, record artifact checksums in a release-candidate manifest. Do not tag a release, do not upload to KDP, and do not mark author approval.

## Permission limit already hit

Workflow dispatch is forbidden for this token (`HTTP 403`, `Resource not accessible by integration`). Pull-request events still start the workflows. Do not treat a skipped `publish` job as a failed book build, and do not force a publish.
