#Practical 8 : User defined functions

a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
name=input("Enter name:")
print("")
#function without parameters
def greet():
    print("Hello World")

#function with default values
def welcome(name="Guest"):
    print("Welcome",name)

#function with parameters but no return
def add(a,b):
    print(a,"+",b,"=",a+b)

#function with return
def square(a):
    return a*a

#Calling functions
greet()
welcome(name)
add(a,b)
print("Square of",a,"=",square(a))