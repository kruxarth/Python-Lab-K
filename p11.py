# Practical 11 - Exception Handling in Python

# --- Basic try-except ---
try:
    num = int(input('Enter a number: '))
    result = 100 / num
    print('Result:', result)
except ZeroDivisionError:
    print('Error: Cannot divide by zero!')
except ValueError:
    print('Error: Please enter a valid integer.')
else:
    print('Division completed successfully.')
finally:
    print('Program execution complete.')

# ---Multiple exceptions ---
data = [10, 20, 30]

try:
    idx = int(input('\nEnter index (0-2): '))
    print('Value:', data[idx])
except IndexError as e:
    print('Error: Index out of range -', e)
except ValueError:
    print('Error: Invalid index input')

# --- File not found exception ---
try:
    with open('missing.txt', 'r') as f:
        print(f.read())
except FileNotFoundError:
    print('\nError: File does not exist!')

# --- raise statement ---
def check_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative!')
    print('Valid age:', age)

try:
    check_age(-5)
except ValueError as e:
    print('Caught raised exception:', e)
