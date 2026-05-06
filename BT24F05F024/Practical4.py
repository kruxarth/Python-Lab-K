#Practical 4 : Operators in python

#1.Aritmetic
a=10
b=2
print("a+b:",a+b)
print("a-b:",a-b)
print("a*b:",a*b)
print("a/b:",a/b)
print("a//b:",a//b)
print("a%b:",a%b)
print("a**b:",a**b)
print("")
#2. Comparison
print("a==b",a==b)
print("a!=b",a!=b)
print("a<=b",a<=b)
print("a>=b",a>=b)
print("a>b",a>b)
print("a<b",a<b)
print("")
#3.Assignment
c=5
print("c=5",c)
print("c+=5",c+5)
print("c-=5",c-5)
#4.Logical
print("a>5 and b<5",(a>5 and b<5))
print("a>5 or b>5",(a<5 or b<5))
print("not(a==b)",not(a==b))
print("")
#5.Bitwise
print("a&b:",a&b," a|b:",a|b," a^b:",a^b,"\n","~a:",~a," a<<1:",a<<1," a>>1:",a>>1)
print("")
#6. Identity
list1=[1,2,3]
list2=[1,2,3]
list3=list1
print("list1 is list2:",(list1 is list2))
print("list1 is list3:",(list1 is list3))
print("list1 is not list3:",(list1 is not list3))