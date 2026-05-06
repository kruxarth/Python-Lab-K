def add(a, b):
    return a + b

# function to check even or odd
def check_even_odd(num):
    if num % 2 == 0:
        print("Number is Even")
    else:
        print("Number is Odd")
# function to find factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("\nAddition:", add(x, y))

num = int(input("\nEnter a number to check even/odd: "))
check_even_odd(num)

n = int(input("\nEnter a number to find factorial: "))
print("Factorial:", factorial(n))