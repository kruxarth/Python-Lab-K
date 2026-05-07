# File Handling using 'with'

# 1. Writing to a file
with open("student.txt", "w") as file:
    file.write("Name: Kapil Tekam\n")
    file.write("Course: Computer Engineering\n")
    file.write("Year: 2nd Year\n")

print("Data written successfully!\n")

# 2. Reading file
with open("student.txt", "r") as file:
    print("Reading File Content:\n")
    print(file.read())

# 3. Appending data
with open("student.txt", "a") as file:
    file.write("College: GECA\n")

print("\nData appended successfully!\n")

# 4. Reading updated file
with open("student.txt", "r") as file:
    print("Updated File Content:\n")
    print(file.read())