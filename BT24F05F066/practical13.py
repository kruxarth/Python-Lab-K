import csv

# data to be written
data = [
    ['Name', 'Age', 'City'],
    ['Anjali', 20, 'Aurangabad'],
    ['Rahul', 22, 'Pune'],
    ['Sneha', 19, 'Mumbai']
]

# open file in write mode
with open('students.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # write multiple rows
    writer.writerows(data)

print("CSV file created successfully!")