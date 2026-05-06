"""Practical 5: Conditional Statements (if, if-else, nested if, if-elif-else)"""

value = 10

# Simple if condition
if value > 5:
    print("value is greater than 5")

# if-else for even/odd check
if value % 2 == 0:
    print("Even")
else:
    print("Odd")

# Nested if statements
if value > 0:
    if value < 20:
        print("value is between 0 and 20")

# if-elif-else ladder for grade calculation
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")