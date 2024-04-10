
import numpy as np
import matplotlib.pyplot as plt

'''
This function animates projectile motion using matplotlib tools
'''

# Initial conditions/values
v_0 = 5 #initial velocity (m/s)
theta0 = 80 # initial angle (degrees)
g = 9.81 # gravitational acceleration(m/s^2)

theta0_rad = theta0 * np.pi/180 # initial angle converted to radians (rad)
T = 2*v_0*np.sin(theta0_rad)/g #time when the projectile hits the ground

t = np.arange(51)/50*T # chopping up from 0 to impact into 50 subintervals

x = v_0*np.cos(theta0_rad) * t  # x coordinates over time
y = -g * (t**2)/2 + v_0*np.sin(theta0_rad)*t  #y coordinates over time

# Generate figure
fig, ax = plt.subplots(1,1)
ax.axis([np.min(x), np.max(x), np.min(y), np.max(y) + (0.05 * np.max(y))])
plt.xlabel("X-Position [m]")
plt.ylabel("Y-Position [m]")

# Enable interactive mode for plotting
plt.ion()
#ax.plot(x,y)   #include this if you want to see the parabola on your plot
# Loop over, and plot, each calculated projectile point
for i in range(np.size(x)):
      if i == 0:
          lines = ax.plot(x[i],y[i], 'ko', markersize = 10)
      else:
          lines[0].set_xdata(x[i])
          lines[0].set_ydata(y[i])
      plt.draw()
      plt.pause(0.05)
 

