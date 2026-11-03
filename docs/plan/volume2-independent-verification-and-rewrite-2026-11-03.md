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

**Current checkpoint (3 November 2026):** baseline and both 72-result/144-exercise registers are committed. Eight named mathematical results and nine exercise solutions have two documented checks; the rewritten Ramanujan formal-series solution now has a separate adversarial symbolic pass, though expert external review remains pending. Five concrete prerequisite defects have been repaired or redesigned (including one explicit change of mathematical exercise at `pb:glaisher`). An earlier completed build revealed and prompted a correction to the KDP spine validator; an exact-final-head CI pass, entire-book mathematical audit, full-page proof and publisher checks remain open. **For exact head, latest failures, commits, status and next task, always follow the companion live review ledger and PR #103, not this summary.**
