# Volume 4: old manuscript to new book

The old files are the manuscript on `origin/main` at the branch point of `cursor/volume4-rewrite-ee7f`. “Retained” means the mathematical statement stays available to the reader, not that a paragraph was copied.

Reader-facing text does not describe this replacement as a revision. This file is an editorial record.

## Global

| Old feature | Disposition | Why |
| --- | --- | --- |
| Twelve chapters in three parts, plus the extremal appendix | Retained in order | Later volumes cite chapters by number |
| Admitted facts: Lebesgue measure on \(\mathbb R^d\), infinite products, Fubini–Tonelli | Removed as proof steps | The reader has no measure theory. The same jobs are done by interval length, binary digits, and continuous iterated integrals, proved in this volume |
| Workshop problems `pb:*` inside the chapters | Removed from the logical path | Not cited outside this volume. Several solutions needed Fourier analysis, representation theory of \(S_n\), or inequalities from later books. The method each one was here to practise is kept when it belongs to the chapter’s own exercises |
| `chapters/gilmer.tex`, included at the end of the old Chapter 4 | Removed until re-proved | The constant \((1-\ln 2)/2\) is the value of that expression. The entropy comparison is restored only as a finished proof after finite entropy exists in the new Chapter 4. It is not required for any later-volume citation |
| `chapters/orders.tex` | Already absent | Lives in Volume 1. Do not import it |
| Cover art and About the Cover | Kept | The picture is still Galton’s quincunx, and Chapter 6 is still the central limit theorem |

## Chapter 1, Counting and Paradoxes

| Old section | Disposition | Why |
| --- | --- | --- |
| Probability spaces, finite and the Kolmogorov axioms in full | Rebuilt | Volume 1 already has finite and countable spaces. The new section records that, then builds infinite coin tosses from one uniform |
| Conditioning and independence | Retained, rewritten | The definitions stay. Examples are not a second copy of Volume 1’s Monty Hall write-up; the exercises still compute the host’s rule |
| Birthdays | Retained as an exercise and a short calculation | The shared-birthday threshold is Volume 1’s theorem. Volume 4 asks for the probability that someone shares a fixed person’s birthday, which is a different number |
| Monty Hall | Exercise, not the chapter’s opening | Volume 1 already computes the three-door host. Exercise 1.5 keeps the \(n\)-door version |
| Bertrand’s three models | Retained and proved | Three experiments, three probabilities \(\frac13,\frac12,\frac14\). This is the warning that “at random” is a choice of model |
| Ballot theorem | Retained and proved by reflection | Interface with Catalan numbers and with Chapter 7 |
| Buffon’s needle | Retained for \(\ell\le d\) | Volume 9 cites the formula. The integral is one-variable calculus from Volume 1 |
| Exercises 1.1–1.6 | Rebuilt in the same slots | Same jobs: own birthday, two children, two tests, Penney, \(n\)-door host, pairwise versus mutual |
| Exercise 1.7 Catalan | Retained | Series interface |
| `pb:whichroot`, `pb:nouniform`, `pb:bollobas`, `pb:granularity` | Removed from the path | Bollobás’s set-pairs inequality and the degree bound for Boolean functions are not used later by label. Bollobás’s inequality is combinatorics that does not serve a probability theorem in this book |

## Chapter 2, Discrete Random Variables

| Old section | Disposition | Why |
| --- | --- | --- |
| Laws, expectation, variance | Retained, with Volume 1 cited for the finite case | New work is absolute convergence on countable spaces and variables on the coin space |
| Classical families | Retained | Bernoulli, binomial, geometric, Poisson. The Poisson limit of the binomial is proved; Volume 1 only defined the masses |
| Cycles and fixed points | Retained | Mean number of fixed points is Volume 1’s example. Mean number of cycles \(H_n\) is proved here. Long-cycle probability is Exercise 2.6 |
| Coupon collector | Retained as a theorem | Volume 1 left it as an exercise |
| Exercises 2.1–2.5 and 2.7 | Rebuilt | Records, fixed-point variance, quicksort expectation, factorial moments, reservoir sampling, birthday waiting time. Each is solvable from this chapter and Volume 1 |
| Exercise 2.6 prisoners and long cycles | Retained | Series interface: \(H_{2n}-H_n\to\ln 2\) |
| `pb:leastqnr` through `pb:lcs` | Removed from the path | Quadratic non-residues, influence, Arrow, and longest common subsequences import tools or length that the main development does not need |

## Chapter 3, Generating Functions

| Old section | Disposition | Why |
| --- | --- | --- |
| Probability generating functions | Retained | |
| Sums and random sums | Retained | |
| Galton–Watson extinction | Retained | Smallest root of \(s=f(s)\). Continuity of the power series is Volume 1 |
| Catalan numbers, paths, trees | Retained | Exercise 3.7 carries the binomial series Volume 5 cites |
| `pb:sicherman`, `pb:loaded`, `pb:subsetsum` | Removed from the path | Sicherman dice are a generating-function puzzle with a finite check; a short main-text example on dice can carry the method if the chapter needs one. The three workshop labels are not external interfaces |

## Chapter 4, Inequalities, Large Numbers and Entropy

| Old section | Disposition | Why |
| --- | --- | --- |
| Markov and Chebyshev | Cited from Volume 1, not re-proved in full | One line points back. The chapter spends its proofs on sharper tails |
| Weak law and Bernstein polynomials | Retained | Weierstrass via Bernstein is a Volume 6 citation |
| Chernoff and Hoeffding | Retained and proved | Volume 5 cites Hoeffding here |
| Borel–Cantelli | Retained, scoped to the coin space of Chapter 1 | Both lemmas. The second needs independence |
| Jensen and entropy, typical sequences | Retained for a finite alphabet | Jensen is Volume 1. The asymptotic equipartition property for i.i.d. finite alphabets is proved from Hoeffding or Chebyshev, not from ergodic theory |
| Gilmer’s union-closed bound | Off the path until re-proved | See the global row |
| `pb:capset`, `pb:kac`, `pb:bonami`, `pb:kacring`, `pb:nbonacci` | Removed from the path | Cap-set and hypercontractivity are not premises of later citations of this chapter |

## Chapter 5, Continuous Probability Done Properly

| Old section | Disposition | Why |
| --- | --- | --- |
| Vitali, \(\sigma\)-algebras, Dynkin, uniqueness of measures | Replaced | The negative Vitali statement may be a remark with the axiom of choice named. The working theory is distribution functions and continuous densities. Dynkin’s theorem is not a step |
| The Lebesgue integral, monotone convergence, Fatou, dominated convergence in that generality | Replaced | Dominated convergence is proved for continuous functions with a continuous integrable dominant. That is the theorem the rest of this volume uses |
| Lebesgue measure and densities | Rebuilt as Riemann densities | A random variable has a density when \(P(X\in[a,b])=\int_a^b f\) for a nonnegative continuous \(f\), or a regulated improper integral, with total mass 1 |
| Change of variables | Rebuilt for the maps we use | One-variable substitution is Volume 1. The chapter proves the polar computation for the Gaussian integral in the plane and the triangular map for ordered arrival times |
| Independence | Retained for densities and for the bit construction | |
| Box–Muller | Retained | Needs the polar computation just proved |
| Exercises 5.1–5.6 and 5.8 | Rebuilt on the new integral | Counter-examples to careless limits, uniqueness of densities, Gaussian tails, Cauchy, gamma, order statistics, beta–gamma if the gamma integral is available from Volume 1’s \(\Gamma\) on positive integers and half-integers only — otherwise gamma is defined here for the integer shape first |
| Exercise 5.7 Cantor distribution | Retained | Series interface |
| `pb:laplace`, `pb:passone`, `pb:irwinhall`, `pb:borwein`, `pb:stick` | Removed from the path | Buffon’s needle in the plane of a tiled floor can be a remark. The other four are not external labels |

## Chapter 6, Convergence and the Central Limit Theorem

| Old section | Disposition | Why |
| --- | --- | --- |
| Modes of convergence | Retained | In probability, almost surely (outer content), and in distribution via bounded uniformly continuous test functions, with the portmanteau link to distribution functions proved |
| Strong law, fourth moment | Retained | The bounded case is in Chapter 4. The fourth-moment proof stays here so Chapter 6 still contains a strong law, as Volume 7’s citation expects |
| Glivenko–Cantelli | Rebuilt and proved | The old sentence that a jump is harmless “with a little more care” is replaced by a complete argument |
| Characteristic functions | Retained at the easy strength | Definition, examples, and “convergence in distribution implies pointwise convergence of characteristic functions”. Uniqueness is proved for laws with a density by Fourier inversion only if the inversion integral is justified in the chapter; otherwise uniqueness for the normal limit goes through the swapping theorem and mollifiers. Lévy’s continuity theorem is not claimed |
| Lindeberg by swapping | Retained as environment 6.10 | Smooth test functions. This is the cited theorem |
| Local theorem and Stirling’s constant | Retained as a reading of Volume 1’s Stirling, not a second proof of the constant | The local binomial theorem is proved from Stirling |
| Gaussian vectors | Retained | Spectral theorem from Volume 1, cited |
| Exercise 6.1 Slutsky, 6.7 cycle CLT | Retained | Series interfaces |
| Exercises 6.2–6.6 | Rebuilt | Confidence interval, delta method, Cauchy counter-example, Poisson median, random-walk returns |
| `pb:sincsum` | Removed from the path | Depends on a companion sinc problem that is also removed |

## Chapter 7, Random Walks

| Old section | Disposition | Why |
| --- | --- | --- |
| Simple random walk | Retained | |
| Reflection, first returns, maximum | Retained | Uses the ballot theorem |
| Arcsine law | Retained in the discrete form, proved | The continuous arcsine law is the Brownian statement in Chapter 11, or a limit named as such |
| Gambler’s ruin | Retained | |
| Pólya’s theorem | Retained | Dimensions 1, 2, and \(\ge 3\) |
| Harmonic functions and Dirichlet | Retained, and Exercise 7.8 is the electrical form | Series interface |
| Random walk that solves 2-SAT | Retained if the argument stays elementary | It is a finite Markov chain in disguise. If it needs a theorem from Chapter 8, it moves to Chapter 8 or is cut. It is not an external citation |
| `pb:rootwalk` | Removed from the path | Roots of unity and return probabilities are a Volume 2/5 flavour, not needed here |

## Chapter 8, Markov Chains

| Old section | Disposition | Why |
| --- | --- | --- |
| Transition matrices, irreducibility, period, stationary distributions | Retained | Existence by Cesàro averages and Bolzano–Weierstrass in the simplex, proved from Volume 1 |
| Convergence and coupling, ergodic theorem for finite chains | Retained | Coupling, not Perron |
| Reversibility and walks on graphs | Retained | |
| Walk on a cycle | Retained as an example | |
| Random transpositions | Upper bound by coupling or by a marking argument, if it stays elementary | The sharp cutoff is Volume 10 / Volume 11, and the text says so |
| Riffle shuffles | Model defined; rising sequences in Exercise 8.8; the seven-shuffle profile is history, not a lemma | Bayer–Diaconis needs the Fourier analysis of \(S_n\) |
| Exercises 8.1–8.5, 8.7 | Rebuilt | Lazy chain, knight, Ehrenfest, PageRank as a finite chain, Metropolis |
| Exercises 8.6 and 8.8 | Retained | Series interfaces |
| `pb:carries` through `pb:gilbreath` | Removed from the path | Carries are a nice chain but not an interface. Gilbreath and the hypercube cutoff are not premises |

## Chapter 9, Poisson Processes

| Old section | Disposition | Why |
| --- | --- | --- |
| Exponential law and memorylessness | Retained | |
| Construction by exponential gaps | Retained | The joint density of arrival times uses the triangular change of variables from Chapter 5 |
| Uniform order statistics, independent increments | Retained | |
| Colouring lemma | Retained as environment 9.5 | Volume 12 cites Lemma 9.5 |
| Thinning and superposition | Retained | |
| Inspection paradox | Retained | |
| Le Cam’s inequality | Retained if the coupling proof uses only Chapter 2 | It is the quantitative Poisson approximation |
| M/M/1 | Retained | Birth–death balance on the countable state space, stationary geometric law for load \(<1\) |
| Old exercises except the workshop list | Rebuilt around these theorems | |
| `pb:spacings`, `pb:dixie` | Removed from the path | Not external labels |

## Chapter 10, Martingales

| Old section | Disposition | Why |
| --- | --- | --- |
| Conditioning on a finite partition | Retained | This is the definition the chapter uses |
| \(L^2\) projection | Retained for a finite list of square-summable variables | Not an infinite-dimensional Hilbert space. Volume 1’s orthogonal projection on \(\mathbb R^n\) is the tool |
| Conditional expectation in general | Scoped | The tower property is proved for finite partitions. The general measurable case is named as Volume 7 / Volume 11 |
| Martingales, optional stopping, the \(+1\) counter-example | Retained | Three sufficient conditions, stated |
| Doob’s maximal inequality | Retained on this class | |
| \(L^2\) convergence and upcrossings | Retained for martingales with bounded increments on the coin space, or for \(L^2\)-bounded ones with the upcrossing inequality written out | Almost-sure convergence means outer content zero |
| Azuma | Retained | |
| ABRACADABRA | Retained as the example | |
| Old exercises | Rebuilt from these theorems | No `pb:` labels lived in this chapter |

## Chapter 11, Brownian Motion

| Old section | Disposition | Why |
| --- | --- | --- |
| Scaling limit of the walk, as motivation | Retained as motivation | Donsker’s theorem is Volume 11 and is not used |
| Lévy’s construction | Retained as environment 11.4 | Gaussians come from Chapter 5, not from an admitted product |
| Scaling, symmetry, time inversion | Retained | |
| Quadratic variation and Paley–Wiener–Zygmund nowhere differentiability | Retained if the proofs close | |
| Martingale property and reflection, environment 11.12 | Retained | |
| First look at Itô | Retained as a dyadic expansion | The integral is Volume 12 |
| Binomial Black–Scholes | Retained as a limit under the local central limit theorem, on one numerical contract | The price is a theorem about the binomial model, not a claim about markets |
| Exercise 11.3 zeros | Retained | Series interface. The proof uses Chapter 5’s integral, not an unnamed Tonelli theorem |
| Exercises 11.1, 11.2, 11.4–11.7 | Rebuilt | Joint law of maximum and endpoint, Brownian bridge, hitting density, \(p\)-variation, put–call parity, one-step binomial |
| No `pb:` labels in this chapter | — | |

## Chapter 12, The Probabilistic Method

| Old section | Disposition | Why |
| --- | --- | --- |
| First moment, alteration, second moment | Retained | |
| Symmetric local lemma | Retained | |
| Subcritical random graph | Retained at the precision of component size \(O(\log n)\), not the giant-component constant | The old exercise that proves a linear component in the supercritical regime may stay as an exercise if its proof uses only first and second moments |
| “With high probability” | Defined before use | |
| Exercises 12.1–12.3 and 12.5–12.7 | Rebuilt | Caro–Wei, tournaments, sum-free sets, property B, connectivity threshold, giant component |
| Exercise 12.4 crossing lemma | Retained | Series interface. Euler’s formula is proved before it is used |
| The long `pb:` list from `pb:vanish` through `pb:inspection` | Removed from the path | Thirty-three problems. None is cited by label outside this volume. Several are research-length and use later books. Keeping them would either smuggle those tools or leave solutions the new exposition cannot support |

## Appendix, Extremal Problems and Ramsey Theory

| Old section | Disposition | Why |
| --- | --- | --- |
| Turán | Retained | |
| Forbidding a square | Retained if the proof is elementary counting | Kővári–Sós–Turán at the convexity bound Volume 1 can support |
| Ramsey numbers, \(R(3,3)=6\), Ramsey’s theorem | Retained | |
| Schur, van der Waerden | Schur retained. Van der Waerden retained only with a complete elementary proof | A citation of the colouring theorem is not a proof |
| Sunflower lemma | Retained | |
| Erdős–Ko–Rado by Katona’s double counting | Retained | |
| The broken “Theorem L.2” pointer | Removed by writing the Erdős lower bound where it is proved, in Chapter 12 | The old plan’s repair |
| Exercises, hints, solutions | Rebuilt to match the new proofs | |

## What later volumes may still say

Recorded so a later citation repair is a choice, not a surprise.

- Volume 5 says Chapter 5 proved dominated convergence for the Lebesgue integral. The new theorem is the continuous case, which is what Volume 5’s own corollary uses.
- Volume 7 says it discharges admitted fact (A1). The new book constructs the product it needs.
- Volume 12’s phrase “Tonelli” inside the pointer to Exercise 11.3 meets a proof that computes the expected measure by the integral of Chapter 5.
