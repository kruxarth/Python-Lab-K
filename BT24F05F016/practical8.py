def greet():
    print("Hello, Welcome to Python Functions!")

greet()

def add_numbers(num1, num2):
    result = num1 + num2
    print(f"Sum of {num1} and {num2} is {result}")

add_numbers(10, 20)

def multiply(a, b):
    return a * b

product = multiply(7, 8)
print(f"Product: {product}")

def power(base, exponent=2):
    return base ** exponent

print(f"3 squared: {power(3)}")
print(f"2 cubed: {power(2, 3)}")

def get_user_info(name, age):
    message = f"Hello, {name}!"
    is_adult = age >= 18
    return message, is_adult

msg, adult = get_user_info("Alice", 25)
print(msg)
print(f"Is Adult: {adult}")

def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(f"Sum of 1,2,3: {sum_all(1, 2, 3)}")
print(f"Sum of 5,10,15,20: {sum_all(5, 10, 15, 20)}")

def print_student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_student_info(name="Bob", age=20, major="Computer Science")

def flexible_function(name, *args, **kwargs):
    print(f"Name: {name}")
    print(f"Additional args: {args}")
    print(f"Keyword args: {kwargs}")

flexible_function("Charlie", 1, 2, 3, color="blue", size="large")

square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

add = lambda x, y: x + y
print(f"5 + 3 = {add(5, 3)}")

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared_numbers}")

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(f"Is 17 prime? {is_prime(17)}")
print(f"Is 15 prime? {is_prime(15)}")

def factorial(n):
    if n < 0:
        return "Invalid input"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

print(f"Factorial of 5: {factorial(5)}")

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence

print(f"First 8 Fibonacci numbers: {fibonacci(8)}")

def reverse_string(text):
    return text[::-1]

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

test_string = "Python Functions"
print(f"Reversed: {reverse_string(test_string)}")
print(f"Vowel count: {count_vowels(test_string)}")

def find_maximum(numbers):
    if not numbers:
        return None
    return max(numbers)

def find_minimum(numbers):
    if not numbers:
        return None
    return min(numbers)

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

test_list = [10, 45, 23, 67, 34, 12]
print(f"Maximum: {find_maximum(test_list)}")
print(f"Minimum: {find_minimum(test_list)}")
print(f"Average: {calculate_average(test_list)}")

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

add_five = outer_function(5)
print(f"Inner function result: {add_five(10)}")

def greet_person(name: str, age: int) -> str:
    return f"Hello {name}! You are {age} years old."

print(greet_person("Diana", 28))

def power_recursive(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power_recursive(base, exponent - 1)

print(f"3^4 using recursion: {power_recursive(3, 4)}")


# ==============================================================================
# 2. FUNCTION WITH PARAMETERS
# ==============================================================================

def add_numbers(num1, num2):
    """Add two numbers and print the result."""
    result = num1 + num2
    print(f"Sum of {num1} and {num2} is {result}")

# Call with arguments
add_numbers(10, 20)
add_numbers(5, 15)


# ==============================================================================
# 3. FUNCTION WITH RETURN VALUE
# ==============================================================================

def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b

# Call function and store result
product = multiply(7, 8)
print(f"Product: {product}")


# ==============================================================================
# 4. FUNCTION WITH DEFAULT PARAMETERS
# ==============================================================================

def power(base, exponent=2):
    """
    Calculate power with default exponent of 2.
    
    Args:
        base: The base number
        exponent: The power (default = 2)
    
    Returns:
        The result of base raised to exponent
    """
    return base ** exponent

print(f"3 squared: {power(3)}")           # Uses default exponent=2
print(f"2 cubed: {power(2, 3)}")          # Uses custom exponent=3


# ==============================================================================
# 5. FUNCTION WITH MULTIPLE RETURN VALUES
# ==============================================================================

def get_user_info(name, age):
    """Return multiple values."""
    message = f"Hello, {name}!"
    is_adult = age >= 18
    return message, is_adult

msg, adult = get_user_info("Alice", 25)
print(msg)
print(f"Is Adult: {adult}")


# ==============================================================================
# 6. FUNCTION WITH *ARGS (Variable Number of Arguments)
# ==============================================================================

def sum_all(*numbers):
    """
    Sum any number of arguments.
    
    Args:
        *numbers: Variable length argument list
    
    Returns:
        Sum of all numbers
    """
    total = 0
    for num in numbers:
        total += num
    return total

print(f"Sum of 1,2,3: {sum_all(1, 2, 3)}")
print(f"Sum of 5,10,15,20: {sum_all(5, 10, 15, 20)}")


# ==============================================================================
# 7. FUNCTION WITH **KWARGS (Keyword Arguments)
# ==============================================================================

def print_student_info(**details):
    """
    Print student information using keyword arguments.
    
    Args:
        **details: Keyword arguments (key=value pairs)
    """
    for key, value in details.items():
        print(f"{key}: {value}")

print_student_info(name="Bob", age=20, major="Computer Science", gpa=3.8)


# ==============================================================================
# 8. FUNCTION WITH BOTH *ARGS AND **KWARGS
# ==============================================================================

def flexible_function(name, *args, **kwargs):
    """
    Demonstrate flexible function with all parameter types.
    
    Args:
        name: Required argument
        *args: Variable positional arguments
        **kwargs: Variable keyword arguments
    """
    print(f"Name: {name}")
    print(f"Additional args: {args}")
    print(f"Keyword args: {kwargs}")

flexible_function("Charlie", 1, 2, 3, color="blue", size="large")


# ==============================================================================
# 9. LAMBDA FUNCTIONS (Anonymous Functions)
# ==============================================================================

# Basic lambda function
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Lambda with multiple arguments
add = lambda x, y: x + y
print(f"5 + 3 = {add(5, 3)}")

# Lambda with map() function
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared_numbers}")

# Lambda with filter() function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")


# ==============================================================================
# 10. PRACTICAL EXAMPLES
# ==============================================================================

# Example 1: Check if a number is prime
def is_prime(num):
    """
    Check if a number is prime.
    
    Args:
        num: Integer to check
    
    Returns:
        True if prime, False otherwise
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(f"Is 17 prime? {is_prime(17)}")
print(f"Is 15 prime? {is_prime(15)}")


# Example 2: Calculate factorial
def factorial(n):
    """
    Calculate factorial of n.
    
    Args:
        n: Non-negative integer
    
    Returns:
        Factorial of n
    """
    if n < 0:
        return "Invalid input"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

print(f"Factorial of 5: {factorial(5)}")


# Example 3: Fibonacci sequence
def fibonacci(n):
    """
    Generate first n Fibonacci numbers.
    
    Args:
        n: Number of Fibonacci numbers to generate
    
    Returns:
        List of first n Fibonacci numbers
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence

print(f"First 8 Fibonacci numbers: {fibonacci(8)}")


# Example 4: String manipulation
def reverse_string(text):
    """Reverse a string."""
    return text[::-1]

def count_vowels(text):
    """Count vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

test_string = "Python Functions"
print(f"Reversed: {reverse_string(test_string)}")
print(f"Vowel count: {count_vowels(test_string)}")


# Example 5: List operations
def find_maximum(numbers):
    """Find maximum number in a list."""
    if not numbers:
        return None
    return max(numbers)

def find_minimum(numbers):
    """Find minimum number in a list."""
    if not numbers:
        return None
    return min(numbers)

def calculate_average(numbers):
    """Calculate average of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

test_list = [10, 45, 23, 67, 34, 12]
print(f"Maximum: {find_maximum(test_list)}")
print(f"Minimum: {find_minimum(test_list)}")
print(f"Average: {calculate_average(test_list)}")


# ==============================================================================
# 11. NESTED FUNCTIONS
# ==============================================================================

def outer_function(x):
    """Outer function with nested inner function."""
    
    def inner_function(y):
        """Inner function defined inside outer function."""
        return x + y
    
    return inner_function

add_five = outer_function(5)
print(f"Inner function result: {add_five(10)}")  # 5 + 10 = 15


# ==============================================================================
# 12. FUNCTION DOCUMENTATION AND TYPE HINTS (Python 3.5+)
# ==============================================================================

def greet_person(name: str, age: int) -> str:
    """
    Greet a person with their age information.
    
    Args:
        name (str): The person's name
        age (int): The person's age
    
    Returns:
        str: A greeting message
    
    Example:
        >>> greet_person("John", 30)
        'Hello John! You are 30 years old.'
    """
    return f"Hello {name}! You are {age} years old."

print(greet_person("Diana", 28))


# ==============================================================================
# 13. RECURSIVE FUNCTIONS
# ==============================================================================

def power_recursive(base, exponent):
    """Calculate power using recursion."""
    if exponent == 0:
        return 1
    else:
        return base * power_recursive(base, exponent - 1)

print(f"3^4 using recursion: {power_recursive(3, 4)}")


# ==============================================================================
# SUMMARY OF KEY CONCEPTS
# ==============================================================================
"""
KEY POINTS:
1. def keyword - Define a function
2. Parameters - Input variables for a function
3. Return statement - Return value from function
4. Default parameters - Set default values
5. *args - Accept variable positional arguments
6. **kwargs - Accept variable keyword arguments
7. Lambda - Anonymous functions for simple operations
8. Docstrings - Document your functions with triple quotes
9. Type hints - Specify expected parameter and return types
10. Recursion - Function calling itself with a base case
11. Scope - Local vs global variables
12. Nested functions - Functions defined inside other functions
"""
