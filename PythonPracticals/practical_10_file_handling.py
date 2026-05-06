file = open("vijay_data.txt", "w")
file.write("Name: Vijay Shinde\n")
file.write("City: Aurangabad\n")
file.write("Course: BCA\n")
file.close()
print("Student: Vijay | File written successfully.")
file = open("vijay_data.txt", "r")
content = file.read()
file.close()
print("Student: Sarika | File Content:\n", content)
file = open("vijay_data.txt", "a")
file.write("Marks: 88\n")
file.close()
print("Student: Omkar | Data appended.")
with open("vijay_data.txt", "r") as file:
    lines = file.readlines()
print("Student: Omkar | Lines in file:")
for line in lines:
    print(line.strip())
import os
if os.path.exists("vijay_data.txt"):
    print("File exists.")
else:
    print("File not found.")
