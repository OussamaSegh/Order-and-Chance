# Batch G — Gaussian and Eisenstein arithmetic

## Changes implemented
Defined integral domains, cancellation versus inversion, prime versus irreducible elements and proved prime implies irreducible. Made the general norm hypotheses in the Euclidean-factorization theorem explicit. Added an exact Eisenstein Euclidean division and Bézout certificate. Expanded the exceptional-prime allocation in cubic Fermat descent. Qualified the historical shorthand about Euler's gap with the existing Edwards reference.

## Mathematical improvements
The general norm theorem now states precisely which properties its induction uses. Cubic descent review checks lambda valuations 3n-2,1,1, no other common prime, the n=1 obstruction, the unit coefficient and the coprime smaller equation. Rounding bounds remain 1/2,3/4,3/4 in the three original rings. The Gaussian and Eisenstein prime classifications retain their non-associate conjugate checks.

## Pedagogical improvements
An unfamiliar ring is introduced with enough vocabulary to justify the computation. The new triangular-lattice example ends with a checkable identity equal to 1, explaining what the algorithm certifies.

## Content preservation
All three original rings, full cubic descent, seven exercise triples and original assets are retained. All original semantic labels remain. No general algebra course is inserted.

## Verification
Complete PDF build passes layout/style/body identity/cover preflight, 179 interior pages. Cumulative PDFs/logs at `/workspace/volume1-checkpoints/G/`. Inventory and diff checks pass. Exact expansion verifies (2-w)(2+w)=5+w and (-1-w)(5+2w)+(1+2w)(2-w)=1 using w^2=-1-w. check_math.py independently verifies lambda^4 divisibility of unit cubes on representative coefficient pairs; source review supplies the universal proof.

## Remaining issues
Quadratic fields/ideals and p-adic foundational expansion remain. Historical interpretation is now appropriately qualified rather than asserted more strongly than the cited account warrants.

## Next work
Batch H: split quadratic integers from ideal arithmetic; justify integrality and residue-count norms; audit the class group and splitting of 2.
