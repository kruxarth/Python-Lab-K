print("For loop example")
for i in range(1, 6):
	print("Count:", i)

print("\nWhile loop example")
n = 1
while n <= 5:
	print("Number:", n)
	n += 1

print("\nNested loops example")
for row in range(1, 4):
	for col in range(1, 4):
		print(f"({row},{col})", end=" ")
	print()
