# Practical 8 User Defined Functions

# 1. Basic function
def area_rectangle(length, width):
    return length * width
print("Area:", area_rectangle(5, 3))

# 2. Default argument
def greet(person, message="Hello"):
    return f"{message}, {person}!"
print(greet("Alice"))                        # uses default
print(greet("Bob", "Good Morning"))          # custom msg

# 3. *args
def add_all(*numbers):
    print(f"Sum of {len(numbers)} numbers:", sum(numbers))
add_all(1, 2, 3)
add_all(10, 20, 30, 40)

# 4. **kwargs
def student_profile(**details):
    print("\nStudent Profile:")
    for k, v in details.items():
        print(f" {k:<12}: {v}")
student_profile(name="Alice", roll=101, grade="A")

# 5. Lambda
cube_func = lambda n: n**3
even_check = lambda n: n % 2 == 0
print("\nCube of 4:", cube_func(4))
print("Is 7 even:", even_check(7))

# 6. Recursive Factorial
def factorial(num):
    if num <= 1: return 1                      # base case
    return num * factorial(num - 1)              # recursive call

for idx in range(1, 7):
    print(f"{idx}! = {factorial(idx)}")










    