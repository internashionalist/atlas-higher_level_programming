#!/usr/bin/python3
"""
UnitTests for Square
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
from unittest.mock import patch, MagicMock


class TestSquare(unittest.TestCase):
    """
    TestSquare class
    """
    def test_valid_attributes(self):
        """
        Test valid attributes
        """
        square = Square(2, 4, 6, 1)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 6)
        self.assertEqual(square.id, 1)

    def test_attribute_cases(self):
        """
        Test attribute cases
        """
        square = Square(1)
        self.assertEqual(square.size, 1)

    def test_invalid_size(self):
        """
        Test invalid size cases - string, negative, zero
        """
        with self.assertRaises(TypeError):
            Square("string")

        with self.assertRaises(ValueError):
            Square(-1)

        with self.assertRaises(ValueError):
            Square(0)

    def test_invalid_x(self):
        """
        Test invalid x cases - string, negative
        """
        with self.assertRaises(TypeError):
            Square(1, "string")

        with self.assertRaises(ValueError):
            Square(1, -1)

    def test_invalid_y(self):
        """
        Test invalid y cases - string, negative
        """
        with self.assertRaises(TypeError):
            Square(2, 4, "string")

        with self.assertRaises(ValueError):
            Square(1, 2, -1)

    def test_area(self):
        """
        Test area method
        """
        square = Square(2)
        self.assertEqual(square.area(), 4)

    def test_display(self):
        """
        Test display method
        """
        square = Square(2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            square.display()
            self.assertEqual(fake_out.getvalue(), "##\n##\n")

    def test_str(self):
        """
        Test __str__ method
        """
        square = Square(2, 4, 6, 1)
        self.assertEqual(square.__str__(), "[Square] (1) 4/6 - 2")
