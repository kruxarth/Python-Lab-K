print("Student: Ritu")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
print("Student: Kiran")
try:
    num = int("hello")
except ValueError:
    print("Error: Invalid conversion to integer.")
print("Student: Naina")
try:
    marks = [90, 85, 78]
    print(marks[5])
except IndexError:
    print("Error: Index out of range.")
print("Student: Gaurav")
try:
    x = int(input("Enter a number: ") if False else "0")
    result = 100 / x
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero.")
except ValueError:
    print("Error: Please enter a valid number.")
finally:
    print("Execution complete.")
print("Student: Mohit")
try:
    file = open("notfound.txt", "r")
except FileNotFoundError:
    print("Error: File not found.")
print("Student: Pallavi")
try:
    age = -5
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print("Age:", age)
except ValueError as e:
    print("Custom Error:", e)
