import math
import random

"""
This is a tutorial on numbers in Python.
"""

# Integer
num_int = 10
print("Integer:", num_int)

# Long (No longer needed in Python 3)
# num_long = 1234567890123456789
# print("Long:", num_long)

# Float
num_float = 3.14
print("Float:", num_float)

# Complex
num_complex = 2 + 3j
print("Complex:", num_complex)

# Type conversion
x = 5
y = float(x)
z = complex(x)
print("Type Conversion: Int to Float - x:", x, "=> y:", y)
print("Type Conversion: Int to Complex - x:", x, "=> z:", z)

# Mathematical functions
num = -4.3
print("Absolute - num:", num, "=> abs(num):", abs(num))
print("Ceil - num:", num, "=> math.ceil(num):", math.ceil(num))
# print("Cmp:", cmp(num, 0))  # Deprecated in Python 3
print("Exponential - num:", num, "=> math.exp(num):", math.exp(num))
print("Absolute (Float) - num:", num, "=> math.fabs(num):", math.fabs(num))
print("Floor - num:", num, "=> math.floor(num):", math.floor(num))
print("Logarithm - math.e:", math.e, "=> math.log(math.e):", math.log(math.e))
print("Logarithm (Base 10) - num:", 1000, "=> math.log10(1000):", math.log10(1000))
print("Maximum:", 3, 6, 2, 9, "=> max(3, 6, 2, 9):", max(3, 6, 2, 9))
print("Minimum:", 3, 6, 2, 9, "=> min(3, 6, 2, 9):", min(3, 6, 2, 9))
print("Modulus - num:", num, "=> math.modf(num):", math.modf(num))
print("Power - base:", 2, "exponent:", 3, "=> math.pow(2, 3):", math.pow(2, 3))
print("Rounded Value - num:", num, "=> round(num):", round(num))
print("Square Root - num:", 25, "=> math.sqrt(25):", math.sqrt(25))

# Random number functions
number_list = [1, 2, 3, 4, 5]
print("Random Choice - number_list:", number_list, "=> random.choice(number_list):", random.choice(number_list))
print("Random Range:", 1, 10, "=> random.randrange(1, 10):", random.randrange(1, 10))
print("Random Float:", "=> random.random():", random.random())
# random.seed(10)  # Uncomment to seed the random number generator
shuffled_list = number_list.copy()
random.shuffle(shuffled_list)
print("Random Shuffle - number_list:", number_list, "=> shuffled_list:", shuffled_list)
print("Random Uniform:", 1, 10, "=> random.uniform(1, 10):", random.uniform(1, 10))

# Trigonometric functions
angle = 45
print("Cosine - angle:", angle, "=> math.cos(math.radians(angle)):", math.cos(math.radians(angle)))
print("Sine - angle:", angle, "=> math.sin(math.radians(angle)):", math.sin(math.radians(angle)))
print("Tangent - angle:", angle, "=> math.tan(math.radians(angle)):", math.tan(math.radians(angle)))
print("Arc Cosine - 0.5:", "=> math.acos(0.5):", math.acos(0.5))
print("Arc Sine - 0.5:", "=> math.asin(0.5):", math.asin(0.5))
print("Arc Tangent - 1:", "=> math.atan(1):", math.atan(1))
print("Arc Tangent 2 - x:", 1, "y:", 1, "=> math.atan2(1, 1):", math.atan2(1, 1))
print("Degrees to Radians - angle:", 180, "=> math.radians(180):", math.radians(180))
print("Radians to Degrees - math.pi:", math.pi, "=> math.degrees(math.pi):", math.degrees(math.pi))

# Mathematical constants
print("Pi:", math.pi)
print("E:", math.e)
