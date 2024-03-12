# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 11:14:51 2024

@author: mwelz
"""

import numpy as np
import matplotlib.pyplot as plt

#set up a figure for 2 x 2 plots
fig, ax = plt.subplots(2,2, sharex= True)

x = np.linspace(-5,5,30)
y1 = np.arctan(x)

#upper left plot
ax[0,0].plot(x,y1, color = 'magenta', linewidth = 2, linestyle = 'dashed')
ax[0,0].set_ylabel(r'$f(x) = \arctan(x)$')
ax[0,0].set_title('Plot 1')
#upper right plot
ax[0,1].scatter(x,y1, color = 'black', marker = '*')
ax[0,1].set_ylabel(r'$f(x) = \arctan(x)$')
ax[0,1].set_title('Plot 2')

#lower left
y2 = np.exp(-x**2)
ax[1,0].plot(x,y1, color = 'red', linewidth = 2, linestyle = 'dotted')
ax[1,0].set_ylabel(r'$g(x) = e^{-x^2}$')
ax[1,0].set_title('Plot 3')
#lower right plot
ax[1,1].scatter(x,y1, color = 'green', marker = '+')
ax[1,1].set_ylabel(r'$g(x) = e^{-x^2}$')
ax[1,1].set_title('Plot 4')
fig.tight_layout()  #helps prevent objects from overlapping


#simulate a bunch of die rolls and make a histogram

size = 100
rolls = np.ceil(np.random.rand(size)*6)

fig, ax = plt.subplots()

ax.hist(rolls, color = 'g', edgecolor = 'black',
        bins = [0.5,1.5,2.5,3.5,4.5,5.5, 6.5])

ax.set_xlabel('Die Value')
ax.set_ylabel('Frequency')
ax.set_title(f'Distribution of {size} Rolls')

#a polar coordinate plot

r = np.linspace(0,10,5000)
theta = np.cos(r**2)

fig, ax = plt.subplots(subplot_kw = {'projection':'polar'})

ax.plot(theta,r)

#3-D surface plot

#inputs
from matplotlib import cm
x = np.linspace(-2,2,50)
y = np.linspace(-2,2,50)

X, Y = np.meshgrid(x,y)  #makes a grid of X and Y values

Z = np.exp(-(X**2 + Y**2)) #function of X and Y

fig, ax = plt.subplots(subplot_kw = {'projection':'3d'})
ax.plot_surface(X,Y,Z,
                cmap = cm.twilight, #color map
                alpha = 0.8,
                linewidth = 0.25,
                cstride = 1,
                rstride = 1) 


