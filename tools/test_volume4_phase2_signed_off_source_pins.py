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
        # 2026-11-11: pb:goodman and pb:samecycle appended. Earlier claim labels unchanged.
        # The new statements were checked in this preparation. Not an independent sign-off.
        # 2026-11-11: Goodman part (b) denominator corrected from 6 to 8. Not an independent sign-off.
        "sha": "e37bf3057f41100109c0a323e4c75c585c56368f",
        "claims": "thm:poissonlimit prop:fixedpoisson prop:cycles thm:coupon lem:geovar prop:couponvar prop:empty".split(),
        "exercises": "ex:records ex:fixedvar ex:quicksort ex:factorial ex:reservoir ex:prisoners ex:birthdaywait ex:twopoisson pb:goodman pb:samecycle".split(),
    },
    "ch07-entropy.tex": {
        # Writer repair 2026-11-11: the deepest sibling is named a leaf (V4R2-17). Labels unchanged. Not an independent sign-off.
        # 2026-11-11: ex:mcmillan appended. Earlier claim labels unchanged.
        "sha": "d079cee4d70bf027c17ef23d77a863512c847abf",
        "claims": "prop:gibbs thm:aep thm:kraft thm:shannon prop:chain thm:kl thm:mutual thm:huffman".split(),
        "exercises": "ex:entropymax ex:prefixoptimal ex:entropychain ex:entropyproduct ex:ambiguouscode ex:typicalcount ex:mcmillan".split(),
    },
    "extremal.tex": {
        # Reread 2026-11-11: the appendix states that it is lettered B (V4-17).
        # Reread 2026-11-11 for the van der Waerden wording and the k=1 family (V4R2-11, V4R2-12). Labels unchanged.
        # 2026-11-11: ex:wlower appended. Earlier claim labels unchanged.
        # The new statement was checked in this preparation. Not an independent sign-off.
        "sha": "e7823562c81462cd47a16f9f05de7ea262f24554",
        "claims": "thm:turan thm:ramsey thm:schur thm:sunflower thm:ekr thm:vdw3 thm:vdw".split(),
        "exercises": "ex:r33 ex:turanedges ex:ekrsharp ex:schurtwo ex:ekrcomplement ex:wlower".split(),
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
