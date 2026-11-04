# Volume 2 — global dependencies and story review

DEP-073,4 November2026. This supplements the exact-source inventory, actual
Volume1 proof-site crosswalk, named/keyed proof registers and whole-source
review. Those records contain the reconstructions; this record checks where
the tools enter and what may depend on them. All checks are internal.
Historical/bibliographic completeness, final formats and external acceptance
remain separate. A reference/context checker is not a formal proof checker.

## Printed route and permitted edges

The11 chapter sources were read completely in printed order, including all144
prompt/hint/idea/writeup groups, examples, captions and bibliography. Preface,
field guide, blurb/listing and cover note were separately read. The inventory's
319 local references resolve. Each of the85 forward occurrences has its own
manual role/explanation and exact context hash in
[the forward-use register](volume2-forward-reference-review-2026-11-04.json).
None is accepted as a needed forward premise: they are navigation, diagrams,
practice after a local proof, alternate proofs on taught routes, or explicitly
future outlooks. Duplicate references on one line remain separate entries.

Run `python3 review/volume2-independent/check_dependencies.py`. New/removed/
changed forward contexts, unexplained exceptions and a forward-premise role
fail; three regression tests exercise those failures. The guard also freezes
Volume1 source hashes, to force reconsideration if the actual earlier toolkit
changes. Those hashes record provenance, not a claim that every Volume1 proof
has been newly audited. Plain-text implications and notation still require the
manual source/argument review; no mechanical all-mathematics certificate is
claimed.

| Chapter | Incoming tools actually available | New work and outgoing question |
| --- | --- | --- |
| 1 Divisibility | High-school integer arithmetic; actual Volume1 well ordering/induction, elementary group definition, counting/probability, limits and areas | Integer division gives gcd/Bézout, prime cancellation/FTA, valuations and algorithms. Prime factorisation raises infinitude/counting questions. |
| 2 Primes | C1 division/FTA/valuations; Volume1 positive series/log/integral comparison and finite counting | Euclid, reciprocal-prime divergence, Chebyshev/Bertrand and elementary sieve. Residues organize prime questions without using a later progression theorem. |
| 3 Congruences | C1 gcd/Bézout/FTA; Volume1 polynomial division/root bound/binomial arithmetic | Rings/fields/units, modular arithmetic, Euler/Wilson, CRT and locally proved Hensel. Divisor/periodic identities lead toward functions and orders. |
| 4 Arithmetic functions | C1 FTA; C3 totient/divisor count; Volume1 finite sums, limits/integral comparisons and finite probability | Convolution/Möbius inversion, perfect numbers and hyperbola count. Multiplication of residue classes suggests order/generators. |
| 5 Primitive roots | C3 unit groups/CRT/polynomial root bound; C4 inversion and preceding optional mean-value material only where explicitly required | Orders, cyclicity, lifting,2-power classification, cosets/discrete logarithms. Squares become a group question. |
| 6 Reciprocity | C3 Euler/CRT/Hensel; C5 generators; Volume1 complex roots, finite additive orthogonality and prime-cyclotomic irreducibility only on the optional Gauss-sum route | Legendre/Jacobi and full reciprocity; finite tests/certificates and locally taught character-sum extensions. Sums of squares become the next equation question. |
| 7 Sums of squares | C1 FTA/descent; C3 finite field algebra; C6 supplementary−1/reciprocity and elementary residue obstructions | Two/four-square proofs and lattice count. The quoted three-square converse is future context, not a premise in either proof or the redesigned triangular-equivalence exercise. |
| 8 Diophantine equations | C1 factor valuations; C7 two-square divisibility; high-school quadratic/coordinate geometry | Pythagorean parameters, fourth-power and7 descents, conic exceptions, Mordell shift and Markov descent. Pell asks for exact identities from approximation. |
| 9 Continued fractions | C1 Euclid/Bézout/Fibonacci; Volume1 real limits, e/pi irrationality and elementary quadratic algebra | Convergents/error/best approximation/periodicity and complete Pell search/power classification. Quadratic norms motivate changing rings. |
| 10 Gaussian/Eisenstein | C3 ring/field axioms; Volume1 conjugation/modulus multiplication; C5 primitive roots; C7 two-square existence | Concrete norm division proves Bézout⇒irreducible-prime⇒UFD, classifications/counts and closed-family cubic descent. Failure at sqrt−5 is proved locally. |
| 11 Characters/products/sieve | C3 CRT; C5 complete cyclic-product classification; C4 convolution/Möbius; Volume1 complex roots and real series/calculus | Characters/count/orthogonality, absolutely convergent products and exact finite sieve. Optional finite Gauss/Jacobi sums, formal theta identities and local counts have earlier or locally supplied proofs. Analytic boundary nonvanishing is explicitly conditional/future. |
| Field guide/preface/jacket | Concrete examples and earlier proved tools above; high-school squares mod4 in preface | Summarize exact scopes and invite Volume3's group/ring/homomorphism viewpoint. General ideals and p-adic notation are marked future previews, not exercise prerequisites. |

The chapter graph moves only forward through proved inputs. Optional detours
may require an earlier exercise's complete solution; their prompts name that
route and those solutions are supplied. A reader is never told to obtain a
missing proof by reading a later book.

## Technical meanings and earliest permitted applications

“First” here distinguishes a motivational name from a mathematical premise.
Preface names of later subjects, where-this-leads boxes and a labelled diagram
preview do not supply theorem inputs. The following ledger traces substantive
meanings and applications; the full proof obligations stay in the keyed/named
and unnamed registers, not in a keyword-search result.

| Terms/notation | Definition and full justification available before required use | Concrete example/first application and boundary |
| --- | --- | --- |
| Divides,prime,unit,N,N* | C1 opening fixes integer domains/divisibility/prime. DEP-073 adds the missing integer-unit definition at its first use and proves the only possibilities±1 by abs(a)abs(b)=1; direct integer inverse/sign gives a separate check. |252/198 division;1 is excluded from primes without assuming the later ring-unit definition. High-school prime meaning also supports preface5/7. |
| Well ordering,strong induction | Actual Volume1 ch01-sums induction/well-order equivalence, crosswalk. C1 thm:div derives remainder existence and uniqueness. | Negative division−17 and Euclid termination. No later completeness principle is imported. |
| Group,subgroup,closure | Actual Volume1 def:elementary-group. C1 subgroup paragraph defines subtraction closure and derives identity/inverses/sums before prop:subgroups. |6Z works; odds fail;4Z+6Z is a combination set. General ideal language is explicitly later. |
| gcd,lcm,coprime,Bézout | C1 definition after prop:subgroups; thm:bezout proves combinations and divisibility characterization, with zero conventions. |252/198 certificate; extended recurrence and full ax+by=c family. |
| Prime cancellation,FTA | C1 thm:gauss then thm:fta, existence by strong induction and uniqueness by prime cancellation. | All later factor/valuation arguments use these local proofs. Integer units do not rely on C10. |
| Integer/rational valuation | C1 defines prime exponents after FTA, proves product/divisibility formulas, defines rational valuation by a difference and proves representation independence/integrality. | Factorial-ratio and random-valuation exercises; v_p(0) is excluded until the marked field-guide preview. |
| Probability,expectation,independence | Actual Volume1 finite experiment/expectation/independence and finite inclusion–exclusion proof sites in crosswalk; C1 prompts state finite uniform experiments before limits. DEP-073 spells out asymptotic independence as factorization of fixed joint limiting probabilities. | pb:valuation,pb:parity; no uniform measure on all positive integers and no unbounded limit exchange without the proved tail estimate. |
| O,o,~,log derivatives,integrals | Actual Volume1 sequences reminder and derivative/MVT/FTC/series proof sites; C1 also explains O(log b) before its exercise uses. | C2 elementary logarithm inequalities, C4 hyperbola error, optional powerful-number estimates. Base of Pratt's k digits now stays explicitly binary in prompt and proof. |
| Squarefree and exponent decomposition | C1 pb:parity solution's final paragraph defines a positive squarefree integer; C2 ex:erdosdiv repeats it and derives n=ab² uniquely by exponent parity. DEP-073 also repeats the definition in the main C4 multiplicative-functions example, so first-route readers need not have taken those optional exercises. | Empty subset gives1; C3 Korselt and C4 Möbius use already available meanings. See the exact source correction below. |
| Residue/congruence,modulus,representative | C2 tracks locally define a≡bmod4 as4 divides a−b. C3 general definition/operations and prop:ringZn precede their algebraic uses. | Units/linear cancellation, clock/CRT grids; all m≥1, with mod1 explicitly retained. |
| Ring,field,unit,F_p | C3 axioms and definitions before prop:ringZn; field condition0≠1 and nonzero units; F_p and modular inverses defined/proved before polynomial calculations. | Mod6 nonunit example and prime fields. Preface/C1 ring names are future outlooks. |
| Ring morphism,isomorphism,CRT/product | C3 defines maps preserving addition,multiplication,1 and bijection before thm:crt; theorem proves both compatible coordinate construction and uniqueness. | Explicit Sunzi23 and fresh52mod105; C11 unit-product proof uses this earlier bijection, not later abstract ring theory. |
| Totient,order,cyclic group,primitive root | Totient defined C3; prop:units/Euler proved there. C5 defines least positive order/cyclic generator then prop:order/thm:cyclic and full prime-power classification. | Powers7mod100 preview is computed directly; modulo13/29 examples and all2-power representatives use the proved classifications. |
| Coset,subgroup of squares,index | C5 defines aH and derives partition/equal sizes before using index; cor:mod8squares identifies the square subgroup. | Four explicit mod16 cosets; generalized Wilson solution includes its own four-element partition argument. |
| Discrete logarithm | C5 defines index in Z/(p−1)Z after primitive-root theorem; exponent addition follows directly from powers and uniqueness. | x^4=3 and fresh x^5=3mod13; ex:kth applies the already available coordinate map. Hardness is qualified future computational context. |
| Arithmetic function,multiplicativity,convolution,epsilon | C4 definitions then prop:conv proves algebra and unit/inverse criterion; thm:mobius supplies mu*1=epsilon. | Exact12/30 divisor sums, fresh inversion/workshop data and primitive-word counts. |
| Primitive word,period,necklace | C4 exercise defines a shorter-word power as concatenation before use; full solution proves unique primitive root and divides by orbit length only after proving it. | Binary length4 count; irreducible-polynomial count is a Volume3 preview with the required degree factor, not a C4 premise. |
| Formal derivative/simple root/lift | C3 formal coefficient derivative is defined before binomial one-step expansion and thm:hensel. Unit derivative persists after lifting. |2→7→57 roots of−1mod5^k. A p-adic completion is not needed or claimed here. |
| Indicator function | DEP-073 expands the first C3 hint's word into its1-at-a/0-elsewhere meaning. The polynomial1−(x−a)^(p−1) has those values by the already proved Fermat theorem. | All subsequent finite counts/inclusion–exclusion/character detectors use this same meaning. Nonunit detector terms are checked explicitly. |
| Legendre symbol,Euler criterion,Gauss lemma | C6 definition; thm:eulercrit uses C5 cyclicity or square counting; thm:gausslemma supplies the residue-sign proof and cor:two. | Complete residues11, supplementary signs, lattice reciprocity and partial expectations. |
| Jacobi symbol | C6 definition multiplies Legendre factors over a positive odd denominator; prop:jacobi proves laws. | Jacobi1 need not imply a composite-modulus square; polynomial/quadratic tests do not use its converse. |
| Gauss sums/root phases | Actual Volume1 finite geometric orthogonality and conjugation on the optional C6 route; ex:gausssum defines the finite sums and proves the additional signs locally. C11 cubic prompt defines e(t) independently of a representative. | C6 second QR proof is separate from the full lattice proof. No unseen Fourier-analysis theorem or later field extension is imported. |
| Pseudoprime,Carmichael,liar,certificate | C3 Korselt prompt defines squarefree/Carmichael; C6 exercises define the various tests and give complete local order/CRT counts. |511-composite figure uses all bases under the stated model; Pratt/Pocklington/Proth routes have earlier orders/primitive roots. Elliptic methods are outlook only. |
| Descent,minimal measure,two/four squares | C7/C8 explicitly select least positive integer multiplier,height or exponent and verify nonzero/integral strictly smaller outputs. | Thue two-square, Euler four-square, Fermat fourth-power and7-descent. No unproved three-square converse supports them. |
| r2,representation equivalence | Defined as ordered signed integer pairs in C7; count formula is explicitly deferred and locally proved in C10 thm:r2 by UFD plus a multiplicative divisor sum. | Prime uniqueness also deferred.65 and85 representations are independently exact; no circular uniqueness in C7. |
| Conic,chord,affine exceptions | C8 prop:chord restricts a rational quadratic to a line, checks line-factor/tangent/vertical/degree-drop cases. | Two exact unit-circle charts; the caption's Markov panel now explicitly defines its positive integer triples as a preview. |
| Markov triples/tree,Vieta jump | DEP-073 caption defines the relation at its first diagram; thm:markov below proves preserved equation, positivity, decreasing sorted sum and unique parent. | All nine displayed nodes/eight edges checked directly. Preview data do not prove the infinite structure. |
| Convergent/complete quotient/determinant | C9 finite definitions then prop:cfconv; floor/reciprocal recurrence and exact tail are proved before approximation/existence/best lemmas. | Negative workshop and exact sqrt2 order. Legendre is proved before the complete Pell-search bound uses it. |
| Periodic quadratic expansion | C9 thm:periodic uses quadratic field arithmetic explicitly derived there and bounded integer quadratic coefficients. | sqrt3/sqrt2 periods; D61 exact period/candidate count. Finiteness is proved generally, not inferred from a decimal sample. |
| Real-quadratic norm/ring/unit/Pell | C9 defines Z[sqrt(d)] and norm/unit before the proof. thm:pell proves existence and minimal-unit power structure; local Legendre bound proves all positive solutions occur among convergents. | Integer coordinates distinguished from the larger full ring: d5 Pell generator=phi^6. Full algebraic-integer classification is future work. |
| Associate,irreducible,prime element,domain | C10 defines them using prior ring axioms before norm-unit/Euclidean results; cancellation comes from a complex subring, not an inverse in that subring. | thm:six and coprime-without-Bézout example show precisely which reverse implication fails in sqrt−5. |
| Complex quadratic norm,Euclidean division,UFD,valuation | Volume1 conjugation gives multiplicativity; C10 proves integer norms/unit lists, rounded remainder bounds, Bézout, irreducible⇒prime and UFD before exponent extraction. | Three complete division chains; Gaussian/Eisenstein classification and cubic descent use the local UFD. |
| Ramification | C10 first1+i example defines the unit-times-square behavior before subsequent uses; lambda²=−3omega is proved explicitly. | Corrected norm3 lambda arrow and all prime-disc ink classes. General ideal ramification is a later topic. |
| Dirichlet character,homomorphism,principal/nonprincipal | C11 def:t1-character and immediate homomorphism identity/inverse proof precede the cyclic-product count and orthogonality. Zero extension is justified separately. | Full modulo5 table and new modulo8 rows/detector. Nonzero values are proved roots of unity, not assumed. |
| Dirichlet series,Euler product,zeta,L | C11 p-series/absolute convolution lemmas precede thm:t1-eulerprod; finite product expansions and tail/nonzero estimates justify every infinite limit. Earlier optional zeta2 uses have local convergence proofs. | Principal-mod6 removed factors and mu/zeta identity; no substitution s1 into an s>1 theorem. |
| Summation by parts,boundary logarithm | C11 finite telescoping identity is derived in ex:t1-char-series. DEP-071 real-log integral error uses the exact actual Volume1 FTC/derivative proofs. | Ordinary chi4 convergence is proved; the prime-progression boundary continuity/nonvanishing step remains explicitly conditional/future. |
| Jacobi sums/cubic trace | C11 pb:fermatcubic prompt defines J and now names it before hints use the name; Gauss-sum product/norm and the three-cycle mod3 proof are local. | p7/13 and all207 plotted traces separately checked. Norm uniqueness uses the earlier C10 UFD, not Volume13. |
| Theta series/formal products/four-ball volume | C3 pb:ramanujan5 defines formal coefficient operations and proves the triple/cubic product identities before C11 pb:jacobi cites them. C11 derives its needed4-ball volume by a finite annulus squeeze. | Jacobi four-square coefficients and10^7 count; no complex-analytic infinite-product theorem or later measure volume is imported. |
| Local/primitive density,lifting count | C11 pb:densities defines the finite residue counts and limits, proves primitive lift recursions and the dyadic pairing before evaluating the product. | Uses the earlier finite-field square counts and locally proved Jacobi formula. Q_p/O_K are not premises. |
| Powerful numbers/complex Dirichlet phase | C11 pb:powerful defines exponent condition and unique square/cube decomposition; solution defines n^(−s) and complex zeta domain before regrouping, with real absolute majorants. | Count error from local tails; infinitely many neighboring pairs use C9 Pell. |
| General ideals,number fields,algebraic integers,p-adic symbols | C1/C10 references are explicitly future motivation. Field guide marks the later-volume preview and supplies basic names, while Volume13's actual prop:OK/ideal/unit sites were checked for accuracy. | No offered exercise depends on those later theories. Volume3 studies the already encountered homomorphism rule; it does not first name it. |

## Whole-book seams and remaining gates

The main route retains one concrete incoming/outgoing arithmetic question per
chapter. Mandatory tools precede use; future applications are marked as such.
Repeated examples/workshops were replaced with new data or removed with the
old/new obligation documented in the whole-source record. All144 exercise
keys retain hints/full solutions, including the documented redesigns; the
exercise count is not used as a proxy for proof completeness.

New global repairs: integer-unit definition at C1 first use, main-route squarefree definition, explicit joint-limit
meaning, indicator meaning in C3, naming J before its hints, a Markov diagram
preview with its defining relation, the actual4^a(8b+7) three-square exclusion,
and binary-digit scope in Pratt's complexity explanation. No cover art or
exercise statement/answer was removed. The first-reader/editorial review,
complete global history/bibliography/current-status pass and final-source
artifact/every-page/CI gates remain open. This file does not close P00–P13.
