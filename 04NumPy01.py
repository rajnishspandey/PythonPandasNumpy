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