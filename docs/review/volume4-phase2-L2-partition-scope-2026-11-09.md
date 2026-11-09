# Volume 4 Phase 2 — L2 martingale theorem event-domain audit
Date: 9 November 2026. Sole mathematical validator: GPT-6 (author-designated).
Branch baseline: main at merge #122 6c12b6f7d2be9de3771ff38397f25710d8671ee1.
Confirmed issue: V4-P2-012 (P1, proof hypothesis / probability-model mismatch).
Status: SOURCE-FIXED; CI and acceptance at exact PR head pending. Whole Volume 4 Phase 2 mathematical acceptance not finished.

## Adversarial verification of the actual source

In the printed Chapter 11 source volume4-chance/chapters/ch10-martingales.tex, thm:L2conv stated L2 martingale convergence for arbitrary "finite partitions", but the actual almost-sure proof said every maximal-deviation event was a finite union of digit cylinders. That does *not* follow merely from finiteness of a partition. Without assuming a countably additive measure on arbitrary sample-space events, the step equating the outer content of the countable union of maximal-deviation events with the limit of its finite-stage probabilities was unproved. This is an applicability/justification gap, not a counterexample to the usual L2 martingale convergence theorem on standard measure spaces. The following theorem thm:asconv already explicitly restricted its partitions to intervals for exactly this reason.

## Minimal source repair

1. State thm:L2conv precisely for refining finite partitions of the Chapter 1 unit interval whose atoms are **finite unions of half-open intervals**. They include the book's finite-digit cylinder experiments. That hypothesis justifies the expectation and countable outer-content continuity needed by the proof. The statement retains every conclusion: almost-sure and square-mean convergence and conditional expectation identity on each finite atom.
2. In the proof replace the unsupported inference "every finite partition event is a digit cylinder" with the correct interval hypothesis and cite the elementary length/outer-content argument already proved in prop:modes. Spell out that the general probability-space version needs continuity from below.
3. In thm:polyaurn construct an explicit admissible realization rather than silently assuming a colour-history partition is a finite union of **binary** cylinders, which is generally impossible for conditional probabilities like 2/3. Map the empty colour history to [0,1); recursively represent each red/blue history by one half-open interval, split into adjacent subintervals in proportions R/(n+2) and (n+2-R)/(n+2). This gives exact conditional Pólya urn history probabilities as interval lengths and refining finite interval partitions. Hence the L2 theorem applies to the urn on the book's elementary probability space.
4. Note carefully that the **abstract** L2 martingale theorem remains true for general filtrations under countably additive probabilities (introduced in later Volumes 7 and 11). The narrowed Volume4 formulation is the variant actually proved in its earlier foundational setup; downstream uses of the general theorem need the measure-theoretic extension, not a false blanket assertion about arbitrary finite-cylinder events.

## Independent regression

tools/test_volume4_phase2_L2_interval_partitions.py:
- Verify exact theorem hypothesis and the proof's outer-content bridge.
- Recursively enumerate all 2^n distinct Pólya urn histories and corresponding rational half-open intervals for 0<=n<=10 (1,024 histories at n=10); verify exact interval tiling, probability j!(n-j)!/(n+1)!, and each R_n mass 1/(n+1).
- Verify martingale conditional identity from every history interval to its two child intervals at every tested n.
These independent exact-arithmetic checks confirm the *specific urn application's* hypotheses; they are not a formal proof of arbitrary martingale convergence or full exercise acceptance.

## Acceptance boundary

Source repairs and exhaustive tests must pass full Build books and native Volume 4 QA at the new exact PR head before merge. No published V1–3 content changed. Four parts, fourteen printed chapters, Appendix B unchanged.

Remaining Phase2 work: a full pinned-blob math review of all 127 proof-bearing assertions, 107 exercise statements/hints/solutions, detailed all-41 figure semantics/reader QA, prerequisite and all downstream Volumes5–15 references. The author selected GPT-6 as sole validator; no external referee required, but the validator must still document mathematical evidence for each signoff. The new result does not authorize an all-book PASS.
