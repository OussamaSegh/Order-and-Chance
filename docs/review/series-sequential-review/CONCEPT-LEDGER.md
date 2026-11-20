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

## Volume 2

Book order in `volume2-integers/main.tex`: preface, then Chapters 1–7, then Diophantine equations, then continued fractions, then the Gaussian and Eisenstein integers, then characters. File paths are under `volume2-integers/`. A forward pointer is not an introduction. Binet’s formula is still only the solution of Volume 1’s `ex:fibmat` (V2-001).

### Chapter 1 — Divisibility (`chapters/ch01-divisibility.tex`)

- \(a\mid b\), units \(\pm1\), prime, remainder in \([0,b)\) — `sym:divides`, line 31. Euclidean division — `thm:div`, line 36.
- Additive subgroup of \((\Z,+)\); every subgroup is \(d\Z\) — `prop:subgroups`, line 73. The inclusion \(d\Z\subset H\) is V2-004.
- \(\gcd(a,b)\) as the positive generator of \(a\Z+b\Z\); \(\gcd(0,0)=0\); \(\operatorname{lcm}(a,0)=0\) — `sym:gcd`, line 81.
- Bézout — `thm:bezout`, line 95. Euclid’s lemma — `thm:gauss`, line 106.
- Unique factorisation — `thm:fta`, line 117.
- \(v_p\) on \(\Z\setminus\{0\}\) and on \(\Q^\times\); \(\gcd\) and \(\operatorname{lcm}\) by min and max; \(d\mid n\) iff \(v_p(d)\le v_p(n)\) — `sym:valuation`, `sym:lcm`, lines 154–164. This is the exponent test missing from Volume 1.
- Legendre’s formula \(v_p(n!)\) — `prop:legendre`, line 168.
- Euclidean algorithm, extended coefficients, general solution of \(ax+by=c\) — lines 217–245.
- Lamé’s bound — `thm:lame`, line 266. The \(O(\log b)\) sentence uses Binet (V2-001).
- Ideal, as a name for \(a\Z+b\Z\), not a theory — line 91.

### Chapter 2 — Primes (`chapters/ch02-primes.tex`)

- Infinitely many primes — `thm:euclid-primes`, line 36.
- Sieve of Eratosthenes and the stopping rule at \(\sqrt N\) — line 64.
- \(\sum_{p\le x}1/p\ge\ln\ln x-1\) — `thm:euler`, line 96. The telescoping sum is V2-006.
- \(\pi(x)\); \(\vartheta(x)=\sum_{p\le x}\ln p\); \(\mathrm{Li}(x)=\int_2^x dt/\ln t\) — lines 136–149.
- Binomial bounds and the missing primes in \((2n/3,n]\) — `lem:binom`, line 157.
- \(\prod_{p\le x}p<4^x\) and the Chebyshev bounds of order \(x/\ln x\) — `thm:cheb`, line 179.
- Bertrand: for \(n\ge1\) a prime in \((n,2n]\) — `thm:bertrand`, line 247. The first monotonicity sentence is V2-007.
- Prime-number theorem named, not proved; its home is Volume 6.

### Chapter 3 — Congruences (`chapters/ch03-congruences.tex`)

- Residue class, commutative ring with identity, unit, field — lines 29–41.
- \(\varphi(n)\), with \(\varphi(1)=1\) — `sym:phi`, line 41.
- \(\Z/n\Z\) — `prop:ringZn`, line 43. Units and \(\mathbb F_p\) — `prop:units`, line 74.
- Euler and Fermat — `thm:eulerthm`, line 91. Wilson — `thm:wilson`, line 120.
- Ring morphism, isomorphism; Chinese remainder theorem — `thm:crt`, line 155. \(\varphi(mn)=\varphi(m)\varphi(n)\) for coprime \(m,n\), and \(\varphi(p^k)=p^k-p^{k-1}\).
- Linear congruences: \(d\) solutions modulo \(n\) iff \(d\mid b\) — `prop:lincong`, line 173. Compatibility when \(\gcd(m,n)\) divides the difference of remainders.
- \(\sum_{d\mid n}\varphi(d)=n\) — `prop:phisum`, line 199.
- Formal Taylor expansion of an integer polynomial; Hensel’s lemma for a simple root — `thm:hensel`, line 270.
- Carmichael number, in `ex:korselt`. Lucas’s theorem, in `ex:lucas`.

### Chapter 4 — Arithmetic functions (`chapters/ch04-arithmetic-functions.tex`)

- Arithmetic function, multiplicative, completely multiplicative — line 59.
- Squarefree; \(\mathbf1\), \(\mathrm{id}\), \(\varepsilon\), \(\tau\), \(\sigma\), \(\mu\) — `sym:mu`, line 72.
- Dirichlet convolution — line 97. Commutative, associative, unit \(\varepsilon\), preserves multiplicativity — `prop:conv`, line 101.
- Möbius inversion — `thm:mobius`, line 179. Then \(\varphi=\mu*\mathrm{id}\), \(\tau=\mathbf1*\mathbf1\), \(\sigma=\mathrm{id}*\mathbf1\), with the prime-power formulae.
- Perfect number; even perfect numbers are \(2^{p-1}(2^p-1)\) with \(2^p-1\) prime — `thm:perfect`, line 284.
- \(\sum_{n\le x}\tau(n)=x\ln x+(2\gamma-1)x+O(\sqrt x)\) — `thm:hyperbola`, line 418.
- Probability two random integers are coprime tends to \(6/\pi^2\), in `ex:coprimeprob`, from the Basel value in Volume 1.

### Chapter 5 — Primitive roots (`chapters/ch05-primitive-roots.tex`)

- \(\operatorname{ord}_n(a)\); \(a^m\equiv1\) iff the order divides \(m\); \(\operatorname{ord}_n(a^j)=k/\gcd(k,j)\) — `prop:order`, line 59.
- Primitive root: order \(\varphi(n)\).
- \((\Z/p\Z)^\times\) is cyclic, with \(\varphi(p-1)\) generators — `thm:cyclic`, line 133.
- Lifting a primitive root to \(p^k\) — `lem:lift`, line 226.
- \((\Z/n\Z)^\times\) cyclic iff \(n=1,2,4,p^k,2p^k\) — `thm:cyclicn`, line 234.
- Discrete logarithm \(\operatorname{ind}_g\) — line 287.
- Units modulo \(2^k\) are \((-1)^a5^b\) — `thm:twopower`, line 326. A unit is a square iff it is \(1\pmod8\) — `cor:mod8squares`, line 351.

### Chapter 6 — Quadratic reciprocity (`chapters/ch06-quadratic-reciprocity.tex`)

- Quadratic residue; Legendre symbol — `def:legendre`, line 47.
- Euler’s criterion, including \((-1/p)=(-1)^{(p-1)/2}\) — `thm:eulercrit`, line 55.
- Gauss’s lemma — `thm:gausslemma`, line 171. The letter \(\mu\) here is a sign count (V2-009).
- \((2/p)=(-1)^{(p^2-1)/8}\) — `cor:two`, line 200.
- Quadratic reciprocity — `thm:qr`, line 233. Eisenstein’s floor sum — `lem:eisenstein`, line 254.
- Jacobi symbol and its reciprocity, without the square-root conclusion — `prop:jacobi`, line 340.
- Infinitely many primes \(1\pmod4\), in `ex:onemod4`. The empty-list step is V2-011.

### Chapter 7 — Sums of squares (`chapters/ch07-sums-of-squares.tex`)

- Brahmagupta–Fibonacci identity — line 27.
- Thue’s lemma — `lem:thue`, line 33.
- An odd prime is a sum of two squares iff it is \(1\pmod4\) — `thm:twosq`, line 69.
- \(n\) is a sum of two squares iff every prime \(3\pmod4\) has even exponent — `thm:twosqn`, line 80.
- \(r_2(n)\) named; the formula \(4\sum_{d\mid n}\chi_4(d)\) is previewed and proved in Chapter 10.
- Every nonnegative integer is a sum of four squares — `thm:foursq`, line 160. Euler’s four-square identity is inside the proof.
- Three squares: the obstruction \(4^a(8b+7)\) is `ex:three`. The converse is named as Volume 13, not proved.
- \(N(R)=\#\{x^2+y^2\le R^2\}\) and \(\lvert N(R)-\pi R^2\rvert\le 2\sqrt2\,\pi R+2\pi\) — `thm:circle`, line 277.

### Chapter 8 — Diophantine equations (`chapters/ch09-diophantine.tex`)

- Primitive Pythagorean triples \(x=m^2-n^2\), \(y=2mn\), \(z=m^2+n^2\) — `thm:pyth`, line 113. Inradius \(r=n(m-n)\).
- No positive solution of \(x^4+y^4=z^2\) — `thm:fermat4`, line 218.
- Chord method for a conic with one rational point — `prop:chord`, line 321.
- \(y^2=x^3+7\) has no integer solution — `thm:mordell7`, line 369.
- Markov’s theorem — `thm:markov`, line 410. The equality case is V2-010. Uniqueness of the largest entry is stated as open.

### Chapter 9 — Continued fractions (`chapters/ch08-continued-fractions.tex`)

- Simple continued fraction, convergent \(p_k/q_k\), recurrence — `prop:cfconv`, line 36.
- \(\lvert x-p_n/q_n\rvert<1/q_n^2\), and infinitely many such for irrational \(x\) — `thm:cfapprox`, line 145.
- An infinite expansion determines its value — `lem:cfexistence`, line 171.
- Best approximation — `lem:best`, line 198.
- Legendre: \(\lvert x-p/q\rvert<1/(2q^2)\) implies a convergent — `thm:legendre`, line 206.
- Eventually periodic iff quadratic irrational — `thm:periodic`, line 275.
- Pell’s equation: fundamental solution \(\varepsilon\), and all solutions \(\pm\varepsilon^k\) — `thm:pell`, line 324. The search is the convergents of \(\sqrt d\).
- Ring \(\Z[\sqrt d]\) and norm \(x^2-dy^2\), inside the Pell section. Unit means norm \(\pm1\).

### Chapter 10 — Gaussian and Eisenstein integers (`chapters/ch10-gaussian-eisenstein.tex`)

- \(\Z[i]\), \(\Z[\omega]\) with \(\omega=e^{2\pi i/3}\), norm, units — `prop:quadunits`, line 83.
- Euclidean division in those rings and in \(\Z\) — `prop:eucl`, line 127.
- Bézout, irreducible implies prime, unique factorisation up to units — `thm:ufd`, line 202. Valuation \(v_\pi\).
- \(6=2\cdot3=(1+\sqrt{-5})(1-\sqrt{-5})\) in \(\Z[\sqrt{-5}]\), four irreducible non-associates — `thm:six`, line 228.
- Gaussian primes — `thm:gaussprimes`, line 267.
- \(r_2(n)=4\sum_{d\mid n}\chi_4(d)\) — `thm:r2`, line 295.
- Eisenstein primes, and \(3=-\omega^2\lambda^2\) with \(\lambda=1-\omega\) — `thm:eisprimes`, line 340.
- \(\theta^3\equiv\pm1\pmod{\lambda^4}\) if \(\lambda\nmid\theta\) — `lem:cube`, line 353.
- No nonzero solution of \(x^3+y^3=z^3\) — `thm:flt3`, line 368.

### Chapter 11 — Characters (`chapters/ch14-characters.tex`)

- Dirichlet character modulo \(m\): homomorphism \((\Z/m\Z)^\times\to\C^\times\), extended by \(0\) off the units — `def:t1-character`, line 43.
- Sum of a non-principal character over a period is \(0\) — `prop:t1-charsum`, line 90.
- Structure of \((\Z/m\Z)^\times\) as a product of cyclic groups, using Chapters 3 and 5 — `prop:t1-unitproduct`, line 123.
- Exactly \(\varphi(m)\) characters; they separate units from \(1\) — `thm:t1-charcount`, line 135.
- Orthogonality — `thm:t1-ortho`, line 162.
- \(\sum_{n>X}n^{-s}\le \lfloor X\rfloor^{1-s}/(s-1)\) for \(s>1\) — `lem:t1-pseries`, line 209.
- Product of absolutely convergent Dirichlet series is the series of the convolution — `lem:t1-dseries`, line 219.
- Euler product for a completely multiplicative \(f\) with \(\lvert f\rvert\le1\), \(s>1\), and the limit is nonzero — `thm:t1-eulerprod`, line 230. \(\zeta(s)\) and \(L(s,\chi)\) are the two cases.
- \(\sum\mu(n)n^{-s}=1/\zeta(s)\) — `cor:t1-mu-zeta`, line 270. The series \(\sum\mu(n)/n\) is not claimed to converge.
- \(\Phi(x,z)=\sum_{d\mid P(z)}\mu(d)\lfloor x/d\rfloor\); if \(z\ge\sqrt x\) then \(\Phi(x,z)=1+\pi(x)-\pi(\min\{x,z\})\) — `thm:t1-sieve`, line 315.
- Dirichlet’s theorem on primes in arithmetic progressions is not proved. Volume 6 is named as its home.

### Field guide (`chapters/field-guide.tex`)

- No new theorem. It records the conventions already proved, including \(\gcd(0,0)=0\), and names \(\lvert x\rvert_p\), \(\Z_p\) and \(\Q_p\) as later-volume notation, not as tools of this book.
- Odd prime factor of \(n^2+1\) is \(1\pmod4\), by `ex:onemod4`. Infinitely many primes of the form \(n^2+1\) is left open.

### Notation clashes with Volume 1, and inside Volume 2

- \(\gcd(0,0)\) is undefined in Volume 1 and is \(0\) here (`sym:gcd`, line 84). The field guide repeats the new convention.
- \(\varphi\) is the golden ratio in Volume 1’s Binet exercise and again at `ch01-divisibility.tex:272` and in the continued-fraction chapter. From Chapter 3, \(\varphi(n)\) is Euler’s totient (`sym:phi`).
- \(\mu\) is the Möbius function from Chapter 4 (`sym:mu`). Gauss’s lemma (`thm:gausslemma`) uses \(\mu\) for a sign count (V2-009).
- \(\pi(x)\) is the prime-counting function from Chapter 2. \(\pi\) remains the circle constant.
- \(N(\alpha)\) is the field norm from Chapter 10. The same letter is a bound in several estimates, always local.
- \(\chi_4\) is the non-principal character modulo \(4\), introduced with Jacobi’s formula and again as a Dirichlet character. It is not the Chebyshev polynomial \(T_n\) of Volume 1.
- The exponent form of the lcm, missing as a proof in Volume 1, is proved in Chapter 1 here. Later volumes may cite `sym:lcm` in this chapter. They should not cite the unfinished sentence in Volume 1.

## Volume 3

Book order in `volume3-symmetry/main.tex`: preface, Chapters 1–12, then Appendix A Positive Matrices, B Symmetry Diagonalises, C The Linear Algebra Method, D Hadamard matrices, the afterword, the index. File paths are under `volume3-symmetry/`. A forward pointer is not an introduction. The primitive-element proof is V3-002. The cyclotomic degree \([\Q(\zeta_n):\Q]=\varphi(n)\) is the solution of `ex:phin`, not a numbered theorem (V3-003). Rank–nullity over a finite field is not stated (V3-001). Right cosets are used before they are defined (V3-005).

The shared counter numbers definitions, examples, propositions, lemmas, theorems, and corollaries together. Starred environments (`lemmax` and its siblings) are unnumbered.

### Chapter 1 — Groups as Symmetries (`chapters/ch01-groups.tex`)

- Group, abelian, order \(\lvert G\rvert\); additive notation — `def:group`, line 30.
- Unique identity and inverses, cancellation, \((ab)^{-1}=b^{-1}a^{-1}\), Latin squares — `prop:rules`, line 42.
- Powers \(a^ma^n=a^{m+n}\) and \((a^m)^n=a^{mn}\), prose at line 93.
- Field axioms over an arbitrary \(K\), and a vector space over \(K\) — prose at line 106. The prime fields are Volume 2.
- Exchange over any field: finite basis, extension of an independent set, invariance of dimension, subspaces finite-dimensional — `lem:anyfield`, unnumbered, line 115.
- Determinant facts transfer to any field, including \(\mathbb F_p\): \(n\) independent columns are a basis, \(\det(AB)=\det A\det B\), invertible iff the determinant is nonzero — prose at line 134. The Leibniz proof is Volume 1, `thm:det`.
- \(\mathfrak S(X)\), \(\mathfrak S_n\), composition “first the right factor”, transposition \((a\,b)\), \(GL_n(K)\), \(SL_n(K)\) — `ex:examples`, line 136.
- Dihedral group \(D_n\) (\(n\ge 3\)), order \(2n\), \(r^n=s^2=e\), \(srs=r^{-1}\) — `prop:dihedral`, line 152. Then \(sr^k=r^{-k}s\).
- Rotations of the cube \([-1,1]^3\): 24 orientation-preserving isometries, the three axis types — `prop:cube`, line 237. The isomorphism with \(\mathfrak S_4\) is the solved `ex:cubeS4`.
- Subgroup; the test \(ab^{-1}\); \(\langle S\rangle\) as words — `prop:subgroup`, line 318.
- Order \(o(g)\); \(g^k=e\) iff \(n\mid k\); \(o(g^k)=n/\gcd(n,k)\) — `prop:order`, line 368.
- \(k\)-cycle, order \(k\), prose at line 426.
- Left coset \(gH\), index \([G:H]\) — definition at line 436. Right cosets are not defined here.
- Lagrange — `thm:lagrange`, line 440.
- Orders divide \(\lvert G\rvert\); Euler–Fermat again; a group of prime order is cyclic — `cor:lagrange`, line 467.
- Homomorphism, isomorphism, cyclic group — definition at line 520.
- Classification of cyclic groups; one subgroup per divisor; \(\varphi(n)\) generators; \(\varphi(d)\) elements of order \(d\) — `thm:cyclic`, line 532.
- Finite subgroups of \(K^\times\) are cyclic, with the root bound written for an arbitrary field — solution of `ex:fieldcyclic`.
- A group of exponent 2 is abelian — solution of `ex:square`. Groups of order 4 — solution of `ex:order4`.
- \(\lvert GL_2(\mathbb F_p)\rvert=(p^2-1)(p^2-p)\) — solution of `ex:gl2`.

### Chapter 2 — Morphisms and Quotients (`chapters/ch02-quotients.tex`)

- Kernel, image, fibres are cosets of the kernel; kernels are normal — `prop:kerim`, line 47. Alternating group \(A_n=\ker\varepsilon\).
- Normal subgroup: the three equivalent conditions, including \(gN=Ng\) — `prop:normal`, line 129. The symbol \(Ng\) is V3-005.
- Quotient group — `thm:quotient`, line 178.
- First isomorphism theorem — `thm:iso1`, line 252.
- Correspondence, second and third isomorphism theorems — `thm:iso23`, line 286.
- Group form of the Chinese remainder theorem — `thm:crt`, line 389.
- Internal direct product — `prop:internal`, line 447.
- Semidirect product — `prop:semidirect`, line 500. The reverse inverse is V3-007.
- Centre, derived subgroup, characteristic subgroup — exercises `ex:centre`, `ex:commutator`, `ex:normalnormal`.
- Quaternion group of order 8, as matrices — solution of `ex:quaternion`. Five groups of order 8 — solution of `ex:order8`.

### Chapter 3 — Group Actions and Counting (`chapters/ch03-actions.tex`)

- Action, orbit, stabiliser — definition at line 20, and `ex:actions`.
- Cayley: \(G\) embeds in \(\mathfrak S(G)\) — `thm:cayley`, line 49.
- Orbit–stabiliser, conjugate stabilisers — `thm:orbstab`, line 99.
- Burnside — `thm:burnside`, line 182.
- Pólya, cycle index — `thm:polya`, line 235. Necklace formula in `ex:necklaceformula`.
- Class equation — `thm:classeq`, line 300. The box writes \(C(x_i)\) (V3-006).
- A nontrivial finite \(p\)-group has nontrivial centre; the \(p^2\) abelian argument is inside the proof — `cor:pgroup`, line 350.
- Cauchy — `thm:cauchy`, line 386.
- Centraliser \(C_G(x)\), conjugacy class, centre restated in the class-equation proof.

### Chapter 4 — The Symmetric Group (`chapters/ch04-symmetric.tex`)

- Cycle, support — `def:cycle`, line 20.
- Disjoint cycle decomposition, unique up to order — `prop:cycles`, line 26.
- Order is the lcm of the lengths; sign is \((-1)^{n-c(\sigma)}\) — `cor:ordersign`, line 75.
- Conjugacy classes are cycle types; the conjugation formula — `prop:conjSn`, line 136.
- Generators: adjacent transpositions, all transpositions, \(3\)-cycles for \(A_n\) — `prop:gens`, line 238.
- \(V_4\) is normal in \(\mathfrak S_4\) and in \(A_4\); \(A_4\) has no subgroup of order 6 — `prop:a4`, line 304.
- Fifteen-puzzle: reachable positions are the even permutations — `thm:fifteen`, line 357.
- A nontrivial normal subgroup of \(A_n\) (\(n\ge 5\)) contains a \(3\)-cycle — `lem:split`, line 549.
- \(A_5\) is simple — `thm:a5`, line 611.
- \(A_n\) is simple for \(n\ge 5\) — `thm:an`, line 689.

### Chapter 5 — Sylow Theorems and Finite Groups (`chapters/ch05-sylow.tex`)

- \(\binom{p^am}{p^a}\equiv m\pmod p\) — `lem:binom`, line 32. The binomial divisibility is V3-011.
- Sylow I, existence — `thm:sylow1`, line 87.
- Sylow II and III: conjugacy, \(n_p\equiv 1\pmod p\), \(n_p\mid m\) — `thm:sylow23`, line 121.
- A Sylow subgroup is normal iff it is unique — `cor:sylownormal`, line 187.
- A subgroup of every order \(p^k\) dividing \(\lvert G\rvert\) — `cor:pk`, line 213.
- No group of order 30 is simple — `prop:thirty`, line 259.
- Groups of order \(pq\) — `thm:pq`, line 309.
- Solvable group: a subnormal series with abelian factors — definition at line 417.
- Subgroups, quotients, and extensions preserve solvability; a non-abelian simple group is not solvable — `prop:solv`, line 435.
- \(A_5\) is the smallest non-abelian simple group, and the only simple group of order 60 — unboxed subsection at line 550.

### Chapter 6 — Rings and Ideals (`chapters/ch06-rings.tex`)

- Commutative ring with identity; domain; the examples, including \(\Z[\sqrt{-5}]\) — definition and `ex:rings`.
- A finite domain is a field — `prop:finitedomain`, line 47.
- Ideal, quotient ring, kernels of ring maps — `prop:quotring`, line 119.
- Prime and maximal ideals — `prop:primemax`, line 216.
- Chinese remainder theorem for rings — `thm:crtring`, line 292.
- \(6=2\cdot 3=(1+\sqrt{-5})(1-\sqrt{-5})\), four non-associate irreducibles — `prop:zm5`, line 372.
- In a UFD, irreducible iff prime — `lem:primeufd`, line 471. The unit-absorption sentence is V3-016.
- Euclidean implies PID implies UFD — `thm:edpidufd`, line 537. \(K[X]\) is Euclidean.
- A PID that is not Euclidean — `prop:pid-not-euclidean`, line 620.
- Field of fractions of a domain — prose at line 700. Distributivity is V3-015.
- Content, Gauss’s lemma — `lem:gauss`, line 747.
- Primitive polynomials, irreducibility over the fraction field — `prop:gaussirr`, line 771.
- \(R[X]\) is a UFD when \(R\) is — `thm:gaussufd`, line 829.
- Eisenstein and reduction for a general UFD, sketched after the theorem — V3-014.

### Chapter 7 — Modules over a PID (`chapters/ch07-modules.tex`)

- Module, submodule, quotient, homomorphism — definition at line 31, and `ex:modules`.
- Index of a nonzero ideal in \(\Z[i]\), by the norm — `thm:normindex`, line 75.
- Smith normal form over a PID — `thm:smith`, line 172. The pivot return is V3-018.
- A submodule of a finite-rank free module is free of rank at most that rank — `lem:subfree`, line 247.
- Structure theorem: invariant factors and elementary divisors — `thm:structure`, line 295. The symbol \(v_p\) is V3-019.
- Finitely generated abelian groups — `cor:abelian`, line 451.
- \([\Z^n:A\Z^n]=\lvert\det A\rvert\) when \(\det A\neq 0\) — `cor:index`, line 531.
- Presentation by a matrix — `prop:presentation`, line 591.
- Rational canonical form — `thm:frobenius`, line 702.
- Cayley–Hamilton, second proof — `cor:cayleyhamilton`, line 778. Volume 1 already has one proof.
- Jordan form when the characteristic polynomial splits — `thm:jordan`, line 829.

### Chapter 8 — Field Extensions (`chapters/ch08-extensions.tex`)

- Degree \([L:K]\), intermediate field — prose at line 21.
- Tower law — `thm:tower`, line 29.
- Degrees of intermediate steps divide; prime degree means no strict intermediate field — `cor:towerdiv`, line 70.
- Algebraic, transcendental, \(K[\alpha]\), \(K(\alpha)\) — prose at line 102.
- Minimal polynomial — `prop:minpoly`, line 119.
- \(K[X]/(m_\alpha)\cong K(\alpha)\) — `thm:simple`, line 176.
- Finite extensions are algebraic — `cor:finitealg`, line 242.
- Kronecker: a root of an irreducible as the class of \(X\) — `thm:kronecker`, line 321.
- Splitting field; existence, with degree at most \(n!\) — `prop:splitexists`, line 391.
- Extension of an isomorphism to one root — `lem:extend1`, line 445.
- Characteristic of a field — prose at line 503.
- An irreducible over a field of characteristic 0 has distinct roots — `lem:sep`, line 515.
- Uniqueness of splitting fields; the number of extensions equals the degree when the roots are distinct — `thm:splitunique`, line 577.
- Constructible number — prose at line 679. Not in Volume 1.
- Constructible numbers form a field closed under square roots — `prop:constrfield`, line 683. Addition is V3-020.
- Wantzel: quadratic tower iff constructible; a power of 2 is necessary — `thm:wantzel`, line 820.
- Classical problems: cube, trisection of \(60^\circ\), pentagon, prime-gon obstruction — `cor:classical`, line 937.
- A real number of degree 4 that is not constructible — `prop:quartic-nonconstructible`, line 1049.
- Primitive element for subfields of \(\C\) — `thm:primitiveelement`, line 1122. The gcd step is V3-002.

### Chapter 9 — Finite Fields (`chapters/ch09-finite-fields.tex`)

- A finite field has prime-power order — `prop:primefield`, line 25.
- Freshman’s dream and the Frobenius automorphism — `lem:frob`, line 73. This is the first main-text proof of \((a+b)^p=a^p+b^p\) in an arbitrary field of characteristic \(p\).
- The field of four elements — `ex:f4`, line 125.
- A finite subgroup of \(K^\times\) is cyclic — `thm:cyclicmult`, line 133. The root bound’s citation is V3-021.
- \(X^q-X=\prod_{a\in K}(X-a)\) — `lem:xqx`, line 219.
- Existence and uniqueness of \(\mathbb F_q\) — `thm:fq`, line 258.
- One subfield per divisor of the degree — `thm:subfields`, line 314.
- \(\mathrm{Aut}(\mathbb F_{p^n}/\mathbb F_p)=\langle\varphi\rangle\), cyclic of order \(n\) — `thm:galfq`, line 401. Here \(\varphi\) is Frobenius.
- \(X^{q^n}-X\) is the product of the monic irreducibles whose degree divides \(n\) — `thm:xqnx`, line 451. Two sentences are V3-022.
- \(N_q(n)\) by Möbius inversion, and \(N_q(n)\ge 1\) — `thm:countirr`, line 497.
- Hamming distance; Reed–Solomon distance at least \(n-k+1\) — `prop:rsdist`, line 594.
- Berlekamp–Welch — `thm:bw`, line 633.
- Trace, in the statement of `pb:mseq`. The square step is V3-023.

### Chapter 10 — Galois Theory (`chapters/ch10-galois.tex`)

- Galois group, fixed field, \(\lvert\mathrm{Gal}\rvert=[L:K]\) — `def:galois`, line 38.
- Automorphisms permute roots and embed into \(\mathfrak S_n\) when the roots generate the top field — `lem:permroots`, line 44.
- At most \([L:K]\) automorphisms — `prop:autbound`, line 78. Uses `thm:primitiveelement`.
- The four Galois criteria in characteristic 0 — `thm:galoischar`.
- Artin’s lemma — `lem:artin`, line as numbered 10.5.
- Fundamental theorem — `thm:ftgt`, line as numbered 10.6. The inclusion \(\sigma(M)\subseteq M\) is V3-027.
- \(K(\zeta_n)/K\) is Galois and the exponent map injects into \((\Z/n\Z)^\times\); for prime \(p\) it is an isomorphism onto a cyclic group — `prop:cyclo`.
- Gauss–Wantzel, forward direction: if \(\varphi(n)\) is a power of 2 then the regular \(n\)-gon is constructible — `thm:gw`. The converse uses `ex:phin` (V3-003).
- A cyclic Kummer extension is radical — `lem:kummerstep`.
- Solvable by radicals implies solvable Galois group — `thm:radsolv`.
- \(X^5-4X+2\) has Galois group \(\mathfrak S_5\), so it is not solvable by radicals — `thm:abelruffini`. The “every quintic” sentence is V3-028.
- Dedekind’s independence of characters — `lem:dedekind`.
- Kummer generator — `prop:kummer`.
- The converse criterion, and solvability in degrees at most 4 — `thm:galoiscrit`.
- \([\Q(\zeta_n):\Q]=\varphi(n)\) and \(\mathrm{Gal}(\Q(\zeta_n)/\Q)\cong(\Z/n\Z)^\times\) — solution of `ex:phin`, not a numbered theorem.

### Chapter 11 — Representations and Characters (`chapters/ch11-characters.tex`)

- Representation, degree, subrepresentation, irreducible, intertwiner — definition at line 31.
- Trivial representation, sign representation, permutation representation, regular representation — `ex:reps`.
- Hermitian inner product, complex Gram–Schmidt — prose at line 51. The induction step is shorter than Volume 1’s real case.
- Maschke — `thm:maschke`, line 76. The “second proof” is V3-029.
- Schur’s lemma — `lem:schur`.
- An irreducible representation of an abelian group has degree 1 — `cor:abelianirr`.
- Character, class function, inner product of class functions — definition at line 218.
- Degree, conjugacy, inverse, and the permutation character — `prop:charbasic`.
- Orthogonality of irreducible characters — `thm:orth`.
- Multiplicities; same character implies isomorphic; sum of squares of degrees equals \(\lvert G\rvert\) — `cor:mult`.
- Irreducible characters are a basis of the class functions; their number equals the number of classes — `thm:classes`.
- Column orthogonality — `cor:columns`.
- Character tables of \(\mathfrak S_3\) and \(\mathfrak S_4\), degrees \(1,1,2,3,3\) — `ex:s3`, `ex:s4`. The cube cycle types are V3-031.
- Fourier inversion and Parseval on a finite abelian group — `thm:fourier`.
- Dirichlet character modulo \(q\), redefined, and the orthogonality filter — `prop:dirichletorth`. Already in Volume 2.
- Algebraic integer, in `ex:divides`. Frobenius–Schur indicator, in `pb:frobschur`.

### Chapter 12 — Quaternions and Rotations (`chapters/ch12-quaternions.tex`)

- Quaternion algebra, conjugate, norm, pure quaternions — definition and `prop:quat`. The complex matrix model.
- Euler’s formula for a rotation, and the half-angle form — `lem:euler`.
- Double cover \(S^3\to SO(3)\), kernel \(\{\pm 1\}\) — `thm:su2so3`. Path lifting is written from Volume 1’s sequence tools.
- Finite subgroups of \(SO(3)\): cyclic, dihedral of order \(2n\ge 4\), or \(A_4\), \(\mathfrak S_4\), \(A_5\) — `thm:finiteso3`. The solid names are V3-004. The circle subgroup is V3-033.
- Binary tetrahedral and binary icosahedral groups — solutions of `ex:2T` and `ex:2I`.
- Hurwitz order and left Euclidean division — `ex:hurwitz`. The tools line is V3-032.
- \(\pi_1(SO(3))\cong\Z/2\Z\), defined in the text from the double cover. Not a citation of Volume 7.

### Appendix A — Positive Matrices (`chapters/linear-ch07-perron.tex`)

- Perron: a positive matrix has a simple positive eigenvalue equal to the spectral radius, with a positive eigenvector — `linear:thm:perron`.
- Oscillation lemma — `linear:lem:oscillation`.
- Convergence of the power method — `linear:thm:powerconv`.
- Irreducible, period, primitive — `linear:def:irreducible`.
- Cyclic levels of an irreducible nonnegative matrix — `linear:prop:levels`.
- Frobenius, 1912 — `linear:thm:frobenius`.
- The three conditions for a primitive matrix — `linear:thm:primitive`.
- Wielandt’s bound — `linear:thm:wielandt`.
- Ergodic theorem for a finite Markov chain — `linear:cor:markov`.
- PageRank — `linear:exa:pagerank`. Leslie models — `linear:exa:leslie`.

### Appendix B — Symmetry Diagonalises (`chapters/linear-ch09-symmetry.tex`)

- Eigenvalues of a circulant — `linear:thm:circulant`.
- The commutant of the cycle shift — `linear:prop:commutant`.
- Character of a finite abelian group, additive form — `linear:def:character`.
- A commuting family of diagonalisable matrices is simultaneously diagonalisable — `linear:lem:commuting`.
- The character group diagonalises the group algebra — `linear:thm:characters`.
- An abelian symmetry is diagonalisable — `linear:thm:invariant`.
- Paley graphs, strongly regular — `linear:thm:paley`.
- Krawtchouk polynomials — `linear:def:krawtchouk`. Distances in the cube — `linear:thm:krawtchouk`.
- Delsarte’s linear programming bound — `linear:thm:delsarte`. The corollary is `linear:cor:lp`. Plotkin — `linear:cor:plotkin`.
- Group determinant — `linear:thm:groupdet`.
- Plancherel for this normalisation, prose near line 1270. The double sum is V3-036.

### Appendix C — The Linear Algebra Method (`chapters/combinatorial.tex`)

- Oddtown — `combinatorial:thm:oddtown`. Orthogonal complement over \(\mathbb F_2\) — `combinatorial:lem:perp`.
- Eventown — `combinatorial:thm:eventown`.
- Fisher, non-uniform — `combinatorial:thm:fisher`.
- Two-distance sets — `combinatorial:thm:twodist`. Planar maximum — `combinatorial:prop:planarmax`.
- Frankl–Wilson, modular and non-uniform, and the explicit Ramsey graph — `combinatorial:thm:fwmod`, `combinatorial:thm:fw`, `combinatorial:thm:explicitramsey`.
- Grid vanishing — `combinatorial:lem:grid`. Combinatorial nullstellensatz — `combinatorial:thm:cn`.
- Cauchy–Davenport — `combinatorial:thm:cd`.
- Power sums — `combinatorial:lem:powersum`. Chevalley–Warning — `combinatorial:thm:cw`.
- Erdős–Ginzburg–Ziv — `combinatorial:thm:egz`.
- Cap set — `combinatorial:def:cap`. Slice rank — `combinatorial:def:slicerank`.
- A subspace has a heavy vector — `combinatorial:lem:support`. Tao’s diagonal lemma — `combinatorial:lem:diag`.
- Ellenberg–Gijswijt — `combinatorial:thm:capset`. The bound on \(M_n\) — `combinatorial:prop:mn`.

### Appendix D — Hadamard matrices (`chapters/paley.tex`)

- For \(n>2\), a Hadamard matrix of order \(n\) needs \(4\mid n\) — `prop:hadamard-four`.
- Sylvester’s doubling — `conjectures:prop:kron`.
- Quadratic character on \(\mathbb F_q\) — `conjectures:lem:chi`. Jacobsthal matrix — `conjectures:lem:jacobsthal`.
- Paley I and Paley II — `conjectures:thm:paley1`, `conjectures:thm:paley2`.

### Afterword (`chapters/afterword.tex`)

- No new theorem. The walk on \(\Z/2\Z\) gives \(\Pr(X_t=0)=(1+(1-2p)^t)/2\), from finite experiments and the transition matrix. The handoff names Volume 4, *Chance: The Logic of Uncertainty*.

### Notation clashes with Volumes 1 and 2, and inside Volume 3

- \(D_n\) is the number of derangements in Volume 1, and later the Dirichlet kernel. From `prop:dihedral` it is the full isometry group of a regular \(n\)-gon, order \(2n\), for \(n\ge 3\). Chapter 12 uses the same letters for a subgroup of \(SO(3)\), with half-turns in place of reflections, and defines \(D_2\) as the Klein group. The solution of `ex:2T` says so. The theorem statement does not.
- \(\varphi\) is the golden ratio in Volume 1, in the \(A_5\) table, and in the icosahedron. It is Euler’s totient from Volume 2, Chapter 3, and again in `ex:phin` and `ex:primpoly`. In `thm:galfq` it is the Frobenius automorphism.
- \(\chi\) is a Dirichlet character from Volume 2, Chapter 11. Chapter 11 uses it for a representation character, then redefines the Dirichlet character. Appendix B uses it for an additive character \(G\to\C^\times\). Appendix D uses it for the quadratic character on \(\mathbb F_q\). In the \(A_5\) solution, \(\chi_4\) and \(\chi_5\) are irreducible characters; in Volume 2, \(\chi_4\) is the non-principal character modulo 4. The figure writes \(\psi_3,\psi_4,\psi_5\) for the rows the solution calls \(\chi_3,\chi_4,\chi_5\).
- \(\pi(7)\) and \(\pi(11)\) in the solution of `pb:fibmodp` are Fibonacci periods, 16 and 10. From Volume 2, Chapter 2, \(\pi(x)\) is the prime-counting function.
- “Primitive element” is a generator of a finite extension of subfields of \(\C\) (`thm:primitiveelement`) and a generator of \(\mathbb F_q^\times\) (Chapter 9, line 186). The chapter distinguishes them. Volume 1 uses “primitive” for a root of unity, and Volume 2 uses “primitive root” for a generator of \((\Z/n\Z)^\times\).
- \(N\) is the quaternion norm, and also the order of a finite rotation group in the classification. In Volume 2 it is the field norm.
- \(\log\) in the shuffle sentence of Chapter 4, and in `pb:conjugate`, is the natural logarithm. Volumes 1 and 2 write \(\ln\).
- Appendix B’s Fourier transform has no factor \(1/\lvert G\rvert\) in the forward sum. Chapter 11 puts that factor in the forward transform. Both conventions are stated.
- \(K_n\) is the complete graph in Appendix B, and \(K_k(t)\) is a Krawtchouk polynomial. The second always has an argument.

## Volume 4

Book order: preface, then Chapters 1–14 as numbered by `main.tex`, then Appendix B (`\appendix` and `\setcounter{chapter}{1}` before the chapter, so there is no Appendix A). File paths are under `volume4-chance/`. Proofs are supposed to use Volume 1 and earlier chapters of this volume. The preface says no proof cites a theorem of Volume 2 or Volume 3. Starred environments do not take a number. The shared counter is theorem, proposition, lemma, corollary, definition, example.

### Preface (`chapters/preface.tex`)

- No new theorem. Finite fair-coin strings, and \(P(n\text{ tails})=2^{-n}\). The infinite string is postponed to Chapter 1.

### Chapter 1 — From Games to Probability Spaces (`chapters/ch01-counting.tex`)

- Uniform on \([0,1)\): an interval \([c,d)\) has probability \(d-c\) — `def:uniform`, Definition 1.1.
- Binary digits by doubling, dyadic convention ending in zeros — prose at line 45.
- Digits are fair and mutually independent — `prop:bits`, Proposition 1.2.
- Finite-bit event: a finite union of those cylinders — prose at line 80.
- Outer content \(P^*\); almost surely means the exceptional set has outer content 0 — `def:outer`, Definition 1.3.
- Countable subadditivity of outer content — `prop:subadd`, Proposition 1.4.
- Dyadic outer content equals length; a countable set of points has outer content 0 — unnumbered `lemmax` after line 101.
- Infinitely many digits equal to 0 and to 1, almost surely — `prop:infdigits`, Proposition 1.6.
- First-head time \(T\), with \(P(T=k)=2^{-k}\) and \(\mathbb E[T]=2\) — prose at line 147.
- Ballot theorem: strict lead throughout has probability \((a-b)/(a+b)\) — `thm:ballot`, Theorem 1.7.
- Conditional sample spaces: at least one boy (\(1/3\)); at least one boy born on Tuesday (\(13/27\)); the \(n\)-door host — prose at line 200.
- Catalan count \(C_n=\binom{2n}{n}/(n+1)\) from the ballot theorem — solution of `ex:catalan`.
- Secretary thresholds, \(p_r\to 1/e\) along \(r/n\to 1/e\), for this family of strategies — solution of `ex:secretary`.

### Chapter 2 — Random Variables and Their Laws (`chapters/ch02-discrete.tex`)

- Law on a countable space; absolute convergence permits rearranging \(\mathbb E[X]=\sum x\,P(X=x)\) — prose at line 25.
- Variance when \(\mathbb E[X^2]<\infty\), and covariance — unnumbered `definitionx` at line 51, and prose at line 61. The factor 2 in the monotone case is V4-013.
- Poisson limit of binomial laws, for each fixed \(k\) — `thm:poissonlimit`, Theorem 2.1.
- If \(np_n\to 0\), the count tends to the point mass at 0 — prose at line 110.
- Integral bounds on \(-\ln(1-x)\) — `ex:rare`, Example 2.2.
- Fixed-point counts tend to Poisson\((1)\) — `prop:fixedpoisson`, Proposition 2.3.
- \(\mathbb E[X_k]=1/k\) and \(\mathbb E[C_n]=H_n\) — `prop:cycles`, Proposition 2.4.
- Coupon collector \(\mathbb E[T]=nH_n\sim n\ln n\) — `thm:coupon`, Theorem 2.5.
- Geometric variance \((1-p)/p^2\) — `lem:geovar`, Lemma 2.6.
- Coupon stages are independent and \(\operatorname{Var}T=n^2\sum k^{-2}-nH_n<2n^2\) — `prop:couponvar`, Proposition 2.7.
- Empty boxes after \(m\) throws — `prop:empty`, Proposition 2.8.
- Records have mean \(H_n\) — solution of `ex:records`. Long-cycle probability \(H_{2n}-H_n\to\ln 2\) — solution of `ex:prisoners`.

### Chapter 3 — Generating Functions and Random Families (`chapters/ch03-generating.tex`)

- Probability generating function \(f(s)=\mathbb E[s^X]\) on \([0,1]\), with \(0^0=1\) — prose at line 33.
- \(p_k=f^{(k)}(0)/k!\) — `prop:pgfcoeff`, Proposition 3.1.
- \(\lim_{s\uparrow 1}f'(s)=\mathbb E[X]\in[0,\infty]\) — `prop:pgfmean`, Proposition 3.2.
- Variance from \(f''(1)\) when both derivatives are finite — `prop:pgfvar`, Proposition 3.3.
- PGFs of the Bernoulli, binomial, and Poisson laws — `ex:pgfexamples`, Example 3.4.
- PGF of an independent sum is the product — `prop:pgfsum`, Proposition 3.5.
- Random sum, PGF \(g(f(s))\), on finite records — `prop:randomsum`, Proposition 3.6.
- Generation means \(\mathbb E[Z_n]=m^n\) — `prop:genmean`, Proposition 3.7.
- Extinction probability is the smallest root of \(s=f(s)\) in \([0,1]\) — `thm:extinction`, Theorem 3.8. The events \(D_j\) in that proof are first-extinction generations, not derangement counts.
- Dyck generating function \(c(x)=(1-\sqrt{1-4x})/(2x)\) — prose at line 296. The count is Chapter 1’s `ex:catalan`.
- \(\sum\binom{2n}{n}x^n=(1-4x)^{-1/2}\) for \(|x|<1/4\) — solution of `ex:binseries`.

### Chapter 4 — Concentration and the Laws of Large Numbers (`chapters/ch04-inequalities.tex`)

- Convergence in probability, as the name of the weak-law limit — line 16.
- Hoeffding’s lemma — `lem:hoeffding`, Lemma 4.1. Hoeffding’s inequality — `thm:hoeffding`, Theorem 4.2.
- Kolmogorov’s inequality — `thm:kolmogorov`, Theorem 4.3.
- Borel–Cantelli, both halves, for finite unions of digit intervals — `thm:bc`, Theorem 4.4.
- Strong law for bounded variables — `thm:sllnbound`, Theorem 4.5.
- Bernstein polynomials, and Weierstrass on \([0,1]\) — `thm:weierstrass`, Theorem 4.6.

### Chapter 5 — Continuous Chance (`chapters/ch05-continuous.tex`, with `ch05-geometric.tex`)

- Distribution function \(F(x)=P(X\le x)\) — line 20. Density — `def:density`.
- Standard normal density \(\phi\), mean 0, variance 1, and the Gaussian tail — `prop:gausstail`.
- Expectation of a continuous function of a density — `prop:densitymean`.
- Exponential law as \(-\ln U\) — line 129.
- Continuous Fubini on a compact rectangle — `prop:fubini`. Plane uniform continuity is V4-014.
- Disk integral by cutoffs, and the polar-rectangle identity — `prop:polar`. The identity is V4-002.
- Independent uniforms from one bit string — `prop:manyuniforms`.
- Joint density of \((\min,\max)\) of two uniforms — `prop:orderpair`.
- Inverse of a continuous strictly increasing distribution function, and the generalised inverse — `prop:inverse` and the prose at line 295.
- Dominated convergence for continuous integrands — `thm:dct`.
- Box–Muller — `thm:boxmuller`, Theorem 5.10. The change of variables is V4-002.
- Bertrand’s three chord models, probabilities \(1/3\), \(1/2\), \(1/4\) — `thm:bertrand`. The inner-disk area sentence is V4-015.
- Buffon’s needle, probability \(2\ell/(\pi d)\) for \(\ell\le d\) — `thm:buffon`, Theorem 5.12.

### Chapter 6 — Why the Bell Curve Appears (`chapters/ch06-clt.tex`)

- Almost-sure convergence, convergence in probability, convergence in distribution — `def:modes`, Definition 6.1.
- Comparisons of the three modes — `prop:modes`, Proposition 6.2. The open-set decomposition is V4-003.
- Expectations of bounded uniformly continuous test functions, as grid sums — `prop:cdf`, Proposition 6.3. Countable jumps are V4-016.
- Product of independent bounded monotone factors, at most four in the statement; the proof’s finite-\(r\) identity is the one used later — unnumbered `prop:indepproduct`.
- Strong law under a fourth moment — `thm:slln4`, Theorem 6.4.
- Glivenko–Cantelli — `thm:gc`, Theorem 6.5.
- Characteristic function — sentence label `def:charfn`, before Theorem 6.8. Not a numbered definition.
- Differentiation under the integral — `lem:diffint`, Lemma 6.6.
- Characteristic functions of the coin, the normal, and a density — `prop:cfexamples`, Proposition 6.7.
- Convergence in distribution passes to characteristic functions — unnumbered `thm:cfconv`.
- Uniqueness and inversion — `thm:inversion`, Theorem 6.8. The indicator comparison is V4-004. The smoothing sentence is V4-017.
- Sum of independent normals — `lem:normalsum`, Lemma 6.9.
- Lindeberg, smooth-test form — `thm:lindeberg`, Theorem 6.10.
- Classical central limit theorem — `cor:clt`, Corollary 6.11.
- Local de Moivre–Laplace — `thm:local`, Theorem 6.12.
- Cycle count as a sum of independent Bernoulli summands — `prop:cyclebern`, Proposition 6.13.
- Gaussian vectors — `thm:gaussvec`, Theorem 6.14. The rotation step is V4-005.

### Chapter 7 — Entropy, Codes and Typical Sequences (`chapters/ch07-entropy.tex`)

- Surprise and Shannon entropy \(H(X)\) — opening section.
- Gibbs: \(H(X)\le\log_2 m\) — `prop:gibbs`, Proposition 7.1.
- Typical set — `thm:aep`, Theorem 7.2.
- Kraft — `thm:kraft`, Theorem 7.3. Shannon’s code — `thm:shannon`, Theorem 7.4.
- Chain rule — `prop:chain`, Proposition 7.5.
- Relative entropy — `thm:kl`, Theorem 7.6. Mutual information — `thm:mutual`, Theorem 7.7.
- Huffman merge — `thm:huffman`, Theorem 7.8. The tie-break slogan in the example is V4-019.
- Block Shannon code \(H\le L_n/n<H+1/n\) — prose in “Coding long blocks”.

### Chapter 8 — Random Walks (`chapters/ch07-walks.tex`)

- Simple symmetric random walk on \(\Z\), from fair bits — opening.
- Reflection — `thm:rwreflect`, Theorem 8.1.
- Gambler’s ruin — `thm:ruin`, Theorem 8.2. Duration — `prop:duration`, Proposition 8.3.
- Expected number of visits — `prop:visits`, Proposition 8.4.
- Pólya: recurrent in dimensions 1 and 2, transient for \(d\ge 3\) — `thm:polya`, Theorem 8.5. The comparison sentence is V4-018.
- Last visit and the discrete arcsine law — `thm:arcsine`, Theorem 8.6.
- Harmonic hitting probabilities — `prop:harmonic`, Proposition 8.7.
- Arcsine limit — `thm:arcsinelimit`, Theorem 8.8.
- Central binomial lower bound — `lem:centralbin`, Lemma 8.9.
- Papadimitriou: expected time at most \(n^2\) on a satisfiable 2-SAT formula — `thm:twosat`, Theorem 8.10.

### Chapter 9 — Markov Chains and Mixing (`chapters/ch08-markov.tex`)

- Finite transition matrix and the chain, from independent uniforms — opening.
- One period on an irreducible chain — `lem:period`, Lemma 9.1.
- A stationary distribution exists, and is unique if the chain is irreducible — `thm:stationary`, Theorem 9.2. Proved here. Not a citation of Volume 3.
- Total variation, and the coupling inequality — `lem:coupling`, Lemma 9.3.
- Convergence for irreducible aperiodic finite chains — `thm:ergodic`, Theorem 9.4.
- Top-to-random: uniform at time \(\tau\), with \(\mathbb E[\tau]=nH_n\) and distance at most \(e^{-c}\) — `thm:top`, Theorem 9.6.
- Total variation does not increase — `lem:tvcontract`, Lemma 9.7.
- \(a\)-shuffle — `def:ashuffle`, Definition 9.8.
- Bayer–Diaconis formula — `thm:bayerdiaconis`, Theorem 9.9. The bijection is V4-007.
- An \(a\)-shuffle followed by a \(b\)-shuffle is an \(ab\)-shuffle — `prop:rifflecompose`, Proposition 9.10. The inverse model is V4-008.
- Random-transposition lower bound — `prop:untouched`, Proposition 9.11. The matching upper bound is Volume 11, not a premise.

### Chapter 10 — The Poisson Clock (`chapters/ch09-poisson.tex`)

- Memorylessness — `prop:memoryless`, Proposition 10.1.
- Joint density of partial sums of exponentials — `lem:gamma`. The passage to region probabilities is V4-009.
- Poisson process — `def:pp`, Definition 10.3.
- Counts are Poisson, and conditional uniformity — `thm:uniform`.
- Independent colouring of a Poisson number of points — `lem:colouring`.
- Independent increments — `thm:increments`. Thinning — `thm:thinning`. Superposition — `thm:superpose`.
- Residual life, the one-sided gap, and two competing clocks — `prop:residual`, `prop:onesidedgap`, `prop:race`.
- Le Cam’s inequality — `thm:lecam`.
- M/M/1 stationary distribution when \(\lambda<\mu\) — `thm:mm1`.

### Chapter 11 — Martingales and Fair Games (`chapters/ch10-martingales.tex`)

- Conditional expectation on a finite partition — `def:condexp`.
- Martingale — `def:mart`, Definition 11.2. Stopping time — `def:stopping`.
- Optional stopping at a bounded time — `thm:os`, Theorem 11.4.
- Two further sufficient conditions — `thm:os2`, Theorem 11.5.
- Upcrossings — `thm:upcross`.
- Orthogonal increments and the square-mean Cauchy criterion — `prop:orthinc`, `prop:l2cauchy`.
- Doob’s \(L^2\) inequality — `thm:doob`. Azuma — `thm:azuma`.
- Waiting time for a word — `thm:monkey`.
- \(L^2\) convergence — `thm:L2conv`, Theorem 11.12.
- Pólya’s urn — `thm:polyaurn`, Theorem 11.13.
- Almost-sure convergence — `thm:asconv`.

### Chapter 12 — Brownian Motion (`chapters/ch11-brownian.tex`)

- Brownian motion: continuous paths, independent Gaussian increments — `def:bm`, Definition 12.1.
- Covariance \(\min(s,t)\) when the finite-dimensional distributions are centred Gaussian — `prop:bmgauss`.
- Dyadic increments — `lem:levylevel`, Lemma 12.3.
- Existence on \([0,1]\) by piecewise-linear interpolation, then on \([0,\infty)\) by independent copies — `thm:levy`, Theorem 12.4. Second moments and indicator events are V4-010.
- Scaling — `prop:scaling`. Quadratic variation — `thm:qv`.
- Dyadic expansion, not an Itô integral — `thm:dyadicito`.
- Nowhere differentiable — `thm:pwz`.
- Finite-observation martingale identity — `prop:bmmart`.
- Restart at a hitting time — `prop:restart`. The monotone-limit sentence is V4-010.
- Reflection — `thm:reflection`, Theorem 12.12.
- Square martingale at finitely many observation times — `prop:bmsquare`. The unbounded product is V4-010.

### Chapter 13 — The Probabilistic Method (`chapters/ch12-method.tex`)

- A mean below 1 forces a colouring with no monochromatic \(K_k\); \(R(k,k)>2^{k/2}\) — `thm:erdos`, Theorem 13.1. The symbol is V4-020.
- Alteration — `thm:alter`, Theorem 13.2.
- Symmetric local lemma — `thm:lll`, Theorem 13.3.
- Second-moment bound — `prop:second`, Proposition 13.4.
- Euler’s formula and \(e\le 3v-6\) — `prop:euler`, Proposition 13.5. The proof is V4-001.
- Crossing number \(\operatorname{cr}(G)\ge m-3n\), and \(m^3/(64n^2)\) when \(m\ge 4n\) — `prop:crossing`, Proposition 13.6. The deletion half is V4-001. The sampling half is complete once that bound is granted.

### Chapter 14 — Random Graphs and the Search for Structure (`chapters/ch14-graphs.tex`)

- \(G(n,p)\), independent edges — opening.
- Subcritical components are \(O(\log n)\) with high probability — `thm:subcrit`, Theorem 14.1. The exploration is the proof. The Prüfer count is V4-021. No supercritical giant-component theorem.
- Triangles at \(p=c/n\) — `thm:triangles`, Theorem 14.2.
- One vertex has a linear component with probability bounded below, for \(c>1\) — solution of `ex:giant`. Not a high-probability claim.
- Handoff to Volume 5, *Calculation: From Formula to Insight* — last paragraph. No new theorem.

### Appendix B — Extremal Problems and Ramsey Theory (`chapters/extremal.tex`)

- Turán — `thm:turan`, Theorem B.1.
- Ramsey numbers \(R(s,t)\), with \(R(3,3)=6\) — `thm:ramsey`, Theorem B.2. The symbol was already used in Chapter 13 (V4-020).
- Schur — `thm:schur`, Theorem B.3.
- Sunflower — `thm:sunflower`, Theorem B.4.
- Erdős–Ko–Rado — `thm:ekr`, Theorem B.5.
- Two colours, arithmetic progression of length three, on \(\{1,\ldots,9\}\) and not on \(\{1,\ldots,8\}\) — `thm:vdw3`, Theorem B.6.
- Van der Waerden — `thm:vdw`, Theorem B.7. The stretch is V4-011. The passage to arbitrarily long progressions in a finite colouring of the positive integers is complete.

### Notation clashes with Volumes 1–3, and inside Volume 4

- \(\pi\) is the circle constant from Volume 1. In Chapter 2 it is also a permutation, written \(\pi(k)\). Volume 2 uses \(\pi(x)\) for the prime-counting function. From Chapter 9, \(\pi\) is a stationary distribution.
- \(D_n\) in Chapter 2 is the derangement count, as in Volume 1. Volume 3 uses \(D_n\) for the dihedral group. Inside the extinction proof, \(D_j\) is the event that extinction occurs first at generation \(j\).
- \(H(X)\) is Shannon entropy from Chapter 7. \(H_n\) remains the harmonic number.
- \(\phi\) is the standard normal density from Chapter 5. In the Chernoff example it is a local exponent. In the \(d\ge 3\) half of Pólya’s theorem it is the step average \(\phi(\theta)=d^{-1}\sum_j\cos\theta_j\). Volume 1 uses \(\varphi\) for the golden ratio. Volumes 2 and 3 use \(\varphi(n)\) for Euler’s totient.
- \(\Phi(x)=\int_{-\infty}^x\phi\) is the standard normal distribution function. Volume 1 and Volume 3 use \(\Phi_n\) for the cyclotomic polynomial.
- \(\chi_\eta\) is a radial cutoff in `prop:polar`. Volume 2 uses \(\chi\) for a Dirichlet character.
- \(D(p\|q)\) is relative entropy from Theorem 7.6. The same letter is a sum of squared ranges in Hoeffding’s proof, and a chord distance in Bertrand’s paradox. Volume 1’s \(D_n\) does not appear as a derangement count after Chapter 2.
- \(\log\) in the subcritical theorem is \(A\log n\); the proof writes \(\ln\). Entropy writes \(\log_2\). Any fixed base is absorbed into \(A(c)\).
- \(K_n\) in Goodman’s exercise is the complete graph, as in Volume 3, Appendix B. It is not a Krawtchouk polynomial.
- \(N(t)\) is the Poisson counting process. \(N(0,h)\) is a normal law of variance \(h\).
- In Chapter 13 the letter \(e\) is the base of the exponential in the local lemma and, two sections later, the number of edges in Euler’s formula.
- \(f\) is the probability of ever returning, in Chapter 8; the number of faces, in Euler’s formula; and the focus of a progression, in Appendix B. They are not in the same argument.

## Volume 5

Book order: preface, then Chapters 1–13. File paths are under `volume5-calculation/`. `chapters/bbp-borwein.tex` is part of Chapter 4. `chapters/hardy-ramanujan.tex` is Chapter 12. `chapters/ch12-agm.tex` is Chapter 13. The shared counter restarts each chapter. Bernoulli numbers use \(B_1=-\frac12\). On the line, \(\hat f(\xi)=\int f(x)e^{-2\pi ix\xi}\,dx\). The DFT is \(\hat a_j=\sum_k a_k\omega^{-jk}\) with inversion divided by \(n\).

### Preface (`chapters/preface.tex`)

- The Gaussian integral equals \(\sqrt\pi\), the full-line value. Chapter 4 proves the half-line \(\sqrt\pi/2\).
- \(\zeta(-1)=-\frac1{12}\) in the sense of the functional equation. Proved in Chapter 10.
- Admitted, and not used by a theorem: Tonelli (Volume 7, Theorem 9.5) in two exercises; convex volume (Volume 7, Theorem 7.11) in one Chapter 6 exercise; Fulton–Harris, Proposition 3.12, in one Chapter 5 exercise; Mertens’s third theorem (Volume 6, Chapter 1) in one Chapter 13 problem; the prime-number theorem (Volume 6, Chapter 5) in one solution, for comparison. The quoted Rademacher theorem is not in this list. See V5-010.

### Chapter 1 — Finite Calculus (`chapters/ch01-finite.tex`)

- Difference \(\Delta F(x)=F(x+1)-F(x)\), falling power \(x^{\underline m}\), and \(\Delta x^{\underline m}=m x^{\underline{m-1}}\) — `def` and `prop:falling`, 1.4.
- Fundamental theorem of the sum: \(\sum_{a\le k<b}\Delta F=F(b)-F(a)\) — `thm:ftfc`, 1.2.
- Summation by parts — `prop:parts`, 1.5. Abel summation — `prop:abel`, 1.7. Dirichlet’s test — `thm:dirichlet`, 1.8.
- \(\sum_{k=1}^n\sin kx=\sin\frac{nx}2\sin\frac{(n+1)x}2\big/\sin\frac x2\), and the series \(\sum\sin(kx)/k\) — `prop:sinsum`, 1.9. The absolute-convergence sentence is V5-001.
- Stirling numbers of both kinds and the change of basis — `thm:stirlingrec`, 1.11, and `thm:change`, 1.12.
- Bernoulli numbers from \(t/(e^t-1)=\sum B_n t^n/n!\), with \(B_1=-\frac12\), and \(B_n=0\) for odd \(n\ge3\) — `prop:bernoulli`, 1.14. The radius sentence is V5-002.
- Bernoulli polynomials \(B_n(x)\), with \(B_n(0)=B_n\) and \(\Delta B_n(x)=n x^{n-1}\). Then \(B_1(1)=\frac12\).
- Faulhaber: \(\sum_{k<n}k^p=(B_{p+1}(n)-B_{p+1})/(p+1)\) — `thm:faulhaber`, 1.15.
- Newton’s divided-difference series — `thm:newton`, 1.16.
- The sum of the first thousand tenth powers is \(91409924241424243424241924242500\).

### Chapter 2 — Generating Functions (`chapters/ch02-generating.tex`)

- Ordinary generating function \(\sum a_n x^n\) and exponential generating function \(\sum a_n x^n/n!\).
- The ring \(\C[[x]]\), and \(\C[x]\) as a Euclidean domain, from Volume 3, Chapter 6.
- Exponential formula for sets of labelled components — `thm:expformula`.
- Pentagonal-number theorem: \(\prod_{k\ge1}(1-x^k)=\sum_{j\in\Z}(-1)^j x^{j(3j-1)/2}\) — `thm:pentagonal`.
- Partition function \(p(n)\), with \(p(200)=3972999029388\).
- Quicksort: \(C_n=2(n+1)H_n-4n\) — `ex:quicksortexact`.
- Alternating permutations, \(A_n\), with generating function \(\sec z+\tan z\). The pole form is Chapter 9.
- Motzkin numbers, involutions \(t_n\), connected graphs, and the coin-change count \(4563\).

### Chapter 3 — Classic Series and Products (`chapters/ch03-series.tex`)

- Infinite products: \(\sum\log(1+a_n)\) for \(a_n>-1\) — `prop:products`. The sine product cites it past that hypothesis. See V5-003.
- \(\pi\cot\pi x=1/x+\sum_{n\ge1}2x/(x^2-n^2)\) on \((0,1)\), by Herglotz — `thm:cot`.
- \(\sin\pi x=\pi x\prod_{n\ge1}(1-x^2/n^2)\) — `thm:sineproduct`.
- Wallis’s product — `cor:wallis`. Viète’s product.
- \(\zeta(2k)=(-1)^{k+1}B_{2k}(2\pi)^{2k}/(2(2k)!)\) — `thm:zeta2k`. Values \(\pi^2/6\), \(\pi^4/90\), \(\pi^6/945\), \(\pi^8/9450\).
- \(\pi^2\) is irrational — Niven’s argument.
- Six proofs of \(\zeta(2)=\pi^2/6\) are named: Volume 1, Exercise 6.7; this chapter; Ritelli in the exercises, which admits Tonelli; two Fourier proofs in Chapter 6; the residue corollary in Chapter 9.

### Chapter 4 — Integration (`chapters/ch04-integrals.tex`, `chapters/bbp-borwein.tex`)

- Parameter dependence on a compact set — `thm:paramcompact`, 4.1.
- Fubini for a continuous function on a rectangle.
- Dominated convergence for continuous functions — `cor:dct`.
- \(\int_0^\infty e^{-x^2}\,dx=\sqrt\pi/2\).
- Frullani, \(\int_0^\pi\log\sin\theta\,d\theta=-(\pi/2)\log 2\), and the Dirichlet integral \(\pi/2\).
- BBP: the hexadecimal digits of \(\pi\) from a series of rational integrals — `thm:bbp`, 4.12. Not in the index. See V5-006.
- The Borwein identity and its deficit — 4.14 and 4.15. Not in the index.
- Fresnel integrals \(\int_0^\infty\cos(x^2)\,dx=\int_0^\infty\sin(x^2)\,dx=\frac12\sqrt{\pi/2}\).
- Golomb–Dickman constant \(\approx0.62433\). Its exercise is graded `[Journey]`. See V5-005.
- Two exercises admit Tonelli: Ritelli, and Sondow. Both name Volume 7, Theorem 9.5.

### Chapter 5 — Gamma and Beta (`chapters/ch05-gamma.tex`)

- \(\Gamma(x)=\int_0^\infty t^{x-1}e^{-t}\,dt\) for \(x>0\), with \(\Gamma(x+1)=x\Gamma(x)\) and \(\Gamma(n+1)=n!\).
- Bohr–Mollerup: log-convexity and \(\Gamma(1)=1\) pick out \(\Gamma\) — `thm:bohrmollerup`.
- Gauss’s product and the Weierstrass product.
- Stirling’s formula for real \(x\), from Volume 1, Theorem `thm:stirling`, with the constant \(\sqrt{2\pi}\).
- Beta function \(B(x,y)=\Gamma(x)\Gamma(y)/\Gamma(x+y)\) — `thm:betagamma`.
- \(\Gamma(\frac12)=\sqrt\pi\), the reflection formula \(\Gamma(z)\Gamma(1-z)=\pi/\sin\pi z\), and the duplication formula — `thm:reflection`, `thm:duplication`.
- Volume of the unit ball in dimension \(n\). In particular \(V_5=8\pi^2/15\).
- Digamma exercise `ex:digamma`: \(\Gamma'(1)=-\gamma\). Used in Chapter 13.
- One exercise quotes Fulton–Harris, Proposition 3.12, and is labelled quoted.

### Chapter 6 — Fourier Series (`chapters/ch06-fourier.tex`)

- Coefficients \(c_n(f)=\frac1{2\pi}\int_{-\pi}^\pi f(t)e^{-int}\,dt\), on the circle of length \(2\pi\).
- Dirichlet kernel and the convergence theorem for a piecewise \(C^1\) function — `thm:dirichletfourier`.
- Fejér means and Fejér’s theorem — `cor:fejer`. The kernel is `lem:fejerkernel`.
- Parseval — `thm:parseval`.
- Gibbs constant \((2/\pi)\operatorname{Si}(\pi)\approx1.17898\).
- Weyl’s equidistribution criterion.
- Inversion on \(\Z^d\).
- Hurwitz: \(4\pi A\le L^2\), with the shoelace formula as the definition of area.
- One exercise admits the volume of a convex body, Volume 7, Theorem 7.11, and is labelled admitted.

### Chapter 7 — The DFT and the FFT (`chapters/ch07-fft.tex`)

- \(\omega=e^{2\pi i/n}\), \(\hat a_j=\sum_{k=0}^{n-1}a_k\omega^{-jk}\), and inversion divides by \(n\).
- Convolution theorem — `thm:convolution`, 7.6.
- FFT operation counts, and the prime \(998244353=119\cdot2^{23}+1\) with primitive root \(3\).
- Gauss sums on \(\Z/n\Z\), used again in Chapter 8.
- Discrete cosine transform — `prop:dct`, 7.12. The index calls this line the convolution theorem. See V5-007.

### Chapter 8 — The Fourier Transform (`chapters/ch08-transform.tex`)

- Unitary convention \(\hat f(\xi)=\int_{\R}f(x)e^{-2\pi ix\xi}\,dx\). Volume 15 cites Theorem 8.6 in this convention.
- \(e^{-\pi x^2}\) is its own transform, and \(\int e^{-\pi x^2}\,dx=1\) — `thm:gaussianft`, 8.3.
- Inversion and Plancherel — `thm:ftinversion`, 8.6, and `thm:plancherel`, 8.7.
- Heat kernel on the line — `prop:heatline`, 8.8.
- Poisson summation — `thm:poisson`, 8.9. Jacobi’s theta \(\vartheta(t)=\sum_{n\in\Z}e^{-\pi n^2 t}\), with \(\vartheta(1/t)=\sqrt t\,\vartheta(t)\) — `cor:theta`, 8.10. The book keeps \(\vartheta\) for this series.
- \(\sum_{n\in\Z}1/(x+n)^2=\pi^2/\sin^2(\pi x)\), and the second proof of the cotangent expansion — Corollary 8.12. The index line is V5-009.
- Fresnel evaluation and the sign of the Gauss sum \(G(n)\) — `lem:fresnel`, 8.13, and `thm:gausssign`, 8.14. For a prime, \(G(p)=\sqrt p\) if \(p\equiv1\pmod4\) and \(i\sqrt p\) if \(p\equiv3\pmod4\).
- Shannon sampling at rate \(2W\) — `thm:shannon`, 8.15.
- Heisenberg, with equality for \(e^{-\pi x^2}\) — `thm:heisenberg`, 8.16.
- The opening digit count for \(\sum e^{-\pi n^2/100}\) says 135 places. The excess is \(7.3\times10^{-136}\). See V5-008.

### Chapter 9 — Complex Analysis (`chapters/ch09-complex.tex`)

- Holomorphic, entire, and the Cauchy–Riemann equations — `prop:cr`, 9.2.
- Goursat, including one exceptional point — `thm:goursat`, 9.7, and `cor:goursatpoint`, 9.8.
- Cauchy’s theorem on a star-shaped set — `thm:cauchy`, 9.9. The homology form is named as Volume 8, Chapter 14, and is not used.
- Cauchy’s integral formula, holomorphic implies analytic, and Cauchy’s estimates — 9.10, 9.11, 9.12.
- Morera, Liouville, the fundamental theorem of algebra, the identity theorem, the maximum principle, and removable singularities — 9.14 through 9.20.
- Laurent series and the residue — 9.22 and the definition 9.23.
- Winding number of the positive boundary of a bounded convex set is \(1\) — `prop:winding`, 9.25.
- Residue theorem on such a boundary — `thm:residue`, 9.26.
- \(\int_{-\infty}^\infty dx/(1+x^4)=\pi/\sqrt2\). The transform of \(1/(1+x^2)\) is \(\pi e^{-2\pi|\xi|}\).
- Reflection formula again, from a rectangle, without the sine product.
- \(\pi\cot\pi z\) has residue \(1\) at the integers, and \(|\cot\pi z|\le\coth(\pi/2)<2\) on the squares \(C_N\) — `lem:cotbound`, 9.32.
- Sums by residues — `thm:residuesum`, 9.33. Basel, the sixth proof — `cor:baselres`, 9.34. Partial fractions on \(\C\) — `cor:cotc`, 9.35.
- \(\Gamma\) on \(\operatorname{Re}z>0\), with \(|\Gamma(z)|\le\Gamma(\operatorname{Re}z)\), extended with simple poles of residue \((-1)^n/n!\) at \(-n\), and no zeros — `thm:gammac`, 9.36.
- Argument principle and Rouché — `thm:argument`, 9.37, and `thm:rouche`, 9.38.
- Dedekind sums \(s(h,k)\) and the reciprocity law. The exercise is graded `[Journey]`. See V5-005. The same sums reappear in Rademacher’s formula.

### Chapter 10 — The Zeta Function (`chapters/ch10-zeta.tex`)

- Dirichlet series, convolution of coefficients, and uniqueness — `prop:dirseries`, 10.1, and `prop:dirmult`, 10.2.
- Euler product for a multiplicative function, and \(\zeta(s)=\prod_p(1-p^{-s})^{-1}\) for \(\operatorname{Re}s>1\) — `thm:eulerproduct`, 10.3.
- \(\sum\mu(n)n^{-s}=1/\zeta(s)\) and \(\sum\varphi(n)n^{-s}=\zeta(s-1)/\zeta(s)\) — `cor:mobius`, 10.4. So \(\zeta(s)\ne0\) for \(\operatorname{Re}s>1\).
- \(\sum_p 1/p=\infty\) — `cor:primesdiverge`, 10.5.
- \(\zeta(s)-1/(s-1)\) is holomorphic for \(\operatorname{Re}s>0\), with value \(\gamma\) at \(s=1\) — `prop:zetastrip`, 10.6.
- Mellin transform of the Gaussian — `lem:mellingauss`, 10.7. Write \(\omega(t)=(\vartheta(t)-1)/2\).
- Completed function \(\xi(s)=\frac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)\), entire, and \(\xi(1-s)=\xi(s)\) — `thm:functional`, 10.8.
- Continuation of \(\zeta\) to \(\C\setminus\{1\}\), simple pole of residue \(1\), \(\zeta(0)=-\frac12\), trivial zeros at \(-2,-4,\ldots\), and the asymmetric equation \(\zeta(1-s)=2(2\pi)^{-s}\cos(\pi s/2)\Gamma(s)\zeta(s)\) — `cor:zetaplane`, 10.9.
- \(\zeta(1-2k)=-B_{2k}/(2k)\) — `thm:zetaneg`, 10.10. Thus \(-\frac1{12}\), \(\frac1{120}\), \(-\frac1{252}\), \(\frac1{240}\).
- Smoothed sums \(\sum n^k e^{-n/N}=k!\,N^{k+1}+(-1)^k B_{k+1}/(k+1)+O(1/N)\) — `prop:smoothed`, 10.11.
- Hardy's function \(Z(t)\) is real on the critical line. The phase is called \(\alpha\), so that \(\theta\) stays free for Chebyshev and \(\vartheta\) for Jacobi.
- The ordinates \(14.13,21.02,25.01,30.42,32.94,37.59,40.92,43.33,48.01,49.77\) are computed values, rounded to two decimals. The Riemann hypothesis is stated as open. Gourdon’s \(10^{13}\) zeros and the Platt–Trudgian check to height \(3\cdot10^{12}\) are cited as computations.
- Gauss–Kuzmin: the invariant density \(1/((1+t)\log 2)\) and the contraction \(2\zeta(3)-\frac32\). The exercise is graded `[Journey]`. See V5-005.
- Lévy’s constant \(\pi^2/(12\log 2)=1.18657\ldots\).

### Chapter 11 — Asymptotics (`chapters/ch11-asymptotics.tex`)

- \(O\), \(o\), and \(\sim\), as in Volume 1. Asymptotic expansion \(f\approx\sum a_k\varphi_k\), unique, and \(e^{-x}\) has the zero expansion — `prop:asymunique`, 11.2.
- Euler’s series \(\int_0^\infty e^{-t}/(1+xt)\,dt\approx\sum(-1)^k k!\,x^k\), with remainder of the sign of the first omitted term — `prop:eulerseries`, 11.3. At \(x=1\) the value is \(0.5963473623\ldots\).
- Periodic Bernoulli functions \(\bar B_m\), with the Fourier series for \(m\ge2\) — `lem:bernoullifn`, 11.4.
- Euler–Maclaurin formula — `thm:eulermaclaurin`, 11.5.
- \(H_n=\ln n+\gamma+\frac1{2n}-\sum_{k<M}B_{2k}/(2k\,n^{2k})+O(n^{-2M})\), and the error is smaller than the first omitted term and has its sign — `cor:harmonic`, 11.6.
- Continuation of \(\zeta\) by Euler–Maclaurin — `prop:zetaem`, 11.7.
- Stirling’s series for \(\ln\Gamma(x)\), with \(0<\rho_m/T_m<1\) — `thm:stirlingseries`, 11.8.
- Laplace’s method — `thm:laplace`, 11.9. It gives Stirling’s formula again, and \(\binom{2n}n\sim 4^n/\sqrt{\pi n}\).
- Binomial series of \((1-z)^{-\alpha}\), with one further term — `prop:binomcoef`, 11.12.
- Transfer theorem — `thm:transfer`, 11.13.
- \(\ln p(n)\le\pi\sqrt{2n/3}\), from the product bound. The matching asymptotic is Chapter 12.

### Chapter 12 — The Hardy–Ramanujan Formula (`chapters/hardy-ramanujan.tex`)

- \(P(z)=\sum p(n)z^n=\prod_{k\ge1}(1-z^k)^{-1}\) for \(|z|<1\), and \(P(z)=e^{L(z)}\) — `lem:pdisc`, 12.1.
- \(\log P(e^{-t})\le\pi^2/(6t)\) — `lem:plog`, 12.2.
- Dedekind’s \(\eta(\tau)=e^{\pi i\tau/12}E(e^{2\pi i\tau})\) on the upper half-plane — definition, 12.3. Then \(\eta(\tau)=\sum_j(-1)^j e^{\pi i\tau(6j-1)^2/12}\).
- \(\eta(-1/\tau)=\sqrt{-i\tau}\,\eta(\tau)\), with the principal square root — `thm:eta`, 12.4.
- Transformation of \(P\), and \(P(e^{-t})=\sqrt{t/(2\pi)}\exp(\pi^2/(6t)-t/24)\,P(e^{-4\pi^2/t})\) — `lem:ptrans`, 12.5.
- \(p(n)=e^{\pi\sqrt{2n/3}}/(4\sqrt3\,n)\,(1+O(n^{-1/4}))\) — `thm:hr`, 12.6. The table ratios are \(0.873\), \(0.956\), \(0.969\), \(0.986\).
- Rademacher’s convergent series, numbered Theorem 12.7 and marked quoted. It is not proved, and nothing later uses it. See V5-010. The partial sums at \(n=200\) were recomputed.

### Chapter 13 — The Arithmetic–Geometric Mean (`chapters/ch12-agm.tex`)

- \(a_{n+1}=(a_n+b_n)/2\), \(b_{n+1}=\sqrt{a_nb_n}\), \(c_n=\sqrt{a_n^2-b_n^2}\), common limit \(M(a,b)\) — `prop:agm`, 13.1. The gap satisfies \(a_{n+1}-b_{n+1}\le(a_n-b_n)^2/(8b)\).
- \(I(a,b)=\int_0^{\pi/2}(a^2\cos^2\theta+b^2\sin^2\theta)^{-1/2}\,d\theta=\pi/(2M(a,b))\) — `thm:gaussagm`, 13.2.
- Complete elliptic integrals \(K(k)=I(1,k')\) and \(E(k)\), with \(k'=\sqrt{1-k^2}\).
- Landen: \(K(k)=(1+k_1)K(k_1)\) — `cor:landen`, 13.3.
- Lemniscate constant \(\varpi=2\int_0^1(1-r^4)^{-1/2}\,dr=2.62205755429211981\ldots\), and \(\varpi/\pi=1/M(1,\sqrt2)\) — `cor:lemniscate`, 13.4.
- Perimeter \(L(a,b)=4J(a,b)\), with \(J=(a^2-\sum_{n\ge0}2^{n-1}c_n^2)I\) — `thm:perimeter`, 13.7. The step is `prop:jstep`, 13.6, from `lem:jderiv`, 13.5.
- \(E'=(E-K)/k\) and \(K'=(E-k'^2 K)/(k\,k'^2)\) — `prop:kederiv`, 13.8.
- Legendre: \(EK'+E'K-KK'=\pi/2\) — `thm:legendre`, 13.9.
- Brent–Salamin: \(\pi=4M(1,1/\sqrt2)^2\big/(1-\sum_{n\ge1}2^{n+1}c_n^2)\) — `thm:brentsalamin`, 13.10.
- \(\Gamma(\frac14)=(2\pi)^{3/4}/\sqrt{M(1,\sqrt2)}=3.62560990822\ldots\), from the lemniscate integral of Chapter 5.
- Closing problems introduce, as exercises and not as theorems of the chapter: Dedekind’s reciprocity is already Chapter 9; Kummer’s carry count for \(v_p\binom{m+n}m\); Lucas’s reading of central binomial coefficients; the unitary DFT and its eigenvalue multiplicities; Dickman’s function \(\rho\), with \(\int_0^\infty\rho=e^\gamma\); the polynomial Mertens product \(E_n\sim e^{-\gamma}/n\). Mertens’s third theorem is admitted in `pb:dickmanint`. The prime-number theorem is quoted in `pb:primezeta`.

### Notation clashes with Volumes 1–4, and inside Volume 5

- \(\log\) in the number-theory chapters is the natural logarithm. Volume 1 writes \(\ln\). The two symbols are the same function. \(\log_2\) is named when the base is \(2\).
- \(\pi\) remains the circle constant. It is not reused for a permutation or for the prime-counting function. Volume 2’s \(\pi(x)\) is only named, in the preview of Volume 6.
- \(\varphi(n)\) is Euler’s totient, as in Volume 2. Volume 1 uses \(\varphi\) for the golden ratio, and Volume 4 uses \(\phi\) for the standard normal density. This volume does not use the normal density.
- \(\chi\) is the Legendre symbol in the Hadamard and progression problems, as in Volume 2. In the solution of `pb:mappings` the same letter is a cutoff \(\chi(x)=(e^{-x^2/2}-[x\le1])/x\). Volume 3 uses \(\chi\) for a representation character. The three uses are not in one argument.
- \(D_n\) is a derangement count in Chapter 9, as in Volume 1, and the dihedral group in `pb:rank`, as in Volume 3.
- \(E\) is the complete elliptic integral of the second kind from Chapter 13, and an expectation in the closing problems of that chapter. \(K(k)\) is the elliptic integral of the first kind. Volume 3 and Volume 4 use \(K_n\) for the complete graph.
- \(\omega\) is a root of unity, as before. In Chapter 10, \(\omega(t)=(\vartheta(t)-1)/2\) is the tail of Jacobi’s theta series.
- Chapter 10 says the series keeps \(\theta\) for Chebyshev’s function. Volume 2 writes that function as \(\vartheta(x)=\sum_{p\le x}\ln p\), and this volume also uses \(\vartheta\) for Jacobi’s theta series. Hardy’s phase on the critical line is \(\alpha\). See V5-019.
- The isoperimetric equality case is V5-011. The cotangent generating function in the Chapter 3 remark is V5-012. The lemniscate’s geometric length is V5-013. The limit for connected graphs is V5-014. The ball-volume maximum at dimension 5 is V5-015.
- \(B_1=-\frac12\) is \(B_1(0)\). The value \(B_1(1)=\frac12\) is the other end of the same polynomial. Odd indices at least \(3\) vanish.
- The Fourier transform on the line is unitary, with \(2\pi\) in the exponent. Chapter 7 puts the factor \(1/n\) on the inversion of the DFT, and says that Volume 3, Chapter 11, divided by \(n\) in the forward transform. The closing problem `pb:dftspectrum` uses the unitary matrix with \(1/\sqrt n\) on both sides.
- \(\xi(s)\) is the completed zeta function from Chapter 10. It is not a character and not a random variable.
- \(q\) is the size of a finite field in Chapters 9 and 13, and \(q(n)\) is the number of partitions into distinct parts in Chapter 12.
- \(M(a,b)\) is the arithmetic–geometric mean. It is not a mean of a random variable. \(M_n\) in the ones-in-a-partition exercise is an average count.
- \(s(h,k)\) is a Dedekind sum. The formula in Chapter 9 and the formula in Rademacher’s series agree when \(\gcd(h,k)=1\).
- \(\gamma\) remains Euler’s constant from Volume 1. The lemniscate constant is \(\varpi\), not \(\gamma\).

## Volume 6

Book order: preface, then Chapters 1–12. File paths are under `volume6-crossroads/`. \(\log\) is the natural logarithm. \(\mathrm{Li}(x)=\int_2^x dt/\log t\). The shared counter restarts each chapter.

### Preface (`chapters/preface.tex`)

- Admitted, and not used by a theorem: the functional equation of a primitive Dirichlet \(L\)-function (Volume 13, Chapter 12), in one remark of Chapter 7; Tonelli’s theorem for improper integrals (Volume 7), in the solution of `pb:beukersthree`.

### Chapter 1 — Mertens (`chapters/ch01-mertens.tex`)

- \(\Lambda(n)=\log p\) if \(n=p^k\), and \(\Lambda*\mathbf 1=\log\).
- \(\theta(x)=\sum_{p\le x}\log p\) and \(\psi(x)=\sum_{n\le x}\Lambda(n)\). Volume 2 writes the first sum as \(\vartheta\). See V6-002.
- Abel summation — `lem:abelint`, 1.1.
- Chebyshev’s bounds, including \(\theta(x)<x\log 4\) — `prop:chebyshev`, 1.2.
- \(\prod_{p\le x}(1-1/p)\sim e^{-\gamma}/\log x\) — `thm:mertens1`, 1.3. The ratio of \(\theta\) — `cor:chebratio`, 1.4.
- \(\sum_{p\le x}1/p=\log\log x+M+O(1/\log x)\), with the Meissel–Mertens constant \(M\) — `thm:mertens2`, 1.5.
- \(\sum_{p\le x}\log p/(p-1)=\log x-\gamma+o(1)\), and \(M+H=\gamma\) — `thm:mertens3`, 1.6.

### Chapter 2 — Averages (`chapters/ch02-averages.tex`)

- Wintner’s mean value: if \(f=\mathbf 1*h\) and \(\sum |h(d)|/d<\infty\), then the mean is \(\sum h(d)/d\) — `thm:wintner`, 2.2.
- Hyperbola method — `lem:hyperbola`, 2.8. \(\sum_{n\le x}\tau(n)=x\log x+(2\gamma-1)x+O(\sqrt x)\).
- \(\sum_{n\le x}\varphi(n)=(3/\pi^2)x^2+O(x\log x)\), and the squarefree count \((6/\pi^2)x+O(\sqrt x)\) — `thm:errorterms`, 2.6.
- The constant term of \(P_3\) is quoted as \(3\gamma^2-3\gamma-3\gamma_1+1\), with Stieltjes \(\gamma_1=-0.0728\). The gloss “the coefficient after \(\gamma\)” is V6-004. The display is not a theorem.
- \(\sum_{n\le x}2^{\omega(n)}=(6/\pi^2)x\log x+O(x)\). The secondary constant \(0.7869\) is named inside that error. See V6-006.

### Chapter 3 — Characters (`chapters/ch03-characters.tex`)

- Dirichlet characters modulo \(q\), and orthogonality — `prop:orth`, 3.1. The same facts are Volume 2, Theorem 11.5, and Volume 3, Proposition 11.15.
- Conductor and primitive characters — `prop:conductor`.
- \(|\tau(\chi)|=\sqrt q\) for primitive \(\chi\) — `thm:gauss`.
- \(L(s,\chi)=\sum\chi(n)n^{-s}\) for \(\operatorname{Re}s>0\) when \(\chi\ne\chi_0\), and the Euler product for \(\operatorname{Re}s>1\).
- \(L(1,\chi)\ne 0\) — `thm:lnonzero`, 3.8. Section `sec:siegel` is 3.5 in the index.
- Dirichlet’s formula for \(L(1,\chi)\) — `thm:l1formula`, 3.10. In particular \(L(1,\chi_{-4})=\pi/4\) and \(L(1,\chi_{-3})=\pi/(3\sqrt 3)\).
- The class-number formula \(L(1,\chi)=\pi h(-p)/\sqrt p\) is quoted, and proved in Volume 13, Chapter 11.
- The caption limit \(L(\sigma,\chi_5)\to 0\) as \(\sigma\to 0\) is V6-007.

### Chapter 4 — Dirichlet’s theorem (`chapters/ch04-dirichlet.tex`)

- Infinitely many primes \(p\equiv a\pmod q\) when \(\gcd(a,q)=1\) — `thm:dirichlet`, 4.1. The proof uses \(L(1,\chi)\ne 0\).
- \(\sum_{p\le x,\,p\equiv a\pmod q}1/p=(1/\varphi(q))\log\log x+C(q,a)+O(1/\log x)\) — the progression form of Mertens.

### Chapter 5 — The prime number theorem (`chapters/ch05-pnt.tex`)

- The weight \(3+4\cos\theta+\cos 2\theta=2(1+\cos\theta)^2\), and \(L(1+it,\chi)\ne 0\) — `thm:line`, 5.2.
- Newman’s theorem — `thm:newman`, 5.3. The monotone lemma — `lem:monotone`, 5.4.
- \(\psi(x)\sim x\), and \(\pi(x)\sim\mathrm{Li}(x)\sim x/\log x\) — `thm:pnt`, 5.5. The comparison of \(\mathrm{Li}\) is Exercise `ex:li`, 5.1.
- \(\sum_{n\le x}\mu(n)=o(x)\) — `thm:mobiussum`, 5.7.
- The prime number theorem in arithmetic progressions — `thm:pntap`, 5.8.
- \(p_n\sim n\log n\) — Exercise `ex:nthprime`.
- The Vinogradov–Korobov shape is quoted, not proved.

### Chapter 6 — Zeros (`chapters/ch06-zeros.tex`)

- Complex Stirling — `thm:stirlingc`, 6.1. Hardy’s phase is \(\alpha(T)\), and the series keeps \(\theta\) for Chebyshev.
- Jensen’s formula — `thm:jensen`, 6.3. Borel–Carathéodory — `lem:borel`, 6.5.
- Hadamard’s product for \(\xi\) — `thm:hadamard`, 6.7.
- \(N(T)=\alpha(T)/\pi+1+S(T)\) — `thm:rvm`, 6.9.
- The completed \(\xi\) of Volume 5, with \(\xi(s)=\xi(1-s)\) — `prop:xi`.
- Zero-free region \(\sigma\ge 1-1/(c\log(|t|+2))\) — `thm:zerofree`, 6.12. The explicit factor in the proof is \(1/(14A'\log|t|)\) for \(|t|\ge 2\).
- Proportions of zeros on the critical line (Levinson, Conrey, Pratt–Robles–Zaharescu–Zeindler) are quotations.

### Chapter 7 — The explicit formula (`chapters/ch07-explicit.tex`)

- Perron — `lem:perron`, 7.1. Truncated Perron — `prop:truncperron`, 7.2. Good heights — `lem:goodT`, 7.3.
- The explicit formula for \(\psi_0\) — `thm:explicit`, 7.5. The exact formula — `cor:exactexplicit`, 7.6.
- \(\psi(x)=x+O\bigl(x\exp(-c\sqrt{\log x})\bigr)\) — `thm:pnterror`, 7.8, and the same shape for \(\pi(x)-\mathrm{Li}(x)\) — `cor:pnterrorpi`, 7.9.
- The Riemann hypothesis is equivalent to \(\psi(x)=x+O(\sqrt x\log^2 x)\) — `thm:rhequiv`, 7.10.
- \(\zeta'/\zeta(0)=\log(2\pi)\). The value of \(B\) is taken from a later exercise. See V6-008.
- The bias identity for \(\theta(x;4,3)-\theta(x;4,1)\). The functional equation of \(L(s,\chi_{-4})\) is admitted in the remark and is not used by a theorem.

### Chapter 8 — Sieves (`chapters/ch08-sieves.tex`)

- Legendre’s sieve — `prop:legendre`, 8.1.
- Selberg’s sieve — `thm:selberg`, 8.2, with \(|\lambda_d|\le 1\).
- Brun–Titchmarsh — `thm:bt`, 8.4. The short-interval form is Exercise `ex:btap`.
- Brun’s theorem on twin primes — `thm:twins`, 8.5, and the convergent sum — `cor:brun`, 8.6.
- The large sieve — `thm:largesieve`, 8.8. The arithmetic large sieve — `thm:arithls`, 8.10.
- The twin-prime constant \(C_2=\prod_{p>2}(1-1/(p-1)^2)=0.66016\ldots\).
- Buchstab’s function for \(u>3\), and Maier’s theorem, are quoted and proved in Volume 15.

### Chapter 9 — Erdős–Kac (`chapters/ch09-erdoskac.tex`)

- Turán–Kubilius — `thm:tk`, 9.1.
- The normal order of \(\omega(n)\) and of \(\Omega(n)\) — `thm:hr`, 9.2.
- Erdős–Kac: \((\omega(n)-\log\log n)/\sqrt{\log\log n}\) tends in law to \(\mathcal N(0,1)\) — `thm:erdoskac`, 9.7.
- The Gaussian characteristic function and the inversion formula are Volume 4, Proposition 6.7 and Theorem 6.8(b).

### Chapter 10 — Random primes (`chapters/ch10-random.tex`)

- Cramér’s model: independent Bernoulli variables of mean \(1/\log n\) for \(n\ge 3\) — `def:cramer`, 10.1.
- The model satisfies \(\pi_{\mathcal C}(x)\sim\mathrm{Li}(x)\) almost surely — `thm:cramerpnt`, 10.2.
- \(\limsup(q_{i+1}-q_i)/\log^2 q_i=1\) almost surely — `thm:cramergaps`, 10.4.
- The singular series \(\mathfrak S(H)\). It is positive exactly for admissible \(H\) — `prop:ssconv`, 10.5.
- A model that knows the small primes — `prop:smallprimes`, 10.6.
- Gallagher: \(\sum_{d\le h}\mathfrak S(\{0,d\})=h+O(\sqrt h)\) — `thm:gallagher`, 10.7.
- Maier’s theorem is quoted and proved in Volume 15, Chapter 2. Hoeffding is Volume 4, Theorem 4.2. Both halves of Borel–Cantelli are Theorem 4.4.

### Chapter 11 — Exponential sums (`chapters/ch11-sums.tex`)

- \(\bigl|\sum_{n=M+1}^{M+N}e(\beta n)\bigr|\le\min\bigl(N,1/(2\|\beta\|)\bigr)\) — `lem:geom`, 11.1. Here \(e(x)=e^{2\pi ix}\) and \(\|x\|\) is the distance to \(\Z\).
- Van der Corput’s inequality — `lem:vdc`, 11.2. The difference theorem — `thm:vdcdiff`, 11.3.
- Weyl: a polynomial with one irrational coefficient besides the constant term is equidistributed modulo \(1\) — `thm:weylpoly`, 11.4. Squares — `cor:nsquared`, 11.5.
- Weyl’s inequality for squares — `thm:weylineq`, 11.7, from `lem:summin`, 11.6.
- Kusmin–Landau — `lem:kl`, 11.8. The second-derivative test — `thm:secondderiv`, 11.9.
- \(n^c\) is equidistributed modulo \(1\) for non-integral \(c\in(0,2)\) — `thm:nc`, 11.10. The case \(c>2\) is Exercise `ex:nc23`.
- Pólya–Vinogradov: a primitive character sum is at most \(\sqrt q\,(1+\log q)\) — `thm:pv`, 11.11.
- The least quadratic non-residue is \(O(p^{1/(2\sqrt e)+\varepsilon})\) — `thm:vinogradov`, 11.12.
- Weyl’s criterion is Volume 5, Theorem 6.13. The bound \(|\alpha-p/q|<1/q^2\) for convergents is Volume 2, Theorem 9.2.

### Chapter 12 — Modular forms (`chapters/ch12-modular.tex`)

- \(\mathrm{SL}_2(\Z)\) acts on the upper half-plane by Möbius transformations. \(T\tau=\tau+1\) and \(S\tau=-1/\tau\), and they generate the group — `prop:generators`, 12.1.
- The fundamental domain \(F=\{|\operatorname{Re}\tau|\le 1/2,\,|\tau|\ge 1\}\) meets every orbit, and meets an orbit once in the interior — `thm:fundamental`, 12.2.
- A modular form of weight \(k\), the spaces \(M_k\) and \(S_k\), and the nome \(q=e^{2\pi i\tau}\) — `def:modform`, 12.3. Then \(M_k=0\) for odd \(k\).
- The Eisenstein series \(G_k\) for even \(k\ge 4\) — `lem:latticesum`, 12.4, and `prop:eisenstein`, 12.5.
- \(G_k=2\zeta(k)+\frac{2(2\pi i)^k}{(k-1)!}\sum\sigma_{k-1}(n)q^n\), and \(E_k=G_k/(2\zeta(k))=1-\frac{2k}{B_k}\sum\sigma_{k-1}(n)q^n\) — `thm:eisensteinq`, 12.6. In particular \(E_4=1+240\sum\sigma_3(n)q^n\) and \(E_6=1-504\sum\sigma_5(n)q^n\).
- \(\eta(-1/\tau)=\sqrt{-i\tau}\,\eta(\tau)\), and \(\Delta=\eta^{24}=q\prod(1-q^n)^{24}=\sum\tau(n)q^n\) is a cusp form of weight \(12\) — `thm:eta`, 12.7. Volume 5, Theorem 12.4, is the first proof. The contour limit is V6-009.
- \(\dim M_k=\lfloor k/12\rfloor\) or one more, and \(M_2=0\) — `thm:dimension`, 12.9. Thus \(E_4^2=E_8\).
- \(\sigma_7(n)=\sigma_3(n)+120\sum_{m<n}\sigma_3(m)\sigma_3(n-m)\) — `cor:sigma7`, 12.10.
- \(1728\Delta=E_4^3-E_6^2\), and \(\tau(n)\equiv\sigma_{11}(n)\pmod{691}\) — `cor:delta`, 12.11.
- Hecke operators \(T_p\), and \(T_p\) preserves \(M_k\) and \(S_k\) — `lem:hermite`, 12.12, and `thm:hecke`, 12.13.
- \(\tau(p)\tau(n)=\tau(pn)+p^{11}\tau(n/p)\), so \(\tau\) is multiplicative — `thm:mordell`, 12.14. The values through \(n=12\) match the product.
- Deligne’s bound \(|\tau(p)|\le 2p^{11/2}\), the Sato–Tate measure \((2/\pi)\sin^2\theta\), and modularity for elliptic curves are quoted, as a preview of Volume 13.
- Closing problems, proved there and not numbered as theorems of the chapter: Singer’s difference sets; the squarefree-neighbour densities \(\prod(1-2/p^2)\) and \(\prod(1-3/p^2)\); Beukers’s proofs that \(\zeta(2)\) and \(\zeta(3)\) are irrational; \(\int_0^1\{1/x\}\,dx=1-\gamma\); Menon’s identity \(\sum_{\gcd(a,n)=1}\gcd(a-1,n)=\varphi(n)\tau(n)\); Rényi’s law of \(\Omega-\omega\), with \(2^kd_k\to 1/(4C_2)\); the Landau–Ramanujan constant \(K=C/\sqrt\pi=0.7642\ldots\); Ramanujan’s equations for \(D=\frac1{2\pi i}\frac{d}{d\tau}\); Landau’s formula and the Guinand–Weil explicit formula, the second under the shape stated in `pb:hearzeros`; Schur’s evaluation \(G=\sqrt p\) or \(i\sqrt p\); Hecke’s equidistribution of the angles of the Gaussian primes; Romanoff’s theorem. The ordinate assertion in Landau’s formula is V6-010. The exercises graded `[Journey]` are V6-001.

### Notation clashes with Volumes 1–5

- \(\log\) is the natural logarithm, the same function as Volume 1’s \(\ln\) and Volume 2’s \(\ln\).
- Chebyshev’s function is \(\theta(x)\) from Chapter 1. Volume 2 writes \(\vartheta(x)\). Volume 5 uses \(\vartheta\) for Jacobi’s theta series and \(\alpha\) for Hardy’s phase. Chapter 6 of this volume repeats that choice of \(\alpha\). See V6-002 and V5-019.
- \(\tau(n)\) in Chapter 12 is Ramanujan’s coefficient. Chapters 1–11 use \(\tau(n)\) for the number of divisors, as in Volume 2. The opening of Chapter 12 says the three uses of the letter are distinct. The same letter is the variable in the upper half-plane.
- \(q=e^{2\pi i\tau}\) is the nome from Chapter 12. Earlier chapters use \(q\) for a modulus.
- \(\omega(n)\) is the number of distinct prime factors, as in Volume 2. Buchstab’s function in Chapter 8 is also written \(\omega(u)\). Volume 5 writes \(\omega(t)=(\vartheta(t)-1)/2\) for the tail of Jacobi’s series. The three are not in one argument.
- \(\sigma_k(n)=\sum_{d\mid n}d^k\). The same letter \(\sigma\) is the real part of \(s=\sigma+it\), as in Volume 5.
- \(E_k\) is the normalised Eisenstein series. \(E\) is also an expectation in the probabilistic chapters, as in Volume 4. \(M_k\) is the space of modular forms of weight \(k\). \(M\) is the Meissel–Mertens constant from Chapter 1.
- \(\chi\) is a Dirichlet character, as in Volume 2, Chapter 11, and Volume 3, Proposition 11.15. Volume 3 also uses \(\chi\) for a representation character. The orthogonality cited from Volume 3 is the Dirichlet one.
- \(\Lambda\) is von Mangoldt’s function. Volume 5’s completed function is \(\xi\), and this volume keeps that letter.
- \(\varphi(n)\) remains Euler’s totient. In Chapter 12, \(\varphi_p=\arctan(b/a)\) is the angle of a Gaussian prime.
- The exercise grade `[Journey]` is V6-001. It is the same grade Volume 5 prints in three exercises. See V5-005.

## Volume 7 — Spaces

File names are under `volume7-spaces/chapters/`. The shared counter numbers theorems, propositions, lemmas, corollaries, definitions, and examples inside each chapter. Exercises use a separate counter and restart each chapter. \(\N\) includes \(0\). The logarithm constructed in Chapter 2 is \(\ln\). In later chapters \(\log\) is that same natural logarithm, except in a ratio of logarithms, where the base cancels.

### Chapter 1 — Sets (`ch01-sets.tex`)

- \(\N\) is the smallest inductive set, and it contains \(0\) — definition 1.1.
- Peano’s axioms — `thm:peano`, 1.2. Recursion — `thm:recursion`, 1.3.
- \(\N\) is a semiring — `prop:semiring`, 1.4. Well-order — `prop:wellorder`, 1.5.
- \(\Z\) from pairs of natural numbers — `prop:integers`, 1.6. \(\Q\) is the field of fractions, by the same pattern as Volume 3, Chapter 6.
- Ordered field, Archimedean, least upper bound — definition 1.7.
- \(\R\) is the ring of rational Cauchy sequences modulo null sequences — definition 1.8. The three Cauchy facts — `lem:cauchybasic`, 1.9. Part (c) is an order statement. Its use for \(\Q_p\) is V7-001.
- \(\R\) is a complete Archimedean ordered field with the least upper bound property — `thm:reals`, 1.10. Any two such fields are isomorphic — `thm:uniqueR`, 1.11. This clears the least-upper-bound debt from Volume 1.
- Equipotence — definition 1.12. Countable unions of countable sets need countable choice — `prop:countable`, 1.13. The phrase is V7-007.
- Cantor — `thm:cantor`, 1.14. Schröder–Bernstein — `thm:sb`, 1.15. \(\lvert\R\rvert=\lvert\mathcal P(\N)\rvert\) — `thm:continuum`, 1.16. The continuum hypothesis is independent of ZFC, quoted.
- The axiom of choice — definition 1.17. Partial order, chain, maximal element, well-order — definition 1.18.
- Zorn’s lemma — `thm:zorn`, 1.19. Well-ordering — `thm:wellordering`, 1.20. Every vector space has a basis — `thm:basis`, 1.21. A Hamel basis of \(\R\) over \(\Q\).
- Algebraic closure of a field is asserted and not proved. See V7-003. Krull’s theorem is Exercise `ex:krull`.
- The Calkin–Wilf tree and Newman’s successor are Exercise `ex:calkinwilf`. A positive square root in a complete ordered field is Exercise `ex:v7c01c`. Nested intervals are Exercise `ex:v7c01d`.

### Chapter 2 — Metric spaces (`ch02-metric.tex`)

- Metric and norm — definition 2.1. Open, closed, closure, dense — definition 2.3. Uniform continuity, Lipschitz, contraction, isometry — definition 2.5. The square-root example is V7-005.
- Closure and continuity — `prop:closure`, 2.4. Cauchy sequence, complete, Banach space — definition 2.6. Complete subspaces and \(C_b(X)\) — `prop:complete`, 2.7.
- An isometry of a dense subset into a complete space extends — `lem:extension`, 2.8. Completion, unique up to isometry — `thm:completion`, 2.9.
- \(\Q_p\) is the completion of \(\Q\) for \(\lvert x\rvert_p=p^{-v_p(x)}\), and \(\Z_p=\{x:\lvert x\rvert_p\le 1\}\) — `thm:Qp`, 2.10. The field step is V7-001. \(v_p\) is Volume 2, Chapter 1. Ostrowski’s theorem is quoted and unused.
- \(\Z_p\) is sequentially compact, and \(\Q_p\) is locally compact — `cor:Zpcompact`, 2.11. The names compact and locally compact are given in Chapter 4. The word connected, used of \([-1,1]\), is V7-006. Volume 8, Chapter 8, uses this corollary for Haar measure.
- Banach’s fixed point theorem — `thm:banach`, 2.12. The cosine example, with \(\sin 1<0.85\), is Example 2.13. That bound is V7-004.
- Cauchy product of absolutely convergent series — `lem:cauchyproduct`, 2.14.
- \(\exp\), \(\cos\), \(\sin\), \(e\), and \(\pi\) as twice the first positive zero of \(\cos\) — definition 2.15 and `thm:exp`, 2.16. This clears the debt from Volume 1. \(\ln\) is the inverse of \(\exp\) on \(\R\). A monotone intermediate-value lemma — `lem:monoivt`, 2.17.
- Hausdorff distance on the nonempty closed bounded sets — definition 2.18. That space is complete when \(X\) is — `thm:hausdorffcomplete`, 2.19. Hutchinson’s attractor — `thm:hutchinson`, 2.20.
- The middle-thirds Cantor set \(C\) is the attractor of \(x\mapsto x/3\) and \(x\mapsto(x+2)/3\). The devil’s staircase is the fixed point in Exercise `ex:devil`. Exercise `ex:Z2cantor` identifies \(\Z_2\) with \(C\).

### Chapter 3 — Topology (`ch03-topology.tex`)

- Topology, closed, neighbourhood, interior, closure, continuous, homeomorphism — definition 3.1. A basis generates a topology — `prop:basis`, 3.3.
- Product topology — definition 3.4 and `prop:product`, 3.5. Quotient topology — definition 3.6. Universal property — `prop:quotient`, 3.7. \(\R/\Z\) is homeomorphic to the circle.
- Connected — definition 3.9. The connected subsets of \(\R\) are the intervals — `thm:intervals`, 3.10. Images, closures, and products — `prop:connected`, 3.11. Intermediate value theorem — `cor:ivt`, 3.12.
- Path-connected — definition 3.13. An open connected subset of a normed space is path-connected; the topologist’s sine curve is connected and not path-connected — `prop:openconnected`, 3.14. The sphere sentence is V7-002. The Cantor-set sentence is V7-009.
- Hausdorff and normal — definition 3.15. Urysohn’s function in a metric space — `prop:urysohn`, 3.16. Urysohn’s lemma for a general normal space is quoted from Munkres and unused.
- First countable, second countable, separable — definition 3.17. In a metric space the three agree with sequential continuity — `prop:sequences`, 3.18. Tietze for metric spaces — `prop:tietze`, 3.19.
- The Furstenberg topology on \(\Z\) is Exercise `ex:furstenberg`, the same topology as Volume 2, Exercise 2.8.

### Chapter 4 — Compactness (`ch04-compact.tex`)

- Compact — definition 4.1. Closed subsets, continuous images, and the finite intersection property — `prop:compactbasic`, 4.2. A finite product of compact spaces is compact — `prop:finiteproduct`, 4.3.
- Heine–Borel — `thm:heineborel`, 4.4. Extreme values — `cor:extreme`, 4.5. Norms on a finite-dimensional space are equivalent — `cor:norms`, 4.6.
- Sequentially compact and totally bounded — definition 4.7. In a metric space the three compactness notions agree — `thm:compactmetric`, 4.8. Heine — `thm:heine`, 4.9.
- Fermat, Rolle, the mean value theorem, and the Lipschitz form — `thm:mvt`, 4.10. This is the mean value theorem of Volume 1, proved again.
- Tychonoff — `thm:tychonoff`, 4.11. Kelley’s converse, that Tychonoff implies the axiom of choice, is quoted.
- Cantor space \(\{0,1\}^\N\) with \(\N=\{1,2,\ldots\}\) in this definition only, and the Cantor set — definition 4.12. The homeomorphism and the stage sets \(C_n\) — `prop:cantor`, 4.13.
- Equicontinuous and pointwise bounded — definition 4.14. Arzelà–Ascoli — `thm:ascoli`, 4.15. A closed bounded equi-Lipschitz set is compact — `cor:lipcompact`, 4.16.
- A subalgebra that separates points — definition 4.17. The absolute-value approximation — `lem:abs`, 4.18. Stone–Weierstrass — `thm:sw`, 4.19. Polynomials are dense in \(C([a,b])\) — `cor:weierstrass`, 4.20.

### Chapter 5 — Baire (`ch05-baire.tex`)

- Nowhere dense, meagre, comeagre, \(G_\delta\), \(F_\sigma\) — definition 5.1. Baire’s theorem — `thm:baire`, 5.2. A dense \(G_\delta\) is comeagre, and \(\Q\) is not a \(G_\delta\) — `cor:bairecor`, 5.3.
- Generic and typical — definition 5.4. The slope squeeze — `lem:squeeze`, 5.5. The Takagi function is continuous and nowhere differentiable — `thm:takagi`, 5.6. A comeagre set of continuous functions is nowhere differentiable — `thm:banachmaz`, 5.7.
- Oscillation, and the continuity points of a function are a \(G_\delta\) — `prop:continuitypoints`, 5.8. A Baire class one function has a comeagre set of continuity points — `thm:baireclassone`, 5.9. A derivative is Baire class one — `cor:derivative`, 5.10.
- Null, before measure exists — definition 5.11. Liouville number — definition 5.12. The Liouville numbers are a comeagre null set — `thm:liouville`, 5.13. Khinchin’s scale is quoted here and proved in Chapter 13. It is not a premise.
- The set of binary sequences with limsup of the proportion of ones equal to \(1\) is comeagre — `prop:nonnormal`, 5.14. The greedy expansion is `prop:cantor`. Borel normality is a preview of Chapter 7.
- The Weierstrass series and Hardy’s condition \(ab\ge 1\) are quoted and unused.

### Chapter 6 — Jordan (`jordan.tex`, `jordan-polygon.tex`)

- A polygonal Jordan curve separates the plane into two components — `thm:jordanpoly`, 6.1. Parity of crossings — `lem:parity`, 6.2. The two chains of sectors — `lem:sides`, 6.3.
- A continuous argument along a path that misses a point — `lem:lift`, 6.4. Winding number \(n(\gamma,a)\) — definition 6.5. It is an integer, constant on components, and \(1\) for the circle — `prop:windingprops`, 6.6.
- The disc does not retract to the circle, and Brouwer’s fixed point theorem — `thm:brouwer`, 6.7. Crossing paths — `lem:crossing`, 6.8. An arc does not separate the plane — `lem:arc`, 6.9. The Jordan curve theorem — `thm:jordan`, 6.10. This clears the debt from Volume 5, Chapter 9.
- Osgood’s curve of positive area, the Lakes of Wada, Schoenflies, and Carathéodory’s boundary theorem are quoted and unused.

### Chapter 7 — Measures (`ch06-measures.tex`)

- \(\sigma\)-algebra, measure, and the Borel \(\sigma\)-algebra — definition 7.1. Continuity of measure and the Borel–Cantelli lemma — `prop:measureprops`, 7.2.
- \(\pi\)-system and \(\lambda\)-system — definition 7.3. Dynkin — `thm:dynkin6`, 7.4. Uniqueness of finite measures that agree on a \(\pi\)-system — `thm:uniq6`, 7.5.
- Outer measure and Carathéodory’s measurable sets — definition 7.6. The measurable sets form a \(\sigma\)-algebra and the outer measure is a measure there — `thm:caratheodory`, 7.7.
- Semiring and premeasure — definition 7.8. A semiring generates the product sets — `lem:semiring`, 7.9. Extension — `thm:extension`, 7.10. Lebesgue measure on \(\R^d\) — `thm:lebesgue`, 7.11. This clears the debt from Volume 5. Inner and outer regularity — `prop:regularity`, 7.12.
- Lebesgue–Stieltjes measure of a non-decreasing right-continuous function — `thm:stieltjes`, 7.13. Quantile — `prop:quantile`, 7.14.
- Vitali’s non-measurable set — `thm:vitali6`, 7.15. Solovay’s model and the Banach–Tarski paradox are quoted and unused.
- Binary digits of a uniform random variable — `lem:digits6`, 7.16. An independent sequence with prescribed laws on \(\R\) — `thm:independent`, 7.17. The fourth-moment bound — `lem:fourth`, 7.18. Almost every number is absolutely normal — `thm:borelnormal`, 7.19.

### Chapter 8 — The integral (`ch07-integral.tex`)

- Measurable function and simple function — definition 8.1. Sums, products, and limits of measurable functions — `prop:measurablefns`, 8.2.
- The integral of a nonnegative measurable function — definition 8.3. Monotone convergence — `thm:mct6`, 8.4. Linearity — `cor:linearity6`, 8.5. Markov’s inequality — `prop:markov`, 8.6. Fatou — `thm:fatou6`, 8.7.
- Integrable, and \(\mathcal L^1(\mu)\) — definition 8.8. Dominated convergence — `thm:dct6`, 8.9.
- The Riemann integral of a continuous function on \([a,b]\) equals the Lebesgue integral — `thm:riemanncont`, 8.10. This clears the debt from Volume 1. Lebesgue’s criterion — `thm:lebesguecriterion`, 8.11.
- Convergence in measure and in \(L^1\) — definition 8.12. The modes of convergence — `prop:modes`, 8.13. Uniform integrability — definition 8.14. Absolute continuity of the integral — `lem:abscont`, 8.15. Vitali’s convergence theorem — `thm:vitali7`, 8.16. Differentiation under the integral sign — `thm:parameter`, 8.17.
- The layer-cake representation is Exercise `ex:layercake`. The Dirichlet integral equals \(\pi/2\) as an improper integral, not a Lebesgue integral, in Exercise `ex:dirichlet`.

### Chapter 9 — Products (`ch08-products.tex`)

- The product of Borel \(\sigma\)-algebras — `prop:borelproduct`, 9.1. Sections — `lem:sections`, 9.2. A section of a measurable set is measurable — `lem:slicemeasurable`, 9.3.
- Product measure — `thm:product`, 9.4. Tonelli — `thm:tonelli`, 9.5. Fubini — `thm:fubini`, 9.6. These clear the debts from Volumes 4, 5, and 6.
- A linear map multiplies volume by \(\lvert\det\rvert\) — `thm:lineardet`, 9.7. Change of variables for a \(C^1\) diffeomorphism — `thm:cov`, 9.8. The cube estimate — `lem:cube`, 9.9.
- Polar coordinates — `thm:polar`, 9.10. Surface measure on the sphere is written \(\sigma\). The volume of the ball — `thm:ball`, 9.11. The Gaussian density — `thm:gaussdensity`, 9.12.
- \(\Gamma(a)\Gamma(b)=B(a,b)\Gamma(a+b)\) and the simplex volume \(1/n!\) are exercises.

### Chapter 10 — \(L^p\) (`ch09-lp.tex`)

- Young’s inequality — `lem:young`, 10.1. Hölder — `thm:holder`, 10.2. Minkowski — `thm:minkowski`, 10.3.
- \(L^p\) for \(1\le p<\infty\), and \(L^\infty\) with the essential supremum. Riesz–Fischer: \(L^p\) is a Banach space — `thm:rieszfischer`, 10.4.
- Jensen’s inequality — `thm:jensen`, 10.5. Simple functions are dense — `prop:simpledense`, 10.6. \(C_c\) is dense in \(L^p(\R^d)\) for \(p<\infty\) — `thm:ccdense`, 10.7.
- Translation is continuous on \(L^p\) — `prop:translation`, 10.8. Convolution — `prop:convolution`, 10.9. Approximate identities — `thm:approxid`, 10.10. \(C_c^\infty\) is dense — `thm:smoothdense`, 10.11.
- Young’s inequality for convolutions is Exercise `ex:youngconv`. Hardy’s inequality, with sharp constant \(p/(p-1)\), is Exercise `ex:hardy`.

### Chapter 11 — Differentiation and conditional expectation (`ch10-radon.tex`)

- The positive and negative parts of a signed measure — `lem:positivepart`, 11.1. Hahn decomposition — `thm:hahn`, 11.2. Jordan decomposition — `cor:jordan`, 11.3.
- Absolute continuity and singularity. Radon–Nikodym — `thm:rn`, 11.4. Lebesgue decomposition — `thm:lebdecomp`, 11.5. The three parts of a finite signed measure — `cor:threeparts`, 11.6.
- Vitali’s covering lemma, with the enlarged balls of radius \(3\) times — `lem:vitalicover`, 11.7. The Hardy–Littlewood maximal function and the weak inequality with constant \(3^d\) — `thm:maximal`, 11.8. Lebesgue points — `thm:lebdiff`, 11.9.
- Outer regularity of a finite Borel measure on a metric space — `lem:outerreg`, 11.10. Differentiation of measures — `thm:diffmeasures`, 11.11. A monotone function is differentiable almost everywhere — `thm:monotone`, 11.12.
- Absolute continuity of a function — definition 11.13. The fundamental theorem — `thm:ftc`, 11.14.
- Conditional expectation — `thm:condexp`, 11.16. The tower property — `thm:tower`, 11.17. Example 11.15 is a fair die.

### Chapter 12 — Measures on metric spaces (`ch11-metricmeasures.tex`)

- On a Polish space every finite Borel measure is tight — `thm:ulam`, 12.1. Partitions of unity — `lem:pou`, 12.2.
- A positive linear functional on \(C(K)\), for \(K\) compact metric, is integration against a unique finite Borel measure — `thm:riesz`, 12.3.
- Portmanteau — `thm:portmanteau`, 12.4. Weak convergence from convergence of distribution functions at continuity points — `cor:cdfweak`, 12.5.
- A compact metric space is separable — `lem:separable`, 12.6. Prokhorov: a tight sequence of probabilities on \(\R^d\), or on a compact metric space, has a weakly convergent subsequence — `thm:prokhorov`, 12.7. The equivalence on a general Polish space is quoted and unused.
- Kolmogorov’s extension for a consistent family of laws on \(\R^n\) — `thm:kolmogorov`, 12.8. The metric on \(\R^\N\) is \(\sum 2^{-n}\min(1,\lvert x_n-y_n\rvert)\).
- Hausdorff content \(\mathcal H^s_\delta\) and Hausdorff measure \(\mathcal H^s\). The dimension jumps from \(\infty\) to \(0\) — `prop:jump`, 12.9. The mass distribution principle — `lem:massdist`, 12.10.
- \(\dim_H C=\log 2/\log 3\), and \(\tfrac12\le\mathcal H^s(C)\le 1\) — `thm:cantordim`, 12.11. The equality \(\mathcal H^s(C)=1\) is quoted and unused. Remark `rem:hausdorffquoted`: Falconer’s two facts, that \(\mathcal H^s\) is a Borel measure and that \(\mathcal H^d\) is a multiple of Lebesgue measure, are quoted and unused. Moran–Hutchinson is quoted and unused.
- The carpet has dimension \(\log 8/\log 3\), and the Sierpiński triangle has dimension \(\log 3/\log 2\), in Exercise `ex:carpet`.

### Chapter 13 — Almost every number (`ch12-harder.tex`)

No statement in this chapter is numbered as a theorem. The problems are exercises of Chapter 13. Continued fractions are Volume 2, Chapter 9: the error is Theorem 9.2, the best-approximation lemma is Lemma 9.4, Legendre’s theorem is Theorem 9.5, and periodicity is Theorem 9.6. Weyl’s criterion is Volume 5, Theorem 6.13. The prime number theorem is Volume 6, Theorem 5.5. Here \(\lVert t\rVert\) is the distance to \(\Z\), and \(e(t)=e^{2\pi it}\), as in Volumes 5 and 6. The Gauss map is \(G(x)=\{1/x\}\).

- If \(\sum q\psi(q)<\infty\), almost every \(x\) has only finitely many solutions of \(\lvert x-p/q\rvert<\psi(q)\) — `pb:khinconv`. The Liouville numbers are null. Almost every \(x\) satisfies \(\lvert x-p/q\rvert\ge c(x)/(q^2\log^2 q)\).
- Badly approximable numbers are those with bounded continued-fraction digits. The set is meagre, null, dense, and uncountable — `pb:badnull`. Jarník’s theorem \(\dim_H\mathrm{Bad}=1\) is quoted.
- Borel–Bernstein: conditional on a cylinder, the next digit is large with probability comparable to \(1/k\) — `pb:borelbernstein`.
- Khinchin’s theorem, under the hypothesis that \(q^2\psi(q)\) decreases — `pb:khinchin`. The constant \(c<4.4\) is V7-010. Almost every \(x\) meets \(1/(q^2\log q)\) infinitely often, and meets \(1/(q^2(\log q)^{1+\varepsilon})\) only finitely often. Lévy’s constant \(\pi^2/(12\log 2)\) and the Duffin–Schaeffer theorem are quoted. Volume 11 proves Lévy’s constant from the ergodic theorem.
- Euler’s expansion of \(e\) is quoted. The number \(e\) loses to a random number — `pb:econt`.
- \(\dim_H W(\tau)\le 2/\tau\), so the Liouville numbers have dimension \(0\) — `pb:wtau`. The matching lower bound is `pb:jarnik`.
- Numbers whose digits tend to infinity have dimension at most \(1/2\) — `pb:good`. Good’s equality is quoted.
- The set of numbers with digits in \(\{1,2\}\) — `pb:etwo`. The golden ratio is \(\varphi=(1+\sqrt 5)/2\) in this problem. The value \(0.53128\ldots\) is quoted from Jenkinson and Pollicott.
- Besicovitch–Eggleston: \(\dim_H B_p=H(p)/\log 2\) with \(H(p)=-p\log p-(1-p)\log(1-p)\) — `pb:eggleston`.
- The Cantor set contains uncountably many Liouville numbers, and the intersection has dimension \(0\) — `pb:cantorL`.
- For any distinct integers \(a_n\), \((a_n x)\) is equidistributed for almost every \(x\) — `pb:weylae`. The sequence \(n!\,x\) — `pb:factorial`. The Davenport–Erdős–LeVeque criterion — `pb:del`. Koksma: \((x^n)\) is equidistributed for almost every \(x>1\) — `pb:koksma`.
- The Fourier transform of the Cantor measure does not tend to \(0\) — `pb:cantorfourier`. The law of \((3^n x)\) under that measure is a preview of Volume 11 and is not used.
- Every real is a sum of two Liouville numbers — `pb:erdosL`. No measurable set cuts every interval in a fixed ratio — `pb:halves`. A set of positive measure contains an affine copy of every finite set — `pb:similar`.
- The geometric means of the digits oscillate on a comeagre null set — `pb:typicalcf`. Khinchin’s constant \(2.685\ldots\) is quoted. A Bernstein set is neither measurable nor meagre — `pb:bernsteinset`. The one-sentence gap is V7-011.

### Notation clashes with Volumes 1–6

- \(\N\) includes \(0\), as in Chapter 1. The Cantor-space definition in Chapter 4 sets \(\N=\{1,2,\ldots\}\) for the index of the tosses. The sentence says so.
- \(\log\) is the natural logarithm, the same function as Volume 6’s \(\log\) and as this volume’s \(\ln\). A ratio of logarithms, as in a Hausdorff dimension, does not depend on the base.
- \(\theta\) is an argument or an angle. Volume 6 uses \(\theta\) for Chebyshev’s function.
- \(\lambda\), and \(\lambda_d\), are Lebesgue measure. Volume 6 uses \(\Lambda\) for von Mangoldt’s function.
- \(\sigma\) is surface measure on the sphere in Chapter 9, and a singular measure in Chapter 11. Volume 6 uses \(\sigma_k(n)\) for the sum of \(k\)th powers of the divisors, and \(\sigma\) for the real part of \(s\).
- \(\varphi\) is Euler’s totient in the opening of Chapter 13, the golden ratio in `pb:etwo`, and a map or an angle elsewhere. Volumes 2 through 6 use \(\varphi(n)\) for the totient.
- \(C\) is the middle-thirds Cantor set from Chapter 2, and also a constant.
- \(\lvert\cdot\rvert_p\) is the \(p\)-adic absolute value. The ordinary absolute value keeps its Volume 1 meaning. The letter \(p\) remains a prime, as in Volume 2.
- \(e(t)=e^{2\pi it}\) and \(\lVert t\rVert\), the distance from \(t\) to \(\Z\), are the Volume 5 and Volume 6 conventions. They are named again at the start of Chapter 13.

## Volume 8 — Analysis

File names are under `volume8-analysis/chapters/`. The shared counter numbers theorems, propositions, lemmas, corollaries, definitions, and examples inside each chapter. Exercises use a separate counter and restart each chapter. The sixteen main chapters are numbered 1–16. The six appendices are A–F. \(\log\) is the natural logarithm, as in Volumes 6 and 7. In Chapter 16, \(e(t)=e^{2\pi it}\) and \(\lVert t\rVert\) is the distance to \(\Z\), the same conventions as Volumes 5 and 6.

### Chapter 1 — Banach spaces (`ch01-banach.tex`)

- A linear map between normed spaces is continuous exactly when it is bounded — `prop:boundedcont`, 1.1.
- Riesz’s lemma — `lem:riesz`, 1.2. The closed unit ball of an infinite-dimensional normed space is not compact — `thm:rieszcompact`, 1.3.
- Hahn–Banach, analytic form — `thm:hb`, 1.4. The norm-preserving extension — `cor:hbnorm`, 1.5. The geometric form — `thm:separation`, 1.6.
- Uniform boundedness — `thm:ubp`, 1.7. A continuous function whose Fourier series diverges at a point — `thm:fourierdiverge`, 1.8.
- Open mapping — `thm:openmapping`, 1.9. Closed graph — `thm:closedgraph`, 1.10.
- Duality of \(L^p\) for \(1\le p<\infty\) — `thm:lpdual`, 1.11. The dual of \(c_0\) — `prop:c0dual`, 1.12. Riesz–Markov — `thm:rieszmarkov`, 1.13.
- If \(\mu\) is \(\sigma\)-finite and \(1<p<\infty\), then \(L^p(\mu)\) is reflexive, and \(c_0\) is not — `prop:reflexive`, 1.14. A weakly convergent sequence is norm bounded, and \(\lVert x\rVert\le\liminf\lVert x_n\rVert\) — `prop:weakbounded`, 1.15.
- Banach–Alaoglu — `thm:alaoglu`, 1.16. The diagonal citation is V8-001. The step-function citation is V8-002. Eberlein–Šmulian is quoted.

### Chapter 2 — Hilbert spaces (`ch02-hilbert.tex`)

- The nearest point in a closed convex set — `thm:projection`, 2.1. Orthogonal decomposition — `cor:orthdecomp`, 2.2.
- Riesz–Fréchet — `thm:rieszrep`, 2.3. The closed unit ball is weakly compact — `cor:weakcompact`, 2.4.
- Orthonormal bases and Parseval — `thm:onb`, 2.5. An infinite-dimensional separable Hilbert space has a Hilbert basis and is isometrically isomorphic to \(\ell^2\) — `cor:separable`, 2.6.
- The exponentials \(e^{int}\) are a Hilbert basis of \(L^2(\mathbb T)\) for the inner product \((2\pi)^{-1}\int f\overline g\) — `thm:fourierl2`, 2.7. The Legendre polynomials are orthogonal with norm squared \(2/(2n+1)\), and the normalised family is a Hilbert basis of \(L^2[-1,1]\) — `prop:legendre`, 2.8.
- Kronecker–Weyl — `thm:kroneckerweyl`, 2.9. Von Neumann’s mean ergodic theorem — `thm:meanergodic`, 2.10.
- Von Neumann’s proof of Radon–Nikodym — `thm:rnvn`, 2.11. The Hahn-decomposition proof remains Volume 7, Theorem 11.4.
- Moore–Aronszajn — `thm:aronszajn`, 2.12. The complex Cauchy–Schwarz step is V8-003. A reproducing kernel is Hermitian and positive semi-definite.

### Chapter 3 — The spectral theorem (`linear-ch05-spectral.tex`)

- Normal, self-adjoint, unitary — `linear:def:normal`, 3.1. The spectral theorem for a normal matrix — `linear:thm:spectral`, 3.2. A Hermitian matrix has real eigenvalues and an orthonormal eigenbasis — `linear:cor:hermitian`, 3.3.
- Courant–Fischer — `linear:thm:courantfischer`, 3.4. Cauchy interlacing — `linear:thm:interlacing`, 3.5. Weyl’s inequalities — `linear:thm:weyl`, 3.6. Eigenvalue stability — `linear:cor:weylpert`, 3.7.
- Birkhoff’s theorem: a doubly stochastic matrix is a convex combination of permutation matrices — `linear:lem:birkhoff`, 3.8. Schur–Horn — `linear:thm:schurmaj`, 3.9.
- Horn’s theorem on spectra of sums, in the form proved here — `linear:thm:horn`, 3.10. Hoffman–Wielandt — `linear:thm:hoffmanwielandt`, 3.11.
- Rado’s identification of the permutohedron is V8-004. Horn’s conjecture is quoted.

### Chapter 4 — Singular values (`linear-ch06-svd.tex`)

- The singular-value decomposition — `linear:thm:svd`, 4.1. Dilation to a Hermitian matrix — `linear:prop:dilation`, 4.2. The polar decomposition — `linear:thm:polar`, 4.3.
- Ky Fan norms — `linear:prop:kyfannorm`, 4.4. Eckart–Young — `linear:thm:eckartyoung`, 4.5. Mirsky’s theorem for every unitarily invariant norm is quoted.
- The Moore–Penrose pseudoinverse — `linear:def:pinv`, 4.6, and `linear:thm:pinv`, 4.7. Principal components — `linear:thm:pca`, 4.8.
- The condition number — `linear:prop:condition`, 4.9. Orthogonal Procrustes — `linear:thm:procrustes`, 4.10.
- The low-rank caption is V8-005.

### Chapter 5 — Graphs (`linear-ch08-graphs.tex`)

- Spectra of the path, the cycle, the complete graph, and the cube — `linear:exa:spectra`, 5.1. The friendship theorem — `linear:thm:friendship`, 5.2.
- A strongly regular graph — `linear:def:srg`, 5.3. Its eigenvalues — `linear:thm:srg`, 5.4. The Hoffman–Singleton bound — `linear:thm:moore`, 5.5.
- Hoffman’s ratio bound — `linear:thm:hoffman`, 5.6. Erdős–Ko–Rado for pairs — `linear:exa:ekr`, 5.7.
- Graham–Pollak — `linear:thm:grahampollak`, 5.8. Huang’s signed adjacency theorem — `linear:thm:huang`, 5.9. Schwenk — `linear:prop:schwenk`, 5.10.
- The matrix-tree theorem is deferred to Volume 12, Appendix A.

### Chapter 6 — Cuts (`spectral-expansion.tex`)

- The Rayleigh quotient of the Laplacian — `expansion:lem:rayleigh`, 6.1. Cheeger’s inequality — `spectral:thm:cheeger`, 6.2.
- The expander mixing lemma — `spectral:lem:mixing`, 6.3. Alon–Boppana, in Nilli’s form — `spectral:thm:alonboppana`, 6.4.

### Chapter 7 — Expanders (`ch09-expanders.tex`)

- Mixing — `prop:mixing`, 7.1. The hitting property — `prop:hitting`, 7.2. The expander Chernoff bound — `thm:expchernoff`, 7.3.
- Non-backtracking polynomials — `lem:nbpoly`, 7.4. Kesten’s measure — `thm:kestenmeasure`, 7.5. McKay’s theorem — `thm:mckay`, 7.6. Serre’s gap — `cor:serre`, 7.7.
- The Ihara determinant — `prop:iharadet`, 7.8. Bass’s formula — `thm:bass`, 7.9. The Riemann hypothesis for graphs — `thm:graphRH`, 7.10. The prime-number theorem for graphs — `thm:graphpnt`, 7.11.
- Friedman, the LPS Ramanujan graphs, and the Huang–McKenzie–Yau proportion are quoted.

### Chapter 8 — Operators (`ch03-operators.tex`)

- The Hilbert-space adjoint — `prop:adjoint`, 8.1. Compact operators — `prop:compactops`, 8.2. A Hilbert–Schmidt kernel gives a compact operator — `ex:hilbertschmidt`, 8.3.
- The Fredholm alternative for a compact perturbation of the identity — `thm:fredholm`, 8.4. The Neumann series — `lem:neumann`, 8.5.
- The spectrum is nonempty and compact, and the spectral radius is the limit of \(\lVert A^n\rVert^{1/n}\) — `thm:spectrum`, 8.6. The Volterra operator has spectrum \(\{0\}\) — `ex:volterraex`, 8.7.
- Gelfand–Mazur — `lem:gelfandmazur`, 8.8. The Gelfand representation of a commutative Banach algebra — `thm:gelfand`, 8.9. Characters of the Wiener algebra — `prop:wcharacters`, 8.10.
- Wiener’s lemma — `thm:wiener`, 8.11.

### Chapter 9 — Compact operators (`ch04-spectral.tex`)

- The norm of a compact self-adjoint operator is a maximum of \(\lvert\langle Ax,x\rangle\rvert\) — `lem:sanorm`, 9.1. The spectrum is real, and the only possible accumulation point is \(0\) — `prop:saspec`, 9.2. A nonzero spectral value is an eigenvalue — `lem:eigenvalue`, 9.3.
- The spectral theorem — `thm:spectralcompact`, 9.4. The normal case — `cor:normal`, 9.5. Courant–Fischer again, for compact operators — `thm:minmax`, 9.6. Weyl’s perturbation bound — `cor:weylpert`, 9.7.
- The initial-value comparison — `lem:ivp`, 9.8. Green’s function — `lem:green`, 9.9. The sine basis — `lem:sines`, 9.10. Sturm–Liouville — `thm:sturm`, 9.11. Weyl’s law on an interval — `cor:weyllaw`, 9.12.
- Hilbert–Schmidt operators — `prop:hs`, 9.13. Mercer — `thm:mercer`, 9.14. Brownian covariance — `ex:minkernel`, 9.15.
- The continuous functional calculus — `thm:funcalc`, 9.16. The positive square root — `cor:sqrt`, 9.17.
- The unbounded spectral theorem, Ambartsumian, Borg, and Gordon–Webb–Wolpert are quoted.

### Chapter 10 — The Fourier transform (`ch05-fourier.tex`)

- The \(L^1\) transform — `prop:ftl1`, 10.1. Inversion — `thm:ftinv`, 10.2. The Schwartz class — `prop:schwartz`, 10.3. Plancherel — `thm:plancherel`, 10.4.
- Hermite functions — `thm:hermite`, 10.5. The three-lines lemma — `lem:threelines`, 10.6. Riesz–Thorin — `thm:rieszthorin`, 10.7. Hausdorff–Young — `cor:hausdorffyoung`, 10.8.
- A finite measure is determined by its Fourier transform — `thm:measuniq`, 10.9. The Cauchy law — `prop:cauchylaw`, 10.10. Means of Cauchy observations — `cor:cauchymean`, 10.11. The pointer to Volume 7, Exercise 10.2, is V8-011.
- Sampling — `thm:sampling`, 10.12. A nonzero \(L^2\) function and its transform cannot both have compact support — `cor:nocompact`, 10.13.
- Poisson summation for a lattice — `thm:poissonlattice`, 10.14. The theta function of a lattice — `cor:thetalattice`, 10.15.
- Bochner’s converse and Beckner’s constant are quoted.

### Chapter 11 — Distributions (`ch06-distributions.tex`)

- A distribution on an open set — definition at line 19, unlabelled, 11.1. The examples, including \(\delta\) — `ex:distexamples`, 11.2. Locally integrable functions — `prop:lloc`, 11.3.
- Distributional derivatives and multiplication by a smooth function — definition at line 57, unlabelled, 11.4. The examples — `ex:derivatives`, 11.5. A distribution with zero derivative is constant — `thm:zeroderiv`, 11.6. Smoothing — `prop:smoothing`, 11.7.
- The Schwartz class is already 10.3. A tempered distribution — definition at line 126, unlabelled, 11.8. Its Fourier transform — definition at line 134, unlabelled, 11.9, and `thm:ftsprime`, 11.10.
- Newton’s potential — `thm:newton`, 11.11. The Sobolev space \(H^s(\R)\) and \(W^{1,p}(I)\) — definition at line 202, unlabelled, 11.12. The embedding — `thm:sobolevR`, 11.13. The space \(W^{1,1}\) — `thm:w11`, 11.14. Rellich — `thm:rellich`, 11.15.
- A weak solution — definition at line 264, unlabelled, 11.16. Lax–Milgram — `thm:laxmilgram`, 11.17. Existence for the Sturm–Liouville weak form — `thm:weaksol`, 11.18. Céa’s lemma — `prop:cea`, 11.19.
- Malgrange–Ehrenpreis in general is quoted.

### Chapter 12 — Finite abelian groups (`ch07-finite.tex`)

- The dual of a product — `prop:dualprod`, 12.1. Duality: the bidual is the group, and there are \(\lvert G\rvert\) characters — `thm:finiteduality`, 12.2.
- The annihilator \(H^\perp\) — definition at line 39, unlabelled, 12.3. Its order — `prop:annihilator`, 12.4. This \(H^\perp\) is a subgroup of the dual, not the orthogonal complement of Chapter 2.
- Convolution — `prop:finiteconv`, 12.5. Poisson summation — `thm:poissonfinite`, 12.6. Splitting along a subgroup — `lem:split`, 12.7. The fast transform — `thm:fftgeneral`, 12.8.
- Donoho–Stark — `thm:donohostark`, 12.9. Chebotarev’s lemma on minors of the Fourier matrix — `lem:chebotarev`, 12.10. Tao’s uncertainty principle — `thm:tao`, 12.11.
- The Gauss sum — `lem:gaussa`, 12.12, and its multiplicativity — `lem:gaussmult`, 12.13. Quadratic reciprocity — `thm:qr`, 12.14.
- A cap-set count — `lem:capcount`, 12.15. Meshulam — `thm:meshulam`, 12.16. Blum–Luby–Rubinfeld — `thm:blr`, 12.17.

### Chapter 13 — Haar measure (`ch08-haar.tex`)

- A left Haar measure — definition at line 19, unlabelled, 13.1. Haar measure on \(GL_n\) — `prop:glnhaar`, 13.2. Uniqueness — `thm:haaruniq`, 13.3.
- Markov–Kakutani — `thm:markovkakutani`, 13.4. An abelian group is amenable — `cor:abelianamenable`, 13.5. Extensions of amenable groups — `prop:amenableext`, 13.6.
- Banach’s finitely additive measure on \(\Z\) — `thm:banachmeasure`, 13.7. The free group on two generators is paradoxical — `prop:f2paradox`, 13.8.
- A free rotation — `lem:freerot`, 13.9. Hausdorff’s paradox — `thm:hausdorff`, 13.10.
- Duals of \(\R\), \(\Z\), the circle and \(\Q_p\) — `thm:duals`, 13.11. Haar measure on \(\Q_p\) — `prop:haarqp`, 13.12. A character orthogonal to a ball — `lem:psiperp`, 13.13.
- \(\Q_p\) is self-dual — `thm:qpselfdual`, 13.14. Fourier analysis on \(\Q_p\) — `thm:qpfourier`, 13.15.
- The general Pontryagin–van Kampen theorem is quoted. Adèles are Volume 13.

### Chapter 14 — Complex analysis (`ch09-complex.tex`)

- Cauchy's theorem in homology form — `thm:globalcauchy`, 14.1. The residue theorem — `cor:globalresidue`, 14.2. The argument principle — `cor:hsc`, 14.3. A criterion for the winding — `prop:hsccriterion`, 14.4.
- Phragmén–Lindelöf — `thm:pl`, 14.5. Convexity of the growth exponent — `cor:convexity`, 14.6. Vertical sizes — `lem:verticalsizes`, 14.7. The convexity bound for \(\zeta\) — `thm:convexzeta`, 14.8.
- Canonical products — `lem:products`, 14.9. A zero count — `lem:zerocount`, 14.10. Hadamard factorisation — `thm:hadamardgen`, 14.11.
- Mellin inversion — `thm:mellininv`, 14.12. A theta sum — `ex:thetamellin`, 14.13. The maximum of geometric levels — `thm:maxgeom`, 14.14.
- Riemann mapping is Volume 9. Bourgain’s \(13/84\) is quoted.

### Chapter 15 — Tauberian theorems (`ch10-tauberian.tex`)

- Regular weights — `lem:regular`, 15.1. Abel’s theorem — `thm:abel`, 15.2. Cesàro implies Abel — `cor:cesaroabel`, 15.3. The series \(\sum(-1)^n\) — `ex:gregoryseries`, 15.4.
- Tauber’s theorem — `thm:tauber`, 15.5. Slowly varying — definition at line 100, unlabelled, 15.6. Hardy–Littlewood–Karamata — `thm:karamata`, 15.7. The power-series form — `cor:karamataseries`, 15.8. A converse to Abel for nonnegative coefficients — `cor:abelconverse`, 15.9.
- A local inverse in \(L^1(\R)\) — `lem:localinv`, 15.10. Translates of an \(L^1\) function with nowhere-zero transform are dense — `thm:wienerl1`, 15.11. Wiener’s Tauberian theorem — `thm:wienertaub`, 15.12.
- Wiener–Ikehara — `thm:ikehara`, 15.13. The prime number theorem — `cor:pntikehara`, 15.14. Progressions — `cor:pntapikehara`, 15.15. The holomorphy citation is V8-010.
- The Euler product for the indicator of sums of two squares — `prop:twosqeuler`, 15.16. The weighted count — `thm:twosqlog`, 15.17. The constant is \(K=2^{-1/2}\prod_{q\equiv 3\pmod 4}(1-q^{-2})^{-1/2}\).
- Littlewood’s \(O(1/n)\) converse, Landau’s unweighted theorem, and Delange’s extension are quoted.

### Chapter 16 — The values of zeta (`ch11-harder.tex`)

No statement in this chapter is numbered as a theorem. The problems are exercises of Chapter 16. Here \(B(x)=\{x\}-1/2\), and \(M(f)\) is the mean of an arithmetic function when the limit exists. The two `[Journey]` grades are V8-008. The two Problem Book pointers are V8-007.

- Selberg’s inequality — `pb:selberg`. Welch’s bound — `pb:welch`. Gerzon’s bound \(R\le n(n+1)/2\) — `pb:gerzon`.
- Halász’s inequality and a large-value bound for character sums — `pb:halasz`. Ingham’s separated-frequency bounds — `pb:ingham`. A mean-value bound without a logarithm — `pb:mvt`.
- The Christoffel kernel for Legendre polynomials — `pb:christoffel`. The Bergman space and \(\operatorname{area}f(\mathbb D)\ge\pi\) — `pb:bergman`. The Fock space — `pb:fock`. The Sobolev kernel on an interval — `pb:sobolev`. Square-summable Dirichlet series — `pb:dirichlet`.
- Franel’s formula — `pb:franel`. Ramanujan’s expansion of \(\sigma(n)/n\), with mean \(\tfrac52\zeta(3)\) — `pb:ramanujan`. The weighted zeta mean \(\log(2\pi)-\gamma\) — `pb:zetamellin`. One direction of Nyman–Beurling — `pb:nyman`.
- Bohr’s closed value set — `pb:bohrvalues`. Relatively dense returns — `pb:almostperiodic`. Van de Lune’s threshold — `pb:vandelune`. The long decimal is marked as a reported approximation.
- Khinchin recurrence — `pb:khinchinrec`. Arbitrarily slow ergodic averages — `pb:norate`. Atoms and Fourier energy — `pb:wiener`. Gebelein’s inequality — `pb:gebelein`.
- Four planar lines — `ex:v8c16a`. A constrained Fock minimiser — `ex:v8c16b`. An atom mixed with Cantor measure — `ex:v8c16c`. The Gaussian conditional operator — `ex:v8c16d`.

### Appendix A — Duality (`linear-ch01-duality.tex`)

- Steinitz exchange — `linear:lem:steinitz`, A.1. Dimension — `linear:thm:dim`, A.2. Grassmann’s formula is proved in the text after the theorem.
- The quotient — `linear:def:quotient`, A.3. The quotient theorems and rank–nullity — `linear:thm:quotient`, A.4. Three examples — `linear:ex:quotients`, A.5.
- The dual space — `linear:def:dual`, A.6. The dual basis — `linear:prop:dualbasis`, A.7. The double dual — `linear:thm:bidual`, A.8. Lagrange interpolation — `linear:ex:lagrange`, A.9. The trace pairing — `linear:prop:trace`, A.10.
- The annihilator \(S^\circ\) and the transpose — definition at line 149, unlabelled, A.11. Annihilators — `linear:thm:annihilator`, A.12. The transpose — `linear:thm:transpose`, A.13. The Fredholm alternative — `linear:cor:fredholm`, A.14.
- Lights Out — `linear:ex:lightsout`, A.15. Oddtown — `linear:thm:oddtown`, A.16. The triangular criterion — `linear:prop:triangular`, A.17.
- A hyperplane in \(M_n\), \(n\ge 2\), contains an invertible matrix — `linear:thm:hyperplane`, A.18. Unisolvent points — `linear:prop:unisolvent`, A.19.

### Appendix B — Determinants (`linear-ch02-volume.tex`)

- The shoelace formula — `linear:ex:shoelace`, B.1. Exterior powers — `linear:thm:exterior`, B.2. The compound matrix — `linear:def:compound`, B.3, and `linear:prop:compound`, B.4.
- Cauchy–Binet — `linear:thm:cauchybinet`, B.5. The sum of squared minors — `linear:cor:pythagoras`, B.6.
- Jacobi’s complementary minors — `linear:thm:jacobi`, B.7. The adjugate identity — `linear:cor:adjugate`, B.8. Desnanot–Jacobi — `linear:thm:desnanot`, B.9. Dodgson condensation — `linear:cor:dodgson`, B.10.
- Lindström–Gessel–Viennot — `linear:thm:lgv`, B.11. The planar non-intersection lemma — `linear:lem:planar`, B.12. A binomial determinant equal to \(1\) — `linear:ex:binomialdet`, B.13.
- Lozenge tilings of a hexagon — `linear:thm:lozenge`, B.14. MacMahon’s product is quoted. The alternating-sign enumeration is quoted.

### Appendix C — Eigenvalues (`linear-ch03-eigen.tex`)

- Eigenvectors for distinct eigenvalues are independent — `linear:prop:indep`, C.1. Triangularisation, and Schur’s orthonormal form — `linear:thm:schur`, C.2.
- Cayley–Hamilton over a commutative ring — `linear:thm:cayleyhamilton`, C.3. The minimal polynomial is defined in the text after the theorem.
- The kernel lemma — `linear:lem:kernels`, C.4. Generalised eigenspaces — `linear:thm:geneigen`, C.5. Diagonalisability — `linear:cor:diag`, C.6. The Dunford decomposition — `linear:thm:dunford`, C.7.
- Kernel increments of a nilpotent — `linear:lem:decreasing`, C.8. The Jordan form of a nilpotent — `linear:thm:jordannil`, C.9. The Jordan normal form — `linear:cor:jordan`, C.10. A matrix and its transpose are similar over \(\C\) — `linear:cor:transpose`, C.11.
- Commuting families — `linear:thm:commuting`, C.12. The matrix exponential — `linear:prop:exp`, C.13. The square-root solution is V8-009.
- Rational canonical form is Volume 3, Chapter 7.

### Appendix D — Inner products (`linear-ch04-inner.tex`)

- An inner product, linear in the first argument — `linear:def:inner`, D.1. Cauchy–Schwarz — `linear:thm:cs`, D.2. The triangle inequality — `linear:cor:triangle`, D.3.
- Orthonormal families — `linear:prop:orthfamily`, D.4. Gram–Schmidt — `linear:thm:gramschmidt`, D.5. The \(QR\) factorisation — `linear:cor:qr`, D.6.
- Orthogonal projection onto a finite-dimensional subspace — `linear:thm:projection`, D.7. Least squares — `linear:thm:lsq`, D.8. The line through three points — `linear:exa:line`, D.9. Gauss–Markov — `linear:thm:gaussmarkov`, D.10.
- Gram determinants — `linear:thm:gram`, D.11. Cauchy’s determinant — `linear:thm:cauchydet`, D.12. The Hilbert determinant and the distance from \(t^n\) — `linear:cor:hilbert`, D.13.
- Legendre polynomials by Rodrigues’s formula — `linear:exa:legendre`, D.14. The three-term recurrence — `linear:thm:recurrence`, D.15. The zeros — `linear:thm:zeros`, D.16. The Jacobi matrix — `linear:prop:jacobi`, D.17. Gauss quadrature — `linear:thm:gaussquad`, D.18.
- Finite-dimensional Riesz representation — `linear:thm:riesz`, D.19. The adjoint — `linear:prop:adjoint`, D.20. Unitary operators — `linear:thm:unitary`, D.21. A distance-preserving map of \(\R^n\) that fixes the origin is linear — `linear:thm:isometry`, D.22. Cholesky — `linear:cor:cholesky`, D.23.
- This finite-dimensional adjoint is the same construction as Chapter 8 once the dual has been identified with the space. Jordan–von Neumann’s criterion over \(\R\) is Exercise `linear:ex:jvn`. Müntz’s theorem in one direction is Exercise `linear:ex:muntz`. The converse is quoted.

### Appendix E — Matrix inequalities (`linear-ch11-inequalities.tex`)

- The Loewner order — `linear:prop:loewner`, E.1. Löwner–Heinz for the square root — `linear:thm:sqrtmonotone`, E.2. Loewner’s characterisation of operator-monotone functions is quoted.
- Schur complements — `linear:prop:schurcomplement`, E.3. Sylvester’s determinant identity — `linear:prop:detIAB`, E.4.
- Hadamard’s inequality — `linear:thm:hadamard`, E.5. The volume form — `linear:cor:hadamardvol`, E.6. Fischer — `linear:thm:fischer`, E.7. Minkowski’s determinant inequality — `linear:thm:minkowskidet`, E.8. Concavity of \(\log\det\) — `linear:thm:logdet`, E.9.
- The Hadamard product — `linear:def:hadamardproduct`, E.10. Schur’s product theorem — `linear:thm:schurproduct`, E.11. Entrywise exponentials and the Gaussian kernel — `linear:cor:entrywiseexp`, E.12.
- Gershgorin — `linear:thm:gershgorin`, E.13. Strict diagonal dominance — `linear:cor:diagdom`, E.14. The separated-union form of Gershgorin is quoted.
- Hilbert’s inequality, with constant \(\pi\) — `linear:thm:hilbertineq`, E.15. De Bruijn–Wilf’s asymptotic is quoted. The 2026 Hadamard-matrix report is a citation, not a proof.

### Appendix F — Linear dynamics (`linear-ch12-dynamics.tex`)

- A norm adapted to the spectral radius — `linear:lem:adaptednorm`, F.1. Powers tend to zero exactly when \(\rho(A)<1\) — `linear:thm:powers`, F.2. Gelfand’s formula — `linear:thm:gelfand`, F.3.
- Exponential stability — `linear:thm:stability`, F.4. Here stable means Hurwitz: every eigenvalue has negative real part. Lyapunov’s equation — `linear:thm:lyapunov`, F.5.
- Chebyshev acceleration — `linear:thm:chebyshevaccel`, F.6. The heavy ball on quadratics — `linear:thm:heavyball`, F.7. Nesterov’s theorem beyond quadratics is quoted.
- Kalman’s rank condition — `linear:thm:kalman`, F.8. The double integrator — `linear:exa:doubleintegrator`, F.9. Maxwell’s cubic — `linear:thm:maxwell`, F.10. The general Routh–Hurwitz criterion is quoted.

### Notation clashes with Volumes 1–7

- \(\lambda\) is an eigenvalue throughout the spectral chapters and the appendices. In Volume 7, \(\lambda\) and \(\lambda_d\) are Lebesgue measure. The two meet in Chapters 11 and 13, where Lebesgue measure keeps the Volume 7 name and eigenvalues keep \(\lambda\).
- \(\sigma\) is a singular value in Chapter 4, a Cesàro mean in Chapter 15, and the real part of a complex variable in Chapters 14–16. Volume 6 uses \(\sigma_k(n)\) for a sum of powers of divisors and \(\sigma\) for the real part of \(s\). The real-part use agrees with Volume 6.
- \(H\) is a Hilbert space in Chapters 1–2 and 16. \(H_n\) is the Hilbert matrix in Appendices D and E. \(H^s\) is a Sobolev space in Chapter 11. Volume 7 uses \(H\) for a distribution function only in passing.
- \(P\) is an orthogonal projection in Chapter 2 and Appendix D, a Legendre polynomial in Chapters 2 and 16 and Appendix D, and a Chebyshev polynomial in Appendix F. The Legendre \(P_n\) agrees with Appendix D’s example and with Chapter 2’s proposition.
- \(\chi\) is a Dirichlet character in Chapters 12, 15 and 16, and \(\chi_A\) is a characteristic polynomial in Appendix C. Volume 6 uses \(\chi\) for characters.
- \(\varphi\) remains Euler’s totient in Chapters 12 and 15. Elsewhere it is a test function or a linear form. Volume 7, Problem `pb:etwo`, uses \(\varphi\) for the golden ratio. That problem is not cited here.
- The annihilator of a subgroup is \(H^\perp\) in Chapter 12. The orthogonal complement is \(W^\perp\) in Chapter 2 and Appendix D. The annihilator of a subspace of a dual pair is \(S^\circ\) in Appendix A. The three are different objects, and each chapter says which.
- \(B(x)=\{x\}-1/2\) in Chapter 16. The same letter is a matrix in the appendices. The sawtooth is named at the start of Chapter 16.
- \(K\) is a reproducing kernel in Chapter 2, a compact set, and the Landau–Ramanujan constant in Chapter 15. The constant is \(K=0.76422365\ldots\), written out where it is used.
- \(\rho(A)\) is the spectral radius in Chapter 8 and Appendix F. In Chapter 15, \(\rho\) is the index of regular variation. In Chapter 16, \(\rho\) is a correlation.
- \(\log\) is the natural logarithm. A ratio of logarithms does not depend on the base. Volume 7’s \(\ln\) is the same function.
- \(e(t)=e^{2\pi it}\) and \(\lVert t\rVert\) are named again at the start of Chapter 16. They agree with Volumes 5 and 6.
