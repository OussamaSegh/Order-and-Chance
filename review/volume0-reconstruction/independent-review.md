# Independent skeptical review of the reconstruction

Reviewer: separate mathematical review agent. Date: 28 October 2026.
This review was performed after the initial drafts were written, by an agent
which did not author them. It is a critical source review, not formal verification
or a claim that every printed page has been visually proofread.

## Scope actually examined

Read the complete new Chapter 0: every definition, stated result and proof,
worked example, workshop, all 18 exercise/hint/solution triples and all three
challenge notes. Read the complete new final circular-binary-word investigation.
Read the new formal-generating-function/decomposition material and four new
counting triples; the new early derivative/FTC/nonnegative-summation material;
the polynomial gcd/Bézout, linear maps/rank-nullity, coordinate change,
orthogonality/PSD and translation-operator additions; the moved Gamma convexity
proof and new finite-Taylor/root-filter quadrature certificate; and the new
probability vocabulary, countable-mass/truncation/coupon construction, covariance
matrix explanation, and two new probability bridge triples. Inspected the
editorial dependency/migration plan and sampled cross-references in revised
algebra sources against their originals.

The three initial subject audits contain the full original-chapter reviews. This
separate pass concentrates on new mathematics and dependency regressions; it does
not pretend to repeat every original proof line a second time. Compilation,
reference resolution, preservation counts, final PDF rendering and full historical
source verification are separate checks performed or recorded by the parent.

## Findings and corrective action

1. **External-book references corrupted by broad chapter replacement.** In the
   algebra drafts, references to chapters of *Concrete Mathematics*, Dunham's
   *Euler*, Horn–Johnson's *Matrix Analysis* and Stigler's *History of Statistics*
   had become semantic links to chapters of this volume. In particular,
   Horn–Johnson Chapter 8 would have printed Chapter 2, and its Chapter 4 would
   have printed Chapter 8. Reported exact locations to the integrating editor and
   algebra author. The algebra author restored all six source-book chapter citations in the
   draft copies and rechecked their source lists. External source chapter numbers
   remain literal; local chapter renumbering must not alter them. This is a real editorial regression,
   even though TeX would compile it without an undefined-reference warning.

2. **Early derivative-rule dependency.** The first D draft proved FTC but used
   power/chain rules for core integral comparisons before those rules were proved
   in Chapter 7. Reported to the parent. The updated D draft now proves sum,
   product, reciprocal and chain rules immediately after defining the derivative,
   derives the real power rule from the named elementary-function assumptions,
   and F reuses that lemma. This resolves the core dependency without admitting
   an additional unacknowledged result.

3. **Complex exponential contract.** A remaining calculus solution referred to
   the series “used to define” the complex exponential, whereas the revised
   complex chapter defines it from the admitted real functions. Reported to the
   analysis author. Updated F now identifies the series in its added part (c),
   keeping definition and later representation distinct. The series-identification
   argument uses real Taylor bounds and absolute Cauchy products, not unproved
   complex differentiation.

4. **Derivative domains.** Reported that derivative definitions must be restricted
   to interior points of an interval, with endpoint derivatives explicitly
   one-sided when needed. Otherwise a singleton interval makes the punctured
   limit condition vacuous. The inverse-function derivative and the later FTC
   restatement should follow the same convention. The new early FTC statement
   already says “at every interior point.” Integration/editor action is required
   for the remaining wording; this is a precision correction, not a change to
   the substantive results.

## Mathematical assessment of the additions

The new language chapter supports the stated secondary-school readership. Its
proof obligations are visible, witnesses are named separately, converse and
contrapositive are distinguished, equivalence/partition proofs work for the empty
set, and image/preimage properties are separated correctly. Its substantial
intersection-image workshop gives the exact injectivity characterisation and
identifies the invalid identification of two existential witnesses. All 18
solutions address their questions and include discovery and write-up sections.
Square-root existence examples explicitly identify the later completeness fact;
they do not silently prove it by a familiar symbol. No mathematical error was
found in the Chapter-0 arguments examined.

The final circular-word workshop is sound for its stated n≥2. The trace counts
closed walks with a fixed starting position; it does not quotient by rotations.
The exact eigenvalue expression, probability and asymptotic equivalence are
correct. The zero-step-walk convention is expressly distinguished from an empty
circular word, and the failed division-by-n shortcut correctly exposes unequal
orbit sizes. This is a substantive synthesis of counting, induction, linear
algebra, probability, limits and equivalence classes.

The new counting methods keep formal generating functions coefficientwise: each
coefficient is a finite sum, so there is no hidden convergence premise. The
nonconsecutive-subset bijection, strip tilings, derangement coefficient identity
and circular k-subset count handle empty/feasibility boundaries separately.
The polynomial Euclidean/Bézout argument and translation-operator bridge are
correct with the specified field and d≥1 assumptions. Moving rank-nullity and
Gram–Schmidt addresses actual proof dependencies. The PSD criterion is attached
to real symmetric matrices, as required.

The numerical quadrature certificate is a proof, not a comparison of decimals:
a finite degree-19 Taylor polynomial leaves only frequencies ±10 under the
10-point filter, and a uniform Taylor remainder controls the rest. Its rational
bound is less than 5×10^-9. The Gamma convexity proof handles λ=0,1 before using
reciprocal exponents, proves the required integral Hölder form on finite intervals,
then uses convergent improper limits. No unjustified infinite interchange was
found in these new arguments.

The probability additions distinguish mutual from pairwise independence and
uncorrelatedness from independence. The covariance matrix is PSD because its
quadratic form is a variance; orthogonal transformation yields uncorrelated
coordinates with no claim of independence. The countable extension is limited
and explicit. The coupon solution constructs normalised masses directly on
finite stopping histories, then uses nonnegative sums; it does not silently
assume an infinite-product probability space. The two new bridge solutions
include deterministic sampling boundaries and retain the fixed-prime-set
condition in the arithmetic asymptotic estimate.

## Independent computations actually executed

`python3 review/volume0-reconstruction/check_independent_examples.py` passed
**6,088 assertions**, recorded in `independent-example-results.json`:

- Exhaustive small finite functions (domains/codomains of sizes 0–3), all domain
  subset pairs, image/intersection injectivity characterisation, image/preimage,
  complement inclusion, and idempotent fibre/fixed-point conclusions.
- Direct enumeration of all circular binary words for n=1,…,16 against matrix
  powers (n=1 is the explicitly marked closed-walk convention).
- Exact rational sampling covariance for every n=2,…,8 and every k=0,…,n.
- Exact finite arithmetic densities for selected fixed prime sets and N=1,…,90,
  including mutual-intersection probabilities when the product divides N.
- Exact rational evaluation of the Taylor/filter certificate:
  `9602693143/2179474715658240000 < 5/10^9`.

These checks can expose mistakes in examples and formulas. They are finite
corroboration; the written arguments establish the universal claims.

## Limits and final acceptance

No independent full historical-source audit, image-rights certification,
physical-printer proof, every-page visual proofread or formal proof-checker run
is claimed. Some existing three-star applications remain intentionally advanced
and should retain explicit return prerequisites. The parent must verify that
reported draft corrections reach the active source, that all 130 original
exercise triples and original assets remain accounted for, and that final
numerical and chapter references match the built manuscript. Passing a source
review does not eliminate the need for those final checks.

## Review of the final G draft

Re-read the final G draft's derangement return, countable law/tail identity,
finite-stopping-word coupon proof, covariance quadratic form and spectral
interpretation, both new bridge statements and complete solutions, and the
birthday asymptotic outlook note. The nearest-integer derangement argument now
uses n≥2 for its strict 1/(n+1)<1/2 bound and checks n=1 separately. The coupon
construction also checks consistency with every finite-M experiment by counting
extensions of stopped words, so the direct mass model matches the intended
experiment. The density error keeps the primes fixed when taking N→∞. No
additional mathematical defect was found in this final G material. The birthday
constant 2/3 is explicitly labelled a referenced outlook, not presented as proved
by its integral heuristic.

## Final integrated source review (after Batch H; Batch I checks underway)

The revised active manuscript was then inspected separately from the drafts.
Read the complete integrated preface/foundational contract, ten-bridge reading
map and final field guide; checked the new Chapter-0 fibre diagram against its
caption and definitions; re-read the new conditional-integral proof in calculus;
verified the earlier corrections in the active chapter sources; and scanned all
chapter source lists for wrongly converted external-book chapter references.

Confirmed in the active source:

- Chapter 3 proves the elementary differentiation rules and real power rule
  before integral comparisons. It proves Rolle and the mean value theorem from
  completeness and extreme values, rather than assuming them. Interior and
  explicitly one-sided endpoint derivatives are distinguished, and limits are
  restricted to accumulation points; singleton continuity is handled separately.
- Chapter 7 reuses the early rules and FTC, states smoothness notation and retains
  its inverse-function argument. The complex exponential series is proved as a
  representation in `ex:taylorln(c)`, consistent with the Chapter-4 definition.
- All previously reported external-book chapter citations have been restored:
  *Concrete Mathematics* 7, Dunham 3, Horn–Johnson 4 and 8, and Stigler 1. No
  semantic local chapter link remains in the “Sources and further reading”
  sections inspected.
- The polynomial gcd statement is now a numbered proposition, so its semantic
  reference can correctly display a proposition number. Kernel/image,
  rank-nullity, change of basis, inner products and Gram–Schmidt precede their
  substantive uses. The spectral proof's complex Euclidean length is defined.
- The finite probability core, explicit countable extension, stopped-word coupon
  law, covariance PSD argument and new arithmetic/sampling bridges match the
  reviewed arguments. The final field guide still distinguishes labelled circular
  words from rotation classes, and exact formulas from asymptotics.
- The new fibre diagram has exactly the stated arrows: two inputs map to a, the
  third to b, and c is an unused codomain value. Its dashed fibre and image caption
  agree with the mathematical definitions.
- The added conditional-integral example is rigorous: integration by parts gives
  a convergent boundary term and an absolutely convergent cosine/x² remainder;
  the sine/x singularity at zero is removable; half-period integrals of
  |sine(x)|/x are bounded below by a divergent harmonic comparison. Its value
  π/2 is correctly identified as a later referenced outlook.

This final pass found three further concrete issues and reported them for
correction: the unintroduced outward-facing interval brackets used by the
retained chapters, the absent Archimedean argument behind arbitrarily large
natural indices, and an inherited promise that Chapter 8 treated Maclaurin's
symmetric-mean inequalities when it did not. The active source now explicitly
identifies both interval conventions, derives unboundedness of N from the
supremum axiom before choosing a limit index, and identifies Maclaurin as an
external advanced outlook in Hardy–Littlewood–Pólya. The preface's ambiguous
“Earlier volumes” wording was also changed to “Other volumes.” An unqualified
“By (c)” in the multiple-roots example, separated from its intended proposition
by the new gcd insertion, was reported for replacement by its explicit semantic
root-multiplicity reference.

Executed again after integration: the independent example checker passes 6,088
assertions. `check_structure.py` reports 155 exercise/hint/solution triples, all
130 original exercises retained, 299 unique labels and no source-reference or
pairing errors. The latest reference count was 507 after removing the false
Maclaurin forward link; counts may increase when the explicit multiplicity
reference is inserted. `git diff --check` passed at the time inspected. These
source checks do not establish layout or PDF navigation correctness; those
remain the final build's recorded responsibility.

No unresolved mathematical defect was found in the newly reviewed arguments
beyond the specific wording/reference corrections reported above. That assessment
is limited to the stated source-review scope and numerical checks. It does not
certify the book error-free, replace the three full subject audits, or claim an
independent every-page proofread or complete historical-source revalidation.
