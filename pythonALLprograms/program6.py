# Loop Program

print("----- LOOP OPERATIONS -----")

# For loop - sum of numbers
n = int(input("Enter number: "))
sum = 0

for i in range(1, n+1):
    sum += i
print("Sum of numbers:", sum)

# While loop - factorial
num = int(input("\nEnter number for factorial: "))
fact = 1
i = 1

while i <= num:
    fact *= i
    i += 1
print("Factorial:", fact)

# Nested loop - pattern
print("\nPattern:")
for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()