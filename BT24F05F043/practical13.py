# Practical - Writing CSV File in Python

import csv

# -------------------------------
# 1. Writing data to CSV file
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    
    # Writing header
    writer.writerow(["Name", "Age", "City"])
    
    # Writing multiple rows
    writer.writerow(["Alice", 21, "Mumbai"])
    writer.writerow(["Bob", 22, "Pune"])
    writer.writerow(["Charlie", 20, "Delhi"])

print("CSV file written successfully.\n")


# 2. Writing multiple rows using writerows()
data = [
    ["David", 23, "Nagpur"],
    ["Emma", 22, "Bangalore"]
]

with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Multiple rows added successfully.\n")


# 3. Writing using DictWriter
data_dict = [
    {"Name": "Amit", "Age": 24, "City": "Mumbai"},
    {"Name": "Neha", "Age": 21, "City": "Pune"}
]

with open("students_dict.csv", "w", newline="") as file:
    fieldnames = ["Name", "Age", "City"]
    
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(data_dict)

print("CSV file using DictWriter created successfully.")