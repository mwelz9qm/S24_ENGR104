"""
Calculates time, gallons of gas used, and cost of gasoline for a trip
"""

distance = float(input("Input trip distance (miles): "))
'''
mpg = float(input("Input your car's average milage (miles/gallon): "))
speed = float(input("Input your average speed on the trip (miles/hour): "))
costPerGallon = float(input("Input the average cost of gasoline (dollars/gallon): "))
'''

mpg = 30.             #car milage
speed = 60.0            #average speed
costPerGallon = 2.85    #price of gasoline


time = distance/speed
gallons = distance/mpg
cost = gallons*costPerGallon

print("\nDuration of the trip = {0:0.1f} hours".format(time))
print("Gasoline used = {0:0.1f} gallons (@ {1:0.0f} mpg)".format(gallons,mpg))
print("Cost of gasoline = ${0:0.2f} (@ ${1:0.2f}/gallon)".format(cost,costPerGallon))