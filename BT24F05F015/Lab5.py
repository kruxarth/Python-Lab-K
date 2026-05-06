x = 10

# Simple if
if x > 5:
    print("x is greater than 5")

# if-else
if x % 2 == 0:
    print("Even")
else:
    print("Odd")

# Nested if
if x > 0:
    if x < 20:
        print("x is between 0 and 20")

# if-elif ladder
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")