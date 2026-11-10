# Volume 4 Phase 3 — pedagogical and editorial audit

**Date:** 10 November 2026.
**Reviewer:** the designated validator (an AI reviewer). Not an external referee, and not a second proof audit.
**Source read:** the Phase 3 branch at `cfe5d152a8aa2bc74b7b96f5824369a86e175b92`, which differs from baseline `2655cf5ac02c0a1c510c0da13f8c6b223c4d9c5f` only in three ink words, two captions, and the tests and notes that record them.
**Method:** each printed chapter was opened at its question, its first definitions, and the bridge into the next idea. Named hazards from Phase 2 were re-read in place: the stopping-time counterexample, the riffle distances that round to 1, the Itô preview, Bertrand’s three sampling rules, the entropy arithmetic in the Chapter 7 opener, and the Volume 5 handoff. Exercise identifiers already match hints and solutions by `tools/test_volume4_route.py`. Phase 2’s proof signoffs were not reopened. This is not a physical reading by a student, and it is not a claim that every sentence was rewritten.

No critical pedagogical defect was demonstrated. No chapter source was changed for style.

## Chapter dispositions

| Chapter | Job of the chapter | Disposition |
| --- | --- | --- |
| Preface and jacket | What “still waiting” means for three tosses, and what an endless string of tails would mean. | PASS |
| 1 Games to spaces | Name the outcomes before the fraction. One uniform number carries every toss. | PASS |
| 2 Random variables | A law is the list of probabilities, not the sample space. Poisson, cycles, coupons. | PASS |
| 3 Generating functions | Attach \(p_k\) to \(s^k\), then extinction is the smaller fixed point. | PASS |
| 4 Concentration | The same 600 heads in 1000 tosses: Chebyshev gives \(1/40\), Hoeffding gives a bound near \(2\times 10^{-9}\). | PASS |
| 5 Continuous chance | Density is not probability. Bertrand’s phrase “at random” is three experiments. | PASS |
| 6 Bell curve | Dice are centred and scaled. A normal tail estimates; Hoeffding bounds. The limit is proved afterwards. | PASS |
| 7 Entropy | Surprise adds for independent symbols. A biased coin’s average surprise is about \(0.469\) bits. | PASS |
| 8 Random walks | Return on the line is not the probability of being at 0 at one time. Dimension changes the answer. | PASS |
| 9 Markov chains | The next move depends on the present stop. Riffle distances that print as \(1.000\) are not equal to 1. | PASS |
| 10 Poisson clock | A fixed arrival time does not wait half a mean gap. Memoryless gaps explain the residual wait \(1/\lambda\). | PASS |
| 11 Martingales | A clock that uses tomorrow’s sign is a random time, not a stopping time. Optional stopping needs the definition. | PASS |
| 12 Brownian motion | Dyadic normals produce a continuous path. Itô’s formula is marked as a preview for Volume 12. | PASS |
| 13 Probabilistic method | A mean below 1 forces some outcome with no monochromatic clique. | PASS |
| 14 Random graphs | Below the critical degree, components are logarithmic with high probability. The last pages name Volume 5. | PASS |
| Appendix B | Turán and Ramsey by counting. The appendix says it is lettered B and that there is no Appendix A. | PASS |

## What was checked, not merely listed

- **Preface.** Three tails have probability \(1/8\). The endless string is distinguished from a finite cylinder. Volumes 2 and 3 are described as useful for shuffles and cycles. The bold prerequisite line then says high-school mathematics and Volumes 1–3. Proof citations found in this pass point at Volume 1 (probability rules, logarithm, Taylor, Cauchy–Schwarz, the Gaussian integral). No Volume 2 or Volume 3 theorem is used as a premise in the passages read. Narrowing the bold line would change a reader-facing promise. That is an author decision; the sentence was not edited.
- **Jacket.** `blurb.tex` names the ballot theorem, Hoeffding, the central limit theorem, Pólya’s theorem on random walks, and the probabilistic method, and it says each chapter has graded exercises with complete solutions. `about-the-cover.tex` identifies Galton’s quincunx, the 1874 Royal Institution demonstration, and *Natural Inheritance* (1889), and it ties the picture to the bell-curve chapter. Those historical details were not re-checked against a library copy in this pass.
- **Chapter 1.** The uniform model on \([0,1)\) is defined before digits. Outer content is defined before “almost surely”. The text says countable additivity for every subset is not claimed. The three-label coin mistake (\(1/3\) versus \(1/4,1/2,1/4\)) is worked before the general language.
- **Chapter 2.** The opener’s \(H_{52}\approx 4.538\) matches \(\ln 52+\gamma+1/(2\cdot 52)\) to three decimals. The law of two tosses is computed before the name “law”.
- **Chapter 3.** The four tickets \(0,1,1,2\) appear before extinction. The fixed-point picture is the one already checked in the figure audit.
- **Chapter 4.** Chebyshev’s two-sided bound \(250/10000=1/40\) and the one-sided Hoeffding bound \(e^{-20}\) are distinguished in the text next to the figure. The section title still says “Chernoff and Hoeffding”; the proved inequality is Hoeffding’s, and the binomial relative-entropy bound is an exercise. That naming is historical, not a false theorem.
- **Chapter 5.** Bertrand’s theorem states three sampling rules and the three probabilities \(1/3\), \(1/2\), \(1/4\). The text says model (b) takes \(D\) uniform by the description of the experiment, not by a theorem about endpoints.
- **Chapter 6.** The opener computes the hundred-dice standard deviation \(\sqrt{3500/12}\) and the height \(\sqrt{60/7}\approx 2.93\), and it says the normal tail does not bound the dice while Hoeffding’s bound is \(e^{-2}\). That \(e^{-2}\) is \(\exp(-2\cdot 50^2/(100\cdot 5^2))\). Characteristic functions are introduced as the tool that multiplies for independent sums, and the text says the continuity theorem that would turn pointwise convergence into convergence in distribution is proved in Volume 11 and is not assumed here. There is no separate “skip this” banner. A reader can still see the dice question before the Fourier work. Adding a banner would be a style choice, not a repair of a false step.
- **Chapter 7.** For \(P(H)=1/10\), \(0.1\log_2 10+0.9\log_2(10/9)\approx 0.469\). The opener states that figure before the general sum.
- **Chapter 8.** The chance of a return at one even time is separated from the chance of ever returning, in the first page.
- **Chapter 9.** After the Bayer–Diaconis formula the text says the first four three-decimal values are rounded, and that \(d_k<1\) because the identity still has positive probability. The top-to-random story in the epigraph matches the strong stationary time later in the chapter.
- **Chapter 10.** The epigraph answers the five-minute guess: the residual wait is \(1/\lambda\), not half the mean gap. The exponential law is defined before memorylessness is characterised.
- **Chapter 11.** Definition `def:stopping` calls the future-dependent clock a random time and gives \(\{\tau\le 0\}=\{X_1=-1\}\) for the one-step fair walk. The optional-stopping theorem then assumes a stopping time bounded by a fixed \(N\).
- **Chapter 12.** Itô’s formula is labelled a preview. The text says Volume 12 constructs the integral. The reflection caption on this branch matches the inks.
- **Chapter 13.** Existence from a mean below 1 is the first paragraph, before the Erdős bound.
- **Chapter 14.** “With high probability” is defined again as probability tending to 1. The small graph \(G(4,1/8)\) has expected number of edges \(6/8\). The closing bridge names Volume 5, *Calculation*, subtitle *From Formula to Insight*, which is the title and subtitle in `common/volume-subtitles.json` and `docs/SERIES-STRUCTURE.md`.
- **Appendix B.** The letter B is explained in the first paragraph. The six-vertex count \(2\cdot 4=8\) against \(3\cdot 3=9\) is the picture and the text.

## Subjective notes, not defects

- Chapter 6’s comparison of modes is a long argument before the bell curve is proved. The definitions themselves are short. A one-line signpost at the start of “Characteristic functions” would tell a first reader that the dice bound is already the rigorous estimate and that the rest of the chapter is the limit. It was not added: it would not correct a false statement.
- The chapters do not end with a repeated “what you can now do” box. Each opener already says what question is being answered. A uniform box would be a template, which the writing rules discourage.
- The section title “Chernoff and Hoeffding” is broader than the theorem that is proved. The exercise `ex:chernoffbin` is the relative-entropy bound. Renaming the section is optional.

## Not claimed

A student did not sit and attempt the exercises without the solutions. Voice was sampled at the openers, the jacket, and the hazard passages above. It reads as a person explaining a calculation. No release-blocking chatbot phrasing was found in those passages, and the book was not rewritten for tone.
