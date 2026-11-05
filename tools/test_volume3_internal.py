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
import check_chapter7
import check_chapter8
import check_chapter9
import check_chapter10
import check_chapter11
import check_chapter12
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

    def test_minimal_simple_order_and_actual_sylow_table(self):
        check_chapter5.check_small_order_arguments()

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

    def test_module_forms_tables_and_earned_problem_location(self):
        check_chapter7.check_actual_smith_and_table()
        check_chapter7.check_jordan_and_units()
        check_chapter7.check_migration_and_zero_scope()

    def test_field_examples_diagram_and_inseparability_boundaries(self):
        check_chapter8.check_exact_radicals()
        check_chapter8.check_pentagon_plate()
        check_chapter8.check_characteristic_probes()

    def test_finite_fields_codes_trace_and_actual_figures(self):
        check_chapter9.check_fields_and_aes()
        check_chapter9.check_actual_figures()
        check_chapter9.check_codes()
        check_chapter9.check_recurrences_and_trace()
        check_chapter9.check_moore()

    def test_galois_fixed_fields_periods_and_prerequisite_order(self):
        check_chapter10.check_actual_lattice()
        check_chapter10.check_periods_and_counts()
        check_chapter10.check_quintic_plot()
        check_chapter10.check_earned_order_and_local_cosine()

    def test_complex_representation_foundations_are_earned_locally(self):
        check_chapter11.check_foundations()

    def test_actual_character_tables_filters_and_periodic_walks(self):
        check_chapter11.check_actual_character_figure()
        check_chapter11.check_walks_and_filters()

    def test_commutators_and_integer_matrix_group(self):
        check_chapter11.check_commutators_and_integer_group()

    def test_indicator_flip_and_signed_involution_model(self):
        check_chapter11.check_indicator_matrix_identity()
        check_chapter11.check_involution_model()
        check_chapter11.check_local_indicator_prerequisites()

    def test_quaternion_cover_and_hurwitz_exact_arithmetic(self):
        check_chapter12.check_quaternion_and_cover_coordinates()
        check_chapter12.check_hurwitz_units()

    def test_icosahedral_attainability_and_actual_rotation_plates(self):
        check_chapter12.check_icosahedral_existence()
        check_chapter12.check_rotation_plate()
        check_chapter12.check_actual_solid_plate()

    def test_workshop_greedy_recurrences_dice_and_subset_characters(self):
        check_chapter12.check_sylvester_and_mersenne()
        check_chapter12.check_dice_and_subset_characters()

    def test_zero_sum_systems_and_finite_abelian_average(self):
        check_chapter12.check_egz_and_systems()
        check_chapter12.check_abelian_coefficient_counts_and_constant()

    def test_local_integrals_and_icosahedral_walk_endpoints(self):
        check_chapter12.check_jensen_finite_products_and_integrals()
        check_chapter12.check_actual_icosahedral_walk()
        check_chapter12.check_workshop_prerequisites()

    def test_changed_reference_context_cannot_keep_classification(self):
        data = copy.deepcopy(volume3_inventory.inventory())
        data['reference_edges'][0]['target'] = 'unreviewed-target'
        with self.assertRaisesRegex(ValueError, 'classifications are stale'):
            volume3_registers.check(data)


if __name__ == '__main__':
    unittest.main()
