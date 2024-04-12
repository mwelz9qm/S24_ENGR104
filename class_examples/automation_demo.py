# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 11:16:28 2024

@author: mwelz
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

#instantiates a webdriver

browser = webdriver.Chrome()

#visit a webpage
browser.get("https://www.fortlewis.edu")

#finds the visit campus button by it's text and clicks it
buttonElem = browser.find_element(By.LINK_TEXT,"Visit Campus")
buttonElem.click()
time.sleep(5)
# navigates to google 

browser.get("https://www.google.com")

#find the search bar by name
search = browser.find_element(By.NAME, "q")

#types a search into the search bar
search.send_keys("Durango, CO Wiki")
time.sleep(2)

#hits return on the search
search.send_keys(Keys.RETURN)

#using directional keys
#just moving around the page physically

body = browser.find_element(By.TAG_NAME, 'body') #just gets us on the page
body.send_keys(Keys.DOWN)
body.send_keys(Keys.DOWN)
body.send_keys(Keys.DOWN)
body.send_keys(Keys.DOWN)
body.send_keys(Keys.DOWN)
body.send_keys(Keys.DOWN)
body.send_keys(Keys.UP)
body.send_keys(Keys.UP)
body.send_keys(Keys.UP)
body.send_keys(Keys.UP)
#goofing around with a loop that hits tab 20 times
# for i in range(20):
#     body.send_keys(Keys.TAB)
#     time.sleep(0.5)

#should find the first link on the search results by the tag h3
first_result = browser.find_element(By.TAG_NAME, 'h3')
first_result.click()

#gather the text from the wiki page by gathering all paragraphs
#that are tagged with 'p'
paragraphs = browser.find_elements(By.TAG_NAME, 'p')

#loops through and prints the paragraphs

for paragraph in paragraphs:
    print(paragraph.text)

# writes thes page text to an output file

with open('example.txt', 'w') as file:
    for paragraph in paragraphs:
        file.write(paragraph.text + "\n\n")


#this logs you into canvas

browser.get('https://courses.fortlewis.edu')

#username box, password box, and submit elements 
#are found below are by name and by id
#be sure to update with your credentials
userElem = browser.find_element(By.ID,'username')
userElem.send_keys('type username')
passwordElem = browser.find_element(By.ID,'password')
passwordElem.send_keys('type your password')
time.sleep(2)
linkElem = browser.find_element(By.NAME,'submit')
linkElem.click()