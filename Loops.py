"""
This is a tutorial on loops in Python.
"""

# While loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1

"""
Explanation:
The `while` loop executes a block of code repeatedly as long as the condition `count < 5` is true.
Here, `count` starts at 0, and in each iteration, it is printed and then incremented by 1.
The loop continues until `count` reaches 5, at which point the condition becomes false, and the loop terminates.
"""

# Do-while loop equivalent
count = 0
while True:
    print("Count:", count)
    count += 1
    if count >= 5:
        break

"""
Explanation:
In Python, there is no direct equivalent of a `do-while` loop like in some other programming languages.
However, we can achieve the same behavior using a `while True` construct and a conditional `break` statement.
In this example, the loop runs indefinitely (`while True`) until the condition `count >= 5` becomes true.
Inside the loop, the current value of `count` is printed, and then it is incremented by 1.
When `count` reaches 5 or greater, the `break` statement is executed, breaking out of the loop.
"""

# For loop with range()
for i in range(5):
    print("Number:", i)

"""
Explanation:
The `for` loop with `range(5)` is used to iterate over a sequence of numbers from 0 to 4 (5 exclusive).
In each iteration, the loop variable `i` takes the value of the current number from the sequence.
Here, `i` is printed on each iteration, producing the output of "Number: 0", "Number: 1", and so on, up to "Number: 4".
"""

# Enumerate() function
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print("Index:", index, "Fruit:", fruit)

"""
Explanation:
The `enumerate()` function is used to iterate over a sequence while keeping track of the index and value of each item.
In this example, the `fruits` list is iterated, and in each iteration, `index` receives the current index, and `fruit` receives the corresponding value.
The values of `index` and `fruit` are printed on each iteration, displaying the index and fruit name side by side.
"""

# Nested loop
for i in range(3):
    for j in range(2):
        print(f"Value of i: {i}, Value of j: {j}")

"""
Explanation:
A nested loop is a loop that appears inside another loop. In this example, there is an outer loop and an inner loop.
The outer loop iterates over the numbers 0, 1, and 2 (3 exclusive), and the inner loop iterates over the numbers 0 and 1 (2 exclusive).
In each iteration of the outer loop, the inner loop completes a full iteration, printing the values of `i` and `j`.
This results in the following output:
    Value of i: 0, Value of j: 0
    Value of i: 0, Value of j: 1
    Value of i: 1, Value of j: 0
    Value of i: 1, Value of j: 1
    Value of i: 2, Value of j: 0
    Value of i: 2, Value of j: 1
"""

# Flat loop
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = 0
for num in numbers:
    sum_of_numbers += num
print("Sum of numbers:", sum_of_numbers)

"""
Explanation:
The flat loop iterates over the `numbers` list, which contains the numbers 1, 2, 3, 4, and 5.
In each iteration, the loop variable `num` receives the current number from the list.
The loop adds the value of `num` to the `sum_of_numbers` variable, accumulating the sum of all the numbers in the list.
After the loop finishes, the total sum is printed as "Sum of numbers:" followed by the calculated sum.
"""
