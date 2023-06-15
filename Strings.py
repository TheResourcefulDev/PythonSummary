"""
This is a tutorial on strings in Python.
"""

# Accessing values in a string
text = "Hello, World!"
print("Text:", text)
print("First character:", text[0])
print("Last character:", text[-1])
print("Second to last character:", text[-2])

# Slicing a string
print("Slice from index 1 to 7:", text[1:7])
print("Slice from index 7 to end:", text[7:])
print("Slice from start to end:", text[:])
print("Reverse string:", text[::-1])

# Updating strings
greeting = "Hello"
name = "Alice"
message = f"{greeting}, {name}!"
print("Message:", message)

# Escape characters
print(f"Newline: {{\\n}} = Hello\nWorld!")
print(f"Tab: {{\\t}} = Hello\tWorld!")
print(f"Backslash: {{\\\}} = Hello\\World!")
print(f"Single Quote: {{\\'}} = \'Hello, World!\'")
print(f"Double Quote: {{\\\"}} = \"Hello, World!\"")


# String formatting using %
age = 25
print(f"My age is {age}")

percentage = 75.5
print(f"Percentage: {percentage:.2f}%")

# String formatting using .format()
quantity = 10
price = 5.99
total = quantity * price
print(f"Total: {total}")

# String formatting using f-strings (Python 3.6+)
name = "Alice"
age = 25
print(f"Name: {name}, Age: {age}")

# Other format conversions
print(f"Character: {chr(65)}")
print(f"String: {'Hello'}")
print(f"Integer: {10}")
print(f"Unsigned integer: {abs(-10)}")
print(f"Octal: {oct(10)}")
print(f"Lowercase hexadecimal: {hex(10)}")
print(f"Uppercase hexadecimal: {hex(10).upper()}")
print(f"Exponential notation: {1e3}")
print(f"Exponential notation (uppercase): {1e3:.2E}")
print(f"Floating-point decimal: {3.14}")
print(f"General format: {3.14:g}")
print(f"General format (uppercase): {3.14:G}")

# Additional formatting options
print(f"Left-aligned: {'Hello':<10}")
print(f"Right-aligned: {'Hello':>10}")
print(f"Zero-padding: {42:05}")
print(f"Custom separator: {'Python'}")

# Triple quotes
multiline = """This is a
multiline
string."""
print("Multiline:", multiline)

# Unicode string
unicode_str = "\u0394\u03b1\u03b9\u03b5\u03c4\u03b5"
print("Unicode String:", unicode_str)
