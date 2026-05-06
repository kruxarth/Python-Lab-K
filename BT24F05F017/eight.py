def add_numbers(a, b):
	return a + b


def greet(name):
	return f"Hello, {name}!"


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
name = input("Enter your name: ")

print("Sum:", add_numbers(x, y))
print(greet(name))
