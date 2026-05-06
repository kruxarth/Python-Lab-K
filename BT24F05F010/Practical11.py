"""Practical 11: Exception Handling - try, except, finally Blocks"""

try:
    # Get user input and perform division
    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the second number: "))
    division_result = first_num / second_num
    print(f"The result of {first_num} divided by {second_num} is: {division_result}")

except ZeroDivisionError:
    # Handle division by zero error
    print("Error: You cannot divide by zero. Please provide a non-zero divisor.")

except ValueError:
    # Handle invalid input error
    print("Error: Please enter valid integers.")

except Exception as error:
    # Handle any other unexpected exceptions
    print(f"An unexpected error occurred: {error}")

finally:
    # This block always executes
    print("End of Program") 