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

    def test_to_dictionary(self):
        """
        Test to_dictionary method
        """
        square = Square(2, 4, 6, 1)
        square_dict = square.to_dictionary()
        self.assertEqual(square_dict, {"id": 1, "size": 2, "x": 4, "y": 6})

    def test_update(self):
        """
        Test update method
        """
        square = Square(2, 4, 6, 1)
        square.update(89, 1, 2, 3)
        self.assertEqual(square.__str__(), "[Square] (89) 2/3 - 1")

    def test_update_kwargs(self):
        """
        Test update method with kwargs
        """
        square = Square(2, 4, 6, 1)
        square.update(id=89, size=1, x=2, y=3)
        self.assertEqual(square.__str__() , "[Square] (89) 2/3 - 1")

    def test_create(self):
        """
        Test create method
        """
        square = Square(1, 2, 3, 89)
        square_dict = square.to_dictionary()
        new_square = Square.create(**square_dict)
        self.assertEqual(new_square.__str__(), "[Square] (89) 2/3 - 1")

    def test_save_to_file(self):
        """
        Test save_to_file method
        """
        square = Square(2, 4, 6, 1)
        Square.save_to_file([square])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(),
                            '[{"id": 1, "size": 2, "x": 4, "y": 6}]')
            
    def test_save_to_file_empty(self):
        """
        Test save_to_file method with empty list
        """
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_None(self):
        """
        Test save_to_file method with None
        """
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_load_from_file(self):
        """
        Test load_from_file method
        """
        square = Square(2, 4, 6, 1)
        Square.save_to_file([square])
        squares = Square.load_from_file()
        self.assertEqual(square.__str__(), squares[0].__str__())

    def test_load_from_file_Missing(self):
        """
        Test load_from_file method with missing file
        """
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])
