Practical 10 : File handling in python 
filename = "sample.txt"

file = open(filename, "w")
text = input("Enter text to write in file: ")
file.write(text)
file.close()

file = open(filename, "r")
content = file.read()
print("\n--- File Content ---")
print(content)
file.close()

file = open(filename, "a")
extra = input("\nEnter extra text to append: ")
file.write("\n" + extra)
file.close()

file = open(filename, "r")
print("\n--- Updated File Content ---")
print(file.read())
file.close()

file = open(filename, "r")
print("\nReading line by line:")
for line in file:
    print(line.strip())
file.close()
