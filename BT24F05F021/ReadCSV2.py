import csv

with open('students.csv', mode='r') as file:
    dict_reader = csv.DictReader(file)
    
    for row in dict_reader:
        print(f"Student: {row['Name']} scored {row['Grade']}")