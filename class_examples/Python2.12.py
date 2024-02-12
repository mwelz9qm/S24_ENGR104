# -*- coding: utf-8 -*-
"""
Python Notes
2/12/2-4

"""
import numpy as np

#reminder of how to build an array
listA = np.array([-4,5,6,7])

#fill a 3x4 matrix with 1's
a = np.ones((3,4),dtype = int)
print(a)

#example of the reshape method

b = np.arange(8)
b = np.reshape(b,(2,4))
print(b)

A = np.array([[1,-2,9,13],[-5,1,6,-7],[4,8,-4,-2],[8,5,-7,1]])
b = np.array([1,-3,-2,5])

#pull in scipy to solve systems of equations

import scipy

#alternatively import scipy.linalg as slin
# solving a couple systems


print(scipy.linalg.solve(A,b))

A = np.array([[11,-3,0],[-3,6,-1],[0,-1,3]])
b = [30,5,-25]

print(scipy.linalg.solve(A,b))