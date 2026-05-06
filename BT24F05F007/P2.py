# Practical 2 Hello World Program

# Basic output
print("Hello, World!")

# print() with parameters
print("Hello", "World", sep=" | ", end="!\n")

# Taking user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# f-string formatting
print(f"\nHello, {name}! \nYou are {age} years old.")
print(f"Welcome to Python Programming!")

# Three formatting styles
print("Result: %d" % (5+3)) #% formatting
print("Result: {}".format (5+3)) #.format() method
print(f"Result: {5+3}") # f-string
