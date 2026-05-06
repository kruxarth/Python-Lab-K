# writing to a file
file = open("sample.txt", "w")
file.write("Hello, this is my first file handling program.\n")
file.write("Learning Python is interesting.")
file.close()

# reading from the file
file = open("sample.txt", "r")
content = file.read()
print("File Content:\n", content)
file.close()

# appending data to file
file = open("sample.txt", "a")
file.write("\nThis line is added later.")
file.close()

# reading updated content
file = open("sample.txt", "r")
print("\nUpdated File Content:\n", file.read())
file.close()