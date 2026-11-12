"""Citations of the form ``Volume N, Theorem X`` must match that volume's numbers.

The walker reproduces the counters a build assigns. Volumes 3, 5, 7, 8, 10
and 12 still have citations whose kind or number does not match; those repairs
belong with the volume being cited. Every other volume is gated here, including
every citation of Volume 1 and of Volume 2.
"""

import re
import unittest

import cross_volume_citations as citations

# Cited volumes whose mismatches are still open. Drop a number when its
# citations have been repaired; the test then guards that volume too.
OPEN_CITED_VOLUMES = {3, 5, 7, 8, 10, 12}


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
            ("theorem", "7.3"): "thm:twosqn",
            ("theorem", "7.4"): "thm:foursq",
            ("theorem", "8.1"): "thm:pyth",
            ("theorem", "8.2"): "thm:fermat4",
            ("theorem", "8.6"): "thm:markov",
            ("proposition", "9.1"): "prop:cfconv",
            ("theorem", "9.2"): "thm:cfapprox",
            ("theorem", "9.6"): "thm:periodic",
            ("theorem", "9.8"): "thm:pell",
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
            "ch05-gamma.tex": ("9", "3", "8", "5", "1", "7", "6"),
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

    def test_sentence_window_does_not_adopt_the_next_local_number(self):
        text = (
            r"\tools{Volume~1, Chapter~8 (Taylor series); "
            r"Proposition~13.12 (central binomial coefficient).}"
        )
        found = citations.citations_in_text(text, "sample.tex")
        self.assertEqual([(item.volume, item.kind, item.number) for item in found],
                         [(1, "chapter", "8")])
