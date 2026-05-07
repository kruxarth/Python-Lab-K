# Complete Operators Program

print("----- OPERATORS DEMONSTRATION -----")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Arithmetic Operators
print("\n--- Arithmetic Operators ---")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponent:", a ** b)
print("Floor Division:", a // b)

# Comparison Operators
print("\n--- Comparison Operators ---")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Assignment Operators
print("\n--- Assignment Operators ---")
c = a
print("Initial c:", c)
c += b
print("c += b:", c)
c -= b
print("c -= b:", c)
c *= b
print("c *= b:", c)
c /= b
print("c /= b:", c)
c %= b
print("c %= b:", c)

# Logical Operators
print("\n--- Logical Operators ---")
print("a > 0 and b > 0:", a > 0 and b > 0)
print("a > 0 or b > 0:", a > 0 or b > 0)
print("not(a > 0):", not(a > 0))

# Bitwise Operators
print("\n--- Bitwise Operators ---")
print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)
print("~a:", ~a)
print("a << 1:", a << 1)
print("a >> 1:", a >> 1)

# Identity Operators
print("\n--- Identity Operators ---")
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print("x is y:", x is y)
print("x is z:", x is z)
print("x is not z:", x is not z)

# Membership Operators
print("\n--- Membership Operators ---")
list1 = [10, 20, 30, 40]
print("20 in list:", 20 in list1)
print("50 not in list:", 50 not in list1)