# for loop
for i in range(5):
    print("For Loop:", i)

# while loop
i = 0
while i < 5:
    print("While Loop:", i)
    i += 1

# nested loop
for i in range(2):
    for j in range(2):
        print(i, j)

# loop control
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print("Control:", i)