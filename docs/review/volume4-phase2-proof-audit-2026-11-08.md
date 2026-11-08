# Volume 4 — Phase 2 mathematical proof ledger (8 November 2026)

**Status: PARTIAL / AWAITING INDEPENDENT REVIEW.** This is an implementation ledger, not a claim of whole-volume proof acceptance, an independent referee report, a formal verification, or publishing approval.

**Base:** main at d3a3fd5f135f3f3f881c8371fa2f16f01c3757ad (merged Phase 1 PR #116). **Implementation branch:** audit/volume4-phase2-proof-dependency-2026-11-08. The excellence plan and independent acceptance register in [PR #115](https://github.com/OussamaSegh/Order-and-Chance/pull/115) remain on an unmerged plan branch; they were consulted there, not silently copied onto main. Phase 1's [baseline audit](volume4-phase1-baseline-math-2026-11-08.md), [historical chapter issue log](volume4-chapter-issue-log.md), and the [prerequisite register](../plan/volume4-prerequisites.md) were reconciled before changing manuscript text.

## 1. Findings, mathematical basis and exact repair commits

| ID / severity | Printed chapter and stable target | Incorrect claim or missing premise | Minimal repair, verification and remaining disposition |
| --- | --- | --- | --- |
| V4-P2-001 / P1 (false prerequisite statement) | Ch. 10, chapters/ch09-poisson.tex, paragraph after the gap fourth-moment calculation and before thm:uniform; depends on thm:slln4 | It said the fourth-moment strong law requires the distribution function to be strictly increasing over all real numbers, and therefore does not apply to exponential gaps. In fact, thm:slln4 explicitly requires the inverse-quantile construction and a finite fourth moment, not that strict monotonicity. For U uniform on (0,1), -ln(1-U)/lambda is exponential(lambda) and its fourth moment is 24/lambda^4. | [bd3704f](https://github.com/OussamaSegh/Order-and-Chance/commit/bd3704f53ff557646921d573d0b311ba28d2dc87) corrects the applicability claim while retaining the independent proof of finite N(t) from Poisson counts. Regression checks inverse-CDF arithmetic and source claim. **Source fixed; independent recheck pending.** |
| V4-P2-002 / P1 (unproved dependency relative to declared route) | Ch. 9, chapters/ch08-markov.tex, thm:ergodic, proof that aperiodicity eventually gives a positive matrix power | The proof explicitly imported Bézout's identity from Volume 2, while the current prerequisite register states that the main Volume 4 proof route requires no Volume 2 result. The theorem is not false, but that dependency contract was untrue. | [575ba40](https://github.com/OussamaSegh/Order-and-Chance/commit/575ba40ea1cbb746c7581ee420e55e17fe31eed4) proves the needed finite gcd-one integer combination using the least positive integer combination and Euclidean division; [517ee84](https://github.com/OussamaSegh/Order-and-Chance/commit/517ee8421d535690e9e6af2b8f2088739778b469) clarifies signs of coefficients. Downstream argument obtains consecutive nonnegative return lengths B,B+1 and all lengths >= B^2. The regression checks return lengths (6,10,15), a gcd-one family with no coprime pair. **Source fixed; independent recheck pending.** |
| V4-P2-003 / P1 (stronger, unestablished Taylor form) | Ch. 8, chapters/ch07-walks.tex, thm:polya, Fourier cosine estimate for d >= 3 | The proof wrote cos(u)=1-u^2/2+(u^4/24)cos(xi), silently invoking the located-point remainder form. The Phase 1 audit established that Volume 1 Chapter 8 proves the Taylor integral remainder and Taylor–Lagrange bound, not the located-point theorem as a working premise. Only the absolute bound was needed. | [209db35](https://github.com/OussamaSegh/Order-and-Chance/commit/209db359a980c88cb0bb16972e0870ebd3ca57eb) uses the already-proved degree-three Taylor–Lagrange inequality, abs(cos(u)-(1-u^2/2)) <= abs(u)^4/24. Subsequent estimates and theorem statement are unchanged. Regression checks source and signed numerical values on [-2,2]. **Source fixed; independent recheck pending.** |

**Regression commits:** [55d9bbb](https://github.com/OussamaSegh/Order-and-Chance/commit/55d9bbbe527481250b0fa965f7244ec012250baa) adds exponential quantile and gcd tests; [bcb648f](https://github.com/OussamaSegh/Order-and-Chance/commit/bcb648f1d8239685af53f5dac1e30d8dc2e27e4f) adds the cosine remainder check. The existing four tests remain intact, for seven mathematical audit tests in that file. All corrections are within existing chapters; no theorem/exercise labels changed.

## 2. Reconciled prior evidence — not reopened by default

The four previously repaired Phase 1 mathematical sites remain present in the source: thm:inversion uses a growing Gaussian tail threshold that does not assume a moment; thm:lindeberg splits strictly at |X| > epsilon; prop:memoryless addresses G(1)=1 on all real times; and the 52-card riffle distances are explicitly three-decimal rounded numbers, not exact 1s. Prior Phase 1 records also corrected Taylor-proof attribution and printed prerequisite numbering. They are not listed as fresh defects here. The repaired passages still require the distinct exact-SHA mathematical review specified in PR #115. Previous chapter-model reads in volume4-chapter-issue-log.md are historical evidence, not automatic acceptance of the present branch.

## 3. Exact branch source inventory and chapter-by-chapter coverage

The following blob IDs are the chapter source versions inspected or statically enumerated on this Phase 2 branch after the repairs. **Static** means a source-level pass counting labels, local references and exercise/hint/solution IDs; it does *not* mean the proofs or exercise answers were checked. **Targeted** means only the named passages were examined mathematically; even those need independent checking after our edits.

| Printed location | Actual included source file | Blob SHA on this branch | Scope completed here | Required remaining mathematics and review |
| --- | --- | --- | --- | --- |
| 1 | ch01-counting.tex | ef5b5ac00bb5f137f4f8cb9934a41c3422984a01 | Static only; prior issue-log consulted | All statements, eight exercises/solutions, infinite-digit model, figures |
| 2 | ch02-discrete.tex | 921ea590d21af564a636dbcce53a73f7ee6cc61b | Static only | All statements, eight exercises/solutions, countable expectations and numerical examples |
| 3 | ch03-generating.tex | 10c1ebdc486ca82ec335654bbacc8cfa6ad0ae76 | Static only | All statements, eight exercises/solutions, extinction edge cases and generating functions |
| 4 | ch04-inequalities.tex | 9501619f8494005eb2c50d0d689541332ea04289 | Static only | All concentration and strong-law arguments, six exercises/solutions, numerics |
| 5 | ch05-continuous.tex plus nested ch05-geometric.tex | 4d2221df7adeb926d46c7526faa7829a77645db9; 2bc6858a1cb598473be2f233ae5ed6b05ff0e93e | Both included and statically enumerated | Full density/integral/quantile and geometric-probability proof and nine exercises/solutions; rendered figures |
| 6 | ch06-clt.tex | 049eba261d47a7d3df9237b93cbbba16365fbaec | Targeted reread of modes, fourth-moment SLLN, characteristic/inversion, Lindeberg, classical CLT and Gaussian vectors; Phase 1 fixes checked in source | Every remaining step, eight exercises/hints/solutions, distribution limits, heavy tails and figure inspection; independent referee |
| 7 | ch07-entropy.tex | 25330e7046f0b585bef9ebffb1408bc907c109df | Static only | All six exercises, entropy/coding proof and equality/quantifier cases |
| 8 | ch07-walks.tex | 8b64abc66f79ccbc792906fbfa9ba50e9ab3e890 | Targeted recurrence/Pólya/reflection/last-visit reread; thm:polya repaired | Remaining statements, eight exercises/solutions, Fourier estimates and independent recheck of corrected proof |
| 9 | ch08-markov.tex | ddfc2e52756052755a0d26437b782f104c069a3f | Targeted stationary/ergodic/coupling/top-to-random/riffle reread; thm:ergodic repaired | Full proof-by-proof and nine-exercise audit; exact-riffle precision and independent dependency recheck |
| 10 | ch09-poisson.tex | 43afe0a5a57a33bf8bd3897927ce4f6b0c9645dd | Targeted memorylessness, exponential/gap moment, Poisson counts/colouring/independent increments/thinning and queue passage; false SLLN premise repaired | Full Poisson process and eight-exercise audit, all continuous-time stopping/integrability cases, independent review |
| 11 | ch10-martingales.tex | 200c6c79d56493bde6e1433719181df94f96b66b | Targeted optional stopping, Doob, L2 and a.s. convergence proofs reread, no changes | Full line-by-line review and five exercise/solution checks, event measurability |
| 12 | ch11-brownian.tex | d058cb52409818e1948fca8ccdb2af8f17dfebf7 | Targeted dyadic construction, scaling, quadratic variation, dyadic expansion, restart/reflection and zero-set solution reread, no changes | Full construction/independence/uncountability and seven-exercise audit plus figure; independent reviewer |
| 13 | ch12-method.tex | 7bb8f4a676a46524817beb217d04f18ad6317a21 | Static theorem/exercise index only | All probabilistic method/local lemma/second-moment/crossing proofs and six exercises/solutions |
| 14 | ch14-graphs.tex | a494b82eee49bc1ed43d43b9b74894ed821706d4 | Targeted subcritical component and triangle second-moment proofs read; six exercises indexed | All six exercises/solutions (especially supercritical lower bound), graph edge cases, figure |
| Appendix B | extremal.tex | 3899f21ebcc1a05e68cd545cdb96e103d215ffad | Targeted Turán, Ramsey, Schur, sunflower, EKR, small and general van der Waerden proofs read | Verify every implication and special case; all five exercises/solutions and both figures independently |

The preface (blob eba4afa0b68e117ace3ad611ef3655a64a04f22e), About the Cover and jacket copy still need an end-to-end mathematical promise/figure/cross-volume review. Earlier historic mathematical signoffs must be matched to identical source blobs and unchanged premises before the acceptance register in PR #115 can be marked PASS. A source-side targeted reread by this PR's author is **not** that independent acceptance.

**Live static scan on the branch:** 17 included chapter/preface/Appendix TeX sources, 6,771 source lines, 291 unique labels, 314 local references all resolving, 107 distinct exercise IDs and matching 107 hint IDs and 107 solution IDs in their source order, and 41 referenced figure calls. This scan excludes bookends, cover and generated graphics. Existence and content of 41 figure sources were previously covered by Phase 1 route tests; the Phase 2 regression suite must rerun before claiming an exact-head PASS. Neither a matching ID nor a source figure call validates the mathematical answer or drawn geometry.

## 4. Downstream proof and dependency checks

* The new Chapter 10 exponential quantile sentence is supported by Chapter 5's inverse-CDF construction and Chapter 6's fourth-moment strong law, both earlier in the printed order. It does not change the proof of finite Poisson counts.
* The Chapter 9 gcd derivation is internal to thm:ergodic, before its coupling bound; the finite-chain result and all downstream citations preserve their exact labels.
* The Chapter 8 cosine bound is precisely what the higher-dimensional Fourier integral uses; no rate, asymptotic, index, label or conclusion was strengthened.
* Cross-references and exercise-number slots are mechanically checked against the printed chapter route. The full Volumes 5–15 citation audit is **not** done. Published Volumes 1–3, common publishing code and covers have not been changed.

## 5. Executable tests, exact-head native workflows and acceptance gates

Commands defined by the repository:

    python3 -m unittest discover -s tools -p test_volume4_math_audit.py
    python3 -m unittest discover -s tools -p test_volume4_route.py
    python3 -m unittest discover -s tools -p 'test_*.py'
    ./build.sh volume4-chance

PR creation triggers **Volume 4 native production QA** and the full **Build books** workflow; the former builds reading and print PDF, EPUB, online reader and publishing cover, and does not supersede protected Build books. At writing, **no local repository checkout, exact-head GitHub Actions log, final PDF, EPUB or production artifact has been obtained**. Status for all commands and native QA: **NOT YET VERIFIED**. Later reports must give the exact PR head, run URL, job results, page count and artifact digest, without implying that a historic SHA is current.

Historical provenance must be ordered by revision: early Phase 1 Build books run 42515128385 at 5bbca61229075359a358ac079c1faa1e074ff7ed passed Python tests but failed the **protected Volume 3 C-GROUP gate**. That early failure was **superseded** by the later Phase 1 exact-head run [42519081478](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42519081478) at 0847b63173bb5d180eb23525d320d8f882c62540, which **completed successfully**; the corresponding Volume 4 native run [42519081530](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42519081530) at the same SHA also **completed successfully**. Neither older pass verifies this Phase 2 branch. No CI/review protection is changed in this PR.

## 6. Remaining-work checklist (cannot close Phase 2 with this PR)

- [ ] Independently review V4-P2-001 through V4-P2-003 on their exact corrected source blobs and record reviewer, date and mathematical disposition. The three **P1 repairs are pending signoff**, not independently closed.
- [ ] Revalidate Phase 1's six recorded repairs and any historical exact-blob chapter signoffs rather than resetting prior reviews.
- [ ] Full theorem/definition/proof/example/numerical audit for every printed chapter, including unexamined passages of Chapters 6, 8–12 and 14 and the entire Chapter 13.
- [ ] Independently check **all 107 exercises, 107 hints and 107 complete solutions**, not just label matching.
- [ ] Inspect **all 41 referenced figures** and their mathematical captions against compiled PDF/EPUB, and verify no cross-volume citation depends on a theorem introduced later.
- [ ] Run and record exact-head seven-test math suite, five-test route suite, full repository suite, V4 native QA and protected full workflow. Investigate failures without bypassing checks.
- [ ] Audit published Volume 1 dependencies and Volumes 5–15 downstream references without modifying published Volumes 1–3.
- [ ] Obtain distinct referee and author approval, native all-page artifacts, real-device and KDP acceptance as applicable before any release claim.

**Current issue disposition:** no *additional* P0/P1 defect was confirmed in the targeted passages beyond the three listed, which are source-fixed but **P1 awaiting independent recheck**. This is not evidence that the unsampled majority of mathematical claims are sound. Phase 2 cannot legitimately be declared complete, accepted or ready to merge on mathematical grounds from this ledger alone.
