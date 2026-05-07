# Practical 4 — Studying Various Types of Operators in Python
# Aim: To study and implement Arithmetic, Comparison, Assignment,
#       Logical, Bitwise and Identity operators.

a, b = 10, 3

# 1. Arithmetic
print("Arithmetic:", a+b, a-b, a*b, a/b, a//b, a%b, a**b)

# 2. Comparison
print("Comparison :", a==b, a!=b, a>b, a<b, a>=b, a<=b)

# 3. Assignment
x = 5;  x += 3;  print("x after +=3 :", x)
x -= 2;          print("x after -=2 :", x)
x **= 2;         print("x after **=2:", x)

# 4. Logical
print("Logical:", (a>5 and b<5), (a<5 or b<5), not(a==b))

# 5. Bitwise
print("Bitwise: &=", a&b, "|", a|b, "^=", a^b,
      "~a=", ~a, "<<", a<<1, ">>", a>>1)

# 6. Identity
lst1 = [1, 2, 3]
lst2 = lst1
lst3 = [1, 2, 3]
print(lst1 is lst2)      # True  — same object in memory
print(lst1 is lst3)      # False — equal values, different objects
print(lst1 is not lst3)  # True
