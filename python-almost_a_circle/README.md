# Python - Almost A Circle

### Context

In this project, you will review everything about Python:

    Import
    Exceptions
    Class
    Private attribute
    Getter/Setter
    Class method
    Static method
    Inheritance
    Unittest
    Read/Write file
    args and kwargs
    Serialization/Deserialization
    JSON

### Step by Step

    Write the first class Base
    Write the class Rectangle that inherits from Base
    Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded)
    Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance
    Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here
    Update the class Rectangle by overriding the str method so that it returns [Rectangle] instance
    Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y
    Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute
    Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, kwargs) that assigns a key/value argument to attributes
    Write the class Square that inherits from Rectangle
    Update the class Square by adding the public getter and setter size
    Update the class Square by adding the public method def update(self, *args, kwargs) that assigns attributes
    Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle
    Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square
    Update the class Base by adding the class method def savetofile(cls, listobjs): that writes the JSON string representation of listobjs to a file
    Update the class Base by adding the static method def fromjsonstring(jsonstring): that returns the list of the JSON string representation jsonstring
    Update the class Base by adding the class method def create(cls, dictionary): that returns an instance with all attributes already set
    Update the class Base by adding the class method def loadfromfile(cls): that returns a list of instances

### General

    What is Unit testing and how to implement it in a large project
    How to serialize and deserialize a Class
    How to write and read a JSON file
    What is *args and how to use it
    What is **kwargs and how to use it
    How to handle named arguments in a function


### Python Scripts

    Allowed editors: vi, vim, emacs
    All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
    All your files should end with a new line
    The first line of all your files should be exactly #!/usr/bin/python3
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should use the pycodestyle (version 2.7.*)
    All your files must be executable
    The length of your files will be tested using wc
    All your modules should be documented: python3 -c 'print(__import__("my_module").__doc__)'
    All your classes should be documented: python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    All your functions (inside and outside a class) should be documented: python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Python Unit Tests

    Allowed editors: vi, vim, emacs
    All your files should end with a new line
    All your test files should be inside a folder tests
    You have to use the unittest module
    All your test files should be python files (extension: .py)
    All your test files and folders should start with test_
    Your file organization in the tests folder should be the same as your project: ex: for models/base.py, unit tests must be in: tests/test_models/test_base.py
    All your tests should be executed by using this command: python3 -m unittest discover tests
    You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base.py
    We strongly encourage you to work together on test cases so that you don’t miss any edge case
