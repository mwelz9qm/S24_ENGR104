# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 11:41:24 2024

@author: mwelz
"""
#this requires using the Sitka, AK weather data file which you can grab from Canvas
#use matplotlib to plot some data

from matplotlib import pyplot as plt
from datetime import datetime
import csv

filename = "sitka_weather_2018_simple.csv"

#lists for storing dates and temps
dates, highs, lows = [], [], []

#reading from the csv file

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    #extract the data
    for row in reader:
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        #this block handles if there missing dates
        try:
            low = int(row[6])   #adding int so it's read like a number not a string
            high = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

#plotting the data

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates,highs, c= 'orange', alpha = 0.5)
ax.plot(dates,lows, c= 'red', alpha = 0.5)

#formatting the plots

#fill between highs and lows
plt.fill_between(dates,highs, lows, facecolor = "purple", alpha = 0.2)
#titles and axis labels
plt.title("Daily Difference between highs and lows in Sitka, 2018", fontsize = 18)    
plt.xlabel("Dates", fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)

#tick marks
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)
plt.show()




