from unittest import TestCase
from statistics import average, variance, stdev
from math import sqrt


class AverageTest(TestCase):

    def test_average_normal_case(self):
        """Test average with normal input."""
        self.assertEqual(3, average([2, 3, 4]))
        self.assertEqual(5, average([5, 5, 5]))
        self.assertEqual(0.0, average([0]))

    def test_average_empty_list(self):
        """Test average with an empty list."""
        with self.assertRaises(ValueError):
            average([])

    def test_average_string_input(self):
        """Test average with string input."""
        with self.assertRaises(TypeError):
            average(["Hello"])

    def test_average_single_value(self):
        """Test average with a single value."""
        self.assertEqual(42.0, average([42]))

    def test_average_negative_numbers(self):
        """Test average with negative numbers."""
        self.assertEqual(-3.5, average([-5, -2]))

    def test_average_mixed_types(self):
        """Test average with mixed types (int and float)."""
        self.assertEqual(3.5, average([3, 4.0]))


class VarianceTest(TestCase):

    def test_variance_typical_values(self):
        """Variance of typical values."""
        self.assertEqual(0.0, variance([10.0, 10.0, 10.0, 10.0]))
        self.assertEqual(2.0, variance([1, 2, 3, 4, 5]))
        self.assertEqual(8.0, variance([10, 2, 8, 4, 6]))

    def test_variance_non_integers(self):
        """Variance should work with decimal values."""
        self.assertAlmostEqual(4.0, variance([0.1, 4.1]))
        self.assertAlmostEqual(8.0, variance([0.1, 4.1, 4.1, 8.1]))

    def test_variance_empty_list(self):
        """Variance should raise ValueError for empty list."""
        with self.assertRaises(ValueError):
            variance([])

    def test_input_str_into_variance(self):
        """String should cause an error in variance."""
        with self.assertRaises(TypeError):
            variance(["Hello"])

    def test_variance_single_value(self):
        """Variance of a single element should be zero."""
        self.assertEqual(0.0, variance([42]))

    def test_variance_identical_elements(self):
        """Variance of identical elements should be zero."""
        self.assertEqual(0.0, variance([5] * 100))


class StdevTest(TestCase):

    def test_stdev_normal_case(self):
        """Standard deviation tests."""
        self.assertEqual(0.0, stdev([10.0]))
        self.assertEqual(2.0, stdev([1, 5]))
        self.assertEqual(sqrt(0.5), stdev(
            [0, 0.5, 1, 1.5, 2]))

    def test_stdev_empty_list(self):
        """Standard deviation should raise ValueError for empty list."""
        with self.assertRaises(ValueError):
            stdev([])

    def test_input_str_into_stdev(self):
        """String should cause an error in stdev."""
        with self.assertRaises(TypeError):
            stdev(["Hello"])

    def test_stdev_single_value(self):
        """Standard deviation of a single element should be zero."""
        self.assertEqual(0.0, stdev([42]))


class LargeNumbersTest(TestCase):

    def test_large_numbers(self):
        """Check handling of large numbers."""
        large_numbers = [1e10] * 100
        self.assertEqual(1e10, average(large_numbers))
        self.assertEqual(0.0, variance(large_numbers))


class NaNValuesTest(TestCase):

    def test_nan_values(self):
        """Check handling of NaN values."""
        import math
        with self.assertRaises(TypeError):
            average([math.nan])

    def test_nan_variance(self):
        """Check handling of NaN values."""
        import math
        with self.assertRaises(TypeError):
            variance([math.nan])

    def test_nan_stdev(self):
        """Check handling of NaN values."""
        import math
        with self.assertRaises(TypeError):
            stdev([math.nan])


if __name__ == '__main__':
    import unittest  # pragma: no cover
    unittest.main(verbosity=1)  # pragma: no cover
