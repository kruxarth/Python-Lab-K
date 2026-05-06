import csv
students = [
    ["Name", "Age", "City", "Marks"],
    ["Amruta Jadhav", 21, "Aurangabad", 88],
    ["Rajesh Kulkarni", 22, "Pune", 76],
    ["Sunanda More", 20, "Nashik", 91],
    ["Ketan Pawar", 23, "Mumbai", 83],
    ["Varsha Shinde", 21, "Nagpur", 79]
]
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)
print("CSV file created.")
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    print("Student: Amruta | All Records:")
    for row in reader:
        print(row)
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    print("Student: Rajesh | Name and Marks:")
    for row in reader:
        print(row["Name"], "->", row["Marks"])
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    marks = [int(row["Marks"]) for row in reader]
print("Student: Sunanda | Max Marks:", max(marks))
print("Student: Ketan | Min Marks:", min(marks))
print("Student: Varsha | Average Marks:", sum(marks)/len(marks))
