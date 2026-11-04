# Chapter 5 prompt-first reconstruction, V3-006

Eight prompts read before their supplied hints/solutions. Main prose and all
Sylow/solvability proofs have been read. Internal AI reconstruction.

- ex:sylowS4: n3=4, four cyclic groups from eight3cycles. n2=3: the preimages
  of the three order2 subgroups under S4->S3 acting on pair partitions have
  order8; each is a square's D4. They are distinct and all Sylows by conjugacy.
  Also normalizer of one square D4 is itself, givingindex3.
- ex:order45: n5divides9 andis1mod5 gives1; n3divides5 andis1mod3 gives1.
  Normal Sylows orders5/9 commute with trivial intersection, so direct product.
  Order9 classification yieldsC45 orC15xC3, both abelian.
- ex:nosimple: order56 has n7=1or8. Insecondcase, eight prime-order subgroups
  contribute48 nonidentity elements oforder7; remaining8 (includingidentity)
  are exactly any Sylow2subgroup, making itunique andnormal. order200 n5=1
  because divisors8 give no other1mod5. order36 n3=1or4; at4 conjugation action
  G->S4 nontrivial. Simplicity would forcekerneltrivial, impossible36>24.
- ex:S5sub: anorder15 subgroupwouldbecyclic bypqtheorem (3notdivide4), hence
  containorder15 element; that would need disjoint cycles costingatleast3+5>5.
  Order30/40 subgroups haveindex4/3. Their coset-action kernel lies insideH;
  normal-subgroup classification ofS5 excludesA5 bysize60 andwholeG by
  nontransitivity, so the kernel is trivial; injection120 into24/6 impossible.
- ex:normalizer: ifg normalizesM=N_G(P), then gPg^-1 is a SylowofM. P is
  normal inM, hence itsuniqueSylow, so gPg^-1=P andg inM. Converseautomatic.
  IncludesP={e},M=G.
- ex:derived: a solvablechain lengthr forcesG^(i)<=G_(r-i), since anabelian
  quotient kills commutators and derived subgroup respects inclusion. Conversely
  reversing a derivedseries reachingE givesa subnormalchain withabelianquotients.
  S4->A4->V4->E; S5->A5->A5... . Sign givesupperbounds; [(12),(23)] a3cycle
  andconjugation generateAn. InA4, [(123),(124)]=(12)(34); conjugation cycles
  allthree doubletranspositions, soA4'=V4. A5' nontrivialnormal in simpleA5,
  henceA5. This distinguishes perfect from merelysimple/solvable.
- ex:sylowGL2: |GL2|=p(p-1)^2(p+1) hasp-partp. U={I+xE12} isadditiveorderp.
  ItscommonfixedspaceL=span(e1); normalizers preserveL andhenceareuppertriangular.
  Conversely uppertriangularg sendsu_x tou_(a/d)x, so B normalizesU. |B|=p(p-1)^2
  givesp+1 conjugates, onefor eachline. TheyareNOTfull linestabilizers: B is.
  EachU_L acts triviallyonL andonV/L, withim(A-I)<=L andker(A-I)>=L. p2works.
- ex:order12: n3=1or4. If4, the conjugation action onfour Sylow3subgroups has
  stabilizeroforder3, hencekerneldividing3. Kernelorder3 wouldbeoneSylowand
  normal, contradictingn3=4; thus faithful embedding intoS4, imageorder12/index2.
  Any index2subgroup ofS4 contains all3cycles (theirimages inC2 trivial), hence
  containsA4 andequalsit. Alternatively count8 order3elements leavingunique
  Sylow2Poforder4; P cannotbeC4 because AutC4 order2 forces theC3actiontrivial,
  sonormalP=V4 andnontrivial3cycleaction givesA4.
  Ifn3=1, Q=C3normal andG=Q semidirectP, P order4=C4orV4. Actions map into
  AutC3=C2. Trivialactions giveC12 andC6xC2. C4nontrivialaction givesC3 semidirect
  C4 (invertinggenerator), unique. V4nontrivialaction haskernelC2 andsplit
  complementC2, givingD3xC2=D6: ifa order3,bcentralorder2,c invertsa, thenab
  order6 andc invertsab. Allnontrivialactions equivalentby changingbasis/generator.
  Distinguishfive: A4 alonehasn3=4; twoabelianones separatedbyorder4; D6 noorder4,
  whileC3 semidirectC4 hasorder4. Thus complete and pairwisenonisomorphic.
