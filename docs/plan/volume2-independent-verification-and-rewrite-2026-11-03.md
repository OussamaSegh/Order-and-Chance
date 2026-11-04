# Volume 2: independent verification and complete reader-first rewrite

**Open working plan, 3 November 2026.** Owner: current editorial PR on branch editorial/volume2-independent-proof-and-reader-rewrite-20261103. **Status: underway, not accepted.**

This is a new, stricter commission after merged PRs #89 (prose and 144 solutions), #97 (continuity and internal source audits), and #102 (new preface/back cover/KDP copy). Their work is the starting manuscript, not a certificate of correctness. This review must independently recover the arguments rather than rubber-stamp previous ledgers. The full acceptance record is this file plus docs/reviews/volume2-independent-verification-ledger-2026-11-03.md; update both after each commit. The PR body gives a short, current checkpoint; this plan is the canonical task list.

## A. Non-negotiable reader contract

1. The only previous book is Volume 1, First Principles, and the only pre-series requirement is high-school mathematics. For every imported lemma, locate its *actual* Volume 1 proof or supply a proof in Volume 2. Do not infer prerequisites from titles.
2. Nothing is **used** before being defined and justified, including notions in diagrams, captions, footnotes, worked examples, exercise questions, hints, solutions, field guide, preface and optional sections. A clearly marked teaser may ask a future question, but cannot serve as a premise.
3. **Every exercise solution, not just one-star solutions, must be executable with tools taught earlier on its offered reading route.** Merely marking a challenge “return after Volume 5/6/13” does not satisfy this requirement. For a nonlocal dependency: move/teach and prove it earlier, provide a self-contained lemma with its own proof at the exercise, or replace/relocate the problem. All solutions must remain complete.
4. Prove every result with explicit domain, quantifiers, edge cases and dependencies. Check calculations and examples twice: first a fresh symbolic reconstruction, then an independent derivation, exhaustive finite test where meaningful, or a standard published reference. Computation never substitutes for proof.
5. Teach like a good friend with a pencil: a numerical case, the need for a tool, the exact statement, the reason each nontrivial proof step follows, and a small check. Plain English; no chatbot introductions, formulaic summaries or motivational filler. Keep intellectual difficulty; remove unnecessary obstacles.
6. Content, part and chapter order, theorem coverage, exercise selection, figure selection and star grades may change when pedagogy or correctness demands it. **Record every change**, reconcile cross-references and publishing claims, and never quietly delete an unsolved obligation. The present eleven-chapter/144-key inventory is a baseline to audit, not a sacred quota.
7. Keep the approved series graphic identity and cover art untouched unless the author specifically authorizes changes. New explanatory interior TikZ plates should use docs/design/interior.md; captions must explain an actual mathematical fact.
8. Treat “independently reviewed”, “tests passed”, “all 144 proved”, “PDF inspected” and “ready to publish” as distinct, evidenced claims. Never call a phase complete on an unchecked checkbox.

## B. Working baseline and printed reading route

Current main.tex order (source stems differ from printed numbers):
- I. The Arithmetic of Integers: 1 ch01-divisibility; 2 ch02-primes; 3 ch03-congruences; 4 ch04-arithmetic-functions.
- II. Patterns in Remainders: 5 ch05-primitive-roots; 6 ch06-quadratic-reciprocity.
- III. Equations in Integers: 7 ch07-sums-of-squares; 8 ch09-diophantine; 9 ch08-continued-fractions; 10 ch10-gaussian-eisenstein.
- IV. The Hidden Structure: 11 ch14-characters; then field-guide.tex.

Source inventory from first connector read, to be rechecked by script: 16 + 11 + 21 + 13 + 15 + 17 + 8 + 8 + 8 + 8 + 19 = 144 exercise/hint/solution/writeup groups. The previous review counted 72 named proof pairs and 99 example blocks. **These are inherited counts, not fresh proof verification.**

Previous reference records: docs/plan/volume2-continuity-implementation-2026-11-03.md, docs/reviews/volume2-prerequisite-order-audit-2026-11-03.md, docs/reviews/volume2-mathematics-examples-audit-2026-11-03.md, docs/reviews/volume2-exercise-solution-audit-2026-11-03.md, review/VOLUME2-REWRITE-PASS.md. Do not overwrite them: they document an earlier standard.

## C. Phase-by-phase delivery gates

### P00 — Reproduce the exact baseline [ ]
- Record default-branch SHA, PR head SHA, and source files read; note any concurrent changes on main.
- Read AGENTS.md, docs/WRITING-STYLE.md, docs/agents/mathematician-writer.md, docs/SERIES-STRUCTURE.md, docs/design/interior.md, Volume 1 main.tex and table of contents, and Volume 2 main.tex/preface/field guide.
- Index all chapters, diagrams/captions, definitions, lemmas, propositions, theorems, proof blocks, worked examples, exercises, hint/idea/writeup and references in *printed* order; use identifiers, not counts alone.
- Run existing Volume 2 guards and test suite (or log explicitly if local execution is unavailable); capture fresh CI against exact head.
- **Exit:** reproducing inventory + named sources + known limitations entered in ledger.

### P01 — Verify the actual Volume 1 toolkit [ ]
- Trace well-ordering/strong induction, divisibility, integers, rationals/reals, Euclidean arguments, elementary proof logic, pigeonhole, binomial identities/inclusion–exclusion, finite counting/probability, series/limits/integrals actually proved there.
- Trace complex numbers, conjugation, norms, roots of unity, simple groups/cyclic groups, polynomials and root counting.
- For every proposed prerequisite, record source path and theorem/section; label “proved in Volume 1”, “high school”, “proved earlier in Volume 2” or **GAP**.
- Check that Volume 1 does not itself require a later volume for the imported proof; when in doubt, prove the tiny needed fact locally.
- **Exit:** a first-use/dependency ledger with no unverified Volume 1 claim.

### P02 — Story architecture and reader experience [ ]
- Read whole Volume 2 as one continuous argument, compare with Volume 1's last chapter and field guide; identify the exact open question inherited from Volume 1.
- For each part/chapter, write a one-sentence mathematical question, a concrete answer, and a specific reason the next chapter is needed. Decide whether to split, combine, move or shorten material.
- Resolve tensions: elementary number theory versus deep analytic digressions; Dirichlet characters introduced only after multiplicative groups; optional challenges versus prerequisites; honest statements about what has and has not been proved.
- Establish an editable story map and list any reordered chapters/sections in PR before editing. Previews cannot create theorem dependencies.
- **Exit:** approved-in-PR current story map, with every chapter's incoming and outgoing bridge.

### P03 — First-use ledger / machine-checkable dependencies [ ]
- For each technical term, notation, assertion and tool, record first use, full definition, worked example, proof, and earliest permitted invocation; include the preface, captions and problems.
- Build a directed graph of conceptual dependencies by actual reading order; treat a backward reference as valid only if the proof is already available, and an advanced return route as valid only when its required material is already taught.
- Detect undefined uses of ring, field, ideal, coset, homomorphism, prime, associate, irreducible, norm, valuation, multiplicative function, convolution, character, complex root, derivative, convergence and asymptotic notation. This list is not exhaustive.
- Add/strengthen repository regression guards for chapter order, missing/duplicate references, forward result uses, exercise keys and later-volume-as-prerequisite phrases, with documented false-positive handling.
- **Exit:** no necessary forward/missing dependency anywhere in the book, not merely its “main lane”.

### P04 — Independent proof audit: every result [ ]
For each named and unnamed proof, create one ledger row (stable identifier, exact assumptions, claim, earlier prerequisites, checker A, checker B, counterexample search, corrected line/commit, final status).
- Derive all implications from definitions, including long computations, signs and equality cases; explicitly check base cases, p=2, n=0/1, nonunits, negative integers, irrational/rational boundaries and zero denominators as applicable.
- Independently test a second route: different proof, computer enumeration, algebraic simplification, or authoritative source check. If a cited theorem is external and not proved in Volume 1, prove the precise needed version in Volume 2; citations are not permission to skip it.
- Log **BLOCKED** rather than “verified” for any step not independently justified.
- **Exit:** 100% results assigned identifiers with two substantive passes and zero unresolved BLOCKED/incorrect claims.

### P05 — Independent audit: worked examples, captions, historical facts [ ]
- Recompute every sample by hand first, then with an independent script, enumeration or alternative identity; check all plotted quantities, axes, labels, units, and figure geometry.
- Reproduce claims about famous problems, attribution and dates from trustworthy sources; remove doubtful incidental claims rather than invent references.
- Check narrative examples actually illustrate the theorem under the theorem's hypotheses, not a special case that secretly uses the conclusion.
- **Exit:** complete keyed example/figure ledger and corrected source.

### P06 — Exercise reconstruction, pass A [ ]
- Enumerate **every** exercise in printed order. For each: prompt, solution target, explicit domains, knowledge required, stars, hint, idea, full derivation, edge case, alternate check.
- Solve *without reading the provided solution* wherever feasible; compare with the answer and rewrite both if needed. Verify that the problem is true, solvable as stated, and its hint does not smuggle in missing tools.
- Regrade based on actual length/dependencies. Replace or move exercises for which no accessible proof route can be taught without breaking the book.
- **Exit:** each key has a correct standalone author-level solution and a reader-facing discovery path.

### P07 — Exercise reconstruction, pass B [ ]
- Reopen every solution using a different method or an adversarial line-by-line proof review, independent of pass A; test small/boundary cases computationally when possible.
- Require source *already taught on the chosen route* for each nontrivial input. This includes optional/challenge solutions and all formula steps, not just introductions.
- Reconcile hint/idea/writeup, verify no proof cycles, no references to unproved later material; inspect readability and formula layout.
- **Exit:** 100% of final exercise keys twice independently checked, no unresolved prerequisite or logical gap, exact key/hint/solution parity validated.

### P08 — Rigorous rewrite chapter by chapter [ ]
Process in printed order. For each chapter: read the entire chapter and relevant prior chapters; repair dependency graph; rethink the story; rewrite weak exposition; explain every proof step; update hints/solutions; add or replace interior figures; run voice pass and mechanical gates; independently re-read; record chapter-specific sign-off and head SHA in ledger. Never declare completion based on word changes alone.
- **C01 Divisibility:** what division means; well-ordering; Bézout's constructive algorithm, FTA and Gauss' lemma; subgroup vocabulary; valuation identities; Lamé bound; full back-substitution and gcd/ideal/carry exercises.
- **C02 Primes:** Euclid versus its false converse; infinitude versus density; Euler's divergence and product justification; sieve boundary, Chebyshev and Bertrand arguments; make every factorial/prime-gap extension locally supported.
- **C03 Congruences:** equivalence classes versus representatives; cancellation/nonunits; units and Euler/Wilson; CRT proof and actual reconstruction; composite/prime-power roots; eliminate dependencies on later Bernoulli theory and Fourier facts in offered exercise routes.
- **C04 Arithmetic functions:** totient, Möbius, convolution; divisor sums and inversion proof; perfect-number classification; elementary versus asymptotic arguments; check optional analytic and character-based exercises.
- **C05 Orders:** cyclicity proof (no Volume 3 shortcut), order tests and lifts; all n with primitive roots; powers of two; discrete logs; Ramanujan sums and gcd moments without deferred analytic assumptions.
- **C06 Quadratic residues:** criteria, sign conventions, Gauss/Eisenstein lemma, quadratic reciprocity and Jacobi symbol; prove the lifting and factorization claims; separately justify all probabilistic primality, field-extension and Waring challenge ingredients.
- **C07 Squares:** two-square necessity/sufficiency, four-square descent with size decrease, representation counts and circle estimate error; test three-square discussion and Zagier's involution; avoid hidden theta-series tools.
- **C08 Diophantine (source ch09):** modular obstructions vs constructions; Pythagorean parameter restrictions; Fermat descent; rational conics; Mordell/Markov/Vieta claims and termination, including negative/zero variables; check all solutions rigorously.
- **C09 Continued fractions (source ch08):** existence/uniqueness of expansion; convergent determinant, precise best-approximation quantifiers, periodic quadratics, Pell all-solutions classification and minimality.
- **C10 Gaussian/Eisenstein:** lattice rounding (including Z[sqrt(-2)]), norm-Euclidean proofs, UFD logic, splits/associates, representations, cube cases and descents; no undocumented ideal theory.
- **C11 Characters/sieve (source ch14):** characters and their existence/orthogonality from local cyclic groups, convergence and rearrangement in Euler products, finite sieve with correct boundaries, separate elementary facts from Dirichlet/analytic extensions, prove or replace theta/local-density/cubic character problem routes.
- **Field guide and preface:** recheck no unintroduced math or false claims and no unintended repetition; the field guide must be usable from what this volume actually proves.
- **Exit:** all chapter rows passed, with a real second reader's audit, source checks, and dependency release gates.

### P09 — Original illustrations and mathematical integrity [ ]
- Make a list of ideas that are opaque without a picture: Euclidean remainders, CRT recombination, cyclic-unit groups, Gauss' lattice lemma, descent, continued fractions/Pell, Gaussian/Eisenstein lattices, character detection.
- For each candidate, choose picture/number/prose by explanatory value; construct accurate TikZ using the common style and real computed coordinates; verify labels, caption, colours and line weight at print size.
- Inspect black/white/colour PDF and Kindle/EPUB scaling; do not mistake source compilation for visual validation.
- **Exit:** no misleading, decorative-only or illegible diagram; figure claims checked in ledger.

### P10 — Whole-book mathematical story and voice [ ]
- Read aloud the preface, entire prose, proofs, captions, exercise lead-ins, solution commentary, field guide and back-cover/KDP copy. Remove filler phrases, stock transitions, gratuitous cheerleading and “AI conclusions”.
- Read Volume 1's final pages immediately before Volume 2's first: the seam must not require an implicit third textbook. The ending must name Volume 3 accurately and pose a *specific* mathematical continuation.
- Run an adversarial “first-year curious reader” pass: can the reader explain why each tool was invented, where each theorem matters and exactly when a section is safely skippable?
- **Exit:** a continuous human mathematical narrative with no unexplained symbol/shift and no weak chapter bridge.

### P11 — Automated quality gates [ ]
- Run Python test discovery, Volume 2 source/key/order/dependency tests, numerical arithmetic regressions, reference and LaTeX environment checks, lint and git diff check; capture command, SHA and output.
- Add tests for every discovered error, including boundary cases; tests must fail on pre-fix source and pass after correction where reproducible.
- Keep independent *mathematical* checking separate from source-string/regex checks; report what each test really proves.
- **Exit:** all applicable tests green on exact final head with no suppressed failures.

### P12 — PDF, EPUB and website reading-quality proof [ ]
- Run complete current-head book build; check reading PDF, KDP interior, complete page-count-derived wrap, EPUB and HTML against the exact source SHA.
- Inspect **every page** of reading PDF and print PDF for maths, clipped/overfull boxes, widows, floats, grayscale contrast and facing-page readability; log actual pages reviewed, not “visual QA” without evidence.
- Check EPUB links and every exercise/hint/solution destination; inspect all figures and formulas on narrow and wide e-reader renderings including Kindle Paperwhite. Confirm content and math agree across formats.
- **Exit:** actual all-page pass + independent navigation/figure/format checks with evidence; rerun on *latest* manuscript commit after all corrections.

### P13 — Editorial sign-off and publication boundary [ ]
- Reconcile final TOC, preface, field guide, blurb, KDP metadata, ISBN, page counts, wrap spine/barcode and every documented artifact hash.
- Distinguish repository sign-off from Kindle Previewer, KDP Print Previewer, matched paperback upload, ISBN/title assignment and **physical paperback proof**. Those publisher account/physical acts require author verification.
- Request an independent mathematical/editorial reviewer for proof-heavy chapters and any external expert argument; unresolved reviews block merge.
- **Exit:** zero open proof/solution/prerequisite issues, exact-head green CI, final artifact evidence, independent review and author approval. Keep PR **draft and open** otherwise.

## D. Per-item evidence schema (mandatory)

For each theorem/proof: ID | source and printed position | exact proposition and assumptions | prior-tool proof links | independent proof A | independent check B and range/limits | defects/counterexample probes | commit SHA | reviewer/status. For each exercise: ID | stars | prompt checked | first independent solution | second independent check | hint + idea + writeup agreement | prerequisite graph | edge cases | source/commit | status. For each figure/example: ID | mathematical claim | independently recomputed data | visual sample location | status.

Use only statuses **UNREVIEWED**, **IN_PROGRESS**, **BLOCKED**, **CORRECTED_NEEDS_RECHECK**, and **VERIFIED_TWICE**. A cross-reference scan cannot set VERIFIED_TWICE; an incomplete computational sample cannot certify a theorem. Every change reopens its affected items and all dependent items for targeted regression.

## E. PR work discipline and next-chat handoff

1. First read this plan, the companion review ledger, PR description and *latest* PR comments; inspect the actual PR head and latest CI before claiming status. Prior historical “completed” flags under #97 have a different scope.
2. Work in small, reviewable commits: one focused mathematical fix or a cohesive teaching section, with its explicit proof/test/ledger update. Avoid combining unrelated chapters with one large unchecked diff.
3. In the ledger, log date, head SHA, current phase, last chapter/item actually checked, newly introduced terms, defects found, citations/evidence, corrected files, remaining issues and *the next exact task*.
4. After every batch, update the PR body checkboxes or add a timestamped progress comment linking files, commit, result and limitations. Never check a box before the required independent pass is recorded.
5. If main moved, compare heads and resolve changes rather than overwriting newer work. If a build fails or is pending, keep the precise head SHA and state; an old green run proves nothing about the new head.
6. When stopping, include a copy-pastable restart command in the last PR comment: “Read this plan and ledger; compare head with main; resume at [item IDs]; preserve outstanding blockers.” Do not close/merge until the full acceptance gate.
7. Keep original audits intact, so another agent can tell the difference between historical evidence and this new strict audit.

## F. Initial open risks, not certifications

- Prior Step 6 accepted later-volume dependencies for numerous optional exercises: Bernoulli/partition congruences, finite-field extensions, total variation, analytic prime counts, theta products, cubic characters and local densities. This new commission **does not permit that as a solution route**. Each requires local teaching/proof, a redesigned exercise, or relocation, then two checks.
- The prior 72-proof/99-example audit was a source-level editorial review, not independently formalized line-by-line mathematics. Reopen every item.
- Existing green CI and published KDP specs on PR #97 predate the newest editorial edits and this branch. No new artifact QA can be inferred from them.
- Large source files and unverified mathematical literature make “perfect” a goal, not a status. Record uncertainties; do not guess at proof steps or references.

**Current checkpoint (3 November 2026, DEP-022):** Strict internal registers now mark **11/72 named mathematical results** and **33/144 exercise solutions** `VERIFIED_TWICE` (six Chapter 1 named + five Chapter 2 named, all 15 Chapter 1 exercises and four Chapter 2 exercises). **61 named results, 111 exercise solutions, all unnamed mathematical passages, the complete first-use dependency graph, full rewrite, all figures at final size, every PDF/EPUB/print page, independent reviewer, KDP physical proof and all P00–P13 exit gates are STILL OPEN.** Work this continuation: 1) Chapter 2 `thm:cheb`: proved all real x≥1 prime product bound via printed odd induction and independent even/odd half-interval induction; verified finite pi(2n) logarithmic inequality for all n≥1 via prime exponents and separately digit carries/inductive binomial, including n=1 equality; made real floor and explicit x≥16 lower constant self-contained; new `tools/test_volume2_chebyshev_prime_bounds.py`. 2) Chapter 2 `thm:bertrand`: fully checked all 11 finite-chain primes and coverage n=1…630, large n≥631 binomial contradiction, h(512)>0 and **two separate infinite-domain positivity arguments** (printed h' and independent monotone h/n); new `tools/test_volume2_bertrand_bounds.py`. Every named Chapter 2 result is double-audited but the chapter itself is **NOT CERTIFIED**. 3) Printed Chapter 2 `ex:mod4`, `ex:mersenne`, `ex:germain`, `ex:fermatnum`: each has two independent symbolic solutions, genuine first-use scope and exact finite checks `tools/test_volume2_ch02_four_exercises.py`, with worked residue and counterexample illustrations; Fermat empty n=0 product made explicit. All mathematics and source/commit evidence in proof ledger **DEP-020, DEP-021, DEP-022**, plus named and exercise registers. Volume 1 actual-source crosswalk now cites logarithm and MVT proof sites, not unearned advanced analysis. **CI:** earlier workflows including #1577, #1585, #1591 were superseded/cancelled by newer pushes, and **NO terminal successful latest-head CI is yet asserted**. **Next:** check a completed **exact-head** Build books workflow (configuration, tests, Volume 2 PDF/EPUB/print and site); fix failures. Then continue Chapter 2 exercises `ex:gaps`, `ex:factorial` (optional Bertrand dependency already proved) and `ex:erdosdiv`, `ex:furstenberg`, before remaining chapters and all production gates. Keep PR #103 DRAFT/unmerged.


**Current checkpoint (4 November 2026, DEP-027; supersedes the DEP-022 count above):** Internal strict registers mark **19/72 named results and 58/144 exercise solutions VERIFIED_TWICE**, leaving **53 named and 86 exercises**, plus all unnumbered proof passages, complete first-use dependency graph, voice, figures, full rendered PDF/EPUB/print inspection, external reviewer, physical KDP proof and all fourteen P00–P13 release gates OPEN. Chapter 3 has eight named and all twenty-one keyed exercise mathematical Pass A/Pass B reviews, but **the chapter is not signed off** until its unnumbered arguments, teaching and visual output are checked. Reconciliation: DEP-026 was missing from the main ledger even though twelve exercises were already certified in the per-exercise register and a focused test; DEP-027 documents independent double proofs for Schur's theorem, F_p interpolation, the AKS congruence criterion, Wolstenholme, Jacobsthal (including p=2), and Kloosterman's moments via two different Fourier counts. A Chapter 3 missing math delimiter was fixed in cc95eff2; an unmatched-math regression check was committed at 52c9817. A fresh terminal **exact-final-head** Build books CI result remains mandatory; prior passing runs never certify newer commits. Next follow the permanent ledger DEP-027 handoff: exact-head CI triage, then printed Chapter 4 ex:360 and ex:muid and named prop:conv, thm:mobius, independently twice, with actual Volume 1 source locations. PR #103 remains DRAFT, unmerged and not approved for publication.


**Current checkpoint (4 November 2026, DEP-028; supersedes DEP-027 and earlier counts):** Strict internal registers mark **21/72 named results and 60/144 exercise solutions VERIFIED_TWICE**, leaving **51 named results and 84 exercises** plus all unnumbered arguments, comprehensive prerequisite/reader-narrative checks, all figures, every rendered PDF/EPUB/print page, independent review, physical KDP proof and all P00–P13 exit gates OPEN. Newly audited Chapter 4 prop:conv and thm:mobius by finite-factor/triple sums versus independent prime-exponent algebra and inclusion–exclusion; ex:360 by local formula versus divisor enumeration and inclusion–exclusion; ex:muid by multiplicativity versus independently counting squarefree subsets. Regression: tools/test_volume2_ch04_convolution_first_exercises.py, with corrected TeX single-backslash matching. Also retained DEP-026 and DEP-027 as evidence of all 21 keyed Chapter 3 exercises checked internally. **Still require terminal successful Build books on the exact final PR head**; a successful earlier run does not transfer. Next inspect Actions for current head, then review Chapter 4 ex:sigmaodd, ex:coprimesum and thm:perfect, thm:hyperbola twice each, resolving any dependencies at first use. PR stays DRAFT/unmerged/unpublished.

**Current checkpoint (4 November 2026, DEP-029; supersedes the counts above):**
**23/72 named results and 67/144 exercise solutions VERIFIED_TWICE internally**;
**49 named and 77 exercise solutions remain**. Every Chapter 4 named result and
keyed solution now has documented mathematical Pass A/Pass B, but the full
chapter is **not signed off**. Added: Euclid–Euler via divisor sums and a separate
reciprocal-divisor exhaustion; real-x hyperbola estimate via strips and disjoint
shells plus an independent all-real-x remainder bound; seven exercise solutions
by distinct parity, Möbius, residue, word-period and finite-prime counting
arguments. Repaired the unproved minimal-word-period assertion, missing explicit
Gauss cancellation, misleading square/diagonal-overlap explanation and abbreviated
infinite-product regrouping. Actual Volume 1 `prop:gamma`, `prop:safe-sums`,
`prop:signedseries` and complete `ex:basel` solution were read; the crosswalk now
records their precise usable content. New regression file
`tools/test_volume2_ch04_perfect_periods_density.py`: 12 passing tests.
Local full suite passes **296 tests with zero skips** after installing the EPUB
compression tools; 189 Volume 2 tests also pass. Ten typeset pages covering the
changed arguments were visually inspected; this is not a full-book format proof.
The full local build is tracked in DEP-029's final verification record.
Incoming-head Build books #1626 **completed successfully**
at `1718ff6524266b5404631801210d093e33cb81c6`; final edited head requires its own
terminal successful run. Comprehensive unnamed-argument/first-use/voice/figures,
every rendered page, external review, physical KDP and **all P00–P13 exits remain
OPEN**. Next: final-head CI triage, then Chapter 5 `prop:order`, `thm:cyclic`,
`lem:lift`, `thm:cyclicn`, `ex:findroots` and `ex:period`, twice each. Keep PR #103
**DRAFT, unmerged and unpublished**.

**Current checkpoint (4 November 2026, DEP-030; supersedes the counts above):** 27/72 named results and 71/144 exercise solutions have two internal mathematical passes; 45 named results and 73 solutions remain. Chapter 5 `prop:order`, `thm:cyclic`, `lem:lift`, `thm:cyclicn`, `ex:findroots`, `ex:period`, `ex:fermatfactor` and `ex:powersum` were reconstructed by two general routes. The noncyclic-modulus proof now explains its coprime-factor partition. The focused Chapter 5 regression passes three tests. All unnamed arguments, remaining Chapter 5 work, narrative/first-use/visual/external/publisher gates and P00–P13 remain open. PR #103 stays DRAFT/unmerged/unpublished; next exact items are `thm:twopower`, `cor:mod8squares`, `ex:kth`, `ex:gausswilson`.

**Current checkpoint (4 November 2026, DEP-031; supersedes prior counts):** 29/72 named results and 73/144 exercise solutions have two internal mathematical passes; 43 named and 71 solutions remain. All six named Chapter 5 results are checked internally, but its remaining exercises and unnamed arguments are open. The generalized Wilson proof now uses elementary four-element cosets, and a duplicate example was removed. The focused regression passes five tests. No chapter, format, external or P00–P13 gate is signed off. PR remains draft. Next: `ex:cyclotomic` and the short Chapter 5 exercises.

**Current checkpoint (4 November 2026, DEP-032; supersedes prior counts):** 29/72 named results and 77/144 exercise solutions have two internal passes; 43 named and 67 solutions remain. The cyclotomic exercise and three short Chapter 5 exercises have two documented reconstructions. The preface no longer suggests that advanced solutions need later volumes; the generalized Wilson hint now matches its local coset proof. Four advanced Chapter 5 keyed problems and all unnamed arguments remain. Exact-head CI, P00–P13 and external/format gates remain open; PR stays draft.

**Current checkpoint (4 November 2026, DEP-033; supersedes prior counts):** 29/72 named results and 81/144 exercise solutions have two internal mathematical passes; 43 named and 63 solutions remain. All six named Chapter 5 results and sixteen keyed solutions now have two-pass records, but its unnamed arguments, first-use graph, examples, figures and visual formats remain open. `pb:phipm1` now defines Λ at first use, proves the log-divisor identity and positivity, and gives an explicit polynomial inverse. The focused regression passes ten tests. Exact-head CI, P00–P13 and external/publisher gates remain open; PR stays draft. Next: Chapter 6 Euler criterion, Gauss lemma and early exercises.

**Current checkpoint (4 November 2026, DEP-034; supersedes prior counts):** 32/72 named results and 81/144 exercise solutions have two internal passes; 40 named and 63 solutions remain. Chapter 6 Euler criterion, Gauss lemma and the law for two now have two mathematical reconstructions and finite regression support. Chapter 6 exercises, later results and all unnamed arguments are still open, as are exact-head CI, P00–P13 and external/format gates. PR remains draft. Next: quadratic reciprocity and the first three Chapter 6 exercises.

**Current checkpoint (4 November 2026, DEP-035; supersedes prior counts):** 34/72 named results and 82/144 exercise solutions have two internal passes; 38 named and 62 solutions remain. Eisenstein’s lemma and quadratic reciprocity now have independent parity/lattice and Gauss-sum reconstructions. The optional Gauss-sum bridge was checked in all four parts against actual Volume 1 proof sites. The focused Chapter 6 regression passes four finite tests, which do not replace proof. Unnamed arguments, remaining exercises, exact-head CI, P00–P13 and external/format gates stay open. PR remains draft. Next: Jacobi proposition and first three Chapter 6 exercises.

**Current checkpoint (4 November 2026, DEP-036; supersedes prior counts):** 35/72 named results and 85/144 solutions have two internal passes; 37 named and 59 solutions remain. All six named Chapter 6 results have two-pass records, including Jacobi reciprocity; its first three exercises are now checked. The `-3` exercise teaches an independent order-three argument. Remaining Chapter 6 exercises and unnamed arguments, exact-head CI, P00–P13 and external/format gates stay open. PR stays draft. Next: Mersenne-factor, consecutive-residue and Pépin exercises.

**Current checkpoint (4 November 2026, DEP-037; supersedes prior counts):** 35/72 named results and 88/144 exercise solutions have two internal passes; 37 named and 56 solutions remain. Mersenne-factor, consecutive-residue and Pépin exercises were reconstructed twice; Pépin now explicitly establishes the base is a unit and gives an independent prime-factor contradiction. Chapter 6's remaining exercises and unnamed passages, exact-head CI, P00–P13 and external/format gates stay open. PR remains draft. Next: residue-chance, residue-11 and primitive-root-sum exercises.

**Current checkpoint (4 November 2026, DEP-038; supersedes prior counts):** 35/72 named results and 91/144 solutions have two internal passes; 37 named and 53 solutions remain. Chapter 6 residue-chance, mod-11 symbol and primitive-root-sum exercises have independent general reconstructions and finite checks. The remaining Chapter 6 advanced/Journey problems, unnamed passages, exact-head CI, P00–P13 and external/format gates stay open. PR remains draft. Next: finite-field cyclotomic factors in `pb:phimodp`.

**Current checkpoint (4 November 2026, DEP-040):** 35/72 named results and 92/144 solutions have two internal passes; 37 named and 52 solutions remain. DEP-039 revalidated the already checked finite-field exercise after shortening its irreducibility proof and did not increase totals. DEP-040 checked all parts of the Fermat-number exercise. Next: Carmichael and Pratt problems. All global review and format gates remain open; PR stays draft.

**Current checkpoint (4 November 2026, DEP-041):** 35/72 named results and 94/144 solutions have two internal passes; 37 named and 50 solutions remain. All parts of Carmichael and Pratt exercises were checked twice; the Chernick-family minimum is clarified. Next inspect existing register states for strong-liar and prime-power-square problems before auditing them. All global gates remain open; PR stays draft.

**Current checkpoint (4 November 2026, DEP-042):** 35/72 named results and 96/144 solutions have two internal passes; 37 named and 48 solutions remain. All named and keyed Chapter 6 items now have internal records. The dyadic square-density proof uses an exact recurrence. Next: printed Chapter 7; unnamed arguments, complete prerequisite/voice/figure/format and external/publisher gates remain open. PR stays draft.

**Current checkpoint (4 November 2026, DEP-043):** 38/72 named results and 98/144 solutions have two internal passes; 34 named and 46 solutions remain. Opening Chapter 7 results and first two exercises checked by independent pigeonhole/gap and Thue/descent routes. The unproved three-square dependency in `ex:eureka` remains explicitly open. Next: primitive and weighted two-square exercises. All global gates remain open; PR stays draft.

**Current checkpoint (4 November 2026, DEP-044):** 38/72 named results and 102/144 solutions have two internal passes; 34 named and 42 solutions remain. Primitive and weighted two-square exercises checked; `ex:eureka` replaced its admitted unproved theorem by the triangular/odd-square equivalence and explicit examples, as requirement3 permits. This does not certify the removed universal theorem. Next: Zagier and four-square results. All global gates remain open; PR stays draft.

**Current checkpoint (4 November 2026, DEP-045):** 40/72 named results and 104/144 solutions have two internal passes; 32 named and 40 solutions remain. All named and keyed Chapter 7 obligations are checked internally, including the redesigned triangular equivalence. The source build has passed layout/style/reading checks and is still producing formats. No chapter or global gate signed off. Next: printed Chapter 8 Diophantine equations.

**Current checkpoint (4 November 2026, DEP-046):** 42/72 named results and 107/144 solutions have two internal passes; 30 named and 37 solutions remain. Opening printed Chapter 8 results and three exercises checked by independent parameter/slope and descent routes. A surrounding imprimitive-triple example has a leg-order correction queued after the fixed-source build. Next: conic chord, Mordell and Markov results. All global gates remain open; PR stays draft.

**Current checkpoint (4 November 2026, DEP-047):** 45/72 named results and 112/144 solutions have two internal passes; 27 named and 32 solutions remain. All named and keyed printed Chapter 8 obligations are checked internally. Repaired the imprimitive-triple ordering, chord exceptions, Mordell explanations and triangle validity. Prior full build succeeded at source0a35237c; these newer source corrections require renewed validation. Next: printed Chapter 9 continued fractions. All global gates remain open; PR stays draft.

**Current checkpoint (4 November 2026, DEP-048):** 48/72 named results and 113/144 solutions have two internal passes; 24 named and 31 solutions remain. Continued-fraction recurrence, strict approximation and infinite-existence results checked by independent matrix/interval routes, plus the first exercise. A tail-floor wording repair is queued in `ex:cfunique`, which remains unreviewed. Next: best approximation and Legendre. All global gates remain open; PR stays draft.

**Current checkpoint (4 November 2026, DEP-049):** 52/72 named results and 113/144 solutions have two internal passes; 20 named and 31 solutions remain. All seven named continued-fraction results checked, including independent matrix-based Pell existence. Remaining exercises and queued tail-floor repair are open. All global gates remain open; PR stays draft.

**Current checkpoint (4 November 2026, DEP-050):** 52/72 named results and 120/144 solutions have two internal passes; 20 named and 24 solutions remain. All named and keyed continued-fraction obligations now have records. Tail-floor recovery, unreduced golden-ratio inputs and Liouville tail/minimal-polynomial steps were clarified. Next: Gaussian/Eisenstein integers. Renew full build validation for these source edits; all global gates remain open and PR stays draft.

**Current checkpoint (4 November 2026, DEP-051):** 56/72 named results and 122/144 solutions have two internal passes; 16 named and 22 solutions remain. Initial quadratic-ring units/division/UFD and failure-of-UFD results plus first two exercises checked. Defined aR+bR at first use. Next: prime classification and remaining Chapter10 mathematics. Current source edits still need renewed full build; all global gates remain open and PR stays draft.

**Current checkpoint (4 November 2026, DEP-052):** 61/72 named results and 122/144 solutions have two internal passes; 11 named and 22 solutions remain. All nine named quadratic-ring results checked, including prime classification and the closed-family cubic descent. Explained χ4 multiplicativity and corrected the descent measure. Next: six remaining Chapter10 exercises, then characters. All source/format and global gates remain open; PR stays draft.

**Current checkpoint (4 November 2026, DEP-053):** 61/72 named results and 128/144 solutions have two internal passes; 11 named and 16 solutions remain, all in the final characters/series chapter. All keyed quadratic-ring exercises checked. Clarified unit cubes, ramification terminology and local UFD references. Renew full build validation for source edits; all unnamed and global gates remain open. PR stays draft.

**Current checkpoint (4 November 2026, DEP-054):** 65/72 named results and 130/144 solutions have two internal passes; 7 named and 14 solutions remain. Character sums/count/orthogonality checked by independent explicit coordinates, plus first two exercises. Proved root-value bounds at first use, made m1 explicit and supplied the missing chi8 prime table. Next: series/products/sieve. All source/format and global gates remain open; PR stays draft.

**Current checkpoint (4 November 2026, DEP-055):** All 72/72 named results and 130/144 solutions have two internal passes; 14 solutions remain. The named-result register is complete internally, but unnamed passages and all whole-book gates stay open. Repaired strictness and ungrouped convergence in the boundary series and clarified product limits. Next: remaining Chapter11 exercises. Current source requires full test/build/visual validation; PR remains draft.

**Current checkpoint (4 November 2026, DEP-056):** All72/72 named results and136/144 solutions have two internal passes; eight advanced Chapter11 solutions remain. Elementary Möbius/sieve and character-series exercises now have two mathematical reconstructions. Supplied Phi(50,5) arithmetic, exact character-sum bound and squarefree domains. Next: pseudoprimes, Pocklington/Proth and Fermat quotients. All whole-book and external/publisher gates remain open; PR stays draft.

**Current checkpoint (4 November 2026, DEP-057):** All72/72 named results and139/144 exercises checked twice internally; five exercises remain. Pseudoprime constructions, Pocklington/Proth and all Fermat-quotient parts now have independent reconstructions. Expanded3329 certificate and clarified integer domains. Next: Mullin, Artin, Euclid game, Pascal modulo3 and powerful numbers. All unnamed and whole-book/external gates remain open; PR stays draft.

**Current checkpoint (4 November 2026, DEP-058):** All72 named results and144 exercise solutions now have two documented internal mathematical checks. This does not certify unnamed arguments or whole-book/dependency/format acceptance. Clarified game sampling, powerful-number convergence/complex definitions, Pascal proportions and Artin's −1 exception. Next: complete printed-order inventory and whole-book source/dependency/narrative/figure/history review, then exact-source build and all-page proof. P00–P13 and external/publisher gates remain open; PR stays draft.

**Current checkpoint (4 November 2026, DEP-059):** Corrected EPUB/reader run-in headings to match PDF's unnumbered design5e style. Integration regression failed before and passes after the fix for ordinary/manual/appendix numbering; all11 EPUB tests pass. Mathematical totals remain72/72 and144/144 internally. Full latest-source build/rendered review and all unnamed/whole-book/external gates remain open. Continue source inventory and chapterwise review; PR stays draft.

**Current checkpoint (4 November 2026, DEP-060):** Added repeatable complete source inventory:1366 items across15 reader-facing files,39 figure-source hashes,3 portrait hashes and resolved local reference edges, plus supporting metadata hashes. Reconciled stale current matrices; counts remain72/72 and144/144 internally. Suite376 tests passes; fb6afe06 full build has passed layout/interior/reading checks and continues. Next Chapter1 whole-source/unnamed/first-use/example/figure/history/narrative review, then printed order. No whole-book or external/publisher gate closed; PR stays draft.

**Current checkpoint (4 November 2026, DEP-061):** Whole Chapter1 source read; unnamed arguments, four retained examples and five figure datasets independently checked in new whole-book review. Defined rational valuations before use, clarified Fibonacci/growth, fixed exact diagram displacement and removed one redundant example (98 remain) plus incidental overclaims. Suite381 tests passes. Full pre-edit fb6afe06 build succeeded in all formats; all38 EPUB Why-this-works headings are unnumbered. New source still requires final build/visual review. Next Chapter2 whole-source pass; all whole-book/external/publisher gates stay open and PR stays draft.

**Current checkpoint (4 November 2026, DEP-062):** Whole Chapter2 read; nine unnamed argument groups, six examples and three complete figure datasets checked internally. Repaired false Fermat-number idea, optional prompt domains/definitions, premature1mod4 assertion and duplicate prose. Original Erdős/Furstenberg sources checked, exact portrait provenance/full history still open. Suite386 passes; inventory current. Next Chapter3 source/unnamed/first-use/four-figure review, then printed order. Current source needs final build/visual proof; all whole-book/external gates remain open and PR stays draft.

**Current checkpoint (4 November 2026, DEP-063):** Whole Chapter3 read; unnamed arguments, six examples and four complete figure datasets checked internally. Repaired modular O(p³) notation, missing Kloosterman comparison, first-use definitions and false Volume1 Carmichael attribution. Historical Sunzi23 example retained; its duplicate exercise redesigned to fresh52mod105 problem and independently revalidated twice, with all hints/solutions/tests aligned. Suite392 passes; inventory current. Next Chapter4 complete-source/unnamed/example/three-figure review. Whole-book/history/visual/external/publisher gates remain open; PR stays draft.

**Current checkpoint (4 November 2026, DEP-064):** Whole Chapter4 read; unnamed arguments, nine examples and all three figure datasets checked internally. Defined the finite probability model, clarified mu/word/domain conventions, corrected the missing irreducible-polynomial degree factor and analytic-preview hypotheses, and replaced a repeated proof workshop by new inversion data. Suite398 passes; inventory current. Chapters1–4 internal source/data work covers25 examples/15 figures; no chapter or final visual/history/external gate closed. Next fixed-snapshot build plus Chapter5 full-source review. PR stays draft/unmerged/unpublished.

**Current checkpoint (4 November 2026, DEP-065):** Whole Chapter5 read; nine unnamed argument groups, ten examples and three complete figure datasets checked internally. Repaired false persistent-root representatives and integer/modular equalities, undefined valuation at n0, first-use subgroup/parity explanations and inaccurate future/history claims. Fresh power/workshop data replace repetitions while earlier proofs remain. Suite405 passes; current inventory unchanged in count. Snapshotf59c9ac5 built all formats successfully (327 print pages,18.93MB EPUB), predating the Chapter5 edits. Through Chapters1–5:35 examples/18 figures internally checked. Next Chapter6 source pass and snapshot layout inspection; all whole-book/external/publisher gates remain open, PR draft.

**Current checkpoint (4 November 2026, DEP-066):** Whole Chapter6 read; nine unnamed argument groups, eight retained examples and four complete figure datasets internally checked. Restored349 omitted liar-plot points and matched both series for all511 odd composites<1500 by independent every-unit enumeration; new generator/freshness check and distinct markers. Explicit all-base sampling model proves4^(−k) including n9; repaired first-use/hypotheses and Bach attribution. Replaced repeated workshop and removed one duplicate example while its full earlier calculation remains (97 examples now). Suite413 passes; inventory1362 items current. New standalone plate rendered/inspected; five pages of the earlier fixed snapshot sampled, with all-page/current-source/external limits explicit. Through Chapters1–6:43 examples/22 figures internally. Next Chapter7 source pass; PR stays draft/unmerged/unpublished, all global gates open.

**Current checkpoint (4 November 2026, DEP-067):** Whole Chapter7 read; ten unnamed argument groups, six examples and three full figure datasets internally checked. Removed a withdrawn preprint as evidence for a proved circle bound; retained published Huxley2003 as a historical benchmark. Corrected factor4/mod8 discovery wording, representation-preview domain, premature uniqueness and future-proof claims. Fresh85 construction replaces a65 repeat. All three plates built/inspected; classification grid labels enlarged. Suite420 passes, inventory1362 current; through Chapters1–7:49 examples/25 figures internally. Next printed Chapter8/source ch09-diophantine review. All latest-source formats/all-page/history/external gates stay open; PR draft/unmerged/unpublished.

**Current checkpoint (4 November 2026, DEP-068):** Whole printed Chapter8/source ch09 read; eleven unnamed argument groups,15 examples and three complete figure datasets internally checked. Corrected epigraph domains, the twice-square parameter, exact circle-chart signs, preview/proof wording and a false criticism of the valid IMO hint. New7-descent replaces a repetition. Actual incircle/chord/tree/flow data recalculated; three standalone plates built/inspected, with stacked panels/larger labels. Suite427 passes; inventory1361 current. Through Chapters1–8:64 examples/28 figures internally. Next new immutable build and Chapter9/source ch08 full-source review. All final artifacts/all-page/history/external/publisher gates remain open; PR stays draft/unmerged/unpublished.

**Current checkpoint (4 November 2026, DEP-069):** Whole Chapter9/source ch08 read; nine unnamed argument groups,12 examples/four full datasets internally checked. Corrected Pell/full-ring preview, proved complete convergent search, replaced repeated workshop with fresh negative fraction, clarified domains/actual Volume1 proof references and historical dates/printout. All40 quality ordinates independently interval-certified; overlapping line labels repaired, all four plates rendered/viewed. Suite435 passes; inventory1361 current. Through Chapters1–9:76 examples/32 figures internally. Immutable681b4b55 build succeeded all formats (329 print pages,19.18MB EPUB), four pages sampled; it predates C09. Next printed Chapter10 then11/global handoffs/history/final formats/all pages. All whole-book/external/publisher gates remain open; PR draft/unmerged/unpublished.

**Current checkpoint (4 November 2026, DEP-070):** Whole Chapter10 read; seven unnamed groups, eight examples and three full datasets checked internally. Fixed the norm3 Eisenstein arrow that had unit length, checked all484 prime-disc points by independent trial factors and enlarged/reflowed the legend. New coprime-but-no-Bezout example and norm65 factor-list workshop replace repetitions while full earlier proofs remain. Clarified first-use/domains/future claims; removed outdated Gaussian-moat open status without certifying a new research result. All three plates built/viewed; suite441 passes, inventory1361 current. Through Chapters1–10:84 examples/35 figures internally. Next Chapter11 then global handoffs/history/metadata/final formats/all pages. All whole-book/external/publisher gates remain open; PR draft/unmerged/unpublished.

**Current checkpoint (4 November 2026, DEP-071):** Whole Chapter11 read; seven unnamed groups,12 examples and four full datasets checked internally. Corrected primorial divisibility, supplied local uniform logarithmic error proof, replaced repeated examples with fresh modulo8/mod6/48→49 work and clarified previews/captions. All207 cubic points separately counted and norm-checked; all four enlarged plates rendered/viewed. All11 chapters now cover96/97 examples and39/39 figure datasets internally; field guide remains. Suite449 passes, inventory1361 current. CI#1664 failed on missing mpmath; explicit test-only requirements and fresh-venv22-test reproduction repair it, terminal new-head CI remains required. Next global front/back matter, credits, first-use/story/history/reference review, final-source formats/every page and external/author gates. PR draft/unmerged/unpublished.

**Current checkpoint (4 November 2026, DEP-072):** Complete preface/field-guide/jacket/listing/cover source pass; final field-guide example checked twice. All97 examples/39 mathematical datasets now have internal records. Corrected cancellation/domain/full-ring/future-language advice, reconciled actual20 Chapter11 exercise groups. Matched/viewed three source portrait originals with local pixel/hash evidence; qualified attribution and removed unused Minkowski credit. Read primary Gardner1964 scan; cover note now identifies pale1 marker, with557 prime dots independently reconstructed and art preserved. Suite452 passes; inventory1361 current. CI#1665 list/test succeeds but books still running. Next complete global conceptual/reference/first-use/story/voice/history/bibliography, then final-source builds/all pages/CI/external/author evidence. PR draft/unmerged/unpublished; all acceptance gates open.

**Current checkpoint (4 November 2026, DEP-073):** Added explicit all-chapter/global conceptual first-use/story review and a guard for all319 references/85 manually classified forward occurrences, with context hashes/actual Volume1 toolkit drift detection and no automatic proof-status claims. Fixed first integer-unit use, main-route squarefree availability, joint-limit/indicator/Jacobi terminology, Markov preview definition, exact three-square exclusion and binary Pratt scope. Suite455 passes; final squarefree wording followed by41 focused checks and current inventory/forward guard. Next immutable all-format build plus complete global history/bibliography/current-status pass, then every-page/EPUB/reader/cover/CI/external/author gates. PR draft/unmerged/unpublished; all acceptance exits remain open.

**Current checkpoint (4 November 2026, DEP-074):** Corrected six historical/citation groups with exact source/contents evidence: Shoup Chapter3, Gray diary/title, Weil ChapterIV, Liouville chronology and unsupported completeness/priority claims. Global62-paragraph bibliography reconciliation continues. Immutablead8f7a9f completed all formats (333 print pages,0.7839-inch spine), predating these bibliography changes; all-page/current-source/external gates remain open. Next full bibliography/current-status and voice, then final artifacts/all pages/CI/independent/author evidence. PR stays draft/unmerged/unpublished.
