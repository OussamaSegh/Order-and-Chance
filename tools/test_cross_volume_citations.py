"""Citations of the form ``Volume N, Theorem X`` must match that volume's numbers.

The walker reproduces the counters a build assigns. Volumes 5, 7 and 10
still have citations whose kind or number does not match; those repairs
belong with the volume being cited. Every other volume is gated here, including
every citation of Volumes 1, 2 and 3.
"""

import re
import unittest

import cross_volume_citations as citations

# Cited volumes whose mismatches are still open. Drop a number when its
# citations have been repaired; the test then guards that volume too.
OPEN_CITED_VOLUMES = {5, 7, 10}


class CrossVolumeCitations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.books = {number: citations.number_volume(number) for number in citations.VOLUMES}
        cls.problems = citations.mismatches(cls.books)

    def test_volume1_numbers_match_the_statements_later_volumes_cite(self):
        book = self.books[1]
        anchors = {
            ("theorem", "3.10"): "thm:mvt",
            ("proposition", "3.17"): "prop:gamma",
            ("proposition", "3.18"): "prop:stirlingshape",
            ("theorem", "4.5"): "orders:thm:es",
            ("theorem", "4.6"): "orders:thm:lym",
            ("theorem", "6.4"): "thm:dalembert",
            ("proposition", "6.8"): "prop:ratroot",
            ("theorem", "6.12"): "thm:symmetric",
            ("theorem", "7.3"): "thm:det",
            ("theorem", "7.9"): "thm:spectral",
            ("theorem", "8.6"): "thm:stirlingC",
            ("theorem", "9.3"): "thm:amgm",
            ("theorem", "9.4"): "thm:cs",
            ("exercise", "1.7"): "ex:fibgcd",
            ("exercise", "4.1"): "orders:ex:klein",
            ("exercise", "6.7"): "ex:basel",
            ("exercise", "8.4"): "ex:eirr",
        }
        for key, label in anchors.items():
            statement = book.by_key[key]
            self.assertEqual(statement.label, label, key)

    def test_chaptermark_is_not_a_chapter(self):
        # Volume 12's unitary-matrix chapter sets a \\chaptermark; it must not
        # advance the chapter counter.
        book = self.books[12]
        self.assertEqual(book.by_key[("theorem", "10.10")].label, "thm:ksmoments")
        self.assertEqual(book.by_key[("proposition", "11.3")].label, "prop:cuelogcorr")
        self.assertNotIn("13", book.chapters)

    def test_volume8_numbers_after_the_rewrite(self):
        book = self.books[8]
        self.assertEqual(book.by_key[("theorem", "13.11")].label, "thm:duals")
        self.assertEqual(book.by_key[("theorem", "A.8")].label, "linear:thm:bidual")
        self.assertEqual(book.by_key[("theorem", "E.5")].label, "linear:thm:hadamard")

    def test_volume4_appendix_is_lettered_b(self):
        book = self.books[4]
        self.assertEqual(book.by_key[("theorem", "5.12")].label, "thm:buffon")
        self.assertEqual(book.by_key[("theorem", "B.5")].label, "thm:ekr")
        self.assertIn("B", book.chapters)

    def test_resolved_volumes_have_no_mismatch(self):
        unexpected = []
        for problem in self.problems:
            cited = int(problem.split("Volume ", 1)[1].split(" ", 1)[0])
            if cited not in OPEN_CITED_VOLUMES:
                unexpected.append(problem)
        self.assertEqual(unexpected, [])

    def test_volume1_prints_the_language_chapter_as_zero(self):
        book = self.books[1]
        self.assertEqual(book.chapters, {str(number) for number in range(11)})

    def test_volume2_numbers_match_the_printed_statements(self):
        book = self.books[2]
        anchors = {
            ("theorem", "1.5"): "thm:gauss",
            ("theorem", "1.6"): "thm:fta",
            ("theorem", "3.5"): "thm:crt",
            ("theorem", "3.8"): "thm:hensel",
            ("theorem", "4.4"): "thm:mobius",
            ("theorem", "4.5"): "thm:perfect",
            ("theorem", "4.6"): "thm:hyperbola",
            ("proposition", "4.3"): "prop:conv",
            ("theorem", "5.3"): "thm:cyclic",
            ("theorem", "5.5"): "thm:cyclicn",
            ("exercise", "5.7"): "ex:cyclotomic",
            ("theorem", "6.5"): "thm:qr",
            ("corollary", "6.4"): "cor:two",
            ("exercise", "6.7"): "ex:gausssum",
            ("theorem", "2.1"): "thm:euclid-primes",
            ("exercise", "2.9"): "ex:t1-factorial-new-prime",
            ("theorem", "7.3"): "thm:twosqn",
            ("theorem", "7.4"): "thm:foursq",
            ("theorem", "7.5"): "thm:circle",
            ("theorem", "8.1"): "thm:pyth",
            ("theorem", "8.2"): "thm:fermat4",
            ("theorem", "8.6"): "thm:markov",
            ("proposition", "9.1"): "prop:cfconv",
            ("theorem", "9.2"): "thm:cfapprox",
            ("theorem", "9.6"): "thm:periodic",
            ("theorem", "9.8"): "thm:pell",
            ("theorem", "10.3"): "thm:ufd",
            ("theorem", "10.5"): "thm:gaussprimes",
            ("theorem", "10.9"): "thm:flt3",
            ("exercise", "1.3"): "ex:zeros",
            ("exercise", "4.7"): "ex:primitive",
            ("exercise", "4.8"): "ex:coprimeprob",
        }
        self.assertEqual(book.chapters, {str(number) for number in range(1, 12)})
        for key, label in anchors.items():
            self.assertEqual(book.by_key[key].label, label, key)

    def test_swapped_volume2_chapter_is_rejected(self):
        # Filename order calls reciprocity Chapter 5 and continued fractions Chapter 8.
        swapped = r"quadratic reciprocity, Volume~2, Chapter~5"
        printed = swapped.replace("Chapter~5", "Chapter~6")
        self.assertTrue(citations.volume2_subject_mismatches(swapped))
        self.assertEqual(citations.volume2_subject_mismatches(printed), [])
        old_pell = r"continued fraction of $\sqrt d$, Volume~2, Theorem~8.6"
        self.assertTrue(citations.volume2_subject_mismatches(old_pell))
        self.assertEqual(
            citations.volume2_subject_mismatches(
                old_pell.replace("Theorem~8.6", "Theorem~9.6")),
            [],
        )
        gauss = r"the Gauss sum satisfies $g^2=q^*$ (Volume~2, Exercise~5.7)"
        self.assertTrue(citations.volume2_subject_mismatches(gauss))
        self.assertEqual(
            citations.volume2_subject_mismatches(
                gauss.replace("Exercise~5.7", "Exercise~6.7")),
            [],
        )

    def test_volume2_pointers_name_the_stated_fact(self):
        """A nearby number can exist and still describe a different theorem."""
        root = citations.ROOT
        bezout = (root / "volume13-arithmetic/chapters/ch12-ideals-quadratic.tex").read_text(encoding="utf-8")
        self.assertIn(
            r"the B\'ezout property in a Euclidean domain, proved in Volume~2, Theorem~10.3",
            bezout,
        )
        self.assertNotIn("Theorem~1.4", bezout)
        factorial = (root / "volume15-order-and-chance/chapters/ch09-lean.tex").read_text(encoding="utf-8")
        self.assertIn(r"Volume~2, Exercise~2.9: a prime factor of $n!+1$", factorial)
        self.assertNotIn("Theorem~2.1", factorial)
        disc = (root / "volume6-crossroads/chapters/ch05-pnt.tex").read_text(encoding="utf-8")
        self.assertIn(r"$\sim\pi x$ (Volume~2, Theorem~7.5, or a direct count)", disc)
        ball = (root / "volume7-spaces/chapters/ch02-metric.tex").read_text(encoding="utf-8")
        self.assertIn("The closed unit ball, and its identification with the compatible residue sequences, are built in this chapter.", ball)
        self.assertNotIn("names this ball", ball)
        triangle = (root / "volume13-arithmetic/chapters/ch12-elliptic.tex").read_text(encoding="utf-8")
        self.assertIn(r"$x^4+y^4=z^2$ has no positive integer solution (Volume~2, Theorem~8.2)", triangle)
        self.assertIn(r"Proposition~\ref{prop:congruent}", triangle)
        self.assertNotIn("square area. Which numbers", triangle)
        signed = (root / "volume5-calculation/chapters/ch08-transform.tex").read_text(encoding="utf-8")
        self.assertIn(r"Volume~2, Exercise~6.7, gives $G(p)^2=", signed)
        index = (root / "volume2-integers/chapters/index.tex").read_text(encoding="utf-8")
        self.assertNotIn("print PDF", index)
        self.assertIn(r"\ocindexpage{sym:divides}", index)
        self.assertIn(r"\ocindexpage{sym:gcd}", index)
        self.assertIn(r"\ocindexpage{sym:lcm}", index)
        self.assertIn(r"\ocindexpage{ex:t1-factorial-new-prime}", index)

    def test_volume3_pointers_name_the_stated_fact(self):
        """Exercise 10.8 is Cardano. The cyclotomic isomorphism is Exercise 10.1."""
        root = citations.ROOT
        cyclo = (root / "volume13-arithmetic/chapters/ch05-cyclotomic.tex").read_text(encoding="utf-8")
        self.assertIn("Volume~3, Exercise~10.1", cyclo)
        self.assertNotIn("Exercise~10.8", cyclo)
        ideals = (root / "volume13-arithmetic/chapters/ch02-ideals.tex").read_text(encoding="utf-8")
        self.assertIn("Volume~3, Theorem~10.6 and Exercise~10.1", ideals)
        curves = (root / "volume13-arithmetic/chapters/ch11-curves.tex").read_text(encoding="utf-8")
        self.assertIn("Volume~3, Theorem~6.18", curves)
        self.assertIn("Volume~3, Proposition~6.17", curves)
        additive = (root / "volume14-primes/chapters/ch11-additive.tex").read_text(encoding="utf-8")
        self.assertIn("Volume~3, Theorem~C.12", additive)
        cubes = (root / "volume15-order-and-chance/chapters/ch08-heuristics.tex").read_text(encoding="utf-8")
        self.assertIn("Volume~3, Theorem~C.12", cubes)
        lie = (root / "volume9-shapes/chapters/ch07-liegroups.tex").read_text(encoding="utf-8")
        self.assertIn("Volume~3, Lemma~12.3", lie)
        self.assertNotIn("as in Volume~3", lie)
        quadrics = (root / "volume9-shapes/chapters/geometry-ch06-quadrics.tex").read_text(encoding="utf-8")
        self.assertIn("Volume~1, Theorem~7.9", quadrics)
        self.assertIn("Volume~1, Theorem~7.10", quadrics)
        self.assertNotIn("Volume~3, Chapter~2", quadrics)
        primitive = (root / "volume13-arithmetic/chapters/ch01-number-fields.tex").read_text(encoding="utf-8")
        self.assertIn("Volume~3, Theorem~8.20", primitive)
        gauss_sum = (root / "volume6-crossroads/chapters/ch12-modular.tex").read_text(encoding="utf-8")
        self.assertIn("Vandermonde determinants (Volume~1, Proposition~7.4)", gauss_sum)
        self.assertIn("eigenvalues and traces (Volume~1, Chapter~7)", gauss_sum)
        self.assertNotIn("Vandermonde determinants (Volume~3)", gauss_sum)
        trig = (root / "volume8-analysis/chapters/linear-ch01-duality.tex").read_text(encoding="utf-8")
        self.assertIn("orthonormal, hence independent; Volume~5, Chapter~6", trig)
        self.assertNotIn("Volume~3 or Volume~4", trig)
        moments = (root / "volume15-order-and-chance/chapters/ra-symmoments.tex").read_text(encoding="utf-8")
        self.assertIn("Volume~3, Corollary~7.7", moments)
        bad = "the Vandermonde determinant (Volume~3)"
        self.assertTrue(citations.volume3_misplaced_subject(bad))
        self.assertEqual(
            citations.volume3_misplaced_subject(
                bad.replace("Volume~3", "Volume~1, Proposition~7.4")),
            [],
        )

    def test_chapter_zero_offset_rejects_a_shifted_gloss(self):
        shifted = (
            "two polynomials that agree at infinitely many points are equal, "
            r"Volume~1, Chapter~7"
        )
        printed = shifted.replace("Chapter~7", "Chapter~6")
        self.assertTrue(citations.volume1_chapter_gloss_mismatches(shifted))
        self.assertEqual(citations.volume1_chapter_gloss_mismatches(printed), [])
        forbidden = r"Volume~1, Chapter~8 (derivatives, $\arcsin$)"
        self.assertTrue(citations.volume1_chapter_gloss_mismatches(forbidden))

    def test_volume1_chapter_glosses_match_the_printed_chapters(self):
        self.assertEqual(citations.gloss_mismatches(), [])

    def test_volume5_volume1_chapters_are_the_printed_numbers(self):
        # Counting Volume 1's language chapter as Chapter 1 shifts every one
        # of these. The gloss check catches a named subject; this pins the rest.
        root = citations.ROOT / "volume5-calculation" / "chapters"
        expected = {
            "ch01-finite.tex": ("6", "2"),
            "ch02-generating.tex": ("2", "3", "3", "6", "8", "3", "8"),
            "ch04-integrals.tex": ("3", "8", "5", "3", "3", "3", "3"),
            "ch05-gamma.tex": ("9", "3", "8", "8", "5", "1", "7", "6"),
            "ch06-fourier.tex": ("9", "8", "5", "5"),
            "ch07-fft.tex": ("5", "5", "5", "5", "5", "7", "5", "5", "7", "5", "7", "7"),
            "ch09-complex.tex": ("3", "5", "6"),
            "ch10-zeta.tex": ("3", "3"),
            "ch11-asymptotics.tex": ("8", "3", "8", "3", "8"),
            "ch12-agm.tex": (
                "5", "5", "7", "7", "8", "7", "6", "8", "8", "8",
                "7", "6", "7", "5", "6", "5", "8", "3", "8", "3",
            ),
        }
        for name, chapters in expected.items():
            text = (root / name).read_text(encoding="utf-8")
            found = []
            for match in re.finditer(r"Volume~1(?![0-9])", text):
                window = text[match.end():match.end() + 40]
                chapter = re.match(
                    r",\s*Chapters?~(\d+)(?:\s+and~?(\d+))?", window)
                if chapter is None:
                    chapter = re.match(r",\s*\nChapter~(\d+)", text[match.end():match.end() + 20])
                    if chapter:
                        found.append(chapter.group(1))
                    continue
                found.append(chapter.group(1))
                if chapter.group(2):
                    found.append(chapter.group(2))
                else:
                    rest = text[match.end():match.end() + 220]
                    extra = re.search(r" and Chapter~(\d+)", rest)
                    if extra:
                        found.append(extra.group(1))
            self.assertEqual(tuple(found), chapters, name)
        gamma = (root / "ch05-gamma.tex").read_text(encoding="utf-8")
        self.assertIn(
            r"(Chapter~8; the shape with an unspecified constant is in Chapter~3)",
            gamma,
        )

    def test_volume4_subject_rejects_a_real_number_aimed_at_the_wrong_fact(self):
        diffusion = r"diffusion on the circle (Volume~4, Chapter~8)"
        self.assertTrue(citations.volume4_subject_mismatches(diffusion))
        self.assertEqual(
            citations.volume4_subject_mismatches(
                r"After $t$ steps the modes have been multiplied by $\cos^t\frac\pi n$."
            ),
            [],
        )
        cone = r"Poincaré's cone condition (keeping the promise of Volume~4, Chapter~8)"
        self.assertTrue(citations.volume4_subject_mismatches(cone))
        chain = r"Volume~4, Proposition~8.4, whose proof applies to any Markov chain"
        self.assertTrue(citations.volume4_subject_mismatches(chain))
        fixed = (
            r"By inclusion and exclusion (Volume~4, Proposition~2.3), "
            r"$P(F_n=k)=\frac1{k!}\sum$"
        )
        self.assertTrue(citations.volume4_subject_mismatches(fixed))
        counted = (
            r"The proof of Volume~4, Proposition~2.3 writes "
            r"$P(F_n=k)=\frac1{k!}\cdot\frac{D_{n-k}}{(n-k)!}$"
        )
        self.assertEqual(citations.volume4_subject_mismatches(counted), [])
        variance = r"Volume~4, Chapter~5 (variance of sums)"
        self.assertTrue(citations.volume4_subject_mismatches(variance))
        self.assertEqual(
            citations.volume4_subject_mismatches(
                variance.replace("Chapter~5", "Chapter~2")),
            [],
        )
        duration = (
            r"Volume~4, Theorem~8.2 gave the same answers, "
            r"$\frac a{a+b}$ and $ab$ steps."
        )
        self.assertTrue(citations.volume4_subject_mismatches(duration))
        split = (
            r"Volume~4, Theorem~8.2 gives the exit probability $\frac a{a+b}$, "
            r"and Volume~4, Proposition~8.3 gives the mean duration $ab$."
        )
        self.assertEqual(citations.volume4_subject_mismatches(split), [])
        one_card = (
            r"Volume~4, Proposition~9.11 (the covariances "
            r"$(1-\frac2n)^t-(1-\frac1n)^{2t}$ are negative)"
        )
        self.assertTrue(citations.volume4_subject_mismatches(one_card))
        two_cards = (
            r"$(1-\frac2n)^t$ is this model's covariance. "
            r"Volume~4, Proposition~9.11 chooses two cards, so the exponent is $2t$."
        )
        self.assertEqual(citations.volume4_subject_mismatches(two_cards), [])

    def test_volume4_pointers_name_the_stated_fact(self):
        root = citations.ROOT
        exit_time = (root / "volume12-random-motion/chapters/ch03-martingales.tex").read_text(encoding="utf-8")
        self.assertIn(r"Volume~4, Theorem~8.2 gives the exit probability", exit_time)
        self.assertIn(r"Volume~4, Proposition~8.3 gives the mean duration", exit_time)
        self.assertNotIn("ab$ steps", exit_time)
        projects = (root / "volume15-order-and-chance/chapters/ch12-projects.tex").read_text(encoding="utf-8")
        self.assertIn("chooses two cards at a step", projects)
        self.assertNotIn(r"Proposition~9.11 (the covariances", projects)
        fixed_points = (root / "volume11-randomness/chapters/ch13-harder.tex").read_text(encoding="utf-8")
        self.assertIn(r"Volume~1, Chapter~2, writes $\frac{D_r}{r!}", fixed_points)
        self.assertNotIn("inclusion and exclusion (Volume~4, Proposition~2.3)", fixed_points)
        self.assertIn("Volume~4, Chapter~2 (covariance)", fixed_points)
        self.assertNotIn("Volume~4, Chapter~5 (variance of sums)", fixed_points)
        independence = (root / "volume11-randomness/chapters/ch01-zero-one.tex").read_text(encoding="utf-8")
        self.assertIn(r"Independence} (Volume~4, Chapter~4", independence)
        walks = (root / "volume5-calculation/chapters/ch07-fft.tex").read_text(encoding="utf-8")
        self.assertNotIn("diffusion on the circle (Volume~4, Chapter~8)", walks)
        self.assertIn(r"e^{i\pi j/n}\cos\frac{\pi j}n", walks)
        self.assertNotIn("two neighbours", walks)
        cycles = (root / "volume11-randomness/chapters/ch12-permutations.tex").read_text(encoding="utf-8")
        self.assertIn(r"Volume~4, Proposition~6.13 writes the number of cycles", cycles)
        self.assertIn(r"Proposition~\ref{prop:firstcycle}", cycles)
        self.assertNotIn("canonical cycle notation, each cycle starting", cycles)
        analysis = (root / "volume12-random-motion/chapters/ch05-analysis.tex").read_text(encoding="utf-8")
        self.assertIn("Volume~4, Proposition~8.7", analysis)
        self.assertIn("The cone condition is proved in this chapter.", analysis)
        self.assertNotIn("cone condition (the finite-graph", analysis)
        self.assertNotIn("promise of Volume~4, Chapter~8", analysis)
        index = (root / "volume4-chance/chapters/index.tex").read_text(encoding="utf-8")
        book = self.books[4]
        # The printed number beside each index label. def:charfn is located as
        # "before Theorem 6.8" and is checked only for existence.
        expected = {
            "thm:ballot": "1.7",
            "thm:bayerdiaconis": "9.9",
            "thm:bc": "4.4",
            "thm:boxmuller": "5.10",
            "def:bm": "12.1",
            "thm:levy": "12.4",
            "thm:reflection": "12.12",
            "thm:buffon": "5.12",
            "cor:clt": "6.11",
            "thm:lindeberg": "6.10",
            "thm:inversion": "6.8",
            "thm:coupon": "2.5",
            "prop:gibbs": "7.1",
            "thm:shannon": "7.4",
            "thm:huffman": "7.8",
            "thm:ekr": "B.5",
            "thm:extinction": "3.8",
            "thm:gc": "6.5",
            "thm:hoeffding": "4.2",
            "thm:local": "6.12",
            "def:mart": "11.2",
            "thm:os": "11.4",
            "thm:os2": "11.5",
            "thm:L2conv": "11.12",
            "prop:memoryless": "10.1",
            "def:outer": "1.3",
            "thm:poissonlimit": "2.1",
            "def:pp": "10.3",
            "thm:polya": "8.5",
            "thm:polyaurn": "11.13",
            "thm:erdos": "13.1",
            "thm:lll": "13.3",
            "thm:ramsey": "B.2",
            "thm:vdw": "B.7",
            "thm:subcrit": "14.1",
            "thm:triangles": "14.2",
            "thm:sllnbound": "4.5",
            "thm:slln4": "6.4",
            "thm:top": "9.6",
            "thm:turan": "B.1",
            "thm:weierstrass": "4.6",
        }
        for label, number in expected.items():
            self.assertIn(f"\\ocindexpage{{{label}}}", index)
            owner = next(item for item in book.statements if item.label == label)
            self.assertEqual(owner.number, number, label)
        self.assertIn("\\ocindexpage{def:charfn}", index)
        characteristic = (root / "volume4-chance/chapters/ch06-clt.tex").read_text(encoding="utf-8")
        self.assertIn(r"\label{def:charfn}", characteristic)

    def test_sentence_window_does_not_adopt_the_next_local_number(self):
        text = (
            r"\tools{Volume~1, Chapter~8 (Taylor series); "
            r"Proposition~13.12 (central binomial coefficient).}"
        )
        found = citations.citations_in_text(text, "sample.tex")
        self.assertEqual([(item.volume, item.kind, item.number) for item in found],
                         [(1, "chapter", "8")])
