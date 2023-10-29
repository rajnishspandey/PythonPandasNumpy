#import pandas
import pandas as pd

#defining dataframe
x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting dictionary to a dataframe
df = pd.DataFrame(x)

#print DataFrame
print(df)

#retrieve the columns ID
print("#retrieve the columns ID\n")
print(df["ID"])

print("find the type of the column\n")
x = df[["ID"]]
print(type(x))

print("#accessing multiple columns\n")
col = df[["ID","Department","Salary"]]
print(col)

print("#create new dataframe \n")
data = {"Student":["David","Samuel","Terry","Evan"],
       "Age":[72,24,22,32],
        "Country":["UK","Canada","China","USA"],
        "Course":["Python","Data Structures","Machine LEarning","Web Development"],
        "Marks":[85,72,89,76]
       }
print(data)

df = pd.DataFrame(data)
print(df)

print("Retrieve the Marks column and assign it to a variable b\n")

b = df[["Marks"]]
print(b)

print(": Retrieve the Country and Course columns and assign it to a variable c\n")
c = df[["Country","Course"]]
print(c)

print("To view the column as a series, just use one bracket\n")
x = df["Name"]
print(x)