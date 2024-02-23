# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 11:15:11 2024
Class 2/21/2024
@author: mwelz
"""

#function reminder

def double_num(x):
    return 2*x

print(double_num(16))


#example using default parameters -- these go at the end

def distance(x1,y1,x2 = 0, y2 = 0 ): 
    """
    a function that take two points and finds the distance between them
    if only one point is given, the distance between the point and origin is returned
    """
    d = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    return d



print(distance(1,2,4,6))
print(distance(5,12))

import numpy as np

#experimenting with how variables do or don't change based on what happens
# to them in a function

def scope_test(s,n,t,l,a,d):
    s = "changed?"
    n = 17
    t = (11.4, 8.6)
    l[0] = "Wednesday"
    a[-1] = 999.99
    d["cat"] = 117
    return s, n, t, l, a

#set s1, n1, t1, l1, a1

s1 = "Python Class"
n1 = np.pi
t1 = (5,6,7)
l1 = [5,12,3,10]
a1 = np.arange(1,15,2)
d1 = {"first_name":"matt", "last_name":"welz"}

scope_test(s1,n1,t1,l1,a1,d1)

print(s1, n1, t1, l1, a1,d1)


#thinking of lists, arrays, dictionaries, as "objects"
#objects have attributes (like data) and methods (functions that act) on the data


a = np.array([12,10,27,8, 47])

print(a.size)
print(a.sum())
a.sort()
a = a.clip(15, 30)
print(a)

