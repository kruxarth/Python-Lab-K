# Practical 7 Built-in Functions

data_set = [5, 2, 9, 1, 7, 4, 8, 3, 6]

# Mathematical
print("abs(-7)  :", abs(-7))
print("round    :", round(3.14159, 3))
print("pow(2,10):", pow(2, 10))
print("divmod   :", divmod(17, 5)) # (3, 2)

# Sequence operations
print("max      :", max(data_set))
print("min      :", min(data_set))
print("sum      :", sum(data_set))
print("sorted   :", sorted(data_set))
print("reversed :", list(reversed(data_set)))

# enumerate
items = ["apple", "banana", "cherry"]
for index, item in enumerate(items, start=1):
    print(f"{index}. {item}")

# zip
marks = [85, 90, 78]
for name, score in zip(items, marks):
    print(f"{name}: {score}")

# map and filter
squared = list(map(lambda num: num**2, data_set))
even_numbers = list(filter(lambda num: num%2==0, data_set))

print("Squares:", squared)
print("Evens:  ", even_numbers)

# any and all
print("any > 8:", any(num > 8 for num in data_set))
print("all > 0:", all(num > 0 for num in data_set))












