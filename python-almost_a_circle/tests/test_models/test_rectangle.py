#!/usr/bin/python3
"""
UnitTests for Rectangle
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
from unittest.mock import patch, MagicMock


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
        with patch('sys.stdout', new=StringIO()) as fake_out:
            rectangle.display()
            self.assertEqual(fake_out.getvalue(), 
                             "##\n##\n##\n##\n")

    def test_display_xy(self):
        """
        Test display method with x and y
        """
        rectangle = Rectangle(2, 4, 2, 2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            rectangle.display()
            self.assertEqual(fake_out.getvalue(), 
                             "\n\n  ##\n  ##\n  ##\n  ##\n")

    def test_to_dictionary(self):
        """
        Test to_dictionary method
        """
        rectangle = Rectangle(2, 4, 6, 8, 1)
        self.assertEqual(rectangle.to_dictionary(), 
                         {'x': 6, 'y': 8, 'id': 1, 'height': 4, 'width': 2})

    def test_update(self):
        """
        Test update method
        """
        rectangle = Rectangle(2, 4, 6, 8, 1)
        rectangle.update(1, 3, 5, 7, 10)
        self.assertEqual(str(rectangle), "[Rectangle] (1) 7/10 - 3/5")

    def test_update_checker(self):
        """
        Test update method with what the checker is looking for
        """
        rectangle = Rectangle(2, 4, 6, 8, 1)
        rectangle.update(89, 1, 2, 3, 4)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 3/4 - 1/2")

    def test_update_kwargs(self):
        """
        Test update method with kwargs
        """
        rectangle = Rectangle(2, 4, 6, 8, 1)
        rectangle.update(width=1, height=2, x=3, y=4, id=89)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 3/4 - 1/2")

    def test_create(self):
        """
        Test create method
        """
        rectangle = Rectangle(89, 1, 2, 3, 4)
        rectangle_dictionary = rectangle.to_dictionary()
        rectangle2 = Rectangle.create(**rectangle_dictionary)
        self.assertEqual(str(rectangle), str(rectangle2))

    def test_save_to_file(self):
        """
        Test save_to_file method
        """
        rectangle = Rectangle(1, 2)
        Rectangle.save_to_file([rectangle])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 53)
    
    def test_save_to_file_empty(self):
        """
        Test save_to_file method with empty list
        """
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_None(self):
        """
        Test save_to_file method with None
        """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_load_from_file(self):
        """
        Test load_from_file method
        """
        rectangle = Rectangle(1, 2)
        Rectangle.save_to_file([rectangle])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(str(rectangle), str(rectangles[0]))
