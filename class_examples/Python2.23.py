# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 11:21:28 2024

@author: mwelz
"""

#requires the input_data.txt and input_data.csv files in the repo to be in the same directory


#inputing from the keyboard -- data is read as string
name = input("What's your name: ")
print(name)


#since string is read naturally, we convert it to an integer so we can do math on it
fav_num = int(input("What's your favorite number: "))
#fav_num = int(fav_num)
print(fav_num)


#formatting with str.format()  {argumentnumber:minspaceused.placesrightofdecimal fixed or scientific}
num1 = 4.23
num2 = 9.78645
print("\nMy most Favorite number is {0:0.3f} and my second favorite number is {1:0.3f}".format(num1,num2))

import numpy as np

#reading in from a text file


exp_id, temp, pressure, reaction = np.loadtxt("input_data.txt", skiprows=6,unpack=True)

print(exp_id, temp, pressure, reaction)


#add usecols just to pick a couple columns from the data set

temp, reaction = np.loadtxt("input_data.txt",usecols=(1,3), skiprows=6,unpack=True)
print(temp,reaction)

#to open a csv
#reading in from a csv, just adding the delimiter parameter and change file extension to csv


temp, reaction = np.loadtxt("input_data.csv",usecols=(1,3), skiprows=6,unpack=True, delimiter = ",")

#writing out to a text file

np.savetxt("output_data.txt", list(zip(temp,reaction)), fmt = "%12.1f")


#add a header file to what we're writing out


info = "Pretend Experiment"
info += "\nData Collected by Matt"
info += "\nDate: 2.26.2024"
info += "\nTemperature \t Reaction"

#add the header parameter and write out


np.savetxt("output_data.txt", list(zip(temp,reaction)),header = info, fmt = "%12.1f")

#to write out to a csv, just add the delimier paramter and change file output to csv

np.savetxt("output_data.csv", list(zip(temp,reaction)),header = info, fmt = "%12.1f", delimiter = ",")