# --- if-elif-else ladder: Grade Calculator
marks = int(input("Enter marks (0-100): "))

if marks >= 90:
    grade = 'O (Outstanding)'
elif marks >= 75:
    grade = 'A+ (Excellent)'
elif marks >= 60:
    grade = 'A (Very Good)'
elif marks >= 50:
    grade = 'B (Good)'
elif marks >= 40:
    grade = 'C (Pass)'
else:
    grade = 'F (Fail)'

print(f"Marks: {marks} Grade: {grade}")

# --- Nested if: Age Category
age = int(input("\nEnter age: "))

if age >= 0:
    if age < 13:
        print("Category: Child")
    elif age < 18:
        print("Category: Teenager")
    elif age < 60:
        print("Category: Adult")
    else:
        print("Category: Senior Citizen")
else:
    print("Invalid age entered!")