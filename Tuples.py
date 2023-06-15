"""
This is a tutorial on tuples in Python.

Tuples are ordered, immutable, and can contain elements of different data types. They are defined using parentheses ().
"""

# Creating a tuple
fruits = ('apple', 'banana', 'cherry')
print("Fruits:", fruits)

# Accessing values in a tuple
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Updating a tuple (Not possible as tuples are immutable)

# Deleting a tuple
print("""# del fruits""")

print("""# print("Fruits after deletion:", fruits)  # This line will throw an error as the tuple is deleted""")

# Basic tuple operations
numbers1 = (1, 2, 3)
numbers2 = (4, 5, 6)
print("Numbers1:", numbers1)
print("Numbers2:", numbers2)

concatenated = numbers1 + numbers2
repeated = numbers1 * 3
print("Concatenated tuple:", concatenated)
print("Repeated tuple:", repeated)

# Iteration
for fruit in fruits:
    print("Fruit:", fruit)

# Tuple functions
print("Length of numbers1:", len(numbers1))
print("Maximum number in numbers2:", max(numbers2))
print("Minimum number in numbers1:", min(numbers1))
print("Converted to tuple:", tuple("Hello"))

