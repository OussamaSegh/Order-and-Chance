# Book 4 — Chance

*The Logic of Uncertainty.*

**Element.** The load of uncertainty. Chance looks like weather. It has a building code.

**On disk.** Volume 3, `tome3-chance`. Twelve chapters and two appendices. About 251 pages in the 7×10 table. The October review scored it 8. The admitted facts are labelled: Lebesgue measure on \(\mathbb R^d\), infinite products, and Fubini–Tonelli, proved in Book 7.

## Promise

A few lines of counting settle a puzzle, and the same subject climbs to the law of large numbers, the central limit theorem, Markov chains, martingales, and a first Brownian motion. The Gaussian, planted in Book 1 as an integral, becomes the law of a sum of many small independent loads. The probabilistic method shows that a load calculation can prove an object exists without building it. That idea returns in Book 14 and Book 15 as the way one talks about the primes.

## Prerequisites

Book 1: counting, series, Stirling, the Gaussian integral, inequalities. Book 3: characters of \(S_n\), for the walk on the symmetric group, and Jordan form for Markov chains. Measure theory is not a prerequisite. Two facts are admitted and labelled, and Book 7 discharges them.

## How the subtitle is delivered

The parts keep their catalog names. *The Logic of Uncertainty* is what they do.

Discrete Probability is the logic: paradoxes, axioms, random variables, generating functions, and the inequalities that turn "likely" into a proof. Limit Theorems is the uncertainty made precise, through the central limit theorem. Random Structures carries the same logic forward in time. Walks, Markov chains, Poisson processes, martingales, and Brownian motion stay in this part, because they follow the walks. The probabilistic method, and the extremal appendix, are uncertainty used as a proof. No part is renamed.

**Move.** Appendix A, Orders (`chapters/orders.tex`), is Dilworth, Sperner, and partial orders. It does not serve this title. MOVE it to Book 1, inside Algebra, Limits and Functions, beside the monotone-subsequence ideas already there. Appendix B stays in Random Structures. The broken "Theorem L.2" pointer is still repaired.

## Parts

| Part | Name | Chapters |
| --- | --- | --- |
| I | Discrete Probability | 1–4 |
| II | Limit Theorems | 5–6 |
| III | Random Structures | 7–12 and Appendix B. Appendix A moves. |

---

### Part I. Discrete Probability

#### Chapter 1. Counting and Paradoxes

**Status.** KEEP — `tome3-chance/chapters/ch01-counting.tex` (616 lines).

**Hook.** Three doors, one car. The host opens a door with a goat. Should you switch? The host's rule is part of the problem. A different rule gives \(\tfrac12\).

**Synopsis.** Probability spaces, conditioning, birthdays, Monty Hall, Bertrand's three chord models \(\tfrac13,\tfrac12,\tfrac14\), the ballot theorem, and Buffon's needle. The needle is the first integral-geometric fact. Book 9's Crofton formula is the return. Bertrand's paradox is the warning that "at random" is a measure, which is why Book 7 has to be built.

**Proved.** The ballot theorem \(\frac{a-b}{a+b}\). Buffon's probability \(\frac{2\ell}{\pi d}\) for \(\ell\le d\). The three Bertrand models, as three different measures.

**Examples.** Monty Hall under two host rules. A birthday calculation with the numbers the review recomputed.

**Figures.** Four.

#### Chapter 2. Discrete Random Variables

**Status.** KEEP — `chapters/ch02-discrete.tex` (522 lines).

**Hook.** Shuffle 52 cards and follow the cycle of 1. How many cycles do you expect?

**Synopsis.** Laws, expectation, variance, the classical families, cycles and fixed points, and the coupon collector. The expected number of cycles is the harmonic number. Book 11's Poisson–Dirichlet law is what this count becomes for the large cycles. The chapter owns the expectation.

**Proved.** Linearity, including the case of dependence. The cycle and fixed-point expectations. The coupon-collector expectation.

**Examples.** The harmonic number \(H_{52}\). A coupon-collector numerical value.

**Figures.** Three.

#### Chapter 3. Generating Functions

**Status.** KEEP — `chapters/ch03-generating.tex` (430 lines). The Kesten–Stigum remark already matches what Chapter 10 proves. Leave it.

**Hook.** Galton, in 1873, asking why aristocratic surnames were dying out.

**Synopsis.** Probability generating functions, random sums, Galton–Watson processes, and Catalan numbers. Extinction probabilities are the theorem. The generating function is the same clothesline as Book 5, used here for a law rather than a formula.

**Proved.** The extinction probability is the smallest non-negative root of \(s=f(s)\). The Catalan generating function, if the chapter derives the path count.

**Examples.** A Galton–Watson process with a named offspring law and a computed extinction probability. One Catalan path.

**Figures.** Three.

#### Chapter 4. Inequalities, Large Numbers and Entropy

**Status.** KEEP — `chapters/ch04-inequalities.tex` (780 lines).

**Hook.** Bernoulli, twenty years on the fact that the proportion of white balls settles.

**Synopsis.** Markov, Chebyshev, the weak law, Bernstein polynomials, Chernoff and Hoeffding, Borel–Cantelli, Jensen, and entropy with the asymptotic equipartition property. Borel–Cantelli is the tool Book 15's Cramér model uses for almost-sure gaps. Entropy is the tool the Crossroads Journey on Shearer may need; if that Journey uses only this chapter and Book 1, it lives at the end of Part I.

**Proved.** Chernoff and Hoeffding. Both Borel–Cantelli lemmas. The weak law under the chapter's hypotheses. Shannon's source-coding bound or the AEP, at the strength the file proves.

**Examples.** A Chernoff bound on \(\mathrm{Bin}(1000,\tfrac12)\) at 600, next to the exact tail. One Borel–Cantelli application with independent events.

**Figures.** Three.

### Part II. Limit Theorems

#### Chapter 5. Continuous Probability Done Properly

**Status.** KEEP — `chapters/ch05-continuous.tex` (727 lines). The two admitted facts stay labelled. REVISE nothing that would smuggle in a proof of Fubini.

**Hook.** A uniform number in \([0,1]\) equals \(\tfrac12\) with probability 0, and so does every other number, and yet it lands somewhere.

**Synopsis.** Why not every set is an event, random variables, the integral the chapter builds, densities, change of variables, independence, and Box–Muller. The Gaussian integral of Book 1 returns as the density of a normal law. The chapter is honest about Lebesgue measure on \(\mathbb R^d\).

**Proved.** The integral's main theorems in the setting the chapter constructs. Box–Muller. The change-of-variables formula for the maps the chapter uses.

**Examples.** Box–Muller on a pair of uniforms. A density whose improper integral is computed both as a Riemann integral and as the chapter's integral.

**Figures.** Three.

#### Chapter 6. Convergence and the Central Limit Theorem

**Status.** REVISE — `chapters/ch06-clt.tex` (575 lines). The Lindeberg limsup at the lines the review named is still the one place to expand, so both error terms are on the page. Delete or prove the sentence that Glivenko–Cantelli holds at a jump "with a little more care". The preface should say the strong law is proved for bounded variables and under a fourth-moment bound, and that the first-moment theorem is Book 11.

**Hook.** A hundred dice sum to 350 on average. What is the chance the sum exceeds 400? There are \(6^{100}\) outcomes. Nobody lists them.

**Synopsis.** Modes of convergence, the strong law in the cases proved, characteristic functions, Lindeberg's central limit theorem by swapping, the local theorem, Stirling's constant from the Poisson(\(n\)) central limit theorem, and Gaussian vectors. This is the climax of the floor. The bell curve is no longer an integral one admires. It is the shape of a sum.

**Proved.** Lindeberg's theorem for the test functions of the chapter. Stirling's constant in this probabilistic form. The strong law under the hypotheses the preface will name.

**Examples.** The hundred dice, exact value against the Gaussian approximation. One Lindeberg array that fails Lyapunov and still satisfies Lindeberg, or the converse warning if the chapter has it.

**Figures.** Three.

### Part III. Random Processes

#### Chapter 7. Random Walks

**Status.** KEEP — `chapters/ch07-walks.tex` (684 lines).

**Hook.** A drunk man finds his way home. A drunk bird may be lost forever.

**Synopsis.** The simple random walk, reflection, the arcsine law, gambler's ruin, Pólya's theorem, harmonic functions, and a walk that solves 2-SAT. Recurrence in dimensions 1 and 2, transience in dimension 3 and higher, is the theorem. Book 12 will prove the same dichotomy for Brownian motion. The citation should run forward from here and backward from there.

**Proved.** The reflection principle. Pólya's theorem. The gambler's-ruin probabilities. The arcsine law in the form the chapter states.

**Examples.** Ruin probabilities for a small capital. One arcsine numerical value.

**Figures.** Four.

#### Chapter 8. Markov Chains

**Status.** KEEP — `chapters/ch08-markov.tex` (775 lines). The sharp cutoff for random transpositions is deferred to Abstraction, and the text says so.

**Hook.** After five riffle shuffles a deck of 52 cards is far from random. After seven it is close.

**Synopsis.** Transition matrices, irreducibility, periodicity, stationary distributions, coupling, the ergodic theorem for finite chains, reversibility, and shuffling by random transpositions. The seven-shuffle story is an announcement. The Bayer–Diaconis profile is Book 15's workshop. This chapter owns convergence of a finite chain, by coupling.

**Proved.** The convergence theorem for a finite irreducible aperiodic chain. Existence and uniqueness of the stationary distribution. The cutoff is not claimed.

**Examples.** A three-state chain with stationary law \(\bigl(\tfrac4{11},\tfrac4{11},\tfrac3{11}\bigr)\). The total-variation numbers for riffle shuffles, presented as a computation, not as the profile theorem.

**Figures.** Four.

#### Chapter 9. Poisson Processes

**Status.** KEEP — `chapters/ch09-poisson.tex` (457 lines).

**Hook.** Buses arrive every ten minutes on average, at random. The expected wait is ten minutes, not five.

**Synopsis.** The exponential law, the Poisson process, thinning, superposition, the inspection paradox, Poisson approximation, and the M/M/1 queue. The inspection paradox is the first bias: a length-biased sample is not the model a naive average suggests. Book 15's Chebyshev bias is a distant cousin. A sentence is enough, or none.

**Proved.** The lack-of-memory characterisation. Thinning. The inspection paradox. M/M/1's stationary mean in the form the chapter computes.

**Examples.** The bus wait. One M/M/1 numerical mean.

**Figures.** Three.

#### Chapter 10. Conditional Expectation and Martingales

**Status.** KEEP — `chapters/ch10-martingales.tex` (787 lines). Optional stopping's three sufficient conditions, and the counter-example of the first hit of \(+1\), stay. The tower property in the generality Books 11 and 12 need is Book 7's job, once the exercise there is promoted. This chapter owns the discrete theory.

**Hook.** A monkey types capital letters at one a second. The expected time to ABRACADABRA is \(26^{11}+26^4+26\) seconds.

**Synopsis.** Conditioning on a partition, the \(L^2\) projection, martingales, stopping, Doob's inequality, \(L^2\) convergence, upcrossings, and almost-sure convergence. The monkey is optional stopping on a carefully chosen martingale. Book 11 returns to martingales for uniform integrability, de Finetti, and Kakutani.

**Proved.** Optional stopping under the three conditions. Doob's maximal inequality. \(L^2\) convergence. Almost-sure convergence via upcrossings.

**Examples.** ABRACADABRA. The martingale that hits \(+1\) and makes optional stopping fail.

**Figures.** Three.

#### Chapter 11. Brownian Motion

**Status.** KEEP — `chapters/ch11-brownian.tex` (602 lines). "A first look at Itô's formula" stays a look. Book 12 owns the integral. Lévy's midpoint construction is the existence proof this floor is responsible for.

**Hook.** Brown's pollen, 1827. Einstein's explanation, 1905. Wiener's mathematical path.

**Synopsis.** From random walks to Brownian motion, Lévy's construction, scaling and the Markov property, quadratic variation, the reflection principle, a first Itô formula, and the binomial model for Black–Scholes. The path is continuous and nowhere differentiable: the "typical" object of Book 7's Baire theorem, now random. Quadratic variation is the clock Book 12 will use.

**Proved.** Lévy's construction gives a continuous process with the right finite-dimensional laws, modulo the measure-theoretic facts labelled as admitted. Quadratic variation along the dyadic partitions. The reflection principle. The Black–Scholes price as a binomial limit, on the numerical example the chapter uses.

**Examples.** \(S_0=K=100\), \(r=0.05\), \(\sigma=0.2\), \(T=1\), with \(d_\pm\) and the binomial prices. One quadratic-variation computation on a dyadic grid.

**Figures.** Four.

### Part IV. Random Structures

#### Chapter 12. The Probabilistic Method

**Status.** KEEP — `chapters/ch12-method.tex` (492 lines). The giant-component remark stays a remark. The exercise proves a component of linear size, not the constant \(\rho\).

**Hook.** To show a haystack contains a needle, show that a random straw is a needle with positive probability.

**Synopsis.** First and second moments, alteration, the symmetric local lemma, and the subcritical random graph. "With high probability" is defined before it is used. This is chance as a method of proof, which is the mood of Book 15's dictionary: a random model can certify a deterministic fact, and it can also fail to match the object.

**Proved.** The first and second moment methods in the forms stated. The symmetric Lovász local lemma. The subcritical random graph's component structure at the precision the chapter claims. Erdős's lower bound \(R(k,k)>2^{k/2}\).

**Examples.** A tournament or a Ramsey lower bound with the alteration. One local-lemma application with the numbers checked.

**Figures.** Two.

#### Appendix A. Orders

**Status.** MOVE — `chapters/orders.tex` (636 lines), to Book 1, Mathematical Thinking. Dilworth, Sperner, and partial orders do not deliver the logic of uncertainty.

**Hook.** Every sequence of \(n^2+1\) distinct numbers has a monotone subsequence of length \(n+1\).

**Synopsis.** Partial orders, lattices, well-founded orders, Dilworth, Sperner, and the Boolean lattice. Dilworth in the Perles form is the theorem. Well-founded orders include the short closure-rule and infinite-tree prerequisites the series structure asked this volume to keep.

**Proved.** Erdős–Szekeres in the monotone-subsequence form. Dilworth. Sperner's theorem.

**Examples.** A sequence of length \(n^2\) with no longer monotone subsequence. One antichain in the Boolean lattice of the Sperner size.

**Figures.** Three.

#### Appendix B. Extremal Problems and Ramsey Theory

**Status.** REVISE — `chapters/extremal.tex` (685 lines). The cross-reference "Theorem L.2" does not land. Point it at the Erdős bound in Chapter 12.

**Hook.** Complete disorder is impossible.

**Synopsis.** Turán's theorem, forbidding a square, Ramsey numbers, Ramsey's theorem, Schur, van der Waerden, and the sunflower lemma. The small Ramsey numbers, including the Clebsch colouring and \(R_3(3)=17\), stay. This appendix is the combinatorial wing of the probabilistic method, not a second Book 14.

**Proved.** Turán. Ramsey's theorem for graphs and for finite colourings of \(k\)-sets, at the depth the file reaches. Schur. The sunflower lemma. The Erdős–Ko–Rado theorem by Katona's proof.

**Examples.** \(R(3,3)=6\). One Turán graph \(T(n,r)\).

**Figures.** Three.

## The old problem book

Book 6 is Crossroads, the analytic volume. The old P1 problem book is removed by the renumbering branch, which appends its problems to Books 1–6. This plan does not place them again. A problem that cites a chapter moved here follows that chapter.

## Owns, defers, hands forward

**Owns.** Conditioning, the classical laws, Galton–Watson, Chernoff, Borel–Cantelli, Lindeberg, Pólya, finite Markov chains, Poisson processes, discrete martingales, Lévy's Brownian motion, the probabilistic method, Dilworth, Sperner, Ramsey.

**Defers.** Fubini–Tonelli and Lebesgue measure on \(\mathbb R^d\) (Book 7). The strong law from a first moment, Lévy's continuity theorem, Berry–Esseen, Donsker (Book 11). Itô's integral (Book 12). The transposition cutoff (Abstraction).

**Hands forward.** The bell curve as a theorem, a path that becomes Brownian motion, martingales, and the method of proving existence by a random straw.

## Pages and effort

Baseline 251 pages. Target 260–290. Effort: light to moderate. Expand the Lindeberg limsup, repair the Glivenko–Cantelli sentence and the "Theorem L.2" pointer, name the strong-law hypotheses in the preface, and split the part titles.
