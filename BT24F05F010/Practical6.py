"""Practical 6: Loop Structures (for, while, nested loops, and loop control)"""

# For loop iteration
for iteration in range(5):
    print("For Loop:", iteration)

# While loop iteration
counter = 0
while counter < 5:
    print("While Loop:", counter)
    counter += 1

# Nested for loops
for row in range(2):
    for col in range(2):
        print(row, col)

# Loop control with continue and break
for num in range(5):
    if num == 2:
        continue  # Skip this iteration
    if num == 4:
        break  # Exit loop
    print("Control:", num)