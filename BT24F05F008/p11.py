# Practical 11 — Exception Handling in Python

# --- Basic try-except ---
try:
    number = int(input('Enter a number: '))
    division_result = 100 / number
    print('Result:', division_result)

except ZeroDivisionError:
    print('Error: Cannot divide by zero!')

except ValueError:
    print('Error: Please enter a valid integer.')

else:
    print('Division completed successfully.')

finally:
    print('Program execution complete.')

# --- Multiple exceptions ---
collection = [10, 20, 30]

try:
    index = int(input('\nEnter index (0-2): '))
    print('Value:', collection[index])

except IndexError as exception_obj:
    print('Error: Index out of range -', exception_obj)

except ValueError:
    print('Error: Invalid index input')

# --- File not found exception ---
try:
    with open('missing.txt', 'r') as file_obj:
        print(file_obj.read())

except FileNotFoundError:
    print('\nError: File does not exist!')

# --- raise statement ---
def check_age(years):
    if years < 0:
        raise ValueError('Age cannot be negative!')
    print('Valid age:', years)

try:
    check_age(-5)

except ValueError as exception_obj:
    print('Caught raised exception:', exception_obj)














    