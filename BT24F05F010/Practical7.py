"""Practical 7: Built-in Functions, Type Casting, and Functional Programming"""

import math
from functools import reduce

# Input and welcome message
user_name = input("Enter your name: ")
print("Welcome,", user_name)

# Type casting and type checking
string_num = "100"

# Convert string to other data types
int_num = int(string_num)
float_num = float(string_num)

print("Integer:", int_num)
print("Float:", float_num)

# Type checking
print("Type of string_num:", type(string_num))
print("Type of int_num:", type(int_num))

# Math functions
value = 16

print("Square root:", math.sqrt(value))
print("Power:", math.pow(2, 3))
print("Ceil:", math.ceil(4.3))
print("Floor:", math.floor(4.7))

# Sequence functions on list
data_list = [10, 20, 30, 40, 50]

print("Length:", len(data_list))
print("Max:", max(data_list))
print("Min:", min(data_list))
print("Sum:", sum(data_list))

# Functional programming functions
numbers = [1, 2, 3, 4, 5]

# map() - apply function to each element
squares = list(map(lambda x: x ** 2, numbers))
print("Squares:", squares)

# filter() - filter elements based on condition
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)

# reduce() - aggregate values
total = reduce(lambda x, y: x + y, numbers)
print("Sum using reduce:", total)