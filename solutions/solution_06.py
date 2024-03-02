"""
Assignment #6 Solution
ENGR 104, Fundamental Of Engineering Computing
"""

import numpy as np

# ============================================================================
# Problem 16.1 (4 Points)
print('\n----- Problem 16.1 (4 Points) -----')
import myTripNiceIOMW

# Problem 16.2 (4 Points)
print('\n----- Problem 16.2 (4 Points)-----')
# Read Text File
dataPt1,time1,height1,error1 = np.loadtxt("mydata.txt",skiprows=5,unpack=True)
time2,height2 = np.loadtxt('mydata.txt',skiprows=5,usecols=(1,2),unpack=True)
# Read CSV File
dataPt3,time3,height3,error3 = np.loadtxt("mydata.csv",skiprows=5,unpack=True,delimiter=',')
# Write text file without header
np.savetxt('writeMyData.txt',list(zip(dataPt3,time3,height3,error3)),fmt='%12.1f')
# Write text file with header
info = 'Data for falling mass experiment'
info += '\nDate 31 July 2022'
info += '\nData taken by Matthew Klema'
info += '\n\n data point time (sec) height (mm) '
info += 'uncertainty (mm)'
np.savetxt('writeMyDataInfo.txt',list(zip(dataPt3,time3,height3,error3)),header=info,fmt='%12.1f')
# # Write to CSV File
np.savetxt('myDataOut.csv',list(zip(dataPt3,time3,height3,error3)),fmt='%0.1f',delimiter=',')

# ============================================================================
# Problem 17.1 (6 Points)
print('----- Problem 17.1 (6 Points) -----')

def sphere_volume():
    r = int(input('Please input the radius of your sphere [L]: '))
    vol = (4/3)*np.pi*r**3
    print('The volume of the sphere of radius %d [L] is %d [L^3].' %(r,vol))
    
SV = sphere_volume()

# Problem 17.2 (6 Points)
print('----- Problem 17.2 (6 Points) -----')
import csv
from datetime import datetime

from matplotlib import pyplot as plt

print('\nStudents should display the differnce between the high or low temperature at a location of their choosing and Sitka, AK for the same year. Results will differ but should result in similar plot for fukl credit. Plot should not display difference in results between high and low for Sitka, AK as this was the exercise completed in class!\n')

filename = 'sitka_data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, and high and low temperatures from this file.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

# Plot the Stika high temperature
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='orange', alpha=0.5)

filename = 'sitka_data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, and high and low temperatures from this file.
    dates, highsDF = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highsDF.append(high)
            
            
ax.plot(dates, highsDF, c='red', alpha=0.5)
plt.fill_between(dates, highs, highsDF, facecolor='purple', alpha=0.2)


# Format plot.
plt.title("Daily high difference Sitka, AK & Death Valley, CA - 2018", fontsize=18)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()


# # ============================================================================
# # Problem 18.1 (10 Points)
print('\n----- Problem 18.1 (4 Points) -----')
age = 38

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 30
else:
    price = 5
    
print(f'Your admission cost is ${price}!')

# # Problem 18.2 (3 Points)
print('\n----- Problem 18.2 (3 Points) -----')
def factorial1(n):
    if n == 1:
        return 1
    else:
        res = n * (factorial1(n-1))
        return res
    
res1 = factorial1(5)
print(res1)

# # Problem 18.3 (3 Points)
# print('\n----- Problem 12.3 (3 Points) -----')
import if_elif_elseExampleMW





