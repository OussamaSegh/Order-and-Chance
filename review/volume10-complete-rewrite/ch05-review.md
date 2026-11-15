# Chapter 5 separate mathematical and editorial source review

Reviewer: `rewrite_ch01_ch02`, a different agent from the Chapter 5 writer. This
reviewer wrote Chapters 1–2, not Chapters 5–6. This is a separate source review,
not human certification, a rendered-page inspection, or a claim that build/EPUB
checks were run here. Parent owns production validation.

Reviewed source: `volume10-abstraction/chapters/ch04-localisation.tex`, SHA-256
`d20adf24fa7fdbd75ea8a1e2af381abf8fce97169a4e195c1d7a383cb9c9d89a`.
Immutable comparison: `starting-statement-content.json`, unit 5, against starting
main `59014a9aad3454ad60786c6549c81fcac88df9df`.

**Result:** source mathematics and editorial review passes on these inputs.
No new blocking finding remains. The writer's explicit zero-algebra correction
is necessary and valid. Printed numbers and rendering remain parent checks.

## Complete reading and statement comparison

Read the entire chapter, including its opening/history, every short formula
introduction, transitions, formal definitions and statements, each proof and
example calculation, all ten exercises/hints/solutions, ending, and sources.
The following table gives a mathematical judgement for every original formal
numbered statement; exercise judgements follow separately. Original hypotheses,
quantifiers and conclusions are retained except for the explicitly justified
nonzero-algebra correction. No assertion is weakened silently.

| Original label / number | Comparison and proof judgement |
| --- | --- |
| def:localisation / 5.1 | Same multiplicative-set equivalence, operations, canonical map and module construction. Extra annihilator t retained; transitivity calculated correctly even with zero divisors. S containing0 correctly gives zero ring. |
| prop:locuniv / 5.2 | Same universal factorisation and kernel test, including uniqueness. Units cancel the witness t, then both denominators; no injection assumption on R→S⁻¹R. |
| prop:locexact / 5.3 | All three parts retained: natural tensor isomorphism, exactness, flatness. Finite common denominators justify tensor reduction; zero test proves injectivity, not merely surjectivity. Ends of exact sequences handled. |
| thm:locprimes / 5.4 | Same inverse inclusion-preserving extension/contraction bijections. Primality and properness are proved; S containing0 gives empty sets on both sides. |
| cor:localring / 5.5 | Same complete prime correspondence and unique maximal ideal. Fractions outside the maximal ideal have the stated inverse. |
| thm:nakayama / 5.6 | Finite-generation and locality hypotheses retained. Minimal generating list argument includes n=1 and zero module; unit1−a_n justified. |
| cor:mingens / 5.7 | Same iff and exact minimal cardinality. Quotient is finitely generated, so Nakayama applies; dependence removes a generator, including empty-list boundary. |
| prop:localzero / 5.8 | Arbitrary modules, primes/maximals, injective and surjective criteria all retained. Proper annihilator in a maximal ideal gives contradiction; kernel/cokernel localisation follows from preceding exactness. Zero-ring case covered. |
| def:spec / 5.9 | Same prime set, V(I) topology and contravariant continuous map. The finite-union and arbitrary-intersection identities are proved, and inverse-image formula is correct. |
| thm:speczx / 5.10 | Every original prime type retained, with max ideals exactly (p,f). Primitive integral contraction proof uses Gauss correctly; quotient case over F_p exhaustive. |
| def:integral / 5.11 | Same monic-root and integral-extension definitions for inclusions of commutative unital rings. Leading coefficient is explicitly distinguished from mere algebraicity. |
| prop:integralcrit / 5.12 | Same three equivalent conditions. Generator determinant kills1, so it vanishes even if chosen generators are dependent. Zero-ring boundary separately stated. |
| cor:integralclosure / 5.13 | Same subring and transitivity conclusions. Finite sets of monic coefficients and successive finite-module generating lists provide the required finite algebra. |
| lem:intfield / 5.14 | Both field directions and nonzero-ideal contraction retained. Minimal monic equation has nonzero constant term in a domain; inverse equation proves descending field property without later tools. |
| thm:goingup / 5.15 | Incomparability, lying over and going up all retain original scope for integral inclusions, not only domains. Domain lemma used only after appropriate prime quotient. Localisation is injective on the inclusion and nonzero; maximal contraction argument is complete. |
| def:krulldim / 5.16 | Same supremum of strict prime-chain lengths. Empty spectrum convention−∞ is made explicit; n+1 primes count n steps. |
| cor:dimintegral / 5.17 | Same equality for integral inclusions, including infinite-dimensional and empty-spectrum cases. Incomparability contracts strictly; going up lifts strictly. |
| lem:noethervar / 5.18 | Same field-independent substitution and constant nonzero leading coefficient. Base-r encoding separates all monomials; positive degree and n=1 checked. Works over finite fields. |
| thm:noethernorm / 5.19 | Explicit correction A≠0. Original included zero K-algebra under permitted zero-ring convention, but no copy of K embeds there. All valid nonzero-algebra conclusions retained. Induction drops one generator and monic relation makes A integral over A′. |
| thm:dimpoly / 5.20 | Same n-dimensional polynomial ring and integral-algebra consequence, n=0 explicit. Monic relation quotient contains the polynomial subring injectively, integral dimension applies, and chain length drops exactly one. |
| def:primary / 5.21 | Same proper-ideal implication and positive power; zero-divisor quotient interpretation correct. |
| lem:primaryradical / 5.22 | Same prime radical. Power of ab, exclusion of all powers of a, and primary implication produce a power of b. Properness retained. |
| lem:irredprimary / 5.23 | Same Noetherian irreducible-ideal hypothesis and primary conclusion. Stabilised colons establish intersection equality; the strictly larger first ideal forces equality of the second with I. Direction typo from original prose repaired. |
| thm:laskernoether / 5.24 | Same finite existence theorem for every proper ideal. Maximal counterexample must split into proper larger ideals, each finitely decomposable; previous lemma supplies primary components. |
| thm:assprimes / 5.25 | Same prime radical-of-colon characterisation, invariance, minimal-over-I and embedded-prime conclusions. Finite intersection formula and isolating witnesses correct; prime intersection equals a member by product avoidance. Empty index gives R, correctly excluded from primes. |

Additional explanatory claims checked: dimZ[x]=2 upper bound as well as chain
lower bound; finite fibres for finite-module normalisation via residue fields and
CRT dimension; K-point surjectivity limited to algebraically closed K; the
hyperbola double fibres s=±2; irreducible-primary intersection example; the
Gaussian-integer splitting interpretation. Going down is explicitly unproved
and unused. No numerical experiment is used as a proof.

## Exercises, hints and complete solutions

| Label / printed exercise | Review judgement |
| --- | --- |
| ex:subringsq / 5.1, ★ | Original tasks retained. Bézout forces every reduced denominator into S; minimal p-order classifies all local ideals, including0 and unit ideal. Hint is useful, solution complete. Unital subring convention matches rings in chapter. |
| ex:golden / 5.2, ★ | Missing golden ratio, finite Z-module and monic quartic all checked. Coefficient1/2 obstruction and t⁴−10t²+1 exact; hint and idea/writeup present. |
| ex:localiff / 5.3, ★★ | Local iff nonunits ideal, nilpotent iff R_f=0, nilradical intersection all retained. Zero ring treated correctly: empty nonunit set is not an ideal. Maximal ideal contraction provides prime avoiding any nonnilpotent. |
| ex:specrx / 5.4, ★★ | Linear/quadratic prime classification, generic0 point and upper-half-plane set bijection complete. Does not confuse the set bijection with Euclidean homeomorphism. |
| ex:quasicompact / 5.5, ★★ | All opens refined to D(f), expression1 finite, selected opens then lifted to original cover; empty spectrum handled. No Noetherian hypothesis silently imposed. |
| ex:hyperbola / 5.6, ★★ | Nonintegral x⁻¹ obstruction has constant term1; s=x+x⁻¹ transcendental argument supplies polynomial subring; both fibre descriptions complete, including missing x=0 and repeated s=±2. |
| ex:v10new-ch05-torsion / 5.7, ★★ | New. Local maps to Z/4,Z/3,Z/5 use denominators invertible in the indicated factor; CRT gives exact product isomorphism. Other primes kill all and15,20,12 give correct witnesses. Complete hint and solution. |
| ex:v10new-ch05-dual / 5.8, ★★ | New. Dual-number nilpotent is nonzero; single maximal prime, dimension0 and homeomorphism correct. General nil ideal need not have common nilpotence exponent; proof correctly works elementwise. |
| ex:v10new-ch05-cusp / 5.9, ★★ | New. Works every characteristic: exponent1 absent, u=u³/u² in field, monic equation gives integral extension, dimension equality, K[u] normality identifies complete closure. |
| ex:v10new-ch05-embedded / 5.10, ★★★ | New. Modq_c calculation shows correct intersection, primary quotient K[x]/x² and radical fixed. Distinct parameters give distinct primary ideals; colons and irredundancy checked. Difficulty appropriate for multi-step counterexample. |

All ten have one useful hint and a complete `idea`/`writeup` solution. Four new
exercises follow the six originals; no dependency on a later exercise is used
as a proof premise.

## Prerequisites and citations actually inspected

- Read current Chapter4 `prop:noetherian`, `prop:noethmodules` and Hilbert-basis
  theorem; they precede this chapter in actual main.tex.
- Inspected Volume3 ring CRT (`thm:crtring`), Gauss/UFD (`thm:gaussufd`) and
  module structure contexts; no field theorem is assumed over a ring.
- Inspected Volume7 `thm:zorn`, printed1.19, which includes the stated choice
  hypothesis. The proper-ideal maximality application uses this earlier tool.
- Ran `python3 review/volume10-rewrite/resolve_citations.py` on Chapters5–6,
  exit0. Read its targets: V7Theorem1.19 and V3Theorem6.18 land correctly.
- References to future arithmetic and going down are previews, not premises.
  Bibliographic records remain literal and historical prose keeps its sources.

## Figures and preservation

Read the original SpecZ[x] source and both new TikZ sources, captions and prose
references. New localisation diagram retains (0),(3) and removes other rational
primes correctly; its connecting lines are stated to mean inclusion. New
monomial grid marks exactly a≥2 or a≥1,b≥1, excluding x and all a=0 points.
Palette is the approved charcoal/rust/grey family. Both new figures occur after
the complete original block. No photograph appears in this chapter's reviewed
source, so there is no chapter-specific photo credit/resolution assertion here.

Executed source preservation comparison (Python, exit0): every original label
retained, no duplicate label, complete original figure block literal, original
figure SHA matches baseline; figures1→3, exercises/hints/solutions6→10 each.

Figure SHA-256 receipts:

- original `ch04-speczx.tex`: `ad084fc660ecfae9f282a722807ce8c3f44e616f08dc62cf172848fc6d4c699e`;
- new `v10-new-ch05-local.tex`: `67fa0fa422910a874dff280e8d0f2b76130d3ad1ddbd9151c72e715cce794df7`;
- new `v10-new-ch05-primary.tex`: `8bd8ef9497a94107791d14e742ca0f6a6cf14be730346af89b081b8ad4bf1fe3`.

No build, rendered layout, photo inspection or EPUB check was performed by this
reviewer. These are specifically left to the parent's production receipts,
not assumed passed from source inspection.
