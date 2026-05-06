# Practical 12 - Read CSV File (Modified Version)

import csv

# --- Create a new CSV file ---
with open('employees.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['EmpName', 'EmpID', 'Department', 'Salary'])
    writer.writerow(['Rahul', 201, 'HR', 30000])
    writer.writerow(['Sneha', 202, 'Finance', 45000])
    writer.writerow(['Amit', 203, 'IT', 50000])
    writer.writerow(['Priya', 204, 'Marketing', 42000])

print('Employee CSV file created.')


# --- Method 1: csv.reader() ---
print('\n--- Reading using csv.reader() ---')
with open('employees.csv', 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)
    print('Headers:', headers)

    for row in reader:
        print(row)


# --- Method 2: csv.DictReader() ---
print('\n--- Reading using DictReader() ---')
with open('employees.csv', 'r') as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(f"Name: {row['EmpName']:<10}", end=' ')
        print(f"ID: {row['EmpID']}", end=' ')
        print(f"Salary: {row['Salary']}")


# --- Filtering data ---
print('\n--- Employees with Salary >= 40000 ---')
with open('employees.csv', 'r') as f:
    reader = csv.DictReader(f)

    for row in reader:
        if int(row['Salary']) >= 40000:
            print(f"{row['EmpName']} - {row['Salary']}")