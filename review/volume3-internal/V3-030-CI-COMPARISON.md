# Actual preliminary local/CI comparison — a0c09b53

Internal AI technical review. This is a prior committed snapshot before C11/C12
changes; it is not final whole-book approval. Source commit
`a0c09b53dd9439c2ef8c386efba3ed9012c473fa`. Actual run1714/41992317151 was
automatically cancelled by later PR concurrency; its Volume3 job succeeded.
Do not report the overall run green. Downloaded actual artifact13400425196,
books-volume3-symmetry,40,848,096bytes; SHA256
4e4ac091ad3a325c8a73de32a91e965d5454078f6bda0da83bd35e00e0bafc60 matches GitHub.
96 members safely extracted. No PR-cache reusability inferred.

80/85 public files byte-identical. Reading/print/wrap PDFs, EPUB and Paley HTML
differ. All516readingpage pixels match at72dpi, with the three earlier actually
opened samples compared at2x.514/515printpages match; the three earlier opened
print samples also match at2x. The sole differing printpage445 is the pipeline's
600ppi-flattened page:2x comparison changes1,005of1,514,376pixels, mean absolute
channel difference0.0037023/max29. The wrap's sole page has identical2xpixels.
Pixel equality transfers only previously actually opened evidence at its tested
resolution, never approval of any remaining unopened page renders.

Actually opened both local/CIprint445 complete pages in colour AND grayscale at2x.
AppendixB3 prose/displays/13nodePaleygraph/caption and full theorem statement box
are legible without observed clipping/collision. Grayscale edge-family weights
and node labels usable. Following proof page/facing spread not approved here.
Only differing HTML text is the Paley footnote wrapper:section versusaside,
sameclasses/id/fragments. Actual narrow/wide behavior remains pending.

EPUB both9,421members. Nine distinct formula PNG paths/pixels differ, with identical
pixel dimensions and CSS dimensions.139ordered math uses/52unique formula attribute
sets differ;43commonPNGpaths byte-identical with CSS rounding atmost0.0001em.
Allnine local/CIglyph pairs actually opened at originalaspect2x: j,1/2,5/8,
n!/z_lambda,n/2,a/b,l,overline f,boldj. Slight raster ink/antialias differences;
no observed clipped strokes/bars/subscripts. Asset inspection does not approve
inline baseline/shape under actual layout. All18differing textmembers are identical
after individually validated CSS rounding, build UUID/time, manifest reordering
and the nine hash-derivedimageids/paths are normalized. Actual downloaded CI EPUB
passed EPUBCheck5.3.0 with zero messages. No all-link/control/device approval.

The JSON companion records all85file hashes, every page's pixel identity, exact
nine-image dimensions, actual comparison statistics and opened-image hashes.
Actual current a1d5192e run1715 is separately terminalsuccessful; this prior run
and its artifacts are not substituted for current or final source evidence.
