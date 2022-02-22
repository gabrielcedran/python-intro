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

### Tuples

### Notes

- The default repository for third party libs is PyPI (Package Index)
- The most important convention is PEP8. Using a linter that enforce the globally accepted style, it will help stardarisation.
- null in python is None. `x = None`