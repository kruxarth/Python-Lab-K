# Built-in Functions Program

numbers = []

n = int(input("How many elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

print("\nList:", numbers)
print("Length:", len(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))
print("Sorted:", sorted(numbers))