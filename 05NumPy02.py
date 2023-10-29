import numpy as np
print("# Create a python list")
a = ["0", 1, "two", "3", 4]
print(a)

print("Print each element")
print("element 1 :",a[0])
print("element 2 :",a[1])
print("element 3 :",a[2])
print("element 4 :",a[3])
print("element 5 :",a[4])

#or
print("###############")
element =1 
for i in a:
    print(f"element {element} :",i)
    element += 1
print("###############")


print("# Create a numpy array")
List = [0, 1, 2, 3, 4]
data = np.array(List)
print(data)

print("###############")
element =1 
for i in data:
    print(f"element {element} :",i)
    element += 1
print("###############")

print("print the numpy version")
Np_Version = np.__version__
print(Np_Version)

print("print the data type of data")
print(data.dtype)

print("Check the type of the array and Value type for the given array b")
b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
Type = type(b)
print(f"the type of arrya b is :{Type}")

Value_Type = b.dtype
print(f"the value type or the data type of data is :{Value_Type}")

print("We can change the value of the array. Consider the array c")
c = np.array([20, 1, 2, 3, 4])
print(c)
print("change the data")
c[0] = 100
print(c)

print("Slicing")
d = c[1:4]
print(d)

print("# Set the 3rd element and 4th element to 300 and 400")
c[2:4] = 300, 400
print(c)

print("define the steps in slicing, like this: [start:end:step]")
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])
#If we don't pass start its considered 0
print(arr[:4])

#If we don't pass end it considers till the length of array
print(arr[4:])

#If we don't pass step its considered 1
print("step")
print(arr[1:5:])

print("Print the even elements in the given array.")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
for i in arr:
    if i%2 == 0:
        print("even elements are ",i)

#or for this array only
print(arr[1::2])
print("size")
print(arr.size)
print(arr.shape)
print("standard deviation")
standard_deviation=arr.std()
print(standard_deviation)

print("max")
Max = arr.max()
print(Max)

print("min")
min = arr.min()
print(min)    

print("how many dimension of array it is :",arr.ndim)


