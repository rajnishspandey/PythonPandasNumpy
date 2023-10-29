#two dimensional array
import numpy as np
import matplotlib.pyplot as plt

A=np.array([[11,12],[21,22]])
B=np.array([[1, 0],[0,1]])

print("multiply")
C = np.multiply(A,B)
print(C)

print("Perform matrix multiplication on array A and B (order will not matter in this case).")
C = np.dot(A,B)
print(C)

print("# Create a list")
a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
print(a)

print("# Convert list to Numpy Array")
# Every element is the same type
A = np.array(a)
print(A)

print("dimensions")
print(A.ndim)

print("Shape")
print(A.shape)

print("size")
print(A.size)

print("# Access the element on the second row and third column")
print(A[1,2])

print("# Access the element on the first row and first column")
print(A[0][0])

print("# Access the element on the first row and first and second columns")
print(A[0][0:2])

print("# Access the element on the first and second rows and third column")
print(A[0:2, 2])

print("new array")
X = np.array([[1, 0], [0, 1]]) 
print(X)

print("# Create a numpy array Y")
Y = np.array([[2, 1], [1, 2]]) 
print(Y)

Z = X+Y
print(Z)

#or
Z = np.add(X,Y)
print(Z)

#similarly we can perform,  subtract, multiply, division, dot(matrix multiplication), sin etc.

print("# Create a matrix C")
C = np.array([[1,1],[2,2],[3,3]])
print(C)
print("Transpose of matric c is :\n", C.T)