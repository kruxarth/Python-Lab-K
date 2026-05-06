"""Practical 8: Functions - Basic, Parameters, Default Arguments, *args, **kwargs, and Lambda"""

# 1. Basic function without parameters
def greet():
    """Simple greeting function"""
    print("Hello, User!")

greet()

# 2. Function with parameters and return value
def add(a, b):
    """Add two numbers and return the sum"""
    return a + b

print("Sum:", add(5, 3))

# 3. Function with default argument
def power(base, exp=2):
    """Calculate base raised to the power of exp"""
    return base ** exp

print("Square:", power(4))        # uses default exp=2
print("Cube:", power(4, 3))       # overrides default

# 4. Function with *args (variable-length positional arguments)
def sum_all(*args):
    """Sum all provided arguments"""
    total = 0
    for num in args:
        total += num
    return total

print("Sum of multiple values:", sum_all(1, 2, 3, 4, 5))

# 5. Function with **kwargs (keyword arguments)
def display_info(**kwargs):
    """Display information passed as keyword arguments"""
    for key, value in kwargs.items():
        print(key, ":", value)

display_info(name="Alice", age=20, city="Delhi")

# 6. Lambda function (anonymous function)
square = lambda x: x ** 2
print("Square using lambda:", square(5))

# Lambda with multiple arguments
add_lambda = lambda a, b: a + b
print("Addition using lambda:", add_lambda(3, 7))