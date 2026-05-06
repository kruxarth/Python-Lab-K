# This program performs basic arithmetic operations (addition, subtraction, multiplication, and division) on two numbers entered by the user.
# practical 4: Sum, Subtraction, Multiplication, Division using functions
def sum_return(a, b):
    return a + b
def sub_return(a, b):
    return a - b
def multi_return(a, b):
    return a * b
def div_return(a, b):
    while(b==0):
        b = int(input("Please enter a valid number for division: "))
    return a / b
    

a = int(input("enter a : "))
b = int(input("enter b : "))

sum = sum_return(a, b)
sub = sub_return(a, b)
multi = multi_return(a, b)
div = div_return(a, b)

print(f"the sum of {a} and {b} is {sum}")
print(f"the sub of {a} and {b} is {sub}")
print(f"the multi of {a} and {b} is {multi}")
print(f"the div of {a} and {b} is {div}")