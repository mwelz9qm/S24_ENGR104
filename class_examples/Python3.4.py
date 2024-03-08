# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 11:14:04 2024

@author: mwelz
"""
#iterate through a list of numbers

mySum = 0
for i in range(1,2001):
    mySum = mySum + i**2

print(mySum)

#iterate through a list of friends

friends = ["Jess", "Rafa", "Simon", "Shelly", "Louise"]

for friend in friends:
    print(f"{friend} is my friend.")

name = "Quentin"


#iterate through a list of characters

track = 0
for letter in name:
    print(f"{letter} is letter {track} in the name")
    track += 1

print("------------------------------")

#loop through letters in a name and keep track of passes through the loop

for counter,letter in enumerate(name):
    print(f"{letter} is letter {counter} in the name")
    
print("------------------------------")

#loop through a dictionary
#print out dictionary keys
D = {"Colorado": 8, "New Mexico": 5, "Utah": 13, "Arizona":6}

for state in D.keys():
    print(state)

print("------------------------------")

   #print out dictionary values

for rank in D.values():
    print(rank)
print("------------------------------")

#print out Fibonacci numbers up to the 100th

back2 = 1
curr =1
for i in range(3,101):
    temp = curr
    curr += back2
    back2 = temp

print(curr)
print("------------------------------")
listA = range(1,201)
listB = []

#put the first 200 squares in a list using a loop

for num in listA:
    listB.append(num**2)

print(listB)
#put the first 200 squares in a list using list comprehension

listB = [num**2 for num in listA]
print(listB)
#list comperehension for putting the first 200 squares
#that are divisble by 4 into a list
listC = [num**2 for num in listA if num % 4 == 0]
print(listC)
