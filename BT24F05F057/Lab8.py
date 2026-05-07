# Practical 8 — Creating User Defined Functions in Python
# Aim: To create and implement user defined functions in Python.

# 1. Basic function
def area_rectangle(l, w):
    return l * w

print("Area:", area_rectangle(5, 3))

# 2. Default argument
def greet(name, msg="Hello"):
    return f"{msg}, {name}!"

print(greet("Adarsh"))                   # uses default msg
print(greet("Subham sir", "Good Morning"))     # custom msg

# 3. *args — variable length arguments
def add_all(*nums):
    print(f"Sum of {len(nums)} numbers:", sum(nums))

add_all(1, 2, 3)
add_all(10, 20, 30, 40)

# 4. **kwargs — keyword arguments
def student_profile(**info):
    print("\nStudent Profile:")
    for key, val in info.items():
        print(f"  {key:<12}: {val}")

student_profile(name="Alice", roll=101, grade="A")

# 5. Lambda functions
cube    = lambda x: x ** 3
is_even = lambda x: x % 2 == 0

print("\nCube of 4:", cube(4))
print("Is 7 even :", is_even(7))

# 6. Recursive function — Factorial
def factorial(n):
    if n <= 1:
        return 1            # base case
    return n * factorial(n - 1)   # recursive call

for i in range(1, 7):
    print(f"  {i}! = {factorial(i)}")
