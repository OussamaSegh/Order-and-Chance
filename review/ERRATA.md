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

## Review 5: Tome 6

A fifth independent pass, over Tome 6 (Spaces, 11 chapters, 27 figures, 11 notebooks). Every proof and every solution was read line by line, and the numerical claims were recomputed in Python: the Newton error bounds for √2 (e₅ ≤ 3.8·10⁻²², 24 correct digits from x₀ = 2), the 5-adic digits 2, 1, 2 of √−1 (57² + 1 = 26·125), the 29 topologies on three points (brute force over the 256 families of subsets), the Dottie number and its contraction ratio sin x* ≈ 0.67, the volumes 2, π, 4π/3, π²/2 of the unit balls, λ₁₀₀(B¹⁰⁰) ≈ 2.4·10⁻⁴⁰ against 2¹⁰⁰, and the Hausdorff dimensions log 2/log 3, log 9/log 10, log 8/log 3, log 3/log 2. Each of the fifteen promises of the Tome 6 plan was traced to the theorem that keeps it (least upper bound property, Ch. 1; exp, cos, sin and π, Ch. 2; intermediate value theorem, Ch. 3; extreme values, Heine, mean value theorem, Ch. 4; Riemann integral, Lebesgue's criterion, differentiation under the integral, Ch. 7; Lebesgue measure and independent sequences, Ch. 6; Tonelli–Fubini, |det T|, change of variables, the n-ball and the Gaussian density, Ch. 8; Hölder and Jensen, Ch. 9; uniform integrability and Vitali, Ch. 7; Kolmogorov's extension theorem, Ch. 11). Pointers to Tomes 0–4 were checked against the chapter files of those tomes, pointers to Tomes 7–12 and C3 against the series plan, and the dates in the storytelling openings (Cantor's letters to Dedekind of 1873, Fréchet 1906, Hausdorff 1914, Banach–Tarski 1924, Solovay 1970, Richardson's coastline data and Mandelbrot 1967, Prokhorov 1956) against the sources. All four PDF formats, the KDP print and cover files and the EPUB build without errors, with no undefined or multiply defined labels; all eleven notebooks run to completion and all their numbered references were matched against the built numbering.

### Tome 6

| Place | Severity | Problem | Fix |
|---|---|---|---|
| Ch. 7, proof of Lebesgue's criterion, Step 1 | math | "At most m intervals of Pₙ contain a point of P": a point of P that is also an endpoint of Pₙ lies in two closed intervals of Pₙ, so the count is 2m. The bound 2m·2M(b−a)/2ⁿ on the next line was already the right one. | "at most 2m intervals". |
| Ch. 3, Furstenberg's topology as an ultrametric (after the profinite remark) | ref | Pointed to Tome 1, Exercise 2.10; Furstenberg's proof is Tome 1, Exercise 2.8. | Exercise 2.8. |
| Ch. 6, after Borel's theorem | ref | Pointed to Tome 3, Chapter 4, for the strong law with a fourth moment; it is Tome 3, Chapter 6 (Theorem "strong law, fourth moment"). | Chapter 6. |
| Ch. 7, remark after the three convergence theorems | ref | Attributed Tannery's theorem to Tome 0, which does not state it (Tome 0 treats only sequences and series without a dominated limit theorem). | The pointer to Tome 0 is removed. |
| Ch. 4, definition of the derivative before the mean value theorem | ref | Pointed to Tome 0, Chapter 3, which is about polynomials; Tome 0 takes the derivative from the analysis course and defines it nowhere. | "(as throughout Tome 0)". |
| Ch. 2, proof of the theorem on exp, cos, sin and π, part (f) | ref | The length of a C¹ curve as ∫|γ'| was attributed to Tome 0; it is defined in Tome 4, Chapter 9 (complex line integrals). | Tome 4, Chapter 9. |
| Ch. 11, after Prokhorov's theorem | ref | Donsker's theorem was placed in Tome 10; the series plan puts the invariance principle in Tome 11 (The Markov property), where Chapter 4 of this tome already places the construction of Brownian motion. | Tome 11. |
| Ch. 1, storytelling opening | text | "Two weeks later Cantor had the answer": Cantor wrote to Dedekind on 29 November 1873 and sent the proof on 7 December 1873, eight days later. | "A week later". |
| Ch. 6, opening and remark after the Vitali set | text | Banach and Tarski (1924) are credited with five pieces; their paper gives finitely many, and five (the minimum) is Robinson's theorem of 1947. | "finitely many pieces", with Robinson's five noted in the remark. |
| Ch. 3, sources | text | Steen and Seebach's book has 143 examples: the four named ones "and 139 more". | 139. |

### Notebooks

| Notebook | Problem | Fix |
|---|---|---|
| Tome 6, ch. 5, exercises P5.1(c), P5.6 and its solution | Referred to "Proposition 5.13" for the comeagre set of non-normal numbers; that statement is Proposition 5.14 (5.13 is the theorem on Liouville numbers). | 5.14, three times. |
| Tome 6, ch. 1–11 | All eleven run; every other numbered reference matches the book. | — |

### Known and left as is

- The Tome 6 plan lists Lévy's continuity theorem among the exercises prepared for Tome 10 in Chapter 11; the chapter proves Helly's selection theorem instead and leaves Lévy's theorem to Tome 10, where the series plan places it ("characteristic functions and Lévy's continuity theorem"). Nothing in the text promises it earlier.
- Chapter 6 refers to amenability for Tome 8 (Shapes). The series plan's Tome 8 has matrix Lie groups and Haar measure but does not name amenability; the pointer is plausible and is left to the Part II writing thread.
- Part III threads cite Tome 6 chapter numbers (Ch. 6 Carathéodory and independent sequences, Ch. 7 convergence theorems and Vitali, Ch. 8 Fubini and change of variables, Ch. 9 Lᵖ, Ch. 10 Radon–Nikodym, Ch. 11 Riesz, portmanteau, Prokhorov, Kolmogorov, Helly). No chapter was renumbered by this review.

## Review: Tome S1

An independent pass over Tome S1 (Linear Algebra in Depth, 12 chapters, 12 notebooks). Every proof and every solution was read line by line, and the numerical claims were recomputed in Python independently of the notebooks: the Lights Out kernels (dimension 0 on 3×3, 4 on 4×4, 2 on 5×5), the lozenge counts T(2,2,2) = 20, T(3,3,3) = 980 and the 34-digit T(10,10,10), Dodgson's example (det −20), the Hilbert determinants 1/det Hₙ = 1, 12, 2160, 6048000, the parabola fit 3/35, 1/5, 6/7, the SVD of [[3,0],[4,5]], the PageRank values of Figure 7.2 recomputed from the figure's own edge list (C 0.351, A 0.329, B 0.169), the low-rank errors 0.30, 0.16, 0.07 recomputed from the pixel data of Figure 6.2, the Wielandt exponents (n−1)²+1 for n ≤ 10, Huang's 48 optimal nine-vertex sets among the 11440 of Q₄, A(8,4) = 16, the Schmidt entropy ≈ 0.843 and λ_max(H₃₀₀₀) ≈ 2.532. Pointers to Tomes 0–7, 12 and C1 were checked against the chapter files of those tomes, pointers to Tomes 8, 9, 11, C2, C4, C5, S2 and S3 against the series plan and the Tome C1 plan; the dates and attributions in the storytelling openings (Erdős–Rényi–Sós 1966, Nisan–Szegedy 1992, Huang's preprint of 1 July 2019, Schmidt 1907, Eckart–Young 1936, Wielandt 1950, Robbins–Rumsey, Schur 1911, de Bruijn–Wilf 1962) were checked against the sources, and the quotations in Chapter 8 against Aaronson's blog post. All four PDF formats, the KDP print and cover files and the EPUB build without errors, with no undefined or multiply defined labels; all twelve notebooks run to completion and every numbered reference in them was matched against the built numbering.

### Tome S1

| Place | Severity | Problem | Fix |
|---|---|---|---|
| Ch. 3, proof of Cayley–Hamilton | math / ref | The identity (XI − A)·adj(XI − A) = χ_A(X)·I over the ring K[X] was attributed to "Tome 0, Chapter 7", which never mentions the adjugate; nowhere in the series was A·adj(A) = (det A)·I proved over a commutative ring (Tome 2, Ch. 7 states it without proof). | New Corollary "adjugate identity" in Ch. 2 after Jacobi's theorem: the case k = 1 of Jacobi gives it for invertible matrices over ℚ, and a polynomial-identity argument extends it to every commutative ring. Cayley–Hamilton now cites that corollary. |
| Ch. 9, Delsarte's inequality | text | `\qedhere` inside a displayed equation; pandoc does not know it, so the EPUB rendered the whole display as raw TeX. | Removed; the box falls on the next line. |
| Ch. 8, epigraph and opening | text | The epigraph ("I think I have found a proof… surprisingly short") and the Aaronson quotations ("one of the most spectacular things", the elevator ride) could not be traced to any source; Aaronson's post of 2 July 2019 says neither. | Epigraph replaced by Huang's own account of the key idea (his comment on that post); Aaronson is now quoted with what he wrote: the conjecture was "one of the most frustrating and embarrassing open problems in all of combinatorics and theoretical computer science", and the "elementary 1.5-page argument" took him half an hour to read. |
| Ch. 6, opening | text | "Two psychologists, Carl Eckart and Gale Young": Eckart was a physicist (quantum mechanics); Young was the psychometrician. | Physicist and psychometrician, writing in Psychometrika. |
| Ch. 7, Wielandt's bound | text | "The first published proof is from 1964": the 1964 paper of Dulmage and Mendelsohn is about gaps in the exponent set; the first published proofs are Rosenblatt (1957) and Holladay–Varga (1958), Wielandt's own proof appearing only in Schneider's 2002 paper. | Corrected, with the sources entry expanded. |
| Ch. 9, solution of the Fourier matrix exercise | text | "Their multiplicities, roughly n/4 each, were found by Gauss": Gauss evaluated the trace (the quadratic Gauss sum); the exact multiplicities of ±1, ±i are due to McClellan and Parks (1972). | Attribution split accordingly. |

## Review 6: Tome 5

A sixth independent pass, over Tome 5 (Where It All Meets, 12 chapters, 12 notebooks). Every proof and every solution was read line by line. The numerical claims were recomputed in Python, independently of the notebooks: Mertens (θ(3000)/3000 = 0.977, ψ(3000)/3000 = 1.0004, R(10³) = −1.298, R(10⁵) = −1.329, R(10⁷) = −1.3324 and the limit −γ − 0.75536 = −1.33258, M = 0.2614972, H = 0.3157184, M + H = γ), the 359 visible points of the 24 × 24 grid, the median 8 and the 34% of τ(n) ≥ 14 below 10⁶, the coprime k-tuple densities 0.60838, 0.83205, 0.92399 against 1/ζ(k), the lattice-point error −43.65 at radius 1000, the constant C = 0.7869 in the 2^ω mean value, L(1, χ₋₃) = π/(3√3) and L(1, χ₋₄) = π/4, the mod 3 Mertens gap 0.675 = 0.368 + 0.308, the mod 4 race (ties at x = 2, 5, 17, 41, 461, then near 26 850; class 1 first ahead at 26861, for two integers; 3406 integers below 10⁷ where class 1 leads), π(10⁸) = 5 761 455 and Li − π = 753, A(10⁴), A(10⁶), A(10⁷) for ∑ μ(n)/n, p₁₀₀₀₀₀₀ = 15 485 863 and Cipolla's 0.29%, lcm(1, …, n)^{1/n} at n = 100, 1000, 10⁸, L'/L(1, χ₋₄) = 0.24561 and its closed form, π₂(10⁸) and the ratio 1.102, the Legendre-sieve ratios 0.998 and 1.034, B = ½ log 4π − 1 − γ/2 = −0.0230957 and −2B, the average zero gap 0.524 at T = 10⁶, Brun's constant from 1.7383570 + 0.1638312, the n² + 1 constant 0.6864, the Erdős–Kac exponent c = 0.086, the Montgomery–Soundararajan constant γ + log 2π − 1 = 1.415, and Deligne's bound for the 5133 primes below 50 000 (largest |x_p| = 0.9904 at p = 39089). Every pointer to Tomes 1–4 (theorems, propositions, corollaries, exercises and chapters) was resolved against the built numbering of those tomes and its statement compared with the use made of it; all are correct. The pointers to Tome 6 (Tonelli–Fubini, Ch. 8), Tome 12 (class number formula, Ch. 8; fundamental domain and the general theory of modular forms, Ch. 13) and Part III (mean values from the probabilistic point of view, Tome 14) agree with the Tome 6 plan, the Part III dependency map and the series plan. All four PDF formats, the KDP print and cover files and the EPUB build without errors, with no undefined or multiply defined labels and no overfull box; all twelve notebooks run to completion and their numbered references match the built numbering. The labels of Chapter 12 that Tome 12 builds on were not touched.

### Tome 5

| Place | Severity | Problem | Fix |
|---|---|---|---|
| Ch. 6, Stirling's formula (Theorem "Stirling's formula", part (b)) | math | Stated for 0 < δ < π with C_δ = (1 − cos δ)^{−3/2}, and the proof claims |u + s|² ≥ (1 − cos δ)(u² + r²) is "clear if c ≥ 0". For δ > π/2 the factor 1 − cos δ exceeds 1 and the inequality fails (take c = 0). Every use in the tome has δ ≤ π/2 (δ = arctan 2 in the zero-density proposition, δ = π/2 on vertical lines). | Statement restricted to 0 < δ ≤ π/2; the proof notes cos δ ≥ 0. |

### Notebooks

| Notebook | Problem | Fix |
|---|---|---|
| Tome S1, ch. 2 | The new corollary shifts the numbering of the theorem-style statements after Jacobi's theorem in Chapter 2 by one. | Numbered references in the notebook updated to the rebuilt numbering. |
| Tome S1, ch. 1–12 | All twelve run; every other numbered reference matches the book. | — |

### Known and left as is

- Chapter 1 (twice) points to "Tome C1, Chapter 11" for the linear algebra method and Fisher's inequality. Tome C1 has nine chapters on main so far; its own plan has twelve, with the linear algebra method as Chapter 11, and the computing thread agreed to that pointer. Left as is.
- Chapters 8, 9 and 11 point to Tome S3 for the Moore graph of degree 57, Paley graphs and the Hadamard conjecture, and Chapter 1 to Tome S2, Chapters 4 (projective duality) and 9 (Pick's theorem); neither tome exists yet, and all four pointers match the series plan.
- Chapter 11 quotes the de Bruijn–Wilf asymptotic π − λ_max(H_N) ~ π⁵/(2 log² N). At N = 3000 the formula gives 2.4 while the true gap is 0.61; the text only says the gap "behaves like" the formula, which is the asymptotic statement, and is left as is.

| Tome 5, ch. 1–12 | None found: all run, every numbered reference matches the book, every number quoted from a notebook in the text appears in that notebook's output. | — |

### Known and left as is

- Chapters 1–5 are being retold in storytelling style by the writing thread, so this review changes nothing in them. The one error found there, the caption of the race figure in Chapter 4 (it said the two counts were equal at x = 26861 "for the first time since x = 2"; they are equal at ten primes from 5 to 26921, and at 26861 class 1 leads), had already been corrected on main by the writing thread while this review ran; the corrected caption and think box agree with the recomputation.
- Chapter 2 quotes the constant term 0.4863 of P₃ and the mean 1.94358 of n/φ(n) "from the notebook"; both appear in the notebook's output and were not recomputed by a second method.
- The figures were not regenerated; the race figure itself (ch04-race) is consistent with the recomputed tie points.

## Review: Tome C1

What was checked and found correct: all twelve chapters, every proof and every solution
re-read, with particular care for the Bruck–Ryser proof (the elimination of the variables
y₁,…,y_v, the case c₁ = 1, and the final descent on primes ≡ 3 mod 4), the slice-rank
cap set proof (the diagonal lemma, the bound M_n ≤ ((1+x+x²)/x^{2/3})ⁿ and the value
2.7552 at x = 0.6), and Bose's and Skolem's constructions of triple systems (every pair
type, the half-idempotent quasigroup of Lemma 12.5, the block counts m(6m+1) and
n(3n−1)/2). Numbers recomputed in Python: the formula-size bound s ≤ 115 900 for n = 20,
the 73-clause saturation of PHP₂, the alkane counts 366 319 and 4 111 846 763, Lyndon words,
the partial fractions of L₀ in Chapter 4, the circulant Ramsey colourings, τ(Q₃) = 384 and
2000 for the Petersen graph, the Kirkman table (105 pairs once, every girl once a day),
the Fano lines, the Bruck–Ryser list up to 30, C(12,7) = 792 < 1000 ≤ C(13,7) = 1716 and the
random bound 59. Figures checked against their captions: the Mirsky labels (three terms
labelled 2), the Prüfer code (4,4,5,5,6), the flow of value 19 and its cut 10+9, the
Gale–Shapley run (both stable matchings), Kruskal's tree of cost 39. Every cross-tome
pointers checked: the numbered ones against the `.aux` files of Tomes 0–6, 12 and S1 (all
correct), the forward ones against the series plan and the computing dependency map.
Dates and attributions checked against sources: Kirkman 1847 and 1850, Steiner 1853,
Fisher 1940, Bose 1938–39, Skolem 1958, Ray-Chaudhuri–Wilson 1971, Kaski–Östergård 2004,
Euler 1782, Tarry 1900, Bose–Shrikhande–Parker 1959–60, MacNeish 1922, Bruck–Ryser 1949,
Lam–Thiel–Swiercz 1989, Bright et al. 2021, Katona and Kleitman–Spencer 1973, AETG 1997,
Segre 1955, Haken 1985, Shannon 1949, Göring 2000, Bernardi 2012, Friedman 2008, and the
journal references of every "Sources" section. All formats build (A4, phone, Kindle, EPUB,
KDP print and cover) with no multiply-defined labels and no undefined references; all
12 notebooks run without error and their printed values agree with the text (73 clauses,
7-clause formula unsatisfiable, 366 319 isomers, 384 and 2000 spanning trees, Table 12.1,
the MOLS counts, the Bruck–Ryser list). Not verifiable from here: the section number
§ 85 given for Russell's 1900 translation of the Leibniz epigraph (the Latin source,
Gerhardt VII, p. 200, is confirmed).

| Place | Severity | Problem | Fix |
|---|---|---|---|
| Ch. 5, tournaments | ref | Landau's king theorem dated 1951; the paper (*On dominance relations and the structure of animal societies* III, Bull. Math. Biophysics 15) is from 1953. | 1953. |
| Ch. 5, Menger's theorem | ref | The gap in Menger's 1927 proof was said to be filled by Kőnig in 1931. Kőnig's lecture of 1931 is the bipartite matching theorem; the complete proof of Menger's theorem is in his paper *Über trennende Knotenpunkte in Graphen*, Acta Sci. Math. Szeged 6, 1933. | 1933. |
| Ch. 7, planarity | ref | Robertson and Seymour's Graph Minors series counted as "twenty-three papers written from 1983 to 2004". Papers I–XX appeared 1983–2004 and XX contains the theorem; XXI–XXIII appeared 2009–2012. | "the twenty papers of their Graph Minors series, written from 1983 to 2004". |
| Ch. 1, first-order logic | ref | Pointer to "Tome C3, Chapter 4" for Gödel's completeness theorem; C3 is unwritten and the dependency map fixes no chapter number. | "Tome C3". |
| Ch. 12, Bruck–Ryser | ref | "Chowla extended it to all symmetric designs": the extension is the joint paper of Chowla and Ryser (1950), cited in the sources. | "Chowla and Ryser extended it to all symmetric designs in 1950." |

## Review: Tome 12

What was checked and found correct: all fourteen chapters, every proof and every
solution re-derived by hand (in particular the Chebotarev proof of Chapter 8 through
Deuring's reduction and the cyclotomic crossing, the local and global Kronecker–Weber
proofs, the Kummer-theory step bounding the ω-eigenspace of U₁/U₁ᵖ, the Riemann–Roch
proof for smooth plane curves, the p-adic filtration and the descent of Chapter 12,
Bombieri's bound and the twist argument of Chapter 13, Hecke's functional equation);
the admitted theorems (Artin reciprocity, the existence theorem, the Hilbert class
field) are labelled "admitted, not proved in this series", and every consequence drawn
from them is labelled "assuming Theorem …" (the x² + ny² theorem, the Hilbert class
fields of Q(√−5) and Q(√−23)); Mazur, Birch–Swinnerton-Dyer, Tunnell, modularity,
Weil's theorem for all curves, the Weil conjectures, Sato–Tate, Petersson and
Eichler–Shimura appear only in remarks. Numbers recomputed (Python, SymPy, PARI):
the minimal polynomial of √2 + ∛2, disc(X⁴ − 10X² + 1) = 147456, 7709321041217 =
37·683·305065927, the Minkowski bounds and class numbers of Chapter 3, Pell for 61,
the regulator of Q(ζ₇)⁺, the Gauss sums modulo 3, 4, 5, 8 and the root numbers,
Σ(a/47)a = −235, the h⁻ table up to 41, κ = π/√20 = 0.70248, the splitting examples
of Chapters 2 and 10 (x² + 14y² below 200: 23, 127, 137, 151; x² + 27y²: 31, 43, 109,
127, 157; the Hilbert class field of Q(√−23) and the roots 4, 13, 42 of X³ − X − 1
modulo 59), Gauss's cubic counts for p = 7, 13, 31, the Hasse figure (667 primes,
largest ratio 0.977), the Sato–Tate figure (78 496 primes), the area-6 triangles from
P, 2P, 4P on y² = x³ − 36x (hypotenuse 2094350404801/241717895860), the Nagell–Lutz
identity, the addition and duplication formulas, the torsion-7 point (3, 8), Bachet's
2P = (129/100, −383/1000), the a_p table of y² + y = x³ − x² against η(τ)²η(11τ)², the
coefficients of ΔE₄, j = q⁻¹ + 744 + 196884q + …, the Klein quartic (N₁ = 3, N₂ = 5,
N₃ = 24, P = 1 + 5T³ + 8T⁶), the F₅ count of y² = x³ − x + 1 and N₂ = 32, N₃ = 104.
Every pointer to Tomes 0, 1, 2, 4, 5 and 6 (about ninety, from "Tome 0, Proposition
3.7" to "Tome 6, Theorem 6.10") was checked against the rebuilt `.aux` files and the
statements themselves; all resolve to the result described. Pointers to Tomes 7, 9,
13 and 14 agree with the series plan and the Part III map. Dates and quotes checked
against sources: Jordan's letter to Minkowski (SMF page on Bayer-Fluckiger's talk),
Weil's letter from Rouen prison ("two or three months locked up every year", MacTutor),
Gauss's diary entry 146 of 9 July 1814, Taniyama's problem 12 (1955), Kronecker 1853,
Weber 1886, Hilbert 1896, Chevalley 1936, Iwasawa's letter 1952/1992, Roch's death at
26, Maclaurin 1720, Cramer 1750, Bézout 1779, Mordell 1922, Weil 1928, Nagell–Lutz
1935–37, Hasse 1933, Stepanov 1969, Bombieri 1973, Deligne 1974. Publishing rules:
author "SEGHAIER Oussama" only, "First edition", no mention of the repository. The
build is clean (no undefined or multiply defined label, no duplicate label, no EPUB
warning); all fourteen notebooks run without error, and every number quoted from a
notebook appears in its output.

### Tome 12

| Place | Severity | Problem | Fix |
|---|---|---|---|
| Ch. 2, figure of the cycle types of X⁵ − X − 1 | text | Caption said "17 981 primes p < 2·10⁵ not dividing 2869"; there are 17 984 primes below 2·10⁵ and 2869 = 19·151, so 17 982 (recounted with PARI: 150, 1450, 3041, 2270, 4487, 3038, 3546 primes for the seven cycle types; the bar heights are unchanged to three decimals). | 17 982. |
| Ch. 3, proof of Hermite's theorem | math (minor) | "All conjugates of θ have absolute value at most max(C_X, 1)": in the complex case the distinguished conjugate satisfies \|τ₁(θ)\|² ≤ C_X² + ¼, which can exceed max(C_X, 1). | Bound replaced by C_X + 1, with the reason; the coefficient bound becomes C(n,k)(C_X + 1)ᵏ. |
| Ch. 3, solution of the discriminant-bound exercise | text | (π/4)⁴(256/24)² ≈ 43.1; it is 43.29. | 43.3. |
| Ch. 12, associativity proof; Ch. 12, Mordell's descent; Ch. 13, twist inequality | text | Three displays overflow the A4 text width by 20–33 pt. | Broken over two lines. |

### Notebooks

| Notebook | Problem | Fix |
|---|---|---|
| Tome 12, ch. 1–14 | None found: all run, every number quoted from a notebook in the text appears in that notebook's output. | — |

### Known and left as is

- Chapter 8 quotes Washington's theorem numbers (5.34, 8.2, 9.3, 4.17) and Chapter 10 its Chapter 14; not re-checked against the book.
- Chapter 9 says Weil "added the additive version, the adèles"; the ring was first written down by Artin and Whaples (1945) as "valuation vectors" and the name is Weil's. Left as is.
- The figures were not regenerated; the cycle-type bars of Chapter 2 were generated with one prime fewer than the recount (3037 against 3038 for the type 2 3), a difference below the resolution of the drawing.

## Review: Tome 7

What was checked and found correct: all ten chapters of Analysis in Depth, every proof
and every solution re-read line by line, with particular care for Hahn–Banach and the
three Baire consequences, the mean ergodic theorem and Moore–Aronszajn, Gelfand's theory
and Wiener's lemma, the spectral theorem and Sturm–Liouville (the Green function bounds,
Weyl's law, Mercer), Plancherel, Hermite functions, Riesz–Thorin and the lattice Poisson
formula, Sobolev embeddings and Lax–Milgram, Chebotarev's minors lemma and Tao's
uncertainty principle, the slice-rank cap set bound (every inequality in the chain to
32·3ⁿ/n), the Haar measure on GL_n and on Q_p, Hausdorff's free rotations (the 3 ∤ b
induction), the Jordan curve theorem (Maehara's proof), Dixon's Cauchy theorem,
Phragmén–Lindelöf, Hadamard's factorisation, the Riemann mapping theorem, Mellin inversion,
Karamata's theorem, Wiener's L¹ theorem, the Wiener–Ikehara theorem and the Landau–
Ramanujan count. Numbers recomputed in Python independently of the notebooks: the
Sturm–Liouville eigenvalues 36.2, 70.4, 119.5, 188.3 for q = 60x; the Karhunen–Loève share
8/π² ≈ 81%; the cap set exponents 2.7552 (t = 0.6) and 2.7551 (t = 0.5931); y₁ ≈ 9.06 and
the wobble bound |P| < 1.6·10⁻⁶ in the maximum-of-geometrics theorem, with γ/ln 2 − ½ =
0.3327; the Landau–Ramanujan constant K = 0.76422365…; the oscillation bounds 0.29 and 1.71
of Exercise 10.6; the Lebesgue constants, the squares-in-Z_p densities p/(2(p+1)), the
Legendre fits and the Basel sums of the exercises. Every cross-tome pointer checked: the
numbered ones (about 150) against the `.aux` files of Tomes 0–6, 12 and S1, all correct, and
the forward ones (Tome 10 for Birkhoff and Lévy, Tome 11 for the Karhunen–Loève path,
Tome 12 for Tate's thesis, modular forms and Chebotarev density, Tome C5 for convex
optimisation) against the series plan. The promises of Tome 4 (general Cauchy, Jordan curve,
L² Fourier theory, Wiener–Ikehara) are all kept, and the chapters match the map that
Part III cites. Dates and attributions checked against sources: Hahn 1927 and Banach 1929,
Steinhaus 1919, Fréchet and Riesz 1907, von Neumann 1929, Fredholm 1903, Gelfand 1941,
Wiener 1932, Mercer 1909, Weyl's inequality 1912, Plancherel 1910, Lax–Milgram 1954,
Chebotarev 1926, Tao 2005, Meshulam 1995, Croot–Lev–Pach and Ellenberg–Gijswijt 2016,
the 2.2202ⁿ construction of 2024, Blum–Luby–Rubinfeld 1990, Haar 1933, Hausdorff 1914,
Jordan 1887 and Veblen 1905, Maehara 1984, Dixon 1971, Bourgain's 13/84, Riemann 1851
and Koebe's trick of 1912, Abel 1826, Tauber 1897 and his death in Theresienstadt, Littlewood
1911, Hardy–Littlewood 1914, Karamata 1930, Ikehara 1931, Landau 1908, Ramanujan's letter
of 16 January 1913, Hardy–Ramanujan 1918, Delange 1954, and the journal references of every
"Sources" section. All formats build (A4,
phone, Kindle, EPUB, KDP print and cover) with no multiply-defined labels and no undefined
references; all ten notebooks run.

### Tome 7

| Place | Severity | Problem | Fix |
|---|---|---|---|
| Ch. 1, duals of the classical spaces | text | "Frigyes Riesz proved in 1909 that there are no others" (the dual of L^p). Riesz's paper is Math. Ann. 69 (1910). | 1910. |
| Ch. 2, opening | text | "Erhard Schmidt who, in 1907, saw that all this was geometry", and Riesz–Fischer "the same year". Schmidt's paper is Rend. Circ. Mat. Palermo 25 (1908), as the chapter's own sources say; Riesz–Fischer is 1907. | 1908, and "the year before, in 1907". |
| Ch. 2, mean ergodic theorem | text | "von Neumann's came first, and the two men argued for years about who had done what" overstates the story: von Neumann proved his theorem first and told Birkhoff, Birkhoff's paper appeared first (December 1931, von Neumann's in January 1932), and the dispute is a historians' question rather than a years-long quarrel. | Rewritten with the dates; Birkhoff's paper and Zund's study (Historia Math. 29, 2002) added to the sources. |
| Ch. 5, interpolation | text | "In 1926 Marcel Riesz proved a general principle": the paper is Acta Math. 49 (1927), as cited in the sources. Thorin's paper is dated 1939 in the sources; it is 1938. | 1927; 1938. |
| Ch. 8, amenability | math | "an extension of the abelian group of rotations and reflections O(2)": O(2) is not abelian (a reflection and a rotation do not commute). The argument only needs the two-element extension of SO(2), which is what the sentence goes on to say. | "the group O(2) of rotations and reflections". |
| Ch. 8, Banach–Tarski remark | text | "S. Wagon and G. Tomkowicz" in the text, "Tomkowicz and Wagon" in the sources (the book's author order). | Tomkowicz and Wagon. |
| Ch. 10, Wiener's L¹ theorem (twice) | ref | Fourier inversion and uniqueness of transforms cited as Theorem 5.3, which is the Schwartz-space proposition; inversion is Theorem 5.2. | Theorem 5.2. |
| Ch. 10, solution of the quicksort exercise | math | "about 2·10⁶ log 10⁶ ≈ 2.8·10⁷ comparisons, against log₂(10⁶!) ≈ 1.9·10⁷: 38% more". The quoted numbers give 47% more; the exact C_n = 2(n+1)H_n − 4n is 2.48·10⁷ against 1.85·10⁷ (34% more), and 38.6% is the limit 2 ln 2 − 1 of the leading terms. | Rewritten with the exact count, a third more, and the limit 2 ln 2 ≈ 1.39. |

### Notebooks

| Notebook | Problem | Fix |
|---|---|---|
| Tome 7, ch. 9 | The convexity bound was cited as Theorem 9.17 (that is the zero-counting lemma) and the Γ-size lemma as Lemma 9.15(a) (that is the convexity theorem). | Theorem 9.15 and Lemma 9.14(a). |
| Tome 7, ch. 10 | Progressions cited as Corollary 10.16 (that is the Euler product proposition); Abel's theorem and its Cesàro corollary cited as Theorem 10.3 and Corollary 10.4. | Corollary 10.15; Theorem 10.2 and Corollary 10.3. |
| Tome 7, ch. 1–10 | All ten run; every other numbered reference matches the book. | — |

### Known and left as is

- Chapter 2 tells the story of Hilbert asking "what is a Hilbert space?" and flags it as untraceable; Chapter 10 paraphrases Abel's "devil's invention" and says so. Both are left as they are.
- Chapter 10 states Landau's unweighted count B(x) ~ Kx/√log x without proof and says so; only the logarithmically weighted version is proved.
- The figures were not regenerated; every number in a caption was recomputed and agrees.

## Review: Tome S2

An independent pass over Tome S2 (Geometry, 12 chapters, 12 notebooks). Every proof and every solution was read line by line and re-derived, with particular care for the four places the writer flagged: the associativity of the cubic group law through Cayley–Bacharach applied to the pair (three-line cubic, E) and the nine flexes via ψ = 12x·f − f'² (Ch. 8), the E8 construction, its 240 roots and the density π⁴/384 (Ch. 9), the Hadwiger–Ohmann proof of Brunn–Minkowski (Ch. 11), the four vertex theorem and Gauss–Bonnet for convex surfaces (Ch. 12); all four are correct. The numerical claims were recomputed in Python independently of the notebooks: Routh's formula in the book's convention, Bachet's 3P = (164323/29241, −66234835/5000211), the six real intersections of x² + y² = 3.24 with y = x³ − 3x, the Poncelet pair d² = 0.28, the Minkowski-sum areas of Figure 11.3 from the generator's triangle, the Soddy and Descartes examples and the gasket curvatures, the Fibonacci example of Gauss reduction, the curve table over F₅, Lazzarini's 1808/3408 = 16·213, the Reuleaux area, the point count of y² = x³ − x + 1 over F₁₀₁ and the spherical median of the last solution of Ch. 12 (the last two were wrong, see below). Pointers to Tomes 0, 1, 2, 3, 4, 12 and S1 were checked against the chapter files of those tomes (two pointers to Tome 0 were wrong, see below), the pointer to Tome 8 (SL₂(ℝ) and the hyperbolic plane) against the series plan. The dates and attributions of the storytelling openings (Morley 1899, Connes 1998, Klein 1872, Fedorov 1891, Pólya 1924, Escher 1922 and 1936, Soddy 1936, Descartes 1643, Hales 2005, Viazovska 2016, Shukhov 1896, Mazur 1977, Hasse 1933, Bachet 1621) and the quotations were checked against the sources (MacTutor for the Bolyai letter, mathpages and the Ladies' Diary of 1825 for Napoleon's theorem, Perrin's notes for Bachet). All four PDF formats, the KDP print and cover files and the EPUB build without errors, with no undefined or multiply defined labels and no overfull box over 10pt; all twelve notebooks run to completion after the fix below.

### Tome S2

| Place | Severity | Problem | Fix |
|---|---|---|---|
| Ch. 12, solution of the "no distance-preserving map" exercise | math | The idea line says the spherical median of an equilateral triangle is *shorter* than in the plane, and gives AM ≈ 0.43195 for a = 0.5. The expansion cos a / cos(a/2) = 1 − 3a²/8 − a⁴/128 + … is *smaller* than the planar cosine 1 − 3a²/8 + 3a⁴/128 + …, so the spherical median is longer: AM = arccos(cos 0.5 / cos 0.25) ≈ 0.43767 against 0.43301. The conclusion of the solution (the two values differ, so no map exists) is unaffected. | Idea line, expansion (a⁴ term added) and number corrected. |
| Ch. 8, text and caption of the finite-curve figure | math | "The 100 affine points of y² = x³ − x + 1 over F₁₀₁; with O, 101 points." The curve has 99 affine points and 100 points with O (the figure file itself, generated by the companion script, records 99); the Hasse gap is \|100 − 102\| = 2. | 99, 100 and 2 ≤ 2√101. |
| Ch. 1, lemma on equilateral triangles | math | "Multiplying by ω gives a + ωb + ω²c = 0" from c + ωa + ω²b = 0: multiplying by ω gives b + ω²a + ωc = 0; the stated form needs ω². | ω². |
| Ch. 1, solution of Euler's OI² = R² − 2Rr | ref | "The product IA·IM equals R² − OI² (the power of I, Tome 0)": Tome 0 has no power-of-a-point result. | Two-line inline proof (points I + tu on the circumcircle, product of the roots of the quadratic). |
| Ch. 3, circles orthogonal to the inversion circle | ref | The proof uses "the power of O with respect to γ" and the tangent–secant relation, which the tome never defines or proves. | Definition and proof (one sentence each) inserted at the start of the proof. |
| Ch. 2, classification of plane isometries | ref | "The orthogonal matrices are the rotations z ↦ e^{iθ}z and the reflections z ↦ e^{iθ}z̄ (Tome 0, Chapter 7)": Tome 0, Ch. 7 does not contain this. | Two-line inline proof from orthonormal columns. |
| Ch. 1, opening | text | "In 1822 Karl Feuerbach found that one circle passes through nine special points of every triangle and touches its four tangent circles": Feuerbach's 1822 paper is about the circle through the midpoints (and feet of the altitudes) touching the in- and excircles; the nine-point statement is Terquem's (1842). | Reworded with both names and dates. |
| Ch. 1, Napoleon's theorem | text | Laplace's reply was given as "The last thing we expected from you, General, was a lesson in geometry". | Wording as in Coxeter and Greitzer, Geometry Revisited, §3.3: "The last thing we want from you, General, is a lesson in geometry." |
| Ch. 10, epigraph | text | Bolyai's sentence was rearranged ("Out of nothing I have created a new, another world"). | Wording of the cited source (MacTutor): "I have created a new, another world out of nothing." |
| Ch. 7, sources | text | "the epigraph is its title", placed after Euler's 1750 paper, reads as if the epigraph were Euler's title; it shortens the title of Bradley and Stemkoski's article. | Reworded. |
| Ch. 8, sources | text | Perrin's lecture notes cited under the one-word title *Bachet*. | Full title *Autour de l'équation de Bachet*. |

### Notebooks

| Notebook | Problem | Fix |
|---|---|---|
| Tome S2, ch. 9 | The density plot labelled a curve `$\mathbb Z^n$`; matplotlib's mathtext requires braces and the cell raised `ParseFatalException`, so the plot never appeared. | `$\mathbb{Z}^n$` in the notebook and in its generator script; notebook re-executed. |
| Tome S2, ch. 1–8, 10–12 | All run to completion; the numbers printed agree with the chapters. | — |

## Erratum: Tome 3 (found while writing the problem books)

| Where | Kind | Problem | Fix |
|---|---|---|---|
| Ch. 6, Exercise 6.5 (`ex:poissonhalf`) | math | The next term of Ramanujan's expansion was given as 1/(3√(2πn)). At n = 100 the true value 0.526562 is matched by 1/2 + 2/(3√(2πn)) = 0.526596, not by 0.513298. | e^{−n} Σ_{k≤n} n^k/k! = 1/2 + 2/(3√(2πn)) + O(1/n). |
## Review: Tome C2

An independent pass over Tome C2 (Algorithms, 12 chapters, 12 notebooks). Every proof,
every algorithm, every running-time claim and every solution was read line by line and
re-derived: the master theorem and its lopsided and root-heavy variants, the amortised
analyses (dynamic array, binary counter, potential functions), the information
bound and Ford–Johnson counts, the 0–1 principle and the bitonic and odd–even networks,
LazySelect, the AVL height bound N(h) = F_{h+3} − 1, universal and perfect (FKS) hashing,
the log* bound for union–find, the backward analysis of skip lists, DFS and Tarjan's
strongly connected components, Dijkstra, Bellman–Ford and Johnson, the quadrangle
inequality for optimal search trees, Edmonds–Karp, Hopcroft–Karp, the blossom algorithm,
successive shortest paths, the simplex method with Bland's rule, strong duality, Farkas,
total unimodularity and matroid intersection, Karger–Stein, Schwartz–Zippel, the power of
two choices, Morris counters, count-min and AMS sketches, Toom–Cook, the Schönhage–Strassen
ring, Newton iteration, multipoint evaluation, Strassen inversion, Tonelli–Shanks, Cipolla,
Korselt, the Monier–Rabin bound, the full AKS proof with its constants, Pollard's rho and
p − 1, KMP, the Z-algorithm, Karp–Rabin, Aho–Corasick, suffix arrays and Kasai's LCP, the
Burrows–Wheeler transform and FM-index, HyperLogLog, the vertex-cover and set-cover
analyses, Christofides–Serdyukov, the Ibarra–Kim FPTAS, the 3/4 MAX-SAT rounding, the
Goemans–Williamson hyperplane constant (the six-digit values of θ₁, θ₂, cos θ₂ and h(θ₂)
recomputed), ski rental, the LRU phase argument and multiplicative weights. Numbers
recomputed in Python independently of the notebooks: the 17 comparisons of the quicksort
figure, the optimal search tree cost 62 for the frequencies 4,1,6,2,9,3,5, the maximum
load of 10⁶ balls, the Pollard rho figure (μ = 2, λ = 8 for x ↦ x² + 2 mod 97 from 2),
every pivot of the bakery dictionaries (one coefficient wrong, see below), the Klee–Minty
solution, the AKS lemmas, the number of strong liars of 703 (wrong in the text, see
below) and the pentagon value 5(1 + cos π/5)/2 ≈ 4.523. Every cross-tome pointer was
checked against the `.aux` files of Tomes 0, 1, 2, 3, 4, C1 and S1 (all correct) and the
four hard-coded in-tome numbers (Propositions 1.8, 1.9, 1.12 and Theorem 1.15) against the
tome's own `.aux` file (all correct); pointers to Tomes C3 and C5 carry no chapter number,
as agreed. Dates and attributions checked against sources: the Brooks quotation (the
original has the plural), the Hoare interview (Plus Magazine, 2021), Knuth's 1970 von
Neumann paper, Lamé 1844, Ford–Johnson 1959, Hoare 1961, Blum et al. 1973, Batcher 1968,
AKS 2002/2004, Christofides 1976, Serdyukov 1978, van Bevern–Slugina 2020, Karlin–Klein–
Oveis Gharan 2020/2021, Dinur–Safra 2005, Khot–Regev 2008, Feige 1998, Dinur–Steurer 2014,
Ibarra–Kim 1975, Håstad 2001, Goemans–Williamson 1994/1995, Khot–Kindler–Mossel–O'Donnell
2007, Sleator–Tarjan 1985, Belady 1966, Fiat et al. 1991, Littlestone–Warmuth 1994,
Freund–Schapire 1997, and the journal references of every "Sources" section. All formats
build (A4, phone, Kindle, EPUB, KDP print and cover, 272 printed pages) with no undefined
references, no multiply-defined labels and no overfull box over 10pt in the A4 build; all
12 notebooks run without error and their printed values agree with the text (the bakery
dictionaries, the 2ⁿ − 1 Dantzig and Fibonacci-like Bland pivot counts on Klee–Minty cubes,
162/702 strong liars for 703, the max-load tables, the comparison counts of Chapter 2).

### Tome C2

| Place | Severity | Problem | Fix |
|---|---|---|---|
| Ch. 7, the bakery after the second pivot | math | The second dictionary gives x₅ = 5/2 + 3/4 x₄ − 3/8 x₃. Substituting x₁ = 3 − 1/4 x₃ + 1/2 x₄ and x₂ = 3/2 + 1/8 x₃ − 3/4 x₄ into x₅ = 1 + x₁ − x₂ gives x₅ = 5/2 + 5/4 x₄ − 3/8 x₃ (the notebook prints the same). The optimum and the other rows are unaffected. | 5/4. |
| Ch. 10, after the Monier–Rabin theorem | math | "703 = 19·37 has 168 strong liars among 702." A direct count gives 162 (fraction 0.2308, as plotted in the liars figure and printed by the notebook). | 162. |
| Ch. 10, Solovay–Strassen | text | "A few months before Rabin, in 1977, Solovay and Strassen had published another randomised test": Chapter 8 dates Rabin's paper to 1976 and the Solovay–Strassen paper is from 1977, so the order was reversed. | "At about the same time, in 1977, …". |
| Ch. 12, opening | text | "For forty-five years nobody could beat the factor 3/2": 1976 to 2020 is forty-four years. | "For more than forty years". |
| Ch. 3, epigraph | text | Brooks's sentence was quoted with "flowchart … it'll be obvious"; the original (The Mythical Man-Month, Ch. 9) has "flowcharts … they'll be obvious". | Wording of the original. |
| Ch. 3, skip-list search length | text | The backward walk "until it reaches level L or the sentinel" is bounded by the waiting time for L heads, but once at the sentinel every step is up, not a coin flip; the bound still holds (those steps only shorten the walk) and the proof now says so. | One parenthesis. |
| Ch. 7, dual of matroid intersection | layout | The one-line display of the dual program overflowed the line by 14pt in the KDP print format and by 117pt on the phone format. | Objective and constraints on two lines. |

### Notebooks

| Notebook | Problem | Fix |
|---|---|---|
| Tome C2, ch. 1–12 | All run to completion (about 7 minutes in all); the numbers printed agree with the chapters after the two fixes above. The chapter 7 notebook reports two random programs on which SciPy's HiGHS disagrees with its exact simplex ("unbounded"); checked by hand and with HiGHS's presolve switched off, the programs are unbounded and the notebook is right. | — |

## Review: Tome 8

An independent pass over Tome 8 (Shapes, 10 chapters, 10 notebooks). Every proof and every solution was read line by line and re-derived, with extra care for the three chapters the coordinator flagged. Chapter 8: the left invariant form det(g)^{-n} ∧dg_ij on GL_n, the modular function |det Ad(h^{-1})|, uniqueness of the normalized Haar measure on a compact group, the QR sampling recipe with the phase correction, Weyl's integration formula with the constant 1/((2π)^n n!), Andreief's identity, Heine's Toeplitz determinant, Gaudin's lemma, the k-point correlations and Dyson's sine-kernel limit, and the solutions (the 126.5° angle, the ratio ≈ 600, the Toeplitz gap) are all correct; the date of the Montgomery–Dyson tea (6 April 1972) was checked against the IAS account. Chapter 9: the hyperbolic metric, geodesics, the polar formula 2π sinh r, the isometry group PSL₂(ℝ), the Iwasawa decomposition, the geodesic flow and its trace formula, the Farey tessellation and Series' cutting sequences (the L/R runs give the continued fraction), the closed geodesic of length 4 log(1+√2), the class-number examples −20 and −23 and the Klein quartic 336 are correct. Chapter 10: the uniqueness of the invariant measure dp dθ on lines, Bertrand's answer 1/2, Crofton's formula 2L, Buffon's noodle 2L/(πd), Cauchy's perimeter formula, Poincaré's 4L₁L₂, Cauchy's surface area formula A/4 and the solutions (the hat-box, Laplace's grid (4ld − l²)/(πd²), the sphere Crofton L/π) are correct. The numerical claims were recomputed independently of the notebooks (Gauss's triangle Hohenhagen–Brocken–Inselsberg and its ≈ 15″ excess, the hairy-ball and Euler-characteristic counts, the Nielsen–Schreier rank 1 + k(n−1), the Betti numbers of the surfaces, Weyl's law on the flat torus). Every numbered pointer to Tomes 1, 2, 5, 6, 7, 12, S1 and S2 was checked against the aux files of those tomes, and the unnumbered chapter pointers (Weyl's criterion, the Riemann–von Mangoldt formula, the explicit formula, Galois theory, the plate trick, Buffon and Bertrand in Tome 3, invariance of domain in Tome 6, Pell in Tome 1, noodles in Tome S2) against their chapter files: all correct. The dates and attributions of the openings (Riemann 1854, Whitney 1936 and 1944, Sard 1942, Morse 1939, Lie 1870, Frobenius 1877, Milnor 1978, Adams 1962, Thomson–Stokes 1850 and 1854, Cartan 1899, de Rham 1931, Chern 1944, Nielsen 1921 and Schreier 1927, Euler 1750 and 1758, Uhlenbeck–Goudsmit 1925, Hurwitz 1897, Weyl 1925, Haar 1933, Montgomery 1973, Odlyzko 1987, Poincaré's Coutances omnibus 1880, Series 1985, Artin 1924, Hopf 1936, Bertrand 1889, Poincaré 1896, Jaynes 1973, Crofton 1868, Hadwiger 1957) were checked. All four PDF formats, the KDP print and cover files and the EPUB build without errors, with no undefined or multiply defined labels, no overfull box and no pandoc warning; all ten notebooks run to completion and their printed numbers agree with the chapters.

### Tome 8

| Place | Severity | Problem | Fix |
|---|---|---|---|
| Ch. 9, after the polar-coordinates proposition | math | "A circle of radius 10 has length about 69 000 times its radius." The length is 2π sinh 10 ≈ 69 000; divided by the radius that is about 6 900 times. | "has length 2π sinh 10 ≈ 69 000, nearly seven thousand times its radius". |
| Ch. 2, sources | text | Lie's remark about mathematicians and prison was said to be "reported" by the MacTutor biography; the MacTutor page tells the arrest but has no such remark. | Attributed to Lie's letters as quoted by Stubhaug. |
| Ch. 1, sources | text | "F. Lafontaine, *An Introduction to Differential Manifolds*": the author is Jacques Lafontaine. | J. Lafontaine. |

### Notebooks

| Notebook | Problem | Fix |
|---|---|---|
| Tome 8, ch. 10 | Problem P10.3 asked to "verify Theorem 10.10"; Cauchy's surface area formula is Theorem 10.9 (the chapter has no 10.10). | Theorem 10.9. |
| Tome 8, ch. 1–10 | All ten run; every other numbered reference matches the book (Theorems 1.30, 2.10, 4.19, 5.16, 5.23, 7.8, 8.7, 8.15, 9.8, 10.1, 10.4, Propositions 1.22, 2.9, 5.11, 6.5, 7.3, 7.4, 9.3, Corollaries 3.21, 8.16, 10.2 and the exercises cited). The zeta-zero cell of ch. 8 takes about two minutes. | — |

### Known and left as is

- Chapter 1 quotes without proof that ℝP² does not embed in ℝ³, Chapter 3 that de Rham's theorem identifies de Rham cohomology with singular cohomology, Chapter 4 that the eigenfunctions of the round sphere are the spherical harmonics; each is flagged as quoted in the text.
- Chapter 8 presents Montgomery's pair correlation conjecture and Odlyzko's 1987 computation as what they are, a conjecture and numerical evidence; the companion notebook reproduces a small version (500 zeros).
- The figures were not regenerated; every number in a caption was recomputed and agrees.

## Review: Tome 10

What was checked and found correct: all twelve chapters, every proof and every
solution re-derived by hand, with extra care on the four places flagged for it:
Donsker's theorem through Skorokhod's embedding (Chapter 3: the exit-time estimates,
the strong Markov step, the tightness via the maximal inequality, Chung–Feller, the
arcsine law and the two laws of the iterated logarithm), Furstenberg's double
recurrence (Chapter 10: the compact/weakly mixing splitting of L², the σ-algebra of
the compact part, almost periodicity by pigeonhole on the torus, the Hilbert–Schmidt
argument for the weakly mixing part, van der Corput, the correspondence principle
and the extraction of an ergodic measure by successive maximisation), the mod-Poisson
local limit theorem (Chapter 11: Cauchy integrals on the circle of radius k/λ, the
bound 1 − cos θ ≥ 2θ²/π², k! ≤ e√k(k/e)ᵏ, uniformity in k) and Billingsley's theorem
by factorial moments (Chapter 12: the marked-cycle count n!/(ℓ₁⋯ℓ_K), the Riemann sum,
Chebyshev's bound on the number of tuples, Mertens on the scale log p/log x, the grid
argument around the hyperplane Σtᵢ = 1, the finite inversion of factorial moments).
Numbers recomputed (Python, mpmath): the random harmonic density g(0) = 0.2499944
and g(2) = 1/8, the Weldon dice χ² = 35.49 (p = 1.0·10⁻⁴), p̂ = 0.3377 and χ² = 8.18,
Pearson's odds 62 499:1, the near-birthday probability 0.4625, the insurer's gamma tail
1.84·10⁻¹⁵ and its Chernoff and Bahadur–Rao values, 1 − Φ(10) = 7.62·10⁻²⁴, the
Brandeis dice tilt (0.054, …, 0.348) and Λ*(4.5) = 0.178, the Chernoff information
0.005077, the Curie–Weiss magnetisations m*(1.5) = 0.8586 and m*(2) = 0.9575, the
Johnson–Lindenstrauss dimension 11 842, Berry–Esseen's 0.7523 + 2.2858, the hash and
run-test numbers, Pólya's constant 0.3405, Khinchin's 2.68545, Lévy's 1.18657,
e^{π²/(6 log 2)} = 10.73, H_{10⁶} = 14.39, e^{−γ}/Γ(2) = 0.56, e^{γ/2}/Γ(½) = 0.75,
log log 10⁸ = 2.91, 2·3⋯23 > 10⁸, the Simpson value 0.14718 and ρ(3) = 0.0486, the
Golomb–Dickman constant, the fourth cumulants −2 and −6/5, the broken-stick figure
(first cycle 251, nine cycles, coupling error below 0.0015) and the smooth-number
proportion 0.067 at u = 3. Every numbered pointer to Tomes 1, 3, 4, 5, 6, 7 and C1
(about ninety) was checked against the rebuilt `.aux` files and the statements
themselves; all resolve to the result described, except the one listed below.
Dates, anecdotes and citations checked against sources: Borel 1909, Steinhaus 1923,
Rademacher 1922, Khintchine–Kolmogorov 1925, Hewitt–Savage 1955, Etemadi 1981 (pages
119–122), Bernoulli's 25 550 trials, Weldon's 26 306 throws and Labby's 2009
recount (bias from the cubes, not the pips), Pearson 1900, Gauss's letter to Laplace
of 30 January 1812 and his diary of 1800, Kuzmin 1928, Lévy 1929/1936, Khinchin 1935,
Erdős–Turán 1936, Roth 1953, Szemerédi 1975, Furstenberg 1977 and the Abel Prize
2020, Host–Kra 2005, Green–Tao 2008, Keating–Snaith 2000, Jacod–Kowalski–Nikeghbali
2011, Goncharov 1944, Moser–Wyman 1958, Hwang 1995, Selberg 1954, Delange 1959/1971,
Golomb 1964, Shepp–Lloyd 1966, Dickman 1930, Billingsley 1972, Kingman 1975, Ewens
1972, Arratia–Tavaré 1992, de Bruijn 1951, Knuth–Trabb Pardo 1976, and the journal
references of all twelve "Sources" sections. Publishing rules: author "SEGHAIER
Oussama" only, "First edition", no mention of the repository. The build is clean (no
undefined or multiply defined label, no EPUB warning, no overfull box above 10 pt in
the paperback, Kindle and phone formats; the A4 format had ten, listed below); all
twelve notebooks run without error, and every number quoted from a notebook appears
in its output.

### Tome 10

| Place | Severity | Problem | Fix |
|---|---|---|---|
| Ch. 2, opening | text | "Etemadi published a proof in three pages": the paper (Z. Wahrsch. verw. Gebiete 55, 1981) is pages 119–122, four pages. | "four pages". |
| Ch. 2, solution of the Chung–Fuchs exercise | pointer | "By the strong Markov property at τ_x (Tome 3, Chapter 7)": Tome 3, Chapter 7 proves the walk starts afresh after a fixed time and after the first return, not after a general stopping time. | The one-line justification is given in place ({τ_x = m} depends only on X₁, …, X_m, and the later increments are independent of it); the pointer is dropped. |
| Ch. 11, solution of the Ω(N_s) exercise | math (minor) | "E[2^{Ω(N_s)}] = ∞ for s close to 1": the expectation is Π_p (1 − p^{−s})/(1 − 2p^{−s}), finite for every s > 1; it tends to infinity as s ↓ 1. | Statement corrected, with the p = 2 factor (1 − 2^{−s})/(1 − 2^{1−s}) that blows up. |
| Ch. 12, after Dickman's corollary | text | "ρ(3) ≈ 0.048" in the text against "ρ(3) = 0.049" in the caption; ρ(3) = 0.04861. | 0.049. |
| Ch. 3, strong Markov proof, Skorokhod E τ = E X², LIL upper bound; Ch. 6, the functions ψ(±w), Step 5 of the Stein solution bounds, the Kolmogorov-from-Wasserstein bound, the hypergeometric conditional second moment; Ch. 7, proof of the types lemma; Ch. 11, solution of the residues exercise; Ch. 12, proof of the small-cycles theorem | text | Ten displays (one inline formula) overflow the A4 text width by 10–166 pt; the narrow formats break them with `\qq`, A4 does not. | Broken over two lines in every format. |

### Notebooks

| Notebook | Problem | Fix |
|---|---|---|
| Tome 10, ch. 1–12 | None found: all run, every number quoted from a notebook in the text appears in that notebook's output. | — |

### Known and left as is

- Chapter 4, Weldon's table: the expected count for 7 successes is 1254.51, printed as 1254 (Pearson's own rounding, which makes the column add up to 26 306).
- The Golomb–Dickman constant is quoted to ten digits from the literature (0.6243299885); the notebook's trapezoidal solution of the delay equation gives 0.6243299882.
