# 1) Simple if-else
num = int(input("Enter a number: "))
if num % 2 == 0:
	print("if-else: Even number")
else:
	print("if-else: Odd number")

# 2) Nested if-else
age = int(input("Enter age: "))
has_id = input("Do you have ID? (yes/no): ").strip().lower()

if age >= 18:
	if has_id == "yes":
		print("nested if-else: Entry allowed")
	else:
		print("nested if-else: ID required")
else:
	print("nested if-else: Underage")

# 3) if-elif-else ladder
marks = int(input("Enter marks (0-100): "))

if marks >= 90:
	print("if-elif-else: Grade A")
elif marks >= 75:
	print("if-elif-else: Grade B")
elif marks >= 50:
	print("if-elif-else: Grade C")
else:
	print("if-elif-else: Grade D")
