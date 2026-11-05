# V3-022 — Chapter 4 complete global pass

Solo internal AI mathematical/editorial review, not human refereeing, a spoken
read-aloud session or formal verification. Read the entire current chapter in
printed order: all prose, nine named full proofs, ten prompts/hints/finding ideas/
complete solutions, actual figure source and twelve bibliography entries. All
nine named statement/proof bytes remain unchanged. Existing mathematical records
are fresh reconstructions, not historical rewrite statuses. The full converse of
the fifteen-puzzle theorem is retained, including the A3-to-A4 seed and explicit
rectangle growth to A15. Two changed exercise triples are reopened below.

The written voice/cadence/adversarial-reader pass replaces a historical epigraph
quantity with the mathematical question of attainability; replaces two repeated
proof summaries by a necessary-versus-sufficient class-union explanation and the
complete small-degree exceptions; defines commutator with its correct ambient
group; and gives the previously unexplained limit-inferior notation plus its
supremum/epsilon equivalence. The prime cyclotomic reminder now repeats Phi_p's
formula. Actual V1 already defined/proved it: this is a recap, not a false claim
of a missing earlier theorem. All full challenge targets, hints, answers and
grades remain. Future solvability/mixing/classification are identified outlooks.

## Actual earlier tools and proof sites

* V1 printed Chapter 6, source ch03-polynomials: general field division and
  factor/root arguments; prop:polynomial-bezout 127–132, with degree termination,
  last-remainder divisibility and back-substitution; thm:eisenstein 327–338 with
  prior Gauss lemma; **ex:eisen(b)** 678–685 shift/binomial/Eisenstein proof, not
  a guessed label ex:eisenb. Formal derivative/product rule 71–79 also reread.
* V2 ch05-primitive-roots thm:cyclic 133–139 and its root-bound/logical/boundary
  explanations through160: N(d) is 0 or phi(d), totient sum forces all deficits
  zero, including p2. V2 ch06-quadratic-reciprocity thm:eulercrit55–117 full
  primitive-generator proof and cor:two202–209 sign-count proof read. Hence
  (2/53)=-1, 2^26=-1 mod53. Order divides52 but neither26 nor4, so it is52;
  modulo51 order8 follows 2^8=1 and no proper divisor1,2,4 works.
* V1 printed Chapter3, ch05-sequences-series: completeness85–87, monotone
  convergence prop:seqcrit246–255, positive series/comparison/integral/Riemann/
  ratio prop:posseries554–585 and safe finite-subsums proof prop:safe-sums668–675
  actually read. V1 printed Chapter8, ch06-integrals-taylor thm:taylor168–218
  full integral-remainder/inequality proof and ex:taylorln(a)772–774 full
  factorial-remainder proof read. The real exponential's initial properties are
  admitted in the actual high-school contract; its power-series identity is
  proved by that exercise, not assumed from an exercise prompt.
* V1 ch02-counting product/bijection rules36–42 and prop:counts69–74 actually
  read: stage counts, factorials and empty permutations. The cycle-rotation
  denominator is then proved locally in C4, not inferred from a chapter title.
* Local C1 integer powers/cyclic groups/Lagrange, C2 sign/kernel/normality/index2,
  and C3 actions/orbit-stabilizer supply the group premises. All actual earlier
  proof records were read; explicit reference roles are separately classified.
  No later Sylow, Galois, characteristic tables or measure theorem is a premise.

## Keyed manual global decisions

| ID | Domain/claim | Reconstruction A | Adversarial check B / correction / limits |
|---|---|---|---|
| 4.prose.ecc3debd15e5682c.1 | navigation: The Symmetric Group chapter. | Entire current chapter, all nine named proofs, ten triples and full actual figure source read. | No advanced problem or solution omitted; named proofs remain byte-identical. |
| 4.prose.40941001d9018a00.1 | question-mathematics: The 4x4 board with only 14/15 swapped is unreachable; ask which other positions are attainable. | One transposition has sign -1, blank remains white; actual theorem proves invariant +1 necessary and sufficient. | No unsupported count of historical solvers. Necessity is motivation, not a substituted proof of attainability. |
| 4.prose.9dce65a9cabaaa85.1 | motivating-mathematics: Four numbered cards have 24 arrangements; swaps generate them. | Sequential choices 4*3*2*1; bubble each required card to its destination by adjacent swaps, decreasing remaining positions. | Cycle (123) equals (13)(12) with rightmost first. Identity uses no swaps; no parity uniqueness assumed here. |
| 4.prose.3667441ec527552a.1 | story-mathematics: Cycle lengths determine order and conjugacy type; types are partitions. | Complete cycle/orbit proof, lcm proof and point-renaming proof follow before any essential invocation. | Preview of proved targets, not a premise of those proofs; fixed points included in partitions. |
| 4.prose.4a653670776666fe.1 | unnamed-mathematics: Swap reverses sign; 3-cycle even; puzzle sign times blank colour preserved. | Actual V1 sign proof164-173, recalled in C2; 3-cycle is two transpositions. Legal slide left-composes the position map with a transposition and reverses checkerboard colour. | Blank label 16 is included, so parity change concerns S16, not a fictitious fixed-blank tile permutation. Full converse earned below. |
| 4.prose.3d13b272d98c2148.1 | story-definition: An is even subgroup; simplicity n>=5 leads to radicals obstruction. | An is kernel of earlier sign map; quotient requires normal subgroup. Simplicity theorem proved later here before C5/C10 use. | Solvability/radicals are identified future questions, never assumptions in the group proof. |
| 4.prose.f96f6ebf395266e0.1 | convention: n>=1 by default; sigma tau applies tau first. | All displayed transposition, conjugacy, rectangle and commutator products reconstructed with this convention. | Explicit n>=2 for split lemma and n>=5 for simplicity; S0 appears only in separately stated probability boundary. |
| 4.prose.cb4c9d4c4a1fecf2.1 | navigation: Cycles section. | Definition, concrete action and full uniqueness proof read. | No premise in heading. |
| 4.definition.def:cycle | definition: Distinct a1..ak in [n], k>=2; cycle, support and disjointness. | Specified map is bijective, inverse reverses traversal; fixes complement. | Repeated entries excluded; fixed 1-cycles later explicitly a counting convention; identity is empty product. |
| 4.prose.47f20666e3664552.1 | unnamed-mathematics: A k-cycle has k cyclic starting names; disjoint cycles commute. | Each choice of starting point follows same directed successor map; there are k distinct possible first entries. For each point at most one disjoint cycle acts nontrivially. | B equality checked pointwise on either support and complement; disjointness essential, (12),(23) do not commute. |
| 4.prose.138f7b9053dfdfe6.1 | definition-example: Cycle type counts fixed points; (142)(35) in S6 has type 3,2,1; S5 identity 1^5. | Actual orbit supports {1,2,4},{3,5},{6}; sum lengths 6. | Same written permutation in S5 would lack the final 1: ambient set matters. Type notation already introduced locally in C3. |
| 4.prose.c5ff113727539c2b.1 | story-mathematics: Conjugation renames points without changing cycle lengths. | tau sigma tau^-1 sends tau(a) to tau(sigma(a)); full converse via matching equally long cycles below. | Preserving lengths alone is only necessity; actual proposition earns sufficiency. |
| 4.prose.64a6925ce0804f51.1 | navigation: Conjugacy classes section. | Entire proof including centralizer bijection/denominator read. | No future character-table classification used. |
| 4.think.1 | discovery-mathematics: Seven partitions of 5 give S5 classes; even ones total 60. | Types 1^5,2 1^3,2^2 1,3 1^2,3 2,4 1,5; counts 1,10,15,20,20,30,24 from n!/z. | B enumerate all 120 permutations by point cycles; even totals 1+15+20+24=60. A5 splitting not assumed yet. |
| 4.prose.8c12b55edf7c8872.1 | numerical-mathematics: 5-cycles count24; double transpositions count15. | z5=5 gives120/5; z_(2,2,1)=2^2*2!=8 gives120/8. | B choose fixed point 5 ways then pair remaining 4 in3 ways; arrange cyclic order on five in4!=24 ways. |
| 4.figure.fig:fifteen | figure-mathematics: Actual swapped board, checkerboard, seven S5 bars/types/labels and even/odd legend. | All 15 tile labels/16 fills read; positions14/15 hold15/14, blank16 white. Seven classes recomputed; bar heights are counts*3.4/30 rounded to .01, correct inks and legends. | B direct enumeration of120 permutations, actual source parser checks all seven heights/counts/inks and all15 positions. Caption explains a legal slide, not an arbitrary allowed swap. Only historical source comment changed; no visual approval from source/hash. |
| 4.prose.d59ac3b7e85aa2c0.1 | story: From classification by renaming to constructive generators. | Full adjacent-swap termination and paired-transposition-to-3-cycle proof read. | Classification and generation are distinct tasks, correctly sequenced. |
| 4.prose.afcfee6c81d58b46.1 | navigation: Generators section. | Both S_n and A_n generation arguments read, including overlapping/disjoint transposition products. | No simplicity used to earn 3-cycle generation. |
| 4.prose.1628d9882418d0af.1 | story-mathematics: Legal puzzle slides are restricted transpositions; blank colour supplies another invariant. | Adjacent-cell restriction matters; checkerboard gives one sign reversal per legal move. | No converse inferred from parity alone: full following proof constructs the reachable subgroup. |
| 4.prose.edc8b6bbdaf3e5db.1 | navigation: 15-puzzle section. | Full necessity and constructive sufficiency proof reread. | Optional historical sources do not replace the proof. |
| 4.prose.180e511907531852.1 | definition-model: 4x4 positions are bijections labels->cells; blank label16, solved identity. | A slide exchanging cells u,v sends sigma to (u v)sigma, so sign reverses. Manhattan adjacency changes row+column parity. | B alternative inverse position map composes on right but has same sign; no left/right convention inconsistency. Blank on white cell16. |
| 4.think.2 | discovery-mathematics: What reverses with arrangement parity at each move? | Blank colour sign delta reverses, hence epsilon(sigma)*delta unchanged. | Both moves from corner and interior obey same rule; no accidental count of allowed directions. |
| 4.remark.1 | history: 1879 Johnson/Story analyses precede1880 craze; distinguish Loyd invention claim from1896 prize offer. | Actual JSTOR journal metadata and Archer original opening/history read; actual Slocum/Sonneveld book text pp109-110/86 discussion separates December1879 manufacturing,1880 craze, January1896 advertised shared prize. | Archer repeats outdated Loyd attribution. Corrected wording no longer implies Loyd never advertised any prize; no own inspection of patent records or original1896 newspaper claimed. |
| 4.prose.63f984d1b09e4bc8.1 | story-mathematics: Sign kernel leads from parity to An simplicity and equations. | An kernel earlier C2; named simplicity below supplies structure before later use. | Future quintic connection is outlook, not a premise. |
| 4.prose.b0c5dafae4e046c0.1 | navigation: Simple groups section. | Abelian classification, split lemma, A5 and uniform An proof read. | Nontriviality in definition retained. |
| 4.prose.0209c7199ec93f05.1 | unnamed-mathematics: Simple nontrivial abelian groups exactly Cp; A5 nonabelian, minimal order postponed. | Every subgroup normal in abelian G; for x!=e, <x>=G; finite composite cyclic has proper subgroup, infinite cyclic has 2Z, prime cyclic has none by Lagrange. | B trivial group excluded, no finiteness assumed in abelian classification. A5 noncentral class size>1 proves nonabelian. Minimum60 explicitly outlook to later proved Sylow argument, not used here. |
| 4.prose.b9b29de73a758fe5.1 | unnamed-mathematics: A normal subgroup must be class union, but arbitrary class union need not be subgroup. | Normality closes each entire conjugacy orbit. A5 proper nontrivial candidate class sums fail divisibility60 before closure is tested. | B identity plus15 doubles has16 elements, cannot be subgroup of60. Class-union condition is necessary only; no converse claimed. |
| 4.think.3 | discovery-definition: Commutator tau sigma tau^-1 sigma^-1 lies in N for N normal in An and tau in An. | Conjugate of sigma belongs to N and sigma^-1 belongs to N, so their product belongs; choose small support to shrink motion. | Restrict tau to actual ambient An; arbitrary element of larger S_n is not justified by An-normality. Replaced unsupported why-cannot question by honest workload question; not asserting class-count methods universally fail. |
| 4.prose.9ffe5c08d67142ba.1 | unnamed-mathematics: Small-degree exceptions: A1,A2 trivial; A3=C3 simple; A4 contains proper normal V4. | |An|=n!/2 for n>=2. Three 3-cycles including identity make A3. Three distinct doubles square to identity; displayed product is third, relabelling earns the other products; inverses give commutation. Conjugation renames doubles. | B exhaustive A4 multiplication/conjugation checks all4 V elements, |V|4<12. Fifth point used in BOTH parity repair and double-transposition case, now explicit. Full quotient exercise remains two stars and unchanged. |
| 4.beauty.1 | outlook-history-mathematics: Later solvability/quintic; random transpositions with holding and ~n log n/2 cutoff; external CFSG/Monster. | Actual C5/C10 proof routes already reconstructed. Primary Diaconis-Shahshahani pp159-160 define independent choices including probability1/n of no change and state both bounds. Actual V11 shuffling law92-99/theorem157-162/corollary205-219 located and read; no future result supplies C4 premise. | Distinct-only model remains in one parity class, so cannot tend to uniform on all permutations. Primary Aschbacher excerpt via MacTutor and AMS2004 quasithin metadata corroborate gap history, not own CFSG proof audit. Actual ATLAS Monster order8.08017...e53 read and exact factorization independently multiplied. Lie-type/sporadic terms explicitly external outlook only. |
| 4.prose.1e4ccc9ccba9038d.1 | navigation: Exercises section. | All ten prompts, including every advanced target, read with hints and complete answers. | No new blind-solving claim; CH04-PROMPT-FIRST chronology remains. |
| 4.reminder.1 | local-mathematics-definition: Odd-prime cyclotomic field Q(zeta), Phi_p, reduced expressions, inverses and sigma_a. | Actual V1 polynomial division/Bezout prop:polynomial-bezout127-132 and ex:eisen(b)678-685 read, plus Eisenstein proof327-338. Add explicit Phi_p=1+...+X^(p-1), identity. Irreducibility forces any vanishing remainder zero by Bezout; coprime P gives inverse; exponent b inverse modp gives sigma_a inverse. | B evaluate all relations, not merely a chosen expression; zeta^a primitive for p notdiva, allroots Phi. Every field containing Q,zeta contains polynomials, so locally constructed field is smallest. Char0, oddp; no later extensions/Galois premise. Actual earlier label is ex:eisen, not an inferred exercise title. |
| 4.prose.ebb49cd8ff7d0835.1 | navigation: Hints section. | All ten actual hints compared again with targets/solutions, including primitive-root/Legendre and finite series routes. | No hint uses future Sylow, Galois correspondence or measure convergence as essential premise. |
| 4.prose.dcbf900256c28752.1 | navigation: Solutions section. | All ten complete ideas/writeups reread, including Landau budget, cube facet invariants, shuffle orders, split criterion, discriminant and convergent product/lower bound. | Two changed full triples explicitly reopened/reconstructed below; other eight hashes unchanged. Quoted cube count remains nonessential outlook, not an earned converse. |
| 4.prose.f37e13469cdf77e3.1 | navigation: Sources and further reading. | All twelve actual entries manually checked with access bounds below. | No citation substitutes for local proof. |
| 4.prose.16e29cf939731ade.1 | bibliography-container: Twelve child entries, five added. | Metadata/text evidence separately keyed below. | Intentional container/child overlap, not twelve extra uninspected sources. |
| 4.bibliography.1 | bibliography-history: Johnson/Story, AJM2(1879)397-404. | Actual JSTOR item DOI10.2307/2369492 names both authors, issue4/December1879/pages397-404. Archer original pp793-794 explicitly distinguishes Johnson necessity from Story sufficiency. | Original1879 complete paper/scan not accessible/read here; historical priority corroborated by original1999 discussion and trusted journal record, not claimed own referee audit. |
| 4.bibliography.2 | bibliography-history: Archer, Monthly106(1999)793-799. | Actual archived original PDF header, opening, generator theorem and graph discussion read; author Google Research bibliography agrees. | False all-rectangular description narrowed to actual4x4 proof and graph discussion. Independent1x4 counterexample has4 reachable states, not12. Historical opening explicitly flagged as outdated. |
| 4.bibliography.3 | bibliography-history: Slocum/Sonneveld, The15Puzzle,2006. | Actual author-foundation flyer2006, actual book text pp109-110, and IU catalog2006/SlocumPuzzleFoundation metadata read. | Read relevant text, not entire144-page history or underlying patent/newspaper archive. Prize1896 is distinct from invention/craze1880; bibliographic author Dic is D., not Dick. |
| 4.bibliography.4 | bibliography-history: Joyner, Adventures in Group Theory2ed,JHU2008. | Actual publisher2008 record and full TOC already read in C2; legal cube configurations Ch11 and illegal Ch9 support bounded content description. | No entire book or legal-state sufficiency proof newly certified. Cube-group order is explicitly external quoted outlook in exercise; Rokicki/cube20 primary count corroboration, not redoing exhaustive search. |
| 4.bibliography.5 | bibliography-history: Rokicki/Kociemba/Davidson/Dethridge,SIAMJDiscreteMath27(2013)1082-1105. | Actual primary author cube20.org account and SIAM DOI10.1137/120867366 previously read in C1; face-turn metric includes quarter/half turns. | Do not confuse20 face turns with quarter-turn metric or claim reproducing computational diameter proof; no new research abstract certificate. |
| 4.bibliography.6 | bibliography-history: Diaconis/Graham/Kantor,AdvApplMath4(1983)175-196. | Actual author-hosted full original PDF first page, main even-deck theorem and Lemma1/order proof pp175-178 read. | Scope deck2n, not every unspecified odd deck convention; bibliography corrected. Original section3 discusses odd sizes separately. Full classification proof not needed or certified here. |
| 4.bibliography.7 | bibliography-history: Dummit/Foote3ed,Wiley2004sections3.5/4.6. | Actual Wiley/VCH TOC read:3.5 Transpositions and Alternating Group,4.6 Simplicity of An. Author Foote2004 metadata distinguished from publisher2003 release earlier. | No entire textbook or inaccessible author sample proof newly read; manuscript proofs independently reconstructed. |
| 4.bibliography.8 | bibliography-history: Diaconis/Shahshahani,ZW57(1981)159-179. | Actual primary journal PDF pp159-160, probability law and both main theorem statements read beyond abstract; exact independent-pick holding convention. Stanford1980 technical report is separate from1981 journal date. | Not claiming entire external representation-theoretic mixing proof was independently audited; V3 mention is explicit outlook. |
| 4.bibliography.9 | bibliography-history: Aschbacher,NoticesAMS51(2004)736-740. | Actual Caltech author-repository metadata read; actual participant article excerpt reproduced by MacTutor discusses proof gaps and closure; AMS2004 quasithin publication metadata read. | Original AMS PDF403, Caltech signed download inaccessible; no claim original full five pages or classification proof read. Four-family classification corroborated by specialist source/ATLAS, not proved locally or invoked. |
| 4.bibliography.10 | bibliography-history: Nicolas,On Landaus Function,in Mathematics of Paul ErdosI,2ed,Springer2013pp207-220. | Actual author survey intro/full statement and bibliography text read; publisher-deposited Crossref DOI10.1007/978-1-4614-7258-2_14 confirms title/book/year/author/pages. | Original1903 paper not read; exact1903 incidental date removed, asymptotic retained explicitly beyond finite task. No survey new-research proof certification from abstract. |
| 4.bibliography.11 | bibliography-history: Zolotareff,Nouvellesannales2ndseries11(1872)354-362. | Actual Numdam original PDF header and TheoremI/proof pp354-355 read: parity of nonzero multiplication equals Legendre symbol using primitive root. | Original uses nonzero residues; adding fixed0 leaves sign unchanged. Retain original printed name. Own full problem proof independently reconstructed, no dependence on reciprocity or remainder of paper. |
| 4.bibliography.12 | bibliography-history: Blackburn/Britnell/Wildon,JLMS86(2012)755-778. | Actual arxiv1108.1784v2 full text intro/theorem1.5 and section9 lower/upper conclusions read, page5 image opened; publisher Crossref DOI10.1112/jlms/jds022 confirms metadata. | Preprint theorem1.5/section9 recall mistakenly write sum from1; actual proofs sum from0 and constant4.2634035 includes P0=1. Disclose that inconsistency rather than importing it. Manuscript lower bound/product independent, matching asymptotic only attributed outlook; not certifying whole external proof. |


Every row above is a specific manual decision; inventory/checker scripts do not
assign approval. Source hashes/coordinates remain in exposition.json and reopen
after change. Included figure-source identity is separately guarded. Diagram
math/source inspection is not page or EPUB viewport approval. Final rendering,
global later-use closure and all remaining chapters/appendices are pending.

## Two reopened full exercise triples

### ex:landau

Domain: Permutations of7 or10 letters; identity/fixed-point padding allowed.

Claim: Largest orders12 and30, attained by types4+3 and5+3+2.

A: Order is lcm. Assign each maximal required prime power to a supporting cycle; pairwise coprime factors have sum<=product, so their total cost<=n. Conversely disjoint cycles with those distinct-prime powers achieve that product. For7 mixed options2+3,2+5,4+3 give6,10,12 and single powers<=7. For10 largestprime7 leaves3 (<=21),5 leaves5 (2+3 gives30), only2/3 gives<=12. Exhibits achieve maxima.

B: B recursive enumeration of all integer partitions gives maximum lcm12/30; reconstruct prime-power reduction with an empty set for identity and one factor equality. For10 single8 or9 cannot combine with3 or2; no missed repeated prime power can improve lcm. Full mathematical solution unchanged; only attributed asymptotic outlook clarified.

Comparison/grade: Two stars retained: prime-power budget transformation plus a finite search. No future PNT/Landau asymptotic is needed. Removed unsupported exact1903 incidental date; retained stronger asymptotic as externally attributed outlook, with Nicolas actual text/metadata.

### pb:conjugate

Domain: Independent uniform sigma,tau in finite S_n, n>=0; S0 one empty permutation, P0=1. Real nonnegative sequences for local liminf; finite real L in epsilon equivalence.

Claim: Sum Pn=positive product C,4.263401<C<4.263406; liminf n²Pn>=C. Matching asymptotic only outlook.

A: Cycle-type count n!/z gives Pn=sum1/z². Finite positive partition subsums exhaust product and series identically; Fj between1+j^-2 andexp(j^-2) by actual V1 Taylor-exponential series, so increasing products bounded and converge. Log inequalities by derivatives, integral tails1/(J+1)-1/(6J³)..1/J, finite12-term sums/ratio tails throughJ1000 give enclosure. Adding a unique(n-k)-cycle for k<n/2 yields Pn>=sum Pk/(n-k)² and n²Pn>=partialsum Pk->C. New tail-infimum definition and both epsilon implications follow V1 completeness.

B: B reconstruct without interchanging signed sums or appealing to measure theory: any finite list of partitions lies in some length/product truncation, every truncation term appears in finite total-size sum. Empty partition supplies P0=1. Long-cycle injection is disjoint across k because unique cycle>n/2 identifies remainder. For any epsilon choose a fixed finite partialsum>C-epsilon and then n>2K; all later n²Pn>C-epsilon. This directly proves liminf bound without existence of a limit. Exact outward45-digit J1000/m12 interval rechecked; P1=1,P2=1/2. Primary preprint begins its A sum at1 but section9 proof and quoted4.2634035 include0; manuscript retains correct own derivation.

Comparison/grade: Three stars retained: positive infinite product, quantitative tails and long-cycle lower-bound discovery. Added missing liminf definition with proof before prompt, all targets/full hint/idea/writeup retained. Cited actual external asymptotic text; no new certification of that full research proof.

The original CH04-PROMPT-FIRST chronology remains; this is a fresh full recheck
after source changes, not another blinded first solve. All nine named proof
records and the other eight triples retain identical accepted source content.
