# File Handling + Exception Handling
# Practice 11: exception handling while file handling
try:
    filename = input("Enter file name: ")

    with open(filename, "r") as file:
        content = file.read()
        print("\nFile Content:\n")
        print(content)

except FileNotFoundError:
    print("Error: File does not exist!")

except Exception as e:
    print("Something went wrong:", e)

finally:
    print("\nProgram executed.")
