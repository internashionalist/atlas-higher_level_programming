# To Mute, or Not to Mute: Immutable and Mutable Objects in Python

![Immutable and Mutable Objects](https://github.com/internashionalist/atlas-higher_level_programming/blob/main/python-everything_is_object/mutable2.png)


## Introduction
Among the many glorious characteristics of Python is the distinction between “mutable” and “immutable” objects. It may be easy to overlook these words when one is simply trying to beat a checker, but it’s essential to fully understand what they mean if you want to beat the checkers down the line. Today, we’ll break down these concepts with a focus on just how Python treats them passing arguments to functions and, hopefully, have a better understanding of what the checkers of the future will want from you.


## ID and Type in Python
To begin - every object in Python has both an ID and a type. The ID points to a location in memory where the object is stored. You can easily check the ID and type of an object using the ‘id()’ and ‘type()’ functions, respectively. These attributes help Python manage object identity and type consistency. We’ll get into how they help you in a moment.

```python
x = 777
print(id(x))  # ID of the object
print(type(x))  # type of the object
```

The output will show the memory location of ‘x’ and its type (‘int’). IDs are unique for each object, but if two variables refer to the same object, they share the same ID. It's important to recognize that the ID of an object remains constant during its lifetime but can change when objects are reassigned. When a variable is reassigned, it points to a new object in memory, even if the value seems the same.

```python
x = 777
print(id(x))  # ID of x
x = 888
print(id(x))  # ID changes after reassignment
```

In the above case, the ID of ‘x’ changes when its value is reassigned to ‘888’ because Python allocates new memory for the new value.

Additionally, when multiple variables refer to the same object, they share the same ID:

```python
a = 777
b = a
print(id(a))  # ID of a
print(id(b))  # ID of b (same as a)
```

Here, ‘a’ and ‘b’ both point to the same memory location, as Python optimizes memory by reusing the same object if the value is identical. Changes to mutable objects can affect all variables referring to the same object, while immutable objects behave differently.


## Mutable Objects
Mutable objects can change (mutate) their state or contents after creation. Lists and dictionaries are typical examples of mutable objects in Python. When you modify a mutable object, like appending an element to a list, it changes the object’s state without creating a new object. 

```python
my_list = [1, 2, 3]
print(id(my_list))  # initial ID
my_list.append(4)
print(id(my_list))  # same ID, list changed
```

The ID remains the same because the list is mutable, and its content can change without changing the object itself.


## Immutable Objects
On the other hand, immutable objects cannot be changed after they are created. This includes types like integers, strings, and tuples. Any operation that alters an immutable object creates a new object with a different ID.

```python
my_string = "hello"
print(id(my_string))  # initial ID
my_string += " world"
print(id(my_string))  # new ID, since strings are immutable
```

Even though ‘my_string’ was modified, Python created a new string object, leaving the original object unchanged.

## Okay, So What?
The difference between mutable and immutable objects becomes more and more important, especially when it comes to memory management and performance. Mutable objects can be updated in-place, which is more efficient, while immutable objects require creating new instances for every change, which can lead to higher memory usage.

Python handles mutable and immutable objects differently in terms of memory and references. This distinction plays a role in how variables point to objects in memory and can lead to unexpected behavior if not carefully managed.

### How Arguments Are Passed to Functions
Python passes arguments to functions by object reference. For immutable objects, this means the function works with a copy of the object. For mutable objects, the function can modify the original object itself:

```python
def modify_list(a_list):
    a_list.append(8)

my_list = [2, 4, 6]
modify_list(my_list)
print(my_list)  # [2, 4, 6, 8]
```

Here, the list was modified in place because lists are mutable. However, when using an immutable object like a string, the original value remains unchanged.

```python
def modify_string(a_string):
    a_string += “ globe"

my_string = "greetings"
modify_string(my_string)
print(my_string)  # still "greetings"
```

Since strings are immutable, the function ‘modify_string’ does not affect the original string, and a new object is created instead.


## Conclusion
Beating the checker now is all well and good, but understanding mutable and immutable objects in full will help you actually write efficient code when there’s no checker to beat. Whether you're creating simple list copies or managing complex data structures, this foundational knowledge is key. Grab that Python by the tail NOW before the other end bites YOU.
