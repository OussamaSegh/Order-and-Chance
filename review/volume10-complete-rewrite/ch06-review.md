# Chapter 6 separate mathematical and editorial source review

Reviewer: `rewrite_ch01_ch02`, separate from the Chapter6 writer. This agent wrote
Chapters1–2, not Chapters5–6. Read the full final Chapter6 only after its writer
reported stability. This is a source review, not human certification or a claim
of rendered/build/EPUB inspection. Parent owns production checks.

Reviewed source: `volume10-abstraction/chapters/ch05-dedekind.tex`, SHA-256
`96fec7f723eafe2a645c1a2d9ad8d4c3937851a6cc3724028025a25fa57e9575`.
Immutable comparison: unit6 of `starting-statement-content.json`, starting main
`59014a9aad3454ad60786c6549c81fcac88df9df`.

**Result:** source mathematical and editorial review passes on these inputs.
No blocking finding remains. Every original numbered mathematical conclusion
is retained; no silent weakening found. The prerequisite repairs are valid.

## Complete reading and every original formal statement

Read every paragraph and short clause in the chapter, all statements and proofs,
all worked norm/ideal calculations, the historical opening and quoted lore,
end-of-chapter bridge, all ten exercises/hints/solutions and sources. The
following judgements compare all fourteen original formal numbered blocks.

| Original label / number | Comparison and mathematical judgement |
| --- | --- |
| def:fractional / 6.1 | Same nonzero-submodule, common denominator, product, colon and inverse definitions over a domain. Finite sums explicit, and colon shown genuinely fractional using one nonzero a=r/s. |
| lem:invertible / 6.2 | All four original equivalences/claims retained. Inverse uniqueness and finite-generation argument from1=Σa_ib_i correct. Product-factor inverses valid. Local unit summand proves principality. Finite generators justify local colon identity before local-zero criterion on R/IJ. |
| def:dvr / 6.3 | Same PID/exactly-one-nonzero-prime definition. Valuation form follows from earlier PID⇒UFD; v(0)=∞ handles cancellation. Formal-power-series example explicitly deferred and not used before its proof. |
| thm:dvr / 6.4 | All four equivalent conditions and extra (c)⇒(a) assertion retain hypotheses/conclusions. Principal maximal ideal proof gives intersection of powers0 via ACC and1−cπ unit. Normal⇒principal proof makes nilradical quotient nilpotent with finite generators and uses determinant on a nonzero generating vector; no hidden field or characteristic assumption. |
| def:dedekind / 6.5 | Same Noetherian, normal, nonfield domain and nonzero-prime maximality. Nonfield convention is maintained throughout rather than silently using the convention allowing fields. |
| thm:dedekind / 6.6 | All four equivalences plus uniqueness retained. Local normality denominators handled. (b)⇒(a) intersection of local rings proved. (c)⇒(d) maximal counterexample has strictly larger proper I m⁻¹. Difficult (d)⇒(c) independently checked: cancellation lemma uses invertible left factors only; quotient factors over P are nonzero since they contain a∉P; matching quotient prime lists lifts equality of each prime ideal, hence of actual products. This yields maximality of invertible primes, then all primes invertible via a principal factorisation. No cancellation is assumed before it is earned. |
| cor:contain / 6.7 | All iff, valuation comparison, min sum and max intersection formulas retained for fractional ideals. L explicitly nonzero, as IJ⁻¹ must be. Nonzero intersection justified by clearing denominators. |
| ex:sixtwice / 6.8 | All four ideal identities and nonprincipality of all three primes retained. Normality and dimension are proved at this location rather than borrowing later trace/intclosure. Rational integrality of2a and a²+5b², denominator d²|5 and mod4 parity are correct. Quotient maps, products and norm-gcd nonprincipal obstructions checked directly. |
| def:classgroup / 6.9 | Same fractional/principal ideal quotient and finite-order class-number definition. Only nonzero fractional ideals occur in the group. |
| prop:classseq / 6.10 | Exact sequence retains every map and kernel; PID iff trivial class group iff UFD holds under Dedekind hypothesis. UFD⇒PID argument uses irreducible prime inside a maximal nonzero prime and ideal factorisation, not a general false UFD⇒PID assertion. |
| prop:twogen / 6.11 | Same prescribed nonzero first generator and second generator conclusion. Unit case uses b=0. Finite prime list of aR, CRT modulo p_i^(n_i+1), valuation containment and exact minima give I=(a,b); no prime outside list can obstruct. |
| lem:trace / 6.12 | Same f^(n/d) characteristic polynomial for any finite extension, integral coefficients/trace over normal R. Companion blocks justified by tower basis. Roots and symmetric expressions give integral minimal coefficients; separability is correctly unnecessary here. |
| thm:intclosure / 6.13 | Finite separability, primitive integral θ, same nonzero trace determinant/common denominator, finite module, Dedekind and fraction-field conclusions retained. Local primitive-element proof repairs V3's characteristic-zero-only citation. Bad c set finite over infinite K, gcd T−β, iterated generation and scaling are valid in arbitrary characteristic. Distinct conjugates give Vandermonde square nonzero; Cramer bound finite module; transitivity gives normality and integral dimension gives1. Degree1 and empty Vandermonde product give d=1. |
| thm:fundid / 6.14 | Same full sumΣe_if_i=n, with contextual hypotheses now explicit in theorem. Prime-power layers each1-dimensional over residue field; other valuations0 forbid intermediate ideals. Finite torsion-free local module over PID has rankn, reduction gives k^n, and allowed denominators already invertible on S/pS. Both counts complete; no Galois/transitivity premise sneaks in. |

Additional substantive passages checked: primary prime powers and no embedded
primes for nonzero ideals; Claborn and Krull–Akizuki clearly quoted and unused;
class-number2/finiteness and Galois efg=n clearly later previews. The local
squarefree cubic normality proof uses characteristic0 and squarefree denominators
correctly before any Dedekind factorisation. Its nonvertical three distinct roots,
vertical two roots, and vertical repeated-root case are all handled. The
elliptic class-group bijection is explicitly not claimed proved.

## Every original and added exercise

| Label / exercise | Hint and complete solution judgement |
| --- | --- |
| ex:zsqrt5 / 6.1, ★ | All four ideal products verified in both directions. Norm of a hypothetical p-generator divides4 and6 and cannot be1 or2. Hint gives the exact obstruction and solution complete. |
| ex:powerseries / 6.2, ★ | Recursion defines each inverse coefficient by a finite sum; no analytic convergence assumed. Minimum order gives all ideals and unique nonzero prime, fraction field k((t)), constants and zero valuation included. |
| ex:semilocal / 6.3, ★★ | Finite prime list nonempty by nonfield condition. CRT produces valuation1 at selected prime and0 elsewhere; all nonzero primes and then all ideals principal. |
| ex:notdedekind / 6.4, ★★ | First example noninvertible m via two-dimensional m/m² and local Nakayama generator criterion; second has missing integral ω, p prime with p²=2p and no cancellability. Both ring hypotheses and failed Dedekind condition stated. |
| ex:circle / 6.5, ★★ | Given Dedekind hypothesis retained explicitly. m²=(x−1) algebra exact; norm divides x−1 while nonzero real norm degree even, ruling out generator. Complex Laurent isomorphism explicit, PID via localisation. No unsupported whole-class-group computation used. |
| ex:cubicnotprincipal / 6.6, ★★★ | Unique a+by, conjugation multiplicativity, parity of norm degrees and units correct. m²=(x), gcd norm degree1 contradiction, direct normality with squarefree denominator all complete. Singular y²=x³ gives valid missing integral y/x obstruction. |
| ex:v10new-ch06-arithmetic / 6.7, ★★ | New. Correct min/max/product exponents, fractional colon IJ⁻¹, neither inclusion. Numerical (12),(54) give sum6, intersection108, product648 and colon(2/9)Z. CRT R/I correct. |
| ex:v10new-ch06-projective / 6.8, ★★ | New. Explicit f,g with fg=id give direct summand and projectivity using earlier Chapter3 criterion. Fraction-field localisation gives rank1; principal iff free and locally free rank1 proved. Works for an arbitrary domain with invertible fractional I. |
| ex:v10new-ch06-gaussian / 6.9, ★★ | New. 2=(1+i)² up to unit,3 quadratic irreducible and F9,5=(2+i)(2−i) with distinct F5 quotients. e,f and all sums2 correct. Repeated root corresponds nilpotent layer, not two primes. |
| ex:v10new-ch06-cusp / 6.10, ★★★ | New. All characteristics valid. Ring integral finite over K[t²] and dimension1; m maximal. m²=t²m, cancellation would force t³∈t²R, false because t absent. Missing integral t witnesses normality failure. |

All ten have exactly one appropriately useful hint and full idea/writeup solution.
Original six labels/order are unchanged and the four additions are appended.
No later exercise is required as a premise for an earlier proof. Difficulty
ratings match the amount of work; the three-star tasks require several distinct
obstructions rather than a disguised one-line substitution.

## Actual prerequisite audit

Inspected Volume3 current `main.tex`/chapter contexts and actual statements:
ring CRT6.9 (`thm:crtring`), PID⇒UFD6.14 (`thm:edpidufd`), PID-module structure7.6
(`thm:structure`), tower8.2 (`thm:tower`), splitting-field construction and
primitive-element8.20 (`thm:primitiveelement`, explicitly K⊂C). The new local
argument covers the additional characteristic scope in6.13. Inspected Chapter4
`prop:noethmodules` and Chapter5 integral-extension, local-zero, dimension and
nilradical proofs. They precede Chapter6 in actual printed order. The
Vandermonde citation targets Volume1Proposition7.4. Ran citation resolver on
Chapters5–6, exit0; every numbered earlier target lands, and future Volume13
citations are explicit previews. No statement of Volumes11–15 is a proof premise.

## Figures and preservation

Read original cubic TikZ source and protected caption, both new TikZ sources,
all captions and their explanatory prose. Original cubic uses half-size vertical
coordinates with no unit tick marks; its drawn P,Q,R,R′ match the caption's
mathematical points under that vertical scale. No alteration was made.
The new valuation grid puts I at(2,1), J at(1,3), sum at(1,1), intersection at(2,3),
with the stated reverse containment direction. The splitting diagram distinguishes
two primes over5, one degree2 residue field over3, and one double-multiplicity
prime over2. All labels and e,f values match the checked Gaussian calculation.
Both additions occur after the original figure. Palette follows charcoal/rust.
No photograph is in the reviewed Chapter6 source; photo claims are parent-owned.

Executed Python source checks, exit0: every original label retained; no duplicate
label; original whole figure block byte-identical; original figure hash equals
immutable baseline; figures1→3, exercises/hints/solutions6→10 each.

Figure SHA-256 receipts:

- original `ch05-cubicclass.tex`: `f9e525976cba40b37e84e3c4e2073f1fc34394083840cd4c8d42f7c794209f42`;
- new `v10-new-ch06-valuations.tex`: `df295c94cc89fb6dd97876e1829d4c46782a1da36a112f978b3aba3677a414cc`;
- new `v10-new-ch06-splitting.tex`: `51491314ed4932db2c82c9cfa123fcc350e580b9cdbd80f110012541f6c48519`.

No PDF build, rendered-page review, photo inspection or EPUB test was run by this
reviewer. Source approval here does not replace the parent's production checks.
