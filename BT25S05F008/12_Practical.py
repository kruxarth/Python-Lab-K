import csv

# First create a sample CSV
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 25, "Mumbai"])
    writer.writerow(["Bob", 30, "Pune"])

# Read using csv module
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Read as dictionary
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(dict(row))