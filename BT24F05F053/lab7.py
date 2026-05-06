nums = [10, 20, 5, 40, 15]

print("List =", nums)

print("Length of list =", len(nums))
print("Maximum number =", max(nums))
print("Minimum number =", min(nums))
print("Sum of list =", sum(nums))

print("\n----- SORTED LIST -----")
print("Ascending =", sorted(nums))
print("Descending =", sorted(nums, reverse=True))

print("\n----- ABS FUNCTION -----")
x = -25
print("Absolute value of", x, "=", abs(x))

print("\n----- POWER FUNCTION -----")
a = 2
b = 5
print(a, "power", b, "=", pow(a, b))

print("\n----- ROUND FUNCTION -----")
num = 12.56789
print("Rounded to 2 decimals =", round(num, 2))

print("\n----- TYPE CONVERSION FUNCTIONS -----")
val = "100"
print("String value =", val)
print("Converted to integer =", int(val))
print("Converted to float =", float(val))

print("\n----- ALL & ANY FUNCTION -----")
list1 = [True, True, True]
list2 = [True, False, True]

print("all(list1) =", all(list1))
print("all(list2) =", all(list2))
print("any(list2) =", any(list2))