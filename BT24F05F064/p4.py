practical 4 : operator in python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\nArithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponent:", a ** b)
print("Floor Division:", a // b)

print("\nComparison Operators")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

print("\nLogical Operators")
print("(a > 0 and b > 0):", a > 0 and b > 0)
print("(a > 0 or b > 0):", a > 0 or b > 0)
print("not(a > b):", not(a > b))

print("\nAssignment Operators Demo")
c = a
c += b
print("c += b:", c)
c -= b
print("c -= b:", c)
c *= b
print("c *= b:", c)
