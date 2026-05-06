import csv
data = [
    ["Name", "Department", "Salary", "City"],
    ["Aishwarya Desai", "IT", 45000, "Pune"],
    ["Rohit Mane", "HR", 38000, "Mumbai"],
    ["Meghna Patil", "Finance", 52000, "Aurangabad"],
    ["Nilima Jadhav", "IT", 47000, "Nashik"],
    ["Pravin Shinde", "Admin", 35000, "Nagpur"],
    ["Shital More", "Finance", 55000, "Pune"]
]
with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
print("Student: Aishwarya | CSV file written successfully.")
new_employee = ["Rahul Kulkarni", "IT", 49000, "Mumbai"]
with open("employees.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(new_employee)
print("Student: Rohit | New record appended.")
with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    print("Student: Meghna | Employee Records:")
    for row in reader:
        print(row)
with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    it_employees = [row for row in reader if row["Department"] == "IT"]
print("Student: Nilima | IT Department Employees:")
for emp in it_employees:
    print(emp["Name"], "-", emp["Salary"])
with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    salaries = [int(row["Salary"]) for row in reader]
print("Student: Pravin | Total Salary:", sum(salaries))
print("Student: Shital | Average Salary:", sum(salaries)/len(salaries))
