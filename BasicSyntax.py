"""
This is a basic syntax tutorial in Python.
"""

# Printing "Hello, World!"
print("Hello, World!") # This sned's to you console the words : Hello World! :

# Variable assignment and basic data types
message = "Hello, Python!"  # Assigning a string to the variable 'message'
number = 42  # Assigning an integer to the variable 'number'
pi = 3.14159  # Assigning a float to the variable 'pi'
is_python_fun = True  # Assigning a boolean value to the variable 'is_python_fun'

# Basic arithmetic operations
a = 10
b = 5
sum_result = a + b  # Addition
difference_result = a - b  # Subtraction
product_result = a * b  # Multiplication
quotient_result = a / b  # Division

# Conditional statements
if is_python_fun:
    print("Python is fun!")
else:
    print("Python is not fun.")

# Looping with a for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Defining a function
def square(number):
    """
    This function calculates the square of a number.

    Args:
        number (int): The number to be squared.

    Returns:
        int: The square of the input number.
    """
    return number ** 2

# Calling the function and printing the result
result = square(5)
print("Square:", result)
