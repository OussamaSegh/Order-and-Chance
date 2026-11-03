# Volume 2 continuity: initial source and prerequisite audit

Date: 2026-11-03. Branch: editorial/volume2-continuity-foundations-20261103.
Status: partial source audit, **not** a theorem-by-theorem mathematical sign-off.

## CI failure and repair

The initial PR #97 run, https://github.com/OussamaSegh/Order-and-Chance/actions/runs/41551781706, passed the earlier source and export unit tests but failed before typesetting at the series metadata check. The new four-part main.tex disagreed with the old Volume 2 part names in common/series-catalog.json.

Repaired the canonical catalog and its cover-source SHA-256 in tools/assets/series/manifest.json. The original catalog checksum matched the existing manifest before the update. The common metadata file is a shared build input, so this change may cause CI to rebuild all fifteen volumes.

## Source-level baseline

Reviewed the eleven chapters in the approved printed order plus the preface and field guide. The inspection counted:

| Check | Result |
| --- | --- |
| Chapter sources and parts | Eleven chapters, four approved parts |
| Exercise identifiers | 144 |
| Hint identifiers | 144, in matching order |
| Solution identifiers | 144, in matching order |
| Distinct manuscript-local labels | 266 |
| Duplicate local labels | Zero |
| Missing local reference targets | Zero |
| Main-body forward reference occurrences | 15 |
| Exercise, hint, solution and other forward reference occurrences | 18 |

The 15 main-body forward references were examined in their surrounding text. They concern previews of modular inverses, continued fractions, Gaussian integers, characters and sieves; none was an explicit invocation of a later theorem as an earlier displayed proof premise. This is a **reference-context scan**, not a certification that every implicit theorem prerequisite has been found.

The 18 exercise-area forward references warrant a separate challenge audit, notably links to character-problem machinery introduced only in the final chapter.

## Repairs made during this audit

1. **Canonical book parts.** Synchronized the new part names with the series metadata and cover-manifest checksum.
2. **CRT versus sieve.** Replaced a statement incorrectly identifying the Chinese remainder theorem with the exact sieve identity. The manuscript now distinguishes CRT's reconstruction of compatible residue information from the Möbius/inclusion-exclusion formula for finite sieving.
3. **Unproved ring claim.** The Diophantine chapter referred to the Gaussian/Eisenstein chapter as though it developed arithmetic in the ring Z[sqrt(-2)]. It does not. The revised prose treats the example as beyond the local toolkit, verifies only the displayed examples, and directs broader theory to Volume 13.
4. **Stale printed numbers.** Replaced the advanced reciprocity solution's old Volume 2 Chapter 4/5 numbers with stable references to the actual orders, reciprocity and characters chapters.
5. **Wrong destination for CRT.** A challenge in divisibility incorrectly sent the reader to Volume 3 Chapter 2 for Chinese remainders; it now points to Volume 2's congruences chapter.
6. **Gauss-sum cross-reference.** An arithmetic-functions challenge now points directly to the Gauss-sum exercise instead of an obsolete numerical chapter.
7. **Regression tests.** Added source checks that require book parts and the canonical catalog to match and that find duplicate/missing manuscript-local reference targets.

## Reordering prerequisite spot-check

Arithmetic functions follows prime factorisation and congruences, and its references to characters are previews. Primitive roots uses earlier congruences and does not invoke quadratic reciprocity as a premise. The quadratic-residue chapter precedes sums-of-squares applications. The moved Diophantine chapter does not explicitly invoke results from the now-later continued-fractions chapter.

Searches through subsequent main chapter bodies did not find Hensel lifting or Chebyshev/Bertrand material being invoked as a stated prerequisite. This is only a spot-check: every implicit dependency still needs review.

## Remaining gates

- Independently audit every theorem, lemma, corollary and full proof for hypotheses, definitions and edge cases.
- Check arithmetic examples and non-elementary analytic constants, especially the Basel evaluation in coprime density, prime estimates, quadratic reciprocity signs, Pell solutions, sum-of-squares descents, norm division and Euler products.
- Review all 144 exercises, hints and solutions, including explicit signposts on challenges needing later chapters.
- Confirm every chapter-opening and transition reflects the reordered neighbours and first-reading route.
- Run complete tests and regenerate the reading PDF, EPUB and new-page-count paperback cover. Verify the ISBN 9798167208650 and matching barcode in final artifacts, not only source.
- Conduct author-side KDP title association, Print Previewer and physical proof reviews separately.

Keep PR #97 in draft. This source scan does not certify mathematical correctness, KDP acceptance or readiness to merge.

## Additional advanced-exercise dependency repair

Five Chapter 4 prompts have been signposted without deleting exercises or changing their identifiers: the coprime-density exercise points to Volume 1's Basel proof; Eisenstein's trigonometric reciprocity proof and the Euler--Jacobi liar problem explicitly require the later reciprocity chapter; the largest-prime-factor problem names the quantitative prime-distribution tool from Volume 6; and the finite-field sum-of-squares exercise defines its quadratic-symbol notation and marks the later quadratic Gauss sum and Volume 4 total-variation tool. These repairs preserve the corpus but do not yet constitute a full solution audit.

## Proof-focused review pass: concrete findings

This pass examined the full displayed proofs and statements of Euclid's theorem,
Chebyshev-type bounds and Bertrand's postulate, the basic modular and Hensel
arguments, the four-square descent, the Pell existence-and-classification
argument, the Euclidean-division estimate in three imaginary quadratic
integer rings, the quadratic reciprocity construction, character
orthogonality, Euler-product convergence and Legendre's finite sieve.

- **Corrected a theorem boundary case in Chapter 11 (Legendre's sieve).**
  The original printed statement assumed only $x\ge1$ and $z\ge\sqrt{x}$,
  and asserted $\Phi(x,z)=1+\pi(x)-\pi(z)$. This is false whenever
  $z>x$: for example, $x=4$, $z=10$ gives $\Phi(4,10)=1$ but the
  old right-hand side is $1+\pi(4)-\pi(10)=-1$.
  The corrected statement is
  $\Phi(x,z)=1+\pi(x)-\pi(\min\{x,z\})$, for these hypotheses.
  The proof now notes that the prime interval $(z,x]$ may be empty.
  A regression test directly compares finite sifted counts with the
  corrected formula for many small $x,z$, including $z>x$.
- **Corrected a mistaken statement about Chapter 10's scope.**
  A previous editorial change incorrectly said that Chapter 10 did not
  treat $\mathbb{Z}[\sqrt{-2}]$. It actually develops norms, units and
  Euclidean division in that ring alongside the Gaussian and Eisenstein
  integers. The Diophantine passage now acknowledges that material while
  correctly withholding a classification of $y^2=x^3-2$ that the chapter
  does not prove.
- **Caught a one-star challenge with future prerequisites.**
  The Fibonacci-coprimality exercise in Chapter 1 used the later gcd
  distribution and expected-value problem in Chapter 5. It is now
  labelled a Journey/advanced return problem, with the missing tool named
  directly in the prompt.
- **Caught a high-level quadratic-residue challenge using final-chapter
  machinery.** The two-$k$-th-powers problem now explicitly calls out
  the character-orthogonality and Jacobi-sum tools from Chapter 11 as
  prerequisites rather than leaving them hidden.
- **Numerical and logical proof spot checks:** the displayed
  four-square identity and descent reduce a positive multiplier;
  the elementary Pell argument constructs a norm-one unit and reduces
  any positive unit via the least fundamental unit; the Hensel proof
  correctly invokes invertibility of the derivative modulo $p$;
  the Euler product's nonvanishing follows from absolute convergence
  for $s>1$; the sieve boundary above was the identified failed case.
  These spot checks do not certify every claim or optional exercise.

All source-local IDs and cross-references must be rechecked by the
full CI suite after these edits. The remaining mathematical proof
and exercise audit is substantial. Do not convert this partial audit
into a proof-complete, CI-green or publication-ready sign-off.

## Further exercise-domain and numerical checks

- In Chapter 4's optional Eisenstein trigonometric reciprocity
  exercise, part (a) now specifies that $q$ is a **positive** odd integer.
  The original phrase "let $q$ be odd" included negative integers for
  which the asserted product indexed from $1$ to $(q-1)/2$ was not the
  formula proved in the solution.
- In Chapter 1, the reduced-random-fraction problem now chooses $a,b$
  independently and uniformly on $\{1,\ldots,N\}$ and explicitly takes
  $N\to\infty$. Without a specified finite experiment or limiting
  process, its statement "with probability $1/(p+1)$" was ambiguous.
- Independently enumerated small integers as sanity checks, separate
  from the source regression suite: Legendre's corrected sieve formula
  passed **8,474** pairs of $x,z$ ($1\le x\le90$,
  $\max(2,\lceil\sqrt x\rceil)\le z\le100$); the representation formula
  $r_2(n)=4\sum_{d\mid n}\chi_4(d)$ and the two-square prime-exponent
  criterion each passed **120** integers; quadratic reciprocity passed
  **650** ordered pairs of distinct odd primes at most $103$.
  Finite enumeration can find counterexamples but cannot certify a
  theorem for all inputs.

The test matrix is evidence for these specific formulas, **not** an
audit of every chapter, every exercise solution, or every proof.
