# Array Representation
"""
An array is a collection of elements of the same type, stored at contiguous memory locations. In Python, arrays are
represented using the 'array' module.
"""

import array as arr

# Creating an array
numbers = arr.array('i', [1, 2, 3, 4, 5])
print(f"numbers array :  {numbers}")
# 'i' represents the type code for signed integer

# Accessing elements of an array
print("Element at index 0:", numbers[0])
print("Element at index 3:", numbers[3])

# Array Operations
"""
Arrays support various operations such as traversal, insertion, deletion, search, and update.
"""

# Traversing an array
print("Array elements:")
for num in numbers:
    print(num)

# Inserting elements into an array
numbers.insert(2, 6)  # Insert 6 at index 2
print('# Insert 6 at index 2')
print(numbers)
numbers.append(7)     # Append 7 at the end
print('# Append 7 at the end')
print(numbers)

# Deleting elements from an array
numbers.remove(3)     # Remove element 3
print('# Remove element 3')
print(f"numbers = {numbers}")

del numbers[4]        # Delete element at index 4
print('# Delete element at index 4')
print(f"numbers = {numbers}")

# Searching for an element in an array
search_value = 5
print(f"search value : {search_value}")
if search_value in numbers:
    print(f"{search_value} found in the array")
else:
    print(f"{search_value} not found in the array")

# Updating elements in an array
numbers[1] = 8
print("change number index 2 to '8'")
print(f"number list = {numbers}")

# Finding the length of an array
print("Length of the array:", len(numbers))

# Array Concatenation
numbers2 = arr.array('i', [9, 10])
concatenated_array = numbers + numbers2

# Printing the concatenated array
print("Concatenated array:")
for num in concatenated_array:
    print(num)
