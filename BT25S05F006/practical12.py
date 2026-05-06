import csv
file = open("data.csv", "r")

reader = csv.reader(file)

print("CSV File Content:")

for row in reader:
    print(row)

file.close()