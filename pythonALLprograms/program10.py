# File Handling Program

# Writing
with open("student.txt", "w") as file:
    name = input("Enter name: ")
    age = input("Enter age: ")
    file.write("Name: " + name + "\n")
    file.write("Age: " + age)

# Appending
with open("student.txt", "a") as file:
    file.write("\nCourse: BCA")

# Reading
with open("student.txt", "r") as file:
    print("\nFile Content:")
    print(file.read())