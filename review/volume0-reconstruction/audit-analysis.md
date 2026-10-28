# Analysis review for Volume 0 reconstruction

Reviewer: analysis subagent. Date: 28 October 2026.
Baseline source: commit `3259d462860e13150fc6cb15ecb0e3109f95b5ed`.
This report is an audit, not manuscript implementation. Source line numbers refer
to the original eight-chapter baseline.

## Scope and evidence

Read all 672 lines of `ch04-inequalities.tex`, all 856 lines of
`ch05-sequences-series.tex`, and all 712 lines of `ch06-integrals-taylor.tex`,
including every result, proof, example, workshop, exercise, hint, solution,
challenge and source list. Read the existing factual-review report and inspected
the relevant figure sources. Long figure coordinate lists were inspected partly
through a structural summary rather than point by point. No PDF was rendered by
this reviewer; layout, clipping, readability, asset licensing and visual QA remain
the integration/build reviewer's responsibility. No new external historical-source
verification was performed. Retained references are evidence of attribution, not
an independent revalidation of every biographical assertion.

Counts independently extracted from source:

| Original chapter | Numbered theorems | Numbered propositions | Unnumbered propositions | Exercises/hints/solutions |
|---|---:|---:|---:|---:|
| 4 Inequalities | 5 | 3 | 2 | 17/17/17 |
| 5 Sequences, Series and Limits | 7 | 5 | 1 | 15/15/15 |
| 6 Integrals and Taylor Formulas | 3 | 5 | 1 | 15/15/15 |

All 47 exercise statements have matching hints and solutions in these sources.
This is a count and reading result, not formal proof certification.

## Existing coverage: preserve before adding

**Inequalities.** Rules of signs, absolute-value triangle and reverse triangle
inequalities, Bernoulli, convexity by chords and derivatives, tangent support,
finite Jensen, weighted AM–GM with equality, real and integral Cauchy–Schwarz with
zero-vector cases, Engel form, rearrangement, all real power means including
limits at zero and infinity, Chebyshev's sum inequality, Young/Hölder in a solved
exercise, Minkowski, quantitative slack and stability workshop, Carleman with
sharpness, Hardy outlook, entropy and polygon optimisation. These already supply
nearly all requested inequality topics. Do not recreate them wholesale.

**Sequences.** Quantified convergence, infinite divergence, algebra of limits,
squeeze, subsequences, little-o/big-O/equivalence and cancellation warning,
geometric series, supremum completeness, monotone and adjacent sequences,
Bolzano–Weierstrass by peaks, Cauchy criterion, fixed-point recursion, Cesàro,
positive series and comparison/integral/ratio tests, absolute and alternating
convergence, Cauchy product, harmonic asymptotics/Euler's constant, Stirling,
continuity including sequential characterisation, IVT/EVT/Heine/Rolle/MVT with
proofs, Abel summation, Dirichlet/Abel tests with tail bound, accelerated logarithm
workshop, condensation, Stolz, Kempner, Riemann rearrangement and a dilogarithmic
Euler acceleration. The source is far richer than its section headings suggest.

**Calculus.** Derivative rules with proof including the careful chain-rule zero
case and inverse continuity, explicit elementary-function contract, antiderivative
methods, improper integrals, FTC/parts/substitution/Riemann sums, Taylor with
integral remainder and quantitative/Young forms, Wallis, Stirling constant and
first correction, l'Hôpital in 0/0 and infinity/infinity forms, Gamma and its
log-convexity, midpoint/trapezoid estimates, Simpson outlook, rational Gaussian
approximation workshop, Gaussian integral by a squeeze, irrationality of e and pi,
Beta integrals, Frullani, sophomore's dream, Basel/transcendence outlooks. The
reconstruction should mainly repair placement and a few precision gaps.

## Findings, classified and actionable

### Essential corrections

1. **Incorrect rounded harmonic values.** `ch05:727` prints
   `H_12366 ≈ 9.99997` and `H_12367 ≈ 10.00005`. Independent 60-digit evaluation
   gives `9.999962147921639...` and `10.000043008275807...`. To five decimal
   places use `9.99996` and `10.00004`. The first index 12367 itself is correct.

2. **Cauchy criterion should not presuppose a real supremum of an unbounded set.**
   `ch05:129` writes `sup_{p,q≥n}|u_p-u_q| → 0` for an arbitrary sequence. For
   unbounded sequences these suprema do not exist in R, and extended reals have
   not been introduced. State the quantified criterion directly:
   for every epsilon>0, some N makes |u_p-u_q|≤epsilon for p,q≥N.
   The proof at lines 139–140 already proves this formulation. Alternatively
   explicitly allow +infinity, but that is unnecessary machinery.

3. **Periodic quadrature exercise lacks its requested proof of the numerical
   guarantee.** `ch06:420` says “show” ten points give eight decimals. Solution
   `ch06:616` gives numerical comparisons and an Euler–Maclaurin outlook, neither
   an explicit finite error bound nor a derivation of the stated decimal
   guarantee. A rigorous and useful roots-of-unity bridge is available:
   write `e^{cos t}=e^{e^{it}/2}e^{e^{-it}/2}`. The Fourier coefficient for m≥0 is
   `c_m=sum_{j≥0} 1/[2^{m+2j}j!(m+j)!]`, bounded above by
   `e^{1/4}/(2^m m!)`. Absolute convergence justifies finite filtering and termwise
   integration, which can also be established by uniform tail bounds here.
   Consequently `T_10-I=4pi sum_{l≥1}c_{10l}` and
   `0<T_10-I<4.35×10^-9`. Prove a geometric bound for the tail of the displayed
   positive factorial series. This supplies a mathematical guarantee without
   invoking systematic Fourier theory or Euler–Maclaurin. The actual difference
   is `3.45945653506638...×10^-9`. If this is too much for a two-star exercise,
   separate numerical observation from a three-star certified bridge; do not
   leave a numerical comparison labelled as a proof.

4. **Clarify Taylor intervals when x<a.** `ch06:124,136,145` use `[a,x]` for
   a segment even though the theorem allows x<a. Define the segment as
   `[min(a,x),max(a,x)]`, keeping the oriented integral from a to x. This is a
   notation/domain correction; the proof's absolute-value argument is sound.

5. **Nonnegative AM–GM use should be acknowledged.** The main AM–GM statement
   `ch04:147–157` assumes strictly positive inputs, while Carleman's statement
   `ch04:368–375` permits zeros and its solution `ch04:575` applies AM–GM to them.
   Extend the unweighted finite inequality to nonnegative inputs with the simple
   observation that a zero makes its left side zero. No limiting theorem is
   needed. The Carleman conclusion itself is correct.

6. **Unproved infinite nonnegative interchange.** Carleman's proof `ch04:577`
   and divisor-series identity `ch05:824–825` use unrestricted nonnegative double
   summation. The current latter text expressly defers the rule to Volume 3.
   Volume 0 should give a short elementary lemma from monotone partial sums:
   both iterated sums equal the supremum of finite rectangle sums. It is already
   within the completeness framework, and avoids a silent foundational exception.
   Similarly, the claim that absolute sums behave like finite ones at
   `ch05:590–592` deserves a short finite-tail rearrangement argument if relied on.

### Essential dependency repairs for the new order

7. **Bernoulli before geometric decay.** `ch05:103` relies on the proof currently
   in inequalities. Move its elementary statement/proof (`ch04:67–73`) to the
   induction chapter or prove it locally before geometric sums; the inequality
   chapter can reference it. This is a genuine prerequisite, not added breadth.

8. **Real sequences precede complex numbers.** `ch05:213,215,219,227` explicitly
   use C and real/imaginary parts before the proposed new complex chapter. State
   the initial signed-series/Cauchy-product theorems over R. Preserve the complex
   extension and exponential addition proof in the complex chapter with links
   back to the real theorem. Do not delete the mathematical content. This avoids
   assuming complex numbers in the chapter that supplies their series theory.

9. **Taylor is currently used before being established.** The sine-iteration
   solution `ch05:675–679` uses a sixth-order small-angle remainder; the Stirling
   solution `ch05:710–713` uses a fourth-order logarithmic remainder. These are
   correct formulas but exceed the named elementary-function assumptions. For
   Stirling, integrate the finite geometric identity for 1/(1+t):
   `log(1+x)=x-x²/2+x³/3+R`, `|R|≤x⁴/4` for 0≤x≤1. The integral/FTC contract
   must be named at this point, or move this exercise/proof to calculus and leave
   an explicit deferred result. For the sine recurrence, solve part (a) now and
   visibly mark (b) as a return problem after Taylor; alternatively move the
   complete exercise to calculus as a bridge. Retain the old ID and solution.
   An explicit cross-reference is acceptable; pretending Taylor is already part
   of the proved limits calculus is not.

10. **Gamma log-convexity would depend on a later inequality chapter.**
    `ch06:246,256–260` invokes Young/Hölder and convexity from current Ch.4,
    moved to new Ch.8. Prefer retain Gamma's definition, convergence, recurrence
    and half-integer values in calculus, and move statement/proof (c) as a
    calculus–inequalities bridge in Ch.8. Preserve its content and mention that
    log-convexity is proved there. A viable alternative is prove Young locally by
    minimising `a^p/p-ab+b^q/q` in a, then prove integral Hölder here; later
    inequalities can refer back. That duplicates less if arranged carefully, but
    the first option gives the clearer conceptual ownership.

11. **Minkowski/Hölder prerequisite lives in solutions.** `ch04:284–293`
    explicitly cites the proof of Hölder in the exercise solutions. This is not
    a hidden dependency, but require the reader to solve/read that lemma before
    Minkowski. Move Young/Hölder into the exposition, retaining the original
    exercise as “reconstruct the argument” or a meaningful extension, if the
    reconstruction wants a fully linear progression. Avoid mechanically deleting
    this good exercise solely because a proof moves.

12. **Derivative placement is a tradeoff, not a missing topic.** The continuity
    section at `ch05:275–388` includes derivative definition and Rolle/MVT; the
    calculus chapter begins from them. Keeping this minimal material in new Ch.3
    lets polynomial root-counting use Rolle later. The calculus chapter should
    clearly resume it with computation and integration. Moving all derivatives
    to Ch.7 would force new Ch.5 polynomials to defer root-location arguments.
    Thus retaining the short section is justified by the prerequisite graph.

13. **Named integration contract must be available before Ch.3 uses it.** Integral
    comparison `ch05:186,194–195`, Euler's constant `245`, and the workshop
    `438–469` use integration, antiderivatives and FTC long before new Ch.7. The
    present contract assumes integral existence/basic properties but proves FTC
    in old Ch.6. Choose explicitly: prove a minimal FTC from integral axioms in
    Ch.3 and refer to it in calculus; or move analytic integral applications and
    use grouping/telescoping proofs of comparison first, with an explicit return
    section for later material. The minimal FTC proof is ~one paragraph and has
    no circularity once continuity/MVT are proved; put it after those results.
    Reorder the existing sections so continuity comes before these applications.

### Pedagogical enhancements, not missing-content emergencies

- `ch05:85–95`: strong asymptotic caution exists; add a worked comparison that
  exposes constants and an explicit error, not another list of asymptotic symbols.
- `ch04:297`: obtain the arbitrary-real-vector p-norm inequality from
  `|a_i+b_i|≤|a_i|+|b_i|` before interpreting the nonnegative theorem geometrically.
- `ch04:31`: “never subtract or divide inequalities” is a useful warning but too
  absolute. Say one cannot subtract two bounds in the same direction; explain
  that a≤b and c≤d imply a-d≤b-c. This teaches the valid transformation.
- `ch06:74`: absolute improper convergence refers to a continuous Cauchy
  criterion “as for series” without proving it. A short bound on truncated tails
  plus the Cauchy criterion for R would complete the foundation.
- `ch06:319`: the divergent full Stirling expansion is an advanced assertion;
  mark explicitly as an outlook with the existing appropriate reference.
- Existing workshops are effective and should survive. Some repeated jokes
  (“subscription”, “parachute”, “wearing a tie”) may be reduced during editorial
  integration if they distract; this is a voice decision, not a mathematical fix.
- Avoid adding measure theory, general Lp integration, the full Euler–Maclaurin
  formula, Bohr–Mollerup proof or systematic Fourier analysis here.

## Exercise review ledger

“Read; no defect found” below means the statement, hint and write-up were read and
reasoned through, with no defect identified beyond the shared dependencies above.
It does not claim formal verification or exhaustive independent computation.

| Original chapter | IDs read, no further defect found | Specific action |
|---|---|---|
| 4 | `ex:8abc`, `ex:sqrtk`, `ex:intcs`, `ex:euler`, `ex:nesbitt`, `ex:triangle`, `ex:aabbcc`, `ex:holder`, `ex:means3`, `ex:bernoulli`, `ex:lagrangeid`, `ex:cauchyinduction`, `ex:heron`, `ex:entropy`, `ex:chebsumapp`, `ex:schur` | Keep all; label Heron's formula as supplied input; derivative/integral dependencies become earlier after relocation. |
| 4 | `ex:carleman` | Extend AM–GM to zeros; justify nonnegative interchange. Sharpness notes correctly use truncated 1/n and Stirling. |
| 5 | `ex:nature`, `ex:bertrand`, `ex:ln2`, `ex:kempner`, `ex:rearr`, `ex:nested`, `ex:newton`, `ex:stolz`, `ex:condensation`, `ex:sinn`, `ex:riemannrearr` | Keep; supply elementary-function/integration prerequisites and new chapter pointers. Newton's 100-digit bound is correctly an absolute-error statement, not guaranteed decimal rounding. |
| 5 | `ex:sin`, `ex:stirling` | Repair/mark Taylor forward dependencies as above. |
| 5 | `ex:oresme` | Correct rounded H values; n=12367 remains correct. |
| 5 | `ex:eulerbasel` | Keep finite-remainder proof; explicit dependence on FTC already cited. Avoid duplicating the logarithm workshop in calculus exercise without explaining the second route. |
| 6 | `ex:xnlnx`, `ex:riemann`, `ex:taylorln`, `ex:eirr`, `ex:wallisprod`, `ex:rl`, `ex:gaussian`, `ex:xnex`, `ex:leibnizpi`, `ex:frullani`, `ex:gammahalf`, `ex:niven`, `ex:sophomore` | Keep. Gaussian n=1 is valid. Fourier e-irrationality proof handles q=1. Niven's stated strict upper bound follows from strict interior bounds, though write-up states a weak bound sufficient for contradiction. |
| 6 | `ex:lhopital` | Part (a) asks x log x “by Taylor–Young”; write-up only provides l'Hôpital for that limit. Add y=1/x and finite exponential growth comparison, or ask Taylor only for the first two and another elementary bound for x log x. Taylor at 0 does not apply directly to log x. |
| 6 | `ex:trapezoid` | Supply certified periodic bound or explicitly separate observation/proof; see finding 3. |

The three challenge blocks were also read. Most advanced claims have named sources
and remain appropriate outlooks. The Hardy note is a proof of sharpness only,
not a full proof of Hardy's inequality; its statement directs readers to Steele.
Keep that distinction visible. The rationality/transcendence outlook deliberately
uses advanced Hermite/Lindemann facts; do not silently treat them as proved tools
for regular exercises. Gamma irrationality status and numerical digit-avoidance
constants were not newly checked against current literature by this reviewer.

## Numerical and symbolic checks actually executed

Ran a Python script in the configured virtual environment with `mpmath` at 60
working digits. Checked these independent values, all agreeing with the relevant
baseline rounding except the harmonic pair noted above:

| Quantity | Computed value |
|---|---:|
| Carleman L/sum(a) at N=10 | 1.51949509170271 |
| At N=100 | 1.93739127177050 |
| At N=10000 | 2.29437199393913 |
| Accelerated log-2 six-term bound | 1.08558255182245e-7 |
| Gaussian right-rectangle n=8 error | 0.0404660528935167 |
| sine T5(pi), T9(pi), T13(pi) | 0.524043913417169; 0.006925270707505; 0.0000211425675581 |
| integral exp(cos x), 0 to 2pi | 7.9549265210128452745 |
| ten-point periodic trapezoid | 7.9549265244723018096 |
| Their difference | 3.45945653506638e-9 |
| Suggested factorial-coefficient upper bound | 4.34230670272454e-9 |
| H12366 | 9.9999621479216393434 |
| H12367 | 10.0000430082758076947 |

The existing project fact-check script was inspected but not rerun by this
reviewer because it writes a tracked historical-results artifact outside this
reviewer's edit scope. The parent can run it after adapting its fixed
130-exercise expectation and per-file assumption to the reconstruction.
Numerical tests support checks; they are not proofs of the universal results.

## Migration recommendation

- Preserve all 47 exercise IDs, hints and solutions; migrate as intact triples.
- Old Ch.5 real sequence/series theory becomes new Ch.3, with continuity before
  integral applications and explicit foundational contract.
- Minimal derivative definition/Rolle/MVT stay there for polynomial prerequisites.
- Old Ch.5 complex extensions become a small addition in new Ch.4.
- Old Ch.6 becomes new Ch.7; preserve every application and figure. Gamma (c)
  moves to new Ch.8, giving an existing substantive bridge instead of extra filler.
- Old Ch.4 becomes new Ch.8, except Bernoulli's short induction proof moves earlier.
- Replace hard-coded chapter numbers by semantic chapter labels. Particularly
  old Ch.4 references Chapters 2,5,7; old Ch.5 references Chapters 1,3,4,6; old
  Ch.6 references Chapters 2,4,5. Track their semantic targets rather than applying
  one numeric search-and-replace blindly.
- Current extensive analysis material is already close to the requested scope.
  Correct dependencies and one missing certification before expanding topics.
