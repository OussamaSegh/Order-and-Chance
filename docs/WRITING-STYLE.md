# Order and Chance — series writing style

**Canonical voice for every volume.** Tool-agnostic: Cursor, Claude Code, Codex, and human editors all follow this file. Do not invent a parallel style guide.

Audience: a serious beginner who wants to become strong — curious, willing to work, not assumed to know university jargon. Prefer plain English. Never talk down.

## Voice

- Warm, plain, concrete: a friend who loves mathematics, explaining the step. Not a lecture hall, not a blog, not a chatbot. The full test is [Sound human](#sound-human).
- Short sentences by default. One idea per sentence when teaching a step.
- Prefer common words: *use*, *show*, *mean*, *because*, *so* over *employ*, *demonstrate*, *inasmuch as*.
- Second person is fine when guiding (“Now check the case \(n=2\)”). Avoid “one must”.
- No hype, no slang, no stacked exclamation marks. Wonder is allowed; cheerleading is not.
- Humour only if it clarifies; never at the reader’s expense. A light mathematical joke belongs when it teaches the point.
- First-edition copy: do not call this a revision, reconstruction, or reordering of an older edition. Do not mention companion notebooks in reader-facing text (see `AGENTS.md`).

## Sound human

The reader should hear a friend who loves mathematics and is taking the time to explain. Easy to follow. Warm, plain, concrete. A stiff textbook fails that test. A chatbot fails it too. The mathematics stays rigorous: domains, quantifiers, hypotheses, and algebra do not get softer so the sentence can sound casual.

Write the step as you would say it to someone sitting beside you with a pencil. Short sentences. A number, a picture, or a small case when the general claim would otherwise float. Use “you” when the reader should check something (“Now check the case \(n=2\)”). Use “we” when the argument is shared work. Stop before the voice turns cute or chatty for its own sake.

The step-by-step rule still wants one plain sentence on what is about to happen. That sentence names the object and the job. It does not announce the outline.

**Do.** The number of ways to choose 2 items from 5 is 10. The next argument shows why \(\binom{n}{k}=\binom{n}{n-k}\).

**Don’t.** In this section we will explore binomial coefficients and delve into their applications.

**Do.** To prove a claim for every natural number, check the first case, then show that each true case forces the next.

**Don’t.** Let’s delve into the powerful method of induction.

**Do.** Over the real numbers, \(x^2=1\) has two solutions, \(1\) and \(-1\). Over the positive reals it has one. The sentence changed. The algebra hardly did.

**Don’t.** It is important to note that the domain plays a crucial role in the solution set.

**Do.** You unpacked the definition, calculated, and packed it up again. Connectives are the words that join the next sentence.

**Don’t.** In conclusion, definitions are important building blocks on our mathematical journey.

A short map is welcome when each stop names a mathematical job: “Quantifiers say who chooses the number.” Rewrite a template summary that only restates headings, and any transition that only announces a change of topic. Put a fact or a question in its place.

**Do.** One counterexample is enough. On \(x\ge 0\), the map \(x\mapsto x-1\) is increasing and takes the value \(-1\).

**Don’t.** It might perhaps be worth considering that this could potentially suggest a possible limitation of the claim.

**Do.** An integer \(n\) is even when \(n=2k\) for some integer \(k\). For 18, the witness is \(k=9\).

**Don’t.** This robust framework seamlessly leverages the comprehensive structure of the integers.

**Do.** Now check the case \(n=2\).

**Don’t.** Okay, let’s hop into the magical little case \(n=2\)!

Hollow intensifiers and buzzwords praise the subject and do not teach it. Do not use them as filler: *robust*, *comprehensive*, *seamless*, *leverage*, *delve*, and the same empty family (*landscape*, *tapestry*, *unlock*, *journey*, *pivotal*, *underscore*, *realm*). Prefer *use*, *show*, *mean*, *because*, *so*. Any sentence that sounds like a model summarizing the section, rather than a person teaching it, gets rewritten.

The same voice covers the jacket. The back-cover blurb is the volume’s `blurb.tex`. About the Cover, and the one-line cover credit that points to it, live in `common/cover-notes.json`. Both are reader-facing. Both take this test.

A blurb tells a friend what the volume actually teaches. Name the objects. One picture or one theorem can carry a sentence.

**Do.** You will meet the intermediate value theorem, Stirling’s formula, and the law of large numbers, each rebuilt from the definitions in this volume.

**Don’t.** This comprehensive volume seamlessly unlocks the journey of mathematical thinking.

About the Cover says what the picture is, one checked fact, and why that picture belongs on this volume. The credit line can stay a single sentence. Do not invent a biography, and do not sell the drawing.

**Do.** The cover draws the Collatz tree on the integers from 2 to 8,000. The pale curve is the orbit of 27. The problem is still open, which is why it faces the chapter on language.

**Don’t.** This stunning artwork leverages a robust visualization to underscore the pivotal landscape of the Collatz conjecture.

**Voice pass.** This is the house rule for every volume, including the back cover. Before a chapter pull request, read the new prose aloud. Rewrite stock openers (“In this section we will…”, “Let’s delve into…”), the filler “It is important to note that…”, stock closers (“In conclusion…”), hollow intensifiers, stacked hedging, template summaries, buzzword salad, and transitions that announce structure. Repeat until the chapter sounds like a friend teaching. Run the same reading on `blurb.tex` and on the About the Cover copy when that text is in the assigned work. An independent review uses the same test.

## Explain everything, step by step

For every definition, theorem, and worked example:

1. **Say what we are about to do** in one plain sentence. Name the object and the job ([Sound human](#sound-human)); do not announce the outline.
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
- **EPUB figures: full text width, responsive, legible labels.** The shared pipeline turns every TikZ plate into a PNG at least 1600 pixels wide with `width: 100%`, `max-width: 100%` and `height: auto`, and no fixed pixel width. Inline formulas are images whose em width and em `vertical-align` put the TeX baseline on the text line. Do not set a pixel width on a figure. `tools/check_epub_media.py` rejects a plate or a formula that breaks this. The print page is unchanged.
- Portraits and historical photos stay credited; do not invent biography. A short historical aside belongs when the fact is checked and it helps the reader see why the idea matters.
- Do not change approved cover art unless the author asks.

## Chapter architecture

- Open with a short hook (problem, picture, or question) tied to the series thread: *order* vs *chance*.
- End with a **bridge**: what this chapter prepared, and the single next question the following chapter answers.
- Between sections: one or two bridging sentences that carry a fact or a question. No abrupt topic jumps, and no sentence whose only job is to announce the next heading ([Sound human](#sound-human)).
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
- Not a chatbot summary of the mathematics. The test is [Sound human](#sound-human).
- Not a sales pitch on the jacket. The back-cover blurb and About the Cover use that same test.
