practical 6 : Loops in python 
n = int(input("Enter a number: "))

print("\nFor loop:")
for i in range(1, n + 1):
    print(i, end=" ")

print("\n\nWhile loop:")
i = 1
while i <= n:
    print(i, end=" ")
    i += 1

print("\n\nFor loop with list:")
nums = [10, 20, 30, 40, 50]
for num in nums:
    print(num, end=" ")

print("\n\nNested loop (pattern):")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
