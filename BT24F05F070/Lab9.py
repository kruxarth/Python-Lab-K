text = "python"
print("String:", text)
print("Upper:", text.upper())
print("Slice:", text[1:4])

numbers = [10, 20, 30]
numbers.append(40)
numbers.remove(20)
print("List:", numbers)

fruits = ("apple", "banana", "mango")
print("Tuple:", fruits)
print("Count of apple:", fruits.count("apple"))
print("Index of mango:", fruits.index("mango"))

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Set union:", set_a.union(set_b))
print("Set intersection:", set_a.intersection(set_b))
