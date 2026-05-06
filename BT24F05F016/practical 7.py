numbers = [3, 1, 4, 1, 5, 9, 2, 6]

print("Length:", len(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))

print("Range:", list(range(1, 6)))

print("Type of string:", type("hello"))
print("Type of list:", type([1, 2, 3]))

string = "hello"
print("Uppercase:", string.upper())
print("Lowercase:", string.lower())
print("Capitalized:", string.capitalize())

text = "a,b,c,d"
parts = text.split(",")
print("Split:", parts)

joined = "-".join(["a", "b", "c"])
print("Joined:", joined)

text = "hello world"
print("Find 'world':", text.find("world"))
print("Replace:", text.replace("world", "python"))

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("Concatenated list:", combined)

text = "  hello world  "
print("Stripped:", text.strip())

numbers = [5, 2, 8, 1, 9]
print("Sorted:", sorted(numbers))

num = "123"
print("String to int:", int(num))

num = 123
print("Int to string:", str(num))

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print("Squared:", squared)

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Evens:", evens)

numbers = [3, 1, 4, 1, 5]
print("All elements present:", all([x > 0 for x in numbers]))
print("Any element even:", any([x % 2 == 0 for x in numbers]))

for i, value in enumerate([10, 20, 30]):
    print(f"Index {i}: {value}")

data = zip([1, 2, 3], ["a", "b", "c"])
print("Zipped:", list(data))

print("Reversed:", list(reversed([1, 2, 3, 4, 5])))

print("Exists:", callable(print))

d = {"name": "Alice", "age": 25}
print("Keys:", list(d.keys()))
print("Values:", list(d.values()))
print("Items:", list(d.items()))

print("=" * 70)
print("BUILT-IN FUNCTIONS IN PYTHON")
print("=" * 70)

# ==================== STRING FUNCTIONS ====================
print("\n" + "=" * 70)
print("STRING FUNCTIONS")
print("=" * 70)

# 1. len() - Length of string
print("\n1. len() - Length of string:")
print("-" * 70)
text = "Hello World"
print(f"String: '{text}'")
print(f"Length: {len(text)}")

# 2. str() - Convert to string
print("\n2. str() - Convert to string:")
print("-" * 70)
num = 123
converted = str(num)
print(f"Number: {num}, Type: {type(num)}")
print(f"Converted: {converted}, Type: {type(converted)}")

# 3. upper() - Convert to uppercase
print("\n3. upper() - Convert to uppercase:")
print("-" * 70)
word = "python"
print(f"Original: {word}")
print(f"Uppercase: {word.upper()}")

# 4. lower() - Convert to lowercase
print("\n4. lower() - Convert to lowercase:")
print("-" * 70)
text = "PYTHON PROGRAMMING"
print(f"Original: {text}")
print(f"Lowercase: {text.lower()}")

# 5. strip() - Remove leading/trailing spaces
print("\n5. strip() - Remove leading/trailing spaces:")
print("-" * 70)
text = "  Hello World  "
print(f"Original: '{text}'")
print(f"After strip: '{text.strip()}'")

# 6. replace() - Replace substring
print("\n6. replace() - Replace substring:")
print("-" * 70)
text = "I like Python. Python is great!"
print(f"Original: {text}")
print(f"Replaced: {text.replace('Python', 'Java')}")

# 7. split() - Split string into list
print("\n7. split() - Split string into list:")
print("-" * 70)
text = "apple,banana,orange,mango"
print(f"Original: {text}")
print(f"Split by comma: {text.split(',')}")

# 8. join() - Join list to string
print("\n8. join() - Join list to string:")
print("-" * 70)
fruits = ["apple", "banana", "orange"]
print(f"List: {fruits}")
print(f"Joined: {', '.join(fruits)}")

# 9. find() - Find substring position
print("\n9. find() - Find substring position:")
print("-" * 70)
text = "Hello World Hello"
print(f"String: {text}")
print(f"Position of 'World': {text.find('World')}")
print(f"Position of 'Hello': {text.find('Hello')}")

# 10. startswith() and endswith()
print("\n10. startswith() and endswith():")
print("-" * 70)
text = "Python Programming"
print(f"Text: {text}")
print(f"Starts with 'Python': {text.startswith('Python')}")
print(f"Ends with 'ing': {text.endswith('ing')}")

# ==================== NUMBER FUNCTIONS ====================
print("\n" + "=" * 70)
print("NUMBER FUNCTIONS")
print("=" * 70)

# 1. int() - Convert to integer
print("\n1. int() - Convert to integer:")
print("-" * 70)
num_str = "42"
print(f"String: '{num_str}'")
print(f"Converted: {int(num_str)}, Type: {type(int(num_str))}")

# 2. float() - Convert to float
print("\n2. float() - Convert to float:")
print("-" * 70)
num_str = "3.14"
print(f"String: '{num_str}'")
print(f"Converted: {float(num_str)}, Type: {type(float(num_str))}")

# 3. abs() - Absolute value
print("\n3. abs() - Absolute value:")
print("-" * 70)
numbers = [10, -20, 5, -15, 0]
print(f"Numbers: {numbers}")
for num in numbers:
    print(f"abs({num}) = {abs(num)}")

# 4. round() - Round number
print("\n4. round() - Round number:")
print("-" * 70)
numbers = [3.4, 3.5, 3.6, 2.449, 2.451]
for num in numbers:
    print(f"round({num}) = {round(num)}")

# 5. pow() - Power function
print("\n5. pow() - Power function:")
print("-" * 70)
print(f"pow(2, 3) = {pow(2, 3)}")
print(f"pow(5, 2) = {pow(5, 2)}")
print(f"pow(10, 3) = {pow(10, 3)}")

# 6. min() - Minimum value
print("\n6. min() - Minimum value:")
print("-" * 70)
numbers = [45, 23, 89, 12, 56]
print(f"Numbers: {numbers}")
print(f"Minimum: {min(numbers)}")

# 7. max() - Maximum value
print("\n7. max() - Maximum value:")
print("-" * 70)
numbers = [45, 23, 89, 12, 56]
print(f"Numbers: {numbers}")
print(f"Maximum: {max(numbers)}")

# 8. sum() - Sum of numbers
print("\n8. sum() - Sum of numbers:")
print("-" * 70)
numbers = [10, 20, 30, 40, 50]
print(f"Numbers: {numbers}")
print(f"Sum: {sum(numbers)}")

# ==================== LIST/SEQUENCE FUNCTIONS ====================
print("\n" + "=" * 70)
print("LIST/SEQUENCE FUNCTIONS")
print("=" * 70)

# 1. len() - Length of list
print("\n1. len() - Length of list:")
print("-" * 70)
items = [1, 2, 3, 4, 5]
print(f"List: {items}")
print(f"Length: {len(items)}")

# 2. append() - Add element to list
print("\n2. append() - Add element to list:")
print("-" * 70)
fruits = ["apple", "banana"]
print(f"Original: {fruits}")
fruits.append("orange")
print(f"After append: {fruits}")

# 3. extend() - Add multiple elements
print("\n3. extend() - Add multiple elements:")
print("-" * 70)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"List1: {list1}")
print(f"List2: {list2}")
list1.extend(list2)
print(f"After extend: {list1}")

# 4. insert() - Insert at specific position
print("\n4. insert() - Insert at specific position:")
print("-" * 70)
items = ["a", "c", "d"]
print(f"Original: {items}")
items.insert(1, "b")
print(f"After insert(1, 'b'): {items}")

# 5. remove() - Remove element
print("\n5. remove() - Remove element:")
print("-" * 70)
items = [1, 2, 3, 2, 4]
print(f"Original: {items}")
items.remove(2)
print(f"After remove(2): {items}")

# 6. pop() - Remove and return element
print("\n6. pop() - Remove and return element:")
print("-" * 70)
items = [10, 20, 30, 40]
print(f"Original: {items}")
removed = items.pop(2)
print(f"Removed: {removed}")
print(f"After pop(2): {items}")

# 7. sort() - Sort list
print("\n7. sort() - Sort list:")
print("-" * 70)
numbers = [45, 23, 89, 12, 56]
print(f"Original: {numbers}")
numbers.sort()
print(f"After sort: {numbers}")

# 8. reverse() - Reverse list
print("\n8. reverse() - Reverse list:")
print("-" * 70)
items = [1, 2, 3, 4, 5]
print(f"Original: {items}")
items.reverse()
print(f"After reverse: {items}")

# 9. index() - Find index of element
print("\n9. index() - Find index of element:")
print("-" * 70)
fruits = ["apple", "banana", "orange", "mango"]
print(f"List: {fruits}")
print(f"Index of 'banana': {fruits.index('banana')}")

# 10. count() - Count occurrences
print("\n10. count() - Count occurrences:")
print("-" * 70)
numbers = [1, 2, 2, 3, 2, 4, 2, 5]
print(f"List: {numbers}")
print(f"Count of 2: {numbers.count(2)}")

# ==================== TYPE/CONVERSION FUNCTIONS ====================
print("\n" + "=" * 70)
print("TYPE AND CONVERSION FUNCTIONS")
print("=" * 70)

# 1. type() - Get data type
print("\n1. type() - Get data type:")
print("-" * 70)
var1 = 42
var2 = 3.14
var3 = "hello"
var4 = [1, 2, 3]
var5 = {"name": "John"}
print(f"type({var1}) = {type(var1)}")
print(f"type({var2}) = {type(var2)}")
print(f"type({var3}) = {type(var3)}")
print(f"type({var4}) = {type(var4)}")
print(f"type({var5}) = {type(var5)}")

# 2. isinstance() - Check instance type
print("\n2. isinstance() - Check instance type:")
print("-" * 70)
value = 42
print(f"Value: {value}")
print(f"isinstance(value, int): {isinstance(value, int)}")
print(f"isinstance(value, str): {isinstance(value, str)}")

# 3. bool() - Convert to boolean
print("\n3. bool() - Convert to boolean:")
print("-" * 70)
values = [0, 1, "", "hello", [], [1, 2], None]
for val in values:
    print(f"bool({repr(val)}) = {bool(val)}")

# 4. list() - Convert to list
print("\n4. list() - Convert to list:")
print("-" * 70)
string = "HELLO"
print(f"String: {string}")
print(f"list(string): {list(string)}")

# 5. tuple() - Convert to tuple
print("\n5. tuple() - Convert to tuple:")
print("-" * 70)
items = [1, 2, 3]
print(f"List: {items}")
print(f"tuple(list): {tuple(items)}")

# 6. dict() - Create dictionary
print("\n6. dict() - Create dictionary:")
print("-" * 70)
pairs = [("a", 1), ("b", 2), ("c", 3)]
print(f"Pairs: {pairs}")
print(f"dict(pairs): {dict(pairs)}")

# 7. set() - Create set
print("\n7. set() - Create set:")
print("-" * 70)
items = [1, 2, 2, 3, 3, 3, 4]
print(f"List: {items}")
print(f"set(items): {set(items)}")

# ==================== ITERATION FUNCTIONS ====================
print("\n" + "=" * 70)
print("ITERATION FUNCTIONS")
print("=" * 70)

# 1. range() - Generate sequence
print("\n1. range() - Generate sequence:")
print("-" * 70)
print(f"list(range(5)): {list(range(5))}")
print(f"list(range(2, 8)): {list(range(2, 8))}")
print(f"list(range(0, 10, 2)): {list(range(0, 10, 2))}")

# 2. enumerate() - Get index and value
print("\n2. enumerate() - Get index and value:")
print("-" * 70)
fruits = ["apple", "banana", "orange"]
for idx, fruit in enumerate(fruits):
    print(f"{idx}: {fruit}")

# 3. zip() - Combine sequences
print("\n3. zip() - Combine sequences:")
print("-" * 70)
names = ["Alice", "Bob", "Charlie"]
ages = [20, 25, 30]
for name, age in zip(names, ages):
    print(f"{name}: {age} years old")

# 4. map() - Apply function to sequence
print("\n4. map() - Apply function to sequence:")
print("-" * 70)
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Numbers: {numbers}")
print(f"Squared: {squared}")

# 5. filter() - Filter sequence
print("\n5. filter() - Filter sequence:")
print("-" * 70)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Numbers: {numbers}")
print(f"Even numbers: {evens}")

# 6. sorted() - Sort sequence
print("\n6. sorted() - Sort sequence:")
print("-" * 70)
numbers = [45, 23, 89, 12, 56]
print(f"Original: {numbers}")
print(f"sorted(): {sorted(numbers)}")
print(f"sorted(reverse=True): {sorted(numbers, reverse=True)}")

# ==================== USEFUL FUNCTIONS ====================
print("\n" + "=" * 70)
print("OTHER USEFUL FUNCTIONS")
print("=" * 70)

# 1. all() - Check if all elements are true
print("\n1. all() - Check if all elements are true:")
print("-" * 70)
list1 = [True, True, True]
list2 = [True, False, True]
print(f"all({list1}): {all(list1)}")
print(f"all({list2}): {all(list2)}")

# 2. any() - Check if any element is true
print("\n2. any() - Check if any element is true:")
print("-" * 70)
list1 = [False, False, False]
list2 = [False, True, False]
print(f"any({list1}): {any(list1)}")
print(f"any({list2}): {any(list2)}")

# 3. chr() - Get character from ASCII
print("\n3. chr() - Get character from ASCII:")
print("-" * 70)
print(f"chr(65): {chr(65)}")
print(f"chr(90): {chr(90)}")
print(f"chr(97): {chr(97)}")

# 4. ord() - Get ASCII value of character
print("\n4. ord() - Get ASCII value of character:")
print("-" * 70)
print(f"ord('A'): {ord('A')}")
print(f"ord('Z'): {ord('Z')}")
print(f"ord('a'): {ord('a')}")

# 5. hex() - Convert to hexadecimal
print("\n5. hex() - Convert to hexadecimal:")
print("-" * 70)
numbers = [10, 20, 255, 4095]
for num in numbers:
    print(f"hex({num}): {hex(num)}")

# 6. bin() - Convert to binary
print("\n6. bin() - Convert to binary:")
print("-" * 70)
numbers = [10, 20, 255]
for num in numbers:
    print(f"bin({num}): {bin(num)}")

# 7. input() - Get user input (demonstration)
print("\n7. input() - Get user input (demonstrated):")
print("-" * 70)
print("Note: input() reads user input as string")
# user_input = input("Enter something: ")
# print(f"You entered: {user_input}")

# 8. print() - Print output
print("\n8. print() - Print output:")
print("-" * 70)
print("Multiple values:", 1, 2, 3, sep="-")
print("With end parameter", "no newline", end="")
print(" - line continued")

# 9. eval() - Evaluate expression
print("\n9. eval() - Evaluate expression:")
print("-" * 70)
expression = "2 + 3 * 4"
result = eval(expression)
print(f"Expression: {expression}")
print(f"Result: {result}")

# 10. len() on different types
print("\n10. len() on different types:")
print("-" * 70)
string = "Python"
list_items = [1, 2, 3, 4]
dict_items = {"a": 1, "b": 2, "c": 3}
print(f"len('Python'): {len(string)}")
print(f"len([1, 2, 3, 4]): {len(list_items)}")
print(f"len({{'a': 1, 'b': 2, 'c': 3}}): {len(dict_items)}")

print("\n" + "=" * 70)
print("END OF PROGRAM")
print("=" * 70)
