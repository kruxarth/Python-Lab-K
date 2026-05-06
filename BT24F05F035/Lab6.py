counter = 0
while counter < 5:
    print("For Loop:", counter)
    counter += 1

num = 0
while num < 5:
    print("While Loop:", num)
    num += 1

for row in range(2):
    for col in range(2):
        print(row, col)

for idx in range(5):
    if idx == 2:
        continue
    if idx == 4:
        break
    print("Control:", idx)