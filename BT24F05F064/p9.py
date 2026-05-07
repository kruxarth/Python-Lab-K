Practical 9 : String,list,tuple and sets
text = input("Enter a string: ")

print("\n--- String Operations ---")
print("Original string:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Length:", len(text))
print("Reversed:", text[::-1])

lst_input = input("\nEnter list elements (space separated numbers): ")
lst = list(map(int, lst_input.split()))

print("\n--- List Operations ---")
print("List:", lst)
lst.append(100)
print("After append:", lst)
lst.remove(lst[0])
print("After remove first element:", lst)
print("Sorted list:", sorted(lst))
print("Max:", max(lst), "Min:", min(lst))

t = tuple(lst)

print("\n--- Tuple Operations ---")
print("Tuple:", t)
print("Length:", len(t))
print("First element:", t[0])
print("Last element:", t[-1])

set_input = input("\nEnter set elements (space separated numbers): ")
s = set(map(int, set_input.split()))

print("\n--- Set Operations ---")
print("Set:", s)

s.add(999)
print("After add:", s)

if len(s) > 0:
    s.pop()
print("After pop:", s)

print("Union with {1,2,3}:", s.union({1, 2, 3}))
print("Intersection with {1,2,3}:", s.intersection({1, 2, 3}))
