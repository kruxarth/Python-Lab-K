for i in range(1, 6):
    print(i)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

text = "Python"
for char in text:
    print(char)

numbers = [1, 2, 3, 4, 5]
sum_num = 0
for num in numbers:
    sum_num += num
print("Sum:", sum_num)

list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
for i, j in zip(list1, list2):
    print(i, j)

for i in range(1, 6):
    for j in range(1, 4):
        print(f"({i},{j})", end=" ")
    print()

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

for i in range(1, 6):
    if i == 3:
        break
    print(i)

i = 1
while i <= 5:
    print(i)
    i += 1

count = 0
while count < 3:
    print("Iteration", count)
    count += 1

num = 0
while num < 10:
    if num == 5:
        break
    print(num)
    num += 1

num = 0
while num < 5:
    if num == 2:
        num += 1
        continue
    print(num)
    num += 1

x = 0
while True:
    print(x)
    x += 1
    if x >= 3:
        break

for i in range(3):
    for j in range(2):
        print(f"{i},{j}", end=" ")

# 2. FOR loop with list
print("\n2. FOR LOOP - Iterating through a list:")
print("-" * 70)
fruits = ["apple", "banana", "orange", "mango"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# 3. FOR loop with string
print("\n3. FOR LOOP - Iterating through a string:")
print("-" * 70)
word = "HELLO"
for char in word:
    print(f"Character: {char}")

# 4. FOR loop with dictionary
print("\n4. FOR LOOP - Iterating through a dictionary:")
print("-" * 70)
student = {"name": "John", "age": 20, "gpa": 3.8}
for key, value in student.items():
    print(f"{key}: {value}")

# 5. FOR loop with range parameters
print("\n5. FOR LOOP - Range with start, stop, and step:")
print("-" * 70)
print("Even numbers from 0 to 10:")
for i in range(0, 11, 2):
    print(i, end=" ")
print()

# 6. FOR loop with enumerate
print("\n6. FOR LOOP - Enumerate (index and value):")
print("-" * 70)
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")

# 7. FOR loop with break
print("\n7. FOR LOOP - With BREAK statement:")
print("-" * 70)
for i in range(1, 10):
    if i == 5:
        print(f"Breaking at {i}")
        break
    print(i, end=" ")
print()

# 8. FOR loop with continue
print("\n8. FOR LOOP - With CONTINUE statement:")
print("-" * 70)
print("Skipping even numbers:")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

# 9. FOR loop with else
print("\n9. FOR LOOP - With ELSE clause:")
print("-" * 70)
for i in range(1, 4):
    print(f"Loop iteration: {i}")
else:
    print("Loop completed successfully!")

# 10. Practical example: Sum of numbers
print("\n10. PRACTICAL EXAMPLE - Sum of numbers:")
print("-" * 70)
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print(f"Numbers: {numbers}")
print(f"Sum: {total}")

# ==================== WHILE LOOP ====================
print("\n" + "=" * 70)
print("WHILE LOOP")
print("=" * 70)

# 1. Basic WHILE loop
print("\n1. BASIC WHILE LOOP - Counting:")
print("-" * 70)
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

# 2. WHILE loop with user condition
print("\n2. WHILE LOOP - Until condition is met:")
print("-" * 70)
num = 1
while num <= 10:
    if num % 2 == 0:
        print(f"Even: {num}")
    num += 1

# 3. WHILE loop with break
print("\n3. WHILE LOOP - With BREAK statement:")
print("-" * 70)
i = 0
while True:
    print(f"Value: {i}")
    i += 1
    if i == 5:
        print("Breaking the loop")
        break

# 4. WHILE loop with continue
print("\n4. WHILE LOOP - With CONTINUE statement:")
print("-" * 70)
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(f"Odd: {i}", end=" ")
print()

# 5. WHILE loop with else
print("\n5. WHILE LOOP - With ELSE clause:")
print("-" * 70)
i = 1
while i <= 3:
    print(f"Loop: {i}")
    i += 1
else:
    print("While loop completed!")

# 6. Practical example: Factorial calculation
print("\n6. PRACTICAL EXAMPLE - Factorial Calculation:")
print("-" * 70)
num = 5
factorial = 1
temp = num
while temp > 1:
    factorial *= temp
    temp -= 1
print(f"Factorial of {num} = {factorial}")

# 7. Practical example: Powers of 2
print("\n7. PRACTICAL EXAMPLE - Powers of 2:")
print("-" * 70)
power = 1
while power <= 32:
    print(power, end=" ")
    power *= 2
print()

# ==================== NESTED LOOPS ====================
print("\n" + "=" * 70)
print("NESTED LOOPS")
print("=" * 70)

# 1. Nested FOR loops - Multiplication table
print("\n1. NESTED FOR LOOPS - Multiplication Table (1-5):")
print("-" * 70)
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i}x{j}={i*j}", end="\t")
    print()

# 2. Nested FOR loops - Pattern
print("\n2. NESTED FOR LOOPS - Star Pattern:")
print("-" * 70)
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# 3. Nested FOR loops - Number Pattern
print("\n3. NESTED FOR LOOPS - Number Pattern:")
print("-" * 70)
for i in range(1, 4):
    for j in range(1, i+2):
        print(j, end=" ")
    print()

# 4. Nested FOR loops - 2D List
print("\n4. NESTED FOR LOOPS - 2D List (Matrix):")
print("-" * 70)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

# 5. Nested WHILE loops
print("\n5. NESTED WHILE LOOPS:")
print("-" * 70)
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"({i},{j})", end=" ")
        j += 1
    print()
    i += 1

# 6. Nested loops with break
print("\n6. NESTED LOOPS - With BREAK:")
print("-" * 70)
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break
        print(f"{i}{j}", end=" ")
    print()

# 7. Nested loops with continue
print("\n7. NESTED LOOPS - With CONTINUE:")
print("-" * 70)
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            continue
        print(f"{i}{j}", end=" ")
    print()

# 8. Practical example: Prime numbers up to 50
print("\n8. PRACTICAL EXAMPLE - Prime Numbers (up to 50):")
print("-" * 70)
for num in range(2, 51):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print("\n")

# 9. Practical example: 2D array (Matrix) sum
print("\n9. PRACTICAL EXAMPLE - Matrix Sum:")
print("-" * 70)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix:")
for row in matrix:
    print(row)

total_sum = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        total_sum += matrix[i][j]

print(f"Sum of all elements: {total_sum}")

# 10. Practical example: Diamond pattern
print("\n10. PRACTICAL EXAMPLE - Diamond Pattern:")
print("-" * 70)
n = 5
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    print()

for i in range(n-1, 0, -1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    print()

# 11. Mixed loops - FOR and WHILE
print("\n11. MIXED LOOPS - FOR and WHILE:")
print("-" * 70)
for i in range(1, 4):
    j = 1
    while j <= i:
        print(f"{i}-{j}", end=" ")
        j += 1
    print()

# 12. Loop with pass statement
print("\n12. LOOPS - With PASS statement:")
print("-" * 70)
for i in range(1, 6):
    if i == 3:
        pass  # Do nothing for 3
    else:
        print(f"Number: {i}")

print("\n" + "=" * 70)
print("END OF PROGRAM")
print("=" * 70)
