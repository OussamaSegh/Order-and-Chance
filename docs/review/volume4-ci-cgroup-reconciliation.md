# PR #111 — isolated full-books CI C-GROUP drift reconciliation

**Date:** 2026-11-07. **Scope:** only the Volume 3 **forward seam into Volume 4**, not a re-review or new acceptance of Volume 3 or Volume 4. **Reviewer:** GPT-6, internal source-consistency assessment. **No independent grok-4.7 / human review claimed.** Source head before repair: `3fdbf7c227e5a04b1b2b8c41d00050457fb8c774`. Branch remains draft, unmerged.

## Observed failure

[Build books #42355290692](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42355290692) failed in the **list** job at `review/volume3-internal/registers.py` → `check_global_ledgers.py:118`, reporting `Whole-volume conceptual source/figure drift: C-GROUP`. It occurs *before* the all-books build matrix; no Volume 4 TeX failure in that job. [Volume 4 native #42355290683](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42355290683) succeeded for exactly the same head, making its PDF/print/EPUB/cover; the print interior has 227 pages, with all mathematical/production acceptance gates still open.

## Mechanical scope of change — checked against `origin/main`

The **entire 90-path** conceptual fingerprint in `review/volume3-internal/concepts.json` was compared with the actual PR #111 changed-files list. Exactly **five of the 90 paths** were changed by this PR; all other 85 remained unmodified. The stored baseline fingerprint `a6c2d765797b970ef0d5d90f7a4765f326fe6fabdacd18fc0bf81056a7bc2a11` was independently reproduced by SHA-256 of canonical sorted-path JSON (keys `path`, `sha256`). On each of these five paths, baseline bytes match the old fingerprint. These are the *actual* source changes (not simply the first failing ID):

| Path | Old SHA-256 | Source SHA-256 at `3fdbf7c2` | Semantic change relevant to Volume 3 |
| --- | --- | --- | --- |
| `common/cover-notes.json` | `38933db274749424821e7bb44c41ad9b344d45f029f108d39cb981a4911e9735` | `9ab1630fa57790024a14b6e699ac0c21d7c1bc58edcfad6330bbb291a799ad47` | One Volume 4 `about` line renames the CLT chapter from `Convergence and the Central Limit Theorem` to `Why the Bell Curve Appears`; no Volume 3 entry changed |
| `volume4-chance/main.tex` | `24f833eed5c2d0488fef527de390b41b818f7aac3ee88f513ca492d8edff22bd` | `e2233b3db10565076de7b375aadabac29f4374910071757599f142678a951190` | Now routes 14 chapters in four parts, retaining the title `Chance: The Logic of Uncertainty`; first Chapter 1 is `ch01-counting.tex`, followed by finite/discrete laws and later Markov |
| `volume4-chance/chapters/preface.tex` | `aadf6236e6882f896f277d0e47b14a194dd21fb1f22cdc66271046627548900f` | `689e6fbd5904922fb40b6e66d4a65a4c02221af74bcca4c1565a4236128681db` | New independent-fair-coin opening (first 3 tails probability 1/8), declares finite vs infinite model distinction, describes Markov as future tool and no Volume 3 dependency |
| `volume4-chance/chapters/ch01-counting.tex` | `5738ececb50279e607ef65aa03900800d9654361d8d0bfd570ebddaa5d4c048d` | `8a9fbee4b79b7490bad006c571f8442124dd78cb3d0e4f3aa764467fe9f99f1f` | Chapter renamed to `From Games to Probability Spaces`, starts by naming finite outcomes and weights, then builds infinite fair tosses through binary digits. Still meets V3's *forward* statement that V4 begins with counting outcomes |
| `volume4-chance/chapters/ch08-markov.tex` | `3999f55f802d6e896c89e68ceed8cea36a731a979d12cf3049f1f9c5e1de2967` | `1ae7ee3f4d291cfe849bddb1bbcc694b4c30b2ca2b5949f2018ca7b89c70b9b6` | Now printed Chapter 9 `Markov Chains and Mixing`; defines finite transition matrices, stationary laws, total variation and coupling, includes an irreducible/aperiodic convergence theorem and a mixing comparison. This file was previously tracked as a future-topic pointer, not a Volume 3 premise or a proof review of Volume 4 |

The Volume 3 inventory `review/volume3-internal/inventory.json` already carries exactly the updated `common/cover-notes.json` hash. Against `main`, that inventory differs in **one supporting-source SHA only**; all 22 source_files, 22 figure inputs, item identities, earlier-source evidence and other metadata were not changed by this PR. `review/volume3-internal/concepts.json` and `seam-sources.json` remained at pre-rewrite fingerprints, which explains the guard. `main` full-books CI [run #42237725258](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42237725258) passed at `5c4840cc`.

## What was actually re-read

`volume3-symmetry/chapters/preface.tex` ends: Volume 4 is *Chance: The Logic of Uncertainty* and asks what can be learned when a change is chosen randomly. V4 title metadata and new preface preserve both claims.

`volume3-symmetry/chapters/afterword.tex` proves a **finite** random-walk calculation on `Z/2Z`: for independent moves (stay with probability 1-p, flip with probability p), the two-state recurrence gives `u_t=[1+(1-2p)^t]/2`. This proof only invokes Volume 1 finite probability and geometric powers, not any theorem from Volume 4. Its final bridge says “Volume 4 ... begins with counting outcomes and builds the tools” for forgetting a starting state. The revised V4 Chapter 1 begins with finite outcome weights before giving an infinite-toss construction; printed Chapter 9 develops finite-state mixing by coupling. The concrete sentence and forward reference still match, without importing any later theorem into Volume 3.

The old `review/volume3-internal/V3-018-SEAMS-COPY.md` explicitly classified its V4 preface/Chapter 1 and Markov reads as a **seam and future-topic pointer**; the Markov `read_scope` in `seam-sources.json` said “not a prerequisite and not full V4 review.” That distinction remains essential.

**Disposition:** The actual five changes alter **future-facing Volume 4 source**, not Volume 3 proofs, figures, references or conceptual anchors. The Volume 3→4 *navigation claim* was manually reread and remains accurate. A fingerprint-only update of the stored seam source hashes and conceptual fingerprint is warranted, **without changing any accepted-internal status, chapter review outcome, authored Volume 3 content, or CI check logic**. This does **not** sign off the newly revised V4 mathematics, independent review or full-volume depth. Re-evaluate the seam whenever V4 changes again.

## Verification / guard integrity

- Reconstruct the old 90-file canonical snapshot SHA-256 and confirm it matches the original stored `a6c2d765...` before writing. Require exactly the five listed old hashes; abort on any other drift.
- Recompute new snapshot SHA-256 using the exact current source byte hashes; update all `reviewed_snapshot_sha256` identities consistently but **do not change** each entry's existing `status`, `first_use_status` or `later_use_status`.
- Update exactly the four Volume 4 entries in `seam-sources.json`; do not change Volume 1–3 source files or the protected `check_global_ledgers.py` / `.github/workflows/build.yml`.
- Re-run [Build books](https://github.com/OussamaSegh/Order-and-Chance/actions) and [V4 native QA](https://github.com/OussamaSegh/Order-and-Chance/actions) on the final checkpoint SHA. Report results truthfully. Other unrelated failures, if any, remain open.

This note is a **source-identity and semantic seam review**, not independent mathematical approval of another volume.