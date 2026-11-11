"""Pin Volume 4 Chapters 1, 3 and 4 sole-validator mathematical audit blobs.

This is source identity/version control, not automated mathematical proof.
Changed source invalidates the prior human-style sole-validator reasoning until
the new exact blob is reread and the pin deliberately updated.
"""
import hashlib
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1] / "volume4-chance" / "chapters"
SCOPE = {
    "ch01-counting.tex": {
        # Reread 2026-11-11 for the countable-cover wording and the tail-of-ones
        # argument (V4-14), and for the named host sentence (V4-15).
        "sha": "f4129ed5d7477942cbae9e83b122d871e0a7c6c2",
        "claims": "prop:bits prop:subadd prop:infdigits thm:ballot".split(),
        "exercises": "ex:mybirthday ex:twochildren ex:penney ex:montyn ex:pairwise ex:aces ex:catalan ex:smallballot".split(),
    },
    "ch03-generating.tex": {
        # Reread 2026-11-11 for the undefined S_N and the O(log n) bridge (V4-09, V4-10).
        "sha": "369bbb43ea41bbfb7e81340c9248516564135d3d",
        "claims": "prop:pgfcoeff prop:pgfmean prop:pgfvar prop:pgfsum prop:randomsum prop:genmean thm:extinction".split(),
        "exercises": "ex:thinning ex:golden ex:lotka ex:randomsumvar ex:progeny ex:firstpassage ex:binseries ex:poissongw".split(),
    },
    "ch04-inequalities.tex": {
        # Reread 2026-11-11 for the countable moment-generating product (V4-12)
        # and the integer atom in the longest-run solution (V4-11).
        # Reread 2026-11-11 for removal of the unused Shannon source line (V4R2-05). Labels unchanged.
        "sha": "f1fc8df91bdcb119f5345059525680e367dec5cc",
        "claims": "lem:hoeffding thm:hoeffding thm:kolmogorov thm:bc thm:sllnbound thm:weierstrass".split(),
        "exercises": "ex:markovsharp ex:chernoffbin ex:bcfinite ex:bernstein2 ex:gapfill ex:runs".split(),
    },
}
PROOFS = re.compile(r"\\begin\{(?:theorem|lemma|proposition)\}(?:\[[^\]]+\])?\s*\\label\{([^}]+)\}")
EXERCISES = re.compile(r"\\begin\{exercise\}(?:\[[^\]]+\])?\s*\\label\{([^}]+)\}")
HINTS = re.compile(r"\\begin\{hint\}\{([^}]+)\}")
SOLUTIONS = re.compile(r"\\begin\{solution\}\{([^}]+)\}")


class TestSignedOffProofAndExerciseSourceIdentity(unittest.TestCase):
    def test_exact_source_git_blob_sha1(self):
        for file, contract in SCOPE.items():
            with self.subTest(file=file):
                data = (ROOT / file).read_bytes()
                payload = b"blob " + str(len(data)).encode() + b"\x00" + data
                self.assertEqual(hashlib.sha1(payload).hexdigest(), contract["sha"])

    def test_every_mathematically_audited_claim_label(self):
        for file, contract in SCOPE.items():
            with self.subTest(file=file):
                data = (ROOT / file).read_text(encoding="utf8")
                self.assertEqual(PROOFS.findall(data), contract["claims"])

    def test_all_audited_exercises_have_matching_hints_and_solutions(self):
        for file, contract in SCOPE.items():
            with self.subTest(file=file):
                data = (ROOT / file).read_text(encoding="utf8")
                for rx in (EXERCISES, HINTS, SOLUTIONS):
                    self.assertEqual(rx.findall(data), contract["exercises"])


if __name__ == "__main__":
    unittest.main()
