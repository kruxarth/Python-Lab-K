practical 8 : User defined function
def greet(name):
    print("Hello", name)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

name = input("Enter your name: ")
greet(name)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Addition:", add(x, y))
print("Multiplication:", multiply(x, y))

num = int(input("Enter a number for factorial: "))
print("Factorial:", factorial(num))

check = int(input("Enter a number to check even or odd: "))
if is_even(check):
    print("Even number")
else:
    print("Odd number")
