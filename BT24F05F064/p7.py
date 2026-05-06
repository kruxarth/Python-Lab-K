practical 7 : Build in function 
num = int(input("Enter an integer: "))
text = input("Enter a string: ")
lst_input = input("Enter numbers separated by space: ")

lst = list(map(int, lst_input.split()))

print("\n--- Number Functions ---")
print("Absolute value:", abs(num))
print("Power (num^2):", pow(num, 2))
print("Binary:", bin(num))

print("\n--- String Functions ---")
print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

print("\n--- List Functions ---")
print("List:", lst)
print("Length of list:", len(lst))
print("Maximum:", max(lst))
print("Minimum:", min(lst))
print("Sum:", sum(lst))
print("Sorted list:", sorted(lst))

print("\n--- Type Conversion Functions ---")
print("String to int:", int("100"))
print("Int to string:", str(num))
print("Float conversion:", float(num))

print("\n--- Misc Built-in Functions ---")
print("Type of num:", type(num))
print("Rounded value of 5.6:", round(5.6))
print("Absolute of -25:", abs(-25))
