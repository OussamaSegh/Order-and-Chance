"""Lock Chapter 5 (including geometric section), 13 and 14 mathematical signoffs.

Git object SHA-1 checks ensure a source change invalidates a previous
mathematical review rather than silently retaining a PASS. These tests
verify identity and completeness, not mathematical truth.
"""
import hashlib
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1] / "volume4-chance" / "chapters"
SOURCES = {
    "ch05-continuous.tex": (
        # Reread 2026-11-11 for the generalised-inverse identity and the
        # Box--Muller grid cover (V4-21, V4-03). Labels unchanged.
        "08a0b40df7de40abf6ebb36acc14f88cfcced266",
        "prop:densitymean prop:gausstail prop:fubini prop:polar prop:manyuniforms prop:orderpair prop:inverse thm:dct thm:boxmuller",
        "ex:counter ex:densityunique ex:tail ex:cauchy ex:gamma ex:order ex:cantor ex:usquare ex:radius",
    ),
    "ch05-geometric.tex": (
        "2bc6858a1cb598473be2f233ae5ed6b05ff0e93e",
        "thm:bertrand thm:buffon",
        "",
    ),
    "ch12-method.tex": (
        "7bb8f4a676a46524817beb217d04f18ad6317a21",
        "thm:erdos thm:alter thm:lll prop:second prop:euler prop:crossing",
        "ex:carowei ex:tournament ex:sumfree ex:crossing ex:propertyb ex:localcolour",
    ),
    "ch14-graphs.tex": (
        "a494b82eee49bc1ed43d43b9b74894ed821706d4",
        "thm:subcrit thm:triangles",
        "ex:connectivity ex:giant ex:trianglecount ex:susceptibility ex:criticalisolated ex:trianglesecond",
    ),
}
PROOFS = re.compile(r"\\begin\{(?:theorem|lemma|proposition)\}(?:\[[^\]]+\])?\s*\\label\{([^}]+)\}")
EXERCISES = re.compile(r"\\begin\{exercise\}(?:\[[^\]]+\])?\s*\\label\{([^}]+)\}")
HINTS = re.compile(r"\\begin\{hint\}\{([^}]+)\}")
SOLUTIONS = re.compile(r"\\begin\{solution\}\{([^}]+)\}")


class TestSoleValidatorCh5Ch13Ch14SignoffSourceIdentity(unittest.TestCase):
    def test_git_blob_shas_match_mathematically_checked_source(self):
        for file, (sha, _, _) in SOURCES.items():
            with self.subTest(file=file):
                data = (ROOT / file).read_bytes()
                obj = b"blob " + str(len(data)).encode() + b"\0" + data
                self.assertEqual(hashlib.sha1(obj).hexdigest(), sha)

    def test_proofs_and_all_exercise_triples_complete(self):
        for file, (_, proof_labels, exercise_labels) in SOURCES.items():
            with self.subTest(file=file):
                src = (ROOT / file).read_text(encoding="utf8")
                self.assertEqual(PROOFS.findall(src), proof_labels.split())
                for regex in (EXERCISES, HINTS, SOLUTIONS):
                    self.assertEqual(regex.findall(src), exercise_labels.split())

    def test_ch5_geometry_is_actually_part_of_the_printed_chapter(self):
        text = (ROOT / "ch05-continuous.tex").read_text(encoding="utf8")
        self.assertIn(r"\input{chapters/ch05-geometric}", text)


if __name__ == "__main__":
    unittest.main()
