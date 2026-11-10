"""Structural regression checks for the approved Volume 4 reading route.

This is a static, source-level check, not TeX compilation or a mathematics review.

Run: python3 -m unittest discover -s tools -p test_volume4_route.py
"""

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VOL = ROOT / "volume4-chance"
CHAPTERS = VOL / "chapters"

APPROVED_CHAPTERS = (
    "ch01-counting",
    "ch02-discrete",
    "ch03-generating",
    "ch04-inequalities",
    "ch05-continuous",
    "ch06-clt",
    "ch07-entropy",
    "ch07-walks",
    "ch08-markov",
    "ch09-poisson",
    "ch10-martingales",
    "ch11-brownian",
    "ch12-method",
    "ch14-graphs",
)

INPUT = re.compile(r"\\input\{([^{}]+)\}")
LABEL = re.compile(r"\\label\{([^{}]+)\}")
REF = re.compile(r"\\(?:ref|eqref|pageref|autoref)\{([^{}]+)\}")
FIG = re.compile(r"\\fig\{([^{}]+)\}")
EXERCISE = re.compile(
    r"\\begin\{exercise\}(?:\[[^\]]*\])?\s*\\label\{([^{}]+)\}"
)
HINT = re.compile(r"\\begin\{hint\}\{([^{}]+)\}")
SOLUTION = re.compile(r"\\begin\{solution\}\{([^{}]+)\}")


def manuscript():
    """Follow only authored TeX inputs, excluding comments and the generated preamble."""
    source = (VOL / "main.tex").read_text(encoding="utf-8")
    source = "\n".join(line.split("%", 1)[0] for line in source.splitlines())
    included = []
    visited = set()

    def descend(file):
        if file in visited:
            raise AssertionError(f"duplicate or cyclic input: {file}")
        visited.add(file)
        if not file.is_file():
            raise AssertionError(f"missing input: {file}")
        text = file.read_text(encoding="utf-8")
        lines = "\n".join(line.split("%", 1)[0] for line in text.splitlines())
        included.append((file, lines))
        for value in INPUT.findall(lines):
            # Only inspect local chapter-to-chapter references, not common/ imports.
            sub = (VOL / value).with_suffix(".tex")
            descend(sub)

    for name in INPUT.findall(source):
        if name.startswith("chapters/") or name == "about-the-cover":
            descend((VOL / name).with_suffix(".tex"))
    return source, included


class TestVolume4Route(unittest.TestCase):
    def test_approved_four_part_fourteen_chapter_path_and_appendix_b(self):
        main, files = manuscript()
        chapter_names = re.findall(r"\\input\{chapters/([^{}]+)\}", main)
        self.assertEqual(
            tuple(name for name in chapter_names if name not in ("preface", "extremal")),
            APPROVED_CHAPTERS,
        )
        self.assertEqual(len(re.findall(r"\\part\{", main)), 4)
        self.assertEqual(sum(bool(re.search(r"\\chapter\{", text)) for _, text in files), 15)
        appendix = main.index(r"\appendix")
        self.assertLess(appendix, main.index(r"\setcounter{chapter}{1}"))
        self.assertLess(main.index(r"\setcounter{chapter}{1}"), main.index(r"\input{chapters/extremal}"))
        paths = {path.name for path, _ in files}
        self.assertIn("ch05-geometric.tex", paths)  # Included by Chapter 5.
        self.assertIn("extremal.tex", paths)

    def test_local_labels_and_references_resolve_uniquely(self):
        _, files = manuscript()
        labels = {}
        refs = []
        for path, text in files:
            for label in LABEL.findall(text):
                if label in labels:
                    self.fail(f"duplicate label {label!r} in {path} and {labels[label]}")
                labels[label] = str(path)
            for ref in REF.findall(text):
                refs.append((path, ref))
        for path, ref in refs:
            with self.subTest(file=path.name, ref=ref):
                self.assertIn(ref, labels, f"missing reference {ref} in {path}")
        self.assertGreaterEqual(len(labels), 290)  # Pin against accidental deletion.

    def test_all_exercises_have_exactly_one_matching_hint_and_solution(self):
        _, files = manuscript()
        all_exercises = []
        for path, text in files:
            ex = EXERCISE.findall(text)
            hints = HINT.findall(text)
            solutions = SOLUTION.findall(text)
            with self.subTest(path=path.name):
                self.assertEqual(ex, hints, "exercise/hint mismatch")
                self.assertEqual(ex, solutions, "exercise/solution mismatch")
            all_exercises.extend(ex)
        self.assertEqual(len(all_exercises), len(set(all_exercises)))
        self.assertGreaterEqual(len(all_exercises), 107)

    def test_dependency_register_uses_current_printed_exercise_numbers(self):
        """Catch stale citation slots when a historical source filename is misleading."""
        register = (ROOT / "docs/plan/volume4-prerequisites.md").read_text(
            encoding="utf-8"
        )
        actual = {}
        for chapter_number, name in enumerate(APPROVED_CHAPTERS, start=1):
            source = (CHAPTERS / (name + ".tex")).read_text(encoding="utf-8")
            for exercise_number, label in enumerate(EXERCISE.findall(source), start=1):
                actual[label] = f"{chapter_number}.{exercise_number}"
        documented = dict(
            (label, slot)
            for slot, label in re.findall(
                r"^\|\s*(?:\*\*)?(\d+\.\d+)(?:\*\*)?\s*\|\s*\x60(ex:[^\x60]+)\x60",
                register,
                flags=re.MULTILINE,
            )
        )
        expected = {
            "ex:catalan", "ex:prisoners", "ex:binseries", "ex:cantor",
            "ex:slutsky", "ex:cyclesclt", "ex:electric", "ex:toptorandom",
            "ex:risingmean", "ex:zeros", "ex:crossing",
        }
        self.assertTrue(expected.issubset(documented.keys()))
        for label, slot in documented.items():
            with self.subTest(exercise=label):
                self.assertEqual(actual.get(label), slot)

    def test_every_referenced_figure_source_exists(self):
        _, files = manuscript()
        names = set()
        for _, text in files:
            names.update(FIG.findall(text))
        # Phase 3 inventory: exactly these plates are called by \fig. Unused
        # files in figures/ are not part of the book.
        self.assertEqual(
            names,
            {
                "appb-turan-balance",
                "ch01-ballot",
                "ch01-bertrand",
                "ch01-buffon",
                "ch01-digits",
                "ch01-tuesday",
                "ch02-couponstages",
                "ch02-cycles",
                "ch02-lawmap",
                "ch02-poissonbars",
                "ch03-cobweb",
                "ch03-contour",
                "ch03-familytree",
                "ch03-lawpoly",
                "ch04-bernstein",
                "ch04-chernoff",
                "ch04-squaregaps",
                "ch05-cantor",
                "ch05-densityarea",
                "ch05-inversecdf",
                "ch05-polar",
                "ch06-dice-zscore",
                "ch06-lindeberg",
                "ch06-sums",
                "ch07-prefixtree",
                "ch07-typicalcoin",
                "ch08-chain",
                "ch08-reflectstep",
                "ch08-riffle",
                "ch08-ruinprob",
                "ch09-commonjump",
                "ch09-inspection",
                "ch10-poissonclock",
                "ch10-polya",
                "ch10-queue-rates",
                "ch10-upcross",
                "ch12-ramsey",
                "ch12-reflection",
                "ch14-exploration",
                "extremal-ch08-focusing",
                "preface-tails",
            },
        )
        for name in names:
            with self.subTest(figure=name):
                self.assertTrue(
                    (VOL / "figures" / (name + ".tex")).is_file(),
                    f"missing figure source for {name}",
                )


if __name__ == "__main__":
    unittest.main()
