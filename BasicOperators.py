"""
This is a tutorial on decision making in Python.
"""

# Basic if statement
x = 5
if x > 0:
    print("x is positive.")

# if-else statement
y = -2
if y > 0:
    print("y is positive.")
else:
    print("y is non-positive.")

# if-elif-else statement
z = 0
if z > 0:
    print("z is positive.")
elif z < 0:
    print("z is negative.")
else:
    print("z is zero.")

# Nested if statements
a = 10
b = 5
if a > 0:
    print("a is positive.")
    if b > 0:
        print("b is also positive.")

# Flat if statements
c = 15
d = 20
if c > 0 and d > 0:
    print("Both c and d are positive.")

# Ternary conditional operator
e = 7
positive = True if e > 0 else False
print("e is positive:", positive)
