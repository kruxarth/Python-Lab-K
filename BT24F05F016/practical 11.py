try:
    num = int(input("Enter a number: ") or "10")
    result = 100 / num
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input!")

try:
    x = [1, 2, 3]
    print(f"Element: {x[5]}")
except Exception as e:
    print(f"Error: {e}")

def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except ValueError:
        print("Invalid data type!")

print(divide(10, 2))
print(divide(10, 0))

try:
    data = {"name": "Alice", "age": 25}
    print(data['name'])
    print(data['gpa'])
except KeyError as e:
    print(f"Key not found: {e}")

try:
    num = int("abc")
except ValueError as e:
    print(f"ValueError: {e}")
except Exception as e:
    print(f"Error: {e}")

try:
    file = open("test.txt", 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
finally:
    try:
        file.close()
    except:
        pass

try:
    with open("data.txt", 'r') as f:
        lines = f.readlines()
except FileNotFoundError:
    print("File does not exist")

class CustomError(Exception):
    def __init__(self, message):
        self.message = message

try:
    raise CustomError("This is a custom error")
except CustomError as e:
    print(f"Custom Error: {e.message}")

try:
    num = 5
    if num < 10:
        raise ValueError("Number is too small")
except ValueError as e:
    print(f"ValueError: {e}")

try:
    x = 10
    y = 0
    result = x / y
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Error: {type(e).__name__}")

def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 120:
        raise ValueError("Age is unrealistic")
    return age

try:
    validate_age(150)
except ValueError as e:
    print(f"Validation error: {e}")

try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError:
    print("Index out of range")

try:
    result = eval("5 + 3")
    print(result)
except SyntaxError:
    print("Syntax error")
except Exception as e:
    print(f"Error: {e}")



# ==============================================================================
# PART 3: TRY-EXCEPT-FINALLY BLOCK
# ==============================================================================

print("\n" + "=" * 70)
print("PART 3: TRY-EXCEPT-FINALLY BLOCK")
print("-" * 70)

# 3.1 Finally Block Execution
print("\n3.1 Finally Block Always Executes")

def process_file():
    """Example showing finally block with file handling."""
    try:
        print("  Step 1: Opening file")
        # Simulate file operations
        result = 10 / 2  # This succeeds
        print(f"  Step 2: Processing completed (result = {result})")
    except ZeroDivisionError:
        print("  ✗ Error during processing")
    finally:
        print("  Step 3: Finally block - Cleanup operations")
        print("  (Always executed, with or without exception)")

print("Scenario 1 - No Exception:")
process_file()

print("\nScenario 2 - With Exception:")
def process_file_error():
    """Example with error."""
    try:
        print("  Step 1: Opening file")
        result = 10 / 0  # This causes error
        print(f"  Step 2: Processing completed")
    except ZeroDivisionError:
        print("  ✗ Error: Division by zero!")
    finally:
        print("  Step 3: Finally block - Cleanup operations")

process_file_error()


# 3.2 Finally with Return Statement
print("\n3.2 Finally Block with Return Statement")

def test_finally_with_return():
    """Finally executes even with return statement."""
    try:
        print("  In try block")
        return "Returning from try"
    finally:
        print("  Finally block still executes!")

result = test_finally_with_return()
print(f"Result: {result}")


# ==============================================================================
# PART 4: ELSE BLOCK WITH EXCEPTIONS
# ==============================================================================

print("\n" + "=" * 70)
print("PART 4: ELSE BLOCK WITH EXCEPTIONS")
print("-" * 70)

print("\n4.1 Try-Except-Else Block")
print("""
The else block executes ONLY if no exception occurred in the try block.
Syntax: try... except... else... finally...
""")

# Example 1: No exception
print("\nExample 1 - No Exception:")
try:
    num = 10 / 2
    print(f"  Division successful: {num}")
except ZeroDivisionError:
    print("  ✗ Error: Cannot divide by zero!")
else:
    print(f"  ✓ Else block: Division result is {num}")
finally:
    print("  Finally block executed")


# Example 2: With exception
print("\nExample 2 - With Exception:")
try:
    num = 10 / 0
    print(f"  Division successful: {num}")
except ZeroDivisionError:
    print("  ✗ Error: Cannot divide by zero!")
else:
    print(f"  ✓ Else block: This won't print (exception occurred)")
finally:
    print("  Finally block executed")


# ==============================================================================
# PART 5: RAISING EXCEPTIONS
# ==============================================================================

print("\n" + "=" * 70)
print("PART 5: RAISING EXCEPTIONS")
print("-" * 70)

# 5.1 Raising Exceptions
print("\n5.1 Raising Exceptions")

def validate_age(age):
    """Validate age and raise exception if invalid."""
    if age < 0:
        raise ValueError("Age cannot be negative!")
    elif age < 18:
        raise ValueError("Age must be 18 or older!")
    else:
        print(f"✓ Age {age} is valid")

# Valid age
try:
    validate_age(25)
except ValueError as e:
    print(f"✗ Error: {e}")

# Invalid age
try:
    validate_age(10)
except ValueError as e:
    print(f"✗ Error: {e}")

# Negative age
try:
    validate_age(-5)
except ValueError as e:
    print(f"✗ Error: {e}")


# 5.2 Re-raising Exceptions
print("\n5.2 Re-raising Exceptions")

def process_data(data):
    """Process data and re-raise caught exceptions."""
    try:
        if not isinstance(data, list):
            raise TypeError("Data must be a list!")
        return sum(data)
    except TypeError as e:
        print(f"✗ Error in validation: {e}")
        raise  # Re-raise the same exception

try:
    result = process_data([1, 2, 3])
    print(f"✓ Result: {result}")
except TypeError:
    print("✗ Caught re-raised exception!")


# ==============================================================================
# PART 6: CUSTOM EXCEPTIONS
# ==============================================================================

print("\n" + "=" * 70)
print("PART 6: CUSTOM EXCEPTIONS")
print("-" * 70)

# 6.1 Defining Custom exceptions
print("\n6.1 Defining Custom Exceptions")

class InsufficientBalanceError(Exception):
    """Raised when account balance is insufficient."""
    pass

class InvalidAccountError(Exception):
    """Raised when account number is invalid."""
    pass

class BankAccount:
    """Simple bank account class."""
    
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def withdraw(self, amount):
        """Withdraw amount from account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive!")
        if amount > self.balance:
            raise InsufficientBalanceError(
                f"Insufficient balance! Available: ${self.balance}, Requested: ${amount}"
            )
        self.balance -= amount
        print(f"✓ Withdrawn ${amount}. New balance: ${self.balance}")
    
    def deposit(self, amount):
        """Deposit amount to account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive!")
        self.balance += amount
        print(f"✓ Deposited ${amount}. New balance: ${self.balance}")

# Using custom exceptions
account = BankAccount("ACC123", 1000)

# Successful transaction
try:
    account.withdraw(200)
except Exception as e:
    print(f"✗ Error: {e}")

# Insufficient balance
try:
    account.withdraw(5000)
except InsufficientBalanceError as e:
    print(f"✗ Error: {e}")

# Invalid amount
try:
    account.withdraw(-100)
except ValueError as e:
    print(f"✗ Error: {e}")


# 6.2 Custom Exception with Additional Methods
print("\n6.2 Custom Exception with Additional Information")

class ValidationError(Exception):
    """Custom validation error with field information."""
    
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"Validation failed for {field}: {message}")

try:
    raise ValidationError("email", "Invalid email format")
except ValidationError as e:
    print(f"✗ Error in field '{e.field}': {e.message}")


# ==============================================================================
# PART 7: EXCEPTION HIERARCHY
# ==============================================================================

print("\n" + "=" * 70)
print("PART 7: EXCEPTION HIERARCHY")
print("-" * 70)

print("""
Python Exception Hierarchy:
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── StopIteration
    ├── ArithmeticError
    │   ├── FloatingPointError
    │   ├── OverflowError
    │   └── ZeroDivisionError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── AssertionError
    ├── AttributeError
    ├── NameError
    ├── TypeError
    ├── ValueError
    ├── IOError
    ├── OSError
    └── ... (many more)
""")

# 7.1 Catching Parent Exception
print("\n7.1 Catching Parent Exception")

try:
    x = [1, 2, 3]
    print(x[10])  # IndexError
except LookupError as e:  # Parent of IndexError
    print(f"✗ Lookup Error caught: {type(e).__name__}: {e}")

try:
    d = {"name": "Alice"}
    print(d["age"])  # KeyError
except LookupError as e:  # Parent of KeyError
    print(f"✗ Lookup Error caught: {type(e).__name__}: {e}")


# ==============================================================================
# PART 8: GETTING EXCEPTION INFORMATION
# ==============================================================================

print("\n" + "=" * 70)
print("PART 8: GETTING EXCEPTION INFORMATION")
print("-" * 70)

# 8.1 Exception Information
print("\n8.1 Accessing Exception Information")

try:
    x = 10 / 0
except ZeroDivisionError as e:
    print(f"Exception type: {type(e)}")
    print(f"Exception name: {type(e).__name__}")
    print(f"Exception message: {str(e)}")
    print(f"Exception args: {e.args}")


# 8.2 Using Traceback
print("\n8.2 Exception Traceback Information")

try:
    def function_a():
        return function_b()
    
    def function_b():
        return 10 / 0
    
    result = function_a()
except ZeroDivisionError:
    print("✗ Error occurred. Traceback:")
    traceback.print_exc()


# 8.3 Formatted Exception Information
print("\n8.3 Getting Formatted Traceback")

try:
    num = int("invalid")
except ValueError:
    exc_info = sys.exc_info()
    print(f"Exception type: {exc_info[0]}")
    print(f"Exception value: {exc_info[1]}")
    print(f"Traceback object: {exc_info[2]}")
    print(f"\nFormatted traceback:")
    traceback.print_tb(exc_info[2])


# ==============================================================================
# PART 9: CONTEXT MANAGERS (WITH STATEMENT)
# ==============================================================================

print("\n" + "=" * 70)
print("PART 9: CONTEXT MANAGERS")
print("-" * 70)

# 9.1 Context Manager with File
print("\n9.1 Context Manager Handles Exceptions")

try:
    try:
        with open("nonexistent.txt", 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print("✗ File not found! (But resource was cleaned up properly)")
except Exception as e:
    print(f"✗ Unexpected error: {e}")


# 9.2 Custom Context Manager
print("\n9.2 Custom Context Manager")

class DatabaseConnection:
    """Custom context manager for database connection."""
    
    def __init__(self, name):
        self.name = name
        self.connected = False
    
    def __enter__(self):
        """Called when entering with block."""
        print(f"  Connecting to {self.name}...")
        self.connected = True
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting with block."""
        print(f"  Disconnecting from {self.name}...")
        self.connected = False
        
        # Return True to suppress exceptions, False to propagate
        if exc_type is not None:
            print(f"  ✗ Exception occurred: {exc_type.__name__}")
        return False
    
    def query(self, sql):
        """Execute a query."""
        if not self.connected:
            raise RuntimeError("Not connected to database!")
        print(f"  Executing: {sql}")
        return "Query result"

# Using custom context manager
print("\nUsing custom context manager:")
try:
    with DatabaseConnection("MySQL") as db:
        result = db.query("SELECT * FROM users")
        print(f"  Result: {result}")
except Exception as e:
    print(f"✗ Error: {e}")


# ==============================================================================
# PART 10: BEST PRACTICES
# ==============================================================================

print("\n" + "=" * 70)
print("PART 10: BEST PRACTICES")
print("-" * 70)

print("""
BEST PRACTICES FOR EXCEPTION HANDLING:

1. ✓ Be Specific with Exceptions
   - Catch specific exceptions, not generic Exception
   - Avoid bare except: clauses

2. ✓ Use Finally for Cleanup
   - Always release resources in finally block
   - Use context managers (with statement)

3. ✓ Don't Ignore Exceptions
   - Always log or handle exceptions appropriately
   - Inform user about the error

4. ✓ Order Matters
   - Catch specific exceptions before general ones
   - Parent exception should come after child

5. ✓ Raise Meaningful Exceptions
   - Provide clear error messages
   - Include relevant context in exception

6. ✓ Use Custom Exceptions
   - Create custom exceptions for application-specific errors
   - Inherit from appropriate base exception class

7. ✓ Document Exception Behavior
   - Document which exceptions a function can raise
   - Explain error conditions in docstrings

8. ✓ Don't Use Exceptions for Flow Control
   - Use if-statements for predictable conditions
   - Use exceptions for exceptional situations only
""")


# 10.1 Good Exception Handling Example
print("\n10.1 Example: Good Exception Handling")

def process_user_data(user_data):
    """
    Process user data with proper exception handling.
    
    Args:
        user_data (dict): User information dictionary
    
    Raises:
        ValueError: If required fields are missing
        TypeError: If data is not a dictionary
    
    Returns:
        dict: Processed user data
    """
    try:
        if not isinstance(user_data, dict):
            raise TypeError("user_data must be a dictionary")
        
        required_fields = ['name', 'email', 'age']
        for field in required_fields:
            if field not in user_data:
                raise ValueError(f"Missing required field: {field}")
        
        # Validate age
        age = user_data['age']
        if not isinstance(age, int) or age < 0:
            raise ValueError("Age must be a non-negative integer")
        
        print(f"✓ User {user_data['name']} processed successfully")
        return user_data
        
    except ValueError as e:
        print(f"✗ Validation error: {e}")
        return None
    except TypeError as e:
        print(f"✗ Type error: {e}")
        return None
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return None

# Test the function
print("\nTest 1 - Valid data:")
valid_user = {"name": "Alice", "email": "alice@example.com", "age": 25}
process_user_data(valid_user)

print("\nTest 2 - Missing field:")
invalid_user = {"name": "Bob", "age": 30}
process_user_data(invalid_user)

print("\nTest 3 - Wrong type:")
process_user_data("not a dictionary")


# 10.2 Bad Exception Handling (What NOT to do)
print("\n10.2 Example: Bad Exception Handling (What NOT to do)")

print("""
# BAD - Catching everything
try:
    data = process_data()
except:  # Bare except - BAD!
    pass  # Silently ignoring error - BAD!

# BAD - Generic exception handling
try:
    result = risky_operation()
except Exception:  # Too generic - BAD!
    print("Error")  # No information provided

# GOOD - Specific exception handling
try:
    data = process_data()
except ValueError as e:
    print(f"Invalid data: {e}")
except IOError as e:
    print(f"File error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
    raise
""")


# ==============================================================================
# PART 11: PRACTICAL EXAMPLES
# ==============================================================================

print("\n" + "=" * 70)
print("PART 11: PRACTICAL EXAMPLES")
print("-" * 70)

# Example 1: Safe Calculator
print("\n Example 1: Safe Calculator with Exception Handling")

def safe_calculator(a, b, operation):
    """
    Perform calculation with full exception handling.
    
    Args:
        a, b: Operands (should be numbers)
        operation: '+', '-', '*', '/', '%', '**'
    
    Returns:
        Result or None if error occurred
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        print("✗ Error: Both operands must be numbers!")
        return None
    
    try:
        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '*':
            return a * b
        elif operation == '/':
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            return a / b
        elif operation == '%':
            if b == 0:
                raise ZeroDivisionError("Cannot use modulo with zero!")
            return a % b
        elif operation == '**':
            return a ** b
        else:
            raise ValueError(f"Invalid operation: {operation}")
    except ZeroDivisionError as e:
        print(f"✗ Math Error: {e}")
        return None
    except ValueError as e:
        print(f"✗ Error: {e}")
        return None

print("Calculator Tests:")
print(f"10 + 5 = {safe_calculator(10, 5, '+')}")
print(f"10 / 0 = {safe_calculator(10, 0, '/')}")
print(f"'a' + 5 = {safe_calculator('a', 5, '+')}")


# Example 2: List Operations with Error Handling
print("\n Example 2: Safe List Operations")

def get_element(lst, index):
    """Safely get element from list."""
    try:
        return lst[index]
    except (IndexError, TypeError) as e:
        print(f"✗ Error: {type(e).__name__}: {e}")
        return None

numbers = [10, 20, 30, 40, 50]
print(f"Element at index 2: {get_element(numbers, 2)}")
print(f"Element at index 10: {get_element(numbers, 10)}")


print("\n" + "=" * 70)
print("END OF PRACTICAL 11: EXCEPTION HANDLING")
print("=" * 70)
