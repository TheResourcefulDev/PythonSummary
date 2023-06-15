"""
This is a tutorial on variable types in Python.
"""

def variable_info(var):
    """
    This function provides information about a given variable.

    Args:
        var: The variable to inspect.

    Returns:
        str: Information about the variable's type, mutability, slicing capability, indexability, and index searching.
    """
    var_type = type(var).__name__
    mutable = "Yes" if isinstance(var, (list, set, dict)) else "No"
    slicing = "Yes" if isinstance(var, (str, list, tuple)) else "No"
    indexable = "Yes" if isinstance(var, (str, list, tuple, dict)) else "No"
    index_search = "Yes" if isinstance(var, (list, str, tuple)) else "No"

    info = f"Type: {var_type}\n"
    info += f"Mutable: {mutable}\n"
    info += f"Slicing: {slicing}\n"
    info += f"Indexable: {indexable}\n"
    info += f"Index Search: {index_search}\n"

    return info


# Integer
age = 25
print("Age:")
print(variable_info(age))
print()

# Float
pi = 3.14159
print("PI:")
print(variable_info(pi))
print()

# String
name = "John Doe"
print("Name:")
print(variable_info(name))
print()

# Boolean
is_python_fun = True
print("Is Python Fun?")
print(variable_info(is_python_fun))
print()

# List
fruits = ["apple", "banana", "cherry"]
print("Fruits:")
print(variable_info(fruits))
print()

# Tuple
person = ("John", 25, "USA")
print("Person:")
print(variable_info(person))
print()

# Dictionary
student = {"name": "John Doe", "age": 25, "country": "USA"}
print("Student:")
print(variable_info(student))
print()

# Set
numbers = {1, 2, 3, 4, 5}
print("Numbers:")
print(variable_info(numbers))
print()

# None
result = None
print("Result:")
print(variable_info(result))
print()

# Long
large_number = 1234567890123456789012345678901234567890
print("Large Number:")
print(variable_info(large_number))
print()

# Complex
complex_number = 1 + 2j
print("Complex Number:")
print(variable_info(complex_number))
print()
