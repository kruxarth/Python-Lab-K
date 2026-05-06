try:
    first = int(input("Enter the first number: "))
    second = int(input("Enter the second number: "))
    ans = first / second
    print("The result of", first, "divided by", second, "is:", ans)

except ZeroDivisionError:
    print("Error: You cannot divide by zero. Please provide a non-zero divisor.")

except ValueError:
    print("Error: Please enter valid integers.")

except Exception as err:
    print("An unexpected error occurred:", err)

finally:
    print("End of Program")