# Advanced CSV File Handling Program

import csv

print("----- CSV FILE OPERATIONS -----")

# Open and read CSV file
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    
    data = list(reader)   # Convert into list
    
    print("\n--- COMPLETE DATA ---")
    for row in data:
        print(" | ".join(row))

# Count rows and columns
print("\n--- FILE DETAILS ---")
print("Total Rows:", len(data))

if len(data) > 0:
    print("Total Columns:", len(data[0]))

# Display header separately (if exists)
print("\n--- HEADER ---")
header = data[0]
print(header)

# Display remaining records
print("\n--- RECORDS ---")
for row in data[1:]:
    print(row)

# Searching in CSV
search = input("\nEnter value to search: ")
found = False

for row in data:
    if search in row:
        print("Found in row:", row)
        found = True

if not found:
    print("Value not found")

# Count specific column values (example: counting occurrences)
column_index = int(input("\nEnter column index to count values: "))

value_count = {}

for row in data[1:]:
    key = row[column_index]
    
    if key in value_count:
        value_count[key] += 1
    else:
        value_count[key] = 1

print("\n--- VALUE COUNT ---")
for key, value in value_count.items():
    print(key, ":", value)

print("\nProgram completed successfully!")