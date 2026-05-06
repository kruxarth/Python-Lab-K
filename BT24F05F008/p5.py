# Practical 5 Conditional Statements

# --- if-elif-else ladder: Grade Calculator
score = int(input("Enter marks (0-100): "))

if score >= 90:
    rating = 'O (Outstanding)'
elif score >= 75:
    rating = 'A+ (Excellent)'
elif score >= 60:
    rating = 'A (Very Good)'
elif score >= 50:
    rating = 'B (Good)'
elif score >= 40:
    rating = 'C (Pass)'
else:
    rating = 'F (Fail)'

print(f"Marks: {score} Grade: {rating}")

# --- Nested if: Age Category
years = int(input("\nEnter age: "))

if years >= 0:
    if years < 13:
        print("Category: Child")
    elif years < 18:
        print("Category: Teenager")
    elif years < 60:
        print("Category: Adult")
    else:
        print("Category: Senior Citizen")
else:
    print("Invalid age entered!")



