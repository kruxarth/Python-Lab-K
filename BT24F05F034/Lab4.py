a = 10
b = 3

print("Arithmetic Operators")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a % b =", a % b)
print("a ** b =", a ** b)
print("a // b =", a // b)

print("\nComparison Operators")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

print("\nAssignment Operators")
x = 5
print("x =", x)
x += 2
print("x += 2 ->", x)
x *= 3
print("x *= 3 ->", x)

print("\nLogical Operators")
p = True
q = False
print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)

print("\nBitwise Operators")
m = 6   # 110
n = 2   # 010
print("m & n =", m & n)
print("m | n =", m | n)
print("m ^ n =", m ^ n)
print("~m =", ~m)
print("m << 1 =", m << 1)
print("m >> 1 =", m >> 1)

print("\nIdentity Operators")
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]
print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)
print("list1 is not list3:", list1 is not list3)
