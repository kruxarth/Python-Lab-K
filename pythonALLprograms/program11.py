# Exception Handling Program

try:
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))

    print("Division:", a / b)

    list1 = [1, 2, 3]
    print(list1[5])  # will cause error

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")

except IndexError:
    print("Index out of range")

finally:
    print("Program ended")