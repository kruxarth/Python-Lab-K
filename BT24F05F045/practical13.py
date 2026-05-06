# Practical 13 - Write CSV File

import csv

# --- Writing CSV file ---
with open('students.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # Header
    writer.writerow(['Name', 'Roll', 'Branch', 'Marks'])

    # Data rows
    writer.writerow(['Alice', 101, 'CS', 85])
    writer.writerow(['Bob', 102, 'IT', 90])
    writer.writerow(['Charlie', 103, 'ENTC', 78])
    writer.writerow(['Diana', 104, 'CS', 92])

print("CSV file created successfully!")