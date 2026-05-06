# Write to file
with open("sample.txt", "w") as f:
    f.write("Hello, File Handling!\n")
    f.write("Line 2\nLine 3\n")

# Read entire file
with open("sample.txt", "r") as f:
    print(f.read())

# Read line by line
with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())

# Append to file
with open("sample.txt", "a") as f:
    f.write("Appended line\n")

print("File operations done!")