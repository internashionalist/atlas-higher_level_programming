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

    def test_invalid_height(self):
        """
        Test invalid height cases - string, negative, zero
        """
        with self.assertRaises(TypeError):
            Rectangle(2, "string", 6, 8)

        with self.assertRaises(ValueError):
            Rectangle(2, -10, 6, 8)

        with self.assertRaises(ValueError):
            Rectangle(2, 0, 6, 8)

    def test_invalid_x(self):
        """
        Test invalid x cases - string, negative
        """
        with self.assertRaises(TypeError):
            Rectangle(2, 4, "string", 8)

        with self.assertRaises(ValueError):
            Rectangle(2, 4, -10, 8)

    def test_invalid_y(self):
        """
        Test invalid y cases - string, negative
        """
        with self.assertRaises(TypeError):
            Rectangle(2, 4, 6, "string")

        with self.assertRaises(ValueError):
            Rectangle(2, 4, 6, -10)

    def test_area(self):
        """
        Test area method
        """
        rectangle = Rectangle(2, 4)
        self.assertEqual(rectangle.area(), 8)

    def test_str(self):
        """
        Test __str__ method
        """
        rectangle = Rectangle(2, 4, 6, 8, 1)
        self.assertEqual(str(rectangle), "[Rectangle] (1) 6/8 - 2/4")

    def test_display(self):
        """
        Test display method
        """
        rectangle = Rectangle(2, 4)
        rectangle.display() 

