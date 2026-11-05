# Chapter 4 prompt-first solutions, V3-005

Ten prompts read before supplied hints/solutions. Main proof text has been read,
including the complete rectangle-loop attainability argument and all An
commutator cases. Internal AI reconstruction only.

- ex:landau: maximum orders12 inS7 (4+3) and30 inS10 (5+3+2). Enumerate partitions
  and their least common multiples; certify maximum by complete partition list.
- ex:order2: k=1,2,3 disjoint transpositions inS6 number15,45,15; total75 of
  order2, with45 even. Identity must not be counted.
- ex:gens12n: n>=2 needed. Conjugating(12) by long-cycle powers gives adjacent
  transpositions. For(13),(1234), preserve diagonal-pair partition; conjugates
  give(13),(24), group isV4 semidirectC2 onfour cycle positions, order8. Forprimep,
  name cycle positionsZ/p; transposition endpoints differ byd nonzero. Its cyclic
  conjugates exchange(r,r+d). Since0,d,...,(p-1)d list allpoints, these include
  adjacent swaps in that ordering and generateS_p. p2 included.
- ex:v4: double-transposition set plusidentity is closed and a fullcycle-type
  union, hence normal. Action onthree pairpartitions has a3cycle from(123) and
  transposition from(12), hence allS3; V4 lies inkernel and both haveorder4.
- ex:normalSn: N intersectAn isEorAn bysimplicity. IfAn included, N=AnorSn.
  Otherwise sign injectsN intoC2, so N hasorder<=2. A normalorder2 element is
  central. CenterSn trivial forn>=3: ifz sendsi toj!=i, choosek distincti,j;
  transposition(jk) fixes i but does not commute withz at i. ThusN=E. Index2
  subgroupnormal, hence mustbeAn.
- ex:rubik: eachquarterturn inducesa4cycle oncorners anda4cycle onedges, so
  productofsigns fixed. For edgeorientation, represent anedgeposition byits two
  perpendicular facenormals. Primarynormal chosenUD first, elseFB. For eachface
  quarterrotation compute whetherprimary maps toprimary atnewposition: U,D,L,R
  preserve for allfour affectededges; F,B reverse for allfour. Binaryorientation
  parity thereforefixed for arbitrary cubie orientations, notjust solvedcube.
- ex:shuffle: out mapdoublingmod51 plusfixedlastposition, order8 because2^8=1,
  properdivisors1,2,4 do notwork. Inmap2i+1mod53 (exclude residue52); shift i+1
  givesdoubling, whoseorder is52:2^26=-1mod53 and2^4!=1 exclude everyproperdivisor.
- ex:split: oddcyclelength needed because anevencycle itself is anoddcentralizer.
  Repeatedoddlengthd gives odd permutation swapping matching cycles, productofd
  swaps. Ifalllengthsoddanddistinct, commuting permutationpreserves eachsupport
  and restrictsto apowerofthatcycle, hence iseven. Lemmasplit then applies.
  Earliestnon-ncycle example n4, type(3,1). n2/3 checkedexplicitly.
- pb:discphi: derivativePhi_p atzeta^i is p zeta^-i/(zeta^i-1); product=p^(p-2),
  fromproduct(zeta^i-1)=Phi_p(1)=p andsum i multiplep. Productderivatives equals
  (-1)^binom(p-1,2) Delta², givingDelta²=p* p^(p-3). DivideDelta byp^((p-3)/2)
  to getsquare-root. Vandermondeon residues0..p-1 gives signpi_a congruent
  a^(p(p-1)/2)=a^((p-1)/2), henceLegendrebyEuler (oddp). Automorphismpermutes
  nonzero rootindices, so sendsDelta tosignpi_a Delta. Needlocallyearn Q(zeta)
  andautomorphismexistence fromearlierPhi_p irreducibility/polynomialBezout;
  these arenotavailable merelyfromfutureextension/Galoischapters.
- pb:conjugate: classprobability1/z_lambda yieldsPn=sum_lambda1/z_lambda².
  Summing allweightedpartitions givesproduct_j sum_m1/(j^(2m)m!²). Positive
  finite truncations andfactorbound proveconvergence; decimalrequires bounded
  numericaltail, notanuncontrolledtruncation. Forr<=M andn>2M, cycletypes witha
  singlelongcycle n-r contributePr/(n-r)² andaredisjoint. Thusliminf n²Pn
  >=sum_{r<=M}Pr, andM->infinitygivesthefullconstant. No interchangeoflimits.

The explicit fifteen-puzzle rectangle cycles/growth conditions will be checked
again by independently simulating legal blank slides. An proofcommutator products
will be checked directly with rightmost-first permutations, includingn5/6 edges.
