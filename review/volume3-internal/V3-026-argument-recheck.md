# V3-026 — changed and new complete arguments

Solo internal AI reconstruction, not human refereeing or formal verification.
All current full proofs read. Exact computation supports general proofs.

## thm:splitunique

Domain: FieldsK,Kprime, isomorphism sigma, nonconstantP; L/Lprime splitting fields. DegreeD finite; at leastone and atmostD extensions, exactlyD iftargetrootsdistinct.

A: StronginductiononD. D1: L=K, sigmaP already splitsKprime soLprime=Kprime. Otherwise choosealpha∉K withirreducibleQdegree d>1. sigmaQ divides sigmaP, hencehas e distincttargetroots,1<=e<=d. Extend1uniquelygives each mapKalpha→Kprimebeta. TreatL/Lprimeas splittingfields overthosebases; degreeD/d<D. Inductiongives1..D/d mapsperbranch, disjointbyimagealpha, total1..eD/d<=D. IfsigmaPdistinct thene=dandallsubbranchesexactD/d. Takingidentitybasegivesautomorphismcount, notusedininduction.

B/boundaries: RebuildasembeddingtreewithbranchfactorboundedbyminimaldegreeandproductdegreesD. Fulltargetsplit ensuresno deadbranch. Anyextensionrestrictstoonefirstrootmap, so countiscomplete, notjustlowerbound. RepeatedPoverdegree1hasexact1; purelyinsepXp-tdegreep has1map,strictinequality. Distinctmonicfactorsinchar0share no root byminimality. Newgrammar separates existencefromupperboundwithoutchangingstatement.

Correction: Reword distinct-root count from awkward at leastone,andatmostd to twocomplete assertions; original full theorem/count retained.

## prop:constrfield

Domain: Finite Euclideanconstructionsfrom0,1; linefromtwodistinctknownpoints, circleknowncentre/distance, isolatedintersectionsofdistinctcurves. Ccal subfieldC, conjugationandbothsquareroots, coordinatesiff.

A: Perpendicularbisectorbytwocirclesthroughoppositeendpoints; perpendicularthroughp usescircleatp throughoneoftwoknownlinepoints, atmostoneistangentfoot; thenbisectoroftwointersections. Twiceperpendiculargivesparallel. Axes/unitcirclegivei, projectionsandcirclelengthtransfergivesignedx,y, converselyvertical/horizontalmeet. Signedlengthaddition/subtraction. Productline1→ib y=b(1-x), parallelthrougha y=b(a-x), imaginterceptiab; quotientlinea→i slope-1/a, parallelthroughb y=(b-x)/a, a!=0. Transferimagcoordinates. Complexproduct/reciprocaldenominatorx²+y²>0 makefield. Positivea:diameter[-1,a]circle yields(0,±sqrt a). Fornonzeroz,realpositivecircleinterceptr=absz isconstructible;u=z/runit, u=-1givesi√r;elsev=(1+u)/abs(1+u), v²uusingu*conju1. Then√r*v squaresz. z0andnegativeotherrootclosedbyfield.

B/boundaries: Independentcoordinateauditallgeometricsteps: centres/radiiallalreadyknown, selectedcirclepositive twointersections evenpinline; noassumptionanunknownperpendicularfootisconstructed. Productb0or a0 landsalreadyknown0, no demandnewintersection; quotientrequiresa!=0. Halfangle denominatorpositiveexceptu=-1handled, r>0provedbeforedivision. Negativea usescomplexrootformula ratherthanrealpositivecircle. Bothrootsdifferbysign. Fulldefinitionearnsfiniteconstruction, excludescoincidentcurves/unfixedline. Explicitlineequations replace unsupported as-in-V1geometrypointer.

Correction: Teach product/quotientlineequations andexplicitradiuslengthtransfer locally; preserve entire field/conjugation/squareroot/coordinateclaim.

## cor:classical

Domain: Q/C Euclideanconstruction; cuberoot2,60degtrisection,pentagon,heptagon; primepolygonp>=3 necessaryp-1power2.

A: X³-2 Eisenstein2givesdegree3. u=2cos20 obeysu³-3u-1bytripleangle; rationalcandidates±1fail, so degree3. Wantzelpower2 rulesbothout. Pentagonzeta:1+zeta+...+zeta4=0 gives t=zeta+zeta^-1 root t²+t-1, positive t=(√5-1)/2. cos72=t/2,sin72positive√(1-t²/4); repeatedcomplexmultiplicationgivesfivevertices. PrimePhi shift=((X+1)^p-1)/X=sum binompk X^(k-1),monic, lowercoeffsdivpfromprimebinomialdivisibility,constantpexact; Eisensteinand invertibleshiftirred⇒degreep-1. Constructiblepolygonvertex⇒p-1power2, p7degree6contradiction.

B/boundaries: Separate geometric pentagoncircle centre-.5/radius√5/2positiveroot/twoperpendicular intersections agreesalgebraandactualscaledplate. Rational-rootcubiccandidatevalues±1bothnonzero; constructingcos20equivalentu viafieldclosurealreadyproved. p2cyclopolynomialdegree1validbutpolygondefinitionrequiresp>=3. Primeconditionnotclaimed sufficientuntilC10; newquarticshowsdegreepower2aloneinsufficient. Actual V1printedC6fullEisenstein/ex:eisen(b)678-684read; oldmultilineChapter3pointercorrectedto6withoutchangingmath.

Correction: Correct source pointer andearn full shiftedbinomialproof locally, retain alloriginal classicalclaims.

## prop:quartic-nonconstructible

Domain: Everycomplexroot ofmonic f=X4-X-1overQ; realrootexistsin(1,2). Allhavefielddegree4andnoneconstructible.

A: Modulo2f=X4+X+1 hasno0/1root; anyreduciblequarticwithoutlinear factorswouldbetwoirreduciblequadratics. OnlymonicirreducquadX²+X+1,squareX4+X2+1differs. C6monicreduction/Gauss⇒Qirreddegree4. Ifalphaconstructible,WantzelfinitequadraticEchain. Foranyotherrootbeta, actualearlierextend1 mapsQalpha→Qbeta. FiniteQbasisE generatesoverQalpha; addonegeneratoratime, mappedminimalpolyhascomplexrootbyactualV1FTA,extend1extendsmaptoE. Originalchainimagespreservedegreesbybasisbijection, soallbetaconstructible. Allfourri incalC. e1=0,e2=0,e3=1,e4=-1. Set s=r1+r2=-(r3+r4),u=r1r2,v=r3r4,y=u+v. e2 gives s²=y,e3gives s(v-u)=1,uv=-1. Thus1=s²(v-u)²=y(y²+4), yrootY³+4Y-1. Monicrationalroot±1give4,-6⇒irreddegree3contradictsWantzel. f1=-1,f2=13andactualearlierIVTgiverealroot.

B/boundaries: Independentfullresolvent: threepairingvaluesyi have sum e2, pairsum e1e3-4e4, product e3²+e4(e1²-4e2), bydirectsymmetricexpansion; substituting0,0,1,-1againY³+4Y-1. Exact4variablepolynomialdictionaryexpandsallthreeidentities, bitpolynomialdivisiontestsall6monicdegree1/2factorsF2, cubicvalues/endpoints. AdversarialembeddingcheckneedsneitherprimitiveelementnorGaloiscorrespondence/normalclosure: finitegenerators/one-stepisomorphism/FTAandbasisdegreepreservation suffice. No divisionbys, u-vorrootdifferences. DomainQchar0; p2calculationonlyreductiontestnotconstructionfield. CounterboundaryX4-2irreddegree4yetconstructiblebytwosquareroots(andiallroots), resolventY(Y²+8)reducible, so notallquarticsruledout. Statementcoversallcomplexrootsnotonlychosenrealone.

Correction: Newfull157thnamedproofearnsformerlyasserted necessary-not-sufficient boundary. No weakerreplacement or removedtarget. ProofA/Breconstructed before externalWantzelpapercomparison; actualWantzel371alsohasaquarticcriterion, laterreadonlyasattributioncomparison.

## ex:algfield (whole triple)

A: Qalpha,beta finitebyminpoly;betaoriginalQpolystillannihilatesoverQalpha, towerfinite. Sum/difference/product/inversebeta!=0 livefiniteextensionandthusalgebraic, provingQbarfield. FornonzeropolynomialPoverQbarandcomplexrootgamma, fieldMgeneratedbyfinitelymanycoefficientsfiniteoverQ; gammaalgebraicoverM⇒Mgam/Qfinite⇒gamma∈Qbar. ActualV1FTAgivesrootforeverynonconstantP, repeateddivisionoverQbargivesfullsplitting. Enumerateintegerpolysbydegree+sumabscoeffsbound, finiteeachbound; eachfinitecomplexrootlist lexorderedreal/imag. CountablelistallQbar. SubsetA→sum2/3^nconvergesbyboundedmonotonepartialsumandgeometrictail;firstdiffkgivesgap>=1/3^k. Anylistrealwouldthuslistallsubsets,contradictactualV1diagonalpowersetargument. HenceR/Cuncountable, interleavingtwocountablelistsprovestranscendentalcomplementuncountable.

B/boundaries: Separatefinite-coefficient-fieldtransitivity reconstruction: chooseQbasisM, thenpowersgammauptominimaldegree, theirproductsfiniteQspanbyactualtowerproof. ThiscoversALLcomplexrootsofP, notonlyone. Constantsnonzero havenorootbutnotneededforalgebraicallycloseddefinition; zeropolynomialexcludedfromalgebraicwitness/rootcount. Oldeverypolynomialwordingthereforecorrectedtononconstant. Integerpolynomialboundwithleadingzero conventionsstillfinite; nonzeroconstantscontributenoroot,duplicatesharmless. Ternarymapusesdigits0/2, firstdifference2/3^kexceedstail1/3^k, soendpointdouble-expansioncannotidentifytwochosen digitlists. MonotoneboundedpartialsumisactualearlierV1proof, notunprovedinfiniteprocess. CountableunionalgebraicnumberspluscountablecomplementwouldenumerateC, contradiction. Allprompt/hint/idea/fullsolutionread, originalthree-parttargetandgrade2retained; originalCH08-PROMPT-FIRST exposure chronology unchanged, no new blindsolveclaim.
