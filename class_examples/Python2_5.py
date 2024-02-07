# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 11:13:50 2024
ENGR 104

2.5.2024

"""

a = list(range(8))
print(a)

#testing out the ways to add elements and remove them from a list

listA = list(range(1,11))
listA.append(99)
listA.insert(3,-99)
del listA[5]
listA.pop(7)
listA.remove(-99)

#sorting and reversing a list
listB = [10, -7, 12, 4, 18]
listB.sort()
listC = ["dog", "cat", "elephant"]
listC.sort()
listC.reverse()

# looking at slices of lists

print(listB[1:4])
print(listB[2:5])
print(listB[1:])  #moves from 1 to end
print(listB[:3]) #starts from beginning
print(listB[:]) #whole list

listD = list(range(1,17))

print(listD[0::2]) #runs through whole list with step size 2
print(listD[2::3]) #start at index 2 with step size 3





