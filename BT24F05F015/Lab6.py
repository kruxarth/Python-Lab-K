# For loop
for i in range(5):
    print("For Loop:", i)

# While loop
i = 0
while i < 5:
    print("While Loop:", i)
    i += 1

# Nested loop
for i in range(2):
    for j in range(2):
        print(i, j)

# Loop control
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print("Control:", i)