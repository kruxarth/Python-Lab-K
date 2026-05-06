# for loop
for i in range(1, 6):
    print("for:", i)

# while loop
n = 1
while n <= 5:
    print("while:", n)
    n += 1

# nested loop (multiplication table)
for i in range(1, 4):
    for j in range(1, 4):
        print(i*j, end="\t")
    print()