# Batch B — Elementary number theory

## Changes implemented
Chapters 1–2: explicit zero/sign conventions, unit coin cases, elementary binomial input for exercise n2n, trial-division/primality/factorization distinctions and analytic prerequisites before prime bounds. Historical claim about the first complexity analysis is qualified.

## Mathematical improvements
The introductory exercise no longer borrows Fermat from a later chapter. Its proof derives the required base-2 congruence directly from binomial divisibility and legal cancellation. Valuation formulas stay restricted to nonzero inputs. The coin solution explicitly includes a denomination 1.

## Pedagogical improvements
Distinguish a primality decision, a factor and a complete factorization; distinguish input digits from numerical magnitude. Retain the ideal-theoretic gcd definition: the existing concrete wheel opening and complete Euclidean/back-substitution examples already support it, and it is the invariant reused in later rings.

## Content preservation
All 205 labels and all 97 original exercise/hint/solution triples retained. No figure, portrait or bibliography entry removed. Original source checkpoint: volume1-batch-A.

## Verification
Full PDF build passes layout, style, PDF-body identity and cover preflight. Cumulative reading/interior PDFs and logs at `/workspace/volume1-checkpoints/B/`. Independent script `check_math.py` executes 32,298 finite/exact-symbolic assertions, including signed division, coin degeneracies, prime-power bounds, reciprocity, four-square identity, ideal lattice products and singular-root survival. These support source review and do not prove universal claims. `inventory.py` and `git diff --check` pass.

## Remaining issues
Structural moves, advanced exposition and complete second-pass proof/solution review remain. No claim of a final mathematical audit yet.

## Next work
Batch C: remove the totient dependency barrier and reorder the middle elementary chapters; define ring-map terminology.
