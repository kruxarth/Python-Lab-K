num = int(input("Enter a number: "))

# Simple if
if num > 0:
    print("Positive")

# if-else
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# nested if
if num > 0:
    if num > 100:
        print("Large positive")
    else:
        print("Small positive")

# if-elif-else
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")