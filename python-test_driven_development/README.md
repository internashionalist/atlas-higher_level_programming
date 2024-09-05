***Python - Test-Driven Development***

**Background Context**

Important notice on intranet checks for Python projects

Starting from today:

    Based on the requirements of each task, you should always write the documentation (module(s) + function(s)) and tests first, before you actually code anything
    The intranet checks for Python projects won’t be released before their first deadline, in order for you to focus more on TDD and think about all possible cases
    We strongly encourage you to work together on test cases, so that you don’t miss any edge case. But not in the implementation of them!
    Don’t trust the user, always think about all possible edge cases


**Learning Objectives**

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

    Why Python programming is awesome
    What’s an interactive test
    Why tests are important
    How to write Docstrings to create tests
    How to write documentation for each module and function
    What are the basic option flags to create tests
    How to find edge cases


**Requirements**

*Python Scripts*

    Allowed editors: vi, vim, emacs
    All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
    All your files should end with a new line
    The first line of all your files should be exactly #!/usr/bin/python3
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should use the pycodestyle (version 2.7.*)
    All your files must be executable
    The length of your files will be tested using wc

*Python Test Cases*

    Allowed editors: vi, vim, emacs
    All your files should end with a new line
    All your test files should be inside a folder tests
    All your test files should be text files (extension: .txt)
    All your tests should be executed by using this command: python3 -m doctest ./tests/*
    All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)')
    A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
    We strongly encourage you to work together on test cases, so that you don’t miss any edge case – The Checker is checking for tests!

**Tasks**

0. Integers addition

    Write a function that adds 2 integers.

    Prototype: def add_integer(a, b=98):
    a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
    a and b must be first casted to integers if they are float
    Returns an integer: the addition of a and b
    You are not allowed to import any module


1. Divide a matrix

    Write a function that divides all elements of a matrix.

    Prototype: def matrix_divided(matrix, div):
    matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message matrix must be a matrix (list of lists) of integers/floats
    Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message Each row of the matrix must have the same size
    div must be a number (integer or float), otherwise raise a TypeError exception with the message div must be a number
    div can’t be equal to 0, otherwise raise a ZeroDivisionError exception with the message division by zero
    All elements of the matrix should be divided by div, rounded to 2 decimal places
    Returns a new matrix
    You are not allowed to import any module


2. Say my name

    Write a function that prints My name is <first name> <last name>

    Prototype: def say_my_name(first_name, last_name=""):
    first_name and last_name must be strings otherwise, raise a TypeError exception with the message first_name must be a string or last_name must be a string
    You are not allowed to import any module


3. Print square

    Write a function that prints a square with the character #.

    Prototype: def print_square(size):
    size is the size length of the square
    size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
    if size is less than 0, raise a ValueError exception with the message size must be >= 0
    if size is a float and is less than 0, raise a TypeError exception with the message size must be an integer
    You are not allowed to import any module


4. Text indentation

    Write a function that prints a text with 2 new lines after each of these characters: ., ? and :

    Prototype: def text_indentation(text):
    text must be a string, otherwise raise a TypeError exception with the message text must be a string
    There should be no space at the beginning or at the end of each printed line
    You are not allowed to import any module


5. Max integer - Unittest

    Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.

    In this task, you will write unittests for the function def max_integer(list=[]):.

    Your test file should be inside a folder tests
    You have to use the unittest module
    Your test file should be python files (extension: .py)
    Your test file should be executed by using this command: python3 -m unittest tests.6-max_integer_test
    All tests you make must be passable by the function below
    We strongly encourage you to work together on test cases, so that you don’t miss any edge case

    