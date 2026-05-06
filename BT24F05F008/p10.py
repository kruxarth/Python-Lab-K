# Practical 10 — File Handling in Python

# --- Writing to a file ---
with open('student.txt', 'w') as file_obj:
    file_obj.write('Name: Alice\n')
    file_obj.write('Roll: 101\n')
    file_obj.write('Branch: CS\n')
    file_obj.write('Grade: A\n')

print('File written successfully.')

# --- Reading entire file ---
with open('student.txt', 'r') as file_obj:
    file_content = file_obj.read()

print('\n--- File Content ---')
print(file_content)

# --- Reading line by line ---
print('--- Line by Line ---')
with open('student.txt', 'r') as file_obj:
    for current_line in file_obj:
        print(current_line.strip())

# --- Appending to a file ---
with open('student.txt', 'a') as file_obj:
    file_obj.write('City: Mumbai\n')

print('\nContent after append:')
with open('student.txt', 'r') as file_obj:
    print(file_obj.read())

# --- readlines() method ---
with open('student.txt', 'r') as file_obj:
    all_lines = file_obj.readlines()

print(f'Total lines: {len(all_lines)}')
print('First line:', all_lines[0].strip())





















