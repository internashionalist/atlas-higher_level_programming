#!/usr/bin/python3
"""
UnitTests for Rectangle
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """
    TestRectangle class
    """
    def test_valid_attributes(self):
        """
        Test valid attributes
        """
        rectangle = Rectangle(2, 4, 6, 8, 1)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(rectangle.height, 4)
        self.assertEqual(rectangle.x, 6)
        self.assertEqual(rectangle.y, 8)
        self.assertEqual(rectangle.id, 1)

    def test_attribute_cases(self):
        """
        Test attribute cases
        """
        rectangle = Rectangle(1, 2)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)

    def test_invalid_width(self):
        """
        Test invalid width cases - string, negative, zero
        """
        with self.assertRaises(TypeError):
            Rectangle("string", 4, 6, 8)

        with self.assertRaises(ValueError):
            Rectangle(-10, 4, 6, 8)

        with self.assertRaises(ValueError):
            Rectangle(0, 4, 6, 8)

