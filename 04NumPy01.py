"""
NumPy is a Python library used for working with arrays, linear algebra, fourier transform, and matrices.
A numpy array is similar to a list. NumPy stands for Numerical Python and it is an open source project.The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

Arrays are very frequently used in data science, where speed and resources are very important.

NumPy is usually imported under the np alias.

It's usually fixed in size and each element is of the same type. 
We can cast a list to a numpy array by first importing numpy:
"""

import numpy as np

a = [1,2,3,4,5]
print(a)
x = np.array(a)
print(x)

print("#find the type of array")
Type = type(x)
print(Type)

print("Find the shape of the array")
Shape = np.shape(x)
print(Shape)

print("Find the type of data in the array")
Data_type = x.dtype
print(Data_type)

print("find the mean of the array")
Mean = x.mean()
print(Mean)