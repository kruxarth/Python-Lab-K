#Practical 9 : Strings,List,Tuple,Set
#STRING
word="India"
print("String:",word)
print("Length of String:",len(word))
print("Uppercase:",word.upper())
print("Lowercase:",word.lower())
print("First letter:",word[0])
print("Last letter:",word[len(word)-1])
print(f'Hello {word}')
print("")

#LIST
nums=[1,2,3,4,5]
print("List:",nums)
print("List length:",len(nums))
nums.append(2)
print("List after append:",nums)
nums.remove(3)
print("List after remove:",nums)
sorted(nums)
print("List after sort:",nums)
print("")

#TUPLE
tup=(1,2,3,4,5)
print("Tuple:",tup)
print("Tuple length:",len(tup))
print("Last element:",tup[len(tup)-1])
print("")

#SET
val={10,20,30,40,50}
print("Set:",val)
print("Set length:",len(val))
val.add(70)
print("Set after add:",val)