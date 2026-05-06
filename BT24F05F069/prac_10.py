# File Handling

# 1. Writing to a file
with open("lab_notes.txt", "w") as file:
    file.write("Python laboratory work in progress.\n")
    file.write("Project: File operations implementation.\n")

print("File created and data written successfully.")

# 2. Reading a file
with open("lab_notes.txt", "r") as file:
    print("Reading from file:")
    print(file.read())

# 3. Appending to a file
with open("lab_notes.txt", "a") as file:
    file.write("Submission date: April 10, 2026.\n")

print("Data appended successfully.")

# 4. Reading updated file
with open("lab_notes.txt", "r") as file:
    print("Reading from file after appending:")
    print(file.read())