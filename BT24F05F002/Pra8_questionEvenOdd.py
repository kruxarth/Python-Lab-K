# This program counts the number of even, odd, and zero digits in a given number.
# practical 8: Count Even, Odd, and Zero Digits in a Number
def count_digits(n):
    even = odd = zero = 0
    if n == 0:
        zero += 1
    else:
        while n > 0:
            d = n % 10
            if d == 0:
                zero += 1
            elif d % 2 == 0:
                even += 1
            else:
                odd += 1
            n = n // 10

    return zero, even, odd

# taking input
num = int(input("Enter a number: "))
z, e, o = count_digits(num)
print(f"no. of zeros are : {z}")
print(f"no. of evens are : {e}")
print(f"no. of odds are : {o}")
