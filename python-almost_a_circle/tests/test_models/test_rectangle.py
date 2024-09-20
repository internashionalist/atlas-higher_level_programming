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
        rectangle = Rectangle(2, 4, 6, 8)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(rectangle.height, 4)
        self.assertEqual(rectangle.x, 6)
        self.assertEqual(rectangle.y, 8)
