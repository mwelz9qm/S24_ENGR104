# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:14:25 2024

@author: mwelz
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('sensor_data.csv')
#df = pd.read_csv('sensor_data.csv', skiprows = 5) <- skip the first five rows
print(df)
print(df.info())

#isolate an individual column
#print(df['Temperature_C'])

#or alternatively

#print(df.Temperature_C)

#change the header names

# df = pd.read_csv('sensor_data.csv', skiprows =1,
#                  names = ['A', 'B', 'C','D','E','F'] )

# print (df.head())

#referring to an individual 'cell'
#the reference is "backwards" since we refer to column and then row
print(f"The value in the 4th row of the Humidity col is {df['Humidity'][4]}")

# returns all elements in the dataframe with humidity >45 
print(df[df['Humidity']>45])

#let's plot temperature vs humidity

fig, ax = plt.subplots()

ax.scatter(df['Temperature_C'], df['Humidity'], marker = '*', color = 'm')
ax.set_xlabel('Temperature(C)')
ax.set_ylabel('Humidty(%)')
ax.set_title('Temperature vs Humidity')

#create a figure with two plots that plot Temp vs Humidity
#for LocationA and LocationB separately

dfA = df[df['Location'] == "Location_A"] #Location_A frame
dfB = df[df['Location'] == "Location_B"] #Location_B frame

fig, ax = plt.subplots(2,1, sharex = True, sharey = True)

ax[0].scatter(dfA['Temperature_C'], dfA['Humidity'], marker = '*', color = 'm')
ax[0].set_xlabel('Temperature(C)')
ax[0].set_ylabel('Humidty(%)')
ax[0].set_title('Location A')

ax[1].scatter(dfB['Temperature_C'], dfB['Humidity'], marker = '*', color = 'g')
ax[1].set_xlabel('Temperature(C)')
ax[1].set_ylabel('Humidty(%)')
ax[1].set_title('Location B')

fig.tight_layout() #this prevents weird overlap from axes

#other read-ins
#from text file seperate by unknown amount of space

sd = pd.read_table('states_data.txt', sep = '\s+' )
#alternative
#sd = pd.read_table('states_data.txt', delim_whitespace = True )
print(sd.info())
print(sd.head())
#print data for all states with population of at least 5000000
print(sd[sd['Population'] > 5000000])
