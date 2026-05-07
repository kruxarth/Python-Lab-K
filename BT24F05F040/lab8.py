#user defined functions
#Parameterized Function
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("aksh")  
#Function with default arguments
def fun(x, y=50):  
    print("x:", x)  
    print("y:", y)  

fun(10)
#Functions with Return value
def fun(num):
    return num * num

res = fun(5)
print(res)

