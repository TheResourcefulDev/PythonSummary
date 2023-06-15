"""
This is a tutorial on lists in Python.
"""

# Accessing values in a list
fruits = ['apple', 'banana', 'cherry']
print("Fruits:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Updating lists
fruits[1] = 'orange'
print("fruits[1] = 'orange'")
print("Updated fruits:", fruits)

# Deleting elements from a list
del fruits[0]
print("del fruits[0]")
print("Fruits after deletion:", fruits)

# Basic list operations
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
print("Numbers1:", numbers1)
print("Numbers2:", numbers2)

concatenated = numbers1 + numbers2
repeated = numbers1 * 3
print("Concatenated list:", concatenated)
print("Repeated list:", repeated)

# Membership check
print("Is 2 in numbers1?", 2 in numbers1)
print("Is 7 in numbers2?", 7 in numbers2)

# Iteration
for fruit in fruits:
    print("List Iteration : ")
    print("Fruit:", fruit)

# Slicing a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Numbers:", numbers)
print("Slice from index 2 to 6:", numbers[2:6])
print("Slice from index 5 to end:", numbers[5:])
print("Slice from start to end:", numbers[:])
print("Reverse list:", numbers[::-1])

# List functions
print("Length of numbers:", len(numbers))
print("Maximum number:", max(numbers))
print("Minimum number:", min(numbers))
print("Converted to list:", list("Hello"))

# List methods
grape = 'grape'
print("Grape:", grape)
fruits.append(grape)
print(f"Fruits after append: {fruits}")

print("Count of 'orange' in fruits:", fruits.count('orange'))

added_fruits = ['mango', 'pineapple']
print("Added fruits:", added_fruits)
fruits.extend(added_fruits)
print(f"Fruits after extend: {fruits}")

print("Index of 'cherry' in fruits:", fruits.index('cherry'))

inserted_fruit = 'pear'
fruits.insert(1, inserted_fruit)
print("Inserted fruits:", inserted_fruit)
print(f"Fruits after insert: {fruits}")

popped = fruits.pop()
print("Popped fruit:", popped)
print(f"Fruits after pop: {fruits}")

removed_fruit = 'orange'
print("Removed fruit:", removed_fruit)
fruits.remove(removed_fruit)
print(f"Fruits after remove: {fruits}")

fruits.reverse()
print(f"Reversed fruits: {fruits}")

fruits.sort()
print(f"Sorted fruits: {fruits}")
