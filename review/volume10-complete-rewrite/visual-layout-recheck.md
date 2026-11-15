# Focused visual-layout repair review

Reviewer: `independent_review`, separate from the diagram repair author.
Scope: three newly added illustrations only. No original baseline figure,
caption or diagram source is changed. No manuscript edits, builds or commits
were performed by this reviewer.

Read the complete old and replacement sources and their diffs. Opened and visually
inspected the actual standalone PNG previews compiled by the parent at
`/workspace/v10-inspection/fixed-figures/`. These are rendered previews, not an
assumption from source coordinates. Their final in-book scale and EPUB raster
rendering must still be inspected after the parent copies the accepted bytes
and reruns the required builds.

**Disposition: all three replacement source/preview pairs pass this focused
mathematical and visual review.** Labels are separated and readable in the
previews; no mathematical conclusion, value or orientation changes.

## Diagram judgements

- `v10-new-ch01-yoneda.tex`: all four square objects and arrows are unchanged:
  Hom(A,A) to Hom(A,B) by h^A(f), F(A) to F(B) by F(f), and the vertical alpha
  components. The formerly floating element labels are expressed centrally as
  alpha_A(id_A)=x and alpha_B(f)=F(f)(x), the same evaluations represented by the
  original labels. Neither identity collides with the object names or arrows.
  The arrow orientations and variance agree with Yoneda's naturality proof.
- `v10-new-ch04-staircase.tex`: only the legend position changes, moving it above
  the lattice. The marked excluded monomials still have exponent sum at least
  two, exactly the ideal (X^2,XY,Y^2); the three standard monomials 1,X,Y, axis
  directions, staircase and generator labels are unchanged. The legend is clear
  of all crosses and does not conceal a data point.
- `v10-new-ch10-hookprob.tex`: all four transition arrows are unchanged. From A,
  each of B,C,D has probability 1/3, and B goes to C with probability 1. The
  probabilities have been moved off overlapping arrow labels to nearby free
  space, preserving their colours and association with the arrows. C and D
  remain the two corners. With uniform start on A,B,C,D, the displayed
  Pr(C|A)=2/3, Pr(D|A)=1/3 and totals Pr(C)=2/3, Pr(D)=1/3 are correct.
  The separate labels are unambiguous in the rendered preview.

## Exact accepted inputs and inspected previews

The parent must copy these replacement bytes without modification to the named
repository destinations. The temporary path is an input to this focused review,
not a published artifact.

| Repository destination | Accepted temporary source | SHA-256 |
| --- | --- | --- |
| `volume10-abstraction/figures/v10-new-ch01-yoneda.tex` | `/tmp/v10-layout/v10-new-ch01-yoneda.tex` | `fb844d1b00be2b595a3d5afcc8ad2383949c3ba01eef76568b6ed295ba96825c` |
| `volume10-abstraction/figures/v10-new-ch04-staircase.tex` | `/tmp/v10-layout/v10-new-ch04-staircase.tex` | `54ee3cb7be57e1f0686381e33b775f8e03eb8ae8844e342b9cda67188acd320c` |
| `volume10-abstraction/figures/v10-new-ch10-hookprob.tex` | `/tmp/v10-layout/v10-new-ch10-hookprob.tex` | `a7a181aa88cce991862346e1b22b00a2932a7bfc2475b4a87b53ea40cc772a20` |

| Inspected preview | Pixel dimensions | SHA-256 |
| --- | --- | --- |
| `/workspace/v10-inspection/fixed-figures/v10-new-ch01-yoneda.png` | 470 x 220 | `18c64a54272e5cbc7228bc6f1bfd39da782eef58ae4251a2749260098cbadceb` |
| `/workspace/v10-inspection/fixed-figures/v10-new-ch04-staircase.png` | 452 x 330 | `966680710714c6d33f93918431563bdedf3006110b614964d92704bde594808b` |
| `/workspace/v10-inspection/fixed-figures/v10-new-ch10-hookprob.png` | 553 x 248 | `4d6ca93742e6b508a33f4a30e42de80625fb201d6078d1e008da9f63428d8a79` |

The mathematical source acceptance in the chapter reports remains valid, with
these three reviewed new-figure hash replacements. Chapter prose, original
statement/exercise/figure numbers, exercise content, original figure blocks and
cover artwork are unchanged by this repair. This report does not claim that the
parent's final PDF/full builds, print export, EPUB or published-artifact reruns
have already passed.

The coordinating writer copied these exact accepted replacement bytes into the
three repository paths. The initial complete full build on book sources 8506bdfa
exited 0 at 279 print pages with 34 EPUB plates; it is historical because its
three diagram labels still needed this visual repair. Both final builds are rerun.
