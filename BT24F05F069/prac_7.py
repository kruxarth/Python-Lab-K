# INPUT AND PRINT FUNCTION
name = input("Enter your name: ")
print("Welcome,", name)

# TYPE CASTING & TYPE CHECKING
x = "250"

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

num = 49

print("Square root:", math.sqrt(num))
print("Power:", math.pow(5, 2))
print("Ceil:", math.ceil(8.1))
print("Floor:", math.floor(8.9))

# SEQUENCE FUNCTIONS
lst = [5, 15, 25, 35, 45]

print("Length:", len(lst))
print("Max:", max(lst))
print("Min:", min(lst))
print("Sum:", sum(lst))

# FUNCTIONAL PROGRAMMING FUNCTIONS
numbers = [2, 4, 6, 8, 10]

# map()
squares = list(map(lambda x: x**2, numbers))
print("Squares:", squares)

# filter()
even_numbers = list(filter(lambda x: x > 5, numbers))
print("Numbers > 5:", even_numbers)

# reduce()
from functools import reduce
total = reduce(lambda x, y: x * y, numbers)
print("Product using reduce:", total)