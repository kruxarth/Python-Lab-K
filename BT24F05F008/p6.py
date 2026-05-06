# Practical 6 Loops in Python

# 1. for loop
print("Squares using for loop:", end=" ")
for counter in range(1, 6):
    print(counter**2, end=" ")
print()

# 2. while loop Fibonacci series
print("Fibonacci (while loop):")
first, second, count = 0, 1, 8
while count > 0:
    print(first, end=" ")
    first, second = second, first+second
    count -= 1
print()

# 3. Nested loop: Multiplication table
print("\nMultiplication Table (3x3):")
for counter in range(1, 4):
    for col in range(1, 4):
        print(f"{counter*col:3}", end="")
    print()

# 4. break and continue
print("\nSkip even, stop at 7:")
for val in range(1, 10):
    if val % 2 == 0: 
        continue  # skip even numbers
    if val == 7: 
        break     # stop at 7
    print(val, end=" ")
print()

# 5. for-else clause
numbers = [2, 4, 7, 10]
for item in numbers:
    if item == 7:
        print("\n7 found in list!")
        break
else:
    print("\n7 not found")

    