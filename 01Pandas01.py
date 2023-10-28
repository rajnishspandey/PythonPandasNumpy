"""A Series is a one-dimensional labeled array in Pandas. It can be thought of as a single column of data with labels or indices for each element. You can create a Series from various data sources, such as lists, NumPy arrays, or dictionaries"""
import pandas as pd

Data = [10, 20, 30, 40, 50]
s = pd.Series(Data)
print(s)

#accessing elements of series
#by lable
print("by lable :",s[2])
#by position
print("by position :",s.iloc[3])
#multiple elements
print("multiple elements\n")
print("All :\n",s[:]) #all
print("limited :\n",s[1:4])
print("range with skips :\n",s[0:4:2])

print("values :")
print(s.values)
print("value count :")
print(s.value_counts())
print("index :")
print(s.index.values)
print("size :")
print(s.size)
print("mean :")
print(s.mean())
print("unique :")
print(s.unique())
print("sorting :")
print(s.sort_values())
print("is null :")
print(s.isnull)

"""
values: Returns the Series data as a NumPy array.
index: Returns the index (labels) of the Series.
shape: Returns a tuple representing the dimensions of the Series.
size: Returns the number of elements in the Series.
mean(), sum(), min(), max(): Calculate summary statistics of the data.
unique(), nunique(): Get unique values or the number of unique values.
sort_values(), sort_index(): Sort the Series by values or index labels.
isnull(), notnull(): Check for missing (NaN) or non-missing values.
apply(): Apply a custom function to each element of the Series.
"""