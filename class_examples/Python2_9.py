# -*- coding: utf-8 -*-
"""
class exmaples 2/9/2024

@author: mwelz
"""

import numpy as np  #import numpy

a = np.array([4,7,8,12.,-9])   #manually creating a numpy array
print(a)

b = np.linspace(0,30,5)   #linspace evenly spaces out numbers from start to stop
print(b)

c = np.arange(0,15,3) #arange runs from start to stop (exclusive) with given step size
print(c)

d = np.ones(6, dtype = int) #fills array with ones, dtype = int makes them ints instead of floats

print(d)

e = np.zeros(10, dtype = int) #same as above but with zeros
print(e)


# doing math on an array element by element
a = np.array([-4,10,3,8,17])
print(a + 3)
print(a ** 2)
print((a-3)*2)

print(np.sin(a))
angles = np.arange(0,91,5) #build an array of angles from 0 to 90, with steps of 5 degrees
sines = np.sin(np.radians(angles)) #convert angles to radians and plug into sign


sixes = 6 * np.ones(10, dtype = int)

a = np.array([4.2,3,-6,1])
b = np.array([8,-12,7,4])

#doing math across arrays

AplusB = a+b
AminusB = a - b
AdivideB = a/b
AtimesB = a * b






