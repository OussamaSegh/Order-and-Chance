# D-22 equivalence table: unique factorisation of ideals (filed before Chapter 4's long proof was removed)

| Where | Label | Hypotheses | Conclusion | Method |
| --- | --- | --- | --- | --- |
| Volume 10, Theorem 6.6 | `thm:dedekind` (V10) | Noetherian domain, not a field; Dedekind = integrally closed + non-zero primes maximal (V10 Def. 6.5) | (a) Dedekind ⇔ (b) local rings DVR ⇔ (c) fractional ideals invertible ⇔ (d) non-zero proper ideals are products of primes; factorisation unique | Localisation, DVRs (V10 Thm 6.4) |
| Volume 10, Theorem 6.13 | `thm:intclosure` (V10) | R Dedekind, L/K finite separable | Integral closure of R in L is a finitely generated R-module and Dedekind | Trace form, discriminant |
| Volume 13, Chapter 2 | `thm:dedekind` (V13) | Quadratic field, O = Z[ω_d] | Ideals ≠ O are products of maximal ideals, uniquely | Hurwitz's lemma I Ī = (N(I)) and induction on the norm. Kept, headed "second proof" |
| Volume 13, Chapter 4 (before) | `thm:ufi` | Number field | Same as V10 (d) for O_K | Own proof via `lem:containsprod`, `lem:missing`, `prop:pinv` (P^{-1} ≠ O, PP^{-1} = O) |
| Volume 13, Chapter 4 (after) | `thm:ufi` | Number field | Same | O_K is Dedekind (`lem:okdedekind`, from `prop:noeth` or V10 Thm 6.13 with char 0), then V10 Thm 6.6 |

Statements are the same: V13 `thm:ufi` is V10 Thm 6.6(d) for R = O_K. The hypotheses of V10 Thm 6.6 are discharged by `prop:noeth` (a)–(d), which is kept with its proof.

Labels used by the removed proofs and cited elsewhere: `lem:containsprod`, `lem:missing`, `prop:pinv` were cited only inside `ch02-ideals.tex` (checked with grep over all volumes). `thm:ufi` (cited in ch05-cyclotomic, ch08-zeta) and `cor:divides` (ch03-geometry, ch06-local) keep their statements. `prop:pinv` (P^{-1}P = O, IP^{-1} ≠ I) is used by `cor:divides` and `prop:normideal`; it is kept, with a two-line proof from V10.

Numbering: the three statements 4.3–4.5 are kept as numbered statements (4.3 is now "O_K is Dedekind", label `lem:okdedekind`; 4.4 `lem:missing` now states PP^{-1} = O; 4.5 `prop:pinv` unchanged), so Theorem 4.18 (`thm:decomp`, cited by Volume 14) and Theorem 4.20 (`thm:dedekindcycle`, cited by Volume 15) keep their numbers. The direct argument survives as an unnumbered "Why this works" paragraph.
