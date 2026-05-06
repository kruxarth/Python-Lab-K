
print("Counting to 5 using for loop:")
for i in range(1, 6):
    print(i, end=" ")

print("\n\nCounting down from 3 using while loop:")
count = 3
while count > 0:
    print(count)
    count -= 1  

print("\nNested Loop Output:")
for row in range(3):
    for col in range(3):
        print(f"({row},{col})", end=" ")
    print()