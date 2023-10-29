import matplotlib.pyplot as plt
import numpy as np

print("We can create the following numpy array in Radians")
x = np.array([0, np.pi/2 , np.pi])
print(x)

x = np.sin(x)
print(x)

"""
#Linspace :
A useful function for plotting mathematical functions is linspace. 
Linspace returns evenly spaced numbers over a specified interval

numpy.linspace(start, stop, num = int value)

start : start of interval range

stop : end of interval range

num : Number of samples to generate.
"""

# Makeup a numpy array within [-2, 2] and 5 elements
print("for 5 element")
element = np.linspace(-2, 2, num=5)
print(element)

# Make a numpy array within [-2, 2] and 9 elements
print("for 9 element")
element  = np.linspace(-2, 2, num=9)
print(element)

print("# Make a numpy array within [0, 2π] and 100 elements" )
x = np.linspace(0, 2*np.pi, num=100)
print(x)

print("# Calculate the sine of x list")
y = np.sin(x)
print(y)

plt.figure("Testing")
plt.plot(x,y)
plt.show()