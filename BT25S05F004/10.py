# Writing into a file
file = open("student.txt", "w")
file.write("Hello, I am sayli machave.\n")
file.write("Welcome to learning files in Python with me.\n")
file.close()

# Reading the file
file = open("student.txt", "r")
data = file.read()
print("File Content:")
print(data)
file.close()

# Appending new data
file = open("student.txt", "a")
file.write("This line is added later.\n")
file.close()

# Reading line by line
file = open("student.txt", "r")
print("Reading line by line:")
for line in file:
    print(line.strip())
file.close()