x = 10

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")

score = 78

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade F")

marks = 55

if marks >= 50:
    print("Pass")
else:
    print("Fail")

temp = 35

if temp > 40:
    print("Hot")
elif temp > 20:
    print("Warm")
elif temp > 0:
    print("Cold")
else:
    print("Freezing")

a = 10
b = 20

if a > b:
    print("a is greater")
elif a < b:
    print("b is greater")
else:
    print("Equal")

print("=" * 60)
print("IF-ELIF-ELSE LADDER IN PYTHON")
print("=" * 60)

# 1. SIMPLE IF STATEMENT
print("\n1. SIMPLE IF STATEMENT:")
print("-" * 60)
age = 20

if age >= 18:
    print(f"Age is {age}: You are an adult!")

# 2. IF-ELSE STATEMENT
print("\n2. IF-ELSE STATEMENT:")
print("-" * 60)
marks = 45

if marks >= 50:
    print(f"Marks: {marks} - PASSED")
else:
    print(f"Marks: {marks} - FAILED")

# 3. IF-ELIF-ELSE LADDER (Simple)
print("\n3. IF-ELIF-ELSE LADDER (Simple):")
print("-" * 60)
score = 75

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score} - Grade: {grade}")

# 4. IF-ELIF-ELSE LADDER (Multiple conditions)
print("\n4. IF-ELIF-ELSE LADDER (Grading System):")
print("-" * 60)

students = [88, 92, 45, 67, 78, 95, 34, 88]

for student_score in students:
    if student_score >= 90:
        print(f"Score {student_score}: Grade A (Excellent)")
    elif student_score >= 80:
        print(f"Score {student_score}: Grade B (Very Good)")
    elif student_score >= 70:
        print(f"Score {student_score}: Grade C (Good)")
    elif student_score >= 60:
        print(f"Score {student_score}: Grade D (Pass)")
    else:
        print(f"Score {student_score}: Grade F (Fail)")

# 5. IF-ELIF-ELSE LADDER (Category classification)
print("\n5. IF-ELIF-ELSE LADDER (Age Classification):")
print("-" * 60)

ages = [5, 15, 25, 60, 80]

for person_age in ages:
    if person_age < 13:
        category = "Child"
    elif person_age < 18:
        category = "Teenager"
    elif person_age < 65:
        category = "Adult"
    else:
        category = "Senior Citizen"
    
    print(f"Age {person_age}: {category}")

# 6. NESTED IF-ELIF-ELSE
print("\n6. NESTED IF-ELIF-ELSE:")
print("-" * 60)

user_age = 25
has_license = True

if user_age >= 18:
    if has_license:
        print(f"Age: {user_age}, License: Yes")
        print("You can drive a car!")
    else:
        print(f"Age: {user_age}, License: No")
        print("You are old enough but need a license!")
else:
    print("You are not old enough to drive!")

# 7. PRACTICAL EXAMPLE: ATM System
print("\n7. PRACTICAL EXAMPLE: ATM System")
print("-" * 60)

balance = 5000
withdrawal = 2000

print(f"Current Balance: Rs. {balance}")
print(f"Withdrawal Amount: Rs. {withdrawal}")

if withdrawal > balance:
    print("Error: Insufficient balance!")
elif withdrawal % 100 != 0:
    print("Error: Amount must be a multiple of 100!")
elif withdrawal <= 0:
    print("Error: Invalid amount!")
else:
    balance -= withdrawal
    print(f"Withdrawal successful! New balance: Rs. {balance}")

# 8. PRACTICAL EXAMPLE: Traffic Light
print("\n8. PRACTICAL EXAMPLE: Traffic Light")
print("-" * 60)

colors = ["red", "yellow", "green", "blue"]

for color in colors:
    if color == "red":
        action = "STOP"
    elif color == "yellow":
        action = "READY"
    elif color == "green":
        action = "GO"
    else:
        action = "INVALID COLOR"
    
    print(f"Traffic Light: {color} - {action}")

# 9. PRACTICAL EXAMPLE: Temperature Advisory
print("\n9. PRACTICAL EXAMPLE: Temperature Advisory")
print("-" * 60)

temperatures = [5, 15, 25, 30, 35, 40, 42, 45]

for temp in temperatures:
    if temp < 0:
        advice = "Extreme Cold - Stay Indoors"
    elif temp < 10:
        advice = "Cold - Wear Warm Clothes"
    elif temp < 20:
        advice = "Cool - Light Jacket Recommended"
    elif temp < 30:
        advice = "Pleasant - Comfortable Weather"
    elif temp < 35:
        advice = "Hot - Drink Water Frequently"
    elif temp < 40:
        advice = "Very Hot - Avoid Going Out"
    else:
        advice = "Extreme Heat - ALERT!"
    
    print(f"Temperature: {temp}°C - {advice}")

# 10. PRACTICAL EXAMPLE: Student Grade and Feedback
print("\n10. PRACTICAL EXAMPLE: Student Feedback System")
print("-" * 60)

student_marks = {"Alice": 95, "Bob": 78, "Charlie": 45, "Diana": 88}

for name, marks in student_marks.items():
    if marks >= 90:
        feedback = "Outstanding performance!"
    elif marks >= 80:
        feedback = "Good work, keep it up!"
    elif marks >= 70:
        feedback = "Average performance, needs improvement"
    elif marks >= 60:
        feedback = "Below average, study harder"
    else:
        feedback = "Poor performance, needs serious attention"
    
    print(f"{name}: {marks}/100 - {feedback}")

# 11. MULTIPLE CONDITIONS WITH AND/OR
print("\n11. MULTIPLE CONDITIONS:")
print("-" * 60)

age = 25
income = 50000
credit_score = 750

if age >= 21 and income >= 30000 and credit_score >= 700:
    print("Loan Approved!")
    print(f"Age: {age} ✓, Income: {income} ✓, Credit Score: {credit_score} ✓")
elif age >= 21 or income >= 30000:
    print("Partially eligible - Missing some criteria")
else:
    print("Loan Rejected!")

# 12. PRACTICAL EXAMPLE: Number Classification
print("\n12. PRACTICAL EXAMPLE: Number Classification")
print("-" * 60)

numbers = [-5, 0, 3, 10, 15, 20]

for num in numbers:
    if num < 0:
        print(f"{num}: Negative number")
    elif num == 0:
        print(f"{num}: Zero")
    elif num > 0 and num <= 10:
        print(f"{num}: Single digit positive")
    elif num > 10 and num <= 20:
        print(f"{num}: Double digit positive (10-20)")
    else:
        print(f"{num}: Large positive number")

# 13. PRACTICAL EXAMPLE: Eligibility Check
print("\n13. PRACTICAL EXAMPLE: Voter Eligibility")
print("-" * 60)

voter_age = 20
citizenship = True
criminal_record = False

if age >= 18:
    if citizenship:
        if not criminal_record:
            print(f"Age: {voter_age} ✓")
            print("Eligibility: ELIGIBLE TO VOTE ✓")
        else:
            print("Eligibility: NOT ELIGIBLE (Criminal Record)")
    else:
        print("Eligibility: NOT ELIGIBLE (Not a Citizen)")
else:
    print("Eligibility: NOT ELIGIBLE (Below 18)")

print("\n" + "=" * 60)
print("END OF PROGRAM")
print("=" * 60)
