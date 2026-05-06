# Basic function
def greet(name):
    return f"Hello, {name}!"

# Default argument
def power(base, exp=2):
    return base ** exp

# *args
def add_all(*args):
    return sum(args)

# **kwargs
def info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

# Lambda
square = lambda x: x * x

print(greet("Alice"))
print(power(3), power(2, 10))
print(add_all(1, 2, 3, 4))
info(name="Bob", age=20)
print(square(5))