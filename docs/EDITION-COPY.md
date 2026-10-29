# First-edition publication copy

The author requested on 27 October 2026 that the books make no mention of their
accompanying Python notebooks for the first edition.

The policy covers all fifteen books, including the integrated appendices,
prefaces, captions, exercises, hints, solutions, paperback
blurbs, the default back-cover template, and KDP descriptions and keywords.
References to calculations are written as independent mathematical examples,
finite checks or numerical experiments. No theorem, proof, exercise, hint,
solution or label was removed as part of this edit.

Historical manuscript titles (including Ramanujan's Notebooks, the Scottish Book,
Collatz's handwritten records and the Escher bibliography) and the research
workshop's advice to keep a personal research journal remain mathematical content.
Repository documentation and the separate experimental files are not book copy.

The first-edition copy rule is enforced by the book build and documented in root `AGENTS.md`.

## Completed validation

- The edition-copy audit passes for all nineteen flattened books, every back-cover
  blurb and the shared fallback. Remaining uses of “notebook” refer only to
  historical handwritten mathematics or a personal research journal.
- All nineteen books converted successfully through the digital-edition parser and
  numbering filter. All nineteen generated KDP listings pass the copy audit and
  KDP description/keyword limits.
- Volumes 0, 9 and P3 each compiled through three PDF passes with zero undefined or
  multiply defined references. Extracted PDF text contains no notebook mentions.
- The theorem, proposition, lemma, exercise, hint, solution and label sequences were
  compared against the prior sources; these structures were preserved. Displayed
  equations were compared independently and were unchanged.
- All fifteen publishing regression tests, shell syntax, Python compilation and
  `git diff --check` pass.
- `tools/check_edition_copy.py` now runs before each book build. It rejects
  references to digital companions and permits the documented historical/journal
  references; both acceptance and rejection were exercised locally.

PDF page counts may change as promotional sentences disappear. The normal build
regenerates each paperback wrap from its newly built interior page count.
