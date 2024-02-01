# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:27:44 2024
stuff we did in class on 1/31
@author: mwelz
"""

#in-class problem 
#====================================

print("\n -------In-class Problem-------")

distance = 400    #miles
mpg = 30     #gas mileage
speed = 60    #avg speed
costPerGallon = 2.85     #gas price

time = distance/speed   #time(hrs)
gallons = distance/mpg 
cost = gallons * costPerGallon

print(f"The trip took {round(time,2)} hours.")
print(f"The trip used {round(gallons,2)} gallons.")
print(f"The trip cost ${round(cost,2)}.")

#importing modules
print("\n-------Using numpy-------")
import numpy as np

a = np.sin(2)
print(f"The sine of 2 is {a}.")
print(f"The square root of 7 is {np.sqrt(7)}.")

x1, y1 = 1.4, -2   #first point
x2, y2 = -3, 2.5   #second point

dist = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"The distance between the points is {round(dist,2)}.")








