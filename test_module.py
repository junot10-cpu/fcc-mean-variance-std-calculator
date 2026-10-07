"""Learning tests for the calculator; these are not the official FCC tests."""
import contextlib
import importlib
import io
import unittest

import mean_var_std
from mean_var_std import calculate


class CalculateTests(unittest.TestCase):
    def assert_results(self, actual, expected):
        self.assertEqual(list(actual), list(expected))
        for key in expected:
            self.assertEqual(len(actual[key]), 3, f"'{key}' must have 3 entries")
            for columns_or_rows in actual[key][:2]:
                self.assertIsInstance(columns_or_rows, list)
            for got, want in zip(actual[key][0], expected[key][0]):
                self.assertAlmostEqual(got, want, msg=f"{key} (columns)")
            for got, want in zip(actual[key][1], expected[key][1]):
                self.assertAlmostEqual(got, want, msg=f"{key} (rows)")
            self.assertAlmostEqual(actual[key][2], expected[key][2], msg=f"{key} (all)")

    def test_sequence_zero_to_eight(self):
        expected = {
            'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
            'variance': [[6.0, 6.0, 6.0],
                         [0.6666666666666666] * 3, 6.666666666666667],
            'standard deviation': [[2.449489742783178] * 3,
                                   [0.816496580927726] * 3, 2.581988897471611],
            'max': [[6, 7, 8], [2, 5, 8], 8],
            'min': [[0, 1, 2], [0, 3, 6], 0],
            'sum': [[9, 12, 15], [3, 12, 21], 36],
        }
        self.assert_results(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]), expected)

    def test_other_integers(self):
        expected = {
            'mean': [[4.666666666666667, 4.333333333333333, 2.6666666666666665],
                     [5.0, 3.0, 3.6666666666666665], 3.888888888888889],
            'variance': [[9.555555555555555, 11.555555555555555, 4.222222222222222],
                         [10.666666666666666, 0.0, 14.88888888888889],
                         9.209876543209877],
            'standard deviation': [[3.0912061651652345, 3.39934634239519,
                                    2.0548046676563256],
                                   [3.265986323710904, 0.0, 3.858612300930075],
                                   3.034777840832814],
            'max': [[9, 9, 5], [9, 3, 9], 9],
            'min': [[2, 1, 0], [1, 3, 0], 0],
            'sum': [[14, 13, 8], [15, 9, 11], 35],
        }
        self.assert_results(calculate([9, 1, 5, 3, 3, 3, 2, 9, 0]), expected)

    def test_negative_numbers_and_decimals(self):
        expected = {
            'mean': [[3.3333333333333335, -0.16666666666666666, -0.3333333333333333],
                     [0.16666666666666666, 0.8333333333333334, 1.8333333333333333],
                     0.9444444444444444],
            'variance': [[12.722222222222221, 4.388888888888889, 1.5555555555555556],
                         [2.0555555555555554, 9.38888888888889, 14.38888888888889],
                         9.080246913580247],
            'standard deviation': [[3.5668224265054493, 2.094967514996089,
                                    1.247219128924647],
                                   [1.4337208778404378, 3.064129385141706,
                                    3.793268892247014],
                                   3.0133448049601372],
            'max': [[7, 2, 1], [2, 4.5, 7], 7],
            'min': [[-1.5, -3, -2], [-1.5, -3, -2], -3],
            'sum': [[10.0, -0.5, -1], [0.5, 2.5, 5.5], 8.5],
        }
        self.assert_results(
            calculate([-1.5, 2, 0, 4.5, -3, 1, 7, 0.5, -2]), expected
        )

    def test_too_few_numbers_raises_error(self):
        with self.assertRaisesRegex(ValueError, 'List must contain nine numbers.'):
            calculate([1, 2, 3, 4, 5, 6, 7, 8])

    def test_too_many_numbers_raises_error(self):
        with self.assertRaisesRegex(ValueError, 'List must contain nine numbers.'):
            calculate(list(range(10)))

    def test_import_is_silent(self):
        captured_output = io.StringIO()
        with contextlib.redirect_stdout(captured_output):
            importlib.reload(mean_var_std)
        self.assertEqual(captured_output.getvalue(), '')


if __name__ == '__main__':
    unittest.main(verbosity=2)
