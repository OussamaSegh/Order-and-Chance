# Errata and review log

Each finished tome is reviewed after it is written: every proof re-read, every
solution re-derived, every number in the text and the figure captions recomputed
in Python, every cross-reference checked against the built `.aux` files, and every
companion notebook executed. This file records what was found and how it was fixed.
Severity: **math** (a false statement or a gap in a proof), **ref** (a wrong pointer
or citation), **text** (clarity, typos).

## Review 1: Tomes 0 and 1

What was checked and found correct: all eight chapters of Tome 0 and twelve of Tome 1,
including every solution; the numbers quoted in figure captions (Runge errors 1.9 and
0.11, Taylor values of sin at π, det H₁₂ ≈ 2.6·10⁻⁷⁸, D₁₀/10! within 3·10⁻⁸ of 1/e,
the Poisson bars to four decimals, the Gaussian sandwich areas); π(10⁵) = 9592, Σ τ(n≤30) = 111,
N(6) = 113, N(10) = 317, the period of √61, the continued fraction of 0.24219,
e^{π√163}; all hardcoded cross-tome references ("Tome 0, Exercise 1.6", "Proposition 3.7", ...);
all 20 notebooks run without error.

### Tome 0

| Place | Severity | Problem | Fix |
|---|---|---|---|
| Ch. 2, closing remarks | math | Said the *sign* of the Gauss sum gives quadratic reciprocity in Tome 1. Tome 1 uses its square G² = ±p; the sign is a deeper theorem. | Corrected. |
| Ch. 3, d'Alembert–Gauss proof | math | ρ used both for the radius of the disc and for the modulus of −P(z₀)/c; the coefficients c_k and the degree n never introduced, and k reused; the bound "t < \|P(z₀)\|/M" breaks if M = 0; the real quotient in the factorisation over ℝ was not justified. | Radius renamed R, P = Σ c_j X^j introduced, the case M = 0 covered, and a sentence on uniqueness of Euclidean division added. |
| Ch. 3, hint to Exercise 3.5 | ref | Hardcoded "Exercise 1.6". | Now `\ref{ex:fermat}`. |
| Ch. 4, closing remarks | ref | "In Tome 4, Hölder is the key to Lᵖ spaces": Lᵖ spaces are in Tome 6. | Tome 6. |
| Ch. 5, Exercise 5.1 | math | The solution differentiated a power series termwise, "legitimate, Chapter 6", but no chapter proves this. | New self-contained solution by index shifting: A = Σ n/2ⁿ = 2, B = Σ n²/2ⁿ = 2A + 2 = 6; hint updated; the power-series route kept as an aside, flagged as not proved here. |
| Ch. 5, closing remarks | ref | Fubini placed in Tome 4; it is in Tome 6. | Tome 6. |
| Preface | text | "A few facts of topology" left implicit which results are admitted. | Lists them: intermediate values, extreme values, Heine, the mean value theorem, basic properties of exp, ln, cos, sin, π. |

### Tome 1

| Place | Severity | Problem | Fix |
|---|---|---|---|
| Ch. 2, Bertrand, small n | math | "n < q′ < 2q ≤ 2n" is false for n = 1 (q = 1, q′ = 2). | "q′ ≤ 2q", with the equality case noted. |
| Ch. 6, proof of reciprocity | text | Did not say why lattice points below the line automatically satisfy y ≤ (q−1)/2. | One clause added (qx/p < q/2). |
| Ch. 7, Exercise 7.2 | text | "find all n ≤ 2030 in {2021,…,2030}". | Simplified. |
| Ch. 7, sources | ref | Bourgain–Watt exponent "R^{0.6283} or so"; it is 517/824 ≈ 0.6275. | Corrected. |
| Ch. 7, three squares | ref | "Proved in Tome 5"; the series plan proves it in Tome 12 (Hasse–Minkowski). | Tome 12. |
| Ch. 8, Hurwitz's theorem | ref | Promised a proof in Tome 4 via Farey tessellations; Tome 4 does not contain it. | One-line idea of the proof and a pointer to Hardy–Wright. |
| Ch. 8, closing remarks | ref | Promised transcendence of e and π in Tome 4, which is not in its plan. | Dates (Hermite 1873, Lindemann 1882) instead of a promise. |
| Ch. 8, calendar solution | math | Claimed 31/128 is off by "one day in 5000 years". It is off by 2.5·10⁻⁶ day per year, one day in about 400 000 years, far below the precision of 0.24219 itself. | Corrected, with a remark on the drift of the year. |
| Ch. 9, Proposition 9.3 (chord method) | math | False without a hypothesis: on xy = 0, the line y = 0 lies in the conic and meets it in infinitely many points. | Added "Q has no factor of degree 1", and the proof now shows why g ≢ 0. |
| Ch. 9, Legendre and Mordell | ref | Placed in Tome 5; the plan has them in Tome 12. | Tome 12. |
| Ch. 10, Lemma 10.7 | text | 7 pt overfull display in the A4 PDF. | Line break. |
| Ch. 11, Proposition 11.8(d) | text | Letter m used both for the integer and for a coefficient. | a + bω. |
| Ch. 11, unit theorem, class number formula | ref | Placed in Tomes 2 and 5; the plan has them in Tome 12. | Tome 12. |
| Ch. 11, closing remarks | text | Confusing sentence on Exercise 11.8 "needing more than a congruence". | Rewritten: the answer is a congruence (p ≡ 1, 9 mod 20) but the proof needs the class group; for n = 14 or 27 no congruence suffices. |
| Ch. 11, sources | ref | Cox cited as 2nd ed. (Wiley 2013) here, 3rd ed. (AMS Chelsea 2022) elsewhere. | 3rd ed. everywhere. |

### Notebooks

| Notebook | Problem | Fix |
|---|---|---|
| Tome 0, ch. 2 | "Proposition 2.2" for orthogonality. | Proposition 2.4. |
| Tome 0, ch. 3 | "Lagrange (Theorem 3.2)". | Theorem 3.5. |
| Tome 0, ch. 8 | "Proposition 8.2" for the derangement formula; birthday attack averaged only 5 runs at 32 bits (result 27 % off the prediction); Tracy–Widom placed in Tome 5. | Proposition 8.3; 20 runs; Tome 11 (random matrices). |
| Tome 1, ch. 3 | CRT called "Theorem 3.4" (that is Wilson). | Theorem 3.5. |
| Tome 1, ch. 9 | Lebesgue's theorem called "Theorem 9.4". | Theorem 9.5. |
| Tome 1, ch. 11 | "Theorem 11.17" (does not exist) for h(−20) = 2; norm = index "proved in Tome 12" while the book says Tome 2. | Theorem 11.15; Tome 2. |

### Known and left as is

- A few overfull lines (up to 35 pt, mostly wide figures and long inline formulas) in the phone PDFs of both tomes; cosmetic.
- Tome 0, Ch. 4: the optimality of the constant e in Carleman's inequality is shown numerically (notebook), not proved; it is stated as a remark, not a theorem.
- The series plan lists Legendre's theorem on ax² + by² = cz² as the last section of Tome 1, Chapter 12; the chapter instead ends with the Hasse principle and Selmer's cubic. A candidate addition.

## Review 2: Tome 2

A second independent pass, this time over Tome 2 (Structures, 12 chapters, 13 figures, 12 notebooks). Every proof and every solution was read line by line, and the computations were redone by hand and in Python: the counts of Chapter 3 (necklaces, bracelets, cube colourings, graphs on four vertices), the 15-puzzle (every short loop is a cycle of the stated length, and the generated group has 15!/2 elements), the Landau values, the class sums of A₅, the Smith form of the figure (invariants 2, 6, 12), the minimal polynomial of √2 + ∛2, the discriminants, the Reed–Solomon decoding over F₇, the Gauss period for the 17-gon, the Gauss sum for ζ₇, the character tables of S₃, S₄ and A₅ (orthogonality relations), the Rubik's cube count, the 24 Hurwitz units and the four-square examples. All matched the text. The twelve notebooks run without error, and every theorem, proposition, example and section number they cite matches the built book. All pointers to Tomes 0 and 1 were checked against the actual chapters of those tomes, and pointers to later tomes against the series plan. The mathematics was found correct; the four items below are two reference bugs and two wording fixes.

### Tome 2

| Place | Severity | Problem | Fix |
|---|---|---|---|
| Ch. 3, Exercises 3.4 and 3.8 (hints and solutions) | ref | The label of Exercise 2.2 (G/Z(G) cyclic ⇒ G abelian) was reused by Exercise 11.4, so the four references in Chapter 3 printed "Exercise 11.4" (LaTeX warned "label multiply defined"). | Exercise 11.4 relabelled; the references now print 2.2. |
| Ch. 11, solution of Exercise 11.7 (A₅) | text | The two 3-dimensional characters were called ψ and ψ′, while the figure, the notebook and Chapter 12 call them ψ₃ and ψ₃′. | ψ₃, ψ₃′. |
| Ch. 4, closing remark | ref | Read as if Tome 3 proved the Diaconis–Shahshahani ½ n log n bound; the plan has riffle shuffles in Tome 3 and that proof in Tome 9. | Sentence split; "a proof that Tome 9 gives in full". |
| Ch. 7, closing remark | text | "(Chapter 11, Tome 5)" could be read as a chapter of Tome 5. | "(Chapter 11, then Tome 5)". |

### Notebooks

| Notebook | Problem | Fix |
|---|---|---|
| Tome 2, ch. 1–12 | None found: all run, all numbered references match the book. | — |

### Known and left as is

- Four displays are shrunk slightly in the phone PDF (the build reports them); cosmetic.

## Review 3: Tome 3

A third independent pass, over Tome 3 (Chance, 12 chapters, 39 figures, 12 notebooks). Every proof and every solution was read line by line, and the numerical claims were recomputed in Python: the birthday probabilities (q₂₃ = 0.4927, 99% at n = 57, 253 others for one's own birthday), the medical-test posterior 0.798, H₅₂ ≈ 4.54 and the standard deviation 1.71 of the cycle count, the coupon-collector values (50 H₅₀ ≈ 225, P(T > n ln n + 2n) ≈ 0.12), the prisoners' 1 − (H₁₀₀ − H₅₀) ≈ 0.31, the two roots 0.8193 and 0.9994 of Lotka's law and its mean 1.26, the Poisson(2) survival probability 0.7968, the Chernoff/Hoeffding/exact tail of Bin(1000, ½) at 600 (I = 0.0201, 1.8·10⁻⁹, 1.36·10⁻¹⁰), the 26 492 samples, the Bernstein errors 0.19, 0.10, 0.05, the longest-run statistics (mean ≈ 7, 97% for a run of 6), the Bloom filter 0.6185^(m/n) and the 111 runs of the median trick, the hundred dice (exact 0.00151 against 0.00155), the delta-method constant 1.64, the roulette values (0.0045, 3667 bets, 0.37), the arcsine 0.09, the Pólya return constant F ≈ 0.3405 and 0.52 expected returns, the knight (336, 168, 42), the Bayer–Diaconis total variation table for 52 cards and the 8.6 of the asymptotic formula, the rising-sequence variance (n + 1)/12, the stationary law (4/11, 4/11, 3/11) of the figure chain, ABRACADABRA's 26¹¹ + 26⁴ + 26 and 116 million years, the empty-bins example (367 879, true standard deviation 312, 2e^(−12.5) < 10⁻⁵), Black–Scholes (d± = 0.35, 0.15, C ≈ 10.45, P ≈ 5.57) and the binomial prices 12.16, 10.25, 10.43, 10.449, the Ramsey bounds R(10) > 100, R(20) > 5817 and 115 by alteration, the tournament counts 0.89 and 0.96, the M/M/1 means 1, 9, 99, and Le Cam's 5·10⁻³. All matched the text. Every theorem, proposition, lemma and corollary is followed by its proof (the only admitted facts are the two labelled "Admitted (proved in Tome 6)" in Chapter 5), every solution has its *How to find it* and *Write-up*, there are no duplicate or undefined labels, the three PDFs and the EPUB build cleanly, the twelve notebooks run without error, and every theorem, proposition, example, exercise, figure and section number they cite matches the built book. All pointers to Tomes 0 and 2 were checked against the actual chapters of those tomes (Propositions 4.1(b), 5.1(c) and 8.3, Theorems 5.6, 6.4 and 7.7, Exercises 3.7 and 6.7 of Tome 0; Chapter 11 of Tome 2), and pointers to Tomes 4, 6, 9, 10 and 11 against the series plan. The mathematics was found correct; the three items below are two reference fixes and a wording fix.

### Tome 3

| Place | Severity | Problem | Fix |
|---|---|---|---|
| Ch. 3, remark after Lotka's law | ref | Said that Chapter 10 "shows" that the limit of Zₙ/mⁿ is positive on survival under E[ξ ln ξ] < ∞ (Kesten–Stigum). Chapter 10 proves this only under a finite offspring variance (Theorem 10.22) and quotes Kesten–Stigum in a remark. | Reworded: Chapter 10 proves it for finite variance; Kesten–Stigum, quoted there, weakens the condition. |
| Ch. 10, remark after the convergence theorem | ref | Uniform integrability was pointed to Tome 6 only; the series plan has uniformly integrable martingales in Tome 10 (Martingales II). | "studied with the Lebesgue integral in Tome 6, and uniformly integrable martingales in Tome 10". |
| Ch. 1, solution of Exercise 1.8 (secretary problem), part (b) | text | The upper bound log((n−1)/(r−2)) for the harmonic sum needs r ≥ 3, which the surrounding range x ≥ 1/√n guarantees but the text did not say. | "for r ≥ 3" added. |

### Notebooks

| Notebook | Problem | Fix |
|---|---|---|
| Tome 3, ch. 1–12 | None found: all run, all numbered references match the book. | — |

### Known and left as is

- The series plan quotes "about 320 pages" for Tome 3; the A4 build is 165 pages. The plan's figure was an estimate, not a target.
- Pointers to "Tome 10" for Lévy's continuity theorem, Berry–Esseen and Cramér's theorem, to "Tome 11" for Itô's formula, the strong Markov property and the continuous Dirichlet problem, to "Tome 9" for Diaconis–Shahshahani, and to "Tome 4" for Fourier inversion all agree with the series plan.

## Review 4: Tome 4

A fourth independent pass, over Tome 4 (Calculation, 12 chapters, 29 figures, 12 notebooks). Every proof and every solution was read line by line, and the numerical claims were recomputed in Python: Σ_{k<1000} k⁵ = 166 167 083 333 250 000 and the von Staudt–Clausen check B₁₂ + ½ + ⅓ + ⅕ + ⅐ + 1/13 = 1, the 4563 ways to pay one euro, p(200) = 3 972 999 029 388, the connected-graph counts 1, 1, 4, 38, 728, the Motzkin, involution and Bell numbers, Viète's polygon areas 2, 2.83, 3.06, Si(π) = 1.8519 and the Gibbs constants 1.17897, 0.179, 0.0895, the minimum of Γ at 1.4616 (value 0.8856), V₅ = 8π²/15 ≈ 5.264, V₂₀ ≈ 0.026, the sphere areas 31.01, 33.07, 32.47 for n = 6, 7, 8, ϖ = 2.62205755429211981 and Γ(¼) = 3.62560990822, the primes 83969 = 41·2¹¹ + 1 and 998 244 353 with primitive root 3, the NTT example modulo 17 (all four vectors), the Karatsuba-versus-FFT table, θ(100) − 1, the ten zeta zeros below 50, ζ(½) = −1.4604, Euler's divergent series (f(1) = 0.5963473623, f(0.1) = 0.9156333394, errors 1.77·10⁻⁴ at K = 10 and 8·10⁻³ at K = 20), the H₁₀ expansion (error 4.1·10⁻¹¹ against the next term 4.2·10⁻¹¹), the best Stirling-series errors 10⁻³·⁵, 10⁻⁶·⁴, 10⁻¹² at x = 1, 2, 4 and the size e^(−2πx)/(π√x) of the smallest term, the ζ(3) exercise (1.2020569031742, bound 1.05·10⁻¹⁰, error 1.5·10⁻¹¹), the 2-regular graph counts 1, 3, 12, 70, 465 and the 2 % at n = 30, ln p(n)/(π√(2n/3)) = 0.74, 0.89, 0.92, the Motzkin ratio 0.988 at n = 200, the AGM differences for M(1, √2) and M(1, 0.01), the ellipse perimeter L(2, 1) = 9.68844822054767619842, the Earth-orbit factor 0.99993027, Ramanujan's errors 3·10⁻⁶ and 0.5 %, the Brent–Salamin digit counts 1, 4, 9, 20, 42, 85, 173, 347, e₀ ≈ 0.0518 and the 10⁻¹³⁹⁶ after ten steps, the pendulum factors 18.0 %, 0.19 % and "almost four", a₅ = 1.19814023473559220744, and the AGM-logarithm errors 6.8·10⁻³, 1.25·10⁻⁴, 3.6·10⁻¹². All matched the text. Every theorem, proposition, lemma and corollary is followed by its proof (the only admitted fact is Tonelli for the Ritelli integral, labelled "Admitted (proved in Tome 6)"), every solution has its *How to find it* and *Write-up*, there are no duplicate or undefined labels, the three PDFs (141 pages A4) and the EPUB build cleanly, the twelve notebooks run without error, and every theorem, proposition, example, exercise, figure and section number they cite matches the built book. All numbered pointers to Tomes 0–3 were checked against the built numbering of those tomes (Propositions 2.1 and 5.5, Theorems 3.3, 5.6 and 6.4, Exercises 2.5, 2.7, 2.8 and 6.6 of Tome 0; Theorems 4.4 and 5.3, Proposition 4.5, Exercises 4.8 and 6.7 of Tome 1; Theorem 11.14 of Tome 2; Exercise 2.3 of Tome 3) and all chapter-level pointers against the chapter files; pointers to Tomes 5, 6, 7, 11, 12 and 13 were checked against the series plan and the Tome 6 plan. The mathematics was found correct; the three items below are one reference fix and two wording fixes.

### Tome 4

| Place | Severity | Problem | Fix |
|---|---|---|---|
| Ch. 6, remark after the equidistribution corollary | ref | Said only that Tome 5 uses Weyl sums. The review moved the pointer to Tome 13 following the series plan, but the detailed Tome 5 plan keeps this promise in its Chapter 11 (Weyl differencing, van der Corput, equidistribution of polynomial sequences), so the writing thread restored Tome 5 when merging. | "Tome 5, Chapter 11 estimates Weyl sums … proving the equidistribution of n²α". |
| Ch. 1, after the difference rule for falling powers, Δ x^(m) = m x^(m−1) | text | "For m = −1 the rule would give Δ x^(0) = 0": it is m = 0 that gives this; the point is that no m reaches the falling power x^(−1). | "To reach x^(−1) one would need m = 0, and the rule then gives Δ x^(0) = 0". |
| Ch. 2, Franklin's proof of the pentagonal theorem ("A maps 𝒜 to ℬ") | text | The check that μ is not exceptional used only the case s(μ) = σ(μ) + 1 without saying why s(μ) = σ(μ) is excluded (it was shown two lines earlier that s(μ) > σ(μ)). | The case split is now spelled out. |

### Notebooks

| Notebook | Problem | Fix |
|---|---|---|
| Tome 4, ch. 1–12 | None found: all run, all numbered references match the book. | — |

### Known and left as is

- Chapter 9 promises the homology form of Cauchy's theorem and the Jordan curve theorem for Tome 7, and Chapter 11 promises the Hardy–Ramanujan asymptotic for p(n) by the circle method for Tome 13. The plan's Tome 7 lists "Complex analysis II" and its Tome 13 the circle method without naming these results; the Part II writing thread has recorded both promises, so they are left as is.
- Pointers to Tome 6 (Tonelli for Ritelli's integral, Fubini and change of variables for Γ(x)Γ(y) = B(x, y)Γ(x + y), Lebesgue measure and Cavalieri for the n-ball) all appear in the Tome 6 plan's promise table; pointers to Tome 5 (ζ(1 + it) ≠ 0 and the prime number theorem, Mertens, sums of squares through theta functions), Tome 11 (Brownian motion) and Tome 12 (elliptic functions and modular forms) agree with the series plan.
