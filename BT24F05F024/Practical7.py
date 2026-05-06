#Practical 7 : Working with built-in functions
#input and output
name=input("Enter your name:")
print("Hello "+name)

#Math related
print("-----------------------------------------------------------")
a=-5
b=10
c=2
d=2.456789
print("absolute value of a:",abs(a))
print("maximum between a,b,c:",max(a,b,c))
print("minimum between a,b,c:",min(a,b,c))
print("sum of [a,b,c]:",sum([a,b,c]))
print("d round of to two place:",round(d,2))
print("c^5",pow(c,5))

#type conversion
print("-----------------------------------------------------------")
print("Integer d:",int(d))
print("Float b:",float(b))
print("String c:",str(c))

#length,type,sort
print("-----------------------------------------------------------")
list=[1,2,3,6,9,5,7,8,4]
print("Original list:",list)
print("Length of list:",len(list))
print("Type:",type(list))
print("Sorted list:",sorted(list))


