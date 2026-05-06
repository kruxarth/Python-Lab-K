# Practical 9 Strings, Lists, Tuples and Sets

# --- STRINGS ---
text = "Hello, Python World!"
print(text.upper(), text.lower())
print("Length :", len(text))
print("Slice  :", text[7:13])           # Python
print("Reverse:", text[::-1])
print("Replace:", text.replace("Python", "Beautiful"))
print("Split  :", text.split(", "))
print("Find   :", text.find("Python"))

# --- LISTS ---
list_data = [40, 10, 30, 50, 20]
list_data.append(60)
list_data.insert(2, 99)
list_data.remove(99)
list_data.sort()
print("\nList   :", list_data)
print("Sliced :", list_data[1:4])
squared_nums = [n**2 for n in range(1, 6)] # list comprehension
print("Squares:", squared_nums)

# --- TUPLES ---
tuple_data = (1, 2, 3, 2, 4, 2)
print("\nTuple   :", tuple_data)
print("Count 2 :", tuple_data.count(2))
print("Index 3 :", tuple_data.index(3))
x, y, *remaining = tuple_data                      # tuple unpacking
print("Unpack  :", x, y, remaining)

# --- SETS ---
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print("\nUnion        :", set_a | set_b)
print("Intersection :", set_a & set_b)
print("Difference   :", set_a - set_b)
print("Sym Diff     :", set_a ^ set_b)

set_a.add(10)
set_a.discard(1)
print("Updated A    :", set_a)








