# V3-007 — prompt exposure and exercise reconstruction

Main prose/proofs and all eight prompts were read in order. During a source chunk
read, supplied solutions for the first six exercises were also displayed before
this permanent reconstruction was written. No prompt-first or blinded-solution
claim is made for those six. Their A/B checks must be substantive mathematical
reconstructions despite that exposure. The last two supplied solutions have not
been displayed at this checkpoint; the following solutions are recorded first.

- ex:crtinterp: write P=aX²+bX+1. Conditions a+b=-1 and2a+b=2 give a3,b-4,
  hence P=3X²-4X+1. Independently the CRT residues are1modX and2(X-1)mod(X-1)²;
  solve by P=(X-1)²+2X(X-1), degree2, giving the same. Uniqueness: a difference
  has root0 and double root1, thus divisible by degree3 X(X-1)². This local double
  root assertion follows division by (X-1)²/remainder a+b(X-1), whose derivative
  at1 is b. Ideals coprime since (X-1)²+X(2-X)=1. Two stars.
- ex:x4p1: shift by1 gives X4+4X3+6X2+4X+2, Eisenstein at2; translation is
  an invertible Q-algebra map, so original irreducible. Mod2 it is(X+1)^4.
  For oddp at least one of-1,2,-2 is square: if firsttwo nonsquares their product
  is square by the Legendre multiplicative rule. a²=-1 gives(X²+a)(X²-a);
  b²=2 gives(X²+bX+1)(X²-bX+1); c²=-2 gives(X²+cX-1)(X²-cX-1).
  All factors monic degree2, even when coincident or reducible further; these are
  valid nontrivial factorizations for every oddp. Independent extension route:
  any root of order8 overFp has Frobenius orbit length dividing2 since p²=1mod8,
  but this route needs future finite-field machinery and is NOT a reader premise.
  Three elementary displayed factorizations earn the exercise now. Three stars.

Fresh reconstructions after the recorded exposure of the first six:
- idealsZn: use inverse images dZ containing nZ; d|n,n>=1. Quotient Zd, so
  proper prime/maximal iff d prime dividingn. Units12={1,5,7,11}; nonzero zero
  divisors{2,3,4,6,8,9,10}. Independent test multiplication table/annihilator
  gcd gives same. n1 has sole improper zero ideal, none prime/maximal.
- quot: explicit evaluation at±1 inverse(a,b)->[(a+b)/2+(a-b)X/2]. Double-root
  algebra has basis1,x, x²0 withxnonzero. Square-zero elements in R²/C onlyzero,
  so noiso. Alternative R² has nontrivial idempotent while dualnumbers haveonly0/1;
  solve(a+bx)²=a+bx: a²a,2abb ->b0. Two fieldquotients impossiblechar2 case
  is irrelevant because coefficientfieldisR, where2invertible.
- zsqrtm5: I consists exactlya+bw witha+b even, hence proper/index2 viaexplicit
  F2map. Generator wouldhave normdividing4and6 ->1or2, latterimpossible, former
  unitcontradiction. Alternative Z-basis2,1+w hasdet2; norm generatorwouldequal
  latticeindex2 (multiplicationmatrix determinant a²+5b²), impossible. 3irredvia
  norm9/no3; divides(1+w)(1-w)=6butneitherfactor coefficient1 divisible3.
- zi: rectangularcell coveringradius² (1+d)/4 forZ[sqrt(-d)], so d1=>1/2,
  d2=>3/4; divisionremainderN≤these*N(b)<N(b). d5center(1+w)/2 hasradius²3/2,
  nearestfourlatticepointsallm,n0/1 andallothersfarther. a1+w,b2 givesN(r)>=6>4.
  Independent exactremaindernorm is(1-2m)²+5(1-2n)²>=6. Nfailurealonecannot
  disproveallEuclideanfunctions; nonprincipalidealIandED=>PIDdo.
- zxnotpid: fordomainRnotfield choose nonzero nonunita. A generator d of(a,X)
  dividesconstantanonzero, henceconstant bydegree, anddividesX so unit byXcoeff.
  Butidealproperbyconstantterm at0 belongs(a), contradiction. Conversefield
  degreeEuclidean. IfRnotdomain,R[X]notdomain byconstantzero divisors/1=0;
  PIDdefineddomain, so equivalenceholdsallcommutativeunitalringswiththatconvention.
- boolean: set y=-1 in identity y²=y ->1=-1, thus2=0; distributivitygives2x0.
  Independent expansion(2x)²=2xandx²x gives4x2x->2x0. Domain equationx(x-1)0
  forcesonly0/1. PrimequotientinheritsBoolean/isdomain=>F2=>maximal. Powerset
  exampleisproduct ofF2 coordinatewise, includingemptysetuniversezero ring.
