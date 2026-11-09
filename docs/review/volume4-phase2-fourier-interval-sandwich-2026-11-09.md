# Volume 4 Phase 2 — Fourier inversion interval-identification proof
**Date:** 2026-11-09
**Issue:** V4-P2-013, mathematical proof completeness, high priority
**Validator:** ChatGPT GPT-6, assigned by author (no external-referee requirement)
**Scope:** printed Chapter 6, Theorem 6.8, source label thm:inversion, part (b)
**Disposition:** targeted source correction submitted for exact-head CI, not an all-volume mathematical signoff.

## Defect and argument

The previous published-candidate source correctly constructed a continuous inverse-Fourier candidate f, established its nonnegativity, total mass one and equality E[g(X)]=integral(g f) for every continuous, compactly supported test function g. It then used only **one outer trapezoidal cutoff** dominating the interval indicator to conclude P(a<=X<=b)=integral_a^b f. An outer test provides only P(interval) <= integral f in the limit. Without an inner cutoff, the opposite inequality and no-atom property for endpoints were unproved. This is a missing logical inference, not an assertion that Fourier inversion is false.

The correction introduces both compactly supported, continuous piecewise-linear cutoffs for any a<b and 0<epsilon<(b-a)/2:
- g^-: zero outside [a,b]; rises from zero at a to one at a+epsilon, remains one until b-epsilon, falls to zero at b.
- g^+: one on [a,b], rises from zero to one on [a-epsilon,a], falls from one to zero on [b,b+epsilon], zero outside.
Thus g^- <= 1_(a,b] <= g^+. Because f>=0 and E[g(X)]=integral(gf) for both compactly supported cutoffs, their integrals bound P(a<X<=b) from below and above. Continuity of f makes the discrepancy from integral_a^b f vanish with epsilon. It follows P(a<X<=b)=integral_a^b f. A further continuous tent dominating 1_{X=a} yields P(X=a)=0 from the vanishing mass of its shrinking support; this removes any hidden endpoint atom.

The correction does not import Lebesgue's measure-extension theorem, the Levy continuity theorem or general inversion without hypotheses. It preserves the proof's exact assumption integral |phi_X| finite and the original Fourier transform and density.

## Independent regression

tools/test_volume4_phase2_fourier_interval_sandwich.py provides **four tests**:
1. Guards the source for both cutoffs, the two-sided interval-indicator inequality, nonnegativity and endpoint-atom conclusion.
2. Verifies the pointwise inequality on rational grids and critical endpoints for several intervals and shrinkages.
3. For the independent density f(x)=2x on [0,1], performs **exact rational quadrature** (piecewise quadratic integrands; Simpson integration is exact on each piece) to confirm both cutoff expectations squeeze the exact interval mass b^2-a^2 and their gap shrinks with epsilon.
4. Confirms exact shrinking-interval mass at a=0,1/2,1, as the no-atom argument requires.

These are regression tests of the *specific inference* and not a mathematical proof of Fourier inversion for all characteristic functions. The source proof supplies that general inference.

## Publication and acceptance scope

The patch changes only current editable Volume 4 Chapter 6, new tests and this ledger. It does not alter Volumes 1–3, chapter architecture, proof depth or figures. Full Build books and Volume 4 native QA must be green on the exact final PR head before merge, with source/CI evidence checked.

Whole Phase 2 remains open pending complete independent exact-manuscript audit of 127 theorem/lemma/proposition claims, 107 exercises/hints/solutions, individual semantic acceptance of 41 figures and downstream source dependencies. Green CI and this fixed theorem do not imply all of those gates are closed.
