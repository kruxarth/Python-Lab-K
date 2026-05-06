
marks = int(input("Enter your marks (0-100): "))

if marks >= 40:
    print("Result: Passed")
else:
    print("Result: Failed")

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
else:
    grade = "C"

print(f"Grade assigned: {grade}")

if marks >= 40:
    if marks >= 75:
        print("Congratulations! You passed with Distinction.")
    else:
        print("You passed, but keep working hard for a distinction.")
