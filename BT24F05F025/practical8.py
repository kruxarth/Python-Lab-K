# Simple function
def student():
    rollno=input("Enter Roll no : ")
    name=input("Enter name : ")
    per=input("Enter percentage : ")
    print(f"Hello my Roll no is {rollno} my name is {name} and my per is {per}")
student()

# Parameterized function 
def student(rollno,name,per):
    print(f"Hello my Roll no is {rollno} my name is {name} and my per is {per}")
student(2,"John",92.40)

#Lambda Function
add = lambda a, b: a + b
print(add(3, 5))  
