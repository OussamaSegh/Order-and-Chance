# V3-009 — Chapter8 independent exercise solutions before hints/solutions

Entire main argument and all8 current prompts read, stopping before Hints1149.
No supplied C8 hints/solutions opened before this record. The existing primitive
exercise exactly repeats an already-proved main theorem; its planned replacement
retains the theorem and asks quantitative/application/boundary questions instead.
Internal AI reasoning only, not a claim of independent human work.

- sqrt23: E=Q(sqrt2,cuberoot2) hasdegree<=6, and contains subfieldsdegrees2/3,
  so degree divisible6 by tower, hence6. Letalpha=s+t. Expand numerator
  alpha³+6alpha-2=8s+12t+3st²=s(8+6st+3t²)=s(3alpha²+2).
  Denominator>0 sincealphareal. Thus s inQalpha,andt=alpha-s,soQalpha=E,
  degree6. Independent substitution/polynomial expansion verifies formula.
- inverse:t³2 gives(1+t)(1-t+t²)=3, sofirstinverse(1-t+t²)/3.
  (1+t+t²)(t-1)=t³-1=1, sosecondinverse t-1. Both exactproducts, nozero
  divisions, actual t>0. Can alternatively solve three rational coefficients
  via multiplicationmatrix onbasis1,t,t².
- classical: complexproducts/quotientsgiveangles±,square-rootsgivehalves(up
  to180degrees, repairedwithconstructible-1). 72-60=12,halve twicegives3.
  Allmultiples3constructible incl0/negative. If3notdivide n,Bezout an+3b=1,
  soconstructible n°and3°wouldgive1°,then20°,contradictingproved60°trisection
  obstruction. 72°trisectsto24°=8*3°.
- polygons: t7=ζ+ζ^-1 and1+...+ζ6=0 imply(t³-3t)+(t²-2)+t+1=0,
  hence t³+t²-2t-1. t9tripleanglegives t³-3t+1. Bothcubics lack±1 roots,
  henceirreducibleanddegree3; regularverticesconstructiblewouldgive tconstructible.
  For17,[Qζ:Q]=16fromshiftEisenstein; ζrootY²-tY+1 overrealQt,notinrealQt,
  so[Qζ:Qt]=2,tdegree8. Necessarypower2conditionnotaconstructionproof.
- algfield: Q(a,b)finiteforallalgebraica,bbycorfinitealg;everyelementincluding
  sums/products/inversesalgbyfinite=>alg. Enumerateintegercoefficientpolys by
  degreeandsumabsolutevalues; eachfinitebucket, eachnonzeropolyfinitezeros,
  soalgcomplexcountable. Forcoefficientsalg,finitegeneratedcoefficientfieldE/Q,
  rootzfiniteE(z)/EthenfiniteQbytower,soalgQ. TranscendentalsbecauseRuncountable;
  actualearlierCantorproofavailabilitymustbecheckedbeforeacceptance.
- splitdeg: X4-2hasEisenstein2roota degree4; allroots±a,±ia,fieldQ(a,i).
  Q(a)realand i notreal,soadjoiningi degree2,total8. Xp-1 splittingQζp,
  degreep-1byprimecyclotomicshiftEisenstein,p2givesdegree1 explicitly.
- oddeg: primedegreeno properintermediate,soanyalphaoutsideKgenerates.
  If[Kalpha:K]odd, [Kalpha:Kalpha²]<=2 fromY²-alpha²; dividesoddtotalso1.
  Worksallcharacteristics,alpha0/degree1trivial,finiteoddassumptionexplicit.
- primitiveexistingprompt: alreadyprovedexactmain theorem. Fresh check ofgcd
  proofrequiresBezout to infer positivebase-fieldgcd fromacommoncomplexroot;
  usegcd1contradiction atbeta. Finitelymanybadcomplexc; infiniteQcontainedK,
  cavoidsall. Degree1extensionneedschoosegamma0whenbasis-generatorlistempty.

Planned earned replacement ex:primitive, samekey/triple count, three stars:
(a) For m=degreealpha,n=degreebeta, choosegoodintegercfrom0..m(n-1), viaatmost
m(n-1)forbiddenvaluesintheprovedgcdargument (n1onlycandidate0andworks).
(b) Forgamma=sqrt2+c sqrt3,c nonzero rational, gamma!=0 andD=2-3c²!=0 by
rational-squareprimevaluations; sqrt2=(gamma+D/gamma)/2, sqrt3=(gamma-sqrt2)/c.
Thusallnonzerorationalcworkanddegree4byearlierexample. c0failstogeneratesqrt3.
(c) LetS,Tformalindeterminates,charp, L=Fp(S,T), K=Fp(S^p,T^p). Monomials
S^iT^j,0<=i,j<p, span: reducepolynomialexponents; 1/g=g^(p-1)/g^p withg^p inK.
Theyareindependent: clearKdenominators thenmonomialexponentresidueclassesmodp
cannotcancelinFp[S,T]. Hence[L:K]=p². Everygammahasgamma^p inK,so simpledegree
<=p byX^p-gamma^p, strictlylessthanp². No primitiveelementexists. Allneeded
rationalfunction/UFD/characteristictools taughtlocally; nofutureGaloistheory.

Subsequent adversarial check of new(c), independent of the monomial proof:
putU=S^p,V=T^p. OverFp(V)(U), X^p-U is EisensteinatU inFp(V)[U][X],
so adjoiningS hasdegreep and givesFp(S,V). ThenX^p-V is EisensteinatV
inFp(S)[V][X], givingdegreepagain. Tower givesp². This uses onlyC6Gauss/
EisensteinandC8tower, corroboratesbasisdimension, andchecksnohiddenfinite-field
existenceorperfectnessassumption. Everyelement'sp-thpowerinKstilllimitsany
simpledegree<=p, a differentreason frommerefailureofthecharacteristic0proof.
