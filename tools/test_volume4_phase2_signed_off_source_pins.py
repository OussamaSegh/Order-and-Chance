"""Pin sole-validator mathematical signoffs to *exact* source git-blob SHAs.

A later edit to a signed-off chapter must cause these tests to fail until the
claim-level mathematical review is deliberately repeated on the new blob.
These are integrity guards, NOT theorem provers. Other chapters are not passed.
"""
from hashlib import sha1
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1] / "volume4-chance" / "chapters"
PINS = {
    "ch02-discrete.tex": {
        # Reread 2026-11-11 for the finite-additivity derivation (V4R2-02). Labels unchanged.
        "sha": "d6ddee17ed770fd8b017467160d7b36e8f3dc320",
        "claims": "thm:poissonlimit prop:fixedpoisson prop:cycles thm:coupon lem:geovar prop:couponvar prop:empty".split(),
        "exercises": "ex:records ex:fixedvar ex:quicksort ex:factorial ex:reservoir ex:prisoners ex:birthdaywait ex:twopoisson".split(),
    },
    "ch07-entropy.tex": {
        "sha": "25330e7046f0b585bef9ebffb1408bc907c109df",
        "claims": "prop:gibbs thm:aep thm:kraft thm:shannon prop:chain thm:kl thm:mutual thm:huffman".split(),
        "exercises": "ex:entropymax ex:prefixoptimal ex:entropychain ex:entropyproduct ex:ambiguouscode ex:typicalcount".split(),
    },
    "extremal.tex": {
        # Reread 2026-11-11: the appendix states that it is lettered B (V4-17).
        "sha": "9a7f9e14985567962b94061a4f4e54781e2e512f",
        "claims": "thm:turan thm:ramsey thm:schur thm:sunflower thm:ekr thm:vdw3 thm:vdw".split(),
        "exercises": "ex:r33 ex:turanedges ex:ekrsharp ex:schurtwo ex:ekrcomplement".split(),
    },
}
PROOFS = re.compile(r"\\begin\{(?:theorem|lemma|proposition)\}(?:\[[^\]]+\])?\s*\\label\{([^}]+)\}")
EXERCISES = re.compile(r"\\begin\{exercise\}(?:\[[^\]]+\])?\s*\\label\{([^}]+)\}")
HINTS = re.compile(r"\\begin\{hint\}\{([^}]+)\}")
SOLUTIONS = re.compile(r"\\begin\{solution\}\{([^}]+)\}")


class TestExactSoleValidatorSignoffPins(unittest.TestCase):
    def test_three_source_blobs_still_equal_checked_git_shas(self):
        for filename, record in PINS.items():
            with self.subTest(filename=filename):
                data = (ROOT / filename).read_bytes()
                payload = b"blob " + str(len(data)).encode("ascii") + b"\0" + data
                self.assertEqual(sha1(payload).hexdigest(), record["sha"])

    def test_all_checked_proof_label_inventories_remain_exact(self):
        for filename, record in PINS.items():
            with self.subTest(filename=filename):
                text = (ROOT / filename).read_text(encoding="utf-8")
                self.assertEqual(PROOFS.findall(text), record["claims"])

    def test_each_signed_off_exercise_still_has_exact_hint_and_solution(self):
        for filename, record in PINS.items():
            with self.subTest(filename=filename):
                text = (ROOT / filename).read_text(encoding="utf-8")
                expected = record["exercises"]
                self.assertEqual(EXERCISES.findall(text), expected)
                self.assertEqual(HINTS.findall(text), expected)
                self.assertEqual(SOLUTIONS.findall(text), expected)


if __name__ == "__main__":
    unittest.main()
