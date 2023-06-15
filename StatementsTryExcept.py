"""
This is a tutorial on break, continue, and error handling in Python.
"""

# Break statement
for i in range(1, 6):
    if i == 4:
        break
    print(i)

"""
Explanation:
The `break` statement is used to exit a loop prematurely. In this example, the `for` loop iterates over the numbers 1 to 5.
On each iteration, the current value of `i` is checked. If `i` is equal to 4, the `break` statement is encountered, and the loop is terminated.
As a result, the numbers 1, 2, and 3 are printed, but the loop exits before reaching 4 and 5.
"""

# Continue statement
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

"""
Explanation:
The `continue` statement is used to skip the remaining code in a loop's block for the current iteration and move on to the next iteration.
In this example, the `for` loop iterates over the numbers 1 to 5.
When `i` becomes 3, the `continue` statement is encountered, causing the loop to skip the subsequent `print` statement.
The loop continues to the next iteration, printing the numbers 1, 2, 4, and 5.
"""

# Error handling with try-except
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
