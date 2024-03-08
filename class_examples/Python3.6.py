# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 11:13:33 2024
While loops!
@author: mwelz
"""

#ask a user for test scores
scores = []

response = "Y"

while response.lower() == "y":
    score = float(input("Enter a test score: "))
    scores.append(score)
    response = input("Do you want to enter more scores? (Y/N) ")
    

print(f"The list of test scores {scores}.")

#turn the above into a function
def read_scores():
    '''
    a function that asks the user for an indeterminate number
    of test scores
    Returns
    -------
    None.

    '''
    
    scores = []

    response = "Y"

    while response.lower() == "y":
        score = float(input("Enter a test score: "))
        scores.append(score)
        response = input("Do you want to enter more scores? (Y/N) ")
        

    print(f"The list of test scores {scores}.")


read_scores()

#using a while loop to find all fibonacci numbers < 1000

x = 0
y = 1

while x<1000:
    print(x)
    x, y = y, x + y

#function to find n!

def factorial(n):
    '''

    Parameters
    ----------
    n : int
        nonnegative int we want the factorial of.
    Returns
    -------
    prod : int
        the factorial of n.
    '''
    prod =1 
    while n > 1:
        prod = prod*n
        n = n -1    
    return prod


print(f"5! is: {factorial(5)}")

#code to find smallest prime dividing a number

def find_prime(n):
    '''
    Parameters
    ----------
    n : int (positive)
        Searching for smallest prime dividing n.

    Returns
    -------
    i : int
        smallest prime dividing n.
    '''
    i = 2
    while (n % i != 0): #means n not divisble by i
        i = i + 1
    return i

print(find_prime(84798537875984587))