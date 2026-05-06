num = int(input("Enter a number: "))
print("\n1. Simple if")
if num > 0:
    print("Number is positive")

print("\n2. if-else")
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

print("\n3. Nested if")
if num >= 0:
    if num == 0:
        print("Number is zero")
    else:
        print("Number is positive")
else:
    print("Number is negative")
    
print("\n4. if-elif-else ladder")
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")