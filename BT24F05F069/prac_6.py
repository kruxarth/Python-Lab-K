# for loop
for i in range(6):
    print("For Loop:", i)

# while loop
i = 1
while i <= 4:
    print("While Loop:", i)
    i += 1

# nested loop
for i in range(3):
    for j in range(2):
        print(i, j)

# loop control
for i in range(10):
    if i == 3:
        continue
    if i == 7:
        break
    print("Control:", i)