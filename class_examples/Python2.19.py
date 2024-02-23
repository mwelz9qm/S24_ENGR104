# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 11:15:31 2024

@author: mwelz
"""


#function to calculate area of a rectangle

def calculate_area(length, width):
    area = length * width
    return area

#setting a variable equal to the output pf the function
myArea = calculate_area(10,8)

print(f"The result of running the function with 10 and 8 is {myArea}. ")

#passing variables into our function instead of just values

l = 12
w = 30
myNewArea = calculate_area(l,w)

#function to concatenate two strings

def concatenate_strings(string1, string2):
    result = string1 + " " + string2
    return result


s1 = "Hello"
s2 = "World"

print(concatenate_strings(s1,s2))


#function that takes an array of degrees and returns sine values
import numpy as np


def find_sines(angles):
    angles_rad = np.radians(angles) #convert to radians
    sines = np.sin(angles_rad) #find sine values
    sines = np.round(sines,2)  # round to two places
    return sines

#check that it works
a = np.arange(0,361,10)  #array of 0, 10, 20, ..., 360
print(find_sines(a))

    
#a function that returns two values

def rectangle_info(length, width):
    area = length * width
    perimeter = 2 * length + 2 * width
    return area, perimeter
    
a, p = rectangle_info(5,11) #set two variables because function returns two outputs

print(f"The area of my rectangle is {a} and the perimeter is {p}.")

#a function that takes no arguments and returns nothing

def nada():
    print("Just printing this out and nothing else!")

nada()

    
def f(a,b):
    result = a**2 + b**2
    return result

g = lambda a,b:a ** 2 + b ** 2

print(f(3,4),g(3,4))


