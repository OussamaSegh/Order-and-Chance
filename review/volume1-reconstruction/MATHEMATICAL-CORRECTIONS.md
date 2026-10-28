# Mathematical corrections and proof-precision log

| Location | Baseline issue | Revision |
|---|---|---|
| ex:digits | Statement says every integer but its unsigned digit sums fail for negative integers; e.g. -12 is not 3 mod 9. | Prove nonnegative version and explicitly negate the sums for negative inputs. |
| ex:two solution | Final blanket sentence assigns norm 2 to every factor, including inert (2). | Inert maximal ideal (2) has norm 4; split/ramified maximal factors have norm 2. |
| ex:n2n | Introductory hint/solution uses Fermat before its Chapter 3 proof. | Derive the needed base-2 congruence by prime binomial divisibility in the solution. |
| thm:cyclic / prop:phisum | Proposed chapter order would put an essential totient identity later. | Move its original counting proof to Chapter 3; retain inversion consequences in Chapter 6. |
| thm:periodic | Infinite-expansion uniqueness supplied only by a later exercise solution. | Move complete argument to an earlier proved lemma; preserve exercise and its reconstruction strategy. |
| prop:intcrit | Integrality of the rational scalar is implicit because it is the leading coefficient of an integer polynomial; the criterion is valid. | Full monic-divisor proof using primitive integer factors. This is proof clarification, not a false-theorem correction. |
| prop:Zp, Qp construction | Sequential compactness/general equivalence and fraction-field/completeness steps compressed. | Direct covering proof, explicit fraction equivalence, field operations, valuation extension, bounded-Cauchy scaling and density estimates. |
| ex:padicexp | Valuation computation omits x=0 although the radius assertion includes it. | Treat x=0 separately before the nonzero valuation argument. |
| ex:goldenunit | Fibonacci formula has no stated n>=1; F_(n-1) otherwise invokes an undefined index. | State n>=1 explicitly; negative unit powers remain handled separately. |
| ex:primitive, fermatfactor, three, erdosdiv | Positive integer/length or exponent domains implicit. | State those domains. |
| ex:oddperfect | No-prime-factor case n=1 not explicit in solution. | Exclude it by sigma(1)=1. |
| theorem thm:mordell7 title | Specific attribution/date “Lebesgue, 1869” not confidently verified from an accessible source. | Preserve theorem/proof/label, use descriptive Mordell-equation title; flag attribution for historical follow-up. |
| prime distribution/circle remarks | Time-sensitive “best known today” and broad history shorthand. | Date the cited research benchmark; qualify Lamé/Euler history without inventing references. |
| Volume 0 references | Printed numbers point to the superseded eight-chapter architecture. | Replace with concept-based locations and prove tiny inputs locally where useful. |

No theorem is silently weakened to fit a shorter proof. The two added numbered results establish infinite continued-fraction existence/uniqueness and ideal norm as residue count. No mathematical result or original exercise is removed.
