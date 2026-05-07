# Practical 2 — Hello World Program
# Basic output
print("Hello, World!")

# print() with parameters
print("Hello", "World", sep=" | ", end="!\n")

# Taking user input
name = input("Enter your name: ")
age = input("Enter your age : ")

# f-string formatting
print(f"\nHello, {name}! You are {age} years old.")
print(f"Welcome to Python Programming!")

# Three formatting styles
print("Result: %d" % (5+3)) 
print("Result: {}".format(5+3)) 
print(f"Result: {5+3}") 