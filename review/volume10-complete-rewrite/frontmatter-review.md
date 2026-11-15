# Front matter, publication copy, quotations and portrait review

Reviewer: `independent_review`, separate from the writers.
Baseline main: `59014a9aad3454ad60786c6549c81fcac88df9df`.
This is a separate source/editorial review. The parent owns rendered interior,
cover, EPUB, build, CI and published-artifact inspections. None is claimed here.

## Reader-facing copy

Read every sentence and short clause of the rewritten preface, back-cover blurb,
KDP listing, canonical Volume 10 About the Cover entry and generated TeX note.
The concrete progression matches main.tex: three category/tensor chapters,
Noetherian/local/Dedekind algebra, homological algebra and group cohomology,
then three representation chapters. There are eleven numbered chapters and no
appendices. The prerequisite list names actual earlier material in Volumes 3,
7, 8 and 9. The full next-volume title/subtitle is Randomness: Martingales,
Limits and Ergodicity.

The copy accurately distinguishes subsequences from consecutive runs, theorem
proofs from quoted further results, ideal factorisation from element
factorisation, and exact finite trace calculations from limits. The previous
unqualified promise that every theorem is proved is gone. No notebook promise,
revision/previous-edition framing, assigned identifier alteration or paperback
ISBN assignment appears. The prose is plain and concrete throughout, including
formula introductions and brief transition clauses.

The About the Cover note matches the actual snake-lemma motif: two exact rows,
three vertical maps, kernels, cokernels and connecting map from the last kernel
to the first cokernel. Printed Chapter 3 supplies the construction. The canonical
note and generated note agree at this checkpoint; only Volume 10's shared note
entry has changed. The cover credit is preserved. No artwork change is involved.

## Literal quotation and bibliography preservation

Compared the original manuscript at starting main against all rewritten chapter
sources. Normalised line whitespace only when comparing quoted words. The
Strassen epigraph is also byte-for-byte retained as a complete centred block.
The historically attributed passages survive with their words intact:
Mac Lane's adjoint slogan; Gordan's theology remark; the German Dedekind saying;
Lang's homological-algebra exercise; both Burnside preface passages;
Turnbull's description of Young; and Weyl's angel/devil passage. The original
quoted article titles and emphatic bibliography titles are present, with their
bibliographic records retained.

Removed quotation-marked working terms such as determinant trick, degenerate,
almost, and the set of extensions of C by A are explanatory jargon, not omitted
literal historical passages. Their removal or explanation is part of the prose
rewrite. No restoration of vague jargon is required by quotation preservation.

## Portrait identification, rights and native source

Independently opened and inspected the local Hilbert portrait. Retrieved and read
https://commons.wikimedia.org/wiki/File:Hilbert.jpg on 15 November 2026. Its file
page identifies David Hilbert, names the anonymous faculty postcard, describes
sale to Goettingen students in 1912 and cites Constance Reid, Hilbert (1970).
The page explicitly records US public-domain status for publication before
1 January 1931, and EU anonymous-publication status after more than 70 years
without a timely authorship claim. Those statements support the public-domain
evidence recorded in CREDITS.md and the source-evidence JSON.

Independently downloaded the original source JPEG from
https://upload.wikimedia.org/wikipedia/commons/7/79/Hilbert.jpg and compared its
bytes with the repository image: exact equality, 104667 bytes, 437 by 592 pixels,
SHA-256 e0510813434980c4f93329694b0816770d388aacb27f0d83b88588cbc119a930.
No resampling, edits or enlargement are present. At the macro's maximum printed
height of 1.65 inches, native effective resolution is 592/1.65 = 358.7878788 ppi;
preserving aspect ratio gives the same horizontal ppi. This is a source-derived
resolution check. Actual embedded-image resolution and placement remain for the
parent's final rendered-artifact inspection.

The portrait occurs immediately after the first substantive Hilbert discussion
in Chapter 4, alongside an identifying anonymous-postcard/public-domain/Commons
credit. The local portrait macro uses a float without a caption command, so it
does not increment the numbered mathematical-figure counter. The maximum-height
rule and aspect-ratio preservation support consistent presentation. The portrait
has a teaching purpose: it accompanies the named finite-generation argument;
there are no count-driven photographic additions.

## Result and provenance

No blocking source/editorial/rights finding remains in this assigned scope.
Final source hashes at this review checkpoint:

| Path | SHA-256 |
| --- | --- |
| `volume10-abstraction/chapters/preface.tex` | `6952790ab8601591b3f0988f0e0ea565eab955636201335e87e880da27cc75e8` |
| `volume10-abstraction/blurb.tex` | `69cc5072a20c6ad709d5f5880684ac5d5355f80f540a5de16442389ed9b5abc2` |
| `volume10-abstraction/kdp.md` | `45532376caa9cfbadb06335784977030543aab3e2f4ac4ed0f8445d2ccb7a545` |
| `volume10-abstraction/about-the-cover.tex` | `3a3b59e8aebd0df84f49e940576561230477b2a85b804a58f72fa18b8129348e` |
| `volume10-abstraction/main.tex` | `3258df9a11587f0ef2e958be0337ead33a30c6f8dfe3a83367408bb4cad2e6b5` |
| `common/cover-notes.json` | `e2b0dab1f51fb19b768f2c882b83f64c1d74baafd6e1ae244716e2a49538460e` |
| `volume10-abstraction/photos/CREDITS.md` | `178c0833f4e10baf3fa85f48346c5d01dac210582e77d4d88253ad22c4e3876a` |
| `volume10-abstraction/photos/hilbert-source-evidence.json` | `e1a0476a13136192b89c477ecec1e2f3ef29d78613d866b7966440f29aeb1289` |
| `volume10-abstraction/photos/hilbert.jpg` | `e0510813434980c4f93329694b0816770d388aacb27f0d83b88588cbc119a930` |

Any subsequent edits to these files require a focused recheck. Overall source
acceptance also depends on the disjoint chapter reviewers and final preservation
records; this review does not certify production artifacts or publication.

## Focused production-copy recheck

Read the final standalone-cover compatibility change in blurb.tex: replacing
\Z by \mathbb{Z} changes the TeX spelling of the same integer-ring notation,
not its mathematical content. Read the added About the Cover sentence, “The
quotient removes dependence on the chosen lift.” This accurately describes the
connecting homomorphism's cokernel class. The canonical and generated notes agree,
and the existing TikZ-generator identification is retained. Updated hashes above
record these exact reviewed files. No new finding was introduced.
