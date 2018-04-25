# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 11:49:30 2018

@author: jon_c
"""

#question 1
def fahrenheit_to_celsius(temp):
    out = (temp - 32)/180*100
    return out


#question2
def position_velocity(vinit, t):
    y = ((vinit*t)-0.5*9.81*t**2)
    y = round(y, 2)
    dy = (vinit - 9.81*t)
    dy = round(dy, 2)
    return y, dy


#question 3

def minutes_to_years_days(minutes): 
    years = (minutes//(365*24*60))
    days = (minutes % (365*24*60)) // (24*60)
    return years, days

minutes = int(input("How many minutes do you have?"))

years, days = minutes_to_years_days(minutes)
print (minutes, "minutes is approximately", years, "years and", days, "days")


#question 4
from math import sqrt

class Coordinate:
    x = 0
    y = 0

def area_of_triangle(p1, p2, p3):
    side1 = sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)
    side2 = sqrt((p2.x-p3.x)**2+(p2.y-p3.y)**2)
    side3 = sqrt((p3.x-p1.x)**2+(p3.y-p1.y)**2) 
    s = (side1 + side2 + side3)/2
    area = round(sqrt(s*(s - side1)*(s - side2)*(s- side3)), 1)
    return area

p1 = Coordinate()
p2 = Coordinate()
p3 = Coordinate()
p1.x = float(input("X-coordinate of the first point:"))    
p1.y = float(input("Y-coordinate of the first point:"))    
p2.x = float(input("X-coordinate of the second point:"))    
p2.y = float(input("Y-coordinate of the second point:"))    
p3.x = float(input("X-coordinate of the third point:"))    
p3.y = float(input("Y-coordinate of the third point:"))  

area = area_of_triangle(p1, p2, p3)
print ("The area of the triangle is", area)


#question 5
amt = float(input("Enter the monthly saving amount:"))
annualrate = float(input("Enter annual interest rate:"))
rate = annualrate
#((annualrate/12)+1)
def compound_value_sixth_month(amt, rate):
	balance = amt*((1+rate/12)**6 + (1+rate/12)**5 + (1+rate/12)**4 + (1+rate/12)**3 + (1+rate/12)**2 + (1+rate/12))
	return round(balance, 2)

balance = compound_value_sixth_month(amt, rate)
print ("After the sixth month you will have", balance)



#HWquestion1
def celsius_to_fahrenheit(temp):
    out = (temp * 1.8 +32)
    return out

#HWquestion2
def area_vol_cylinder(radius, length):
    import math
    area = (radius * radius * math.pi)
    volume = (area * length)
    return round(area, 2), round(volume, 2)
            

#HWquestion3
temp = float(input("What is the temperature outside in Fahrenheit?"))
speed = float(input("What is the wind speed in mph?"))

def wind_chill_temp(temp,speed):
    twc = 35.74 + (0.6215*temp) - (35.75*(speed**0.16)) + (0.4275*temp*(speed**0.16))
    return twc

twc = wind_chill_temp(temp,speed)
print(twc)


#HWquestion4
def bmi(weight,height):
    kilograms = weight*0.45359237
    meters = height*0.0254
    bodymassindex = kilograms/(meters**2)
    return bodymassindex



#HWquestion5
def investment_val(amt, rate, years):
    invest = amt * (1 + (rate/1200))**(years*12)
    return round(invest, 2)


