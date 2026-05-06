print("1. For Loop")
for i in range(1, 4):
    print(i)

print("\n2. While Loop")
j = 1
while j <= 5:
    print(j)
    j += 1

print("\n3. Nested Loop")
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

print("\n4. Break Statement")
for i in range(1, 6):
    if i == 5:
        break
    print(i)

print("\n5. Continue Statement")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)