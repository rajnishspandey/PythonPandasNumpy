"""A DataFrame is a two-dimensional labeled data structure with columns of potentially different data types. """

import pandas as pd

# Creating a DataFrame from a dictionary
data  = {"Name": ['Alice', 'Bob', 'Charlie', 'David'],
         'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
         }

df = pd.DataFrame(data)
print(df)

#custom selection
print("custom selection\n")
print(df["Name"])

#accessing rows
print("accessing rows\n")
print("####Access the third row by position\n",df.iloc[2])
print("####Access the third row by label\n",df.loc[2])

#slicing
print("slicing :\n")
print("# Select specific columns \n",df[["Name", "Age", "City"]])
print("# Select specific rows \n",df[1:3])

#finding unique elements
print("#finding unique elements")
print(df["Age"].unique())

#conditional filtering
print("#conditional filtering")
print(df[df["Age"]>25]) #it gives the output of the records having age greater than 25
print(df["Age"]>25) #check if it grater than 25 or not returns True or False\

#saving dataframe 
print("#saving dataframe ")
saveDf = df.to_csv("savingTest.csv", index=False)
print("reading the saved csv")
dfcsv = pd.read_csv("savingTest.csv")
print(dfcsv)


print("shape : \n",df.shape)
print("info :\n",df.info())
print("describe :\n",df.describe())
print("head :\n",df.head()) #default is 5 top rows
print("tail :\n",df.tail())#bottom 5 rows
print("sort_values :\n",df.sort_values(by="Age", ascending=False))
print("groupby :\n")
groupdata = df.groupby('Age',as_index=False)
for age, group in groupdata:
    print(f"Age: {age}")
    print(group)
    print("\n")
print("fillna :\n")
print(df.fillna(0))
print("after Drop :\n")
df.drop("City",axis=1,inplace=True) #drops the column
print(df)

print("rename :\n")
print("before rename \n",df)
df.columns = ["Name","Ages"]
print("After renameing \n")
"""
shape: Returns the dimensions (number of rows and columns) of the DataFrame.
info(): Provides a summary of the DataFrame, including data types and non-null counts.
describe(): Generates summary statistics for numerical columns.
head(), tail(): Displays the first or last n rows of the DataFrame.
mean(), sum(), min(), max(): Calculate summary statistics for columns.
sort_values(): Sort the DataFrame by one or more columns.
groupby(): Group data based on specific columns for aggregation.
fillna(), drop(), rename(): Handle missing values, drop columns, or rename columns.
apply(): Apply a function to each element, row, or column of the DataFrame.
"""