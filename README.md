# python-intro

### Virtual Environments
Virtual environments in Python are like a self-contained directory that contains the installations for a given project (controls the python version for that project and helps to handle libraries and dependencies). 
It is good because you don't have to worry about the version it is using when running the programs (e.g python3 {file}.py, python {file}.py). The environment executable will take care of it.

To create a new virtual environment on mac / linux, follow the next steps (for windows it is slighly different):
1. Create project root directory
2. run the command `python3.7 -m venv env` (or whatever version it is)
3. run the command `source env/bin/activate` - a line with read `(env) ...` or something along these lines should be printed out

This configuration will be attached to the terminal session. If you reopen it, to have the virtual environment set up again, just reexecute step #3

### REPL
REPL stands for read-evaluate-print-loop. It allows devs to interact with python interpreter, type in commands and instantly see the output. 
To open the REPL on VSCode, open the command pallet (command + shift + p) and search for `Python: start REPL`.

Useful built-in methods to use with REPL:
1. type(var) = returns the type of a given variable. Python has a dynamic type system (opposed to static ones)
2. dir(var) = returns all the available methods for a given type / object. E.g if you call dir of a string, it will return methods like `format`, `capitalize`, `upper` etc
3. help(type | type.method) - e.g help(str). It returns all the documentation available for a given type
4. on VS Code `control + L` cleans up the terminal 

*things to keep in mind*
Python allows you to override built-in types. If you do so, you lose that feature. Example:
```
list = 1 // list is not a list anymore, but a number
list(2) // it won't work because now it is an int
```

### Types
*Numerics*
You can create an integer by simply assigning a integer number to a variable: `x = 2`.
To create a floating point number, simply add a decimal point `x = 1.0`.
Complex numbers are represented with a suffix `j` - `x = 1j`.

*strings*
String creation in python can be with single or double quotes.
Strings can be concatenated with plus (+) symbol
Long strings can be created with triple quotes (""").

```
x = """my very..
... long text
...
"""
```

Strings formatting:
f-strings (introduced by python 3): it allows to create strings referencing to external variables using curly braces (interpolation):
```
f"Hello {name}, how are you today?"
```

Other (older) formattings: percent formatting, .format method.

### Functions

Functions in python are define with the keyword `def` plus the name of the functions (using snake case), brackets with the arguments it receives and finally colon. Unlike Java, JS and many other programming languages, python defines scopes with tabs. The body of a function need to be indented one level to the right:

```
def my_func(param):
    return "hello there"
```

Arguments of a function can have a default value in case it it not mandatory:

```
def calc(x, y, operation="sum"):
    return x + y
```

Arguments can be positional or keyword arguments. When calling a function a combination of both can be used however the positional ones must come first:

```
calc(1, operation = "sub", y = 2)
```

*Never use a list as a default value of a function's argument. Python only instantiates when it is creating the list. It causes that list to be reused across multiple calls incurring on unexpected results:

```
def add_to_list(a, my_list=[]):
    my_list.append(a)

add_to_list(1) // [1]
add_to_list(3) // [1, 3] not [3]
```

Functions can access variables stored in the outer scopes however they cannot be changed.

```
x = 2

def my_func():
    print(x) // 2
    x = 4
    pront(x) // 4

print(x) // 2
```

### Lists

There are two methods to create lists. 1. using square brackets on the right side of the assignment operator 2. using the api method list.

```
my_list = [1, 2, 3]
my_list = []
my_list = list(1, 2, 3)
my_list = list()
```

The main methods of list objects (and operations) are:

1. `append` to add a new element at the end of the list (`my_list.append(value))
2. `insert` add a new element at a specific position (`my_list.insert(index, value)) - it is not a replace
3. `remove` an element at an specific position (`my_list.remove(index)`)
4. `pop` the last element of the list (`my_list.pop()`) - can also be used with the index of the element that needs to be popped out (`my_list.pop(index)`)
5. `index` to find the position of a given element (`my_list.index(element)`)
6. `in` clause to verify if an element is part of a list (`element in my_list`) - it returns a boolean
7. `count` to find the number of specific elements in a list (`my_list.count(element)`).
8. `len` to get the list size
9. `extend` to join two lists
10. `sort` to sort a list in place (`my_list.sort()`) - it mutates the list 
11. `sorted` to sort the list in a immutable way (`sorted(my_list)`) - a new list is returned and the original list is left intact
12. `reverse` to descendingly sort a list  in place (`my_list.reverse()`) - it mutates the list
13. `sorted(reverse=True)` to descendingly sort a list in a immutable way (`sorted(my_list, reverse=True)`)

### Tuples

Tuples are cointainers that can store different types of data (in theory that are somewhat related) in specific positions. Tuples are immutable.

There are two methods to create tuples. 1. using the built in api method tuple 2. using brackets*** (there is a small caveat here). Examples:

```
http_response = tuple([200, "ok"])
http_response = (200, "ok")

my_tuple = tuple()
my_typle = ()
```

the catch with the brackets assignment is that if there is only one element python will assume the type of that element to be the variable type, not a tuple:

```
my_tuple = tuple([1]) // ok
my_tuple = (1) // my_tuple is now a integer

To overcome this issue, it is necessary to add a trailing comma to inform python that it is a tuple (but it only applied to tuples with one element)
my_tuple = (1,)
```

The main operations and methods on tuples are `count`, `index` and `len`.

Tuples also support destructuring operation in a similar fashion to javascript. In python it is called unpacking. The only detail is that all the positions of a tuple must have a related variable on the left side of the assignment operator:

```
code, text, payload = tuple([200, "ok", "res body"]) 

code, text = tuple([200, "ok", "res body"]) 
```

### Sets

Sets are cointainers that do not allow elements duplication and is very efficient when looking up elements. The efficiency stems from its hashing mechanism when storing a new elements to prevent duplication. It also allows the sets to directly find an element instead of going one by one looking for the one that is needed.

Unlike lists, sets do not guarantee order.

There are two ways of creating new sets. 1. using the api built-in method `set` or 2. using curly braces signal.

```
my_set = set()
my_set = set([1, 2, 1])

my_set = {}
my_set = {1, 2, 1}
```

The main methods and operations on `sets` are:

1. `add` to add a new element to the set (`my_set.insert(element)`)
2. `remove` to remove an element from the set (`my_set.remove(element)`) - returns an error when the element is not present
3. `discard` to remove an element from the set (`my_set.discard(element)`) - does not return an error when the element is not present
4. `update` to join two sets (`my_set.update(list | tuple | set)`)
5. `in` to check if an element is part of the set (`element in my_set`) - it returns a boolean
6. `union` to join two sets (`my_set.union(other_set)`). It also works with | pipe (`my_set | other_set`) - both are not in-place operations and return a new set.
7. `interserction` to get the elements that appear on both sets (`my_set.intersection(other_set)`). It also works with & ampersand (`my_set & other_set`). It is also not an in-place operation.
8. `symmetric_difference` to get elements that are not on both sets (`my_set.difference(other_set)`). It also works with ^ circumflex (`my_set ^ other_set`). It is also not an in-place operation.
h

Sets use the built-in `hash` method (`hash(element)`).  

### Dictionaries

Dictionary is a data structure that allows data to be saved as a key value pair. Like sets, dictionaries are efficient when verifying if a given 
key is part of the dataset because the keys are hashed and can be directly accessed in opposition of going one element by one like lists.
Keys can only be of immutable types.

There are two ways of creating dictionaries: 1. using the built-in method dict or 2. using curly braces:

```
my_dict = {}
my_dict = {"key": "value:}
my_dict = dict()
```

Main methods and operations on a dictionary:

1. Values of a dictionary can be accessed by the square bracket notation with the wanted key (`my_dict[my_key]`). If that key does not exist a type error is returned.
2. To avoid the noisy type error, it is possible to use the method `get` to get the value of a key. And in case that key does not exist, nothing is return but also no error is raised (`my_dict.get(my_key)`). The get method supports a default value in case that key does not have any value stored yet. It is a second argument with the default value after the key.
3. To add new values, use the square brackets notation with the key that needs to be included on the left side of the assigment operator and the value on the right. 
4. `in` to check if a key is present in the dictionary (`key in my_dict`).
5. `update` to join two dictionaries (`my_dict.update(other_dict)`)
6. `keys` to get all the keys of a dictionary
7. `values` to get all the values
8. `items` to get the key value pair - as a tuple

### Booleans

Python has two built-in boolean types: True and False. It also has a built-in method `bool(element)` that returns if a given value will be evaluated to true or false - truthiness. Examples: `bool("")` or `bool("a")`.

Truthiness:

- Numbers: only zero is evaluated to falsy. Everything else, including negative ones, are evaluated to truthy.
- Strings: empty string is evaluated to falsy. Everything else to truthy.
- Empty containers are evaluated to falsy. Populated containers to truthy.
- None type is evaluated to falsy

Comparisons:

When comparing strings, it is important to remeber that python compares them lexicographically (it means by underlying ascii of the charactes).
It is important to keep in mind that capital letters come before lower case ones. When two strings are compared, each character is compared one by one until a difference is found.

```
"T" < "t" // true
"t" < "T" // false
"a" < "b" // true
"TT" == "Tt" // false
"TT" != "Tt" // true
```

Containers are compared also using equals and not equals notation:

```
[0, 1, 2] == [1, 2, 3] // false
[0, 1, 2] != [1, 2, 3] // false
```

To check if two objects are stored in the same memory location, it is necessary to use the keyword `is`.
`Equality vs Identity`.

```
a = [1, 2, 3]
b = [1, 2, 3]

a is b // false

// the opposite is `is not`.
a is not b // true
```

We have to be careful when using AND and OR operators on boolean expressions using truthiness.

```
False and True // returns false
True and True // returns true

[1] and [2] // returns [2]
[1] and {} // returns {}
[] and {1, 2} // returns []

// however
False or True // returns true
True or False // returns true

[1] or [2] // returns [1]
[] or {} // returns {}
(1,) or {} // return (1,)
```
To reverse a boolean expression result, just use the `not` keyword.

### Looping over lists

The simplest way to loop over a list is to use the control flow FOR operation:
```
colours = ['Red', 'White', 'Black']
for colour in colours:
    print(colour) 
```

To iterate over a range, python has a built-in method that returns a range in an efficient way (when the elements are necessary):
```
for number in range(1, 10, 2): // the first parameter is the start number, the second the end number (non inclusive) and the third the step 
    print(number) 
```

If you need to iterate over a list and also have the iteration index at the same time, python has a built-in convenience method named `enumerate()` that return a tuple - first the index, second the value.

```
colours = ['Red', 'White', 'Black']
for i, colour in enumerate(colours):
    print(f"Index {i} colour {colour}")
```

### Looping over dictionaries
Looping over dictionaries is very similar to looping over lists. The only thing to be aware of is that if you iterate directly on the dictionary's variable, you will be iterating over the keys. To iterate over the values you would have to call the `value` method and over both at the same time `items`. 

Unpacking (destructuring) works when iterating over items, as it return a list of tuples (key / value). Enumerating also works with dictionaries.

### Loop with List comprehensions
List comprehensions is a shortcut syntax that reduces repetition of commonly used operations on lists.
The syntax is `[operation for variable in list]`

```
names = ["Gabriel", "Mary", "Bob", "Don"]
[name.upper() for name in names]

#returns squares of the number 1 to 5.
[number * number for number in range(1, 6)]

# returns a tuple
[("length", len(name)) for name in names]

# returns a string with the list comprehension's result (that is a f string) joined by commas 
", ".join([f"Name is {name}" for name in names])
```

#### Conditionals statements in list comprehensions

Conditionals statements in list comprehensions make it way more powerful. To add a conditional just place the if statement after the elements definition (on the right side)

```
# it will only add the even squares to the final list 
[num * num for num in range(10) if num % 2 == 0]
```

### List operations

- sum is a built in method that sum up the values of any numbers `sum(list)`.
- min and max methods are self explanatory
- sorted to sort a list ascendingly and with the parameter `reverse=True` to sort descendingly (sorted in reverse)

### Comprehension on other containers datatypes

Dicts, sets and tuples also have comprehensions. The main difference is that instead of using the list notation it is necessary their own notation. E.g for sets {... for var in element}, dicts {... for var in key: value} 

```
# set comprehension
{num * num for num in range(6)}

# dict comprehension
{item[0]: item[1] * item[1] for item in {"one": 1, "two": 2, "three": 3}.items()}

```

### Comprehension efficiency with generators

Comprehensions build the whole container in memory what could be inneficient for big data sets. 
Python 3 created the concept of generators where values are generated when they are neceesary (kinda just in time), preventing the whole dataset to go into memory at once.

To create a generator, just replace the comprehension type notation (eg square brackets for list) by regular brackets.

```
generator_comprehension = (num * num for num in range(100))
for num in generator_comprehension:
    print(num)

set(num * num for num in range(100))
```

### Slicing lists

```
my_string = "Hello, World!" # strings are a list of characters!
my_string[0] # returns "H"
my_string[-1] # returns "!"
my_string[1:3] # returns "el"
my_string[1:] # returns from position 1 till the end
my_string[:3] # returns from position 0 till position 3 (no inclusive)
my_string[-3: -1] # returns "ld" - two characters before the last
my_string[-3:] # returns "ld!" - the last three characters

# for actual lists it works the same

my_list = ["Dob", "Bob", "Mary"]
new_list = my_list[:] # it gives a copy of the list
new_list = my_list # points to the same list in memory

my_list[::2] #the last parameter is the step. In this case it just returns every other one.
my_list[::-1] # return the list backwards.
```

### Zip Function

Zip function joins two lists into one list of tuples.
```
players = ["Mary", "Don", "Bob"]
scores = [10, 8, 9]
zip(players, scores) # returns a zip object, similar to a generator. The data structure is a list of tuples

# looping over the zip
for item in zip(players, scores):
    print(item)

# looping over the zip unpacking the tuple
for name, score in zip(players, scores):
    print(name, score)

# using dict comprehension to transform the zip back into dict
{item[0]: item[1] for item in  zip(players, scores)}

# using dict comprehension with tuple unpacking
{name: score for name, score in  zip(players, scores)}
```

### External (third party) libraries

To install external libraries it is necessary to use pip (python's package management system). Example of usage:
`python -m pip install requests`

## Object Oriented Programming in Python
OOP paradigme (or programming model)

### Classes
To use classes in REPL keep the class files in the root directory of the project. Then import it using the command `from file import Class` and use it.

```
from cars import Car
my_subaru = Car()
my_subaru.start("Subaru")
```

To reload classes on REPL, follow the next steps:
1. `import importlib`
2. import the file(s) as a module (`import cars`) not as an specific import (from cars import Car)
3. configure importlib to reload the module (`importlib.reload(cars)`)

`self` keyword refers to an instance.
`cls` means that is a class method.

#### Initializer methods (or constructors)

Initializer methods are defined by the dunder init (__init__) as takes at lest one mandatory argument: `self`.

```
def __init__(self, name):
    print("test")
    self.name = name
```

#### class methods
To create a class method you have to decorate the method with `@classmethod` declare the method as usual but receive a argument `cls` instead of `self`.

### Exception(s) and exception handling

Hierarchy: built-in exceptions extend from BaseException. Custom exceptions should not directly inherit from BaseException but from Exception instead. Exception is meant for all built-in and non built-in exceptions that are non-exiting exceptions.
*Never catch BaseException.*

Exception handling:
It follows a very similar approach to any other language. A `try` block followed by a `except` (catch) one that declares which type of exception it is meant to capture. It is also possible to declare a variable to get the error and traceback:

```
not_a_number = 'a'
try:
    int(not_a_number)
except ValueError:
    print("Not a number!")

# labelling the rror
try:
    int(not_a_number)
except ValueError as e:
    print("Not a number!", e)
```

To catch multiple errors at the same type provide a tuple with the errors in place of the single error - important to catch the more specific ones first and the more generic ones after.

```
my_map = {1:1}
user_input = 3
try:
    my_map[user_input]
except (ValueError, KeyError):
    print("something unexpected")
```

It is possible to stack multiple excepts to have more fine grained handling.

#### Custom Exceptions
To create custom exceptions, simply extend from Exception:

```
class MyCustomException(Exception):
    pass
```

And to use them, just use them as you would built-in exceptions with the raise keyword - `raise MyCustomException()`.

```
class IncorrectValueError(Exception):
    def __init__(self, value):
        message = f"Got a bad value: {value}"
        super().__init__(message)

# use:
my_val = 999
if my_val > 998:
    raise IncorrectValueError(my_val)
```

### Libraries and Modules

#### Standard library

Python comes with a comprehensive library set out of the box and is immediately available - python has been designed to be `bateries included`. Some of the standard libraries are: datetime, random, sys, os, math, json, etc

#### Modules and imports

Python 3 does not required a dunder `__init__.py` to create a new module, but it can still be useful.

To create a new module, just create a folder and add a `__init__.py` file in it. Python will automatically recognize it as a module. Then import it in another file. Example:

```
# module: my_math_functions/__init__.py it contains a `add_numbers` function

import my_math_functions
...
my_math_functions.add_numbers(1, 2)

# or 
from my_math_functions import add_numbers
...
add_numbers(1, 3)

# or - but don't do it
from my_math_functions import *
...
add_numbers
```

In case of multiple subfolders, just declare the path accordingly on the import declarations from the root directory (in case there is no `__init__.py` file, you have to include the file name as well):

```
import another_maths_functions.with_sub_folder.my_maths
...
another_maths_functions.with_sub_folder.my_maths.sub(1,2)

# or only import one function
from another_maths_functions.with_sub_folder.my_maths import sub
...
sub(30,3)

# or
from another_maths_functions.with_sub_folder import my_maths
...
my_maths.sub(1,2)
```

It is possible to label imports to make them easier to identify:

```
from pprint import pprint as pp
pp({"a":"a","b":"b"})
```

#### Using external packages

PIP tool is used to install external packages. To browse through third party packages go to `pypi.org` and use the search bar (like maven repository) - there you can find more information about maintainers, statistics and installation instructions.

Example: To install Requests package just run the command `python -m pip install requests`. It runs pip as a module from the virtual environment to avoid conflict of versions. To use, just import in a python file `import requests`.

*Be careful with typo squatters!* Typing the wrong package name could mean installing packages with vunerability issues.

### Notes

- The default repository for third party libs is PyPI (Package Index)
- The most important convention is PEP8. Using a linter that enforce the globally accepted style, it will help stardarisation.
- null in python is None. `x = None`