"""Regressions for corrected mathematics/examples and non-certifying review guards."""
import copy
from pathlib import Path
import sys
import unittest

REVIEW = Path(__file__).resolve().parents[1]/'review/volume3-internal'
sys.path.insert(0, str(REVIEW))
import check_chapter1
import check_chapter2
import check_chapter3
import check_chapter4
import check_chapter5
import check_chapter6
import inventory as volume3_inventory
import registers as volume3_registers


class Volume3InternalReview(unittest.TestCase):
    def test_exact_matrix_and_noncommutative_walk_examples(self):
        check_chapter1.check_matrices()
        check_chapter1.check_walks()

    def test_actual_group_diagrams(self):
        check_chapter1.check_d4_plate()
        check_chapter2.check_subgroup_plate()
        check_chapter3.check_necklace_plate()

    def test_sieving_nilpotent_and_partition_boundaries(self):
        check_chapter3.check_sieving()
        check_chapter3.check_nilpotents()
        check_chapter3.check_touchard()
        check_chapter3.check_colour_orbits()

    def test_changed_proof_cannot_retain_statement_approval(self):
        data = copy.deepcopy(volume3_inventory.inventory())
        proof = next(x for x in data['items'] if x['kind'] == 'proof')
        proof['sha256'] = '0'*64
        with self.assertRaisesRegex(ValueError, 'Changed hint/solution|Stale'):
            volume3_registers.check(data)

    def test_puzzle_attainability_and_permutation_boundaries(self):
        check_chapter4.check_puzzle()
        check_chapter4.check_edge_orientations()
        check_chapter4.check_permutation_cases()

    def test_conjugacy_probability_constant_has_bounded_tail(self):
        check_chapter4.check_probability_constant()

    def test_sylow_normalizers_classification_and_current_count(self):
        check_chapter5.check_sylow_and_derived()
        check_chapter5.check_gl2()
        check_chapter5.check_order12_and_plate()

    def test_ring_boundaries_polynomials_and_actual_lattice(self):
        check_chapter6.check_zero_ring_source()
        check_chapter6.check_residue_and_crt()
        check_chapter6.check_polynomials()
        check_chapter6.check_lattice()

    def test_bibliography_coordinates_exclude_the_next_item(self):
        data=volume3_inventory.inventory()
        for row in data["items"]:
            if row["kind"] != "bibliography":
                continue
            lines=(volume3_inventory.ROOT/row["path"]).read_text().splitlines()
            actual="\n".join(lines[row["line"]-1:row["end_line"]])
            self.assertEqual(actual.count(r"\item"),1,row["id"])

    def test_changed_reference_context_cannot_keep_classification(self):
        data = copy.deepcopy(volume3_inventory.inventory())
        data['reference_edges'][0]['target'] = 'unreviewed-target'
        with self.assertRaisesRegex(ValueError, 'classifications are stale'):
            volume3_registers.check(data)


if __name__ == '__main__':
    unittest.main()
