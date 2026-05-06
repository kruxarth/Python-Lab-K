# Practical 10 - File Handling in Python (Modified Version)

# --- Writing to a file ---
with open('employee.txt', 'w') as f:
    f.write('Name: Rahul\n')
    f.write('ID: 201\n')
    f.write('Department: IT\n')
    f.write('Salary: 50000\n')

print('File created and data written successfully.')


# --- Reading full file ---
with open('employee.txt', 'r') as f:
    data = f.read()

print('\n--- File Content ---')
print(data)


# --- Reading line by line ---
print('--- Reading Line by Line ---')
with open('employee.txt', 'r') as f:
    for line in f:
        print(line.strip())


# --- Appending new data ---
with open('employee.txt', 'a') as f:
    f.write('City: Pune\n')

print('\n--- After Appending ---')
with open('employee.txt', 'r') as f:
    print(f.read())


# --- Using readlines() ---
with open('employee.txt', 'r') as f:
    lines = f.readlines()

print(f'Total number of lines: {len(lines)}')
print('Last line:', lines[-1].strip())