# Practical 4 Operators in Python

num1, num2 = 15, 4

# 1. Arithmetic
print("Arithmetic:", num1+num2, num1-num2, num1*num2, num1/num2, num1//num2, num1%num2, num1**num2)

# 2. Comparison
print("Comparison:", num1==num2, num1!=num2, num1>num2, num1<num2, num1>=num2, num1<=num2)

# 3. Assignment
counter = 8
counter += 2; print("counter after +=2 :", counter)
counter -= 3; print("counter after -=3 :", counter)
counter **= 2; print("counter after **=2:", counter)

# 4. Logical
print("Logical:", (num1>7 and num2<6), (num1<8 or num2<6), not(num1==num2))

# 5. Bitwise
print("Bitwise: &=", num1&num2, "|=", num1|num2, "^=", end=" ")
print(num1^num2, "~num1=", ~num1, "<<", num1<<1, ">>", num1>>1)

# 6. Identity
list_a = [5, 10, 15]
list_b = [5, 10, 15]
list_c = list_a

print(list_a is list_b)      # False - equal values, different objects
print(list_a is list_c)      # True - same object in memory
print(list_a is not list_c)  # False


