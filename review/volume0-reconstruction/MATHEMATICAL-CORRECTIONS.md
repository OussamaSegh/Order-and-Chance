# Mathematical and prerequisite corrections

Locations use retained semantic labels or named sections. This is a record of
changes, not a claim that the book has been formally verified. The three original
audit reports give baseline source lines and fuller reasoning.

| Place | Original issue | Implemented correction |
|---|---|---|
| Chapter 0 | Logic and proof language assumed throughout | Full concrete introduction; inverse and partition proofs, counterexamples, orders, discovery workshop |
| Arithmetic bridge | Well ordering and arithmetic notation used before introduction | Moved after well ordering; explained divisibility, gcd/lcm, congruence, floor, factorial and product notation |
| `prop:bernoulli` | Analytic decay depended on later inequalities | Elementary induction proof moved to Chapter 1 |
| `prop:deltabinom` | Early finite-difference proof used later polynomial root theorem | Direct product-factor proof |
| `ex:kbinom` | Required differentiation before calculus | Algebra/double counting primary; boundary and optional return clarified |
| `ex:squares` | Used Cauchy--Schwarz before its proof | Explicit finite sum-of-squares identity |
| `ex:fibgcd` | gcd(0,0) outside stated arithmetic definition | Admissible indices specified and zero cases handled |
| `ex:intpoly` | Degree of zero polynomial treated as finite | Zero polynomial handled separately |
| `ex:catalan` | Reflection endpoint invalid at n=0 | Empty path C0=1 handled before reflection for n>=1 |
| `ex:stars` | Empty/positive composition boundaries ambiguous | k>=1 and n>=0 stated; no positive solutions for n<k |
| Derangements | D0 implicit; numerical agreement and integer rounding conflated | D0=1; exact count before limits; factorial-scaled error and separate n=1 proof |
| Surjections | 0^0 and empty-set counts unspecified | Empty-map convention and zero-size cases explicit |
| Real triangle inequalities | Used in analysis before proof | Proved before first limit estimates; later chapter recalls them |
| Archimedean property | Arbitrarily large natural N used without deriving it from contract | Short supremum proof from completeness before convergence examples |
| `prop:seqcrit` | Cauchy condition used a real supremum of a possibly unbounded set | Direct quantified criterion |
| Continuity/derivatives | Deleted-neighbourhood limit at isolated point can be vacuous | Accumulation-point limit and interior derivative conventions; endpoint cases explicit |
| `prop:early-differentiation` | Power/chain rules used before proof | Original sum/product/quotient/chain proofs moved earlier; real-power derivative derived |
| `prop:early-ftc` | Series integral comparisons preceded FTC | Minimal FTC proved from explicitly admitted integral axioms |
| `prop:safe-sums` | Infinite nonnegative exchanges deferred or implicit | Rectangle-supremum proof and absolute-rearrangement argument |
| Stirling core | Taylor estimate before Taylor theory | Finite identity integrated with a controlled remainder |
| Harmonic numerical exercise | H12366 and H12367 rounded incorrectly | 9.99996 and 10.00004 to five decimals |
| Complex exponential | Re-defined already admitted sine/cosine; series identification deferred implicitly | Define from real functions and addition laws; prove series agreement explicitly in `ex:taylorln(c)` |
| Roots/cyclotomy | Root-factor and monic-division machinery later | Short elementary arguments at point of use; systematic toolkit follows |
| `ex:sumdist`, `ex:circulant(c)` | n=1 invalid or undefined | Explicit n>=2 domain |
| Polynomial arithmetic | gcd and Bézout genuinely absent | Complete Euclidean algorithm, monic gcd, Bézout and cancellation proof over fields |
| Polynomial normalisation | Symmetric functions described as polynomial in nonmonic coefficients | Refer to coefficients of the monic normalisation |
| `ex:logconcave` | Zero/constant degree ambiguity; false Maclaurin forward promise | n>=1 and nonzero leading coefficient; Maclaurin identified as externally referenced outlook |
| Minimax uniqueness | Delicate weak sign-count argument incomplete | Lagrange leading-coefficient proof at alternating extrema |
| Vector spaces/maps | Axioms and several foundational proofs compressed into reminders | Explicit axioms, examples, kernel/image, rank-nullity, matrix/composition/change-of-basis proofs |
| Spectral theorem | Used orthogonality/Gram--Schmidt before establishment | Inner products and projection precede spectral theorem; complex norm and real eigenvector explained |
| Quadratic forms | Positive semidefinite vocabulary undefined | Definitions and spectral eigenvalue criteria with examples |
| Hilbert conditioning | Used unproved largest-eigenvalue bound | Elementary Rayleigh/determinant bounds suffice |
| Commutator exercise | Overstated implication for all quantum mechanics | Restrict conclusion to canonical commutation relation in finite dimension |
| Taylor remainder | [a,x] ambiguous when x<a | Unoriented segment for suprema, oriented integral retained |
| `ex:lhopital` | Asked Taylor at zero for x log x, not smooth there | Valid Taylor comparisons for first two limits; elementary exponential bound for third |
| `ex:trapezoid` | Requested eight-decimal guarantee not proved by numerical comparison | Finite degree-19 Taylor/root-filter certificate <4.42e-9; upgraded to three stars |
| Improper integral example | Conditional convergence asserted briefly | Explicit integration-by-parts convergence and harmonic-block nonabsolute proof |
| Gamma log-convexity | Circular later-inequality dependence | Complete proof moved to Chapter 8; Young/integral normalisation and endpoint cases supplied |
| AM--GM/Carleman | Positive-input statement applied to zero inputs | Explicit nonnegative extension and proved safe-sum rule |
| Probability vocabulary | Many definitions in one paragraph | Sequential finite models, conditional probability, independence, variables and moments |
| Countable laws/coupons | Infinite expectation used under finite-only contract | Explicit countable masses, truncation tail identity and finite stopped-word law |
| Independence | Pairwise and mutual notions insufficiently distinguished | Product proof and pairwise-but-not-mutual counterexample |
| Covariance | Algebra/probability connection too implicit | PSD proof and sampling-spectrum bridge, with degenerate k=0,n cases |
| Birthday bound | Near-threshold numerical logarithm required care | Certified logarithm enclosure rather than unproved decimal comparison |
| Ramsey and Monty exercises | Boundary and host-model hypotheses needed | Explicit n,k domains and informed-host selection assumptions |
| Birthday-waiting refinement | Heuristic did not prove 2/3 correction | Advanced referenced outlook clearly separated from elementary finite expectation |
| Interval notation | New language used (a,b), legacy text used ]a,b[ | Synonyms explained for all readers |
| Local result pointer after insertion | “By (c)” pointed past newly inserted gcd | Explicit `prop:rootsfactor(c)` reference |

No stated substantive mathematical conclusion was silently weakened to avoid a
proof. Added domains repair undefined/false degenerate cases and are recorded
above. Advanced outlooks remain identified as such. No original numbered exercise
was deleted; the full original exercise sequence is recoverable by identifier and
the numbering concordance.
