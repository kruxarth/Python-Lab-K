# File Handling

# 1. Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a sample text file.\n")
    file.write("My name is Rohit.\n")

print("File created and data written successfully.")

# 2. Reading a file
with open("example.txt", "r") as file:
    print("Reading from file:")
    print(file.read())

# 3. Appending to a file
with open("example.txt", "a") as file:
    file.write("This line is appended to the file.\n")

print("Data appended successfully.")

# 4. Reading updated file
with open("example.txt", "r") as file:
    print("Reading from file after appending:")
    print(file.read())