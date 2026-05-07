# Practical - CSV File Handling in Python

import csv

# 1. Writing to CSV file
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    
    # Writing header
    writer.writerow(["Name", "Age", "City"])
    
    # Writing data rows
    writer.writerow(["Alice", 21, "Mumbai"])
    writer.writerow(["Bob", 22, "Pune"])
    writer.writerow(["Charlie", 20, "Delhi"])

print("Data written successfully.\n")

# 2. Reading entire CSV file
print("--- Reading Full CSV ---")
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    
    for row in reader:
        print(row)

# 3. Reading CSV using DictReader
print("\n--- Reading using DictReader ---")
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        print(f"Name: {row['Name']}, Age: {row['Age']}, City: {row['City']}")


# 4. Appending data to CSV file
with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["David", 23, "Nagpur"])

print("\nData appended successfully.\n")


# 5. Reading updated CSV file
print("--- Updated CSV Content ---")
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    
    for row in reader:
        print(row)


# 6. Counting total rows
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    data = list(reader)

print(f"\nTotal rows (including header): {len(data)}")
print(f"Total students: {len(data) - 1}")