"""
This is a tutorial on modules and imports in Python.

Modules:
--------
A module is a file containing Python code that defines functions, classes, and variables. It allows you to organize your code into logical units and promotes code reusability.

Import statements:
------------------
To use code from a module in your program, you need to import it. There are different ways to import modules in Python:

1. `import module_name`: Imports the entire module. You can access its content using the module name as a prefix.

2. `import module_name as alias`: Imports the module and assigns it an alias. You can use the alias instead of the module name to access its content.

3. `from module_name import name1, name2`: Imports specific functions, classes, or variables from the module. You can use them directly without the module name prefix.

4. `from module_name import *`: Imports all names from the module. This is generally discouraged as it may lead to naming conflicts.

Locating modules:
-----------------
Python searches for modules in the directories listed in the `sys.path` list. You can also add additional directories to this list by modifying the `PYTHONPATH` environment variable.

Namespace and scoping:
----------------------
When you import a module, it creates a new namespace for that module, separate from the global namespace. This allows you to have functions, variables, or classes with the same name in different modules without conflicts.

`dir()`, `globals()`, and `locals()`:
-------------------------------------
The `dir()` function returns a list of names in the current namespace or the names of an object if provided as an argument. `globals()` returns a dictionary of global variables, and `locals()` returns a dictionary of local variables.

Reloading modules:
------------------
If you make changes to a module after it has been imported, you can use the `reload()` function from the `importlib` module to reload the module and apply the changes.

Packages:
---------
A package is a way to organize related modules into a directory hierarchy. A package is a directory that contains a special file called `__init__.py`. It can contain multiple sub-packages and modules.

"""

# Importing modules
import math
import random as rand
from datetime import datetime

# Using module content
print("Square root of 16:", math.sqrt(16))
print("Random number between 1 and 10:", rand.randint(1, 10))
print("Current date and time:", datetime.now())

# Locating modules
import sys

print("Directories in sys.path:")
for directory in sys.path:
    print(directory)

# Namespace and scoping
import module1
import module2

module1.foo()
module2.foo()

# dir(), globals(), and locals()
print("Names in the current namespace:")
for name in dir():
    print(name)

print("Global variables:")
globals_snapshot = globals().copy()  # Create a snapshot of the globals dictionary
for name, value in globals_snapshot.items():
    print(name, "=", value)

print("Local variables:")
locals_snapshot = locals().copy()  # Create a snapshot of the locals dictionary
for name, value in locals_snapshot.items():
    print(name, "=", value)


# Reloading modules
import importlib

import module3
module3.bar()

# Make changes to module3.py and save
importlib.reload(module3)
module3.bar()

# Packages
import package1.module4

package1.module4.baz()

