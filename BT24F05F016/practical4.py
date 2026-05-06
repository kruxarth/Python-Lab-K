a = 20
b = 6

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

x = 10
y = 20

print("Equal:", x == y)
print("Not Equal:", x != y)
print("Greater:", x > y)
print("Less:", x < y)

p = True
q = False

print("AND:", p and q)
print("OR:", p or q)
print("NOT:", not p)

age = 25
income = 50000
print("Age check:", age >= 18 and income >= 40000)

num = 10
num += 5
print("After += 5:", num)

num -= 3
print("After -= 3:", num)

num *= 2
print("After *= 2:", num)

m = 12
n = 10
print("Bitwise AND:", m & n)
print("Bitwise OR:", m | n)
print("Bitwise XOR:", m ^ n)
print("Left Shift:", m << 2)
print("Right Shift:", m >> 2)

list1 = [1, 2, 3, 4, 5]
print("3 in list:", 3 in list1)
print("7 not in list:", 7 not in list1)

var1 = [1, 2, 3]
var2 = [1, 2, 3]
var3 = var1

print("var1 == var2:", var1 == var2)
print("var1 is var2:", var1 is var2)
print("var1 is var3:", var1 is var3)

str1 = "Hello"
str2 = "World"
print("Concatenation:", str1 + " " + str2)
print("Repetition:", str1 * 3)

result1 = 2 + 3 * 4
result2 = (2 + 3) * 4
print("2 + 3 * 4 =", result1)
print("(2 + 3) * 4 =", result2)

price = 100
discount = 0.10
quantity = 3
total = price * (1 - discount) * quantity
print("Total price:", total)
