# Book 7 — Spaces

*Topology, Measure and Limits.*

**Element.** The rooms. A limit, a length, and an interior, defined so the lower floors can say what they used.

**On disk.** Volume 6, `tome6-spaces`. Eleven chapters plus `chapters/ch12-harder.tex`, the former Machinery chapter "Almost Every Number", now input from `main.tex`. About 179 pages before that chapter. The October review scored the eleven chapters 8. The face of the box in the characterisation of Lebesgue measure is now a sandwich argument in `ch06-measures.tex`.

## Promise

The earlier books used number, limit, and length freely. This floor builds the rooms those words were already furnishing: the real line from sets, metric and topological spaces, compactness, Baire, measure, the Lebesgue integral, products, \(L^p\), Radon–Nikodym, and measures on metric spaces. "Typical" becomes a theorem. Fubini, admitted in Books 4 and 5, is proved. The Sierpiński carpet on the cover is Hausdorff dimension \(\log 8/\log 3\), strictly between 1 and 2, and the chapter that computes dimension should be allowed to say so.

## Prerequisites

The calculus and completeness of Book 1. The probability of Book 4, as motivation: this book does not require its theorems, and Book 4's admitted facts are discharged here. No functional analysis.

## How the subtitle is delivered

The parts keep their catalog names. *Topology, Measure and Limits* is what they do.

Metric and Topological Spaces delivers the topology, and the limits that make it: the construction of \(\mathbb R\), convergence, completeness, compactness, and Baire's theorem. Jordan's theorem, moved from Book 8, joins this part. An inside and an outside are topology. Measure and Integration delivers the measure, through the integral and \(L^p\). Measures on Spaces delivers measure on a metric space, including weak convergence, which is a limit of measures, and the retitled problem chapter on almost every number. No chapter fails the subtitle. No part is renamed.

## Parts

| Part | Name | Chapters |
| --- | --- | --- |
| I | Metric and Topological Spaces | 1–5, and Jordan's theorem from Book 8 |
| II | Measure and Integration | 6–9 |
| III | Measures on Spaces | 10–12 |

---

The chapter notes follow the manuscript's file order. The part names are Metric and Topological Spaces, Measure and Integration, and Measures on Spaces.

### Part I. Metric and Topological Spaces

#### Chapter 1. Sets, Choice and the Real Numbers

**Status.** KEEP — `tome6-spaces/chapters/ch01-sets.tex` (682 lines).

**Hook.** Are there more rationals than integers? More reals than rationals? More points in a square than on a side?

**Synopsis.** Sets, the natural numbers, the integers and rationals as pairs, the reals as a complete ordered field, countability, and choice, Zorn, and well-ordering. Cantor's diagonal argument is the moment infinity comes in sizes. The lower floors assumed \(\mathbb R\). This chapter builds it, and it says which properties were assumptions and which are now theorems.

**Proved.** Countability of \(\mathbb Q\). Uncountability of \(\mathbb R\). The characterisation of \(\mathbb R\) as a complete ordered field, at the strength the file proves. Zorn's lemma from the axiom of choice, in the form later compactness uses.

**Examples.** A bijection between \(\mathbb N\) and \(\mathbb Q\). The Cantor set, as a first uncountable null set, if the chapter draws it; otherwise the diagonal argument alone.

**Figures.** Three.

#### Chapter 2. Metric Spaces and Completeness

**Status.** KEEP — `chapters/ch02-metric.tex` (592 lines).

**Hook.** Iterate a contraction and the values settle. Iterate two contractions of the line by \(\tfrac13\) and the Cantor set appears.

**Synopsis.** Distances, convergence, completeness, completion, a metric description of \(\mathbb Q_p\) that points back to Book 2 and forward to Book 8, Banach's fixed-point theorem, the construction of \(\exp\), \(\cos\), \(\sin\), and \(\pi\), and fractals as fixed points. Banach's theorem is the one theorem that solves an equation, draws a fractal, and ranks a page. The exponential that Book 1 admitted is proved here.

**Proved.** Banach's fixed-point theorem. The completion of a metric space. The existence of \(\exp\), \(\sin\), and \(\cos\) as the solutions the chapter constructs, with \(\pi\) the period.

**Examples.** The cosine fixed point \(0.739085\ldots\). The Cantor set as an iterated function system.

**Figures.** Three.

#### Chapter 3. Topological Spaces

**Status.** KEEP — `chapters/ch03-topology.tex` (495 lines).

**Hook.** Glue the opposite sides of a square and you have a torus. Glue them with a twist and you have a surface no mirror sees in three dimensions.

**Synopsis.** Topologies, subspaces, products, quotients, connectedness, and separation. The Möbius band and the torus are the pictures. Nets are not a systematic language; sequences in metric spaces are enough for the later floors.

**Proved.** Connectedness is preserved by continuous images. The intermediate-value theorem recovered from connectedness, matching Book 1 rather than replacing its proof. A quotient description of the circle and the torus.

**Examples.** The torus and the Klein bottle as quotients of the square. One connected set that is not path-connected, if the chapter has it.

**Figures.** Two.

#### Chapter 4. Compactness

**Status.** KEEP — `chapters/ch04-compact.tex` (660 lines).

**Hook.** A continuous function on a closed interval attains its maximum. On an open interval it may not. Compactness is the difference.

**Synopsis.** Compact spaces, compact metric spaces, Rolle and the mean value theorem again from this point of view, Tychonoff by Zorn, Arzelà–Ascoli, and Stone–Weierstrass. Tietze is an exercise with a full solution and can stay an exercise. Heine–Borel is the theorem a reader of Book 1 will recognise.

**Proved.** Heine–Borel. Sequential compactness in metric spaces. Tychonoff for compact spaces, by the form of choice the chapter uses. Arzelà–Ascoli. Stone–Weierstrass, which later books cite as Theorem 4.19 if the numbering is kept.

**Examples.** A continuous function on a compact set attaining its bounds. One equicontinuous family and its convergent subsequence.

**Figures.** Three.

#### Chapter 5. Baire's Theorem

**Status.** KEEP — `chapters/ch05-baire.tex` (474 lines). This is the floor's first climax: "typical" is a precise word.

**Hook.** Is a typical continuous function differentiable somewhere? Is a typical real number well approximated by rationals?

**Synopsis.** Nowhere dense and meagre sets, nowhere differentiable functions, points of continuity of a regulated function, and the distinction between category and measure. A typical continuous function, in the sense of Baire category, is nowhere differentiable. Book 4's Brownian path is a random version of the same fact. The two notions of typical are not the same, and the chapter says so.

**Proved.** Baire's category theorem. The existence of a continuous nowhere differentiable function, as a comeagre set in \(C[0,1]\).

**Examples.** \(\mathbb Q\) as meagre and of measure zero, and a comeagre set of measure zero, or the reverse, so category and measure part company on the page.

**Figures.** Two.

### Part II. Measure and Integration

#### Chapter 6. Measures

**Status.** KEEP — `chapters/ch06-measures.tex` (546 lines). The box-face estimate is repaired. REVISE the outer-measure subadditivity if the case \(\mu^*(A_n)=\infty\) is still not separated: when the outer measure is infinite there is nothing to cover, and the inequality is immediate.

**Hook.** Every interval has a length. Can every set of reals be given a length that adds over countable disjoint unions and is unchanged by translation?

**Synopsis.** Dynkin's \(\pi\)-\(\lambda\) theorem, outer measures, Carathéodory's extension, Lebesgue measure, Lebesgue–Stieltjes measures, a Vitali non-measurable set, and the construction of an infinite independent sequence from one random number in \([0,1]\). That last construction discharges Book 4's admitted infinite product in the coin-toss case. The general product is Chapter 8.

**Proved.** Carathéodory's extension theorem. Uniqueness of Lebesgue measure among translation-invariant Borel measures with \(\mu(]0,1])=1\), by the repaired sandwich. Existence of a non-measurable set. The binary-digit construction of independent fair coins.

**Examples.** The Cantor set, uncountable and of measure zero. A Vitali class.

**Figures.** Two.

#### Chapter 7. The Lebesgue Integral

**Status.** KEEP — `chapters/ch07-integral.tex` (481 lines).

**Hook.** To add a pile of coins, take them in the order they lie, or sort them by value and count each kind. Lebesgue sorts by value.

**Synopsis.** Measurable functions, the integral, monotone convergence, Fatou, dominated convergence, Riemann's integral and Lebesgue's criterion, modes of convergence, and uniform integrability. The escape of mass for \(n\mathbf 1_{]0,1/n[}\) is the picture of a missing hypothesis. Book 4's integral is recovered where the two overlap.

**Proved.** Monotone convergence, Fatou, and dominated convergence. Lebesgue's criterion for Riemann integrability.

**Examples.** \(n\mathbf 1_{]0,1/n[}\). A function that is Lebesgue integrable and not Riemann integrable.

**Figures.** Two.

#### Chapter 8. Product Measures and Change of Variables

**Status.** KEEP — `chapters/ch08-products.tex` (514 lines). Fubini is the theorem Books 4 and 5 labelled "admitted". The numbering, Theorem 8.6 for Fubini and Theorem 8.8 for change of variables, is what later books cite. Do not renumber it without a pass over those citations.

**Hook.** Slice a loaf and add the areas. Slice it the other way. The volume is the same, and the chapter says when.

**Synopsis.** Product \(\sigma\)-algebras, product measures, Tonelli and Fubini, Lebesgue measure under linear maps, the change-of-variables formula, and polar coordinates. The diagonal counter-example when \(\sigma\)-finiteness drops stays. The volume of the ball returns from Book 5, now as a theorem of this chapter's change of variables.

**Proved.** Tonelli and Fubini. The change-of-variables formula, including the inverse-diffeomorphism step. The volume of the Euclidean ball.

**Examples.** The Gaussian integral in polar coordinates, the computation Book 1 and Book 4 both wanted. One Fubini failure on a non-\(\sigma\)-finite space.

**Figures.** Three.

#### Chapter 9. \(L^p\) Spaces

**Status.** KEEP — `chapters/ch09-lp.tex` (392 lines).

**Hook.** A function is a point. Which distance: the largest gap, the average gap, or the energy of the gap?

**Synopsis.** Young, Hölder, Minkowski, the spaces \(L^p\), approximation by continuous functions, and convolution. These are the rooms Book 8's operators will inhabit. Hölder is not "the key to \(L^p\) in Book 5"; the October errata of Book 1 already points here.

**Proved.** Hölder and Minkowski. Completeness of \(L^p\). Density of continuous compactly supported functions in \(L^p(\mathbb R^d)\) for \(p<\infty\).

**Examples.** A function in \(L^1\) and not in \(L^2\), and the reverse. One convolution that smooths a jump.

**Figures.** Two.

#### Chapter 10. Differentiation and Radon–Nikodym

**Status.** EXPAND — `chapters/ch10-radon.tex` (384 lines). Conditional expectation is Exercise `ex:condexp`. The solution gives the defining property and does not write the tower property. Books 11 and 12 use the tower. Promote conditional expectation, including the tower property, to a numbered theorem. This is the one gap in this book that a later citation stands on.

**Hook.** The devil's staircase climbs from 0 to 1 without a jump, and its derivative is 0 almost everywhere. The increase is hiding.

**Synopsis.** Signed measures, Hahn decomposition, Radon–Nikodym, the Hardy–Littlewood maximal function, Lebesgue differentiation, and absolute continuity. The cricket maximal function, if that is the chapter's picture, stays: it is the inequality that differentiates integrals. Radon–Nikodym is Theorem 10.4 in the citations Book 12's Girsanov theorem uses.

**Proved.** Hahn decomposition. Radon–Nikodym and Lebesgue decomposition. The maximal inequality and Lebesgue differentiation. Conditional expectation and the tower property, once the exercise is promoted.

**Examples.** The Cantor function. A density written as a Radon–Nikodym derivative. One conditional expectation given a finite partition, computed by hand, so the new theorem has a small case.

**Figures.** Two.

### Part III. Measures on Spaces

#### Chapter 11. Measures on Metric Spaces

**Status.** REVISE — `chapters/ch11-metricmeasures.tex` (378 lines). Add one line of finite additivity for the cylinder set function before Kolmogorov's extension. Hausdorff measure is an outer measure; the text refers the Borel property and the normalisation \(\mathcal H^d=c_d\lambda_d\) to Falconer. Either prove that a metric outer measure is a Borel measure and record \(\mathcal H^1=\lambda_1\), or keep the citation and stop any later appeal to \(\mathcal H^d\) as a measure this book constructed. The coast of Britain is the right hook for the cover's carpet.

**Hook.** How long is the coast of Britain? A shorter ruler gives a longer coast.

**Synopsis.** Regularity and tightness, Riesz representation for positive functionals on compact metric spaces, weak convergence, portmanteau, Prokhorov's theorem, Kolmogorov's extension on \(\mathbb R^{\mathbb N}\), and Hausdorff dimension. Prokhorov's theorem is what Book 11's Lévy continuity argument stands on. The Sierpiński carpet has dimension \(\log 8/\log 3\).

**Proved.** Riesz–Markov on compact metric spaces, Theorem 11.3 if the numbering holds. Portmanteau. Prokhorov, Theorem 11.7. Kolmogorov's extension for laws on \(\mathbb R^{\mathbb N}\), Theorem 11.8, after the cylinder additivity line. Ulam's tightness theorem for finite Borel measures on a complete separable metric space.

**Examples.** The carpet's dimension, computed from the construction. Weak convergence of binomial laws to a Gaussian, as a picture of Book 4's theorem in this language.

**Figures.** Three.

#### Chapter 12. Almost Every Number

**Status.** REVISE — `chapters/ch12-harder.tex` (about 1086 lines). The mathematics is the finished Machinery chapter, at the standard of Crossroads. The title "Harder problems" is not a structural element. Retitle it **Almost every number**. Place it at the end of Part III, as problems whose tools are this book, Book 2's continued fractions, and Book 11's Gauss map. The Gauss-map problems must name Book 11 as a tool, not pretend to be elementary. The convergence half of Khinchin, covering \(E_q\) by \(q+3\) intervals and getting measure at most \(8q\psi(q)\), stays: the constant is crude and correct.

**Hook.** Khinchin's theorem, as the Fields citation for Maynard described it: how well a typical real number can be approximated by rationals.

**Synopsis.** Dirichlet's approximation for every irrational, Liouville's transcendentals, and Khinchin's almost-everywhere law. If \(q^2\psi(q)\) decreases, then almost every \(x\) has infinitely many \(p/q\) with \(|x-p/q|<\psi(q)\) when \(\sum q\psi(q)\) diverges, and almost none when it converges. Bounded partial quotients are the badly approximable numbers, with \(c=1/(K+2)\). Category and measure, from Chapter 5, part company on the same set of questions. Continued fractions, a law of Book 2, return as a property of almost every real.

**Proved.** The problems are problems: each has a hint and a complete solution. The chapter does not pretend to be a second development of measure.

**Examples.** Khinchin's divergence case. One badly approximable number, the golden ratio, recognised from Book 2's continued fraction.

**Figures.** Three, the ones the Machinery chapter already drew.

## Owns, defers, hands forward

**Owns.** The construction of \(\mathbb R\). Metric spaces, compactness, Stone–Weierstrass, Baire. Lebesgue measure, the integral, Fubini, change of variables, \(L^p\), Radon–Nikodym, Riesz–Markov on compact metric spaces, Prokhorov, Kolmogorov extension for \(\mathbb R^{\mathbb N}\). After the expansion, conditional expectation and the tower property.

**Defers.** The dual of \(L^p\) as a Banach-space theorem (Book 8). Haar measure on a group (Book 8). Stochastic calculus (Book 12). The Gauss map as an ergodic system (Book 11); this book's problem chapter may use it and must cite it.

**Hands forward.** The rooms. Book 8 puts operators in them. Book 11 puts weak convergence and Prokhorov to work. Book 12 differentiates a path with the Radon–Nikodym derivative Girsanov needs.

## Pages and effort

Baseline 179 pages, plus the problem chapter (the old Machinery Chapter 1 was part of a 75-page book). Target 210–240. Effort: moderate. The flagship proofs stay. The work is the conditional-expectation theorem, the cylinder line, the Hausdorff citation, the outer-measure case, and the retitle.
