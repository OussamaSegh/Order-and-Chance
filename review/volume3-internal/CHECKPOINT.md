# Restart checkpoint

Baseline: `7f87c2ab00fdb0c7791dc833423b98bef0870f01`.
Branch: `editorial/volume3-complete-internal-review-20261104`.
Checkpoint: V3-002. PR #104 draft. Chapter 1 source changed; see CH01-REVIEW.md.

Next: build the committed checkpoint in an immutable worktree, continue actual
printed-order reconstruction at Chapter 2 (lines1–140 read so far), record its
exercise prompt-first solutions before opening supplied solutions. Finish global
bibliography/history and all later mathematical/editorial/production gates.
Do not inherit any approval from `review/volume3-rewrite/`. 21 manual internal
mathematical acceptances (8 results/13 exercises); all remaining blocks pending.

Main has no observed advancement since the initial fetch. No builds have been
started yet, no pages opened, no final CI or publication acceptance claimed.

Toolchain: `source /workspace/volume3-tools/activate.sh` adds local optimizers and
library path after required workspace activation. EPUBCheck jar is under
`/workspace/volume3-tools/epubcheck-5.3.0/`. Existing463 tests and the V3/check_chapter1
checks pass. The context regression rejects baseline Chapter11 premise.
