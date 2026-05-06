# 1. BASIC FUNCTION
def greet():
    print("Welcome to Python Lab!")

greet()

# 2. FUNCTION WITH PARAMETERS
def multiply(a, b):
    return a * b

print("Product:", multiply(6, 4))

# 3. DEFAULT ARGUMENT FUNCTION
def calculate_tax(amount, tax_rate=0.05):
    return amount * tax_rate

print("Default Tax:", calculate_tax(1000))        # uses default tax_rate=0.05
print("Higher Tax:", calculate_tax(1000, 0.18))    # overrides default

# 4. *args (VARIABLE LENGTH ARGUMENTS)
def concatenate_strings(*args):
    result = ""
    for word in args:
        result += word + " "
    return result.strip()

print("Joined string:", concatenate_strings("Coding", "is", "very", "fun"))

# 5. **kwargs (KEYWORD ARGUMENTS)
def show_student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

show_student_details(roll_no="BT24F05F999", subject="Python", status="Completed")

# 6. LAMBDA FUNCTION (ANONYMOUS FUNCTION)
double = lambda x: x * 2
print("Double using lambda:", double(12))

# Lambda with multiple arguments
power_lambda = lambda base, exp: base ** exp
print("Power using lambda:", power_lambda(2, 5))