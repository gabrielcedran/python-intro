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
9. 


### Notes

- The default repository for third party libs is PyPI (Package Index)
- The most important convention is PEP8. Using a linter that enforce the globally accepted style, it will help stardarisation.
- null in python is None. `x = None`