try:
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    print(a / b)
except ZeroDivisionError:
    print("Divide by zero error")
except ValueError:
    print("Invalid input")
