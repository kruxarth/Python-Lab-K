# Conditional Statements Program

print("----- NUMBER ANALYSIS -----")

num = int(input("Enter a number: "))

# Positive/Negative
if num > 0:
    print("Number is Positive")
elif num < 0:
    print("Number is Negative")
else:
    print("Number is Zero")

# Even/Odd
if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

# Nested Condition
if num > 0:
    if num < 100:
        print("Number is between 1 and 100")

# Grade Example
marks = int(input("\nEnter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")