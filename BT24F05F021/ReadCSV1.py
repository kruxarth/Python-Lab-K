import csv

with open('students.csv', mode='r') as file:
    csv_reader = csv.reader(file)

    header = next(csv_reader)
    print(f"Headers: {header}")
    
    for row in csv_reader:
        print(f"Name: {row[0]}, Age: {row[1]}, Grade: {row[2]}")



