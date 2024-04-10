#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:46:06 2024

@author: mwelz
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

def f(x,y):
    return np.sin(x) + np.cos(y)

x = np.linspace(0, 2 * np.pi, 120)
y = np.linspace(0, 2 * np.pi, 120).reshape(-1,1)

fig, ax = plt.subplots(figsize = (3.5, 3.5))
fig.subplots_adjust(bottom = 0, top = 1, left = 0, right = 1)
ax.axis("off")

ims = []

for i in range(120):
      x+= np.pi/20.
      y += np.pi/20.
      im = ax.imshow(f(x,y), cmap = plt.get_cmap('plasma'), animated = True)
      ims.append([im])

ani = anim.ArtistAnimation(fig, artists = ims,interval =10, repeat_delay = 0)

plt.show()


# import matplotlib
# #matplotlib.use('TkAgg')  # Set an appropriate backend

# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as anim

# def f(x, y):
#     return np.sin(x) + np.cos(y)

# # Initial setup
# x = np.linspace(0, 2 * np.pi, 120)
# y = np.linspace(0, 2 * np.pi, 120).reshape(-1, 1)

# fig, ax = plt.subplots(figsize=(3.5, 3.5))
# fig.subplots_adjust(bottom=0, top=1, left=0, right=1)
# ax.axis("off")

# ims = []
# for i in range(120):
#     x += np.pi/20.
#     y += np.pi/20.
#     im = ax.imshow(f(x, y), cmap='plasma', animated=True)
#     ims.append([im])

# ani = anim.ArtistAnimation(fig, ims, interval=10, repeat_delay=0)

# plt.show()  # Use plt.show() to ensure the GUI event loop is entered
