# Data Structures Program

# String
text = input("Enter a string: ")
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Length:", len(text))

# List
list1 = []
for i in range(3):
    list1.append(int(input("Enter list element: ")))

print("List:", list1)
list1.sort()
print("Sorted List:", list1)

# Tuple
tuple1 = tuple(list1)
print("Tuple:", tuple1)

# Set
set1 = set(list1)
print("Set:", set1)