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

*things to keep in mind*
Python allows you to override built-in types. If you do so, you lose that feature. Example:
```
list = 1 // list is not a list anymore, but a number
list(2) // it won't work because now it is an int
```
