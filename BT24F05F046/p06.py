# Practical 6 Loops in Python

# 1. for loop
print("Squares using for loop:", end=" ")
for i in range(1, 6):
    print(i**2, end=" ")
print()

# 2. while loop Fibonacci series
print("Fibonacci (while loop):")
a, b, n = 0, 1, 8
while n > 0:
    print(a, end=" ")
    a, b = b, a+b
    n -= 1
print()

# 3. Nested loop: Multiplication table
print("\nMultiplication Table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i*j:3}", end="")
    print()

# 4. break and continue
print("\nSkip even, stop at 7:")
for k in range(1, 10):
    if k % 2 == 0: 
        continue  # skip even numbers
    if k == 7: 
        break     # stop at 7
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

    