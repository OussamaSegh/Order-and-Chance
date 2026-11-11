"""Citations of the form ``Volume N, Theorem X`` must match that volume's numbers.

The walker reproduces the counters a build assigns. Volumes 2, 3, 5, 7, 8, 10
and 12 still have citations whose kind or number does not match; those repairs
belong with the volume being cited. Every other volume is gated here, including
every citation of Volume 1.
"""

import unittest

import cross_volume_citations as citations

# Cited volumes whose mismatches are still open. Drop a number when its
# citations have been repaired; the test then guards that volume too.
OPEN_CITED_VOLUMES = {2, 3, 5, 7, 8, 10, 12}


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

    def test_sentence_window_does_not_adopt_the_next_local_number(self):
        text = (
            r"\tools{Volume~1, Chapter~8 (Taylor series); "
            r"Proposition~13.12 (central binomial coefficient).}"
        )
        found = citations.citations_in_text(text, "sample.tex")
        self.assertEqual([(item.volume, item.kind, item.number) for item in found],
                         [(1, "chapter", "8")])
