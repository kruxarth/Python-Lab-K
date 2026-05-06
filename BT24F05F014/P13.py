import csv

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Yadvi", 20, "Aurangabad"])
    writer.writerow(["Rahul", 22, "Pune"])
    writer.writerow(["Sneha", 19, "Mumbai"])
