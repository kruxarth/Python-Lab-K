# Exception Handling

try:
    # Code that may raise an exception
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is: {result}")

except ZeroDivisionError:
    print("Error: You cannot divide by zero. Please provide a non-zero divisor.")

except ValueError:
    print("Error: Please enter valid integers.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    print("End of Program")