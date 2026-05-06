# INPUT AND PRINT FUNCTION
name = input("Enter your name: ")
print("Welcome,", name)

# TYPE CASTING & TYPE CHECKING
x = "100"

# Type casting
x_int = int(x)
x_float = float(x)

print("Integer:", x_int)
print("Float:", x_float)

# Type checking
print("Type of x:", type(x))
print("Type of x_int:", type(x_int))

# MATH FUNCTIONS
import math

num = 16

print("Square root:", math.sqrt(num))
print("Power:", math.pow(2, 3))
print("Ceil:", math.ceil(4.3))
print("Floor:", math.floor(4.7))

# SEQUENCE FUNCTIONS
lst = [10, 20, 30, 40, 50]

print("Length:", len(lst))
print("Max:", max(lst))
print("Min:", min(lst))
print("Sum:", sum(lst))

# FUNCTIONAL PROGRAMMING FUNCTIONS
numbers = [1, 2, 3, 4, 5]

# map()
squares = list(map(lambda x: x**2, numbers))
print("Squares:", squares)

# filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)

# reduce()
from functools import reduce
total = reduce(lambda x, y: x + y, numbers)
print("Sum using reduce:", total)