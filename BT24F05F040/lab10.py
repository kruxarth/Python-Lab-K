filename = "example.txt"

# 1. Writing to a file (Overwrites if exists)
with open(filename, "w", encoding="utf-8") as file:
    file.write("Hello, this is the first line.\n")
    file.write("Python file handling is simple.\n")

# 2. Appending data to an existing file
with open(filename, "a", encoding="utf-8") as file:
    file.write("This line was appended later.\n")

# 3. Reading the entire file
try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print("--- File Content ---")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

# 4. Reading line by line (Efficient for large files)
print("--- Reading Line by Line ---")
with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        print(f"Line: {line.strip()}")
