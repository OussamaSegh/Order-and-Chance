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
