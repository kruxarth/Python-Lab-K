# Practical 12 - Read CSV File

import csv

# --- First, create a sample CSV file to read ---
with open('students.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Roll', 'Branch', 'Marks'])
    writer.writerow(['Alice', 101, 'CS', 85])
    writer.writerow(['Bob', 102, 'IT', 90])
    writer.writerow(['Charlie', 103, 'ENTC', 78])
    writer.writerow(['Diana', 104, 'CS', 92])

print('Sample CSV file created.')

# --- Method 1: csv.reader() ---
print('\n--- Reading with csv.reader() ---')

with open('students.csv', 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)  # read header row
    print('Headers:', headers)

    for row in reader:
        print(row)

# --- Method 2: csv.DictReader() ---
print('\n--- Reading with DictReader() ---')

with open('students.csv', 'r') as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(f"Name: {row['Name']:<10}", end=' ')
        print(f"Roll: {row['Roll']}", end=' ')
        print(f"Marks: {row['Marks']}")

# --- Filtering data while reading ---
print('\n--- Students with Marks >= 88 ---')

with open('students.csv', 'r') as f:
    reader = csv.DictReader(f)

    for row in reader:
        if int(row['Marks']) >= 88:
            print(f"{row['Name']} - {row['Marks']}")