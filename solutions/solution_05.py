"""
Assignment #5 Solution
ENGR 104, Fundamental Of Engineering Computing
"""

import numpy as np

# ============================================================================
# Problem 14.1 (4 Points)
print('\n----- Problem 14.1 (4 Points)-----')
def Sq_cyl(h,w,l):
    Sq_cyl_vol  = h * w * l
    print('The Square-Cylinder with h=%.2f, w=%.2f and l=%.2f has a volume of %.2f [L^3]' %              (w,h,l,Sq_cyl_vol))
Sq_cyl(2,3,5)

# Problem 14.2 (4 Points)
print('\n----- Problem 14.2 (4 Points)-----')
def Circ_cyl(r,h):
    Circ_cyl_vol = np.pi * r**2 * h
    print('The volume of circular cylinder of radius=%.1f and height=%.1f is %.2f [L^3]' %(r,h,Circ_cyl_vol))
Circ_cyl(2.5,5)

# Problem 14.3 (4 Points)
print('\n----- Problem 14.3 (4 Points)-----')
CCA = lambda r,h: np.pi * r**2 * h
CCA1 = CCA(2.5,5)
print('The circular cylinder area calculated as a anonymous/lambda function is %.2f' %CCA1)

# Problem 14.4 (4 Points)
print('\n----- Problem 14.4 (4 Points)-----')
def Cyl(r,h):
    CC_vol = np.pi * r**2 * h
    CC_surfArea = 2 * np.pi * r**2 + h * 2 * r
    return CC_vol,CC_surfArea

vol1,surf1 = Cyl(2.5,5)
print(f'The volume and surfacer areaes of the cylinder are {vol1} and {surf1}, respectively.')


# ============================================================================
# Problem 15.1 (7 Points)
print('\n----- Problem 15.1 (7 Points) -----')
def func(h_0,v_0,t):
    #h_0=initial height (m)
    #v_0=initial velocity (m/s)
    #t=time of flight (s)
    g = 9.81    # gravitational acceleration (m/s^2)
    h = round(h_0 + v_0*t - 0.5*g*t**2,2)
    v = round(v_0 - g*t,2)
    print(f"The height and the velocity of the object after {t} seconds is {h} (m) and {v} (m/s), respectively")
    
func(1.5,15,1.5)    #method 1
h1 = 15 #(m)
v1 = 35 #(m/s)
t1 = 3   #(s)
func(h1,v1,t1)      #method 2

# Problem 15.2 (7 Points)
print('\n----- Problem 15.2 (7 Points) -----')    
def threesFunction(rows,columns):
    """ Defines an array of the value 2 given a  number of rows and a number of                             columns
    """
    A =2 * np.ones((rows,columns))
    return A

Q15_2 = threesFunction(2,4)
print(f'The resulting array is\n {Q15_2}')
    




