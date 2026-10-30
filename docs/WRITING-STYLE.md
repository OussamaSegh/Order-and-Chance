# Order and Chance — series writing style

**Canonical voice for every volume.** Tool-agnostic: Cursor, Claude Code, Codex, and human editors all follow this file. Do not invent a parallel style guide.

Audience: a serious beginner who wants to become strong — curious, willing to work, not assumed to know university jargon. Prefer plain English. Never talk down.

## Voice

- Warm, clear colleague — not a lecture hall, not a blog.
- Short sentences by default. One idea per sentence when teaching a step.
- Prefer common words: *use*, *show*, *mean*, *because*, *so* over *employ*, *demonstrate*, *inasmuch as*.
- Second person is fine when guiding (“Now check the case \(n=2\)”). Avoid “one must”.
- No hype, no slang, no stacked exclamation marks. Wonder is allowed; cheerleading is not.
- Humour only if it clarifies; never at the reader’s expense. A light mathematical joke belongs when it teaches the point.
- First-edition copy: do not call this a revision, reconstruction, or reordering of an older edition. Do not mention companion notebooks in reader-facing text (see `AGENTS.md`).

## Explain everything, step by step

For every definition, theorem, and worked example:

1. **Say what we are about to do** in one plain sentence.
2. **Motivate** with a small concrete case or picture before the general statement when it helps.
3. **State** the claim cleanly (formal box as the series already uses).
4. **Prove or derive** in numbered or clearly separated steps. Never skip a “obvious” algebra step that a careful beginner might stumble on; compress only when the same move was taught earlier in *this* volume and you point back to it.
5. **Check** a tiny example or edge case.
6. **Say what it buys us** — one sentence on why the result matters for later chapters or later volumes.

If a proof is long, break it into named stages (“Setup”, “Main estimate”, “Finish”). If a step uses a prior lemma, name it and give the chapter or section.

## Illustrations

- Prefer **more figures** when a picture carries the idea faster than prose: number lines, Venn/counting diagrams, graphs of simple functions, trees for proofs by cases, geometric views of inequalities, schematic random experiments. Add the figure in the rewrite when it teaches; do not leave the idea to a later polish pass.
- Every figure needs a caption that states the takeaway, not only “Figure 3”.
- Reuse the series figure palette and interior design (`docs/design/interior.md`, design 5e). New TikZ/pgfplots should match existing stroke weights and colours.
- Portraits and historical photos stay credited; do not invent biography. A short historical aside belongs when the fact is checked and it helps the reader see why the idea matters.
- Do not change approved cover art unless the author asks.

## Chapter architecture

- Open with a short hook (problem, picture, or question) tied to the series thread: *order* vs *chance*.
- End with a **bridge**: what this chapter prepared, and the single next question the following chapter answers.
- Between sections: one or two bridging sentences; no abrupt topic jumps.
- Change chapter or section order when the new order serves clarity. Keep the planned curriculum. Reader-facing copy still must not describe the book as a rearrangement of an older edition.

## Volume-to-volume handoff

- The last chapter (or field guide) must open a door to the next volume by name and subtitle, with one concrete teaser (a problem or object the next book owns).
- Volume 1 ends by pointing to Volume 2: *The Integers: Primes, Patterns and Proofs* — primes, divisibility, and proof habits that outgrow the foundation toolkit.
- Do not spoil later volumes’ climaxes; plant motifs lightly (primes, Gaussian, zeta, walks, symmetry) when the plan says to plant them.

## Exercises

- Keep graded stars (★–★★★) and full solutions at chapter end in the series format.
- Exercise text should be as clear as the main text. Solutions teach; they do not only certify.

## Notation and consistency

- Follow the series notation sheet in `docs/plan/` and `common/` macros. Do not rename standard objects without updating the sheet.
- Cross-references use current volume numbers **1–15** (never legacy 0–14) in reader-facing text.

## What this style is not

- Not telegram fragments or bullet-only chapters.
- Not denser research prose for its own sake.
- Not a problem book with thin commentary.
- Not a change of mathematical depth: keep the content ambitious; make the *path* easy to walk.
