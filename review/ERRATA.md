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
