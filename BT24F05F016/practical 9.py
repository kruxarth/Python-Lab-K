text = "Hello, Python!"
print(text)
print(text[0])
print(text[-1])
print(text[1:4])
print(len(text))

text = "Hello World"
print(text.upper())
print(text.lower())
print(text.replace('World', 'Python'))
print(text.split())

str1 = "Python"
str2 = "Programming"
print(str1 + " " + str2)

name = "Alice"
age = 25
print(f"{name} is {age} years old")

numbers = [1, 2, 3, 4, 5]
print(numbers[0])
print(numbers[-1])
print(len(numbers))

fruits = ['apple', 'banana']
fruits.append('cherry')
print(fruits)

fruits.insert(1, 'orange')
fruits.extend(['date'])
print(fruits)

fruits.remove('orange')
print(fruits)

numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

squares = [x**2 for x in range(1, 6)]
print(squares)

coords = (10, 20, 30, 40, 50)
print(coords[0])
print(coords[-1])
print(len(coords))

point = (10, 20)
x, y = point
print(f"x = {x}, y = {y}")

numbers = (1, 2, 3, 2, 4, 2)
print(numbers.index(3))
print(numbers.count(2))

set1 = {1, 2, 3, 4, 5}
set2 = {'apple', 'banana', 'cherry'}
print(set1)
print(set2)

set_from_list = set([1, 2, 2, 3, 3, 3])
print(set_from_list)

print(2 in {1, 2, 3})

colors = {'red', 'green'}
colors.add('blue')
print(colors)

colors.update(['yellow'])
colors.remove('red')
print(colors)

set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(f"Union: {set_a | set_b}")
print(f"Intersection: {set_a & set_b}")
print(f"Difference: {set_a - set_b}")
print(f"Symmetric: {set_a ^ set_b}")

numbers = [1, 2, 2, 3, 3, 3, 4]
unique = set(numbers)
print(unique)

text = "python python java python java"
words = text.split()
word_set = set(words)
word_count = {word: words.count(word) for word in word_set}
print(word_count)

grades = [85, 90, 78, 85, 92, 78]
unique_grades = set(grades)
print(sorted(unique_grades, reverse=True))

student_info = ("Alice", 25, 3.8, "CS")
print(student_info)

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = set(list1) & set(list2)
print(common)

