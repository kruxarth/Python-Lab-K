#Practical 5 : Conditional Statements
num=int(input("Enter a number:"))
#if statement
if(num>=0):
    print("positive number")

#if-else statement
if(num%2==0):
    print("even number")
else:
    print("odd number")

#nested if-else
if(num>=0):
    if(num<10):
        print("Single Digit Number")
    else:
        print("More Than 1 Digit Number")
else:
    print("negative number")

#if-elif-else ladder
if(num%2==0):
    print("even number")
elif (num==0):
    print("number is zero")
else:
    print("odd number")
