#Practical 10 : File Handling

#1. Writing to a file
file = open("student.txt", "w")
file.write("Name: SSJ\n")
file.write("Age: 19\n")
file.write("Department: CSE\n")
file.close()
print("Data written to file successfully.")
print("")

# 2. Reading from the file
file= open("student.txt", "r")
content = file.read()
print("\nReading file content:")
print(content, end="") # prevents extra blank line
file.close()
print("")

#3. Appending data to the file
file = open("student.txt", "a")
file.write("Grade: A\n")
file.close()
print("\nData appended successfully.")
print("")

#4. Reading file line by line
file= open("student.txt", "r")
print("\nReading file line by line:")

for line in file:
   print(line.strip())
file.close()