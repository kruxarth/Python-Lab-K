# Practical 12 — Read CSV File

import csv

# --- First, create a sample CSV file to read ---
with open('students.csv', 'w', newline='') as file_obj:
    csv_writer = csv.writer(file_obj)

    csv_writer.writerow(['Name', 'Roll', 'Branch', 'Marks'])
    csv_writer.writerow(['Alice', 101, 'CS', 85])
    csv_writer.writerow(['Bob', 102, 'IT', 90])
    csv_writer.writerow(['Charlie', 103, 'ENTC', 78])
    csv_writer.writerow(['Diana', 104, 'CS', 92])

print('Sample CSV file created.')

# --- Method 1: csv.reader() ---
print('\n--- Reading with csv.reader() ---')

with open('students.csv', 'r') as file_obj:
    csv_reader = csv.reader(file_obj)

    column_headers = next(csv_reader)  # read header row
    print('Headers:', column_headers)

    for record in csv_reader:
        print(record)

# --- Method 2: csv.DictReader() ---
print('\n--- Reading with DictReader() ---')

with open('students.csv', 'r') as file_obj:
    csv_reader = csv.DictReader(file_obj)

    for record in csv_reader:
        print(f"Name: {record['Name']:<10}",end=' ')
        print(f"Roll: {record['Roll']}",end=' ')
        print(f"Marks: {record['Marks']}",end='\n')

# --- Filtering data while reading ---
print('\n--- Students with Marks >= 88 ---')

with open('students.csv', 'r') as file_obj:
    csv_reader = csv.DictReader(file_obj)

    for record in csv_reader:
        if int(record['Marks']) >= 88:
            print(f"{record['Name']} - {record['Marks']}")












            