####################################
#          What is Numpy
####################################
import time
import sys
import numpy as np
import matplotlib.pyplot as plt

# create a numpy array
a = np.array([0, 1, 2, 3, 4])
print(a)

# checking numpy version
print(np.__version__)

# check the type of the array
type(a)

# check the type of the values stored in numpy array
print(a.dtype)

# create numpy array
c = np.array([20, 1, 2, 3, 4])
print(c)

# assign the first element to 100
c[0] = 100
print(c)

# assign the 5th element to 0
c[4] = 0
print(c)

# slicing the numpy array
d = c[1:4]
print(d)

# set the fourth element and fifth element to 300 and 400
c[3:5] = 300, 400
print(c)

# we can also define the steps in slicing, like this: [start:end:step]
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])
print(arr[:4])
print(arr[4:])
print(arr[1:5:])

# create the index list
select = [0, 2, 3, 4]
print(select)

# use list to select elements
d = c[select]
print(d)

# get the size of numpy array
print(f"Array a: {a}")
print(a.size)

# get the number of dimensions of numpy array
print(a.ndim)

# get the shape/size of numpy array
print(a.shape)

##############################
# Numpy Statistical Functions
##############################
a = np.array([1, -1, 1, -1])

# get the mean of numpy array
mean = a.mean()
print(mean)

# get the standart deviation of numpy array
standart_deviaton = a.std()
print(standart_deviaton)

# max and min value of an array
b = np.array([-1, 2, 3, 4, 5])
print(b)
print(f"biggest value of b: {b.max()}")
print(f"smallest value of b: {b.min()}")

# numpy array operations
u = np.array([1, 0])
print(u)

v = np.array([0, 1])
print(v)

z = np.add(u, v)
print(z)

t = np.subtract(u, v)
print(t)

# array multiplication
arr1 = np.array([1, 2])
arr2 = np.array([2, 1])

arr3 = np.multiply(arr1, arr2)
print(arr3)

# array division
arr4 = np.divide(arr1, arr2)
print(arr4)

# dot product (X[0]*Y[0] + X[1]*Y[1])
X = np.array([1, 2])
Y = np.array([3, 2])
print(np.dot(X, Y))

# adding constant to array (adds each element of array)
U = np.array([1, 2, 3, -1])
print(U + 1)

# mathematical functions
# x = np.array([0, np.pi/2, np.pi])
# y = np.sin(x)
# print(y)

# linspace numpy.linspace(start, stop, num = int value)
np.linspace(-2, 2, num=5)
x = np.linspace(0, 2*np.pi, num=100)
y = np.sin(x)
plt.plot(x, y)
# plt.show()

# iterating 1-D arrays
arr5 = np.array([1, 2, 3])
print(arr5)

for item in arr5:
    print(item)
