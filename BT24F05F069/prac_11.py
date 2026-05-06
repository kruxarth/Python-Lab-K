# Exception Handling

try:
    # Code that may raise an exception
    val1 = int(input("Enter the numerator: "))
    val2 = int(input("Enter the denominator: "))
    output = val1 / val2
    print(f"Result: {output}")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Invalid input! Please enter numeric digits only.")

except Exception as e:
    print(f"General Error: {e}")

finally:
    print("Execution complete.")