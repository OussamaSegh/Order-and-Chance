"""The Volume 4 preface must match the citations the proofs actually use."""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFACE = ROOT / "volume4-chance" / "chapters" / "preface.tex"
CHAPTERS = ROOT / "volume4-chance" / "chapters"


class TestVolume4PrefacePrerequisites(unittest.TestCase):
    def test_proof_prerequisites_are_volume_1(self):
        text = PREFACE.read_text(encoding="utf-8")
        self.assertIn(
            "The prerequisites for the proofs are high-school mathematics and Volume~1.",
            text,
        )
        self.assertIn("no proof in this book cites a theorem from either volume", text)
        self.assertNotIn("Volumes~1--3.", text)

    def test_chapter_bodies_do_not_cite_volumes_2_or_3(self):
        for path in CHAPTERS.glob("*.tex"):
            if path.name == "preface.tex":
                continue
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("Volume~2", text, path.name)
            self.assertNotIn("Volume~3", text, path.name)


if __name__ == "__main__":
    unittest.main()
