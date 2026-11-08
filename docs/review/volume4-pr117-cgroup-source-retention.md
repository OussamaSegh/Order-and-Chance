# PR #117 — protected Volume 3 conceptual-source retention after a Volume 4 proof correction

**Date:** 8 November 2026. **Status:** source-side, narrow *internal* retention review; **not independent mathematical refereeing, not a full V3 or V4 reread, and not an acceptance of all Phase 2 proof claims.**

## Why the CI guard rejected the initial PR

The protected `review/volume3-internal/check_global_ledgers.py` computes a SHA-256 over 90 exact source and figure paths captured in `review/volume3-internal/concepts.json`. One tracked source is `volume4-chance/chapters/ch08-markov.tex`. The changed file makes the old reviewed fingerprint stale, so the guarded full Build books run [42521690407](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42521690407), at exact source commit `88d53e6c28e9f78d3fda985daa014fb16aaa27e4`, rejected `C-GROUP` as designed. The first full Python step passed **541 tests (32 skipped)** before that guard rejected. No branch protection or test is altered.

The old `reviewed_snapshot.sha256` was **recomputed from its 90 canonical JSON entries**, not trusted blindly, and matched the stored value exactly. The old Chapter 9 tracked file hash was independently recomputed from `main` and matched the snapshot.

| Verified source property | Value |
| --- | --- |
| Initial main/source merge baseline | `d3a3fd5f135f3f3f881c8371fa2f16f01c3757ad` |
| Initial Phase 2 head inspected | `88d53e6c28e9f78d3fda985daa014fb16aaa27e4` |
| Paths in protected source fingerprint | **90** |
| Tracked paths modified in PR #117 | **1**: `volume4-chance/chapters/ch08-markov.tex` |
| Old Markov file SHA-256 | `02b8a27b1cf8ba8341c078820737b26f606cf8e55badda7afce2020093c16b2d` |
| New Markov file SHA-256 | `d428df3669b09246ef53c30abc391f3fb5bb422d6cac3cac99cc99e80716a800` |
| Prior 90-source snapshot fingerprint | `89915e3a8d86d5d43f276e3d8a222a071daa81d3e62963d1233be4e52b7ee38f` |
| Recomputed snapshot with reviewed replacement | `d5a31e812b0aff51b4b7c16877084375d895bab27eb3575d94d69c3461d3fee9` |

For the verified Markov change, both old and new sources contain 468 physical lines and the entire difference is **line 127**, inside proof `thm:ergodic`. The old proof quoted Volume 2's Bézout theorem for the integer-combination step. The new proof inserts an elementary proof: choose the smallest positive integer linear combination `D` of the finitely many return lengths, allowing signed coefficients; any remainder on dividing one of the lengths by `D` would itself be a smaller positive combination. Hence `D` divides every return length; their gcd is 1, so `D=1`. Every later sentence in that proof is byte-for-byte unchanged. In particular, it still obtains nonnegative combinations `B` and `B+1`, all sufficiently long return lengths, one strictly positive matrix power, and the unchanged coupling and contraction bounds.

## Targeted conceptual-dependency decision

The prior [PR #116 conceptual-source retention](volume4-pr116-cgroup-source-retention.md) rechecked links between Volume 3's representation of finite random walks, stochastic matrices, primitive powers, PageRank, and Volume 4's Markov discussion. That review was not an external, independent referee certification. PR #117's additional elementary arithmetic step does **not** alter any definition, theorem hypothesis or conclusion, finite-state transition probability, coupling construction, shuffle law, comparison with Perron theory, plotted figure, or Volume 3 manuscript text. The relevant protected conceptual IDs include `C-PROBABILITY-INDEPENDENCE`, `C-CONVERGENCE`, `C-PERRON`, `C-JORDAN-SPECTRAL-RATE`, and `C-FINITE-STOCHASTIC-MARKOV`; their original Volume 3 proof anchors and later uses remain unchanged. The change **removes** an external prerequisite rather than importing one.

For this **one** assessed difference, retaining the former Volume 3 *internal conceptual* statuses is justified; the entire prior concepts review is not being repeated. The other 89 fingerprinted paths are unchanged relative to the `main` baseline as established by the complete PR file diff, not by claiming to have reread all 89 files. Only this one reviewed path's fingerprint should be migrated, and the protected guard must still check *all* its original paths, original concept rows, anchors, later-use statuses, and prerequisite/seam sources.

The [Phase 2 mathematics ledger](volume4-phase2-proof-audit-2026-11-08.md) separately marks `V4-P2-002` **awaiting independent mathematical review**. This narrower internal V3 retention does not remove that requirement. The historical erroneous Volume 3 printed “Chapter 8” reference to Volume 4's Markov Chapter 9 remains an inherited separate editorial issue; published Volumes 1–3 have not been edited.

## Revalidation

The expected protected result after this **targeted, documented** source-fingerprint migration is that `check_global_ledgers.py` computes the new hash from actual source files and accepts the unchanged conceptual anchors. This migration is not an instruction to weaken, disable, skip, conditionally bypass or delete any protected check. A later **new** source change inside any fingerprinted path must invalidate this evidence again.

**Next:** run full `Build books`, `Volume 4 native production QA`, all mathematics/route regression tests and a distinct mathematical review at the resulting *exact* head. Never mark this snapshot refresh as independent human or mathematical acceptance.
