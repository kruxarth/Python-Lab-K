a = 10
b = 20
num = 5
# if statement
print("If Statement:")
if a < b:
    print("a is less than b")
# if-else statement
print("\nIf-Else Statement:")
if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")
# nested if statement
print("\nNested If Statement:")
if a < b:
    if num > 0:
        print("a is less than b and number is positive")
# if-elif-else ladder
print("\nIf-Elif-Else Ladder:")
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")