"""Structural proof-presence regression for the approved printed Volume 4 route.

This does not verify the mathematics of a proof or its hypotheses. It catches
new statements whose proof was accidentally omitted or moved past the next
statement/section; independently reviewed mathematics remains a separate gate.

Run: python3 -m unittest discover -s tools -p test_volume4_proof_structure.py
"""

import re
from pathlib import Path
import unittest


CHAPTERS = Path(__file__).resolve().parents[1] / "volume4-chance" / "chapters"
INCLUDED_SOURCES = (
    "ch01-counting.tex",
    "ch02-discrete.tex",
    "ch03-generating.tex",
    "ch04-inequalities.tex",
    "ch05-continuous.tex",
    "ch05-geometric.tex",
    "ch06-clt.tex",
    "ch07-entropy.tex",
    "ch07-walks.tex",
    "ch08-markov.tex",
    "ch09-poisson.tex",
    "ch10-martingales.tex",
    "ch11-brownian.tex",
    "ch12-method.tex",
    "ch14-graphs.tex",
    "extremal.tex",  # printed Appendix B
)
CLAIM_ENVIRONMENTS = (
    "theorem",
    "theoremx",
    "lemma",
    "proposition",
    "corollary",
    "corollaryx",
)
CLAIM = re.compile(
    r"\\begin\{(" + "|".join(CLAIM_ENVIRONMENTS) + r")\}(?:\[[^\]]*\])?"
)
STOP = re.compile(
    r"\\begin\{(?:" + "|".join(CLAIM_ENVIRONMENTS) +
    r"|example|examplex|exercise)\}|\\(?:section|chapter)(?:\*?)\{"
)


class TestVolume4ProofStructure(unittest.TestCase):
    def test_every_declared_claim_has_an_adjacent_nonempty_proof(self):
        statements = 0
        problems = []
        for filename in INCLUDED_SOURCES:
            text = (CHAPTERS / filename).read_text(encoding="utf-8")
            # Ignore TeX comments before looking for a proof.
            text = "\n".join(line.split("%", 1)[0] for line in text.splitlines())
            for match in CLAIM.finditer(text):
                statements += 1
                env = match.group(1)
                line = text.count("\n", 0, match.start()) + 1
                ending = r"\end{" + env + "}"
                end_at = text.find(ending, match.end())
                if end_at < 0:
                    problems.append(f"{filename}:{line} unclosed {env}")
                    continue
                body = text[end_at + len(ending):]
                proof_at = body.find(r"\begin{proof}")
                boundary = STOP.search(body)
                if proof_at < 0 or (boundary is not None and boundary.start() < proof_at):
                    problems.append(f"{filename}:{line} {env} missing adjacent proof")
                    continue
                proof_end = body.find(r"\end{proof}", proof_at)
                if proof_end < 0 or not body[proof_at + len(r"\begin{proof}"):proof_end].strip():
                    problems.append(f"{filename}:{line} {env} has empty/unclosed proof")
        self.assertFalse(problems, "\n".join(problems))
        self.assertGreaterEqual(
            statements, 127,
            "Expected the current set of 127 proof-bearing statements; investigate omissions",
        )


if __name__ == "__main__":
    unittest.main()
