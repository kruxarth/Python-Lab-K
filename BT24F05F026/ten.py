file = open("example.txt", "w")
file.write("This is the first line.\n")
file.write("File handling in Python.\n")
file.close()

file = open("example.txt", "a")
file.write("This line is added later.\n")
file.close()

file = open("example.txt", "r")
data = file.read()
file.close()

print(data)
