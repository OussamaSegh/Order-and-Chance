"""A changed forward use cannot silently inherit an editorial exception."""

import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('volume2_dependencies', ROOT/'review/volume2-independent/check_dependencies.py')
checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks)


class DependencyReviewChecks(unittest.TestCase):
    def setUp(self):
        self.data = checks.inventory()
        self.review = json.loads(checks.REVIEW.read_text())

    def test_actual_complete_reference_set_has_current_manual_explanations(self):
        result = checks.check(self.data, self.review)
        # 322 = 319 plus three backward citations in the Fermat-factor solution:
        # the order proposition twice, and the congruences chapter once.
        # The 85 forward uses are unchanged.
        self.assertEqual(result['references'], 322)
        self.assertEqual(result['reviewed_forward_uses'], 85)
        self.assertIn('no automatic', result['scope'])

    def test_new_removed_or_changed_forward_reference_requires_review(self):
        edge = copy.deepcopy(self.data['reference_edges'][0])
        edge['target'] = 'an-unreviewed-forward-application'
        self.data['reference_edges'].append(edge)
        with self.assertRaisesRegex(ValueError, 'stale'):
            checks.check(self.data, self.review)
        self.data['reference_edges'].pop()
        for mutation in ('context_sha256', 'target'):
            review = copy.deepcopy(self.review)
            review['edge_reviews'][0][mutation] = 'changed'
            with self.assertRaisesRegex(ValueError, 'stale'):
                checks.check(self.data, review)
        self.review['edge_reviews'].pop()
        with self.assertRaisesRegex(ValueError, 'stale'):
            checks.check(self.data, self.review)

    def test_no_unexplained_exception_or_forward_premise_can_pass(self):
        for key, value in [('reason', ''), ('role', 'premise')]:
            review = copy.deepcopy(self.review)
            review['edge_reviews'][0][key] = value
            with self.assertRaises(ValueError):
                checks.check(self.data, review)


if __name__ == '__main__':
    unittest.main()
