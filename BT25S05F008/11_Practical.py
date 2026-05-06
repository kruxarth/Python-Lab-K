# Basic try-except
try:
    x = int(input("Enter number: "))
    print(10 / x)
except ValueError:
    print("Invalid input – not a number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print("No exceptions occurred!")
finally:
    print("This always runs.")

# Custom exception
class AgeError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise AgeError("Age cannot be negative!")
    print(f"Age: {age}")

try:
    check_age(-5)
except AgeError as e:
    print(e)