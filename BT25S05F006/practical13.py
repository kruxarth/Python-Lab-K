import csv
with open("student.csv", "w", newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(["Name", "Age"])
    writer.writerow(["Karn", 20])

print("CSV file created and data written successfully.")