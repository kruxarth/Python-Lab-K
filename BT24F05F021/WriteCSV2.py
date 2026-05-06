import csv

fieldnames = ['Name', 'Department', 'Salary']
employees = [
    {'Name': 'Sarah', 'Department': 'IT', 'Salary': 75000},
    {'Name': 'Raj', 'Department': 'HR', 'Salary': 60000}
]

with open('employees.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
   
    writer.writeheader()

    writer.writerows(employees)

print("CSV file 'employees.csv' created successfully.")