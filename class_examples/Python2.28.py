# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 11:27:43 2024

@author: mwelz
"""

x = 764364

#absolute value using an if statement

if x < 0:
    x = -x

fav_animal = input("What's your favorite animal? ")


#printing different messages depending on dog favorability
#uses an if-else setup
if fav_animal == "dog" or fav_animal == "Dog":
    print("woof!")
else:
    print("I don't dogs like either!")
    
#printing if a number is even or odd
# x % 2 is remainder when dividng by 2
if x % 2 == 0:
    print(f"{x} is even")
else:
    print(f"{x} is odd")

#determine letter grade based on number grade
#turn into a function as well
#using if - elif and optional else setup
def return_grade(num_grade):
    if num_grade >= 90:
        print("A")
    elif num_grade >= 80:
        print("B")
    elif num_grade >= 70:
        print("C")
    elif num_grade >= 60:
        print("D")
    else:
        print("F")

return_grade(98)

# returns the nth fibonacci number
#recursion example
def nth_Fib(n):
    #base case tells the function when to stop calling itself
    if n == 1 or n == 2:
        return 1
    else:
        result = nth_Fib(n-1) + nth_Fib(n-2) #recursion relation
        return result

print(nth_Fib(38))


