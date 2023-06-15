"""
This is a tutorial on functions in Python.

A function is a block of code that performs a specific task. It allows you to break down your program into reusable pieces of code.

Defining a function:
---------------------
To define a function in Python, you use the `def` keyword followed by the function name and parentheses. You can also specify parameters inside the parentheses if the function takes any inputs.

Syntax:
-------
def function_name(parameters):
    # Function body

Calling a function:
-------------------
To call a function, you simply write its name followed by parentheses. If the function has parameters, you pass the values inside the parentheses.

Pass by reference vs pass by value:
-----------------------------------
In Python, function arguments are passed by reference. It means that if you modify the parameter inside the function, the original variable outside the function will also be modified. However, if you reassign the parameter to a new value inside the function, it will not affect the original variable.

Function *args and **kwargs:
----------------------------
In Python, you can define functions that accept a variable number of arguments using `*args` and `**kwargs`. `*args` allows you to pass a variable number of positional arguments, while `**kwargs` allows you to pass a variable number of keyword arguments.

Default arguments:
------------------
You can specify default values for function parameters. If the caller doesn't provide a value for that parameter, the default value will be used.

Variable-length arguments:
--------------------------
You can also define functions that accept a variable number of arguments without specifying their names using the `*` symbol. This allows you to pass any number of positional arguments to the function, which will be stored in a tuple.

Anonymous functions (Lambda functions):
--------------------------------------
Python allows you to create anonymous functions using the `lambda` keyword. These functions are typically used for small, one-line operations.

Return statement:
-----------------
The `return` statement is used to exit a function and return a value. It can be used to pass the result of a function back to the caller.

Scope of variables:
-------------------
Variables defined inside a function are considered local variables and can only be accessed within that function. Variables defined outside any function are considered global variables and can be accessed from anywhere in the program.

Global vs local variables:
--------------------------
If a local variable has the same name as a global variable, the local variable takes precedence within the scope of the function. To access the global variable inside a function, you can use the `global` keyword.

"""

# Defining a function
def greet(name):
    print("Hello, " + name + "!")

# Calling a function
greet("Alice")

# Pass by reference
def change_list(my_list):
    my_list.append(4)
    print("Inside the function:", my_list)

numbers = [1, 2, 3]
change_list(numbers)
print("Outside the function:", numbers)

# *args and **kwargs
def foo(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

foo(1, 2, 3, a=4, b=5)

# Default arguments
def multiply(a, b=2):
    return a * b

result1 = multiply(3)
result2 = multiply(3, 4)
print("Default arguments:", result1, result2)

# Variable-length arguments
def add(*args):
    total = 0
    for num in args:
        total += num
    return total

result = add(1, 2, 3, 4, 5)
print("Variable-length arguments:", result)

# Anonymous functions (Lambda functions)
square = lambda x: x ** 2
print("Square of 5:", square(5))

# Return statement
def sum_numbers(a, b):
    return a + b

result = sum_numbers(3, 4)
print("Sum:", result)

# Scope of variables
def my_function():
    x = 10
    print("Inside the function:", x)

my_function()
# print("Outside the function:", x)  # Raises an error

# Global vs local variables
count = 0

def increment():
    global count
    count += 1

increment()
print("Global count:", count)

