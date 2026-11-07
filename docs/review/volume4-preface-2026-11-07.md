# Volume 4 — preface restart and review record (7 November 2026)

**Scope:** preface only; approved four-part/fourteen-chapter plan unchanged; no editing of Chapters 1–14, other volumes, cover design or shared build rules.

**Writer / review status:** GPT-6 writer/reviewer self-check only. **Independent grok-4.7 second review NOT performed** and **NOT claimed**. The owner-approved gate stays pending until an authorised separate highest-effort grok-4.7 session reviews the *exact pushed source* (preface plus figure) and records its own issue log. Preliminary local compilation is not native/full-volume CI acceptance.

**Source milestones:** original preface blob `34c515648e9ab0e9167799bb83863286859432c5`; original ~250-word list rewritten in `1c9c8fcbe2e899e2b8c243d001bfaa5c1d68971d`; original native TikZ diagram committed in `6a1c9388994e4d066d18e3ca0a305c8499e13832`. New reading draft ~860 words. No external photograph needed for this preface; the diagram is original vector mathematics, not observational data. This record is **not** a substitute for Chapter 1 review.

## Fact-check against online academic teaching sources

Sources checked on 7 November 2026; quoted facts are elementary and independently re-derived below.

1. Durham University, *Probability 1: Axioms of probability*, https://www.maths.dur.ac.uk/users/clare.wallace/Prob1/01-axioms.html — sets, sample spaces, modelling choices, infinite fair-toss sample space, event of eventually seeing heads.
2. MIT OpenCourseWare, *Mathematics for Computer Science*, Unit 4, "Fun with Coins", https://mitocw.ups.edu.ec/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-spring-2015/probability/tp11-2/vertical-a2b75a4824b8/ — probability of n consecutive tails is 2^{-n}; probability of no heads in an infinite sequence is zero.
3. OpenStax, *Statistics*, §4.4, https://openstax.org/books/statistics/pages/4-4-geometric-distribution-optional — independent trials and the first-success waiting-time model; the displayed probability of k-1 failures then success has the needed independent-product form.
4. MIT OpenCourseWare, *Topics in Mathematics with Applications in Finance*, Lecture 14, https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/resources/18642-lecture-14-version-2_mp4/ — the description of Brownian motion as a continuous stochastic process with normal increments.
5. The detailed printed structure and claimed prerequisite boundary were checked against repository `volume1-first-principles/chapters/preface.tex`, `volume2-integers/chapters/preface.tex`, `volume3-symmetry/chapters/preface.tex`, `docs/plan/book-04.md`, `docs/plan/volume4-prerequisites.md`, `docs/WRITING-STYLE.md`, `docs/agents/mathematician-writer.md`, and `volume4-chance/main.tex` at branch pre-edit head `0ea39aff9473`. These establish editorial scope, not an independent audit that every later chapter actually honours it.

## Item-level writer checks and issue disposition

| ID | Source / anchor | Finding or test | Result | Status / follow-up |
| --- | --- | --- | --- | --- |
| PF-01 | `chapters/preface.tex`, opening | Prior preface jumped to named theorems without a solvable entry question. | Introduced the fair-coin first-head problem: n independent tails have probability (1/2)^n. Eight 3-toss strings; only TTT means still waiting; 1/8, not 1/3. Supported by Durham/MIT/OpenStax and by product rule. | Writer repair at `1c9c8fcb`; independent prose review pending. |
| PF-02 | `chapters/preface.tex`, infinite-toss question | Risk of falsely deriving probability of an infinite outcome from finite arithmetic alone. | Text poses probability-zero as a **question** and explicitly says the finite calculation does *not* define the infinite experiment. Chapter 1 supplies its binary-digit/outer-content model. The all-tails path corresponds to binary digits all zero (`u=0`) in the current `[0,1)` model, so it is not silently excluded. | Writer-reasoned, review against exact Ch1 pending. |
| PF-03 | `figures/preface-tails.tex` | Every shaded fraction must equal the probability of no head after n independent fair tosses, not a simulation or empirical histogram. | Widths out of 8 units: n=1 4/8=1/2; n=2 2/8=1/4; n=3 1/8; n=4 0.5/8=1/16. Complementary light width is 1-2^{-n}. Text caption says these are exact probabilities; image uses the series figure palette and stays vector. | Original drawing at `6a1c9388`; further native EPUB/PDF visual acceptance pending. |
| PF-04 | `chapters/preface.tex`, prerequisites | The reader must not be assumed to know university probability, general measure theory, or theorems from Volumes 5–15. | Explicitly restricts prerequisites to high-school level and Volumes 1–3; new concepts are to be built before use. All four parts and fourteen subjects match `main.tex` and approved plan. | Copy/prerequisite intent checked; **all later manuscript dependencies not thereby certified**. |
| PF-05 | `chapters/preface.tex`, end bridge | The original ending jumped to Volume 5 without returning to a first-page question. | Keeps accurate Volume 5 title/subtitle and ends with Ch1's two-coin counterexample: four outcomes HH, HT, TH, TT; "one head" has 2/4=1/2, not 1/3. | Writer recheck passed. |
| PF-06 | `chapters/preface.tex` & `figures/preface-tails.tex` | Avoid unproved numerical/statistical/biographical claims, stock AI transitions, and confusing a schematic with observed data. | No historical attribution added; no simulation described as data. Specific examples precede subject names. The mathematical claims are bounded by their stated hypotheses. | Self voice pass completed; independent voice review pending. |
| PF-07 | LaTeX integration, figure | Check syntax of new preface and diagram before triggering CI. | Both TeX sources separately compiled in a **minimal local XeLaTeX wrapper** with TikZ, xcolor and amsmath (`xelatex -halt-on-error -interaction=nonstopmode test-preface.tex`, `test-figure.tex`; exit 0). Three-page local proof-of-syntax PDF and one-page diagram were inspected; this is **not** `./build.sh volume4-chance`. | Native CI at `1c9c8fcb` and later is distinct; inspect actual workflow result. |

## Second writer pass — qualifier fix

**PF-08 (material assumption clarification).** The first draft said “eight equally likely strings” for repeated **fair** tosses before explicitly naming independence. Marginal fairness alone does not imply the joint probabilities are (1/8): for example, three perfectly correlated fair tosses yield only HHH and TTT, each with probability (1/2). The opening now states **independence** before enumerating the eight outcomes, and says that independence permits multiplying the single-toss probabilities. The final two-coin example likewise names **independent tosses**. Corrective source commit: `31141d8a9c536f33bfab0280e586446a3d986463`. The example and its counterexample were manually reconstructed and the updated standalone XeLaTeX preface again compiled with exit 0. This is a **writer self-recheck**, not a distinct second reviewer signoff.

**Current exact preface source for further checks:** `31141d8a9c536f33bfab0280e586446a3d986463` (with figure still at `6a1c9388`). Older `1c9c8fcb` is the dedicated initial rewrite commit, not the final exact source for native PDF/independent review.

## Next actions in the owner's new order

1. Verify native Volume 4 CI at the post-preface commit and inspect the actual preface pages/figure in the produced reading and print PDFs; check EPUB figure extraction at print/display resolution. CI and visual review cannot be inferred from the successful minimal wrapper.
2. Arrange the owner-specified independent grok-4.7 highest-effort **new-context** preface review at exact pushed source SHA and resolve/recheck findings. Only then advance the preface math/voice independent gate; retain separate production acceptance.
3. Move to Chapter 1 as requested by the owner, carrying forward legitimate existing repairs and issue logs. Do not restart other chapter source without reading its current exact-SHA state.
4. Keep PR #111 draft/unmerged; preserve published Volumes 1–3 and the full-books `C-GROUP` protection. Old whole-volume production/page-count and independent review blockers are still open.
