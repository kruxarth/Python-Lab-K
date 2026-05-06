practical 5 : Conditional statements 
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
elif num == 0:
    print("Number is zero")
else:
    print("Invalid input")

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number inside nested if")

if num > 0 and num % 2 == 0:
    print("Positive and Even number")
