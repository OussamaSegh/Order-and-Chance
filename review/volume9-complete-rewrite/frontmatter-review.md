# Preface, jacket, listing and cover explanation

Status: rewritten draft, shared cover-note synchronisation passed. The combined
PDF-only build exited 0 at 403 print pages. This is a checking pass by the writer; the separate
final independent review remains outstanding.

The preface, back-cover blurb and repository KDP description were rewritten in
plain English, with concrete triangle, loop and matrix examples. They describe
all eleven chapters and eleven appendices, preserve the earlier-volume
prerequisites and distinguish proved results from quoted advanced results.
The full associativity theorem remains explicitly deferred to Volume 13.
Montgomery's restricted theorem and the conjectural full zeta pair-correlation
law are distinguished from the proved random-unitary result. No ISBN,
publication identifier, typography or cover artwork was changed. The KDP file
is repository copy only; nothing was uploaded to Amazon.

The preface now names Volume 10 by its catalogued title and subtitle:
*Abstraction: Categories, Algebra and Homology*. Verified against
`common/series-catalog.json` and `docs/SERIES-STRUCTURE.md`.

## Mathematical correction to About the Cover

The old note said Klein's quartic was a quotient of the disc tiling by a
**finite** group. The disc-to-compact-surface quotient uses an **infinite discrete**
group of hyperbolic isometries. The finite group of 168 holomorphic automorphisms
acts on the resulting compact surface, not as that uniformising group.
The replacement says this directly and retains the genus-three connection.
It also says Poincare *used* the model in 1882 rather than assigning him an
unsupported priority claim that he introduced the model itself.
The geometric source is the Chapter 9 hyperbolic setup and Klein-quartic exercise,
with S. Levy (ed.), *The Eightfold Way*, already listed among that chapter's
sources. The cover generator itself uses p=7,q=3 in `tools/covergen/arts.py`.

The canonical note was edited in `common/cover-notes.json` and regenerated with
`python3 tools/series_cover.py`, which exited 0 and checked synchronisation.
Only Volume 9's about text, `docs/COVER-NOTES.md` and the corresponding metadata
hashes in the shared manifest changed. No other volume note, motif or lettering
changed. The short copyright-page cover credit is unchanged. The new note is
96 words, within the generator's 80–150-word requirement.

The rendered full paperback wrap, preface opening (manuscript PDF page 5) and
About the Cover (page 403) were inspected. Blurb, spine and cover text fit with
no visible collision; the artwork and typography are unchanged. Shared cover
checks and all PDF layout/print checks passed. The final complete build and
rendered EPUB inspection remain pending.

The Riemann image now also has independently inspected pre-1931 publication
evidence: the 1892 collected works frontispiece, scan PDF pages 10 and 14.
The source photograph was compared directly against that printed portrait;
URLs, date, publisher and scan SHA-256 are preserved beside the Commons
metadata. The portrait file itself is unchanged.
