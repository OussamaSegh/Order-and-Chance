# Phase 2: Brownian joint-measurability downstream prerequisite repair
Date: 9 November 2026. Sole mathematical validator: ChatGPT GPT-6.
Baseline main: 6c12b6f7d2be9de3771ff38397f25710d8671ee1 (merged PR #122).
Status: V4-P2-011 SOURCE-FIXED, awaiting exact-head CI and post-merge source confirmation. Full Phase 2 incomplete.

## Confirmed defect V4-P2-011 (P1, mathematical prerequisite)

The published-architecture Volume 12 source volume12-random-motion/chapters/ch02-paths.tex contains two false references to **nonexistent subparts** of Volume 4, printed Exercise 12.3 (stable label ex:zeros in volume4-chance/chapters/ch11-brownian.tex):
- In theorem thm:zeroset's proof, the conclusion that a closed set without isolated points is uncountable was attributed to "Volume 4, Exercise 12.3(c)". Volume 4's actual ex:zeros has **no lettered parts**, although its one complete solution DOES prove the needed perfect-set consequence.
- In Volume 12's solution ex:fast, the fact that (t,omega)->B_t(omega) is jointly measurable (needed to invoke Tonelli on the random set of fast Brownian times) was attributed to "Volume 4, Exercise 12.3(a)". Volume 4's ex:zeros contains **no such statement or proof**. This was a missing logical premise, not just cosmetic numbering.

The problem was explicitly anticipated in the historical docs/review/volume4-citation-sweep.md but was not repaired in current source. That historical ledger also contains outdated descriptions of Volume 4's *now present* Fourier-inversion and martingale theorems, so old inventories are not a substitute for checking current blobs.

## Source correction and proof

Do not edit Volume 4 to invent new exercise subparts. Change Volume 12 thm:zeroset's reference to **Volume 4, Exercise 12.3**, accurately invoking its uncountability proof.

Prove joint measurability where Volume 12 uses it:
For every integer m>=1 and t>=0 define B_m(t,omega) = B_{2^-m floor(2^m t)}(omega). For fixed m, this process is constant on deterministic Borel time strips [j2^-m,(j+1)2^-m), and equals the measurable coordinate B_{j2^-m}(omega) there. It is therefore product-measurable as a countable union of measurable strips. For every continuous sample path, the left dyadic approximating times increase toward t within distance strictly less than 2^-m, and continuity implies B_m(t,omega)->B_t(omega) for all t simultaneously. Use a continuous-path modification on the exceptional null set. Pointwise limits of jointly measurable functions are measurable; translation t->t+h preserves this property. The fast-point solution's countable rational-h limsup is now jointly measurable, so the Tonelli step has a proved premise. No proof of general Tonelli is borrowed from V4; Volume 12 has its own measure-theoretic foundations.

This local proof requires only that each B_q is a random variable and that Brownian paths are continuous (both present in Volume 4); it does **not** assume the false conclusion as a prerequisite.

## Tests and scope

tools/test_volume4_phase2_downstream_references.py:
1. Checks ex:zeros truly has no enumerated subparts and that the repaired Volume12 source has the actual dyadic construction, rather than imaginary citations.
2. Independently checks the exact inequality 0<=t-floor(2^m t)/2^m<2^-m for rational times (including t>1), and a deterministic continuous-path approximation.
3. Inspects every current later-volume chapter .tex source for the specific invalid form "Volume 4, Exercise 12.3(a/b/c/...)" and fails if reintroduced.

These are **regression checks**, not a formal proof of joint measurability or a complete mechanical audit of every downstream Volume4 theorem number.

Immutable Volumes 1–3 are untouched. Volume 4's 14 chapters and Appendix B are unchanged. Only Volume 12's logically invalid references and their missing local justification are modified, plus tests and acceptance evidence.

## Remaining mathematical acceptance

Exact-source review still required for all 127 V4 proof-bearing claims and 107 exercise/hint/solution triples (plus 41 individual figure semantics), and full downstream Volumes 5–15 prerequisite/citation graph beyond the two proven errors. The author designated ChatGPT GPT-6 the sole mathematical validator, without any external referee gate, but that does not mean these unfinished checks are already verified.

Merge gate: Build books and Volume 4 native QA on the exact PR head; record actual observed workflow statuses before merging.
