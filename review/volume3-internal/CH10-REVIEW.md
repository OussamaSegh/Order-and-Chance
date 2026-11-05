# V3-011 — full Galois correspondence and radical criterion

Solo internal AI review, not human refereeing or formal verification. Read the
entire chapter, all13 named proofs,11 prompts/hints/complete solutions, both
figure sources, notes and bibliography. CH10-PROMPT-FIRST.md records first
solutions before opening this chapter's supplied answers, except the explicitly
disclosed prior exposure to ex:phin and pb:kronecker during the C7 migration.
Reconstructed every supplied argument adversarially after that comparison.

The exact reader-facing contract remains finite extensions K⊆L⊆C. Thus the
correspondence and radical criterion here are earned in characteristic zero;
they are not represented as a proof of the general inseparable/positive-
characteristic theory. C8 supplies the repeated-root counterexample and C9 the
complete finite-field case. The convention is now illustrated explicitly before
Artin's lemma. No original named theorem has been replaced by a weaker target.

## Named results: hypotheses, reconstruction A, adversarial B

| Key | Exact hypotheses/domain and claim | Reconstruction A | Adversarial B and boundaries |
| --- | --- | --- | --- |
| lem:permroots | Finite L/K in the chapter contract; automorphisms preserve roots of K-polynomials, and act faithfully on the distinct roots generating a splitting field. | Apply σ coefficientwise to P(α)=0. Injectivity permutes the finite root set, composition convention is ordinary function composition, and a map fixing all generators fixes their rational expressions. | Reconstruct inverse action using σ inverse, and check kernel on every numerator/denominator; nonzero denominators stay nonzero under an injective field map. Explicit distinct-root set now avoids ambiguity from repeated indexed roots. Nonzero constant polynomial has empty root set and splitting field K, giving the trivial action; zero polynomial is excluded from the polynomial Galois definition. |
| prop:autbound | Finite L/K⊆C; number of K-automorphisms≤degree. | C8 primitive element γ generates L, each automorphism determined by γ's image, a root of its degree-D minimal polynomial; root bound gives≤D. | Different route: C8 root-extension tree bounds embeddings by product of successive simple degrees D; automorphisms are a subset. Degree1 gives exactly one; a nonnormal real cubic has fewer than degree. No primitive-element theorem for inseparable extensions is assumed. |
| thm:galoischar | Finite K⊆L⊆C; splitting field, full automorphism count, fixed field K and normality are equivalent. | Splitting field of squarefree part gives count via C8; full count and tower force fixed field K; orbit polynomial over fixed field contains irreducible minimal polynomial, forcing it to split; a primitive generator and normality give a splitting field. | Adversarial reconstruction checks squarefree replacement before count, coefficients of the orbit polynomial fixed by the entire group, and degree/tower equality before concluding F=K. L=K works with a linear polynomial. Positive characteristic counterexample Fp(t)⊂Fp(t^(1/p)) has degree p but one automorphism, though Xp−t splits; explicitly supplied locally. The characteristic-zero restriction is essential and disclosed. |
| lem:artin | Finite L/K⊆C, H≤Gal(L/K); degree over fixed field equals order H and the full fixing group is H. | Orbit polynomial of each α has coefficients in F=L^H and degree≤order H. Primitive γ for finite L/F gives degree≤order H. H contained in Gal(L/F), whose size≤degree, gives both equalities. | Independently observe H acts freely on the images of a primitive γ: fixing γ fixes L. Its orbit therefore has exactly order H distinct roots of the minimal polynomial, giving the opposite degree bound directly. Check F finite over K, L/F finite and characteristic zero before primitive invocation; H trivial/full, L=K handled. No use of FTGT to prove its own fixed-field lemma. |
| thm:ftgt | Finite Galois L/K⊆C; inverse inclusion-reversing subgroup/field correspondence, both degree formulas, conjugate fixed fields, normality and quotient restriction isomorphism. | Artin recovers H. A splitting polynomial over K still has splitting field L over intermediate M, so L/M Galois and its full fixed field M. Tower gives index degree. Conjugating a fixed element gives σ(L^H)=L^(σHσ^-1). Normal H preserves M; restriction kernel H and cardinality/automorphism bound give surjectivity and Galois count. Conversely normal M/K is a splitting field whose root set is permuted by every σ, hence M preserved and H normal by injectivity. | Separate reconstruction starts with each proposed assignment and proves each inverse, not just one inclusion. Both inclusions of conjugate fixed fields use inverse σ. Restriction is defined only after σ(M)=M, and surjectivity is proved rather than assumed. Trivial/full subgroups, M=K/L, nonnormal real quartics checked. Corrected prose: extension of M-automorphisms alone does not characterize normality (they extend even for nonnormal M); preservation of M by every automorphism of L does. |
| prop:cyclo | n≥1, K⊆C; K(ζn)/K Galois, group injects into units mod n and is abelian; Q and prime n=p give cyclic order p−1. | All nth roots are powers of ζn, so splitting field; images preserve order, hence exponent a is a unit. Composition multiplies exponents, kernel fixes the generator. Prime irreducibility supplies degree p−1; C8 Galois count and V2 primitive roots give isomorphism/cyclicity. | Direct quotient-field map sending ζp to ζp^a supplies every prime-case automorphism. General K can contain ζn already, with trivial image; surjectivity is not asserted there. n=1 and p=2 give trivial groups, including the unit group of Z/1Z. Stale V1 Chapter7 pointer corrected to actual Chapter3 prime-cyclotomic proof. General n irreducibility is now fully worked before subsequent invocations. |
| thm:gw | Integer n≥3 with φ(n) a power of2; constructible regular n-gon, including all listed Fermat primes. | Injection makes G a2-group; C5 cor:pk gives index2 subgroup recursively. FTGT/Artin yields successive quadratic fields ending at Qζn; C8 Wantzel and multiplication closure construct vertices. | Alternative since G abelian2-group, C7 structure gives a cyclic2-factor series; fixed fields give the same quadratic tower. Empty series mathematically valid. Added full converse: normalize constructed center/radius, ζn belongs to a quadratic tower, so earned degree φ(n) divides2^r. Phi degree now precedes use. Totient prime-power formula/odd-divisor factorization prove exact n=2^k times distinct Fermat primes. No assumption that every extension of power-of-two degree is constructible. |
| lem:kummerstep | m≥1, F⊆C contains primitive ζm, b^m∈F; F(b)/F Galois with abelian group. | b=0 trivial. Otherwise all roots bζm^j lie in F(b), so splitting field and Galois. Image σ(b)/b=ζm^k gives injective homomorphism to additive Z/mZ because σ fixes ζm. | Independently characterize automorphisms as a subgroup of the root-scaling maps that preserve the minimal polynomial. Composition is addition only because roots of unity lie in the base. b=0, m=1 and trivial subextensions checked; without ζ3 the real cube-root field is not normal. Characteristic zero is stated, so separability and roots-of-unity order are earned. |
| thm:radsolv | Nonzero P over K⊆C whose roots lie in a finite radical tower; Gal(P/K) is solvable. | Each radical algebraic over K by finite tower. Take splitting field E of all their K-minimal polynomials plus X^N−1. Order conjugates by original tower step; each new conjugate's njth power lies among conjugates of earlier radicals, and ζnj is already present. Kummer steps and initial cyclotomic step are Galois abelian. FTGT over each preceding field gives a subnormal abelian-quotient series; restriction to P's splitting field gives a solvable quotient. | Reconstruct every conjugate extension using actual C8 extension theorem and check the ordering supplies its radicand before invocation. Intermediate fields need not be normal over K; only each next step over its predecessor and final E/K are normal. Heading corrected accordingly. No circular restriction map or premature normal-tower claim. Empty tower/N=1, zero radicals, repeated roots of P and trivial conjugate steps all work. |
| thm:abelruffini | f=X5−4X+2 over Q has group S5; no individual root is radical, so no universal quintic radical formula. | Eisenstein2; signs at−2,0,1,2 give three distinct real roots; derivative has two real zeros, Rolle rules out four. Irreducibility/char0 ensures all roots simple. Tower/Cauchy gives a5-cycle; conjugation gives one transposition. A nonzero power still of prime order makes its endpoints adjacent, then conjugates yield adjacent swaps and S5. Nonabelian simple A5 obstructs solvability. | Found a genuine gap: original direct repeated-root check examined only ±ρ, although derivative has four complex zeros. Repaired for arbitrary complex z: z4=4/5 implies f(z)=2−16z/5, so a common root would be5/8, impossible. Independent Sturm computation gives exactly3 real roots and gcd derivative1. Prime-cycle power argument checked for every endpoint, not an unspecified long cycle. Individual-root exclusion now earned by normal solvable envelope of any hypothetical radical tower and irreducibility; original proof concluded only not-all-roots. |
| lem:dedekind | Finitely many distinct automorphisms of a field L; they are L-linearly independent as functions on L. | Choose nonzero functional relation of least support r≥2. Pick y separating σ1,σ2, evaluate at yx and subtract σ1(y) times original; one term disappears and second remains, contradiction. | Independent matrix formulation: a least relation among columns of all evaluation vectors is contradicted by diagonal multiplication at a separating y. Verify x remains arbitrary after substitution; coefficients are in the field and c2 times a nonzero difference is nonzero. n=0 vacuous,n=1 evaluate1; proof in fact works in any characteristic without using the chapter's zero assumption. |
| prop:kummer | m≥1, F⊆C contains ζm, E/F finite Galois cyclic order m; E=Fθ with θ^m∈F. | Dedekind makes the resolvent ∑ζ^-j σ^j a nonzero linear map, so choose θ≠0. Reindex gives σθ=ζθ, hence θ^m fixed and in F. No nonidentity power fixes θ; FTGT makes its generated field all E. | Different derivation uses the order-m linear operator σ: its polynomial Tm−1 splits with distinct roots, so diagonalizable; Dedekind prevents the primitive-eigenvalue projection from vanishing. That eigenspace supplies the same θ, and m distinct conjugates force degree m. No nonzero-trace shortcut. m=1, θ≠0 and exact root-of-unity order checked; this is a cyclic extension result, not arbitrary abelian extension in one radical. |
| thm:galoiscrit | Nonzero P over K⊆C; radical-solvable iff Gal(P/K) solvable. | First direction prior theorem. For converse N=order G, adjoin ζN, restrict G'=Gal(LζN/KζN) injectively into solvable G, so G' solvable and its order divides N. Remove repeated subgroup terms and refine abelian quotients to prime cyclic factors. Reverse FTGT series and apply Kummer because every factor prime divides N, producing radical tower ending in LζN. | Adversarially verify restriction preserves L by its root generators, kernel trivial since ζN fixed. Surjectivity onto G is neither needed nor asserted. Refinement now explicitly terminates because strict-chain indices multiply to order G'; empty series handles G'=1. All θ steps have roots of unity in their actual base. Added earned degree≤4 consequence via S4's actual C5 series, including nonzero constants/empty roots. No future theorem supplies a premise. |

## Exercises: complete comparison and adversarial second check

First solutions, exact domains and discovery paths are in CH10-PROMPT-FIRST.md.
Each row below was compared against the actual prompt, hint, finding idea and
full write-up, including all parts. All solution keys and complete answers remain.

| Key | Adversarial reconstruction B and boundary/comparison findings | Grade |
| --- | --- | --- |
| ex:phin | Monic long division over Z, not an unsupported algebraic-integer assertion, proves integrality. Minimal f of any conjugate is the same irreducible polynomial. If f(ζp)≠0, f divides h(Xp) with fh=Xn−1; mod p, a nonconstant irreducible factor of fbar divides hbar, making Xn−1 nonsquarefree, contradiction p∤n. Monicity preserves degrees; n=1 handled. All positive unit exponents factor into primes not dividing n, so every primitive root occurs and degree is φ(n). Independent embedding lemma gives all exponent automorphisms. Full triple moved before main general-degree uses, rather than inheriting proof availability from its prompt. | 3 retained, worked on main route |
| ex:q235 | Independent multiquadratic coefficient/sign computation or earlier biquadratic fixed-field classification excludes sqrt5. Added actual coefficient comparison earning the square-ratio implication. Enumerate all F2³ subgroups: seven planes and seven lines, matching seven quadratic and seven quartic fields. All seven radicands have distinct square classes. Hint/solution cover every requested count and list. | 1→2 for field independence plus subspace classification |
| ex:x42check | Exact eight-dimensional Q-algebra α4=2,i²=−1 computes all automorphisms, ten stabilizers and fixed-space dimensions, and15 cover edges in each actual diagram. Independently show beta±=(1±i)α have degree4 using that their squares generate Qsqrt(−2) and cannot be squares there; supplied alternative Gauss quadratic-factor exclusion for X4+8 is complete. Six normal subgroups/fields, four nonnormal quartics and explicit real-field counterexample agree. Identity/full/central cases included. | 2 retained |
| ex:zeta7 | Independent eta² exponent count gives eta²=eta+2eta'=−eta−2; supplied eta eta' table gives2. Recompute all nine table entries and degree/discriminant−7. Real fixed field degree3 also follows directly because ζ is nonreal and quadratic over Q(ζ+ζ^-1), with total degree6. No extra intermediate subgroup of C6 omitted. | 2 retained |
| ex:gauss17 | Enumerate all64 cross-sums: each nonzero residue occurs4 times, zero never. Independent subgroup-invariance and swap bijections in supplied proof give same counts. Values asserted as an unordered pair, so no unsupported plus-sign choice. Added proof that each subgroup period has stabilizer exactly H via degree16 Φ17 and zero constant coefficient; subsequent quadratic tower claim is now earned, not a slogan. | 2 retained |
| ex:sp | Independently use connected graph of conjugate transposition edges on Fp (nonzero step generates additive Fp); edge transpositions generate Sp. Supplied prime-power relabeling proof checks every transposition endpoint. p2/p3 valid and not called nonsolvable; particular degree5 only excludes radicals. Eisenstein3 and exact signs−17,3,−2,23; independent Sturm count3 and gcd1 support distinct roots. | 2 retained |
| ex:discr | Swap each pair directly in the alternating product, then use FTGT fixed field; no unproved general symmetric-polynomial theorem needed. Independently expand cubic discriminant to−4p³−27q². −108 nonsquare and81 square, irreducibility and transitivity give S3/C3 respectively. Nonzero delta is essential; chapter char0 prevents sign collapse. Corrected the idea/characteristic wording to stay within the proved contract. | 2 retained |
| ex:cardano | First reconstruction used (u+v)³−3uv(u+v), while supplied proof factors u³+v³ into three resolvents and checks all factors. Independent exact polynomial reduction with r3=−r1−r2 and ω²+ω+1 verifies both identities. The cubes satisfy the stated quadratic; branch product−p/3 is essential. p=0, repeated roots/discriminant0 and nonzero radicands checked; no division by u/v occurs. Complex intermediate roots are permitted. | 2 retained |
| pb:kronecker | Integer companion powers give integral P_r; added explicit C7 triangular/Jordan justification even with repeated roots. B uses equality of two power polynomials and permutation-cycle iteration; actual write-up instead uses finite union of their root sets and a repeated power of each nonzero root. Both prove roots of unity; P=X shows why P(0)≠0 matters, P=1 vacuous now explicit. Partb Laurent clearing gives monic Q degree2d/constant1, including endpoints±2 and zero roots. Partc Gauss leading-coefficient contradiction uses primitive5X²−6X+5, no future algebraic-integer closure. All three parts retained after prior migration. | 3 retained |
| pb:rattan | Independent prime-exponent comparison of φ(lcm)/φ(n) gives exactly n-th roots if even,2n-th if odd, including n1/2. Supplied φ(t) bound correct; now explains units±1 for t≥3. Bézout construction of ζlcm and odd root−ζn^((n+1)/2) checked. Tangent denominator nonzero, lattice edges nonzero/n≥3 and actual square exists. Found future C11 closure in Niven hint/solution; replaced by full monic cosine recurrence and rational-root proof, preserving all four parts and grade. | 2 retained |
| pb:ramacube | Source falsely called its heptagon cubic derived earlier in this chapter; now derive it locally from 1+ζ+…+ζ6=0 divided by ζ³. First reconstruction eliminates via Z=s³; supplied proof eliminates m=st, shifting m by3/2 to a pure cube. Both exact polynomial expansions agree, and real-cube-root uniqueness handles branches/signs. No division by s/t; 70-digit numerical support agrees. Complete hint/discovery/solution retained. | 3 retained |

## Whole-chapter reasoning and story

Read the opening/root-symmetry motivation, fixed-field and automorphism-group
definitions, cubic examples, every proof commentary, both full lattice examples,
totient/Fermat classification, reduction remark, radical definition and normal
envelope construction, derived structure obstruction and ending. In particular:

- Restriction maps are defined only after proving preservation of their target
  field. Normality prose was corrected: extension of an intermediate field's
  automorphisms is not the discriminating property.
- The worked cyclotomic triple is a curricular move of all parts, not deletion
  or mathematical weakening. Its source labels persist; exercise numbering
  changes automatically. V3-011-cyclotomic-migration.json maps old/new positions.
  Kronecker's prior C7 relocation remains earned, now with its prerequisite
  earlier in C10 rather than immediately adjacent in Exercises.
- The full polygon converse now uses the actual tower and φ(n) degree proof,
  rather than a prime-only corollary as an unexplained general premise.
- The finite-field proof of reducibility of X4+1 modulo every prime now comes
  before the general Dedekind reduction outlook, including p=2. The latter is
  explicitly quoted future arithmetic and supplies no premise. It asserts a
  matching cycle type, not an arbitrary matching of complex and reduced roots.
- The solvable envelope contains all conjugates of each radical in an order
  that earns every radicand. Intermediate stages need not be normal over K.
  Refinement removes repeated terms and proves termination before Kummer use.
- The quintic check now covers all complex critical points. No individual root
  is radical by the same normal-envelope construction; the stronger wording is
  no longer supported merely by a not-all-roots conclusion.
- The ending now leads to the actual C11 opening about matrix actions/traces.
  The earlier catalog of Langlands/Shafarevich/date/current-open-status claims
  was replaced by the earned radical/group distinction and an explicitly posed
  inverse-Galois outlook question. No theorem or exercise target was removed.
  Völklein remains further reading. The initial historical epigraph was replaced
  by the mathematical question, avoiding an imprecise age claim about a formula.

Exact earlier proof reads: V1 ch05 `prop:seqcrit` (including peak/subsequence
proof), elementary differentiation, `thm:ivt`, `thm:evt`, `thm:mvt` with Fermat/
Rolle/mean-value proofs; V1 ch03 actual Gauss/Eisenstein/prime-cyclotomic and FTA
sites already read; V2 primitive roots; V3 C2 kernels/quotients, C4 adjacent
transpositions/A5 simplicity, C5 `cor:pk` and `prop:solv` full proofs and S4 series,
C6 fraction fields/Gauss, C7 companion/Jordan, C8 simple extensions/tower/
primitive/splitting extension, C9 Frobenius. No exercise prompt or old audit
supplied a premise. The complete earlier-source hashes remain guarded.

All10 lattice subgroup/field labels and all15 edges per panel were recomputed
by exact group/algebra calculations, with independent generated-field ranks and
fixed-space nullities. All7-period table entries,64 cross-sums, seven-plus-seven
multiquadratic field counts, both quintic sign tables, graph root markers and
all220 sampled function values were checked. Additional exact symbolic support
in V3-011-symbolic-evidence.json records Cardano/discriminant expansions, two
Ramanujan eliminations, Sturm counts and cyclotomic checks n1…64. This uses
SymPy1.14.0 as support, not as a proof certificate or new CI dependency.

Primary Galois text was actually read, including the printed preface page417
opened as an image; RESEARCH.md distinguishes the1830 finite-field publication,
1831 prefatory date,1832 letter and1846 memoir publication. Other bibliography/
attributions remain pending the keyed global pass. Chapter-level mathematical
A/B acceptance is13 named/11 exercises, bringing totals to98/155 and101/163.
Global unnamed/context/history closure and actual final rendering remain open.
