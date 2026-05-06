# Practical 7 Built-in Functions

nums = [5,6,1,8,6,3,8]

# Mathematical
print("abs(-7)  :", abs(-7))
print("round    :", round(3.14159, 3))
print("pow(2,10):", pow(2, 10))
print("divmod   :", divmod(17, 5)) # (3, 2)

# Sequence operations
print("max      :", max(nums))
print("min      :", min(nums))
print("sum      :", sum(nums))
print("sorted   :", sorted(nums))
print("reversed :", list(reversed(nums)))

# enumerate
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")

# zip
scores =[65,78,90]
for student, score in zip(fruits, scores):
    print(f"{student}: {score}")
    
# map and filter
squares = list(map(lambda x: x**2, nums))
evens = list(filter(lambda x: x%2==0, nums))

print("Squares:", squares)
print("Evens:  ", evens)

# any and all
print("any > 8:", any(x > 8 for x in nums))
print("all > 0:", all(x > 0 for x in nums))