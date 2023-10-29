import numpy as np

u = np.array([1, 0])
print(u)

v = np.array([0, 1])
print(v)
print("Addition of array")
z = u+v
print(z)

#or
print("or Addition of array")
z = np.add(u,v)
print(z)

a = np.array([10, 20, 30])
print(a)

b = np.array([5, 10, 15])
print(b)

print("subtraction")
c = np.subtract(a,b)
print(c)

i = np.array([1, 2])
print(i)

j = np.array([2, 1])
print(j)

print("Multiplication")
k = np.multiply(i,j)

print(k)

d = np.array([10, 20, 30])
print(d)

e = np.array([2, 10, 5])
print(e)

print("divion")
f = np.divide(d,e)
print(f)

#Dot() - The dot product of the two numpy arrays u and v is given by
X = np.array([1, 2])
Y = np.array([3, 2])

print(np.dot(X,Y)) #1*3+2*2 = 3+4 = 7

print("adding constant")
e = e+1
print(e)

print("####### add constant 5")
arr = np.array([1, 2, 3, -1]) 
print(arr+5)

print("mathematical functions")
pi = np.pi
print(pi)