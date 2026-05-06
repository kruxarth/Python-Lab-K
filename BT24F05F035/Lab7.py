user = input("Enter your name: ")
print("Welcome,", user)

str_num = "100"
int_num = int(str_num)
flt_num = float(str_num)

print("Integer:", int_num)
print("Float:", flt_num)

print("Type of str_num:", type(str_num))
print("Type of int_num:", type(int_num))

import math
value = 16

print("Square root:", math.sqrt(value))
print("Power:", math.pow(2, 3))
print("Ceil:", math.ceil(4.3))
print("Floor:", math.floor(4.7))

arr = [10, 20, 30, 40, 50]

print("Length:", len(arr))
print("Max:", max(arr))
print("Min:", min(arr))
print("Sum:", sum(arr))

nums = [1, 2, 3, 4, 5]

squares = [n**2 for n in nums]
print("Squares:", squares)

even = [n for n in nums if n % 2 == 0]
print("Even Numbers:", even)

from functools import reduce
total = reduce(lambda a, b: a + b, nums)
print("Sum using reduce:", total)