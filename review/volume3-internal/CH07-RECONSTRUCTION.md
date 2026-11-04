# V3-008 — exercise reconstruction and exposure

Entire C7 main argument and all prompts/hints/solutions read. A source chunk
crossed the Hints boundary: all hints and the first supplied solution were shown
before this permanent reconstruction. Later chunks showed the remaining supplied
solutions. No blinded or documented prompt-first claim is made for C7. The
Kronecker general proof and elementary repair were freshly derived in reviewer
reasoning before that supplied solution was displayed, but the permanent record
is later. It is now a C10 problem after ex:phin, with all parts preserved.

Fresh reconstructions and independent methods, now recorded for A/B comparison:
- ab360: 2-primary partitions3,[2,1],[1,1,1],3-primary[2],[1,1],5-primary[1].
  Six invariant lists360;(3,120);(2,180);(6,60);(2,2,90);(2,6,30). Each prime
  exponent multiset can be recovered from element orders/annihilation counts,
  checking distinctness beyond order/product. Table matches all6.
- smithcalc: det-20,gcdentries2 gives2,10. Independently take presentation
  combinations: replace secondrelation bysecond-first gives2x-2y=0; setu=x-y,
  vy, then2u=0 and4u+10v=0 reduces10v0, givingC2+C10. Direct row/column steps
  agree. One star.
- unitsmodn: induction onj bysquaring gives t_(j+1)=t_j+2^(j+1)t_j²odd;
  exact valuationj+2. Order5mod2^k is2^(k-2), no smaller2power, withk3base2.
  5powers lie1mod4, -1lies3; disjointcyclicsubgroupsgiveall2^(k-1)units.
  CRT8,9,5 givesC2²×C6×C4=C2³×C12,exp12; all96units checked independently.
  General odd-prime-power theorem unnecessary: list powers2mod9/5 locally.
- similarQ: a Smith form overK[X] remainsvalid overL[X], includingpolynomial
  inverses and divisibility; monicnormalizationuniquenessforcesidenticalfactors.
  Independently minors' ideal(d) equality has two containments preserved by
  extension: allminors multiplesd and aK[X]linearcombinationequalsd. Thus same
  determinantaldivisors overL, no newgcd canappear. Handlesfinitefields too,
  unlike an infinite-field determinant-specialization argument. Two stars.
- nilpotent: eachinvariantfactor dividesX^m hencepowerX, exponentspartitionn.
  Converselyshiftblocksrealizeallpartitions. Kernelcounts h_k=summin(k,a),
  differencescountsblocks>=k,second differencesexactk. n4fivepartitions kernel
  rows1,2,3,4;2,3,4,4;2,4,4,4;3,4,4,4;4,4,4,4. n0emptytype,zerooperator,
  allkernels0. Alternative constructchainbasesfromsuccessivekernelfiltration,
  corroboratingcounts. Two stars.
- diagonalisable: diagonal=>minimalproductdistincteigenvalues. ConverselyCRT
  Lagrangeprojections e_i(A) haveimagesineigenspaces andsumI, pairwiseproducts0,
  givingdirectsum. Independent V1distinct-root annihilator argument reconstructs
  sameprojections. A²AusesX(X-1), rootsdistinctinanycharacteristic; A^kIoverC
  useskX^(k-1)nonzeroatnonzeroroot. Incharp dividingk thisfails,e.gnonzero
  nilpotentshiftN²0 with(I+N)^pI,notdiagonalizable. n0mu1emptyproduct. Two stars.
- cyclicvector: n>=1, degproduct=n andlargestfactor equalsproduct iffexactly
  onepositive-degreefactor. Generator1basisgivesv,Av,...; converselythatbasis
  makesmatrixcompanion; companionmoduleonefactorprovespolyequality. Independent
  annihilatorofv hasdegreeatleastn bybasisindependence, hencedegreeexactlyn by
  expressingA^nv, andkillswholebasis bycommutation; min=chi. n0previousiff r1
  fails, nowhandledseparatelyemptybasis,C(1),mu=chi1. Two stars.
- sublattices: second-coordinateimagecZ,c>0becauseindexfinite. HorizontalpartaZ
  hasa>0since quotientorder n annihilates(1,0). Pick(b,c),reducebmoda; remove
  secondcoordinatefromanyvector,uniquea,b,c. Indexac eitherdeterminantorunique
  residuesxmoda,ymodcusingtriangularreduction. Thus sum_(a|n)a, n1onlyZ².
  Discoveryneedsbothprojections/nonzerocases;3stars.
- relocatedKronecker: powersofintegercompanionhaveintegercharpolynomials with
  rootsalpha_i^r (complexJordanuppertriangularpowers earns multiplicities).
  Coefficientsboundedbybinomial(d,j), finiteintegerpossibilities; unionfinite
  rootsetscontainsallpowersofeachnonzeroalpha, so repetitionforcesrootunity.
  Independent matchingmethod: equalpowerpolynomialsmatchrootsbypermutation;
  iterationonacycle givesalpha^(r^l-s^l)=1. IrreducibleidentificationPhi_m now
  follows actualearlierex:phin inC10, notfutureC10fromC7. Partb Z^dP(Z+1/Z)
  monicconstant1rootsonthecircle, endpoints±2 repeated±1harmless. Partc g5X²−6X+5
  primitive; ifz^N1,realrationalremainderdividingbyghasdegree<=1andvanishesat
  nonrealz,sozero. Gaussdescendsg|X^N−1toZ,leadingcoefficient5cannotdivide1.
  No lateralgebraic-integerclosureused. Allpartsretained; C10 full prerequisite
  proof-location/argument check is stillpending the full C8–10 pass.
