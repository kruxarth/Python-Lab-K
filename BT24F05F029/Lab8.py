# 1. BASIC FUNCTION
def greet():
    print("Hello, User!")

greet()

# 2. FUNCTION WITH PARAMETERS
def add(a, b):
    return a + b

print("Sum:", add(5, 3))

# 3. DEFAULT ARGUMENT FUNCTION
def power(base, exp=2):
    return base ** exp

print("Square:", power(4))        # uses default exp=2
print("Cube:", power(4, 3))       # overrides default

# 4. *args (VARIABLE LENGTH ARGUMENTS)
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print("Sum of multiple values:", sum_all(1, 2, 3, 4, 5))

# 5. **kwargs (KEYWORD ARGUMENTS)
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

display_info(name="Alice", age=20, city="Delhi")

# 6. LAMBDA FUNCTION (ANONYMOUS FUNCTION)
square = lambda x: x ** 2
print("Square using lambda:", square(5))

# Lambda with multiple arguments
add_lambda = lambda a, b: a + b
print("Addition using lambda:", add_lambda(3, 7))