# String
s = "Hello, Python"
print(s.upper(), s.lower(), s.split(","), s.replace("Python","World"))

# List
lst = [1, 2, 3, 4, 5]
lst.append(6); lst.remove(1)
print("List:", lst, lst[1:4])

# Tuple
tup = (10, 20, 30)
print("Tuple:", tup, tup[0], tup.count(10))

# Set
st = {1, 2, 3, 2, 1}
st.add(4)
print("Set:", st)
a, b = {1,2,3}, {2,3,4}
print("Union:", a|b, "Intersection:", a&b, "Difference:", a-b)