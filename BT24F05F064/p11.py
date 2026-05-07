Practical 11 : Exception handling in python
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Division Result:", result)

    lst = [10, 20, 30]
    index = int(input("Enter index (0-2): "))
    print("List value:", lst[index])

    d = {"name": "Python"}
    key = input("Enter dictionary key: ")
    print("Dictionary value:", d[key])

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid input, please enter numeric values only")

except IndexError:
    print("Error: List index out of range")

except KeyError:
    print("Error: Key not found in dictionary")

except Exception as e:
    print("Unexpected error:", e)

else:
    print("All operations completed successfully")

finally:
    print("Program execution finished")
