# -*- coding: utf-8 -*-
"""
ENGR 104
Class 2/2/2024
Lists
Created on Fri Feb  2 11:19:41 2024


"""

#playing around with lists

myList = [3,4,4,5,4]
a = [7.2, "Cat", 3, "X", "786"]
a[1] = "Cow"
a[2] = a[2] ** 2
print(a)
c = "I can code in Pyton"
d = "C++"
print(c + " and " + d)

#adding strings

first = "Matt"
last = "Welz"
fullName = first + " " + last
print(fullName)

#adding lists

a = [0,5,-3,7]
b = [4, "taco", 120]
print(a+b)
print(b+a)

aa = [4, 7, [3,9,8],6,7]
print(aa[2][2])

#using the range function for generating sequences



aa = list(range(8))  #begins at default 0, steps by 1 as default
print(aa)

bb = list(range(4,9)) #begins at 4, steps by 1 as default

print(bb)

cc = list(range(0,15,3)) #begins at 0, runs up to 15 non-inclusive, steps by 3
print(cc)

dd = list(range(-7, 10, 2)) #begins at -7. steps by 2

print(dd)

ee = list(range(16, 0, -5)) #begins at 16, runs to 0, steps DOWN by 5

print(ee)











