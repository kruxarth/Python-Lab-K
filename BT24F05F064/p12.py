Practical 12 : Read csv file 
import csv

filename = input("Enter CSV file name: ")

print("\n--- Method 1: csv.reader() ---")
try:
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except Exception as e:
    print("Error:", e)

print("\n--- Method 2: csv.DictReader() ---")
try:
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(dict(row))
except Exception as e:
    print("Error:", e)

print("\n--- Method 3: readlines() method ---")
try:
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip().split(","))
except Exception as e:
    print("Error:", e)

print("\n--- Method 4: pandas method ---")
try:
    import pandas as pd
    df = pd.read_csv(filename)
    print(df)
except Exception as e:
    print("Error (pandas may not be installed):", e)
