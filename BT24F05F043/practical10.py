# Practical 10 - File Handling in Python

# --- Writing to a file ---
with open('student.txt', 'w') as f:
    f.write('Name: Alice\n')
    f.write('Roll: 101\n')
    f.write('Branch: CS\n')
    f.write('Grade: A\n')

print('File written successfully.')

# --- Reading entire file ---
with open('student.txt', 'r') as f:
    content = f.read()

print('\n--- File Content ---')
print(content)

# --- Reading line by line ---
print('--- Line by Line ---')
with open('student.txt', 'r') as f:
    for line in f:
        print(line.strip())

# --- Appending to a file ---
with open('student.txt', 'a') as f:
    f.write('City: Mumbai\n')

print('\nContent after append:')
with open('student.txt', 'r') as f:
    print(f.read())

# --- readlines() method ---
with open('student.txt', 'r') as f:
    lines = f.readlines()

print(f'Total lines: {len(lines)}')
print('First line:', lines[0].strip())