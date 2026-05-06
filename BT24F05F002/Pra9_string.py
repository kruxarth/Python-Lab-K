# It combines these concepts to provide a summary of a student's information and marks.
# practical 9: Data Types in Python

# STRING
name = input("Enter your name: ")
print("Uppercase Name:", name.upper())

# LIST (mutable)
marks = [80, 75, 90, 85]
marks.append(95)
print("\nMarks List:", marks)

# TUPLE (immutable)
subjects = ("Math", "Science", "English", "Computer")
print("Subjects Tuple:", subjects)

# SET (unique values)
unique_marks = set(marks)
print("Unique Marks Set:", unique_marks)

# Combining concepts
print("\n--- Summary ---")
print(f"Student: {name}")
print(f"Total Marks: {sum(marks)}")
print(f"Number of Subjects: {len(subjects)}")
print(f"Unique Marks Count: {len(unique_marks)}")

