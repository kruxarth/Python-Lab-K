# Practical 6 Loops in Python

# 1. for loop
print("Squares using for loop:", end=" ")
for i in range(1, 6):
    print(i**2, end=" ")
print()


# 2. while loop – Fibonacci series
print("Fibonacci (while loop):")
a, b, n = 0, 1, 8

while n > 0:
    print(a, end=" ")
    a, b = b, a + b
    n -= 1
print()


# 3. Multiplication table of a number (user input)
num_input = input("\nEnter a number for multiplication table: ")

if num_input.isdigit():
    num = int(num_input)
    
    print(f"\nMultiplication Table of {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
else:
    print("Invalid input! Please enter a number.")


# 4. break and continue
print("\nSkip even, stop at 7:")
for k in range(1, 10):
    if k % 2 == 0:
        continue   # skip even numbers
    if k == 7:
        break      # stop at 7
    print(k, end=" ")
print()


# 5. for-else clause
nums = [2, 4, 7, 10]

for n in nums:
    if n == 7:
        print("\n7 found in list!")
        break
else:
    print("\n7 not found")