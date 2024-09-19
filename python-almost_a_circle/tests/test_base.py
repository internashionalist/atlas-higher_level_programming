#!/usr/bin/python3
"""
UnitTests for Base
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    TestBase class
    """

    def test_id(self):
        """
        Method to test id
        """
        Base._Base__nb_objects = 0
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)
