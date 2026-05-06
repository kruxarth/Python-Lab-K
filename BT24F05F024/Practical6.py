#Practical 6 : Loops,break,continue statements

#for loop
print("Multiplication Table of 5 by for loop:")
for i in range(1,11):
    print(5,"*",i,"=",5*i)

#while loop
print("\n1-10 Squares by while loop:")
j=1
while j<=10:
    print(j**2)
    j+=1
#nested loops
print("\nHalf Star triangle Pattern by nested loops:")
for i in range(1,5):
    for j in range(i):
        print("*",end=" ")
    print( )
#break,continue
print("\nPrinting only odd number between 1 and 20 and breaking it at 15:")
for i in range(1,20):
    if i%2==0:
        continue
    if i==15:
        break
    print(i)