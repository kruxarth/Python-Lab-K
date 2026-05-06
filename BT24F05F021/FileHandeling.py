
with open("example.txt", "w") as file:
    file.write("Hello! This is a test file.\n")
    file.write("Python makes file handling easy.")

print("--- Reading File Content ---")
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

with open("example.txt", "a") as file:
    file.write("\nThis line was added using append mode.")

print("\n--- Reading Line by Line ---")
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip()) # strip() removes extra newlines