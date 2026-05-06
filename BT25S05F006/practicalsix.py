# for loop - sum of first 5 numbers
print("For Loop (Sum):")
sum = 0
for i in range(1, 6):
    sum += i
print("Sum =", sum)
# while loop - factorial of a number
print("\nWhile Loop (Factorial):")
num = 5
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
print("Factorial =", fact)
# nested loop - pattern printing
print("\nNested Loop (Pattern):")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()