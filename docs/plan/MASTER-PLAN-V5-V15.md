# Order and Chance: definitive master plan for Volumes 5–15

**Date.** 2026-11-10.
**Status.** Final architectural plan, awaiting the author's approval. Nothing in this plan has been applied to a manuscript.
**Scope.** Volumes 5 through 15. Volumes 1–3 are published and Volume 4 is the established foundation. This plan does not change them.

## 0. How to read this plan

### 0.1 What this document is

This is the one plan for Volumes 5–15. It decides where every chapter lives, which volume proves which theorem, what each volume may assume, and in what order the work is done. It replaces every earlier recommendation about Volumes 5–15, including the two reviews written in November 2026.

### 0.2 The canonical documents

| Document | Role | Authority |
| --- | --- | --- |
| `docs/plan/MASTER-PLAN-V5-V15.md` (this file) | Series-level decisions, curriculum map, decision register, roadmap, acceptance framework | Final for Volumes 5–15 |
| `docs/plan/book-05.md` … `docs/plan/book-15.md` | The blueprint of each volume: structure, theorems, acceptance | Final, and part of this plan |
| `docs/plan/SERIES-CONTENT-PLAN.md` | The story of the fifteen volumes | Updated to agree with this plan. Where its older wording about Volumes 5–15 could be read differently, this plan decides |
| `docs/plan/SERIES-PLAN-REVIEW-2026-11.md` | First architectural review | Historical record. Not a plan |
| `docs/plan/SERIES-V5-V15-EXECUTION-CHARTER.md` | Execution charter and acceptance gates proposed in review | Historical record. Its accepted parts are restated here |
| `common/series-catalog.json` | Titles, subtitles, parts as printed | Source of printed metadata. One part name changes when decision D-16 is applied |

A sentence about Volumes 5–15 in any other file under `docs/` that disagrees with this plan is out of date.

### 0.3 Two kinds of statement

Every statement in this plan is one of two kinds, and the difference matters.

**Approved architectural decision.** Where a chapter lives, which volume owns a theorem, what a volume may assume, what a theorem's heading must say. These are decided here. They become binding when the author approves this plan. They are listed in the decision register, section 3.

**Outstanding verification task.** Whether a proof on the page is correct and complete. This plan has verified no proof. Every theorem of Volumes 5–15 has the status NOT REVIEWED until the verification phase records otherwise. The tasks are listed per volume in the blueprints and collected in section 6.

### 0.4 What this plan is based on, and what it did not check

The plan was written from the manuscripts on the branch of 2026-11-10, read through each volume's `main.tex`, not from the older specifications.

What was done:

- Every `main.tex` of Volumes 5–15 was traversed to find the files that are actually printed, the chapter order, the part names, the numbered statements, and the files no `main.tex` reaches.
- Every sentence of the form "Volume N" in Volumes 5–15 was extracted, and the citations that point to a later volume were read one by one (195 of them).
- The statements, hypotheses and proof outlines of the theorems at the centre of the known disputes were read: the two circle-method chapters of Volume 5, the zero and explicit-formula chapters of Volume 6, the construction of \(\mathbb Q_p\) in Volume 7, the Haar chapter of Volume 8, the ideal chapters of Volumes 10 and 13, Tate's thesis and class field theory in Volume 13, the bounded-gap, Bombieri–Vinogradov and critical-line chapters of Volume 14, and the Maier and Selberg files of Volume 15.

What was not done:

- No proof was checked line by line. A proof that "reads complete" below means its steps are all written and its citations exist. It does not mean the proof is correct.
- No PDF was built. Every page count in this plan is an estimate from source lines and is marked as an estimate.
- No numerical claim, figure or notebook was re-run.

## 1. The series this plan protects

### 1.1 What does not change

- Fifteen volumes, in six series parts.
- Volumes 1–3 as published. Volume 4 as it stands.
- Every title and every subtitle of Volumes 5–15. No compelling reason to change any of them was found.
- The series question: can pure order and pure chance be told apart, and why do the primes look random yet obey laws?
- Full proofs as the rule. A statement without a proof says so in its heading.
- The author line, the edition wording, and the rule that books do not mention the repository or the notebooks.

| Vol. | Title | Subtitle | Series part |
| --- | --- | --- | --- |
| 5 | Calculation | From Formula to Insight | II. Bridges |
| 6 | Crossroads | Arithmetic Meets Analysis | II. Bridges |
| 7 | Spaces | Topology, Measure and Limits | III. Analysis and Geometry |
| 8 | Analysis | Operators, Spectra and Transforms | III. Analysis and Geometry |
| 9 | Shapes | The Geometry of Connection | III. Analysis and Geometry |
| 10 | Abstraction | Categories, Algebra and Homology | III. Analysis and Geometry |
| 11 | Randomness | Martingales, Limits and Ergodicity | IV. Randomness |
| 12 | Random Motion | The Geometry of Random Paths | IV. Randomness |
| 13 | Arithmetic | From Equations to Hidden Worlds | V. Number |
| 14 | The Primes | Their Hidden Rhythm | V. Number |
| 15 | Order and Chance | The Meeting of Structure and Randomness | VI. Synthesis |

### 1.2 The story in one paragraph

Volume 5 builds the instruments and ends with the functional equation of zeta. Volume 6 spends them: the primes obey laws in bulk, and one remark marks where the coin model will crack. Volumes 7–10 build what those two volumes borrowed: measure, operators, shapes, and the algebra behind them. Volumes 11–12 give chance its full theory, and Volume 12 ends by placing the eigenvalues of a random unitary matrix beside the zeros of zeta. Volume 13 opens the arithmetic that zeta belongs to. Volume 14 proves what is known about the primes up close. Volume 15 puts the theorems and the models side by side and says, statistic by statistic, which agreement is a theorem, which is a model, and which is a conjecture.

### 1.3 Five rules that govern everything below

**R1. Premises point backward.** A proof may use, as a premise, only a statement that appears earlier in the same volume or in an earlier volume. An appendix counts as part of its volume and may be a premise for any chapter of that volume and for later volumes.

**R2. Every other kind of forward mention is typed.** There are exactly four kinds of cross-volume edge.

| Type | Meaning | Allowed direction | Required wording |
| --- | --- | --- | --- |
| Premise | The proof uses it | Backward only | A citation by label |
| Admitted, discharged later | A fact used now and proved in a named later theorem | Forward, to one named theorem | "Admitted here, proved in Volume N, Theorem X" at the point of use, and an entry in the ledger |
| Preview | A pointer to where a story continues | Forward | No proof may depend on it |
| Quoted | A theorem of the literature the series does not prove | None | "Quoted" in the heading, with a source |

**R3. One home per theorem.** Each theorem is proved in one place and cited from everywhere else. A second proof is allowed only when the method is different and the text says "second proof" and names the first.

**R4. A heading tells the truth about the proof.** Proved, proved under a named hypothesis, sketch, admitted, or quoted. A numerical record of the literature is a remark with a source, never a theorem of the book.

**R5. Pages are measured.** A page budget is a number of printed 7×10 pages read from a built PDF. A number computed from source lines is an estimate and is always labelled so.

## 2. What the two earlier reviews got right, and what they missed

### 2.1 Agreement

Both reviews agree, and this plan confirms from the manuscripts, that:

- the specifications `book-05.md` to `book-15.md` no longer describe the manuscripts;
- Volume 8 carries too much, and its random-matrix chapters use theorems of Volumes 9 and 11;
- Volume 5 contains two chapters that use Volume 6;
- Volume 13 proves unique factorisation of ideals more than once;
- Volume 14 states the bound 600 for prime gaps without the data that would prove it;
- Volume 15's printed core is the fourteen chapters reached from `main.tex`, and the unreached files are not part of the book.

### 2.2 Disagreement, and the ruling

| Question | First review | Execution charter | Ruling |
| --- | --- | --- | --- |
| Hardy–Ramanujan in Volume 5 | Keep, repair the dependence | Prefer to move it out | Keep in Volume 5, moved to Part III, with the transformation of \(\eta\) proved there (D-10) |
| Waring in Volume 5 | Keep or move, undecided | Prefer to move it out | Move to Volume 14 (D-11) |
| Haar measure and Fourier analysis on \(\mathbb Q_p\) | Move to Volume 13 | Move to Volume 13 | Stay in Volume 8. The premise both reviews thought missing is already Volume 7, Theorem 2.10 (D-17) |
| The linear-algebra chapters of Volume 8 | An appendix that later text must not depend on | Not decided | Appendices that may be cited as premises, under rule R1 (D-18) |
| Page targets | "Narrative" targets | Measured pages | Measured pages (D-06) |
| Volume 6's zero chapter | Compressed, suspected sketches | Verify before judging | The chain reads complete. It is still NOT REVIEWED (D-13) |

### 2.3 What both missed

These findings come from the manuscripts and appear in neither review. Each one changes a decision.

1. **\(\mathbb Q_p\) is already built in Volume 7.** `volume7-spaces/chapters/ch02-metric.tex`, Theorem `thm:Qp`, constructs \(\mathbb Q_p\) as a completion, with \(\mathbb Z_p\) and the digit expansion. Volume 8's Haar chapter needs exactly that and wrongly says "Volume 13 constructs \(\mathbb Q_p\)". The forward dependence is a wrong sentence and one exercise, not a gap.
2. **Cross-volume citations are typed by hand.** There are about 1,400 citations of the form "Volume 5, Theorem 11.36" in Volumes 5–15, written as plain numbers. Moving one chapter silently breaks every citation behind it. Many are already wrong: Volume 7 points to "Volume 13, Chapter 2" for a chapter that is now Chapter 8, Volume 10 points to "Volume 13, Chapter 4" for the ideal chapters, Volume 5 still names a removed problem book. No move may be made before citations are label-based (D-03).
3. **Problem chapters break the prerequisite order.** Volume 7's closing chapter, "Almost every number", uses Volume 11, Chapter 10 (the Gauss map and Birkhoff's theorem) in more than twenty places as a tool for solutions.
4. **Volume 9 uses Volume 13 as a premise.** `ch09-hyperbolic.tex` takes the statement that two interior points of the fundamental domain are never equivalent from "Volume 13, Theorem 17.1".
5. **The semicircle chapter has forward premises too**, not only the unitary chapter: Stein's lemma and Gaussian concentration from Volume 11.
6. **Volume 12's chapter on log-correlated fields depends on the unitary-matrix chapter.** When the matrix chapters return to Volume 12 they must come before it. The order proposed in the first review would have created a forward reference inside Volume 12.
7. **The riffle-shuffle cutoff is already printed**, in Volume 11's shuffling chapter, with the Bayer–Diaconis theorem. It does not need to be rescued from an unreached file of Volume 15.
8. **Unique factorisation of ideals has three proofs**, not two: Volume 10 (abstract Dedekind domains), Volume 13 for quadratic fields (Hurwitz's norm argument), and Volume 13 for general number fields. Volume 10 already proves that the ring of integers of a number field is a Dedekind domain.
9. **Haar measure on \(\mathbb Q_p\) is built twice**, in Volume 8 and again in Volume 13's chapter on Tate's thesis, which never uses Volume 8's.
10. **Volume 14 can prove its own explicit bounded gap.** Its Proposition `prop:mklower` gives an explicit lower bound for Maynard's constants. A complete, unconditional, explicit bound follows from material already in the chapter, and can replace the unproved 600 as the book's theorem.
11. **Waring's corollary rests on a quoted theorem.** The bound \(G(k)\le 2^k+1\) in the Waring chapter uses positivity of the singular series, which the chapter quotes. The chapter also uses Fourier inversion at a level Volume 5 has not reached.
12. **A possible circle between Volumes 11 and 15.** Volume 11's mod-\(\varphi\) chapter quotes the Selberg–Delange theorem from Volume 15, and Volume 15's proof of that theorem cites Volume 11, Chapter 11. The citation looks like a comparison, but it must be confirmed that it is not a premise.
13. **Volume 15 has stubs where its synthesis should be.** Three of its fourteen chapters are about fifty source lines each (ranks, pseudorandomness, the closing chapter). The printed core is sound, but the volume does not yet end.
14. Smaller: a file of Volume 12 (`moments.tex`) that nothing prints; duplicated "Sources" sections in four chapters of Volume 15; Volume 5 openly admits Tonelli's theorem from Volume 7, which is correct practice and should be the model for every "admitted, discharged later" edge.

## 3. Decision register

Each decision records what was considered and what is final. "Verification" names what still has to be checked. It does not reopen the decision.

### 3.1 Series-level decisions

| ID | Question | Alternatives considered | Decision and reason | Verification still owed |
| --- | --- | --- | --- | --- |
| D-01 | Do titles, subtitles or the six series parts change? | Rename Volume 8 or 12 to fit moved chapters; leave all | **No change.** Every volume delivers its subtitle once the moves below are made | None |
| D-02 | How many plans are there? | A third review beside the first two; one plan | **One.** This file and the eleven blueprints. The two reviews stay as history with a banner | None |
| D-03 | How are cross-volume citations written? | Keep hand-typed numbers and repair after each move; move to labels first | **Labels first.** A citation names a volume and a label, and the printed number is generated. No chapter moves before its citations are migrated. Hand-typed numbers cannot survive the moves this plan makes | The generated numbers must reproduce today's correct citations exactly |
| D-04 | What may a proof depend on? | Volumes strictly linear; free forward references with a warning | **Rules R1 and R2.** Premises backward, four typed edges, appendices count as premises | The edge ledger must be built and checked by machine |
| D-05 | May a theorem be proved twice? | Never; freely | **Rule R3.** Once, unless the second method is different and is labelled a second proof | An equivalence table before any duplicate is removed |
| D-06 | What is a page budget? | Narrative targets; measured pages | **Measured 7×10 pages** from the built PDF (R5). Estimates are labelled | A measured ledger for all eleven volumes |
| D-07 | How is a proof's status recorded? | Free prose; a fixed vocabulary | **Fixed vocabulary**: VERIFIED, CORRECTED, QUOTED, CONDITIONAL, SKETCH, BLOCKED, NOT REVIEWED. Recorded per labelled theorem in a ledger | Everything starts NOT REVIEWED |
| D-08 | Do problem chapters obey the prerequisite order? | Exempt them as "enrichment"; hold them to R1 | **They obey R1.** A solution is a proof. A problem that needs a later volume moves to that volume | Classify each problem of the three problem chapters |
| D-09 | Where do notebooks and experiments stand? | Cite them in the books; keep them outside | **Outside the books**, as now. A number printed in a book must be reproducible from a script in the repository, recorded in the ledger, and the book states the number, not the script | Each printed numerical claim traced to a script or to a source |

### 3.2 Volume decisions

| ID | Question | Alternatives considered | Decision and reason | Verification still owed |
| --- | --- | --- | --- | --- |
| D-10 | Where does the Hardy–Ramanujan asymptotic live? | (a) Volume 14, where it was. (b) Volume 6, after the modular chapter. (c) Volume 5 Part I, as now, citing Volume 6. (d) Volume 5 Part III with its own proof of the \(\eta\) transformation | **(d).** The formula is the insight of the partition generating function, which is Volume 5's subtitle. It needs only Euler's pentagonal theorem, Poisson summation, the identity theorem and the saddle point, all in Volume 5. It becomes Chapter 12, after Asymptotics. The transformation \(\eta(-1/\tau)=\sqrt{-i\tau}\,\eta(\tau)\) is proved there from the pentagonal theorem and Poisson summation. Volume 6 then cites Volume 5 and may keep its own proof as a labelled second proof | The new \(\eta\) proof must be written and verified. The rest of the chapter must be checked to use nothing after Volume 5 |
| D-11 | Where does Waring's problem live? | (a) Volume 5 with local proofs of Weyl's inequality. (b) Volume 6 after Exponential Sums. (c) Volume 14 before Three Primes | **(c).** It needs Weyl's inequality (Volume 6), integrable Fourier inversion (Volumes 7–8), and it is the cleanest rehearsal of the circle method before the primes. Volume 14's Part II is named "Additive Problems and Bounded Gaps" and is the thinnest volume. (a) would duplicate Volume 6. (b) lacks the measure theory | Positivity of the singular series: prove it in the chapter for \(s\ge 4k\) or restate the corollary as conditional on a quoted theorem. Merge the duplicate Dirichlet approximation lemma |
| D-12 | Where does the BBP digit formula live? | Series and Products; where the manuscript has it | **Where it is**, as a section of Integration Techniques | None |
| D-13 | Does Volume 6 change shape? | Add a fourth part; add proofs suspected missing; leave | **Twelve chapters, three parts, no new topic.** Its theorem on \(\eta\) cites Volume 5. The identity for Chebyshev's bias that needs the functional equation of \(L(s,\chi)\) is labelled "admitted, proved in Volume 13". The fundamental-domain theorem gains its second half (D-20) | Line-by-line check of the prime number theorem, Hadamard, Riemann–von Mangoldt, the zero-free region, the explicit formula, Erdős–Kac |
| D-14 | Which volume constructs \(\mathbb Q_p\)? | Volume 2 (old plan); Volume 13; Volume 7 | **Volume 7, Theorem `thm:Qp`**, as the model example of a completion. It gains one corollary: \(\mathbb Z_p\) is compact. Volume 13 owns the arithmetic of \(\mathbb Q_p\) (Hensel, squares, extensions) | Fix the stale pointers in that section |
| D-15 | What happens to Volume 7's problems that use ergodic theory? | Keep with a "tool from Volume 11" label; prove the tools locally; move them | **Move them to Volume 11**, where the Gauss map is. Volume 7's chapter keeps Dirichlet, Liouville and Khinchin, which use only Volume 7 and Borel–Cantelli | Classify the 22 problems |
| D-16 | Where do the semicircle and the unitary ensemble live? | Volume 8 Spectral Theory, as now; Volume 12; split between them | **Volume 12**, both chapters. They need Volumes 9 and 11, which come after Volume 8, and Volume 12's log-correlated chapter needs them. Volume 12's third part is again "Networks and Random Matrices". The graph spectra stay in Volume 8: they need nothing later | After the move, every citation of the sine kernel and of Keating–Snaith in Volumes 9, 14 and 15 points to Volume 12 |
| D-17 | Where do Haar measure and Fourier analysis on \(\mathbb Q_p\) live? | Volume 13 (both reviews); Volume 8 | **Volume 8.** The chapter is Pontryagin duality with three examples, and \(\mathbb Q_p\) is the third. Its only prerequisite is Volume 7, Theorem `thm:Qp`. Moving it would strip Volume 8's duality chapter of its best example and make Volume 13 longer. The wrong sentence is corrected and the one exercise that needs the squares of \(\mathbb Q_p\) moves to Volume 13 | The chapter must be re-read against Volume 7's statement only |
| D-18 | How is Volume 8 organised? | One part of seventeen chapters, as now; remove the linear algebra from the edition; a main path with appendices | **A main path of sixteen chapters and six appendices.** Part II runs: finite-dimensional spectral theorem, singular values, the three graph chapters, operators, the compact spectral theorem. The other six linear-algebra chapters become Appendices A–F, citable as premises. This matches Volume 9 and the series rule that supporting mathematics stays in the appendices of the owning volume | Confirm by citation closure that no main chapter needs an appendix result that is stated after it is used |
| D-19 | Is Volume 8 too long? | Cut the linear algebra; split the volume; accept | **Accept the length, fix the path.** The problem was a reader's path of twenty-five chapters. With the matrices gone and the appendices set apart the main path is about the length of its neighbours. No theorem is cut for length alone | Measured pages |
| D-20 | Who owns the fundamental domain of the modular group? | Volume 13 (as cited now); Volume 9 proves it; Volume 6 | **Volume 6, Chapter 12**, which already proves that every orbit meets the domain. It gains the second half: interior points are inequivalent, and the boundary is glued by \(T\) and \(S\). Volumes 9 and 13 cite it | Write and verify about half a page |
| D-21 | Who owns Bézout's theorem and the group law on a cubic? | Volume 9's appendices; Volume 13 | **Volume 13.** Volume 9's appendices keep the pictures and the special cases they prove, each headed with what is and is not proved | Volume 9's cubic appendix must not use the group law for all triples |
| D-22 | Who owns unique factorisation of ideals? | Each of three places; Volume 13 alone; Volume 10 | **Volume 10** owns the general theorem and the fact that a ring of integers is Dedekind. Volume 13's general chapter deduces the number-field statement in a few lines and drops its own long proof. The quadratic chapter keeps Hurwitz's norm proof as a labelled second proof: it is elementary, explicit, and a different method | Equivalence table of the three statements before anything is deleted |
| D-23 | Who owns Haar measure on \(\mathbb Q_p\), its self-duality and its Fourier inversion? | Volume 13 rebuilds them; Volume 8 | **Volume 8** (see D-17). Volume 13's chapter on Tate's thesis cites them and removes its duplicate construction, unless the comparison shows a different normalisation, in which case one normalising lemma stays | Compare normalisations of measure and character in the two volumes |
| D-24 | What is the shape of Volume 13? | Merge the two quadratic chapters; cut them; keep | **Seventeen chapters.** The two quadratic chapters stay as the worked case that opens the volume. "Polynomial Fermat and three cubes" becomes the closing section of the cyclotomic chapter, with its heuristic labelled. Goppa codes become an exercise. Chapter numbers 1–18 are unchanged, which protects existing citations | None beyond D-22 and D-23 |
| D-25 | Which results of Volume 13 are not proved? | — | **Fixed list**, each named in its heading: Artin reciprocity, the existence theorem, the Hilbert class field (admitted); the functional equation of \(\zeta_K\) for a general field (sketch); Chebotarev in natural density (not proved; Dirichlet density is proved); Weil's bound for a general curve, modularity, Mazur's theorem, Sato–Tate (quoted) | Mordell's theorem: confirm which half of the proof is given in general and say so in the heading |
| D-26 | Where does the shuffling chapter sit in Volume 11? | After the problem chapter, as now; before it | **Before it.** Shuffling Cards is Chapter 13. The problem chapter "Sums of random pieces" is Chapter 14 and closes the volume, as problem chapters do elsewhere | None |
| D-27 | What does Volume 14 claim about bounded gaps? | Keep "600" with a disclaimer; print the witness data; state the book's own bound | **The book's own bound is the theorem.** A fully proved explicit constant from the chapter's own estimate, plus the proved criterion, the printed case \(k=5\), and the consequence of Elliott–Halberstam. The values 600 and 246 go into a remark headed "Records, quoted" | Compute and verify the explicit constant and its admissible tuple |
| D-28 | Which results of Volume 14 are quoted? | — | **Fixed list**: Huxley, Baker–Harman–Pintz, Guth–Maynard; Chen; Zhang; the Vinogradov mean value theorem; Weil's Kloosterman bound; Helfgott; Matomäki–Radziwiłł; Freiman in \(\mathbb Z\); Szemerédi, Kelley–Meka; Green–Tao and its three inputs; a positive proportion of zeros on the line; the approximate functional equation. Montgomery's theorem is proved under the Riemann hypothesis for \(0\le\alpha\le1-\varepsilon\) and its heading says so | Bombieri–Vinogradov audited as one chain back to Siegel's theorem |
| D-29 | What is Volume 15? | Restore the old workshop and tours; the fourteen printed chapters | **The fourteen chapters reached from `main.tex`.** The unreached files leave the volume's directory once it is confirmed that nothing unique is lost. The climax is Maier's theorem and Selberg's central limit theorem | Hypotheses of Gallagher's theorem and Maier's theorem traced to proved statements. The Selberg–Delange citation of Volume 11 confirmed not to be a premise |
| D-30 | How does the series end? | A survey of open problems; projects only; a synthesis | **A synthesis chapter.** Chapter 14 becomes "The Meeting": one ledger of every statistic the series studied, with three columns (theorem, model, conjecture) and the place where each is proved or stated, followed by the two projects. The three stub chapters are written to the same standard as the rest | New writing, then full verification |
| D-31 | Do research-level theorems belong in Volume 15? | Remove them; keep them proved; keep them stated | **Proved when the series can prove them from its own volumes** (Maier, Selberg, Bohr–Jessen, Selberg–Delange, Buchstab). **Stated with a source when it cannot** (Montgomery–Soundararajan, Bhargava–Shankar, Fyodorov–Hiary–Keating results, Lemke Oliver–Soundararajan). Never sketched as if proved | None |

## 4. Curriculum map

### 4.1 Volumes in order, with what each may assume

Premise edges only. Every edge points to an earlier volume, so the graph has no cycle.

| Vol. | Needs as premises | Central question | Climax |
| --- | --- | --- | --- |
| 5 | 1, 2, 3, 4 | When does a formula explain something? | The functional equation of \(\zeta\), and the same symmetry giving \(p(n)\) |
| 6 | 2, 3, 4, 5 | What laws do the primes obey in bulk? | The prime number theorem; the explicit formula; Erdős–Kac |
| 7 | 1 (4 as motivation) | What were limit, length and "typical" all along? | Fubini; Radon–Nikodym; Prokhorov |
| 8 | 3, 5, 6, 7 | What lives in a space of functions? | The compact spectral theorem; Wiener–Ikehara and a second proof of the prime number theorem |
| 9 | 3, 5, 6, 7, 8 | How do spaces join, and what can be measured from inside? | Gauss–Bonnet; Weyl's integration formula |
| 10 | 3, 7, 8, 9 | What is the frame common to all these structures? | Dedekind domains; Peter–Weyl and Weyl's character formula |
| 11 | 2, 4, 5, 6, 7, 8, 10 | What survives when independence or variance fails? | Donsker; Birkhoff; Furstenberg's proof of Roth's theorem |
| 12 | 4, 7, 8, 9, 10, 11 | What does a random path look like, and a random spectrum? | Itô's formula; the sine kernel |
| 13 | 2, 3, 5, 6, 7, 8, 10 | What arithmetic was hidden inside the integers? | Tate's thesis; Mordell's theorem |
| 14 | 5, 6, 8, 11, 13 | How regular are the primes up close? | Bombieri–Vinogradov; bounded gaps |
| 15 | 4–14 | Which agreements between primes and chance are theorems? | Maier's theorem; Selberg's central limit theorem |

Volume 9's need for Volume 6 is the fundamental domain (D-20). Volume 11's need for Volume 10 is the character theory of the symmetric group, used only by the shuffling chapter. Volume 14's need for Volume 11 is a single probabilistic inequality. Each blueprint lists its premises by theorem.

### 4.2 The admitted-and-discharged ledger

These are the only forward edges on which a proof relies. Each must carry the wording of rule R2 at the point of use.

| Used in | Fact | Discharged in |
| --- | --- | --- |
| Volume 4 and Volume 5, Chapter 3 | Fubini–Tonelli for non-negative measurable functions | Volume 7, Chapter 9 (Product Measures) |
| Volume 6, Chapter 7, bias identity | Functional equation of a primitive Dirichlet \(L\)-function | Volume 13, Chapter 12, `cor:dirichletFE` |
| Volume 11, Chapter 11 | The Selberg–Delange formula | Volume 15, Chapter 3, `thm:sd` |
| Volume 12, Chapter 10 | Montgomery's pair-correlation theorem, as a statement for comparison | Volume 14, Chapter 14, under the Riemann hypothesis |

The discharging proof must not use the result that admitted it. For the third row this is an open verification task (finding 12).

### 4.3 Theorem ownership

One home each. "Returns" are citations or labelled second proofs.

| Result | Home | Returns |
| --- | --- | --- |
| Pentagonal number theorem | Volume 5, Ch. 2 | Volume 5, Ch. 12 |
| Poisson summation; sign of the Gauss sum | Volume 5, Ch. 8 | Volume 8 (general groups); Volume 13 (adèles) |
| Functional equation of \(\zeta\) | Volume 5, Ch. 10 | Volume 13, Ch. 12: second proof by Tate |
| Transformation of \(\eta\) | Volume 5, Ch. 12 | Volume 6, Ch. 12: cites, optional second proof |
| Hardy–Ramanujan asymptotic | Volume 5, Ch. 12 | — |
| Prime number theorem | Volume 6, Ch. 5 (Newman) | Volume 8, Ch. 15: second proof by Wiener–Ikehara |
| Classical zero-free region; explicit formula | Volume 6, Ch. 6–7 | Volumes 14, 15 cite |
| Selberg's sieve; large sieve inequality | Volume 6, Ch. 8 | Volume 14 cites |
| Erdős–Kac | Volume 6, Ch. 9 | Volume 15, Ch. 3: second proof from the Kubilius model |
| Weyl differencing, van der Corput | Volume 6, Ch. 11 | Volume 14, Ch. 5–6 cite |
| Fundamental domain of \(SL_2(\mathbb Z)\), both halves | Volume 6, Ch. 12 | Volumes 9, 13 cite |
| \(\mathbb Q_p\) as a completion; \(\mathbb Z_p\) compact | Volume 7, Ch. 2 | Volumes 8, 13 cite |
| Jordan curve theorem | Volume 7, Ch. 6 | — |
| Fubini–Tonelli; change of variables | Volume 7, Ch. 9 | everywhere |
| Conditional expectation; tower property | Volume 7, Ch. 11 | Volumes 11, 12 cite |
| Prokhorov; Kolmogorov extension | Volume 7, Ch. 12 | Volumes 11, 12 cite |
| Finite-dimensional spectral theorem; Courant–Fischer; singular values | Volume 8, Ch. 3–4 | — |
| Cheeger; Alon–Boppana; Ramanujan graphs and Ihara's zeta | Volume 8, Ch. 5–7 | Volume 12 cites |
| Compact self-adjoint spectral theorem | Volume 8, Ch. 9 | Volumes 10, 11 cite |
| Plancherel; Fourier inversion on \(\mathbb R\) | Volume 8, Ch. 10 | Volumes 13, 14 cite |
| Haar measure on a compact metrizable abelian group; Haar measure, self-duality and inversion on \(\mathbb Q_p\) | Volume 8, Ch. 13 | Volume 13 cites |
| Hadamard factorisation, general form; Mellin inversion | Volume 8, Ch. 14 | Volume 15 cites |
| Riemann mapping theorem | Volume 9, Ch. 10 | — |
| Haar measure on a compact Lie group; Weyl integration; finite-\(n\) pair correlation | Volume 9, Ch. 8 | Volume 12 cites |
| Unique factorisation of ideals in a Dedekind domain; \(\mathcal O_K\) is Dedekind | Volume 10, Ch. 6 | Volume 13, Ch. 2: second proof for quadratic fields |
| Peter–Weyl; Weyl character formula for \(U(n)\) | Volume 10, Ch. 11 | Volume 12 cites |
| Lévy continuity; Lindeberg–Feller; Berry–Esseen | Volume 11, Ch. 3–4 | Volumes 12, 15 cite |
| Birkhoff; the Gauss map | Volume 11, Ch. 10 | Volume 11, Ch. 14 (problems moved from Volume 7) |
| Roth's theorem | Volume 11, Ch. 10 (Furstenberg) | Volume 14, Ch. 12: second proof by density increment |
| Transposition and riffle cutoffs | Volume 11, Ch. 13 | — |
| Semicircle law; sine kernel; Keating–Snaith moments | Volume 12, Ch. 9–10 | Volumes 14, 15 cite |
| Matrix-tree theorem | Volume 12, Appendix A | Volume 8 previews |
| Class number finiteness; unit theorem | Volume 13, Ch. 5–6 | Volume 13, Ch. 12: second proof of both by Fujisaki's lemma |
| Hasse–Minkowski | Volume 13, Ch. 10 | — |
| Tate's thesis for \(\mathbb Q\); functional equation of primitive \(L(s,\chi)\) | Volume 13, Ch. 12 | Volumes 6 (admitted), 14, 15 cite |
| Bézout; Riemann–Roch for plane curves; group law; Mordell | Volume 13, Ch. 14–15 | Volume 9 appendices preview |
| Siegel's theorem; Siegel–Walfisz | Volume 14, Ch. 2 | Volume 15 cites |
| Bombieri–Vinogradov | Volume 14, Ch. 4 | Volume 15 cites |
| Waring for \(s\ge 2^k+1\) | Volume 14, Ch. 6 | — |
| Vinogradov's three primes | Volume 14, Ch. 7 | — |
| Maynard's theorem; an explicit bounded gap | Volume 14, Ch. 9 | Volume 15 cites |
| Halász | Volume 14, Ch. 10 | Volume 15 cites |
| Montgomery's theorem under RH | Volume 14, Ch. 14 | Volumes 12 (admitted), 15 cite |
| Buchstab; Maier; Erdős–Rankin | Volume 15, Ch. 2 | — |
| Kubilius model; Selberg–Delange | Volume 15, Ch. 3 | Volume 11 (admitted) |
| Bohr–Jessen; Selberg's central limit theorem | Volume 15, Ch. 11 | Volume 8 problems preview |

Chapter numbers in this table are the numbers after the moves of this plan.

### 4.4 Difficulty and the five hard transitions

The series is not one staircase. It climbs three times: 5–6 (classical analysis to analytic number theory), 7–10 (the abstract toolbox), 11–15 (research-level probability and arithmetic). Each climb starts lower than the previous one ended. The blueprints must make that visible, because a reader who has just finished the explicit formula should not feel lost when Volume 7 begins with sets.

**6 → 7.** Volume 6 ends on a modular form and a marked crack in the coin model. Volume 7 starts again from the real numbers. The joint is debt: Volumes 4, 5 and 6 used Tonelli, integrable limits and "almost every" on trust. Volume 7's preface lists those debts and each chapter says which one it pays. Its closing problem chapter (Khinchin's theorem) returns to continued fractions from Volume 2, so the volume ends back in arithmetic.

**8 → 9.** Volume 8 ends with a second proof of the prime number theorem. Volume 9 begins with manifolds. The joint is Haar measure: Volume 8 builds it on compact abelian groups, Volume 9 builds it on Lie groups and integrates over the unitary group. The Riemann mapping theorem in Volume 9 uses the complex analysis of Volume 8, Chapter 14. With the random matrices gone, Volume 8 no longer needs anything from Volume 9.

**10 → 11.** Algebra to probability, the sharpest change of subject. Volume 11 depends on Volumes 4 and 7 far more than on Volume 10, and its preface says so: a reader may begin Volume 11 after Volume 8. The one true joint is the symmetric group: its characters in Volume 10 are exactly what the shuffling chapter of Volume 11 needs.

**12 → 13.** Volume 12 now ends with the zeros of zeta beside the eigenvalues of a random unitary matrix, and with the largest values of a characteristic polynomial. That is the right place to stop and ask what kind of object zeta is. Volume 13 answers: one of a family, each with a functional equation, which Tate proves on the adèles. Volume 13's preface makes that link in one paragraph and then begins, as it does now, with \(x^2+5y^2\).

**14 → 15.** Volume 14 proves. Volume 15 compares. The danger is that Volume 15 silently uses a theorem Volume 14 only quotes. The rule: every citation of Volume 14 in Volume 15 names the label and its status, and no proof of Volume 15 rests on a quoted theorem without saying so in its own heading. Volume 14's last theorem (Montgomery, under the Riemann hypothesis) is the first line of Volume 15's Chapter 9.

### 4.5 Notation fixed across Volumes 5–15

The notation table of `SERIES-CONTENT-PLAN.md` stays in force. These points are added because the audit found collisions.

| Symbol | Fixed meaning | Collision to remove |
| --- | --- | --- |
| \(\Lambda(n)\) | von Mangoldt | The completed zeta is \(\xi\); Legendre's modulus function in Volume 5 is renamed |
| \(\theta(x)\), \(\psi(x)\) | Chebyshev | Jacobi's theta is \(\vartheta\) |
| \(q\) | A modulus | \(q=e^{2\pi i\tau}\) is announced at first use in each chapter |
| \(\Delta\) | The modular discriminant | The modular function of a group is \(\delta\); the Vandermonde product is \(V\) |
| \(e(x)\) | \(e^{2\pi i x}\) | — |
| \(\hat f(\xi)\) | \(\int f(x)e^{-2\pi i x\xi}\,\mathrm dx\) | Any chapter using another normalisation says so in its first section; Volume 13's local transforms are compared with Volume 8's (D-23) |
| \(H_n\), \(H^n(G,M)\) | Singular homology; group cohomology | Never abbreviated to the same letter without the argument |
| "Volume N" | The only way a book names another | Never "Book", "Tome", or a removed problem book |

## 5. The eleven volumes

Each volume's full blueprint is its `book-NN.md`. This section gives the shape and the decisions that matter.

| Vol. | Shape after this plan | Structural changes | New writing | Size estimate (not measured) |
| --- | --- | --- | --- | --- |
| 5 | 3 parts, 13 chapters | Waring leaves. Hardy–Ramanujan moves to Part III | A proof of the \(\eta\) transformation, about 2 pages | 280–320 pp. |
| 6 | 3 parts, 12 chapters | None | Second half of the fundamental-domain theorem; labels | 230–260 pp. |
| 7 | 3 parts, 13 chapters | Ergodic problems leave the problem chapter | \(\mathbb Z_p\) compact; a table of debts paid | 200–230 pp. |
| 8 | 3 parts, 16 chapters, 6 appendices | Two matrix chapters leave. Part II reordered. Six chapters become appendices | Dependency lines; corrected \(\mathbb Q_p\) section | 360–400 pp., main path 250–280 |
| 9 | 3 parts, 11 chapters, 11 appendices | None | Headings that say what the appendices prove | 310–340 pp. |
| 10 | 3 parts, 11 chapters | None | Citations from Volume 13 arrive | 140–160 pp. |
| 11 | 3 parts, 14 chapters | Shuffling before the problem chapter. Receives problems from Volume 7 | Labels | 230–260 pp. |
| 12 | 3 parts, 11 chapters, 1 appendix | Receives two matrix chapters. Log-correlated chapter moves to the end | Joins between the returned chapters and their neighbours | 180–210 pp. |
| 13 | 4 parts, 17 chapters | One short chapter folded. Two duplicate constructions replaced by citations | Honest headings | 320–350 pp. |
| 14 | 3 parts, 14 chapters | Receives Waring | Explicit bounded-gap theorem; singular series | 160–200 pp. |
| 15 | 5 parts, 14 chapters | Unreached files removed | Three chapters and the synthesis | 200–250 pp. |

### Volume 5 — Calculation

The instruments, each taken from a formula to what it means. Part III now has a real climax: the functional equation of \(\zeta\) in Chapter 10, the saddle point in Chapter 11, and in Chapter 12 the same Poisson symmetry turning the partition generating function into Hardy and Ramanujan's asymptotic. The volume cites nothing after itself except the admitted Tonelli theorem. Risks: the new proof of the \(\eta\) transformation; the renumbering of Chapters 4–13, which every later volume cites. Blueprint: [book-05.md](book-05.md).

### Volume 6 — Crossroads

Unchanged in shape. It is the first summit and the most cited volume, so its numbering is frozen. Its flagship chain (no zero on the line, Newman's theorem, Hadamard, the zero count, the zero-free region, the explicit formula) reads complete and is the first thing to verify. Blueprint: [book-06.md](book-06.md).

### Volume 7 — Spaces

Unchanged in shape. It becomes the declared home of \(\mathbb Q_p\) as a space. Its problem chapter loses the problems that need Volume 11. Blueprint: [book-07.md](book-07.md).

### Volume 8 — Analysis

The volume with the most structural work. Main path: Banach and Hilbert spaces; spectral theory from matrices through graphs to compact operators; Fourier and Tauberian methods ending in the second proof of the prime number theorem. The six appendices are the linear algebra the main path and later volumes cite. Blueprint: [book-08.md](book-08.md).

### Volume 9 — Shapes

Unchanged in shape. It stops using Volume 13, and its appendices on plane curves and cubics say what they prove. Blueprint: [book-09.md](book-09.md).

### Volume 10 — Abstraction

Unchanged in shape. It becomes the declared home of unique factorisation of ideals. Blueprint: [book-10.md](book-10.md).

### Volume 11 — Randomness

One reorder at the end, and it receives the ergodic problems. Blueprint: [book-11.md](book-11.md).

### Volume 12 — Random Motion

Brownian motion, stochastic calculus, then "Networks and Random Matrices": walks on networks, the semicircle, the unitary ensemble and the zeros of zeta, and the largest values of a log-correlated field as the last chapter. Blueprint: [book-12.md](book-12.md).

### Volume 13 — Arithmetic

Seventeen chapters in four parts. It cites Volume 10 for ideals and Volume 8 for local harmonic analysis, and it lists what it admits. Blueprint: [book-13.md](book-13.md).

### Volume 14 — The Primes

Part II becomes a complete account of the circle method: Waring, then three primes, then gaps. The bounded-gap chapter states only what it proves. Blueprint: [book-14.md](book-14.md).

### Volume 15 — Order and Chance

The fourteen printed chapters, with the three stubs written and a closing synthesis. It ends by answering the series question as far as mathematics can: the bulk statistics of the primes are theorems that match the models; Maier's theorem shows a place where the simplest model is wrong; Selberg's theorem shows a place where chance is exactly right; the identification of zeros with a spectrum is a conjecture, and the book says so. Blueprint: [book-15.md](book-15.md).

## 6. Acceptance framework

### 6.1 Three gates, never merged into one

| Gate | Question | Who decides | Evidence |
| --- | --- | --- | --- |
| A. Structural validation | Is the volume built the way this plan says, with no broken or forward premise? | Machines | The automated checks of section 6.3 pass |
| B. Mathematical verification | Is each proof correct and complete from its stated premises? | An independent reviewer, never the writer of the chapter | A verification record per theorem |
| C. Editorial acceptance | Is the volume ready for a reader and for print? | The author | The editorial checklist of section 6.5 |

A volume that passes gate A has not been verified. A chapter that passes gate B has not been accepted. Reports must name the gate.

### 6.2 Status vocabulary

One status per labelled theorem, proposition, lemma and corollary, kept in `docs/plan/ledgers/theorem-status.csv`.

| Status | Meaning |
| --- | --- |
| NOT REVIEWED | Default. No claim is made |
| VERIFIED | An independent reviewer checked every step from the stated premises and recorded it |
| CORRECTED | An error was found and repaired; the repair was then verified |
| CONDITIONAL | Proved under a hypothesis named in the heading |
| SKETCH | An outline, headed as a sketch |
| QUOTED | Not proved in the series; headed as quoted, with a source |
| BLOCKED | A gap is known and not yet repaired. The volume cannot pass gate B |

Six things are never to be confused in a report: a file exists; a file is printed; a statement is cited correctly; a proof reads complete; a proof is verified; a chapter is accepted.

### 6.3 Gate A: automated checks

All of these are scripts in `tools/` run by the test suite. Those marked "new" are deliverables of Phase 0.

| Check | Passes when | Status |
| --- | --- | --- |
| Print closure | Every `.tex` file in a volume's `chapters/` is reached from `main.tex` or is listed in an explicit exclusion file | new |
| Cross-volume references | Every citation of another volume is label-based and resolves; no hand-typed "Volume N, Theorem x.y" outside the baseline list, and the baseline list only shrinks | new |
| Dependency order | No premise edge points forward; every admitted edge names a discharging theorem that exists | new |
| Heading honesty | Every theorem whose ledger status is QUOTED, SKETCH or CONDITIONAL has the matching word in its optional heading | new |
| Proof presence | Every theorem-like statement not marked QUOTED or SKETCH is followed by a proof or cites one by label | new |
| Structure | Chapter order and part names in `main.tex` equal the blueprint's table | new |
| Banned wording | No "Book N", "Tome", "Problem Book", notebook or repository mention in a book | extends `tools/check_edition_copy.py` |
| Layout and outputs | Existing layout, EPUB, cover and print checks | existing |
| Page ledger | Measured pages recorded per volume; a change of more than 5% needs a line in the PR | new |

### 6.4 Gate B: the verification record

For each flagship theorem named in a blueprint, and then for every other theorem, the reviewer files a record with nine parts:

1. the statement, with every hypothesis;
2. the list of premises, each by volume and label, each earlier in the order;
3. confirmation that each premise says what the proof needs, with matching hypotheses;
4. every step checked, with any gap written out;
5. boundary and degenerate cases;
6. every constant and every numerical value recomputed;
7. a comparison with one standard source, cited;
8. the status assigned;
9. for CORRECTED, the diff and a second reader.

The reviewer works from the built PDF and the source, and is not the writer. A proof may be marked VERIFIED only through such a record.

### 6.5 Gate C: the ten quality standards

| Area | Standard |
| --- | --- |
| Mathematical correctness | Every flagship theorem VERIFIED or CORRECTED. No BLOCKED item. Every other theorem at least checked for statement and premises |
| Prerequisite closure | Gate A passes. The blueprint's list of premises equals the ledger's |
| Exercises | Each chapter has exercises at three levels, at least one that asks for a proof and one that asks for a computation; every solution obeys rule R1; no exercise is the only proof of a result used later |
| Pedagogy | Each chapter opens with a question, shows an example before the general statement, and ends by saying what was proved and what comes next |
| Notation | The series table and section 4.5 hold. A local exception is announced where it starts |
| History and bibliography | Every date, quotation and attribution has a source in the chapter's "Sources" section. One "Sources" section per chapter |
| Computational reproducibility | Every printed number that is not proved on the page is traced to a script in the repository or to a cited source, and recorded in `docs/plan/ledgers/numerical-claims.csv` |
| Figures | Each figure is produced from source in the repository, is legible in grey at 7×10, and is referred to in the text |
| PDF, EPUB, print | The existing production checks pass for all three formats |
| Editorial readiness | The voice pass of `docs/WRITING-STYLE.md` is done; the blurb and preface claim nothing the volume does not prove |

### 6.6 Definition of done

**A volume is done** when: its structure equals its blueprint; gate A passes; every flagship theorem of its blueprint is VERIFIED, CORRECTED, CONDITIONAL or QUOTED with a matching heading, and none is BLOCKED or NOT REVIEWED; the ten standards hold; the three formats build; the author has accepted it.

**The series is done** when: all fifteen volumes are done; the dependency ledger for the whole series has no forward premise; every admitted fact is discharged by a VERIFIED theorem; the ownership table of section 4.3 matches the manuscripts; Volume 15's closing ledger agrees, line by line, with the status ledger.

## 7. Implementation roadmap

Work is done in narrow pull requests. One structural move per PR. One chapter per PR for mathematical or editorial work, with an independent review before merge, as `docs/plan/PROGRESS.md` already requires. A PR that moves a chapter changes no mathematics, and a PR that changes mathematics moves nothing.

### Phase 0. Baseline and tools (first; blocks every move)

No printed page changes in this phase.

| PR | Files | Task | Done when |
| --- | --- | --- | --- |
| 0.1 | `tools/print_closure.py`, `tools/test_print_closure.py`, `docs/plan/ledgers/print-closure.json` | Record which files each `main.tex` reaches. List unreached files as explicit exclusions | Test passes; the ledger matches the inventories in the blueprints |
| 0.2 | `common/` (one macro file), `tools/xvol_labels.py`, `tools/check_cross_volume_refs.py`, tests | A macro that prints "Volume N, Theorem x.y" from a volume number and a label, fed by label tables exported from each volume's build. A checker with a baseline of today's hand-typed citations | Building any volume resolves every migrated citation; the checker fails on a new hand-typed citation |
| 0.3–0.13 | One PR per volume, 5 to 15: chapter files only | Replace hand-typed cross-volume citations with the macro. Citations that are already wrong are listed, not guessed | The PDF text of the volume is unchanged except for the listed corrections |
| 0.14 | `docs/plan/ledgers/dependency-edges.csv`, `tools/check_dependency_dag.py` | The typed edge ledger of rule R2, generated from the migrated citations and then classified by hand | Checker runs. Known forward premises are listed as failures to be cleared by Phase 1 |
| 0.15 | `docs/plan/ledgers/pages.csv`, `tools/page_ledger.py` | Measured pages for Volumes 5–15 | One row per volume and per chapter |
| 0.16 | `docs/plan/ledgers/theorem-status.csv`, `tools/check_heading_honesty.py` | One row per labelled statement, all NOT REVIEWED, with QUOTED, SKETCH and CONDITIONAL filled from the lists in this plan | Checker runs |

PRs 0.3–0.13 are independent of each other and can run in parallel after 0.2.

### Phase 1. Structural moves (after Phase 0; order matters where a volume is shared)

| PR | Decision | Files | Depends on | Merge condition |
| --- | --- | --- | --- | --- |
| 1.1 | D-11 | `volume5-calculation/main.tex`, `volume14-primes/main.tex`, move `waring.tex`, citations | 0.3, 0.12 | Both volumes build; gate A structure and reference checks pass; no text change inside the chapter except citations |
| 1.2 | D-10 | `volume5-calculation/main.tex` (order only) | 1.1 | Same |
| 1.3 | D-16 | `volume8-analysis/main.tex`, `volume12-random-motion/main.tex`, move `ch10-semicircle.tex` and `ch11-cue.tex`, reorder Volume 12, `common/series-catalog.json` part name, citations in Volumes 9, 12, 14, 15 | 0.6–0.13 | Same, plus generated metadata refreshed |
| 1.4 | D-18 | `volume8-analysis/main.tex` (order and `\appendix`) | 1.3 | Same; dependency checker shows no main-path premise on a later chapter |
| 1.5 | D-26, D-15 | `volume11-randomness/main.tex`; move the classified problems from `volume7-spaces/chapters/ch12-harder.tex` to Volume 11 | 0.5, 0.9 | Same; the list of moved problems is in the PR |
| 1.6 | D-24 | `volume13-arithmetic/main.tex`, fold `polyfermat.tex` into `ch05-cyclotomic.tex` | 0.11 | Same |
| 1.7 | D-29 | `volume15-order-and-chance/chapters/` unreached files, `volume12-random-motion/chapters/moments.tex` | 0.1 | A written check that each removed file's unique content is printed elsewhere or is listed as dropped |

1.1→1.2 are sequential. 1.3→1.4 are sequential. The five groups {1.1, 1.2}, {1.3, 1.4}, 1.5, 1.6, 1.7 are independent of each other.

After Phase 1 the chapter numbers of every volume are final. `docs/plan/volume-citation-map.md` receives one new table recording the moves.

### Phase 2. Mathematical repairs the architecture requires (after the matching Phase 1 PR)

Each is one PR, with an independent review, and each is followed by a verification record.

| PR | Decision | Task |
| --- | --- | --- |
| 2.1 | D-10 | Volume 5, Chapter 12: prove the \(\eta\) transformation from the pentagonal theorem and Poisson summation; remove the citation of Volume 6. Volume 6, Chapter 12: cite it |
| 2.2 | D-20 | Volume 6, Chapter 12: second half of the fundamental-domain theorem. Volumes 9 and 13: cite it |
| 2.3 | D-14, D-17 | Volume 7, Chapter 2: \(\mathbb Z_p\) is compact; fix pointers. Volume 8, Chapter 13: correct the section opening; move the squares exercise to Volume 13 |
| 2.4 | D-22 | Equivalence table for the three ideal-factorisation theorems; then Volume 13, Chapter 4 deduces from Volume 10; Chapter 2 heads Hurwitz's proof as a second proof |
| 2.5 | D-23 | Comparison of local measures and characters; then Volume 13, Chapter 12 cites Volume 8 |
| 2.6 | D-11 | Volume 14, Chapter 6: singular series, merged lemma, citations of Volume 6 for Weyl's inequality |
| 2.7 | D-27 | Volume 14, Chapter 9: restructure the theorem; compute and prove the explicit bound; records to a remark |
| 2.8 | D-13, D-25, D-28 | Heading corrections across Volumes 6, 13, 14 from the fixed lists |
| 2.9 | D-21 | Volume 9 appendices: headings and the cubic group law |
| 2.10 | D-29 | Volume 15, Chapter 2: hypotheses of Gallagher's and Maier's theorems made explicit. Volume 15, Chapter 3 and Volume 11, Chapter 11: confirm no circle |
| 2.11 | D-30 | Volume 15: write Chapters 8, 12 and 14, one PR each |

### Phase 3. Verification, volume by volume (gate B)

Order: 6, 5, 7, 8, 10, 9, 11, 12, 13, 14, 15. Volume 6 first because every later arithmetic volume stands on it. Volumes whose Phase 1 and 2 work is merged can be verified in parallel by different reviewers, because verification changes no numbering. Within a volume, flagship theorems first. Every correction is its own PR.

### Phase 4. Editorial acceptance (gate C)

Per volume, after gate B: exercises, notation, sources, figures, numerical claims, the voice pass, preface and blurb against the status ledger.

### Phase 5. Production

Per volume: the three formats, the cover checks, the page ledger, release. Volume 15 last, with its closing ledger checked against the status ledger.

### Priorities

1. Phase 0 entire. Nothing else is safe before it.
2. PRs 1.3 and 1.4 (Volume 8 and Volume 12): the largest structural defect.
3. PRs 1.1, 1.2, 2.1 (Volume 5): the earliest forward premise in the series.
4. Verification of Volume 6.
5. PR 2.7 and 2.10: the two places where a headline claim outruns its proof.
6. Everything else in the order above.

## 8. Risks

| Risk | Where | Guard |
| --- | --- | --- |
| A move breaks citations nobody notices | Every volume | Phase 0 before Phase 1; the reference checker |
| The new \(\eta\) proof has a branch or convergence error | Volume 5, Ch. 12 | Verification record with boundary cases; numerical check of the transformation at three points |
| A proof in Volume 6 that reads complete is not | Volume 6, Ch. 5–7 | First in the verification order |
| A main chapter of Volume 8 needs an appendix result in a way that hides a circle | Volume 8 | Dependency checker; each appendix opens with what it assumes |
| Removing Volume 13's duplicate proofs removes a hypothesis a later proof needed | Volume 13 | Equivalence tables first (PRs 2.4, 2.5) |
| The explicit bounded-gap constant is miscalculated | Volume 14, Ch. 9 | The computation is scripted and recorded; the admissible tuple is checked by machine |
| Maier's theorem depends on an unstated zero-free hypothesis | Volume 15, Ch. 2 | PR 2.10 before any other work on Volume 15 |
| Volumes 11 and 15 prove each other | Selberg–Delange | PR 2.10 |
| Volume 15's new chapters overclaim | Volume 15 | Decision D-31; every statement typed as theorem, model or conjecture |
| Page estimates are wrong | All | Rule R5; the measured ledger |

## 9. Final editorial assessment

**Retained from the original series plan.** The fifteen volumes and their titles. The series question and the building metaphor. The promise that a theorem is proved or says it is not. Hardy–Ramanujan in Volume 5 as the insight of the partition generating function. Jordan's theorem in Volume 7 and the Riemann mapping theorem in Volume 9. Shuffling in Volume 11. Volume 15 as a meeting with two climaxes, Maier and Selberg.

**Accepted from the first review.** The return of the random-matrix chapters to Volume 12 and the restored part name. The linear-algebra chapters of Volume 8 as appendices. The number 600 as a record, not a theorem. Chebotarev marked as proved in Dirichlet density only. Volume 15 frozen at its printed core. The idea of an ownership table. The observation that the specifications had drifted from the manuscripts.

**Accepted from the execution charter.** The status vocabulary. Typed dependency edges and an acyclic graph. A baseline inventory before any change. Verification records. Small pull requests with one purpose each. The rule that a file existing, a proof reading complete and a proof being verified are different facts. Measured pages.

**Rejected.** Moving Haar measure on \(\mathbb Q_p\) to Volume 13, recommended by both: the premise they thought missing is in Volume 7. Moving Hardy–Ramanujan out of Volume 5: its prerequisites are all there once one two-page proof is added. Appendices that may not be cited: it would orphan results that Volumes 9, 10 and 12 use. Narrative page targets. The presumption that Volume 6's zero chapter is a sketch. Keeping Waring in Volume 5. Restoring Volume 15's old workshop chapters.

**Decided independently.** Label-based citations as the precondition of every move. Volume 7 as the home of \(\mathbb Q_p\). Volume 10 as the home of unique factorisation of ideals, with Hurwitz's proof kept as a second proof. Volume 8 as the home of local harmonic analysis, cited by Volume 13. Volume 6 as the home of the full fundamental-domain theorem. Problem chapters held to the prerequisite order. The order of Volume 12's third part. A proved explicit bounded gap in Volume 14. Waring in Volume 14 with its singular series. A written synthesis at the end of Volume 15. The check for a circle between Volumes 11 and 15.

**The state of the series, plainly.** The architecture is sound after seven moves, none of which changes a title. The mathematics is unverified: careful in most of what was read, but no theorem of Volumes 5–15 has an independent verification record. The largest pieces of work are the citation infrastructure, the verification of Volume 6, the reshaping of Volume 8, and the ending of Volume 15.
