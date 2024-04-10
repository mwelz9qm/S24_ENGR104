# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:27:05 2024

@author: mattwelz
"""

#Looking at the object properties (data and methods) of numpy arrays

import numpy as np

a = np.array([[1,2,3],[4,5,6]])

print(a.size, a.shape, a.ndim)

print(a.mean(), a.max(),a.reshape((3,2)))



#our first homemade class examples


class Person:
    '''Person class consists of name, age, and a greeting'''
    def __init__(self, name, age):
        '''constructor'''
        self.name = name
        self.age = age
    
    def greeting(self):
        '''a basic greeting method'''
        print(f"Hi, my name is {self.name} and I'm {self.age} years old")
        
    def name_change(self,new_name):
        '''method to change the name of the person'''
        self.name = new_name
    
    def age_change(self, new_age):
        '''method to change the age of the person'''
        self.age = new_age

#instantiates Person objects
p1 = Person("Langston", 25)

p1.greeting()

print(p1.name)

p2 = Person("Shannon", 19)

p2.greeting()

p2.name_change("Lyla")
p2.age_change(23)
p2.greeting()

#build a new data type called resistor

class Resistor:
    '''a basic class to model a resistor'''
    def __init__(self, resistance):
        self.resistance = resistance
    
    def display_info(self):
        print(f"This resistor has resistance {self.resistance} Ohms.")

    def get_current(self, voltage):
        '''given a voltage, returns current through the resistor'''
        return voltage/self.resistance

#instantiate a resistor object
r1 = Resistor(50)
r1.display_info()
voltage = 9
current = r1.get_current(voltage)
print(f"The current through the resistor when the voltage is {voltage} volts, is {current} Amps.")



#create a class for product objects to be inherited by the book type
class Product:
    '''generic product class'''
    def __init__(self, name, price, sku):
        self.name = name
        self.price = price
        self.sku = sku
    
    def display_info(self):
        print(f"Name: {self.name}, Price: ${self.price}, SKU: {self.sku}")



#Book has ***inherited*** attributes from Product
class Book(Product):
    def __init__(self, name, price, sku, author, pages, pub_year, isbn):
        super().__init__(name,price,sku)  #calls the constructor from product base class
        self.author = author
        self.pages = pages
        self.pub_year = pub_year
        self.isbn = isbn
    
    def display_info(self):
        super().display_info()   #prints the product elements
        print(f"Author: {self.author}, Pages: {self.pages}, Year of Publication: {self.pub_year}, ISBN: {self.isbn}")
        
    def is_public_domain(self, current_year):
        return (current_year - self.pub_year) > 70
        

#instantiate a product object
product1 = Product("Black Hoodie", 35, 4738987437)
product1.display_info()

#instantiate a book object

book1 = Book("The Trial", 9.95, 798739478,"Franz Kafka", 160, 1925, 1612931030)

book1.display_info()
if book1.is_public_domain(2024):
    print(f"{book1.name} is in the public domain.")
else:
    print(f"{book1.name} is not in the public domain.")