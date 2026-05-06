#Practical 12 : Read CSV Files
import pandas as pd

#Creating data
data={
    "Name":["Alice","Bob","Charlie","david","Ellis","Frank"],
    "Age":[21,19,20,19,22,20],
    "Department":["Mech","IT","Electronics","CSE","Civil","Electrical"]
}

#converting to data frame
df = pd.DataFrame(data)
#saving to CSV file
df.to_csv("student.csv",index=False)
print("CSV file created and saved successfully")

#reading and displaying it on screen
df=pd.read_csv("student.csv")
print(df)
