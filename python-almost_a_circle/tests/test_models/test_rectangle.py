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
    def test_id_assignment(self):
        """
        Test id assignment
        """
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.id, 1)
