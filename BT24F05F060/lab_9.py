# Practical 9 — Working With Strings, Lists, Tuples and Sets
# Aim: To study and implement Strings, Lists, Tuples and Sets in Python.

# ── STRINGS ──────────────────────────────────────────────────────
s = "Hello, Python World!"
print(s.upper())
print(s.lower())
print("Length  :", len(s))
print("Slice   :", s[7:13])                  # Python
print("Reverse :", s[::-1])
print("Replace :", s.replace("Python", "Beautiful"))
print("Split   :", s.split(", "))
print("Find    :", s.find("Python"))

# ── LISTS ─────────────────────────────────────────────────────────
lst = [40, 10, 30, 50, 20]
lst.append(60)
lst.insert(2, 99)
lst.remove(99)
lst.sort()
print("\nList    :", lst)
print("Sliced  :", lst[1:4])

squares = [x**2 for x in range(1, 6)]      # list comprehension
print("Squares :", squares)

# ── TUPLES ────────────────────────────────────────────────────────
t = (1, 2, 3, 2, 4, 2)
print("\nTuple   :", t)
print("Count 2 :", t.count(2))
print("Index 3 :", t.index(3))

a, b, *rest = t                             # tuple unpacking
print("Unpack  :", a, b, rest)

# ── SETS ──────────────────────────────────────────────────────────
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print("\nUnion        :", A | B)
print("Intersection :", A & B)
print("Difference   :", A - B)
print("Sym Diff     :", A ^ B)

A.add(10)
A.discard(1)
print("Updated A    :", A)
