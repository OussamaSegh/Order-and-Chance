# V3-008 — module structure, Smith termination and canonical forms

Entire Chapter7 read, all prompts/hints/solutions and both actual tables/Smith
figure. Exposure limits and fresh solution reconstructions are recorded in
CH07-RECONSTRUCTION.md; no documented blinded-solution claim. Internal AI A/B
review. Bibliography attribution, topology outlook and final rendering remain
separate. The complete Kronecker triple moves to C10 after ex:phin, retaining all
three parts; its new mathematical sign-off remains pending the C8–10 route audit.

| Key | Exact hypotheses/domain and claim | Reconstruction A | Adversarial B and boundaries |
| --- | --- | --- | --- |
| thm:normindex | Nonzero z=a+bi inZ[i],d=gcd(a,b)>0; quotientadditiveC_d+C_(N/d),indexN | Bezout primitive(a',b') gives integer Udet1; UTfirstcolumn(d,0),toprightdt,bottomrightd(a'²+b'²); subtracttfirstcolumn todiagonal. Rowbasisiso/columnimageequality preserve quotient; countdiagonalresidues | Independently geometryfundamentalcellof multiplicationmatrix T hasareadetT=a²+b², and its minorsgcd d/determinant reconstructsameSmithfactors aftergeneraltheorem isearned. DirectalgebraicfirstproofdoesnotuseSmithasfuturepremise; addedexplicitintegerUinverse. Unitsz±1/±i yieldtrivialquotient; a0or b0 handledbecausegcdpositive; z0explicitlyexcluded,indexinfinite there. |
| thm:smith | PIDR, m,n>=0; A equivalent underGL to nonzero divisibilitychain+zeros, uniqueunits/minors | A nondividingentryb givesBezoutpivotd=ua+vb via2rowdet1 matrix. Properdivisor strictlyreducesirreducible-factorcount lambda(a), earnedPID=>UFD. Finitecleanupclearsfirstrow/col; offendinglowerblockentrybroughtupforcesanotherstrictreduction. Recurseblock keepingd1divisibility. Minoridealsinvariantunderinvertiblelinearrow/columnexpansion; diagonalminorsgcdproduct | Separateterminationargument: everyproperpivotreplacement strictlyenlargesprincipalideal, impossibleinPIDbyuniongeneratorACCprovedC6. NoEuclideannorm assumed. InvariancehandlesBezout2rowchange,notonlyelementaryadditions: multilinearity,repeatedoldrowsvanish,theninversegivesreverseidealcontainment. r0/m0/n0 allowed,Delta0=1; nonzero-productformulaonly1<=k<=r,largerminors0,neverdividebyzero. SourceSmitharrowsandallminorordersindependentlycomputed2,12,144. |
| lem:subfree | PIDR, finite n>=0,LsubmoduleR^n; freebasisrank<=n | Inductlastcoordinateimageideal(a); kernelL0submoduleR^(n-1). a0=>L=L0; otherwisechoosevcoord a. Everyx=x0+rv; sa0forces s0, henceL=L0directsumRv andappendbasis | Independentlychoosefirstnonzero-coordinateprojectioninstead; splitonto(a) viaa->v,well-defined/injectivebecauseadomain, obtainingfreeextensionwithoutassumingLfinitegenerated. n0zero, L0zeroideal,fieldcaseandZsubgroupsallwork. EssentialPID propertyisprincipalimageideal,notvector-spaceGaussianeliminationordivisionbyarbitraryringelement. |
| thm:structure | FinitelygeneratedM overcommutativePID; unique finitefreepart andnonzero-nonunitdivisibilityinvariantfactors | PresentR^nontoM; kernelfreefinitebyLemma,Smithrelationmatrixgivesquotientdiagonal. Torsionsubmoduleintrinsic, M/Tfreefixess. Filtrationp^kT/p^(k+1)ToverfieldR/p hasdimensioncount exponents>k. Recoverr=maxdimT/pT,sort/padleftthenmultiplyprimepowers | SeparateCRTchecksplit eachdintoitsprimepowercyclicfactors; onR/p^v,kthlayeroneR/puntilvthenzero. Thisagreeswithdirectidealcalculation(p^k,d),usingBezoutwhenk>=v; nofinitecardinalityofR/p assumed. Addedtorsionclosure(abkillsx+y),quotientscalarwell-definednessandexactkernelcalculation. T0/r0andRfieldhandledexplicitly; freepartcanbeoverinfiniteR, noelementcountargument. No uniquenessinferredonlyfromonechosenpresentation. |
| cor:abelian | Any finitelygeneratedabeliangroup; uniqueZfree/invariant/primepowerforms; n>=1 finitecountproductpartition(a_p) | ForcedZmodule, PIDstructure; integerCRTsplitcyclicfactors. Right-alignorderedprimeexponentsrecoversinvariantchain. Finitegroupfreeparts0; partitionsofeachvaluationindependent | Independentinvariant: numbersofelementskilledbyp^k inprimarypart equalp^(summin(k,a_i)); logarithmicdifferencesrecoverpartition, sochoicesreallydistinct. n1emptyproduct1/trivialgroupnowexplicit. Actualsix360rowsandtheirprimeexponents/products/divisibilitychecked; e.g4,2,9 gives2/36. |
| cor:index | Aintegern-square,detA!=0,n>=0; indexAZ^n=absdetA, quotientSmithcyclics | InvertibleintegerP,Q preserve latticequotient; allSmithpivotsnonzeroby nonzerodet. Independentresiduecoordinatesgiveproductabsdiagonal;detP/Q±1preserveabsdet | Independenttriangularlatticefundamental-domaincount, consistentwith2DnormexampleandlaterHermiteexercise. n0emptylatticequotientsingleton,emptydet1,product1. Singularmatrixexcluded; itgivesfreequotientpart/infiniteindex,notzeroindex. Negativepivotsabsvalues; unitpivotscontributetrivialfactors. |
| prop:presentation | AnyfieldK,A inM_n(K),n>=0; V_A=K[X]^n/(XI-A)image andSmithpositive-degreefactors multiplychi | Evaluationofpolynomialvectorssurjective; columnrelationsXe_j=sum_i aij e_i killed. Repeateddegree-reductiongivesconstantrepresentativec; ifkernel, c=phi(c)0soimageequalskernel. det(XI-A)monicdegreen,nonzero,givesnnonzeropivotsandmonicnormalizationproductchi | Differentexplicitreductionidentityforvectorv: X^kv-A^kv=(XI-A)sum_(j=0)^(k-1)X^(k-1-j)A^jv; telescopingearnsallrelationswithoutassumingCayleyHamilton. Constantremainderevaluationisunique,so noillegalmatrixsubstitutioninadjugateargument. n0allmapszero,chi1,emptyproduct1; arbitrarypositivecharandnonsplittingKallowed. |
| thm:frobenius | FieldK,n>=0; rationalcompanionblockform uniqueinvariantfactors,mu=lastfactorforn>=1,chi=product; n0both1 | CyclicK[X]/dhasbasis1..X^(m-1); multiplicationXgivescompanionlastcolumn. Joinbasesunderpresentation. ModuleisomorphismifflinearintertwiningSA=BS; structureuniquenessclassifiessimilarity. Annihilatorintersectionof(d_i)=(d_r) | Independentcyclicvectorcalculationg(C(d))1=gmodd,so annihilator(d), then directsumlcm=lastfactor. Companioncharpolycheckedbase m1andfirst-rowcofactorinductionm>=2withbothsigns; noCayleyHamiltonusedtoobtainpresentation. Minimalpolynomialdefinedlocallyasmonicgeneratorofnonzeroannihilatoridealbeforeinvocation. Originalr0last-factorformulaundefined: nowfullzero-dimensionalcaseearned,notcertifiedunderoldformula. C(1)emptyconventionexplicit. |
| cor:cayleyhamilton | AnyfieldK,n>=0; chi(A)0,mu divideschi,sameirreduciblefactors | Rationalfactorschain givesmu=lastdividingproductchi; evaluateproductatA. Primeirreduciblesdividingproductdivideonefactorhencelast. n0chi=mu1andeveryevaluationzeroonzerospace | Independentdirectcyclicsummands: eachd_i divideschi,sochi annihilateseverysummand; irreduciblesetunionofnestedfactorsequalslastset. No own-theorem premise. Positivecharacteristic/repeatedrootsallowed; illustrative3x3uppertriangularmatrixshownexplicitlysoJordanblocknotationisnotinvokedbeforedefinition. |
| thm:jordan | FieldK,chi splitsinK; Jordanblocksuniqueuptoreordering,positiveprimeexponentsgiveblocks | Factorinvariantd_i intolinearpowers; CRTsplitscyclicmodules; basisy^(e-1)..1 givesupper-superdiagonalones. Allbasischoicesproducekernelh_k=summin(k,e); differencescountblocks>=k,second differencesexactk | IndependentlyderiveexponentsfromPIDprimefiltrationsforp=X-lambda; equivalentcountsfromkernelpowersreconstructsizes. Other-eigenvalueblocksareinvertibleafter subtractlambdaI,so contribute0. NoalgebraicclosureassumedunlessK=C; actualV1d'AlembertproofreadforC assertion. n0emptyblocks,arbitrarychar/repeatedrootsinclchar2valid. Splittingessential: realrotationwithchiX²+1 hasnoJordanformoverR. |

| Key | Reconstruction A / answer | Adversarial B, prerequisites and grade |
| --- | --- | --- |
| ex:ab360 | Sixinvariantlists360;(3,120);(2,180);(6,60);(2,2,90);(2,6,30) | Primeexponentpartitionsandannihilationcountsindependentlydistinguishallrows. Actualtableparsed/checkedeachproduct360,adjacentdivisibilityandmatchedprimepowers. Completehint/idea/writeup,one star. |
| ex:smithcalc | C2+C10,gcdentries2,det-20 | Independentgeneratorchangeu=x-y andrelationdifference2u0,remaining4u+10y0=>10y0; agreeswithfouractualrow/columnsteps. Index20,notnegative20;one star. |
| ex:unitsmodn | 5order2^(k-2)mod2^k,k>=3;unitsC2×C2^(k-2). Mod360,C2³×C12,leastuniversalexponent12 | Exactvaluationinductionanddisjoint±5powersgivegeneration; enumerateactualunitsupto2^13andall96units360/exponent12. ReplacedstaleV2Chapter4hintandunneededoddprime-powerappealbyexplicitpowers2mod9/5. k3boundary,powerj0anduniqueexpminimalityearned;two stars. |
| ex:similarQ | SimilarityoverfieldextensionLdescendstoKforKmatrices | Smithmatrices/inversesalreadyoverK[X],stillinvertibleoverL[X]. IndependentdeterminantalidealcontainmentswithBezoutcombinationpreservegcdsafterextension,so samefactorchain. Worksfinitefields/inseparableextensionswithoutdeterminantgeneric-pointassumption. Two stars. |
| ex:nilpotent | Similarityclassespartitionsn,readh_kdifferences; n4fivekernelrowsinreconstructionrecord | Independentexplicitshiftmatricesforpartitionsn0..7andkernelscomputedbyGaussianeliminationchar2/3/5recoverexactparts. n0emptypartition;N0hasnblocks1,notoneblockn. Hint/solutioncomplete,two stars. |
| ex:diagonalisable | iffmu productdistinctKlinears; idempotentsallfields,finiteorderoverC | ReconstructLagrangeCRTprojectionsanddirectsum, independentlydiagonalentriesannihilator. Needlinear-splittingaswellassquarefree: irreduciblerealquadraticcounterexample. Charpdividingk counterexampleI+Nshowswhycomplexhypothesis matters. mu1/n0emptyeigenbasisvalid. Two stars. |
| ex:cyclicvector | mu=chi iffcyclicbasisv..A^(n-1)v iffcompanion | Independentlyannihilatorofcyclicvhasdegree>=nbybasisindependence,anddegree<=nbyA^nvexpression,killswholebasisbycommuting. n0oldr1argumentfalse;sourcehandlesemptybasis/C(1)/mu=chi1separately. Companionminimal/charproofdoesnotuseexerciseitself. Two stars. |
| ex:sublattices | Uniquea,c>=1,bresidue0..a-1,indexac=n;countsumdivisorsa | Secondrouteuniquequotientrepresentativesxmoda,ymodcaftertriangularreductiongiveindexwithoutdetformula. npositive/indexfiniteensuresc/a nonzero; quotientLagrangegivesn(1,0)inL. RemovedunnecessaryfutureVolume13hint,earlierlem:subfreeearnsroute. Three stars. |

Unnamed route: module scalar quotient well-definedness now explicit, polynomial
P(A) action laws follow products of powers of a single A, and stable subspaces
are precisely submodules because X acts as A. Finite direct sums/internal unique
sums are defined before their first use in the Gaussian quotient. Finite basis
rank proof extends actual inverse matrices to the locally constructed fraction
field; it does not purport to prove arbitrary infinite cardinal rank. Torsion
closure and finite layer scalar actions now earned. All loops in Smith proof
have finite cleanup between strictly decreasing factor counts; the prose no
longer says a generalPID needs division/remainder or a smallest-size pivot.

The complete actual Smithfigure has fivecorrectmatrices/fourcorrectarrows,
Delta1=2,Delta2=12,Delta3=144, quotientC2+C6+C12. Companionfirst-row sign is
(-1)^(m+1) times(-1)^(m-1)=+1 forconstantterm. Dimensioncounts match sumdegreesn.
Actual six360table rows and n4kernel table entries recalculated by independent
methods. Grayscale/final-size/page/digital rendering pending after source change.

Actual V1 thm:dalembert proof read: boundedreal/imaginarysubsequences giveclosed-
disccompactness; modulusdominanceat infinity/globalminimum; firstnonconstant
localtermchoosesrootdirectionandstrictlylowerstheminimum. It suppliescomplex
splitting without invokinglateranalysis. Actual earlierdeterminant/rank proofs,
V2Bezout/CRT and C6Gauss/PID proofsites supplythe rest. Researchmetadata ofall
sixbibliographyitems/topologyoutlook stillpending; no attributed research theorem
is supplying a premise for the algebraic route.

Curricular change: the old C7 Kronecker solution explicitly used C10 cyclotomic
irreducibility and C11 algebraic-integer closure. Complete triple relocated after
ex:phin in C10; c now uses only C6 Gauss and polynomialdivision. Statement, grade,
allparts and complete solutions retained. The location-only update in historical
REWRITTEN_EXERCISES.json preserves rewrite membership, not mathematical approval;
V3-008-curricular-migration.json maps all old/new IDs. Full C10 approval remains
pending; do not transfer the historical rewrite status into fresh evidence.
