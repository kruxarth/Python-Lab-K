import csv

data = [
    ['ID', 'Product', 'Price'],
    [101, 'Laptop', 1200],
    [102, 'Mouse', 25],
    [103, 'Monitor', 300]
]

with open('products.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerows(data)

print("CSV file 'products.csv' created successfully.")