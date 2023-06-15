"""
This is a tutorial on dictionaries in Python.

Dictionaries are unordered, mutable, and store data in key-value pairs. They are defined using curly braces {}.
"""

# Creating a dictionary
student = {
    'name': 'John',
    'age': 20,
    'major': 'Computer Science'
}
print("Student:", student)

# Accessing values in a dictionary
print("Student name:", student['name'])
print("Student age:", student['age'])

# Updating values in a dictionary
student['age'] = 21
print("Updated student age:", student['age'])

# Adding a new key-value pair to a dictionary
student['university'] = 'ABC University'
print("Student with university:", student)

# Deleting a key-value pair from a dictionary
del student['major']
print("Student after deleting major:", student)

# Dictionary operations
print("Length of student dictionary:", len(student))

# Dictionary methods
keys = student.keys()
print("Keys:", keys)

values = student.values()
print("Values:", values)

items = student.items()
print("Items:", items)

# Iterating over a dictionary
for key, value in student.items():
    print(f"{key}: {value}")

# Dictionary functions
merged_dict = dict(student, **{'gpa': 3.8})
print("Merged dictionary:", merged_dict)

copied_dict = student.copy()
print("Copied dictionary:", copied_dict)

# Nested dictionaries
car = {
    'make': 'Ford',
    'model': 'Mustang',
    'year': 2022,
    'owner': {
        'name': 'Alice',
        'age': 25,
        'city': 'New York'
    }
}
print("Car:", car)
print("Car owner:", car['owner'])
print("Car owner name:", car['owner']['name'])
