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
y = df[["ID"]]
print(type(y))

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
z = df["Country"]
print(z)
print(type(z))

"""
loc() is a label-based data selecting method which means that we have to pass the name of the row or column that we want to select. 
This method includes the last element of the range passed in it.

iloc() is an indexed-based selecting method which means that we have to pass integer index in the method to select a specific row/column. 
This method does not include the last element of the range passed in it.
"""

print("# Access the value on the first row and the first column\n")
a = df.iloc[0,0]
print(a)

print("# Access the value on the first row and the third column\n")
a = df.iloc[0,2]
print(a)

print("# Access the column using the name\n")
print(df.loc[0:2,["Course","Country"]])
"""
Let us create a new dataframe called 'df1' and assign 'df' to it. 
Now, let us set the "Name" column as an index column using the method set_index().
"""
print("####################\n")
df1 = pd.DataFrame(x)
print(df1)

print("set ID column as index\n")
df1 = df1.set_index("ID")
print(df1)