"""
Assignment #4 Solution
ENGR 104, Fundamental Of Engineering Computing
"""

import math as m
import numpy as np
import scipy.linalg as slin

# ============================================================================
# Problem 11.1 (1 Points)
print('\n----- Problem 11.1 (1 Points) -----')
tpl = ([1,2,'3'],['apple','pineapple','pineapplepieeeeee'],[5,6,'7'])
print(tpl)
tpl[1][2]='pineapplepie'
print(tpl)
print('This works because a list inside the tuple is being modified, you would not be ablet to modify any individual element of the tuple, you would get an operation error!')

# Problem 11.2 (1 Points)
print('\n----- Problem 11.2 (1 Points) -----')
rivers = {'Colorado':'United States','Rhine':'Germany','Stikine':'Canada','Tsangpo':'Tibet','Pasqua':'Chile'}
print(rivers['Stikine'])

# Problem 11.3 (2 Points)
print('\n----- Problem 11.3 (2 Points) -----')
eng2spanishNums = {'one':'uno','two':'dos','three':'tres','four':'quattro','five':'cinco','six':'seis','seven':'siete','eight':'ocho','nine':'nueve','ten':'deiz','eleven':'once','twelve':'doce','thirteen':'trece','fourteen':'catorce','fifteen':'quince'}
print(eng2spanishNums['eight'])

# Problem 11.4 (1 Points)
print('\n----- Problem 11.4 (3 Points)-----')
individuals = {'Chaz':{'first':'Chaz','last':'Wilson','age':48,'location':'hesperus'},'Squirt':{'first':'Ziggy','last':'Welz','age':9,'location':'hesperus'},'Nate':{'first':'nathaniel','last':'Rigsby','age':41,'location':'Corvallis'},}
print(individuals['Nate']['location'])
print(individuals['Nate']['age'])
print('This dictionary is a nested dictionary because there are key value pairs for a singkle key!')

# ============================================================================
# Problem 12.1 (1 Points)
print('----- Problem 12.1 (1 Points) -----')
x = 3.4
y = 5.8
e = np.array([x/y,x+y,x*y,m.cos(x),y**2,x])
print(e)

# Problem 12.2 (1 Points)
print('\n----- Problem 12.4 (1 Points) -----')
s = np.array([1,3,5,7])
a = s*3
print(f'a = {a}')
b = s**2
print(f'b = {b}')
c = s/s
print(f"c = {c}")
d = 6*s/s
print(f"d = {d}")

# Problem 12.3 (2 Points)
print('\n----- Problem 12.3 (2 Points) -----')
sixTwoA = np.linspace(5,50,25)
sixTwoB = np.arange(5,51,1.875)
print(sixTwoA)
print(sixTwoB)
print('The linspace command is easier because the number of evenly spaced values was specified')

# Problem 12.4 (2 Points)
print('\n----- Problem 12.4 (2 Points) -----')
sixThreeA = np.linspace(3,42,14)
sixThreeB = np.arange(3,43,3)
print(sixThreeA)
print(sixThreeB)
print('The arange command is easier because the step size was specified')

# Problem 12.5 (2 Points)
print('\n----- Problem 12.5 (2 Points) -----')
D = np.vstack((np.ones((3,4),dtype=int),np.arange(8,0,-2)))
E = np.vstack((np.zeros((4,3),dtype=int),np.arange(8,5,-1)))
E = E.T
print(D)
print(E)

# Problem 12.6 (2 Points)
print('\n----- Problem 12.6 (2 Points) -----')
v0 = 275    #velocity (m/s)
angles = np.array([15,25,35,45,55,65,75]) #degrees
s = (v0**2)/9.81*np.sin(2*np.radians(angles))   #distances
print(s)
h = (v0**2*np.sin(np.radians(angles))**2)/(2*9.81)
print(h)

# Problem 12.7 (3 Points)
print('\n----- Problem 12.7 (2 Points) -----')
V = np.array([4000,3500,3000,2500,2000,1500,1000]) #sphere volumes in inches^3
r = np.cbrt((3*V)/(4*np.pi))     #sphere radius' calculated from volumes
S = 4*np.pi*r         #sphere surface areas calculated from volumes
sphere_data = np.round(np.vstack((r,V,S)).T,2)  #transpose and round to set precision
print(sphere_data)


# ============================================================================
# Problem 13.1 (4 Points)
print('\n----- Problem 13.1 (3 Points) -----')
mu = 0.38   #coefficient of friction
Theta1 = np.array([5,10,15,20,25,30,35]) #angle of pull in degrees
F1 = (70*mu)/(mu*np.sin(np.radians(Theta1))+np.cos(np.radians(Theta1)))
print(F1)
Theta2 = np.arange(5,35,0.01)
F2 = (70*mu)/(mu*np.sin(np.radians(Theta2))+np.cos(np.radians(Theta2)))
Fmin = F2.min()
loc_Fmin = F2.argmin()
Theta_min = Theta2[loc_Fmin]
print(f"The minimum force needed to move the bag of rice is {Fmin:.4} at an angle of {Theta_min:.4} degrees!")

# Problem 13.2 (2 Points)
print('\n----- Problem 13.2 (2 Points)-----')
A1 = np.array([[-2,5,7],[3,-6,2],[9,-3,8]])
b1 = np.array([-17.5,40.6,56.2])
S1a = slin.solve(A1,b1)
print(S1a)
S1b = slin.inv(A1) @ b1
print(S1b)
S1c = np.dot(slin.inv(A1),b1) #least preffered
print(S1c)

# Problem 13.3 (4 Points)
print('\n----- Problem 13.3 (4 Points) -----')
# Calculates the currents in a circuit
V1,V2,V3=28,36,42          # Voltages in the circuit
R1,R2,R3,R4,R5,R6,R7,R8=16,10,6,12,8,14,4,5        # Resistors in the circuit
# Coefficient Matrix
A2 = np.array([[-(R1+R3),R3,0,0],[R3,-(R2+R3+R4+R6),R4,R6],[0,R4,-(R4+R5+R7),R7],[0,R6,R7,-(R6+R7+R8)]])
# Constant Vector
b2 = [-V1,0,V2,-V3] 
# Solve
S2a = slin.solve(A2,b2)
print(S2a)
S2b = slin.inv(A2) @ b2
print(S2b)
print(f'The electrical current in each of the three loops of the circuit are {S2b[0]:.4} amps,{S2b[1]:.4} amps,{S2b[2]:.4} amps,respectively.')

# Problem 13.4 (4 Points)
print('\n----- Problem 13.4 (4 Points) -----')
# Coefficient matrix

A3 = np.array([[1,1,1,1,1,1],[25,40,60,70,32,0],[0,-1,1,0,0,0],[0,1,0,1,-10,0],[-1,1,1,0,0,0],[1,0,1,0,-4,-4]])
# constant vector
b3 = [100000,4897000,-11000,0,0,0]
# Solve
S3a = slin.solve(A3,b3)
print(S3a)
S3b = slin.inv(A3) @ b3
print(S3b)
print(f"The number of students in attandance was {S3b[0]:.7}!")
print(f"The number of alumni in attandance was {S3b[1]:.7}!")
print(f"The number of faculty in attandance was {S3b[2]:.7}!")
print(f"The number of public in attandance was {S3b[3]:.7}!")
print(f"The number of veterans in attandance was {S3b[4]:.7}!")
print(f"The number of guests in attandance was {S3b[5]:.7}!")





