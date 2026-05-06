#Practical 11 : Exception handling

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("Division:",num1,"/",num2,"=",result)

except ZeroDivisionError:
    print("Can't divide by zero")

except ValueError:
    print("Enter a valid number")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

else:
    print("Division done without error.")

finally:
    print("End of Program.")