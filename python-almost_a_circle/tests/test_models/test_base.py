#!/usr/bin/python3
"""
UnitTests for Base
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    TestBase class
    """
    def test_id_assignment(self):
        """
        Test id assignment
        """
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

    def test_id_type(self):
        """
        Test id type
        """
        b1 = Base(1)
        self.assertIsInstance(b1.id, int)

    def test_id_assignment_string(self):
        """
        Test id assignment with string
        """
        b1 = Base("string")
        self.assertEqual(b1.id, "string")

    def test_to_json_string_None(self):
        """
        Test to_json_string with None
        """
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """
        Test to_json_string with empty list
        """
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_from_json_string_None(self):
        """
        Test from_json_string with None
        """
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """
        Test from_json_string with empty string
        """
        self.assertEqual(Base.from_json_string(""), [])
