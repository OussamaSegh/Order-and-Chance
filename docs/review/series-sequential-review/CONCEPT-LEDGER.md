# Concept ledger

One line per concept, notation, or named result, in the order the series introduces it. Later reviews check a use against the earliest line that actually states it. A forward pointer is not an introduction.

Notation clashes with earlier entries are listed at the end of each volume. Volume 1 has no earlier volume.

## Volume 1

Book order: preface, then Chapters 0–10 as numbered by `main.tex` (`\setcounter{chapter}{-1}`). File paths are under `volume1-first-principles/`.

### Preface (`chapters/preface.tex`)

- \(\N=\{0,1,2,\ldots\}\), \(\N^*=\{1,2,\ldots\}\), \(\Z\subset\Q\subset\R\) — `sym:numbers`, line 40.
- Well-ordering of \(\N\): every nonempty subset has a least element — line 28.
- Completeness of \(\R\): a nonempty set that is bounded above has a least upper bound — line 29. The word supremum is defined in Chapter 0.
- \(e=\exp(1)\), \(e^x=\exp(x)\); \(\exp\) is a standing bijection from \(\R\) onto the positive reals, inverse \(\ln\), with \(\exp(0)=1\) — lines 31 and 42.
- Standing derivatives, only after the word is defined: \(\exp'=\exp\), \(\ln'(x)=1/x\) for \(x>0\), \(\sin'=\cos\), \(\cos'=-\sin\) — line 42.
- Unit-circle values and period \(2\pi\) for sine and cosine. The two leastness sentences used later (least positive zero of cosine, least positive angle with cosine \(-1\)) are not in this list. See V1-008.
- Integral of a continuous function on a closed bounded interval: signed area; linear; preserves order; additive on adjacent intervals; constant \(c\) on \([a,b]\) has area \(c(b-a)\) — lines 33 and 43.
- An integral over an unbounded interval, or up to a blow-up, is a limit of ordinary integrals. Two infinite processes may not be swapped on that ground alone — line 43.

### Chapter 0 — The Language of Mathematics (`chapters/ch00-language.tex`)

- Even \(n=2k\), odd \(n=2k+1\) — `sym:parity`, line 37.
- Axiom, theorem, proposition, lemma, corollary, conjecture; hypothesis and conclusion — lines 47–53.
- Statement, predicate; \(\land\), inclusive \(\lor\), \(\neg\); implication and vacuous truth; \(\Leftrightarrow\); sufficient and necessary — lines 67–99.
- \(\forall\), \(\exists\), scope — `sec:quantifiers`, line 133.
- Negation rules for quantifiers and connectives; De Morgan — `prop:lang-negation`, line 170.
- Direct proof, cases, contrapositive, contradiction, counterexample, \(\exists!\) — lines 216–310.
- Absolute value \(|t|\) — line 225. Irrational: a real that is not rational — line 231.
- Set, element, \(\in\), \(\varnothing\), set-builder; \(\subseteq\), equality by two inclusions, \(\subsetneq\) — lines 324–332.
- Union, intersection, difference, complement in a named \(U\); empty union and empty intersection — lines 336–346.
- Distributivity and De Morgan for sets — `prop:lang-sets`, line 348.
- Power set \(\mathcal P(A)\); ordered pair; Cartesian product; \(\R^n\) — lines 383–397.
- Function, domain, codomain, graph — line 403.
- Intervals \([a,b]\), \((a,b)\), half-open, infinite ends — line 417. Same parentheses as ordered pairs.
- Image, range, inverse image \(f^{-1}(B)\) — lines 421–427.
- Preimages preserve union, intersection, and complement — `prop:lang-preimages`, line 435.
- Injective, surjective, bijective — line 466. Composition, identity, inverse function — lines 490–501.
- Inverse iff bijective; inverse unique — `thm:lang-inverse`, line 509.
- Relation; reflexive, symmetric, transitive; equivalence relation; class \([x]\); partition — lines 543–575.
- Equivalence relations are partitions — `thm:lang-partition`, line 579.
- Partial order, antisymmetry, total order, strict order — lines 602–604.
- Least and minimal; greatest and maximal; upper bound, supremum, infimum — lines 606–623.
- \(f(A\cap B)\subseteq f(A)\cap f(B)\), with equality for every pair of subsets iff \(f\) is injective — workshop, lines 680–685.

### Chapter 1 — Sums, Binomials and Induction (`chapters/ch01-sums.tex`)

- \(\sum\), empty sum \(0\), linearity, reindexing, double sums — line 26.
- Arithmetic sum and geometric sum — line 49.
- \(\prod\), empty product \(1\), \(n!\) for \(n\ge 1\), \(0!=1\) — line 138.
- Telescoping — `prop:telescope`, line 144.
- Weak and strong induction, equivalent to well-ordering — `prop:induction`, line 207.
- Prime (\(p>1\), positive divisors \(1\) and \(p\)); \(d\mid a\) for positive \(d\) — line 228. General \(a\mid b\) at line 595.
- Bernoulli: \((1+x)^n\ge 1+nx\) for \(x\ge -1\), \(n\in\N\) — `prop:bernoulli`, line 270.
- \(\binom{n}{k}\) as a count; Pascal; factorial formula; binomial theorem — `prop:binom`, line 299.
- Vandermonde — `prop:vandermonde`, line 367.
- Polynomial, degree, forward difference \(\Delta\); \(\binom{X}{k}\) — lines 394–398.
- \(\Delta\binom{X}{k}=\binom{X}{k-1}\) — `prop:deltabinom`, line 404.
- Newton’s forward-difference formula — `thm:newton`, line 419.
- Sum of a polynomial in the binomial basis; hockey stick — `cor:sumpoly`, line 451.
- \(\sum_{k=1}^n k^3=(n(n+1)/2)^2\), four proofs — line 486.
- Coprime, \(\gcd\), \(\gcd(a,0)=|a|\), \(\gcd(0,0)\) undefined; \(a\equiv b\pmod m\) — line 595.
- Division algorithm, remainder in \([0,b)\); \(\lfloor a/b\rfloor\) means that integer quotient only — line 597.
- Bézout — line 619. Least common multiple — line 632.
- Euclid’s lemma and unique factorisation for \(n\ge 2\) — line 634.
- Exponent description of the lcm is stated at line 650 and is not proved (V1-001).
- Fibonacci \(F_0=0\), \(F_1=1\) — `ex:fibgcd`, line 727. Harmonic \(H_n\) — `ex:harmonic`, line 740.

### Chapter 2 — Counting and Discrete Reasoning (`chapters/ch02-counting.tex`)

- Sum, product, and bijection rules; \(|A|\) for cardinality — lines 35–38.
- Maps, injections, permutations, subsets, multisets, pigeonhole — `prop:counts`, line 60.
- Inclusion–exclusion — `thm:incexc`, line 132. Indicator \(\mathbf 1_A\) — line 158.
- Fixed point, derangement, \(D_n\), with \(D_0=1\) — line 178. Formula — `prop:derang`.
- Cycle decomposition of a permutation — lines 236–239.
- Lattice paths — `prop:paths`, line 252. Catalan numbers named at line 300; the formula is `ex:catalan`.
- Formal power series, \([t^n]\), Cauchy product — lines 320–338.
- \([t^n](1-t)^{-r}=\binom{n+r-1}{r-1}\) — line 346.
- Euler’s totient as a count — `ex:phi`. Surjections — `ex:surj`. Erdős–Szekeres square case by pigeonhole — `ex:erdos`.

### Chapter 3 — Sequences, Series and Limits (`chapters/ch05-sequences-series.tex`)

- Real triangle inequalities — `prop:real-triangle`, line 40.
- Limit of a sequence, including \(+\infty\) — line 54.
- Archimedean property, from completeness — line 89.
- Real floor \(\lfloor x\rfloor\) — `prop:floor`, line 93.
- \(\sqrt 2\) irrational, and the positive real square root of \(2\) — `prop:sqrt2`, line 120, and line 139.
- Algebra of limits, squeeze, subsequences — line 141.
- \(o\), \(O\), \(\sim\) for sequences — `sym:asymptotic`, line 179. Function form is declared before function limits (V1-049).
- Geometric series for \(|q|<1\) — line 196.
- \(\inf S=-\sup(-S)\) — `sym:inf`, line 247.
- Monotone convergence, adjacent sequences, Bolzano–Weierstrass, Cauchy — `prop:seqcrit`, line 253.
- Cesàro — `thm:cesaro`, line 319. Corollary \(u_n/n\to\ell\) — line 330.
- Limit of a function, continuity, derivative, one-sided derivative — line 371.
- Sum, product, quotient, chain rule — `prop:early-differentiation`, line 391.
- \(x^\alpha\) for \(x>0\), and \((x-a)^n\) for integer \(n\) at every real \(x\) — lines 427–433.
- Intermediate-value theorem; positive \(n\)th roots; odd-degree real root — `thm:ivt`, line 447, and the example at line 475.
- Extreme-value theorem — `thm:evt`, line 489.
- Heine, uniform continuity on a closed bounded interval — `thm:heine`, line 508.
- Fermat, Rolle, mean value, \(f'=0\Rightarrow\) constant — `thm:mvt`, line 534.
- \((1+1/k)^k\to e\) — `prop:e-limit`, line 566.
- \(0<\sin x<x<\tan x\) on the stated intervals, assuming the leastness sentences — `prop:sincmp`, line 589.
- Integral as signed area; Riemann sum — line 605.
- First fundamental theorem — `prop:early-ftc`, line 624.
- Nonnegative series, comparison, integral test, \(p\)-series, ratio test — `prop:posseries`, line 657.
- Absolute convergence, alternating series and remainder, Cauchy product — `prop:signedseries`, line 718.
- Nonnegative double sums; absolute rearrangement — `prop:safe-sums`, line 775.
- Euler’s constant: \(H_n=\ln n+\gamma+o(1)\) — `prop:gamma`, line 792.
- Shape of Stirling: \(n!\sim C\sqrt n\,(n/e)^n\), constant not yet identified — `prop:stirlingshape`, line 824.
- Abel summation — `prop:abelsum`, line 881.
- Dirichlet’s test and Abel’s test — `thm:dirichlettest`, line 897.
- Convergence of \(\sum\sin(k\theta)/k\) for \(\theta\notin 2\pi\Z\); the closed form is postponed to Volume 5 — line 919.

### Chapter 4 — Orders (`chapters/orders.tex`)

- Poset, chain, antichain, cover, comparable — `orders:def:poset`, line 34. The three order axioms are recalled from Chapter 0.
- Hasse diagram — line 49. Linear extension — line 69.
- Topological sorting of a finite poset — `orders:prop:topsort`, line 75. Szpilrajn’s infinite extension is stated, not used — line 88.
- Height and width — line 94.
- Mirsky — `orders:thm:mirsky`, line 98.
- Dilworth, Perles’s proof — `orders:thm:dilworth`, line 120.
- Erdős–Szekeres, rectangular form — `orders:thm:es`, line 152.
- Boolean lattice \(B_n\) — line 197.
- LYM inequality and Sperner — `orders:thm:lym`, line 201.
- Symmetric chain decomposition — `orders:thm:scd`, line 240.
- Erdős–Ko–Rado — `orders:thm:ekr`, line 275. The arc classification in the proof is V1-003.
- Well-founded: every nonempty subset has a minimal element — `orders:def:wf`, line 314.
- Well-founded induction — `orders:thm:wfind`, line 322.
- Lexicographic order on a product of well-founded orders — `orders:prop:lex`, line 342.

### Chapter 5 — Complex Numbers and Roots of Unity (`chapters/ch02-complex-roots.tex`)

- Complex number as a pair; conjugate; modulus; field axioms, inverse after line 74 — lines 34–74.
- Triangle inequality, with the equality case — in the same opening section.
- Sequential limit in \(\C\) — the complex-series subsection.
- \(\exp z\), argument, \(re^{i\theta}\) — `prop:expform`, line 208. De Moivre is part (a).
- Group, subgroup, order of a group, order of an element, cyclic group — `def:elementary-group`, lines 352–362. Placed before \(\mathbb U_n\).
- \(n\)th roots of unity; primitive root; \(X^n-1=\prod(X-\omega^k)\) by the geometric sum — before `prop:rootsfactor`.
- Orthogonality of the powers of a root of unity — `prop:orth`.
- Roots-of-unity filter — `thm:filter`, line 510.
- Cyclotomic polynomial \(\Phi_n\), integer coefficients by monic division — `prop:cyclotomic`. Irreducibility for prime \(p\) is the next chapter’s exercise; general \(n\) is Volume 3.
- Direct similarity; equilateral criterion — `prop:equilateral`.
- Dirichlet kernel \(D_n(\theta)\) — exercise `ex:dirichlet`, line 656. Same letter as the derangement count.

### Chapter 6 — Polynomials (`chapters/ch03-polynomials.tex`)

- Polynomial as a finite list of coefficients; degree of the zero polynomial left undefined; \(\mathbb K[X]\) — opening section.
- Formal derivative, product rule, power rule on \(\mathbb K[X]\) — lines 71–76.
- Euclidean division — `prop:polydiv`.
- Root, factor, multiplicity — `prop:rootsfactor`, line 99. Part (c) for non-real \(a\) is V1-009.
- Polynomial gcd and Bézout in \(\mathbb K[X]\) — `prop:polynomial-bezout`, line 127.
- d’Alembert–Gauss: a nonconstant polynomial over \(\C\) has a root; real polynomials factor into linears and quadratics — `thm:dalembert`, line 155.
- Elementary symmetric polynomials; Viète — `prop:viete`, line 198.
- Lagrange interpolation — `thm:lagrange`, line 222.
- Chebyshev \(T_n\), recurrence, leading coefficient \(2^{n-1}\) — `prop:cheb`.
- Rational-root theorem — `prop:ratroot`, line 313.
- Gauss’s lemma — `prop:gausspoly`, line 326.
- Eisenstein — `thm:eisenstein`, line 339.
- Reduction modulo a prime — `prop:reduction`, line 352.
- Newton’s identities — `prop:newtonid`, line 371.
- Fundamental theorem on symmetric polynomials — `thm:symmetric`.
- Sign changes \(V(P)\); Descartes’ rule — `thm:descartes`.
- Gauss–Lucas — `thm:gausslucas`.
- Discriminant of a cubic, in the exercises.
- \(\mathbb F_p=\Z/p\Z\) as a field, from Bézout, in the secret-sharing example — line 254. Probability words there are V1-010.

### Chapter 7 — Linear Algebra (`chapters/ch07-linear-algebra.tex`)

- Vector space over \(\R\) or \(\C\); subspace; span; independence; basis; dimension — lines 31–56. Exchange lemma in the same theorem.
- Linear map, kernel, image, rank — line 78.
- Rank–nullity — `prop:ranknullity`, line 97.
- Matrix of a map, product, transpose, inverse, similarity, change of basis — lines 106–126.
- Elimination; triangular matrices — line 160.
- Sign of a permutation — `lem:sign`, line 183.
- Determinant — `thm:det`, line 196. Laplace expansion — line 238.
- Vandermonde determinant — `prop:vdm`, line 265.
- Eigenvalue, eigenvector, characteristic polynomial, trace — `prop:charpoly`, line 293.
- Diagonalisability — `thm:diag`, line 317.
- Real inner product, norm, orthogonal matrix — lines 344–350.
- Gram–Schmidt and orthogonal projection — `thm:gramschmidt`, line 354.
- Spectral theorem for a real symmetric matrix — `thm:spectral`, line 399.
- Quadratic form; positive semidefinite and positive definite — line 437.
- \(p\)-dimensional volume; Gram determinant — `thm:gram`, line 458.
- Adjugate and Cramer’s rule — `prop:adjugate`, line 484.
- Cayley–Hamilton — `thm:cayleyhamilton`, line 501.
- Least squares and the normal equation — line 553.
- Condition number, as greatest stretch over least stretch — line 580.
- Nilpotent matrix — `ex:nilp`. Hadamard’s inequality — `ex:hadamard`. Sylvester’s determinant identity — `ex:sylvester`. Integer inverse iff \(\det=\pm 1\) — `ex:intinverse`. PageRank / positive stochastic matrix — `ex:stochastic`. Cauchy’s determinant and the Hilbert closed form — `ex:cauchydet`.

### Chapter 8 — Differential and Integral Calculus (`chapters/ch06-integrals-taylor.tex`)

- Class \(C^k\); one-sided derivative at an endpoint — line 24.
- Inverse-function rule, proved here; the other differentiation rules are Chapter 3 — line 26.
- Antiderivative; substitution, parts, partial fractions as techniques — lines 66–68.
- Improper integral — line 110.
- Integration toolkit: parts, change of variables, Riemann-sum error — `prop:inttools`, line 130.
- Taylor’s formula with integral remainder, Lagrange bound, and Taylor–Young — `thm:taylor`, line 176.
- Cauchy mean-value theorem and l’Hôpital for the \(0/0\) form — `thm:lhopital`, line 266. The \(\infty/\infty\) form is `ex:lhopital`, not the theorem (V1-080).
- Wallis integrals \(W_n=\int_0^{\pi/2}\sin^n t\,dt\) — `prop:wallis`, line 313.
- \(\int_0^\infty e^{-x^2}\,dx=\sqrt\pi/2\) — `prop:gaussianintegral`, line 355.
- Stirling with \(C=\sqrt{2\pi}\) — `thm:stirling` and `thm:stirlingC`, line 396.
- Gamma function \(\Gamma(x)=\int_0^\infty t^{x-1}e^{-t}\,dt\) for \(x>0\); \(\Gamma(x+1)=x\Gamma(x)\); \(\Gamma(1/2)=\sqrt\pi\) — `prop:gammafn`, line 429. Log-convexity is Chapter 9. Bohr–Mollerup is Volume 5.
- Midpoint and trapezoid rules — `prop:quadrature`, line 475.
- One further term of Stirling — `prop:stirlingnext`, line 519.

### Chapter 9 — Inequalities, Convexity and Estimates (`chapters/ch04-inequalities.tex`)

- A square is nonnegative; rearrangement from that — `sec:squares`.
- Convexity: chords, tangents, Jensen — `prop:convex` / `sec:convex`.
- AM–GM — `thm:amgm`.
- Cauchy–Schwarz, sums and integrals — `thm:cs`.
- Young, Hölder.
- Rearrangement inequality.
- Chebyshev’s sum inequality — `prop:chebsum`.
- Power means — `thm:powermeans`.
- Minkowski’s inequality — `thm:minkowski`.
- Carleman’s inequality with constant \(e\). Sharpness of \(e\) is stated at line 599 and the partial-sum step is V1-013 — `sec:carleman`.
- Log-convexity of \(\Gamma\) — `prop:gamma-convexity`, line 609.

### Chapter 10 — First Probability (`chapters/ch09-probability.tex`)

- Finite probability space; uniform count; conditional probability — opening section and `prop:proba`.
- Independent events; random variable; expectation; variance; covariance; pairwise independence — `prop:varsum` and the definition at line 244.
- Bernoulli, binomial, hypergeometric — `prop:laws`.
- Markov and Chebyshev — `thm:chebyshev`, line 369.
- Weak law for pairwise independent variables with a common mean and a common finite variance — `thm:wlln`, line 388.
- Countable probability, marked as such: geometric waiting, Poisson masses — `sec:countable-probability`, line 417.
- Hat-check limit \(D_n/n!\to 1/e\), from Chapter 2’s exact count, Chapter 8’s exponential series, and Chapter 3’s alternating remainder — lines 215–227.
- Ballot theorem, as an exercise. Ramsey \(R(3,3)=6\), as an exercise. Coupon collector, marked countable.

### Field guide (`chapters/field-guide.tex`)

- No new general tool. It uses unique factorisation, the division algorithm, Fibonacci, and the probability chapter’s independence warning.
- A nonconstant integer polynomial takes infinitely many composite values, and only finitely many times a fixed integer value — the unnumbered theorem in “Every such formula breaks”.
- Legal binary words with no two consecutive \(1\)s, counted by a transfer matrix and by \(L_n=F_{n+1}+F_{n-1}\).

### Notation clashes inside Volume 1

No earlier volume, so no clash with a previous book. Inside this volume:

- \(D_n\) is the number of derangements (`ch02-counting.tex:178`) and, later, the Dirichlet kernel \(D_n(\theta)\) (`ch02-complex-roots.tex:658`). The Cauchy-determinant solution also uses \(D_n\) locally for a determinant (`ch07-linear-algebra.tex:933`).
- \((a,b)\) is an ordered pair (Chapter 0, line 389) and an open interval (line 417).
- \(f^{-1}\) is an inverse function and a preimage. The identification for bijections is V1-021.
- \(\gamma\) is Euler’s constant (`prop:gamma`). \(\Gamma\) is the Gamma function (`prop:gammafn`). Different symbols, same spoken name.
- \(\lfloor a/b\rfloor\) in Chapter 1 is the quotient from the division algorithm. The real floor is `prop:floor` in Chapter 3. They agree when both apply.
- The exponent test for \(\operatorname{lcm}\) is printed as a finished fact at `ch01-sums.tex:651` and is not a proved lemma (V1-001). Later volumes should not cite it as proved in Volume 1 until that gap is filled.
- The two cosine leastness sentences are used from Chapter 3 on and are not in the preface list (V1-008). Later volumes that quote `prop:sincmp` or `prop:expform` inherit that hypothesis.
