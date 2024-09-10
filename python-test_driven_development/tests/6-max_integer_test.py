#!/usr/bin/python3

"""
UnitTest for max_integer([..])
"""
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Contains test cases for max_integer function
    """

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([5, 3, 4, 2]), 5)

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        self.assertEqual(max_integer([-1, 2, 3, -4]), 3)

    def test_list_with_duplicates(self):
        self.assertEqual(max_integer([1, 3, 3, 2]), 3)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 3.2, 2.8]), 3.2)

    def test_mixed_types(self):
        self.assertEqual(max_integer([1, 3.5, 2]), 3.5)


if __name__ == "__main__":
    unittest.main()
