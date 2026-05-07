# User Defined Functions

def add(a, b):
    return a + b

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Main Program
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Addition:", add(x, y))

num = int(input("Enter number: "))
print("Factorial:", factorial(num))
print("Even/Odd:", even_odd(num))