# Concept ledger

One line per concept, notation, or named result, in the order the series introduces it. Later reviews check a use against the earliest line that actually states it. A forward pointer is not an introduction. Line numbers are the source on `main` at the start of this round (`15f2289c`).

Notation clashes with earlier entries are listed at the end of each volume. Volume 1 has no earlier volume.

## Volume 1

Book order: preface, then Chapters 0–10 as numbered by `volume1-first-principles/main.tex` (`\setcounter{chapter}{-1}`), then the field guide. Paths are under `volume1-first-principles/`.

### Notation and standing facts

- `\N={0,1,2,\ldots}`, `\N^*`, `\Z`, `\Q`, `\R`, completeness, well-ordering of `\N` — `chapters/ch00-language.tex:50`, and the preface list at `chapters/preface.tex:27–33`.
- `\forall`, `\exists`, scope, vacuous truth — `chapters/ch00-language.tex:91` and `:133`.
- Absolute value, irrational — Chapter 0, after the quantifiers.
- `\subseteq`, union, intersection, power set, ordered pair, function, interval, image, preimage, injective, surjective, bijective, equivalence, partition, partial order, least and minimal, supremum — Chapter 0. The pair and the open interval share parentheses; the text says which (`ch00-language.tex:418`).
- `\sum`, empty sum `0`, `\prod`, empty product `1`, `n!`, `0!=1` — `chapters/ch01-sums.tex:26` and the product paragraph.
- Prime, `a\mid b` for any integers, congruence, `\gcd`, `\operatorname{lcm}`, `v_p` — `chapters/ch01-sums.tex`, the divisibility section. The exponent test `d\mid n` iff `v_p(d)\le v_p(n)` is proved there, after unique factorisation.
- Fibonacci `F_0=0`, `F_1=1`; harmonic `H_n` — exercises of Chapter 1.
- Cardinality, derangement `D_n`, Catalan numbers, formal power series `[t^n]`, Euler’s totient as a count — Chapter 2.
- Limit of a sequence, derivative, continuity, `\exp`, `\ln`, real power `x^\alpha=\exp(\alpha\ln x)`, intermediate-value, extreme-value, Heine, Rolle, mean value — Chapter 3 (`ch05-sequences-series.tex`). The least positive zero of cosine and the least positive angle with cosine `-1` are proved there, before `prop:sincmp`.
- Integral as signed area, four rules, reversed limits, and the vanishing of a continuous nonnegative function with integral zero — the same chapter, after the mean value theorem.
- Poset, chain, antichain, Dilworth, Sperner, symmetric chain decomposition, Erdős–Ko–Rado — Chapter 4 (`orders.tex`). This chapter does not use a limit.
- `\C`, modulus, argument, `e^{i\theta}`, roots of unity, cyclotomic polynomial, group and subgroup — Chapter 5 (`ch02-complex-roots.tex`).
- Polynomial ring, formal derivative, factor theorem, Gauss’s lemma, Eisenstein — Chapter 6 (`ch03-polynomials.tex`).
- Vector space, rank–nullity, determinant, characteristic polynomial, diagonalisability, spectral theorem, Gram matrix, adjugate, Cayley–Hamilton — Chapter 7 (`ch07-linear-algebra.tex`).
- Taylor with remainder, l’Hôpital for `0/0`, Wallis integrals, Stirling’s constant — Chapter 8 (`ch06-integrals-taylor.tex`).
- Convexity, Jensen, AM–GM, Cauchy–Schwarz, Young, Hölder, power means, Carleman — Chapter 9 (`ch04-inequalities.tex`).
- Finite probability, expectation, the classical laws, Markov, Chebyshev, the weak law — Chapter 10 (`ch09-probability.tex`).

### Named results

Every `theorem`, `proposition`, `lemma`, `corollary`, `definition`, and `remark` environment, in book order. An unlabeled environment is marked `—`.

- `sym:numbers` remark [for the record] — `chapters/preface.tex:39`
- `sym:parity` definition [even and odd integers] — `chapters/ch00-language.tex:37`
- `prop:lang-negation` proposition [negating a quantified statement] — `chapters/ch00-language.tex:170`
- `prop:lang-sets` proposition [set operations and logic] — `chapters/ch00-language.tex:348`
- `—` definition [function] — `chapters/ch00-language.tex:403`
- `—` definition [interval notation] — `chapters/ch00-language.tex:417`
- `prop:lang-preimages` proposition [inverse images preserve set operations] — `chapters/ch00-language.tex:435`
- `—` definition [injective, surjective, bijective] — `chapters/ch00-language.tex:466`
- `thm:lang-inverse` theorem [the inverse criterion] — `chapters/ch00-language.tex:509`
- `—` definition [equivalence relation] — `chapters/ch00-language.tex:551`
- `thm:lang-partition` theorem [equivalence relations are partitions] — `chapters/ch00-language.tex:579`
- `—` definition [sigma notation] — `chapters/ch01-sums.tex:26`
- `—` proposition [finite progressions] — `chapters/ch01-sums.tex:49`
- `prop:telescope` proposition [telescoping sums] — `chapters/ch01-sums.tex:144`
- `—` definition [well ordering] — `chapters/ch01-sums.tex:199`
- `prop:induction` proposition [induction principles] — `chapters/ch01-sums.tex:207`
- `—` remark [how to write an induction] — `chapters/ch01-sums.tex:236`
- `prop:bernoulli` proposition [Bernoulli's inequality] — `chapters/ch01-sums.tex:270`
- `prop:binom` proposition — `chapters/ch01-sums.tex:299`
- `prop:vandermonde` proposition [Vandermonde] — `chapters/ch01-sums.tex:367`
- `prop:deltabinom` proposition — `chapters/ch01-sums.tex:404`
- `thm:newton` theorem [Newton's forward difference formula] — `chapters/ch01-sums.tex:419`
- `cor:sumpoly` corollary [sums of polynomials] — `chapters/ch01-sums.tex:451`
- `—` proposition [sum of the first cubes] — `chapters/ch01-sums.tex:486`
- `—` proposition [division with remainder] — `chapters/ch01-sums.tex:597`
- `—` proposition [B\'ezout's identity] — `chapters/ch01-sums.tex:619`
- `—` proposition [Euclid's lemma and unique factorisation] — `chapters/ch01-sums.tex:636`
- `ex:binomfrac` remark — `chapters/ch01-sums.tex:780`
- `—` definition [the three rules of counting] — `chapters/ch02-counting.tex:35`
- `prop:counts` proposition [basic counts] — `chapters/ch02-counting.tex:60`
- `thm:incexc` theorem [inclusion--exclusion] — `chapters/ch02-counting.tex:132`
- `prop:derang` proposition [derangements] — `chapters/ch02-counting.tex:180`
- `prop:paths` proposition [counting paths] — `chapters/ch02-counting.tex:258`
- `prop:real-triangle` proposition [real triangle inequalities] — `chapters/ch05-sequences-series.tex:40`
- `—` definition [limit of a sequence] — `chapters/ch05-sequences-series.tex:54`
- `—` definition [completeness of $\R$] — `chapters/ch05-sequences-series.tex:85`
- `prop:floor` proposition [the floor] — `chapters/ch05-sequences-series.tex:93`
- `prop:sqrt2` proposition [$\sqrt2$ is not rational] — `chapters/ch05-sequences-series.tex:120`
- `—` proposition [first properties of limits] — `chapters/ch05-sequences-series.tex:141`
- `sym:asymptotic` definition [the notations $o$, $O$ and $\sim$] — `chapters/ch05-sequences-series.tex:179`
- `prop:seqcrit` proposition [convergence criteria] — `chapters/ch05-sequences-series.tex:253`
- `thm:cesaro` theorem [Ces\`aro] — `chapters/ch05-sequences-series.tex:323`
- `—` definition [continuity and the derivative] — `chapters/ch05-sequences-series.tex:375`
- `prop:early-differentiation` proposition [elementary differentiation rules] — `chapters/ch05-sequences-series.tex:395`
- `thm:ivt` theorem [intermediate values] — `chapters/ch05-sequences-series.tex:451`
- `thm:evt` theorem [extreme values] — `chapters/ch05-sequences-series.tex:493`
- `thm:heine` theorem [Heine: uniform continuity] — `chapters/ch05-sequences-series.tex:512`
- `thm:mvt` theorem [Rolle, and the mean value theorem] — `chapters/ch05-sequences-series.tex:538`
- `prop:e-limit` proposition [the sequence for $e$] — `chapters/ch05-sequences-series.tex:570`
- `—` proposition [the first positive zeros of cosine] — `chapters/ch05-sequences-series.tex:593`
- `prop:sincmp` proposition [sine and tangent compared with the identity] — `chapters/ch05-sequences-series.tex:633`
- `prop:early-ftc` proposition [a first fundamental theorem] — `chapters/ch05-sequences-series.tex:674`
- `prop:posseries` proposition [series of non-negative terms] — `chapters/ch05-sequences-series.tex:707`
- `prop:signedseries` proposition [signed series] — `chapters/ch05-sequences-series.tex:768`
- `prop:safe-sums` proposition [when changing the order is safe] — `chapters/ch05-sequences-series.tex:825`
- `prop:gamma` proposition [Euler's constant] — `chapters/ch05-sequences-series.tex:842`
- `prop:stirlingshape` proposition [The shape of Stirling's formula] — `chapters/ch05-sequences-series.tex:874`
- `prop:abelsum` proposition [Abel's summation by parts] — `chapters/ch05-sequences-series.tex:931`
- `thm:dirichlettest` theorem [Dirichlet's test] — `chapters/ch05-sequences-series.tex:947`
- `orders:def:poset` definition — `chapters/orders.tex:34`
- `orders:prop:topsort` proposition [topological sorting] — `chapters/orders.tex:75`
- `orders:thm:mirsky` theorem [Mirsky, 1971] — `chapters/orders.tex:98`
- `orders:thm:dilworth` theorem [Dilworth, 1950] — `chapters/orders.tex:120`
- `orders:thm:es` theorem [Erd\H os and Szekeres, 1935] — `chapters/orders.tex:152`
- `—` remark — `chapters/orders.tex:178`
- `orders:thm:lym` theorem [LYM inequality] — `chapters/orders.tex:201`
- `orders:thm:scd` theorem [de Bruijn, van Ebbenhorst Tengbergen and Kruyswijk, 1951] — `chapters/orders.tex:240`
- `orders:thm:ekr` theorem [Erd\H os, Ko and Rado] — `chapters/orders.tex:275`
- `orders:def:wf` definition — `chapters/orders.tex:318`
- `orders:thm:wfind` theorem [well-founded induction] — `chapters/orders.tex:326`
- `orders:prop:lex` proposition — `chapters/orders.tex:346`
- `—` definition — `chapters/ch02-complex-roots.tex:38`
- `—` definition — `chapters/ch02-complex-roots.tex:71`
- `—` proposition [Brahmagupta's identity] — `chapters/ch02-complex-roots.tex:89`
- `—` proposition [triangle inequality] — `chapters/ch02-complex-roots.tex:110`
- `prop:expform` proposition [exponential form] — `chapters/ch02-complex-roots.tex:219`
- `—` remark [a square-root symbol has to choose] — `chapters/ch02-complex-roots.tex:357`
- `def:elementary-group` definition — `chapters/ch02-complex-roots.tex:367`
- `prop:roots` definition [polynomials, in five words] — `chapters/ch02-complex-roots.tex:393`
- `prop:roots` proposition [roots of unity] — `chapters/ch02-complex-roots.tex:397`
- `prop:orth` proposition [orthogonality] — `chapters/ch02-complex-roots.tex:445`
- `thm:filter` theorem [roots-of-unity filter] — `chapters/ch02-complex-roots.tex:525`
- `prop:equilateral` proposition [equilateral triangles] — `chapters/ch02-complex-roots.tex:562`
- `def:cyclotomic` definition — `chapters/ch02-complex-roots.tex:598`
- `prop:cyclotomic` proposition — `chapters/ch02-complex-roots.tex:606`
- `—` definition — `chapters/ch03-polynomials.tex:39`
- `—` definition [formal derivative] — `chapters/ch03-polynomials.tex:71`
- `prop:polydiv` proposition [Euclidean division] — `chapters/ch03-polynomials.tex:84`
- `prop:rootsfactor` proposition [roots] — `chapters/ch03-polynomials.tex:99`
- `prop:polynomial-bezout` proposition [polynomial gcd and B\'ezout] — `chapters/ch03-polynomials.tex:127`
- `thm:dalembert` theorem [d'Alembert--Gauss] — `chapters/ch03-polynomials.tex:155`
- `prop:viete` proposition [Vi\`ete's relations] — `chapters/ch03-polynomials.tex:198`
- `thm:lagrange` theorem [Lagrange] — `chapters/ch03-polynomials.tex:222`
- `prop:cheb` proposition — `chapters/ch03-polynomials.tex:267`
- `—` proposition [closed form] — `chapters/ch03-polynomials.tex:289`
- `prop:ratroot` proposition [rational roots] — `chapters/ch03-polynomials.tex:313`
- `prop:gausspoly` proposition [Gauss's lemma] — `chapters/ch03-polynomials.tex:326`
- `thm:eisenstein` theorem [Eisenstein's criterion] — `chapters/ch03-polynomials.tex:339`
- `prop:reduction` proposition [reduction modulo $p$] — `chapters/ch03-polynomials.tex:352`
- `prop:newtonid` proposition [Newton's identities] — `chapters/ch03-polynomials.tex:371`
- `thm:symmetric` theorem [fundamental theorem of symmetric polynomials] — `chapters/ch03-polynomials.tex:398`
- `thm:descartes` theorem [Descartes' rule of signs] — `chapters/ch03-polynomials.tex:426`
- `thm:gausslucas` theorem [Gauss--Lucas] — `chapters/ch03-polynomials.tex:447`
- `—` definition [vector space] — `chapters/ch07-linear-algebra.tex:31`
- `—` theorem [exchange lemma, and dimension] — `chapters/ch07-linear-algebra.tex:56`
- `prop:ranknullity` proposition [rank--nullity] — `chapters/ch07-linear-algebra.tex:97`
- `lem:sign` lemma [sign of a permutation] — `chapters/ch07-linear-algebra.tex:183`
- `thm:det` theorem [determinant] — `chapters/ch07-linear-algebra.tex:196`
- `—` proposition [Laplace expansion] — `chapters/ch07-linear-algebra.tex:238`
- `prop:vdm` proposition [Vandermonde] — `chapters/ch07-linear-algebra.tex:265`
- `prop:charpoly` definition [eigenvalues, eigenvectors, similarity] — `chapters/ch07-linear-algebra.tex:289`
- `prop:charpoly` proposition [characteristic polynomial] — `chapters/ch07-linear-algebra.tex:293`
- `thm:diag` theorem [diagonalisability] — `chapters/ch07-linear-algebra.tex:317`
- `—` remark — `chapters/ch07-linear-algebra.tex:332`
- `thm:gramschmidt` theorem [Gram--Schmidt and orthogonal projection] — `chapters/ch07-linear-algebra.tex:354`
- `thm:spectral` theorem [spectral theorem] — `chapters/ch07-linear-algebra.tex:399`
- `—` definition [quadratic forms and positivity] — `chapters/ch07-linear-algebra.tex:437`
- `—` definition [volume] — `chapters/ch07-linear-algebra.tex:447`
- `thm:gram` theorem [Gram determinant] — `chapters/ch07-linear-algebra.tex:458`
- `prop:adjugate` proposition [adjugate, Cramer's rule] — `chapters/ch07-linear-algebra.tex:490`
- `thm:cayleyhamilton` theorem [Cayley--Hamilton] — `chapters/ch07-linear-algebra.tex:507`
- `—` remark [small determinant, different question] — `chapters/ch07-linear-algebra.tex:586`
- `—` proposition [rules of differentiation] — `chapters/ch06-integrals-taylor.tex:26`
- `—` definition [improper integrals] — `chapters/ch06-integrals-taylor.tex:105`
- `prop:inttools` proposition [integration toolkit] — `chapters/ch06-integrals-taylor.tex:125`
- `thm:taylor` theorem [Taylor formulas] — `chapters/ch06-integrals-taylor.tex:171`
- `thm:lhopital` theorem [l'H\^opital's rule] — `chapters/ch06-integrals-taylor.tex:261`
- `prop:wallis` proposition — `chapters/ch06-integrals-taylor.tex:308`
- `prop:gaussianintegral` proposition [The Gaussian integral from Wallis] — `chapters/ch06-integrals-taylor.tex:350`
- `thm:stirlingC` theorem [Stirling's formula] — `chapters/ch06-integrals-taylor.tex:391`
- `prop:gammafn` proposition [the Gamma function] — `chapters/ch06-integrals-taylor.tex:424`
- `prop:quadrature` proposition [midpoint and trapezoid rules] — `chapters/ch06-integrals-taylor.tex:470`
- `prop:stirlingnext` proposition [Stirling, one term further] — `chapters/ch06-integrals-taylor.tex:514`
- `—` remark [one formula on each side of a singularity] — `chapters/ch06-integrals-taylor.tex:595`
- `prop:convex` proposition [convexity tests] — `chapters/ch04-inequalities.tex:115`
- `thm:jensen` theorem [Jensen] — `chapters/ch04-inequalities.tex:179`
- `thm:amgm` theorem [AM--GM] — `chapters/ch04-inequalities.tex:209`
- `thm:cs` theorem [Cauchy--Schwarz] — `chapters/ch04-inequalities.tex:278`
- `thm:young` theorem [Young] — `chapters/ch04-inequalities.tex:332`
- `thm:holder` theorem [H\"older] — `chapters/ch04-inequalities.tex:353`
- `prop:rearr` proposition [rearrangement] — `chapters/ch04-inequalities.tex:392`
- `thm:powermeans` theorem [power means] — `chapters/ch04-inequalities.tex:437`
- `prop:chebsum` proposition [Chebyshev's sum inequality] — `chapters/ch04-inequalities.tex:499`
- `thm:minkowski` theorem [Minkowski] — `chapters/ch04-inequalities.tex:526`
- `prop:gamma-convexity` proposition [log-convexity of Gamma] — `chapters/ch04-inequalities.tex:641`
- `prop:proba` proposition [first rules] — `chapters/ch09-probability.tex:177`
- `—` definition [independent random variables, covariance] — `chapters/ch09-probability.tex:244`
- `prop:varsum` proposition [products and sums] — `chapters/ch09-probability.tex:261`
- `prop:laws` proposition [the classical laws] — `chapters/ch09-probability.tex:311`
- `thm:chebyshev` theorem [Markov and Chebyshev] — `chapters/ch09-probability.tex:369`
- `thm:wlln` theorem [weak law of large numbers] — `chapters/ch09-probability.tex:388`
- `—` theorem [prime values of a polynomial] — `chapters/field-guide.tex:61`
- `—` proposition [legal words, by the first letter] — `chapters/field-guide.tex:136`
- `—` proposition [legal words, by closed walks] — `chapters/field-guide.tex:167`

### Clashes

None inside Volume 1. The letter `\mu` is not yet the Möbius function. The word “convex” means the chord property of a real function, not a convex set.
