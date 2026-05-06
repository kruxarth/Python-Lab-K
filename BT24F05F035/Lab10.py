f = open("example.txt", "w")
f.write("Hello, this is a sample text file.\n")
f.write("My name is Meeran.\n")
f.close()

print("File created and data written successfully.")

with open("example.txt", "r") as fh:
    print("Reading from file:")
    content = fh.read()
    print(content)

file_handle = open("example.txt", "a")
file_handle.write("This line is appended to the file.\n")
file_handle.close()

print("Data appended successfully.")

with open("example.txt", "r") as fh:
    print("Reading from file after appending:")
    print(fh.read())