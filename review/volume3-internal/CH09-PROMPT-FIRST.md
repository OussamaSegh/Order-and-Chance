# V3-010 — finite-field independent exercises before supplied hints/solutions

Read entire main argument and all13 prompts, stopping before Hints723. No C9
supplied hint/solution opened before this record. Internal AI reasoning. The
following are reconstructions, not approval of the supplied solution yet.

1. f4tables: bitpairsfor0,1,a,b=a+1, additiveXOR; nonzeroa³1. Multiplication
   rows0all0;1=(0,1,a,b);a=(0,a,b,1);b=(0,b,1,a). Additionrows0=(0,1,a,b),
   1=(1,0,b,a),a=(a,b,0,1),b=(b,a,1,0). AdditiveF4=C2²hasallnonzeroorder2,
   Z4haselementorder4. F2[X]/(X²+1) hasnonzeroclassX+1square0,so notfield.
2. irrF2: degree1 X,X+1; degree2 X²+X+1; degree3 X³+X+1,X³+X²+1;
   degree4 X4+X+1,X4+X3+1,X4+X3+X2+X+1. Noothermonicirreduciblesbycounts
   2,1,2,3. Degree4testsneednolinearrootsANDnotdivisiblebyuniquequad.
   X16-Xproductofalllisteddegree1,2,4factors; totaldegree2+2+12=16,separable.
3. primpoly: firstirreducibleα4=α+1, ordαdiv15. Not1/3byminimaldegree4;
   α5=α²+α!=1so not5, hence15. Phi5classorder5,not15; itisirreducible
   bynolinearroots/quaddivisibilitytest. F16hasphi15=8generators, eachdegree4
   minimalpolyhas4Frobeniusconjugategenerators,so2primitivepolys; otherreciprocal
   X4+X3+1hasrootα^-1. TrivialunitgroupF2notneededherebutnotexcludedbytheorem.
4. minus1: oddqcyclicq-1, uniqueorder2elementg^((q-1)/2)=-1; squareiffeven
   exponentq1mod4. ForF9withβ²=-β-2=2β+1, β4=2=-1, soβ²=2β+1oritsnegative
   β+2issquareroot. Rootfieldisdegree2(noFp3roots). Distinguishfieldgenerator
   frommultiplicativegenerator: classi inFp3[X]/(X²+1)field-generatesbutorder4,
   not8; thisneedslocalteachingwhereC9reuses'primitive element'.
5. twosq: char2Frobeniussquarebijective, a=u²+0². Oddq,Ssquaresincl0has(q+1)/2
   elements. Sanda-Sboth>q/2,intersect,so a=sumofsquares. Zeroallowed; doesnot
   assertnontrivialrepresentationof0when-1nonsquare.
6. powersums: k0sumq=0charp,with0^01. k>0zerocontributes0; cyclicgeometricsum
   nonzerog^jk isq-1=-1ifq-1|k,otherwise0becauseg^k-1invertible. Wilsoninverse
   pairsleaves±1oddchar/-1product; char2onlyselfinverse1and1=-1. Alternative
   generatorproductsameanswerforq-1even/odd. q2allpositiveksums1=-1.
7. rs7: independentlyfitlinef=2X+3,giving(5,0,2,4,6,1),errorspositions2/5.
   E=(X-2)(X-5)=X²+3, Q=fE=2X³+3X²+6X+2 inFp7. Meetsall6equationsanddegree
   requirementsn6k2t2. Exactenumerationof49messageswillcorroborateunique4matches.
8. chevalley: n>=1,degF=d<n, zeroFseparateq^nzeros. N*1=sum(1-F(x)^(q-1)).
   Constanttotalq^n1=0. InF^(q-1),everymonomialtotaldegree<n(q-1),soonevariable
   exponent<q-1; itsone-dimensionalpowersumis0,includingexponent0. Finite
   productssumto0,soN*1=0,andp|N (notclaimq|N). IfF0zero,N>=p>=2givesnonzero
   zero. Homogeneousquadraticn3workschar2aswell. Zero-polynomial/n0convention
   mustnotcreatefalseclaimforzerospace;explicitn>=1.
9. fibmodp: p!=2,5,putδ=(5/p),rootsa=(1+sqrt5)/2,b=(1-sqrt5)/2 inFp/Fp².
   a+b1,ab-1,a-bsqrt5nonzero; verifyBinetFn=(a^n-b^n)/(a-b)byrecurrencen0/1.
   Ifδ1,Fermatgivesa^(p-1)=b^(p-1)=1. Ifδ-1,Frobeniusswapsa/b,soa^(p+1)
   =b^(p+1)=-1and2(p+1)powers1. ThusF_{p-δ}0andperioddividesp-1or2(p+1).
   Fullpairrecurrencemapinvertible=>pureperiodic; leastperioddividesanyperiod
   bydivision/minimality. Actualenumerationp7period16,p11period10. δ=±1according
   pmod5usesactualV2reciprocityproof,readbeforeacceptance. Denominators2/sqrt5
   handled; p2/5excludedintentionally.
10. pascal2: (1+X)^(2^k)=1+X^(2^k)char2,coefficientextractafter(1+X)^m.
   For0<=m<2^k,thetwoshiftedrowsdisjoint,sooddcountdouble. Binaryfactorization
   rown gives2^s(n)distinctsubsetexponents. Summingn0..2^k-1 gives(1+2)^k=3^k.
   Totalentries2^k(2^k+1)/2,fraction2*3^k/(4^k+2^k)->0. k0,n0valid.
11. lucaslehmer: writeN=2^p-1,poddprime. IfNprime,N7mod8and7mod12,so(2/N)1,
   (3/N)-1byactualV2supplement/reciprocity. InF_(N²),u²3,u^N=-u,α=2+u,α^-1=2-u.
   α=(1+u)²/2,andα^((N+1)/2)=((1-u)(1+u))/2^((N+1)/2)=(-2)/2=-1.
   Henceαexactorder2^p. sk=α^(2^k)+α^(-2^k)byrecurrence,ands_(p-2)0because
   b=α^(2^(p-2))hasb²=-1,b^-1=-b. Reverse: ifNdividess_(p-2),takeanyprimeq|N.
   qoddandq!=3becauseN1mod3. Infieldofqorq²elementscontainingu²3,αnorm1nonzero;
   recurrencegivesb²=-1!=1,sothatordαexact2^p=N+1. Lagrangeimpliesq²-1>=N+1,
   henceq>sqrtN. AcompositeNhasaprimefactor<=sqrtN,contradiction. Thisreverse
   avoidsassumingZ/Nisfieldandhandlesallprimefactors,notjustoneexample. p3,N7,
   s1=14boundaryworks. p2excludedbecauseusuals0conditionwouldfailforM3.
12. moore: detDnonzero? asformalpolyrootsinxi at-Σc_jxj causeFqrowdependence.
   Eachnormalizedlast-variablelinearformprime/nonassociate,productdividesD in
   UFDmultivariatering. Degreesbothsumq^j,constant1fromleadingorderedmonomial
   x1*x2^q*...*xn^(q^(n-1)). Alternativeinductinx_n overfractionfieldofprevious
   variables: q^(n-1)distinctformalroots,leadingcoefficientD_(n-1),sameproduct.
   EvaluationD0iffsomefactorzero=nontrivialFqlinearrelation(normalizelastnonzero
   coefficient). n0det1/emptyfamilyvalidifstated. ForVbasisv1..vr,
   P_V(X)=D(v1,..,vr,X)/D(v1,..,vr); numeratorlinearcombinationX,X^q,..,X^(q^r),
   monicdegreeq^r,rootsetexactVbydegree. ThusFqlinear/additive,includingV0P=X.
   SecondderivationinductW+Fqv: P_V=P_W^q-P_W(v)^(q-1)P_W,usingP_W(v)!=0.
   Gradeprobably3ratherthan2forthreepartsmultivariatedeterminant/additivepolys.
13. mseq: Trβ inF2because(Trβ)²-Trβ=β^(2^n)-β0; Tradditive/F2linear.
   Nonzeroevenwhenn even: tracepolynomialnonzerodegree2^(n-1)<2^n,cannotvanish
   onallK. Thussurjective/kernel2^(n-1). PairingTrβxnondegenerate: chooseγwith
   Trγ1andx=γ/βforβ!=0. Since1,α,..α^(n-1)basis, coordinateTβall0forcesTrβx0
   forallx,thenβ0,soTinjective/bijective. WindowsareTα^k; nonzerofieldpowers
   cycleallnonzeroβ,soevery nonzeronbitblockonce,leastperiodN=2^n-1. Allnonzero
   recurrenceinitialvectorscorrespondβ=α^r,soarephases. Trcountsperiodones2^(n-1),
   zeros2^(n-1)-1. Autocorr0<t<N: Trα^k(1+α^t),multipliernonzero,permutesK*,
   sozeros-minusones=-1. Atendpoints t0/NcorrelationN, not-1. n1N1ones1zeros0,
   correlationrangeempty. Tr1=0whenn evenmustnotbeusedasnonzerotraceproof.
