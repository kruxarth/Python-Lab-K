# for writing
f=open("student.txt","w")
f.write("Name: shamal\n")
f.write("Branch : CSE\n")
f.close()

# # for reading
f=open("student.txt","r")
data=f.read()
print(data)
f.close()

#append the content
f=open("student.txt","a")
f.write("Collge : GECA")
f.close()

# read line by line
f=open("student.txt","r")
for line in f:
    print(line)
f.close()

#using with
with open("student.txt","r") as f:
    print(f.read())