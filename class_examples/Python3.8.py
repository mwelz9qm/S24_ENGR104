# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 11:16:16 2024

@author: mwelz
"""

import numpy as np
import matplotlib.pyplot as plt

#x's and y's for our first plot

x = range(1,6)
y = [5,2,1,4,3]

#our first figure

plt.figure(1)

#overlay a line plot on top of a scatter plot

plt.scatter(x,y)
plt.plot(x,y)


plt.figure(2)

#overlay a line plot on top of a scatter plot
#introducing color, markers, size
plt.scatter(x,y, marker = '*', color = 'green', s = 500)
plt.plot(x,y, linewidth = 2, color = 'black')

plt.figure(3)

#figure 3 will be plotting cosine from 0 to 4pi
x = np.linspace(0, 4 * np.pi, 100) #breaks domain into 100 slices
y = np.cos(x)

plt.scatter(x,y, marker = '+', color = 'orange', s = 100)
plt.plot(x,y, linewidth = 2, color = 'm')
plt.xlabel('x (radians)', fontsize = 13)
plt.ylabel('y(x)', fontsize = 13)
plt.legend(['$ y = cos(x)$'])
plt.title('Plot of cosine')

#multiple plots in a figure
#treat individual plots and figures as their own objects

# setting up a figure that will have two plots ax1, ax2


# figure will have 2 rows, 1 plot in each row
#sharex indicates some x-values will be used
fig, (ax1, ax2) = plt.subplots(2,1, sharex = True)


#let's plot some exponential functions
x = np.linspace(-10, 10, 30)
y1  = np.exp(x/10) + 2
y2 = np.exp(-x/10) + 4


#when using this fig, ax approach we have to use "set"
# to set label, and title but not legend

#setup ax1
#ax1.scatter(x,y1, marker = '*', color = 'g', s = 50)
ax1.plot(x,y1, linewidth = 2, color = 'k')
ax1.set_ylabel('y = f(x)')
ax1.set_title('Plot 1')
ax1.legend(['$f(x) = e^{x/10} + 2$']) #between the $ $ is a LaTeX environment
#setup ax2

ax2.scatter(x,y2, marker = '*', color = 'm', s = 50)
ax2.plot(x,y2, linewidth = 2, color = 'orange')
ax2.set_xlabel('x values')
ax2.set_ylabel('y = g(x)')
ax2.set_title('Plot 2')
ax2.legend(['$g(x) = e^{-x/10} + 4$'])

#we're going to replace ax1.scatter with an errorbar plot
ax1.errorbar(x,y1,
             yerr =1,#error bar height
             elinewidth = 0.5, #error lines width
             ecolor = 'red',#color of error bars
             capsize = 4,#error bar cap size
             capthick = 1,#error bar cap thickness
             marker = '*',#marker for data
             color = 'g')#color for data

plt.savefig('myFig.pdf', dpi = 300) #save figure

plt.show()




