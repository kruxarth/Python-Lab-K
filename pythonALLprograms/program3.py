# Variables and Data Types Program

print("----- USER DATA PROGRAM -----")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))
is_student = True

print("\n----- STORED VALUES -----")
print("Name:", name)
print("Age:", age)
print("Marks:", marks)
print("Student Status:", is_student)

print("\n----- DATA TYPES -----")
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of marks:", type(marks))
print("Type of is_student:", type(is_student))

# Type casting
age_str = str(age)
print("\nConverted age to string:", age_str)
print("New type:", type(age_str))