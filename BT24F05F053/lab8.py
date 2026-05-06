def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero not allowed"
    return a / b

print("----- SIMPLE CALCULATOR USING FUNCTIONS -----")
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Addition =", add(x, y))
print("Subtraction =", subtract(x, y))
print("Multiplication =", multiply(x, y))
print("Division =", divide(x, y))

print("\n----- FUNCTION TO CHECK EVEN/ODD -----")
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter number to check even/odd: "))
print(num, "is", check_even_odd(num))

print("\n----- FUNCTION TO FIND FACTORIAL -----")
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

n = int(input("Enter number to find factorial: "))
print("Factorial of", n, "=", factorial(n))