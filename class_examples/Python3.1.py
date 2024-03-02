# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 11:29:32 2024

@author: mwelz
"""

def pass_or_not(grade):
    '''
    Parameters
    ----------
    grade : int/float
        numeric grade.
    Checks if a grade entered is valid and whether or not it's passing
    Returns
    -------
    None.
    '''
    if grade >=0 and grade <= 100: #checking grade is in range
        if grade >= 70:
            print("The grade is passing!")
        else:
            print("The grade isn't passing")
    else:
        print("The grade you entered is out of range.")

pass_or_not(90) #test a pass
pass_or_not(56) #test a fail
pass_or_not(-5) #testing a low out of range
pass_or_not(110) #testing a high out of range

c =14

print( c == 14)
print( c!=20)
print(c >30 or c < 0)
print(c > 10 and c % 2 == 0)
print(not c >10)

def root_classify():
    a = float(input("Enter the a coefficient of your quadratic: "))
    b = float(input("Enter the b coefficient of your quadratic: "))
    c = float(input("Enter the c coefficient of your quadratic: "))
    D = b**2 - 4*a*c
    if D < 0:
        print("Your quadratic has no roots.")
    elif D == 0:
        print("Your quadratic has one root.")
    else:
        print("Your quadratic has two roots.")


root_classify()
    




    