# Write a program to check whether the given string is a palindrome or not.
s=input("Enter the string to check the palindrome or not : ")
rev=""
for ch in s:
     rev=ch+rev
     if(rev==s):
          print("String is palindrome: ", rev)
     else:
          print("String not is palindrome: ", rev)


# Write a program to find the largest and smallest element in a list.
list1={10,20,30,44,33,22}
print("Largest : ",max(list1))
print("Smallest : ",min(list1))

# Write a program to check whether an element exists in a tuple
t1=(10,20,30,40,50)
key=int(input("Enter the element to search : "))
found=False
for item in t1:
    if item==key:
        found=True
        break
if found:
    print("Element exits in tuple")
else:
    print("Element not exits in tuple")