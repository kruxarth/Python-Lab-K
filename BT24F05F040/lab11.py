try:
    # Risky code
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    # Specific error handling
    print("Error: You cannot divide by zero.")
except ValueError:
    # Handling another specific error
    print("Error: Please enter a valid integer.")
except Exception as e:
    # Generic catch-all for other errors
    print(f"An unexpected error occurred: {e}")
else:
    # Executes if no error occurs
    print(f"Success! The result is {result}")
finally:
    # Always executes
    print("Cleaning up and exiting.")
