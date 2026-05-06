"""Practical 10: File Handling - Write, Read, and Append Operations"""

# 1. Writing to a file
with open("example.txt", "w") as output_file:
    output_file.write("Hello, this is a sample text file.\n")
    output_file.write("My name is Meeran.\n")

print("File created and data written successfully.")

# 2. Reading from a file
with open("example.txt", "r") as input_file:
    print("Reading from file:")
    print(input_file.read())

# 3. Appending to a file
with open("example.txt", "a") as append_file:
    append_file.write("This line is appended to the file.\n")

print("Data appended successfully.")

# 4. Reading updated file
with open("example.txt", "r") as input_file:
    print("Reading from file after appending:")
    print(input_file.read())